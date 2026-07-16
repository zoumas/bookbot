# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a command-line tool that analyzes a book's text and prints a
word-count and character-frequency report.

## Usage

```bash
python3 main.py <path_to_book>
```

For example:

```bash
python3 main.py books/frankenstein.txt
```

produces a report like:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
---------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

If no book path is given, it prints a usage message and exits with a
non-zero status:

```
Usage: python3 main.py <path_to_book>
```

The character-count section only lists alphabetical characters (letters),
sorted from most to least frequent, case-insensitively.

### Getting book text to analyze

Book text files aren't checked into this repo (`books/` is gitignored).
Fetch a public-domain sample, e.g.:

```bash
mkdir -p books
curl -L "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt" -o books/frankenstein.txt
```

## About this repo

This is a working-through of the [Build a Bookbot in Python](https://www.boot.dev/courses/build-bookbot-python) course, done using **Specification-Driven Development (SDD)** via [GitHub's Spec Kit](https://github.com/github/spec-kit) instead of coding ad hoc from the lesson prompts.

Setup-only lessons (environment, workspace conventions, etc.) are done directly. Lessons that introduce actual program behavior go through the Spec Kit cycle:

1. **`/specify`** — write a spec describing what the feature should do and why, based on the lesson's requirements.
2. **`/plan`** — turn the spec into a technical plan (language constructs, structure, approach).
3. **`/tasks`** — break the plan into a concrete, checkable task list.
4. **Implement** — work through the tasks, then verify the result against what the lesson expects.

Each lesson's feature builds on the same codebase incrementally, so the specs and plans accumulate alongside the bookbot program itself.
