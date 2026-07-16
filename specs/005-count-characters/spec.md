# Feature Specification: Count Characters

**Feature Branch**: `005-count-characters`

**Created**: 2026-07-17

**Status**: Draft

**Input**: User description: "boot.dev 'Count Characters' lesson: add a function in stats.py that takes book text and returns a dict mapping each lowercased character to how many times it appears. Update main() to call it, store the result, and print both the word count (existing) and the character-frequency dictionary."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - See character frequency counts for the book (Priority: P1)

As the learner running bookbot, I run the program and see, in addition to
the word count, a breakdown of how often each character appears in the book
(case-insensitive), so bookbot's analysis report grows toward its eventual
full statistics report.

**Why this priority**: This is the second analysis metric bookbot produces,
building directly on the word-count feature, and is a prerequisite for later
lessons that will sort/format this data into a readable report.

**Independent Test**: Run the program from the project root and confirm the
console shows the word count followed by a dictionary of character counts
that correctly tallies the book's text case-insensitively.

**Acceptance Scenarios**:

1. **Given** the book text has been loaded, **When** the program runs,
   **Then** the console shows the existing word-count line followed by a
   printed mapping of characters to their occurrence counts.
2. **Given** the character-counting capability is invoked directly with a
   string containing both uppercase and lowercase forms of the same letter
   (e.g. "Aa"), **When** it completes, **Then** both forms are tallied under
   a single lowercase key (e.g. `{'a': 2}`), not split into separate
   uppercase/lowercase entries.
3. **Given** the character-counting capability is invoked with an empty
   string, **When** it completes, **Then** it returns an empty mapping.

### Edge Cases

- Non-letter characters (spaces, punctuation, digits, newlines): each is
  still counted under its own key like any other character; the lesson does
  not ask for filtering to letters only.
- A character that appears zero times in the text simply has no entry in the
  result (no zero-count entries for the full alphabet).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST provide a way to count how many times each
  character appears in a given block of text, returning the result as a
  mapping from character to count.
- **FR-002**: Character counting MUST be case-insensitive: uppercase and
  lowercase forms of the same letter MUST be tallied under one lowercase key.
- **FR-003**: `main` MUST invoke this capability on the loaded book text and
  store the resulting mapping in a variable.
- **FR-004**: `main` MUST print both the existing word-count line and the
  character-frequency mapping, in that order.
- **FR-005**: The new capability MUST live alongside the existing
  word-counting capability (i.e. in the `stats` module established in the
  prior refactor), not duplicated into the entry-point module.

### Key Entities

- **Character frequency mapping**: A mapping from a single lowercase
  character to a non-negative integer count of its occurrences in a given
  text.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Running the program prints the word-count line followed by a
  character-frequency mapping that correctly and completely tallies
  `books/frankenstein.txt`, case-insensitively, on the first attempt.
- **SC-002**: For any input containing mixed-case repeats of the same
  letter, the resulting mapping never contains both an uppercase and a
  lowercase key for that letter.
- **SC-003**: The program runs to completion in under 5 seconds.

## Assumptions

- Per this project's constitution (Standard Library Only / Lesson Fidelity),
  case-insensitivity is achieved via `str.lower()`, as the lesson directs,
  rather than a custom-normalization scheme.
- The new capability's exact function name is not dictated by the lesson
  text; a clear, descriptive name is chosen at planning time (same
  precedent as `get_num_words` in feature 003).
- The mapping is a plain `dict[str, int]`, matching the lesson's stated
  return type, not a specialized counter class — this is the simplest
  option consistent with YAGNI and is sufficient for this lesson's needs.
- No sorting or formatting of the character mapping is required yet — this
  lesson only asks that it be computed and printed as-is; presentation is
  expected to be addressed in a later lesson.
