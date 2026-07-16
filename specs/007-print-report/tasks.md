# Tasks: Print a Report

**Input**: Design documents from `/specs/007-print-report/`
**Prerequisites**: plan.md, spec.md, quickstart.md

**Tests**: Not requested for this feature (no test framework introduced yet,
per the constitution's Course Constraints — correctness is verified via
`bootdev run` and manual output comparison).

## Phase 1: Setup

- [X] T001 Verify `main.py` currently prints the word count and sorted character list as two separate `print()` calls (from feature 006)

## Phase 2: Foundational

*None — this feature only adds one function to the existing `main.py` and updates `main()`.*

## Phase 3: User Story 1 - See one cohesive, formatted analysis report (Priority: P1)

**Goal**: Running the program prints the complete, exactly-formatted report
in one call, replacing the two separate print statements.

**Independent Test**: Run `python3 main.py` from the project root and diff
the output against specs/007-print-report/quickstart.md's expected block.

- [X] T002 [US1] In `main.py`, add `print_report(book_path, num_words, sorted_char_list)` printing the opening header (`============ BOOKBOT ============`), the book line (`Analyzing book found at {book_path}...`), the word-count section (`---------- Word Count ----------` then `Found {num_words} total words`), and the character-count section header (`--------- Character Count -------`)
- [X] T003 [US1] In `print_report`, loop over `sorted_char_list`, and for each `(char, count)` where `char.isalpha()` is true, print `{char}: {count}`
- [X] T004 [US1] In `print_report`, print the closing line (`============= END ===============`) after the character-count loop
- [X] T005 [US1] In `main.py`, replace the two existing `print()` calls in `main()` with a single call to `print_report("books/frankenstein.txt", num_words, sorted_chars)`
- [X] T006 [US1] Run `python3 main.py` and diff the output against specs/007-print-report/quickstart.md's expected block, confirming an exact match
- [X] T007 [US1] Submit the lesson via `bootdev run <lesson-id> -s`

**Checkpoint**: User Story 1 is complete and independently testable — this is
also the full MVP for this feature.

## Dependencies & Execution Order

- T001 → T002 → T003 → T004 → T005 → T006 → T007 (strictly sequential; one file, single story, no parallelism)

## Parallel Execution Examples

*None — one story, all changes land in `main.py` in sequence.*

## Implementation Strategy

MVP = User Story 1 = the entire feature. There is no phased rollout beyond it.
