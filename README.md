# Asanify · Jadavpur University 2026 · Section 1

**35 minutes · 60% of your engineering score**

---

## What this is

A payroll reporting service with **four defects**. Support raised four tickets
this month and someone wrote a test for each one. All four tests fail.

The tests tell you **what** is wrong. None of them tells you **where**.

Five files, under 150 lines total. You are not expected to know anything about
payroll — every bug is findable by reading code.

---

## Getting it running

**Route A — if pip works on your machine**

```
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

**Route B — if pip or your network will not cooperate**

```
python3 check.py
```

Zero installs, nothing downloaded, standard library only. It runs the same four
checks and prints which pass. **Do not spend your clock fighting pip. Switch to
Route B and move on.**

Either way, still open `tests/test_payroll.py` — the tests carry the bug reports
and the expected values, and reading them is most of the work.

Python 3.10 or newer. Check with `python3 --version`.

---

## How we score this

Read this part. It changes how you should spend the 35 minutes.

**1 · Tests passing, against a bigger suite than you can see.**
We grade with a larger set of tests than the four in front of you. Several of
them catch a change that makes a visible test pass while quietly breaking
something else. So a fix that satisfies the test without being *correct* will
not score as well as it appears to.

**2 · The four bugs are not worth the same.**
Two of the failures are **crashes** — you will get a traceback pointing at a
line. Two are **silent**: the code runs, returns a number, and the number is
wrong. The silent pair is worth roughly **twice** the crashing pair, because
finding a bug where nothing throws is the harder and more valuable skill.

If you are running short on time, the silent ones are where the marks are.

**3 · How much you changed.**
A small, surgical fix scores **above** a large one that passes the same tests.
Read before you rewrite. If two candidates pass the same tests, the one who
touched fewer lines ranks higher.

**4 · Partial credit is real.**
Nobody needs all four. **Two bugs fixed properly beats four fixed carelessly.**
There is no penalty for leaving one alone, and there is a real penalty for
rewriting half the codebase to force a green tick.

---

## On using AI

**You may use any AI tool you like.** We use them too. We are not going to
pretend otherwise and we are not watching your screen.

What you should know: on **18 September you will sit with one of our engineers,
your submitted diff printed in front of them.** You will spend five minutes
explaining your own changes, then twelve minutes extending this code live, with
a fifth defect we introduce on the spot. Your laptop stays open. AI stays
allowed.

So use whatever helps you understand the code. **Submitting a fix you cannot
explain is the one strategy that reliably fails.**

---

## If you do not write Python

This is a reading exercise. If you work in C++, Java or JavaScript you can do
it. The entire codebase uses five constructs:

| You will see | It means |
|---|---|
| `@dataclass` above a class | a plain struct — fields, no methods |
| `[x for x in rows if x.a == b]` | filter a list; same as a loop with an `if` |
| `Decimal("12.50")` | exact decimal money — never `float` for rupees |
| `datetime.fromisoformat(s)` | parse `"2026-01-16T00:00:00"` into a date object |
| `def f(a, b=None)` | `b` is optional, defaults to `None` |

That is genuinely all of it. If a line is unfamiliar, ask an AI what it does —
that is a fine use of your time.

---

## Submitting

Zip the whole folder, keeping its structure. Do not rename directories. Do not
include `.venv`.

```
cd ..
zip -r yourname.zip asanify-debug-2026 -x '*.venv*' '*__pycache__*'
```

Windows without `zip`: right-click the folder → Send to → Compressed folder.

Upload it on the form. **Leave four minutes for this.** The form closes at the
stated time and will not accept a late upload.
