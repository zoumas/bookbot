# Tasks: Organize Data

**Input**: Design documents from `/specs/006-organize-data/`
**Prerequisites**: plan.md, spec.md, quickstart.md

**Tests**: Not requested for this feature (no test framework introduced yet,
per the constitution's Course Constraints — correctness is verified via
`bootdev run` and manual execution).

## Phase 1: Setup

- [X] T001 Verify `stats.py` currently has `get_num_words` and `get_num_chars`, and `main.py` prints the word count and raw character dict (from feature 005)

## Phase 2: Foundational

*None — this feature only adds two functions to the existing `stats.py` and updates `main()`.*

## Phase 3: User Story 1 - See characters ranked from most to least frequent (Priority: P1)

**Goal**: Running the program prints the word-count line followed by a list
of `(character, count)` pairs ordered from most to least frequent, with the
raw dict no longer printed.

**Independent Test**: Run `python3 main.py` from the project root and
confirm the printed list's counts are strictly non-increasing.

- [X] T002 [US1] In `stats.py`, add `sort_on(pair)` returning `pair[1]`
- [X] T003 [US1] In `stats.py`, add `chars_dict_to_sorted_list(char_dict)` that builds a `(char, count)` tuple list from `char_dict` and returns `sorted(list, key=sort_on, reverse=True)`
- [X] T004 [US1] In `main.py`, import `chars_dict_to_sorted_list` from `stats` alongside the existing imports
- [X] T005 [US1] In `main.py`, update `main()` to convert `num_chars` via `chars_dict_to_sorted_list` and print the resulting list instead of the raw dict
- [X] T006 [US1] Run `python3 main.py` and confirm the printed list is ordered from most to least frequent, with no raw dict printed, per specs/006-organize-data/quickstart.md
- [X] T007 [US1] Submit the lesson via `bootdev run <lesson-id> -s`

**Checkpoint**: User Story 1 is complete and independently testable — this is
also the full MVP for this feature.

## Dependencies & Execution Order

- T001 → T002 → T003 → T004 → T005 → T006 → T007 (strictly sequential; two files, single story, no parallelism)

## Parallel Execution Examples

*None — one story, tightly coupled changes across two files.*

## Implementation Strategy

MVP = User Story 1 = the entire feature. There is no phased rollout beyond it.
