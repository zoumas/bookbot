# Tasks: Refactor Stats Module

**Input**: Design documents from `/specs/004-refactor-stats-module/`
**Prerequisites**: plan.md, spec.md, quickstart.md

**Tests**: Not requested for this feature (no test framework introduced yet,
per the constitution's Course Constraints — correctness is verified via
`bootdev run` and manual output comparison).

## Phase 1: Setup

- [X] T001 Run `python3 main.py` and record the current output (`Found 75767 total words`) as the pre-refactor baseline

## Phase 2: Foundational

*None — this feature only relocates one existing function; no new shared infrastructure.*

## Phase 3: User Story 1 - Program behaves identically after the split (Priority: P1)

**Goal**: `get_num_words` lives in a new `stats.py` module, `main.py`
imports it explicitly, and program output is unchanged.

**Independent Test**: Run `python3 main.py` after the refactor and confirm
the output exactly matches the T001 baseline.

- [X] T002 [US1] Create `stats.py` at the repository root containing `get_num_words(text)` moved verbatim from `main.py`
- [X] T003 [US1] In `main.py`, remove the `get_num_words` definition and add `from stats import get_num_words` at the top of the file
- [X] T004 [US1] Run `python3 main.py` and confirm the output exactly matches the T001 baseline per specs/004-refactor-stats-module/quickstart.md
- [X] T005 [US1] Confirm `get_num_words` is defined only in `stats.py` (e.g. `grep -n "def get_num_words" *.py` shows exactly one match)
- [X] T006 [US1] Submit the lesson via `bootdev run <lesson-id> -s`

**Checkpoint**: User Story 1 is complete and independently testable — this is
also the full MVP for this feature.

## Dependencies & Execution Order

- T001 → T002 → T003 → T004 → T005 → T006 (strictly sequential; two files, single story, no parallelism)

## Parallel Execution Examples

*None — the move and the import update touch a shared contract (the function
name/signature) and must land together before verifying.

## Implementation Strategy

MVP = User Story 1 = the entire feature. There is no phased rollout beyond it.
