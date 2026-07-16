# Feature Specification: Organize Data

**Feature Branch**: `006-organize-data`

**Created**: 2026-07-17

**Status**: Draft

**Input**: User description: "boot.dev 'Organize Data' lesson: add a sort_on(tuple[str, int]) helper in stats.py that returns the count, and a chars_dict_to_sorted_list(dict[str, int]) function that converts the character-count dict into a list of (char, count) tuples sorted from most to least frequent using sorted(..., key=sort_on, reverse=True). Update main() to convert the character-count dict via this function and print the sorted list (in place of the raw, unsorted dict) after the word count."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - See characters ranked from most to least frequent (Priority: P1)

As the learner running bookbot, I run the program and see the book's
character counts presented as a list ordered from most to least frequent,
instead of an unordered dictionary, so the data starts to look like a real
report rather than a raw data dump.

**Why this priority**: This is a direct, necessary step toward the final
human-readable report the course builds toward — an unordered dict isn't
presentable, and later lessons will depend on having this ordering already
in place.

**Independent Test**: Run the program from the project root and confirm the
printed character data is a list of (character, count) pairs in strictly
non-increasing order of count.

**Acceptance Scenarios**:

1. **Given** a character-frequency mapping has been computed for the book,
   **When** the program runs, **Then** the console shows a list of
   (character, count) pairs ordered from highest count to lowest, printed
   after the word-count line, with the raw unordered mapping no longer
   printed.
2. **Given** the ordering capability is invoked directly with a character
   count mapping, **When** it completes, **Then** it returns a list of
   (character, count) tuples where each element's count is greater than or
   equal to the count of the element that follows it.
3. **Given** two characters share the same count, **When** the list is
   produced, **Then** both appear in the list with their correct shared
   count (relative order between exact ties is not constrained).

### Edge Cases

- Empty character-count mapping: returns an empty list.
- Single-entry mapping: returns a single-element list unchanged.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST provide a way to convert a character-count
  mapping into a list of (character, count) pairs ordered from most to least
  frequent.
- **FR-002**: The ordering MUST be based purely on count, descending; the
  specific tie-breaking order between equal counts is unconstrained.
- **FR-003**: `main` MUST print this ordered list, in place of the previously
  printed raw, unordered character-count mapping, after the word-count line.
- **FR-004**: This ordering capability MUST live in the `stats` module
  alongside the existing word- and character-counting capabilities.

### Key Entities

- **Ordered character frequency list**: A list of (character, count) pairs,
  derived from the character frequency mapping, ordered from highest count
  to lowest.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Running the program prints the word-count line followed by a
  list of (character, count) pairs for `books/frankenstein.txt` in strictly
  non-increasing count order.
- **SC-002**: The raw, unordered character-count mapping no longer appears in
  the program's output.
- **SC-003**: The program runs to completion in under 5 seconds.

## Assumptions

- Per this project's constitution (Lesson Fidelity), the helper function is
  named `sort_on` and the conversion function is named
  `chars_dict_to_sorted_list`, matching the lesson's explicit naming, and
  sorting uses Python's built-in `sorted(..., key=sort_on, reverse=True)`.
- Tuples keep the `(character, count)` order (not `(count, character)`), per
  the lesson's own stated preference for readability, even though a
  `(count, character)` order would sort correctly by default without a `key`
  function.
- The raw character-count dictionary is no longer printed directly; printing
  the ordered list is what "printing results after word count output" is
  taken to mean, consistent with the course's progression toward a single
  coherent report rather than duplicate/raw output.
