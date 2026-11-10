# 🤝 Team workflow: five people, one repository

This page explains how your group shares one GitHub repository without losing anyone's work.
Read it **once, together**, before you start Part 1.

---

## The three habits that prevent 90% of problems

1. **`git pull` before you start working.** Every time. This downloads your teammates' latest work.
2. **Commit small, push soon.** Don't sit on finished work for days. Push it so others can build on it.
3. **One person edits the notebook at a time** (the baton). Other files can be edited in parallel, but **tell the group** which file you're editing.

---

## The daily routine

```bash
# 0. Open the project folder in VS Code, then in the terminal:
.venv\Scripts\Activate.ps1          # Windows   (macOS: source .venv/bin/activate)

# 1. Get the latest version
git pull

# 2. ...do your work, save your files (Ctrl + S)...

# 3. See what changed
git status

# 4. Save a snapshot and upload it
git add .
git commit -m "Short description of what you did"
git push
```

**Using the VS Code buttons instead:** click the **Source Control** icon on the left (it looks like a branch) →
type a message in the box → **✓ Commit** → **Sync Changes** (this pulls and pushes).

### Writing good commit messages
| ❌ Not helpful | ✅ Helpful |
|---|---|
| `update` | `Part 2: fix LGA spellings and Yes/No columns` |
| `final final 2` | `Part 5: add squared rainfall term and coefficient table` |
| `.` | `App: complete TODOs 4-6 (prediction and metrics)` |

---

## The baton: sharing `group_project.ipynb`

Jupyter notebooks are stored as complicated text (JSON). If two people change the notebook at the same time, Git usually **cannot merge** them automatically. So:

> **Only the person holding the baton edits and pushes `notebooks/group_project.ipynb`.**

| Order | Baton holder | Parts |
|---|---|---|
| 1 | Member 1 (Data lead) | 0, 1, 2 |
| 2 | Member 2 (Visualisation lead) | 3 |
| 3 | Member 3 (Statistics lead) | 4, 5 |
| 4 | Member 4 (ML lead) | 6 |
| 5 | Member 2 (Visualisation lead) | 7 |
| 6 | Member 5 (App lead) | 8, 9 |

**Passing the baton**
1. Finish your part → **Run All** → check your ✅s.
2. `git add .` → `git commit -m "Part X: ..."` → `git push`
3. Post in your group chat: **"Part X pushed ✅ [Name], the baton is yours."**
4. **Stop editing the notebook.** If you need to fix something later, ask for the baton back.

**Receiving the baton**
1. `git pull`
2. Open the notebook → **Run All** (so all the variables from earlier parts exist).
3. Do your part.

### Practising while you wait: the `scratch/` folder
`notebooks/scratch/` is listed in `.gitignore`, so **nothing in it is uploaded**. Use it freely:

```bash
# Windows PowerShell
Copy-Item notebooks\group_project.ipynb notebooks\scratch\my_practice.ipynb
# macOS / Linux
cp notebooks/group_project.ipynb notebooks/scratch/my_practice.ipynb
```

Open your practice copy, use the hints and answers to run Parts 1 and 2 (so you have clean data), then try your own part. When the baton reaches you, `git pull` and **type or paste your working code into the real notebook**.

> ⚠️ Running the real notebook changes its outputs, which counts as an edit. If you only want to *look* at the
> real notebook without the baton, **don't save it**. If you saved it by accident, undo your changes before
> the next pull: `git restore notebooks/group_project.ipynb`

### Files you can work on in parallel
| File | Usually edited by | Rule |
|---|---|---|
| `app/streamlit_app.py` | Member 5 | Member 5 only |
| `report/GROUP_REPORT.md` | everyone | Say in the chat when you're editing; pull first; push soon |
| `CONTRIBUTIONS.md` | everyone | Edit only **your own row** |
| `docs/AI_USE_STATEMENT.md` | Member 5 collects from everyone | Send your AI use to Member 5 on WhatsApp |
| `README.md` (top section) | Coordinator | Coordinator only |

---

## When things go wrong

### "Updates were rejected because the remote contains work that you do not have locally"
Someone pushed before you. That's normal:
```bash
git pull
git push
```
If `git pull` opens an editor with a message like *"Merge branch 'main'…"*, just save and close it (in Vim: type `:wq` and press Enter).

### "Your local changes would be overwritten by merge" when you `git pull`
You changed a file that a teammate also changed. Decide:

- **Your changes are NOT important** (e.g. you only ran the notebook): throw them away and pull.
  ```bash
  git restore notebooks/group_project.ipynb
  git pull
  ```
- **Your changes ARE important:** save them as a backup copy first, then throw them away and pull.
  ```bash
  Copy-Item notebooks\group_project.ipynb notebooks\scratch\my_backup.ipynb     # Windows
  git restore notebooks/group_project.ipynb
  git pull
  ```
  Then open your backup and copy your cells into the updated notebook.

### "CONFLICT (content): Merge conflict in notebooks/group_project.ipynb"
Two people edited the notebook. **Don't panic, and don't try to edit the conflict by hand** (it's a notebook).
```bash
git merge --abort                       # go back to how things were before the pull
```
Then follow *"Your changes ARE important"* above. Afterwards, agree in the chat who holds the baton.

### Conflict in a Markdown file (README, report, CONTRIBUTIONS)
These are easy. VS Code highlights the conflict with **Accept Current / Accept Incoming / Accept Both** buttons. Usually choose **Accept Both**, delete anything duplicated, save, then:
```bash
git add .
git commit -m "Merge teammate's changes"
git push
```

### "I committed something by mistake but haven't pushed"
```bash
git reset --soft HEAD~1     # undo the last commit, keep the changes in your files
```

### Something is badly broken and you just want a fresh copy
Rename your project folder (e.g. add `_old`), then **clone the repository again** (README, Step 3b) and recreate the `.venv` (Step 4). Copy anything you need from the old folder.

---

## ⭐ Optional, for confident groups: branches and pull requests
Instead of the baton, each member can work on a **branch** and open a **pull request** (PR) for a teammate to review:
```bash
git switch -c part3-eda             # create a branch and move to it
# ...work, commit...
git push -u origin part3-eda        # GitHub will show a "Compare & pull request" button
```
A teammate reviews the PR on GitHub and clicks **Merge**. You still can't merge two different notebook edits automatically, so keep notebook PRs **one at a time**.
