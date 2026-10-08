# Hevy API contract (as relevant to this repo)

> Source: Hevy's public OpenAPI 3.0 spec ("Hevy API Docs"), read from the `openapi-spec.json` shipped in
> [chrisdoc/hevy-mcp](https://github.com/chrisdoc/hevy-mcp), plus third-party wrappers
> ([ewright3/hevy-py](https://github.com/ewright3/hevy-py)). The official rendered docs at
> <https://api.hevyapp.com/docs/> could not be reached from the research sandbox, so anything marked
> **UNVERIFIED** is inferred. Hevy states it makes no stability guarantees; re-check against the live docs
> if a call starts failing.

## Access

| Item | Value |
|---|---|
| Base URL | `https://api.hevyapp.com` |
| Auth | `api-key: <uuid>` request header (not Bearer). Key from <https://hevy.com/settings?developer> |
| Plan | Hevy **Pro** only |
| Units | Weight is always **kg** (`weight_kg`), distance in **meters**, time in **seconds**, even if the app shows lbs |
| Rate limits | Not documented. **UNVERIFIED**; the client backs off on 429/5xx |
| Deletes | **None exist** on any resource. Templates cannot be edited or deleted either. Creates are permanent and retries create duplicates |

## Endpoints

| Method + path | Purpose | Paging |
|---|---|---|
| `GET /v1/user/info` | Account id/name/url (auth check) | – |
| `GET /v1/exercise_templates` | **Exercise catalog**: built-in + the user's custom exercises | `page`, `pageSize` **max 100** |
| `GET /v1/exercise_templates/{id}` | One template | – |
| `POST /v1/exercise_templates` | Create a custom exercise (403 when the account's custom-exercise limit is hit) | – |
| `GET /v1/routines` | List routines | `pageSize` **max 10** |
| `POST /v1/routines` | Create routine (403 when the routine limit is hit) | – |
| `GET/PUT /v1/routines/{id}` | Read / replace a routine | – |
| `GET/POST /v1/routine_folders`, `GET /v1/routine_folders/{id}` | Folders (ids are **integers**; new folder is inserted at index 0) | `pageSize` max 10 **UNVERIFIED** |
| `GET /v1/workouts` | **History**: logged workouts | `pageSize` **max 10**, 5 default. No date filter |
| `GET /v1/workouts/count` | Total logged workouts | – |
| `GET /v1/workouts/events?since=ISO` | Updated/deleted workouts since a timestamp, newest first. Built for incremental sync | `pageSize` max 10 **UNVERIFIED** |
| `GET /v1/workouts/{id}` · `POST /v1/workouts` · `PUT /v1/workouts/{id}` | Read / log / replace a workout | – |
| `GET /v1/exercise_history/{templateId}?start_date&end_date` | Every logged set for one exercise (ISO 8601 filters) | none |
| `GET/POST/PUT /v1/body_measurements[/{date}]` | Body weight, circumferences. POST 409 if date exists; PUT nulls omitted fields | `pageSize` default 10 |

List responses are `{ page, page_count, <items> }` where `<items>` is `workouts`, `routines`, `exercise_templates`,
`routine_folders` or `events`. Loop until `page >= page_count`. An oversized `pageSize` returns a bare 400.

## What a routine can reference (the compatibility constraint)

A routine exercise is **only** `exercise_template_id` (string such as `"05293BCA"`) plus sets. There is no
free-text exercise name. So every exercise a plan uses must be an existing template, built-in or custom.
The only way to introduce a new one is `POST /v1/exercise_templates`, which is permanent.

### ExerciseTemplate (read)
```
id, title, type, primary_muscle_group, secondary_muscle_groups[], is_custom
```
There is **no equipment field** on read; equipment is only encoded in the title, e.g. `Bench Press (Barbell)`,
`Lat Pulldown (Cable)`, `Squat (Smith Machine)`. Matching must therefore use titles.

### Custom exercise (create)
```json
{ "exercise": { "title": "…", "exercise_type": "weight_reps",
  "equipment_category": "barbell", "muscle_group": "chest", "other_muscles": ["triceps"] } }
```
Response: `{ "id": "…" }`.

| Enum | Values |
|---|---|
| `exercise_type` | `weight_reps` `reps_only` `bodyweight_reps` `bodyweight_assisted_reps` `duration` `weight_duration` `distance_duration` `short_distance_weight` |
| `equipment_category` | `none` `barbell` `dumbbell` `kettlebell` `machine` `plate` `resistance_band` `suspension` `other` |
| `muscle_group` | `abdominals` `shoulders` `biceps` `triceps` `forearms` `quadriceps` `hamstrings` `calves` `glutes` `abductors` `adductors` `lats` `upper_back` `traps` `lower_back` `chest` `cardio` `neck` `full_body` `other` |

The template `type` decides which set fields are meaningful: `weight_reps` → `weight_kg`+`reps`;
`reps_only`/`bodyweight_reps` → `reps`; `duration` → `duration_seconds`; `distance_duration` → both; etc.

### Create routine
```json
{ "routine": { "title": "Upper A", "folder_id": null, "notes": "…",
  "exercises": [ { "exercise_template_id": "05293BCA", "superset_id": null,
    "rest_seconds": 120, "notes": "…",
    "sets": [ { "type": "normal", "weight_kg": null, "reps": null,
                "rep_range": { "start": 6, "end": 8 },
                "distance_meters": null, "duration_seconds": null, "custom_metric": null } ] } ] } }
```
`type` ∈ `warmup | normal | failure | dropset`. `folder_id: null` puts it in "My Routines".
`rep_range` exists on routine sets only (not on logged workout sets). Routine reads return the same shape
plus `index`, `title`, `supersets_id`.

### Workout (history) as read
```
Workout { id, title, routine_id, description, start_time, end_time, updated_at, created_at,
  exercises[ { index, title, notes, exercise_template_id, supersets_id,
    sets[ { index, type, weight_kg, reps, distance_meters, duration_seconds, rpe, custom_metric } ] } ] }
```
`rpe` ∈ 6, 7, 7.5, 8, 8.5, 9, 9.5, 10 or null (only present if the user logs it).

## Consequences for this repo

1. **Catalog first.** Fetch all templates once (`ceil(n/100)` calls), cache locally, and make the coach pick
   exercises only from it. Custom exercises appear automatically (`is_custom: true`).
2. **The catalog and history are personal data** (custom exercise names, training log). They live in
   gitignored `my-data/hevy/`, never in tracked files.
3. **History is slow to pull**: 10 workouts per call and no date filter. Do one full pull, then use
   `/workouts/events?since=` for incremental refresh.
4. **No undo.** Publishing defaults to dry-run, checks existing routine titles first, and uses `PUT` to revise
   a routine instead of creating a second copy.
5. **Library names ≠ Hevy names.** The wiki says "back squat"; Hevy says `Squat (Barbell)`. A resolve step maps
   one to the other; if nothing fits, pick another exercise from the same pattern before creating a custom one.
