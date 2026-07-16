# Tasks: Count Words

**Input**: Design documents from `/specs/003-count-words/`
**Prerequisites**: plan.md, spec.md, quickstart.md

**Tests**: Not requested for this feature (no test framework introduced yet,
per the constitution's Course Constraints — correctness is verified via
`bootdev run` and manual execution).

## Phase 1: Setup

- [X] T001 Verify `main.py` currently has `get_book_text(path)` and `main()` printing the raw book text (from feature 002)

## Phase 2: Foundational

*None — this feature only adds one function and modifies `main()` in the existing `main.py`.*

## Phase 3: User Story 1 - See the book's total word count (Priority: P1)

**Goal**: Running the program prints exactly one line,
`Found {num_words} total words`, with the correct count, and no raw book
text.

**Independent Test**: Run `python3 main.py` from the project root and
confirm the console shows only the word-count line.

- [X] T002 [US1] In `main.py`, add `get_num_words(text)` returning `len(text.split())`
- [X] T003 [US1] In `main.py`, update `main()` to compute `num_words = get_num_words(text)` and `print(f"Found {num_words} total words")`, removing the raw-text `print(text)`
- [X] T004 [US1] Run `python3 main.py` and confirm the output is exactly one line matching `Found {num_words} total words` per specs/003-count-words/quickstart.md
- [X] T005 [US1] Submit the lesson via `bootdev run <lesson-id> -s`

**Checkpoint**: User Story 1 is complete and independently testable — this is
also the full MVP for this feature.

## Dependencies & Execution Order

- T001 → T002 → T003 → T004 → T005 (strictly sequential; single file, single story, no parallelism)

## Parallel Execution Examples

*None — one file, one story. Nothing to parallelize.*

## Implementation Strategy

MVP = User Story 1 = the entire feature. There is no phased rollout beyond it.
