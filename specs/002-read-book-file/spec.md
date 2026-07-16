# Feature Specification: Read Book File

**Feature Branch**: `002-read-book-file`

**Created**: 2026-07-17

**Status**: Draft

**Input**: User description: "boot.dev 'Read File' lesson: replace the greeting-script behavior. Add a get_book_text(path) function that opens a file at a given relative path using a with block and returns its full contents as a string. Add a main() function that calls get_book_text() with the relative path to books/frankenstein.txt and prints the full returned text to the console. main() is invoked when the program runs. This replaces the previous 'greetings boots' print in main.py."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Read and display a book's full text (Priority: P1)

As the learner running bookbot, I run the program and see the entire text of
a book (Frankenstein) printed to the console, so I can confirm the program
can load real book data as the foundation for the analysis features to come.

**Why this priority**: This is the first step toward bookbot's actual purpose
(analyzing novels). Every later analysis feature depends on being able to
load a book's text reliably.

**Independent Test**: Run the program from the project root with the book
file present at its expected location, and confirm the console output is the
book's complete, unmodified text.

**Acceptance Scenarios**:

1. **Given** a book text file exists at the expected relative location,
   **When** the program is run, **Then** the console output is the file's
   entire contents, unmodified, with nothing else printed before or after.
2. **Given** the file-reading capability is invoked directly with a path to a
   text file, **When** it completes, **Then** it returns the file's full
   contents as a single string (not partial, not line-by-line/truncated).

### Edge Cases

- What happens when the book file is missing from its expected location? The
  program MAY fail with a standard file-not-found error; graceful/custom
  error handling is out of scope for this feature (no lesson requirement to
  handle it).
- Empty file: reading an empty file returns an empty string; the program
  prints nothing for the book content in that case.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST provide a way to read the full contents of a
  book text file, given a relative path to it, and return those contents as
  a string. This capability MUST be named `get_book_text`.
- **FR-002**: `get_book_text` MUST return the file's complete contents,
  unmodified (no trimming, encoding changes, or partial reads).
- **FR-003**: The project MUST provide a `main` entry point that: calls
  `get_book_text` with the relative path to the project's Frankenstein text
  (`books/frankenstein.txt`), and prints the returned contents to the
  console.
- **FR-004**: `main` MUST be invoked automatically when the program is run
  (e.g. `python3 main.py`), with no additional input required from the user.
- **FR-005**: The previous "greetings boots" console output MUST no longer
  appear when the program is run.

### Key Entities

- **Book text**: The complete raw text content of a book file, represented
  as a single string once loaded.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Running the program prints the complete text of
  `books/frankenstein.txt` to the console, matching the file's contents
  exactly, on the first attempt.
- **SC-002**: The program runs to completion in under 5 seconds with no
  errors, given the book file is present at its expected location.
- **SC-003**: No trace of the earlier "greetings boots" message remains in
  the program's output.

## Assumptions

- Per this project's constitution (Lesson Fidelity), the function name
  `get_book_text` and the entry-point function `main` are used verbatim, since
  the lesson's own code example names them explicitly, even though the lesson
  text also says naming is "flexible."
- The book file lives at `books/frankenstein.txt` relative to the project
  root (established in the prior "Book Data" lesson) and is not re-downloaded
  or validated by this feature.
- File reading uses the platform's default text encoding, matching the
  lesson's simple `open(path)` / `.read()` example with no explicit encoding
  argument.
- Per the constitution's "Standard Library Only" principle, no third-party
  file-handling libraries are introduced.
