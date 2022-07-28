# Leetcode solutions

This is a compiled list of Leetcode solutions. It will be updated as and when I complete them.

> Note: As of this point in time, all solutions are written in Python, although this may change

## File structure

Each solution's folder follows the following convention.

```
<problem_id>_<day>-<month>-<year>
```

Within each problems folder you'll find:
* problem.md - A markdown copy paste version of the problem available on the Leetcode website
* solution.py - The solution. This will most likely be the solution submitted, however there may also be surrounding code
* run.py - A python file which will run the examples given in the problem.md

## Utils

`` generate.py `` will quickly generate a folder and surrounding files with a given id and today's date.

```
§ python3 utils/generate.py -h
usage: generate.py [-h] -p PROBLEM_ID [-t PROBLEM_TITLE]

Generate the default folder structure for a Leetcode solution

options:
  -h, --help            show this help message and exit
  -p PROBLEM_ID, --problem PROBLEM_ID
                        The problem ID, as seen on the Leetcode website
  -t PROBLEM_TITLE, --title PROBLEM_TITLE
                        The problems title, as given on the Leetcode website
```