# bookbot

A command-line text analyzer written in Python, built as part of boot.dev's guided
project [Build a BookBot in Python](https://www.boot.dev/courses/build-bookbot-python).

The program reads a plain text file, such as a novel from
[Project Gutenberg](https://www.gutenberg.org/), counts its words and characters,
and prints a formatted report.

## Learning goals

### 1. Setup

- Set up a local Python development environment.
- Run Python scripts from the terminal instead of an in-browser editor.
- Use Git for version control and publish the project to GitHub.
- Work with the everyday developer workflow: editor, shell, commits.

### 2. Data analysis

- Read a file from disk with Python's file I/O (`open` and a `with` block).
- Split text into words and count them.
- Count how often each character appears, case-insensitively, using a dictionary.
- Split the logic into small, reusable functions and modules.

### 3. Report

- Sort the character counts from most to least frequent.
- Filter out non-alphabetic characters from the report.
- Print a readable report with formatted strings.
- Accept the path of the book as a command-line argument (`sys.argv`), so the
  program works with any plain text file.
- Report incorrect usage with a helpful message and a non-zero exit code.

## Skills covered

File I/O, text processing, string manipulation, formatted output, and
command-line arguments.

## Usage

```sh
python3 main.py books/frankenstein.txt
```
