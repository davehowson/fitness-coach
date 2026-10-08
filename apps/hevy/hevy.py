#!/usr/bin/env python3
"""Hevy adapter for fitness-coach. Stdlib only. Contract: apps/hevy/API.md.

Auth: HEVY_API_KEY env var (never written to disk). Private cache: my-data/hevy/ (gitignored).
Writes (publish-routine, create-exercise) are dry-run unless --apply is passed; Hevy has no delete.

  hevy.py check
  hevy.py sync-catalog
  hevy.py sync-history [--full]
  hevy.py summary [--weeks 12]
  hevy.py resolve "bench press"...
  hevy.py publish-routine plan.json [--apply] [--update]
  hevy.py create-exercise --title T --type weight_reps --equipment barbell --muscle chest [--other triceps] [--apply]
"""
import argparse, difflib, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE = "https://api.hevyapp.com"  # fixed: the api-key header must never go to another host
ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "my-data" / "hevy"  # gitignored; no override so data cannot land in a tracked path
CATALOG, HISTORY, SUMMARY = DATA / "catalog.json", DATA / "history.json", DATA / "summary.json"

TYPES = {"weight_reps", "reps_only", "bodyweight_reps", "bodyweight_assisted_reps", "duration",
         "weight_duration", "distance_duration", "short_distance_weight"}
EQUIPMENT = {"none", "barbell", "dumbbell", "kettlebell", "machine", "plate", "resistance_band", "suspension", "other"}
MUSCLES = {"abdominals", "shoulders", "biceps", "triceps", "forearms", "quadriceps", "hamstrings", "calves",
           "glutes", "abductors", "adductors", "lats", "upper_back", "traps", "lower_back", "chest", "cardio",
           "neck", "full_body", "other"}
SET_TYPES = {"warmup", "normal", "failure", "dropset"}
TIMED = {"duration", "weight_duration", "distance_duration"}


class HevyError(Exception):
    pass


def die(msg):
    sys.exit(f"error: {msg}")


def api(method, path, params=None, body=None):
    key = os.environ.get("HEVY_API_KEY")
    if not key:
        die("HEVY_API_KEY is not set (get one at https://hevy.com/settings?developer, Hevy Pro required)")
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    data = json.dumps(body).encode() if body is not None else None
    for attempt in range(5):
        req = urllib.request.Request(url, data=data, method=method,
                                     headers={"api-key": key, "Content-Type": "application/json", "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            text = e.read().decode(errors="replace")
            retryable = e.code == 429 or e.code >= 500
            # POST is not idempotent and Hevy cannot delete: never auto-retry a create after a 5xx.
            if retryable and attempt < 4 and (method != "POST" or e.code == 429):
                time.sleep(float(e.headers.get("Retry-After") or 2 ** attempt))
                continue
            hint = {401: " (bad api-key / not Pro?)", 403: " (account limit reached?)", 409: " (already exists)"}.get(e.code, "")
            raise HevyError(f"{method} {path} -> {e.code}{hint}: {text[:300]}")
        except urllib.error.URLError as e:
            if attempt < 4 and method == "GET":
                time.sleep(2 ** attempt)
                continue
            raise HevyError(f"{method} {path}: {e.reason}")


def paginate(path, key, page_size, params=None):
    page, out = 1, []
    while True:
        r = api("GET", path, {**(params or {}), "page": page, "pageSize": page_size})
        out += r.get(key, [])
        if page >= r.get("page_count", 1):
            return out
        page += 1


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1))


def load(path, what, hint):
    if not path.exists():
        die(f"no {what} cache at {path}; run `{hint}` first")
    return json.loads(path.read_text())


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


# ---------- sync ----------

def cmd_check(a):
    u = api("GET", "/v1/user/info")["data"]
    n = api("GET", "/v1/workouts/count")["workout_count"]
    print(f"ok: authenticated as {u.get('name')!r}; {n} workouts logged")


def cmd_sync_catalog(a):
    t = paginate("/v1/exercise_templates", "exercise_templates", 100)
    save(CATALOG, {"app": "hevy", "fetched_at": now(), "exercises": t})
    custom = sum(1 for x in t if x.get("is_custom"))
    print(f"catalog: {len(t)} exercises ({custom} custom) -> {CATALOG}")


def cmd_sync_history(a):
    store = json.loads(HISTORY.read_text()) if HISTORY.exists() else None
    if store and not a.full:
        since = store["synced_at"]
        started = now()
        events, page = [], 1
        while True:
            r = api("GET", "/v1/workouts/events", {"since": since, "page": page, "pageSize": 10})
            events += r.get("events", [])
            if page >= r.get("page_count", 1):
                break
            page += 1
        ws = store["workouts"]
        for e in reversed(events):  # API is newest-first; apply oldest-first so the latest event wins
            if e["type"] == "deleted":
                ws.pop(e["id"], None)
            else:
                ws[e["workout"]["id"]] = e["workout"]
        store["synced_at"] = started
        print(f"history: applied {len(events)} events")
    else:
        started = now()
        ws = {w["id"]: w for w in paginate("/v1/workouts", "workouts", 10)}
        store = {"app": "hevy", "synced_at": started, "workouts": ws}
        print("history: full pull")
    save(HISTORY, store)
    print(f"history: {len(store['workouts'])} workouts -> {HISTORY}")


# ---------- summary ----------

def e1rm(w, r):
    return w * (1 + r / 30) if w and r and 0 < r <= 12 else None


def cmd_summary(a):
    cat = {t["id"]: t for t in load(CATALOG, "catalog", "hevy.py sync-catalog")["exercises"]}
    hist = load(HISTORY, "history", "hevy.py sync-history")
    cutoff = datetime.now(timezone.utc) - timedelta(weeks=a.weeks)
    ws = sorted((w for w in hist["workouts"].values() if parse_ts(w["start_time"]) >= cutoff),
                key=lambda w: w["start_time"])
    ex, weekly = {}, defaultdict(float)
    for w in ws:
        day = w["start_time"][:10]
        for e in w["exercises"]:
            t = cat.get(e["exercise_template_id"], {})
            row = ex.setdefault(e["exercise_template_id"], {
                "title": e["title"], "type": t.get("type"), "primary": t.get("primary_muscle_group"),
                "sessions": 0, "hard_sets": 0, "last_date": None, "last_top_set": None, "best_e1rm_kg": None})
            hard = [s for s in e["sets"] if s["type"] != "warmup"]
            if not hard:
                continue
            row["sessions"] += 1
            row["hard_sets"] += len(hard)
            row["last_date"] = day
            top = max(hard, key=lambda s: (s.get("weight_kg") or 0, s.get("reps") or 0, s.get("duration_seconds") or 0))
            row["last_top_set"] = {k: top.get(k) for k in ("weight_kg", "reps", "duration_seconds", "distance_meters", "rpe")}
            for s in hard:
                v = e1rm(s.get("weight_kg"), s.get("reps"))
                if v and (row["best_e1rm_kg"] is None or v > row["best_e1rm_kg"]):
                    row["best_e1rm_kg"] = round(v, 1)
            if t.get("primary_muscle_group"):
                weekly[t["primary_muscle_group"]] += len(hard)
            for m in t.get("secondary_muscle_groups") or []:
                weekly[m] += 0.5 * len(hard)
    wks = max(a.weeks, 1)
    days = sorted({w["start_time"][:10] for w in ws})
    durs = [(parse_ts(w["end_time"]) - parse_ts(w["start_time"])).total_seconds() / 60 for w in ws if w.get("end_time")]
    out = {
        "app": "hevy", "generated_at": now(), "window_weeks": a.weeks,
        "sessions": len(ws), "sessions_per_week": round(len(ws) / wks, 1),
        "avg_session_minutes": round(sum(durs) / len(durs)) if durs else None,
        "first_session": days[0] if days else None, "last_session": days[-1] if days else None,
        "weekly_hard_sets_by_muscle": {m: round(v / wks, 1) for m, v in sorted(weekly.items(), key=lambda kv: -kv[1])},
        "exercises": sorted(ex.values(), key=lambda r: -r["hard_sets"]),
    }
    save(SUMMARY, out)
    print(f"{out['sessions']} sessions in {a.weeks}w ({out['sessions_per_week']}/wk, ~{out['avg_session_minutes']} min)")
    print("weekly hard sets (secondary = 0.5):", out["weekly_hard_sets_by_muscle"])
    for r in out["exercises"][:15]:
        print(f"  {r['title']}: {r['hard_sets']} sets/{r['sessions']} sess, last {r['last_date']} top {r['last_top_set']}, e1RM {r['best_e1rm_kg']}")
    print(f"-> {SUMMARY}")


# ---------- resolve ----------

def norm(s):
    return re.sub(r"[^a-z0-9 ]", " ", s.lower()).split()


def candidates(query, cat, n=5):
    q = set(norm(query))
    scored = []
    for t in cat:
        tt = set(norm(t["title"]))
        overlap = len(q & tt) / max(len(q | tt), 1)
        ratio = difflib.SequenceMatcher(None, query.lower(), t["title"].lower()).ratio()
        scored.append((max(overlap, ratio) + (0.02 if t.get("is_custom") else 0), t))
    return [t for s, t in sorted(scored, key=lambda x: -x[0])[:n] if s > 0.3]


def find_exact(name, cat):
    hits = [t for t in cat if t["title"].lower() == name.lower()]
    return hits[0] if len(hits) == 1 else None


def cmd_resolve(a):
    cat = load(CATALOG, "catalog", "hevy.py sync-catalog")["exercises"]
    for q in a.query:
        print(f"{q!r}:")
        for t in candidates(q, cat, 6) or []:
            print(f"  {t['id']}  {t['title']}  [{t['type']}; {t['primary_muscle_group']}{'; custom' if t['is_custom'] else ''}]")


# ---------- publish ----------

def build_sets(sets, ttype, where):
    out = []
    for i, s in enumerate(sets):
        st = s.get("type", "normal")
        if st not in SET_TYPES:
            die(f"{where} set {i}: type {st!r} not in {sorted(SET_TYPES)}")
        reps, rr = s.get("reps"), None
        if isinstance(reps, list):
            if len(reps) != 2 or reps[0] > reps[1]:
                die(f"{where} set {i}: reps range must be [low, high]")
            rr, reps = {"start": reps[0], "end": reps[1]}, None
        if ttype in TIMED:
            if not s.get("duration_seconds"):
                die(f"{where} set {i}: {ttype} exercise needs duration_seconds")
        elif reps is None and rr is None:
            die(f"{where} set {i}: needs reps (int or [low, high])")
        out.append({"type": st, "weight_kg": s.get("weight_kg"), "reps": reps, "rep_range": rr,
                    "distance_meters": s.get("distance_meters"), "duration_seconds": s.get("duration_seconds"),
                    "custom_metric": s.get("custom_metric")})
    return out


def build_routine(r, cat, folder_id):
    by_id = {t["id"]: t for t in cat}
    problems, exs = [], []
    for j, e in enumerate(r["exercises"]):
        label = e.get("exercise") or e.get("template_id")
        t = by_id.get(e.get("template_id")) if e.get("template_id") else find_exact(e.get("exercise", ""), cat)
        if not t:
            sug = "; ".join(f"{c['title']} ({c['id']})" for c in candidates(label or "", cat, 3))
            problems.append(f"  {r['title']} #{j + 1} {label!r} is not in the Hevy catalog. Closest: {sug or 'none'}")
            continue
        exs.append({"exercise_template_id": t["id"], "superset_id": e.get("superset_id"),
                    "rest_seconds": e.get("rest_seconds"), "notes": e.get("notes"),
                    "sets": build_sets(e["sets"], t["type"], f"{r['title']} / {t['title']}")})
    if problems:
        die("unresolvable exercises (pick catalog titles or create-exercise):\n" + "\n".join(problems))
    return {"title": r["title"], "folder_id": folder_id, "notes": r.get("notes"), "exercises": exs}


def cmd_publish(a):
    plan = json.loads(Path(a.plan).read_text())
    cat = load(CATALOG, "catalog", "hevy.py sync-catalog")["exercises"]
    existing = {x["title"].lower(): x for x in paginate("/v1/routines", "routines", 10)}
    folders = {f["title"].lower(): f for f in paginate("/v1/routine_folders", "routine_folders", 10)}
    fname, folder_id, new_folder = plan.get("folder"), None, False
    if fname:
        if fname.lower() in folders:
            folder_id = folders[fname.lower()]["id"]
        else:
            new_folder = True
    built = [build_routine(r, cat, folder_id) for r in plan["routines"]]  # validate everything before any write
    for b in built:
        dup = existing.get(b["title"].lower())
        if dup and not a.update:
            die(f"routine {b['title']!r} already exists (id {dup['id']}). Re-run with --update to replace it, or rename.")
        b["_action"] = f"PUT {dup['id']}" if dup else "POST"
    print(f"validated {len(built)} routine(s); folder: {fname or 'My Routines'}{' (will be created)' if new_folder else ''}")
    for b in built:
        print(f"  {b['_action']}: {b['title']} ({len(b['exercises'])} exercises)")
    if not a.apply:
        print(json.dumps({"routine": {k: v for k, v in built[0].items() if k != "_action"}}, indent=1)[:2500])
        print("\nDRY RUN. Nothing sent. Add --apply to write to Hevy (cannot be undone from the API).")
        return
    if new_folder:
        folder_id = api("POST", "/v1/routine_folders", body={"routine_folder": {"title": fname}}).get("routine_folder", {}).get("id")
    for b in built:
        action = b.pop("_action")
        if folder_id is not None:
            b["folder_id"] = folder_id
        if action == "POST":
            r = api("POST", "/v1/routines", body={"routine": b})
            rid = (r.get("routine") or r)
            rid = (rid[0] if isinstance(rid, list) and rid else rid).get("id")
        else:
            rid = action.split()[1]
            put = {k: v for k, v in b.items() if k != "folder_id"}  # PUT folder semantics are not documented
            api("PUT", f"/v1/routines/{rid}", body={"routine": put})
        print(f"  done: {b['title']} -> {rid}")


def cmd_create_exercise(a):
    for val, allowed, name in ((a.type, TYPES, "type"), (a.equipment, EQUIPMENT, "equipment"), (a.muscle, MUSCLES, "muscle")):
        if val not in allowed:
            die(f"--{name} {val!r} not in {sorted(allowed)}")
    bad = [m for m in a.other or [] if m not in MUSCLES]
    if bad:
        die(f"--other values not in muscle list: {bad}")
    cat = load(CATALOG, "catalog", "hevy.py sync-catalog")["exercises"]
    near = candidates(a.title, cat, 3)
    body = {"exercise": {"title": a.title, "exercise_type": a.type, "equipment_category": a.equipment,
                         "muscle_group": a.muscle, "other_muscles": a.other or []}}
    print(json.dumps(body, indent=1))
    if near:
        print("similar existing exercises (use one of these instead if it fits):")
        for t in near:
            print(f"  {t['id']}  {t['title']}")
    if find_exact(a.title, cat):
        die("an exercise with this exact title already exists")
    if not a.apply:
        print("DRY RUN. Custom exercises cannot be edited or deleted via the API. Add --apply to create.")
        return
    r = api("POST", "/v1/exercise_templates", body=body)
    print(f"created {r.get('id')}; refreshing catalog")
    cmd_sync_catalog(a)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    sp.add_parser("check").set_defaults(f=cmd_check)
    sp.add_parser("sync-catalog").set_defaults(f=cmd_sync_catalog)
    s = sp.add_parser("sync-history"); s.add_argument("--full", action="store_true"); s.set_defaults(f=cmd_sync_history)
    s = sp.add_parser("summary"); s.add_argument("--weeks", type=int, default=12); s.set_defaults(f=cmd_summary)
    s = sp.add_parser("resolve"); s.add_argument("query", nargs="+"); s.set_defaults(f=cmd_resolve)
    s = sp.add_parser("publish-routine"); s.add_argument("plan"); s.add_argument("--apply", action="store_true")
    s.add_argument("--update", action="store_true", help="PUT over routines whose title already exists"); s.set_defaults(f=cmd_publish)
    s = sp.add_parser("create-exercise")
    s.add_argument("--title", required=True); s.add_argument("--type", required=True)
    s.add_argument("--equipment", required=True); s.add_argument("--muscle", required=True)
    s.add_argument("--other", nargs="*"); s.add_argument("--apply", action="store_true"); s.set_defaults(f=cmd_create_exercise)
    a = p.parse_args()
    try:
        a.f(a)
    except HevyError as e:
        die(e)


if __name__ == "__main__":
    main()
