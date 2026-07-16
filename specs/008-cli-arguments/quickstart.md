# Quickstart: CLI Arguments

## Prerequisites

- Python 3 installed (`python3 --version`)
- `books/frankenstein.txt`, `books/mobydick.txt`, `books/prideandprejudice.txt`
  present at the project root

## Run

```bash
python3 main.py books/frankenstein.txt
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt
python3 main.py
```

## Expected Outcome

- Each of the first three commands prints a full report (per
  `007-print-report`'s format) naming the respective book path, with correct
  word/character counts for that book.
- The fourth command (no arguments) prints exactly:
  ```
  Usage: python3 main.py <path_to_book>
  ```
  and exits with a non-zero status, with no report output.

## Validation

- Manual: run all four commands above and confirm the outcomes described.
- Automated: `bootdev run <lesson-id>` (and `-s` to submit) against this
  lesson's check.
