# Tasks: CLI Arguments

**Input**: Design documents from `/specs/008-cli-arguments/`
**Prerequisites**: plan.md, spec.md, quickstart.md

**Tests**: Not requested for this feature (no test framework introduced yet,
per the constitution's Course Constraints — correctness is verified via
`bootdev run` and manual runs against all three book files).

## Phase 1: Setup

- [X] T001 Verify `books/frankenstein.txt`, `books/mobydick.txt`, and `books/prideandprejudice.txt` all exist at the project root

## Phase 2: Foundational

- [X] T002 In `main.py`, add `import sys` at the top of the file

**Checkpoint**: `sys` is available; both user stories build on this import.

## Phase 3: User Story 1 - Analyze any book by passing its path on the command line (Priority: P1)

**Goal**: Running `python3 main.py <path>` analyzes the book at `<path>` and
prints its report, working correctly for all three sample books.

**Independent Test**: Run the program against each of the three book files
and confirm each produces a correct, distinct report.

- [X] T003 [US1] In `main.py`, update `main()` to use `sys.argv[1]` as `book_path` instead of the hardcoded `"books/frankenstein.txt"`
- [X] T004 [US1] Run `python3 main.py books/frankenstein.txt`, `python3 main.py books/mobydick.txt`, and `python3 main.py books/prideandprejudice.txt`, confirming each prints a correct report naming that book's path, per specs/008-cli-arguments/quickstart.md

**Checkpoint**: User Story 1 is independently testable and complete.

## Phase 4: User Story 2 - Get a helpful message when no book path is given (Priority: P2)

**Goal**: Running the program with no arguments prints the exact usage
message and exits with a non-zero status, with no report output.

**Independent Test**: Run the program with no arguments and confirm the
usage message and exit behavior.

- [X] T005 [US2] In `main.py`, at the top of `main()`, add a check: if `len(sys.argv) < 2`, print `Usage: python3 main.py <path_to_book>` and call `sys.exit(1)` before any report logic runs
- [X] T006 [US2] Run `python3 main.py` with no arguments and confirm it prints exactly the usage message, exits non-zero, and produces no report output, per specs/008-cli-arguments/quickstart.md

**Checkpoint**: User Story 2 is independently testable and complete.

## Phase 5: Polish

- [X] T007 Submit the lesson via `bootdev run <lesson-id> -s`

## Dependencies & Execution Order

- T001 → T002 → T003 → T004 → T005 → T006 → T007 (sequential; US2's guard is
  added after US1's argument usage to avoid re-testing T004 with a
  half-finished `main()`, though the two checks are logically independent
  within `main()`)

## Parallel Execution Examples

*None — all changes land in the same small `main()` function.*

## Implementation Strategy

MVP = User Story 1 (analyze a book by path). User Story 2 (usage message) is
a fast-follow that completes the feature per the lesson's requirements.
