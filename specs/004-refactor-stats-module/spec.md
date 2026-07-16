# Feature Specification: Refactor Stats Module

**Feature Branch**: `004-refactor-stats-module`

**Created**: 2026-07-17

**Status**: Draft

**Input**: User description: "boot.dev 'Refactor' lesson: move the word-counting function out of main.py into a new stats.py module, and import it back into main.py with `from stats import get_num_words`. Program behavior and output must not change."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Program behaves identically after the split (Priority: P1)

As the learner working through bookbot, I run the program after splitting the
code across files, and it produces exactly the same output as before, so I
can trust that reorganizing code is safe and doesn't silently change what the
program does.

**Why this priority**: This is a pure refactor — the entire point is that
observable behavior is unchanged while the code's internal organization
improves. If output changes, the refactor has failed regardless of how the
files are organized.

**Independent Test**: Run the program before and after the refactor and
confirm byte-for-byte identical console output.

**Acceptance Scenarios**:

1. **Given** the project's text-analysis logic now lives in a separate
   module from the program's entry point, **When** the program is run,
   **Then** the console output is identical to the output before the
   refactor.
2. **Given** the entry point module, **When** its source is inspected,
   **Then** it obtains the word-counting capability via an explicit,
   named import from the analysis module (not a wildcard import, not a
   copy-pasted duplicate definition).

### Edge Cases

- N/A — this feature changes code organization only; there is no new
  input/output behavior to account for edge cases on.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The word-counting capability MUST be defined in a dedicated
  text-analysis module, separate from the program's entry-point module.
- **FR-002**: The entry-point module MUST obtain the word-counting capability
  via an explicit, named import (not `import *`, not a re-implementation).
- **FR-003**: Running the program MUST produce output identical to the
  output before this refactor (still exactly `Found {num_words} total
  words`, with the same count).
- **FR-004**: The file/module MUST be named `stats`, and the imported name
  MUST be `get_num_words`, per the lesson's explicit instructions.

### Key Entities

- N/A — no data entities; this is a code-organization change only.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Running the program after the refactor produces output
  byte-for-byte identical to before the refactor.
- **SC-002**: The word-counting logic exists in exactly one place (the new
  analysis module) — no duplicate definition remains in the entry-point
  module.

## Assumptions

- Per this project's constitution (Lesson Fidelity), the new module is named
  `stats.py` and the import is exactly `from stats import get_num_words`, as
  explicitly instructed by the lesson.
- Per the constitution's Incremental, Non-Destructive Growth principle, only
  `get_num_words` moves in this refactor; `get_book_text` and `main` remain
  in `main.py` since the lesson does not ask to relocate them.
- No behavior, output format, or function signature changes — this is
  structural only, consistent with the lesson's definition of "refactor."
