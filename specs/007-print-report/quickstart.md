# Quickstart: Print a Report

## Prerequisites

- Python 3 installed (`python3 --version`)
- `books/frankenstein.txt` present at the project root

## Run

```bash
python3 main.py
```

## Expected Outcome

Console prints exactly:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
---------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```

## Validation

- Manual: run the command above and diff the output against the block
  above.
- Automated: `bootdev run <lesson-id>` (and `-s` to submit) against this
  lesson's check.
