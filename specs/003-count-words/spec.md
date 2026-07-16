# Feature Specification: Count Words

**Feature Branch**: `003-count-words`

**Created**: 2026-07-17

**Status**: Draft

**Input**: User description: "boot.dev 'Count Words' lesson: add a function that takes the book text string and returns the total word count using Python's str.split(). Update main() so that instead of printing the full book text, it prints 'Found {num_words} total words' with the actual count substituted in. main() still calls get_book_text('books/frankenstein.txt') first to obtain the text."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - See the book's total word count (Priority: P1)

As the learner running bookbot, I run the program and see a report of how
many words are in the book, instead of the raw text dump, so bookbot starts
to feel like an analysis tool rather than a file printer.

**Why this priority**: This is the first genuine analysis feature (as opposed
to just loading data) and the first line of what will become a multi-line
report in later lessons.

**Independent Test**: Run the program from the project root with the book
file present, and confirm the console shows a single line reporting the
correct total word count, with no raw book text printed.

**Acceptance Scenarios**:

1. **Given** the book file is loaded, **When** the program runs, **Then**
   the console shows exactly one line: `Found {num_words} total words`,
   where `{num_words}` is the book's actual total word count.
2. **Given** the word-counting capability is invoked directly with a string
   of text, **When** it completes, **Then** it returns the total number of
   words in that string as an integer.
3. **Given** the program runs, **When** it completes, **Then** the full raw
   book text is no longer printed to the console (replaced by the word-count
   report line).

### Edge Cases

- Empty string input to the word-counting capability: returns `0`.
- Multiple consecutive whitespace characters (spaces, tabs, newlines) between
  words: does not inflate the count — words are separated by runs of
  whitespace, not by single-space splitting.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST provide a way to count the total number of
  words in a given block of text, returning that count as a whole number.
- **FR-002**: Word counting MUST treat any run of whitespace as a single
  separator between words (consistent with Python's default `str.split()`
  behavior), so extra spaces/newlines don't affect the count.
- **FR-003**: `main` MUST print exactly one line in the form
  `Found {num_words} total words`, with `{num_words}` replaced by the actual
  count for `books/frankenstein.txt`.
- **FR-004**: `main` MUST no longer print the book's full raw text.

### Key Entities

- **Word count**: A single non-negative integer representing the total
  number of words found in a given text.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Running the program prints exactly one line of the form
  `Found {num_words} total words`, with the correct count for
  `books/frankenstein.txt`, on the first attempt.
- **SC-002**: No raw book text appears in the program's console output.
- **SC-003**: The program runs to completion in under 5 seconds.

## Assumptions

- Per this project's constitution (Standard Library Only / Lesson Fidelity),
  word counting uses Python's built-in `str.split()` with no arguments, as
  directed by the lesson, rather than a regex or third-party library.
- The word-counting capability's exact function name is not dictated by the
  lesson text; a clear, descriptive name is chosen at planning time (the
  lesson explicitly allows naming flexibility here, unlike `get_book_text`
  and `main` which were named explicitly in an earlier lesson).
- `main` continues to call `get_book_text("books/frankenstein.txt")` first
  (established in the prior "Read File" feature); this feature only changes
  what `main` does with the resulting text and what it prints.
