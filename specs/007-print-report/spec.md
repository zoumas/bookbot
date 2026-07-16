# Feature Specification: Print a Report

**Feature Branch**: `007-print-report`

**Created**: 2026-07-17

**Status**: Draft

**Input**: User description: "boot.dev 'Print a Report' lesson: add a print_report(book_path, num_words, sorted_char_list) function in main.py that prints a formatted analysis report (header, book path, word count section, alphabetical-only character count lines, closing line) in the lesson's exact format. Replace the existing separate print calls in main() with a single call to print_report."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - See one cohesive, formatted analysis report (Priority: P1)

As the learner running bookbot, I run the program and see a single,
readable, formatted report — with a title, the book being analyzed, the
word count, and an alphabetical character-frequency breakdown — instead of
two separate, unlabeled print statements, so bookbot finally looks and reads
like the finished analysis tool the course has been building toward.

**Why this priority**: This is the culmination of every prior analysis
lesson (reading the book, counting words, counting characters, sorting
them) into one presentable output. It's the first time the program's output
is meant to be read by an end user rather than just inspected by the
developer.

**Independent Test**: Run the program from the project root and confirm the
console shows the complete report, matching the required structure and
content exactly, for `books/frankenstein.txt`.

**Acceptance Scenarios**:

1. **Given** the book has been analyzed (word count and sorted character
   counts computed), **When** the program runs, **Then** the console shows,
   in order: an opening header line, a line naming the book being analyzed,
   a word-count section header followed by the word-count line, a
   character-count section header followed by one line per alphabetical
   character (in the existing most-to-least-frequent order) formatted as
   `{character}: {count}`, and a closing line.
2. **Given** the sorted character list contains non-alphabetical entries
   (spaces, punctuation, digits, newlines), **When** the report is printed,
   **Then** none of those entries appear in the character-count section —
   only alphabetical characters are listed.
3. **Given** the report-printing capability is invoked directly with a book
   path, a word count, and a sorted character list, **When** it completes,
   **Then** it produces the complete report as its only output (no other
   print statements execute alongside it).

### Edge Cases

- A sorted character list with zero alphabetical entries: the character
  count section header still appears, followed immediately by the closing
  line (no character lines).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST provide a single capability that prints a
  complete analysis report given: the path of the book being analyzed, the
  total word count, and the sorted list of (character, count) pairs.
- **FR-002**: The report MUST include, in order: an opening header, a line
  identifying the book path being analyzed, a word-count section (header +
  the total word count), a character-count section (header + one line per
  alphabetical character formatted as `{character}: {count}`, in the same
  most-to-least-frequent order as the sorted input), and a closing line.
- **FR-003**: Non-alphabetical entries (whitespace, punctuation, digits,
  symbols) in the sorted character list MUST be excluded from the
  character-count section.
- **FR-004**: The report's literal text — headers, section labels, and
  closing line — MUST match the course's specified wording and punctuation
  exactly, since it is checked by automated tests.
- **FR-005**: `main` MUST produce the report via this single capability,
  replacing the previously separate word-count and character-list print
  statements.

### Key Entities

- **Analysis report**: The complete, formatted console output for one book,
  composed of a header, the book's identity, its word count, and its
  alphabetical character-frequency breakdown, followed by a closing line.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Running the program produces the complete report, matching
  the required text and structure exactly, for `books/frankenstein.txt`, on
  the first attempt.
- **SC-002**: No non-alphabetical character appears in the character-count
  section of the printed report.
- **SC-003**: The program's console output consists of exactly one report
  (no leftover separate print statements from prior lessons).
- **SC-004**: The program runs to completion in under 5 seconds.

## Assumptions

- Per this project's constitution (Lesson Fidelity), the report's exact
  wording, punctuation, and structure are copied verbatim from the lesson's
  provided example output:
  - Opening header: `============ BOOKBOT ============`
  - Book line: `Analyzing book found at {book_path}...`
  - Word count section header: `---------- Word Count ----------`
  - Word count line: `Found {num_words} total words`
  - Character count section header: `--------- Character Count -------`
  - Character lines: `{character}: {count}` (lowercase, one per line, in the
    existing sorted order)
  - Closing line: `============= END ===============`
- Per this project's constitution (Lesson Fidelity), the capability's name
  is `print_report` and it lives in `main.py`, and its parameters are the
  book path, word count, and sorted character list, as explicitly specified
  by the lesson.
- Alphabetical filtering uses Python's `str.isalpha()`, as the lesson
  directs.
