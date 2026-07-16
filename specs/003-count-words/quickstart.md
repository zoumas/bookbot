# Quickstart: Count Words

## Prerequisites

- Python 3 installed (`python3 --version`)
- `books/frankenstein.txt` present at the project root

## Run

```bash
python3 main.py
```

## Expected Outcome

Console prints exactly one line:

```
Found {num_words} total words
```

with `{num_words}` replaced by the actual count. No raw book text is printed.

## Validation

- Manual: run the command above and sanity-check the count against
  `wc -w books/frankenstein.txt` (may differ slightly from Python's
  `str.split()` count on edge-case whitespace, but should be close).
- Automated: `bootdev run <lesson-id>` (and `-s` to submit) against this
  lesson's check.
