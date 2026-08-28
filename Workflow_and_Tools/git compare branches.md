---
title: Git Compare Branches
aliases:
  - Compare two branches in Git
  - git diff branches
  - git log branches
tags:
  - git
  - cli
  - workflow
  - git-diff
  - git-log
  - merge
  - branch
date: 2026-08-28
lang: en
---
To compare two branches in Git, you can inspect commit differences, view file changes (diffs), or check branch merge status.

---

### 1. Check for New Commits (Commit History)

To list commits that exist on `<feature-branch>` but are not present in `<base-branch>`:
```bash
git log --oneline <base-branch>..<feature-branch>
```
- Commits marked with `<` exist only on `main`.
- Commits marked with `>` exist only on `feature-branch`.

> [!example] Example
> ```bash
> git log --oneline --left-right main...moise
> ```
> 
> **Output:**
> ```vim
> < d3fe548 (HEAD -> main, origin/main, origin/HEAD) merge moise branch (2gu, gc, se and is).
> < 667954e updating readme
> < 80e2069 Merge branch 'moise'
> < 466922b test
> ```

### 2. Check Ahead / Behind Count
To display an exact numerical count of how many commits the branches are behind/ahead of each other:
```bash
git rev-list --left-right --count <base-branch>...<feature-branch>
```
- **First number:** Commits unique to the left branch (`<base-branch>`).
- **Second number:** Commits unique to the right branch (`<feature-branch>`).

> [!example] Example
> ```bash
> git rev-list --left-right --count main...moise
> ```
> **Output:**
> ```vim
> 4       0
> ```
### 3. Check Code and File Differences (Diff)

To view a summary of modified, added, or deleted files between the common ancestor and the branch tip:
```bash
git diff --stat <base-branch>...<feature-branch>
```
To view the complete line-by-line diff:
```bash
git diff <base-branch>...<feature-branch>
```
> [!example]  Example
> ```
> git diff --stat main...Walid
> ```
> 
> **Output:**
> ```vim
>  Makefile |   2 +-
>  Prod.dot |  57 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
>  Prod.pdf | Bin 30602 -> 34329 bytes
>  mat.dot  |  31 ++++++++++++++++++++++++++++++-
>  mat.pdf  | Bin 51233 -> 52401 bytes
>  meca.dot |  64 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--
>  meca.pdf | Bin 53221 -> 57514 bytes
>  7 files changed, 149 insertions(+), 5 deletions(-)
> ```
> ```vim
> git diff --stat Walid...main
> ```
> 
> **Output:**
> ```vim
>  2GU.dot   |  68 +++++++++++++++++++++++++++++++++++++++++++++++++++++--------
>  2GU.pdf   | Bin 31909 -> 32527 bytes
>  Makefile  |   4 +++-
>  README.md | 103 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-----------------------------
>  gc.dot    | 215 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++----------------
>  gc.pdf    | Bin 48485 -> 54954 bytes
>  is.dot    | 159 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---------------------------------
>  is.pdf    | Bin 51083 -> 54736 bytes
>  se.dot    | 101 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++------------------------------
>  se.pdf    | Bin 52362 -> 53448 bytes
>  10 files changed, 521 insertions(+), 129 deletions(-)
> ```

### 4. Check if the Branch is Fully Merged

To verify if all commits from `<feature-branch>` are already incorporated into `<base-branch>`:
```bash
git branch --merged <base-branch>
```
To list branches that still contain unmerged changes relative to `<base-branch>`:
```bash
git branch --no-merged <base-branch>
```