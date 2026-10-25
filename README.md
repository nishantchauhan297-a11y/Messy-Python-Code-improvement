# Messy Python Code Improvement

A messy Python script cleaned up with AI assistance. The program prints each student's average, best mark and grade, and gives the **same output** before and after.

## Files

- `messy_original.py`: the original script (one-letter names, no comments, repeated indexing, nested if/else)
- `improved.py`: the cleaned-up version

## What was improved

| Problem in the original | Improvement |
|---|---|
| Names like `f`, `g`, `h`, `d`, `l`, `t` | Clear names: `calculate_average`, `find_highest`, `get_grade`, `student_marks` |
| Manual loop with `range(len(l))` to add numbers | Built-in `sum()` |
| Manual loop to find the largest value | Built-in `max()` |
| Deeply nested `if / else` for grades | Flat `if` checks with early `return` |
| Strings joined with `+` and `str()` | f-strings |
| No docstrings, no comments | Docstrings on every function |
| Crashes with an unclear error on an empty list | Clear `ValueError` message |
| Unused `import sys` | Removed |
| Code running at the top level | `print_report()` plus `if __name__ == "__main__":` |

## How to run

```bash
python messy_original.py
python improved.py
```

Both print:

```
amit avg:86.33 best:92 grade:B
riya avg:52.33 best:60 grade:C
sam avg:76.0 best:81 grade:B
```

## Technologies

Python 3, AI-assisted refactoring (Cursor AI), Git

## Author

Nishant Chauhan, B.Tech CSE, JECRC University, Jaipur
