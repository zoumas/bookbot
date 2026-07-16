# Tasks: Count Characters

**Input**: Design documents from `/specs/005-count-characters/`
**Prerequisites**: plan.md, spec.md, quickstart.md

**Tests**: Not requested for this feature (no test framework introduced yet,
per the constitution's Course Constraints — correctness is verified via
`bootdev run` and manual execution).

## Phase 1: Setup

- [X] T001 Verify `stats.py` currently has `get_num_words(text)` and `main.py` imports it and prints the word count (from feature 004)

## Phase 2: Foundational

*None — this feature only adds one function to the existing `stats.py` and updates `main()`.*

## Phase 3: User Story 1 - See character frequency counts for the book (Priority: P1)

**Goal**: Running the program prints the word-count line followed by a
case-insensitive character-frequency dictionary for the book text.

**Independent Test**: Run `python3 main.py` from the project root and
confirm both lines of output appear, with the character mapping correctly
tallying letters case-insensitively.

- [X] T002 [US1] In `stats.py`, add `get_num_chars(text) -> dict[str, int]` that lowercases `text` and tallies each character into a dict
- [X] T003 [US1] In `main.py`, import `get_num_chars` from `stats` alongside the existing `get_num_words` import
- [X] T004 [US1] In `main.py`, update `main()` to call `get_num_chars(text)`, store the result, and print it after the existing word-count line
- [X] T005 [US1] Run `python3 main.py` and confirm the output shows the word-count line followed by the character mapping, with no split uppercase/lowercase keys, per specs/005-count-characters/quickstart.md
- [X] T006 [US1] Submit the lesson via `bootdev run <lesson-id> -s`

**Checkpoint**: User Story 1 is complete and independently testable — this is
also the full MVP for this feature.

## Dependencies & Execution Order

- T001 → T002 → T003 → T004 → T005 → T006 (strictly sequential; two files, single story, no parallelism)

## Parallel Execution Examples

*None — one story, tightly coupled changes across two files.*

## Implementation Strategy

MVP = User Story 1 = the entire feature. There is no phased rollout beyond it.
