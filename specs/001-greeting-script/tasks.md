# Tasks: Greeting Script

**Input**: Design documents from `/specs/001-greeting-script/`
**Prerequisites**: plan.md, spec.md, quickstart.md

**Tests**: Not requested for this feature (no test framework introduced yet, per
the constitution's Course Constraints — correctness is verified via
`bootdev run` and manual execution).

## Phase 1: Setup

- [X] T001 Verify `python3 --version` succeeds locally (no project files needed yet)

## Phase 2: Foundational

*None — this feature has no shared infrastructure beyond the single entry file created in User Story 1.*

## Phase 3: User Story 1 - Verify the Python environment runs (Priority: P1)

**Goal**: Running the project's entry point prints exactly `greetings boots`
to the console.

**Independent Test**: Run `python3 main.py` from the project root and confirm
the console shows exactly `greetings boots`.

- [X] T002 [US1] Create `main.py` at the repository root containing exactly one statement: `print("greetings boots")`
- [X] T003 [US1] Run `python3 main.py` and visually confirm the output is exactly `greetings boots` per specs/001-greeting-script/quickstart.md
- [X] T004 [US1] Submit the lesson via `bootdev run <lesson-id> -s`

**Checkpoint**: User Story 1 is complete and independently testable — this is
also the full MVP for this feature.

## Dependencies & Execution Order

- T001 → T002 → T003 → T004 (strictly sequential; single file, single story, no parallelism)

## Parallel Execution Examples

*None — one file, one story. Nothing to parallelize.*

## Implementation Strategy

MVP = User Story 1 = the entire feature. There is no phased rollout beyond it.
