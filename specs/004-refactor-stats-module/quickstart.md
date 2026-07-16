# Quickstart: Refactor Stats Module

## Prerequisites

- Python 3 installed (`python3 --version`)
- `books/frankenstein.txt` present at the project root

## Run

```bash
python3 main.py
```

## Expected Outcome

Console prints exactly the same line as before the refactor:

```
Found 75767 total words
```

## Validation

- Manual: run the command above before and after the refactor; confirm the
  two outputs are identical. Confirm `get_num_words` is defined only in
  `stats.py` (`grep -n "def get_num_words" *.py` should show one match).
- Automated: `bootdev run <lesson-id>` (and `-s` to submit) against this
  lesson's check.
