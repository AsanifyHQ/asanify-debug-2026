# Asanify · Jadavpur University 2026 · Section 1

**35 minutes. Weight: 60% of the engineering score.**

## What this is

A payroll reporting service with four defects. Support has raised four tickets
this month and someone has written a test for each of them. All four tests fail.

The tests tell you **what** is wrong. None of them tells you **where**.

## Setup

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Python 3.10 or newer. No other dependencies, no network needed.

## What to do

Make the tests pass. Change only what you need to change.

Two of the four failures are crashes and will be obvious. Two are silent: the
code runs, returns a number, and the number is wrong. Those are the ones that
cost money in production, and they are worth more of your attention.

## On using AI

**You may use any AI tool you like.** We use them too. We are not going to
pretend otherwise and we are not monitoring your screen.

What you should know: on **18 September you will sit with an engineer, your
submitted diff printed in front of them, and spend five minutes explaining your
own changes, then twelve minutes extending this code live** with a fifth defect
we seed on the spot. Your laptop stays open for that. AI stays allowed.

So use whatever helps you understand the code. Submitting a fix you cannot
explain is the one strategy that reliably fails.

## What we score

- Tests passing, against a **larger suite than the one you can see**. Several of
  the hidden cases catch a change that makes a visible test pass while breaking
  something else.
- **How much of the codebase you touched.** A small, surgical diff scores above
  a large one that passes the same tests. Read before you rewrite.

Partial credit is real. Two bugs fixed well beats four fixed carelessly.

## How to submit

Zip the whole folder, keeping the structure, and upload it on the form. Do not
rename directories. Do not include `.venv`.

```
cd .. && zip -r yourname.zip asanify-debug-2026 -x '*.venv*' '*__pycache__*'
```

Deadline is the form close time. A late zip is not accepted by the form.
