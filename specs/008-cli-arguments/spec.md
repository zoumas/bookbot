# Feature Specification: CLI Arguments

**Feature Branch**: `008-cli-arguments`

**Created**: 2026-07-17

**Status**: Draft

**Input**: User description: "boot.dev 'Arguments' lesson (final lesson of the course): remove the hardcoded book path from main.py and instead take it from sys.argv[1]. If sys.argv has fewer than 2 entries, print 'Usage: python3 main.py <path_to_book>' and exit with status 1. Test against books/frankenstein.txt, books/mobydick.txt, and books/prideandprejudice.txt."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Analyze any book by passing its path on the command line (Priority: P1)

As a user of bookbot, I run the program with the path to a book file I want
analyzed, and I get that book's report — so bookbot becomes a reusable tool
rather than a script hardcoded to one book.

**Why this priority**: This is the final capability the course builds toward:
turning the hardcoded analysis script into an actual command-line tool. It's
required for the tool to be useful beyond the one sample book.

**Independent Test**: Run `python3 main.py <path>` for several different book
files and confirm each produces a correct report naming that book's path.

**Acceptance Scenarios**:

1. **Given** a valid path to a book file is provided as the program's first
   command-line argument, **When** the program runs, **Then** it analyzes
   that book and prints its report, with the report's book-path line showing
   the path that was passed in.
2. **Given** three different book files (`books/frankenstein.txt`,
   `books/mobydick.txt`, `books/prideandprejudice.txt`), **When** the
   program is run once per book with that book's path as the argument,
   **Then** each run prints a correct, distinct report for that specific
   book.

### User Story 2 - Get a helpful message when no book path is given (Priority: P2)

As a user of bookbot, if I run the program without telling it which book to
analyze, I get a clear usage message instead of a confusing crash, so I know
exactly how to use the tool correctly.

**Why this priority**: Secondary to actually analyzing books, but necessary
for the tool to be usable by someone other than its author — a cryptic
stack trace on missing input is a poor experience.

**Independent Test**: Run the program with no arguments and confirm the
usage message appears and the program exits with a failure status, without
attempting to analyze anything.

**Acceptance Scenarios**:

1. **Given** the program is run with no book path argument, **When** it
   starts, **Then** it prints exactly `Usage: python3 main.py
   <path_to_book>` and exits with a non-zero (failure) status, without
   printing any part of an analysis report.

### Edge Cases

- Extra arguments beyond the first are not addressed by the lesson and are
  simply ignored (only the first argument is used as the book path).
- A book path that doesn't exist as a file: out of scope for this feature —
  the lesson does not ask for a friendly error here; the program may fail
  with a standard file-not-found error, consistent with `002-read-book-file`.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The program MUST determine which book to analyze from a
  command-line argument rather than a hardcoded path.
- **FR-002**: If no book-path argument is provided, the program MUST print
  the exact message `Usage: python3 main.py <path_to_book>` and terminate
  with a non-zero exit status, without producing any analysis output.
- **FR-003**: If a book-path argument is provided, the program MUST analyze
  the book at that path and print its report exactly as before (per
  `007-print-report`), with the report showing that path.
- **FR-004**: The program MUST work correctly for at least three different
  book files: `books/frankenstein.txt`, `books/mobydick.txt`, and
  `books/prideandprejudice.txt`.

### Key Entities

- N/A — no new data entities; this feature changes how the existing report
  pipeline obtains its input path.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Running `python3 main.py books/frankenstein.txt`,
  `python3 main.py books/mobydick.txt`, and
  `python3 main.py books/prideandprejudice.txt` each produce a correct,
  distinct report naming the respective book path.
- **SC-002**: Running the program with no arguments prints exactly the
  specified usage message and produces no report output.
- **SC-003**: Each run completes in under 10 seconds (larger books, e.g.
  Moby Dick, are still well within this bound).

## Assumptions

- Per this project's constitution (Lesson Fidelity), argument access uses
  `sys.argv`, the minimum-length check is `len(sys.argv) < 2`, the usage
  message and exit call (`sys.exit(1)`) match the lesson's instructions
  verbatim.
- Per the constitution's Standard Library Only principle, `sys` is used
  (it's part of the standard library) with no third-party argument-parsing
  library (e.g. `argparse`), since the lesson doesn't call for one and the
  need (a single positional path) doesn't justify one.
- `books/mobydick.txt` and `books/prideandprejudice.txt` are downloaded via
  the lesson's provided `curl` commands, the same way
  `books/frankenstein.txt` was in the "Book Data" lesson, and are not
  tracked in git (already covered by the existing `books/` gitignore entry).
