# Tasks: Read Book File

**Input**: Design documents from `/specs/002-read-book-file/`
**Prerequisites**: plan.md, spec.md, quickstart.md

**Tests**: Not requested for this feature (no test framework introduced yet,
per the constitution's Course Constraints — correctness is verified via
`bootdev run` and manual execution).

## Phase 1: Setup

- [X] T001 Verify `books/frankenstein.txt` exists at the project root (from the prior "Book Data" lesson)

## Phase 2: Foundational

*None — this feature only modifies the existing `main.py` from feature 001; no new shared infrastructure.*

## Phase 3: User Story 1 - Read and display a book's full text (Priority: P1)

**Goal**: Running the program prints the complete, unmodified contents of
`books/frankenstein.txt` to the console.

**Independent Test**: Run `python3 main.py` from the project root and confirm
the console output is the book's entire text.

- [X] T002 [US1] In `main.py`, add `get_book_text(path)` that opens `path` with a `with` block and returns `f.read()`
- [X] T003 [US1] In `main.py`, replace the body of `main()` with a call to `get_book_text("books/frankenstein.txt")` and `print()` the result, removing the old `print("greetings boots")`
- [X] T004 [US1] Run `python3 main.py` and confirm the output matches `books/frankenstein.txt` exactly (e.g. compare against `cat books/frankenstein.txt`) per specs/002-read-book-file/quickstart.md
- [X] T005 [US1] Submit the lesson via `bootdev run <lesson-id> -s`

**Checkpoint**: User Story 1 is complete and independently testable — this is
also the full MVP for this feature.

## Dependencies & Execution Order

- T001 → T002 → T003 → T004 → T005 (strictly sequential; single file, single story, no parallelism)

## Parallel Execution Examples

*None — one file, one story. Nothing to parallelize.*

## Implementation Strategy

MVP = User Story 1 = the entire feature. There is no phased rollout beyond it.
