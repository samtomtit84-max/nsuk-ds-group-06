# 🍠 What drives yam yield in Nasarawa State?
### NSUK Python for Data Science Workshop 2026 · Group Project

---

## 📌 About our project *(groups: complete this section in your own repository)*

> Delete this grey note once you've filled the section in. Everything under **📘 Assignment instructions** can stay as it is.

| | |
|---|---|
| **Group** | Group ___ |
| **Live app** | *(optional: paste your Streamlit Community Cloud link)* |
| **Report** | [`report/GROUP_REPORT.md`](report/GROUP_REPORT.md) |

| Member | GitHub username | Role | Parts |
|---|---|---|---|
| | @ | Coordinator + Data lead | Parts 1–2 |
| | @ | Visualisation lead | Parts 3 and 7 |
| | @ | Statistics lead | Parts 4–5 |
| | @ | Machine-learning lead | Part 6 |
| | @ | App lead | Parts 8–9 |

**Our key findings (3–5 bullet points with numbers):**
- …

**How to run our work:** see [Step 4](#step-4--everyone-set-up-python-on-your-laptop), then open `notebooks/group_project.ipynb` and click **Run All**, then `streamlit run app/streamlit_app.py`.

---

# 📘 Assignment instructions

## Contents
1. [The project in one minute](#1-the-project-in-one-minute)
2. [Deadlines](#2-deadlines)
3. [Your group and your roles](#3-your-group-and-your-roles)
4. [What's in this repository](#4-whats-in-this-repository)
5. [Step-by-step: from zero to submission](#5-step-by-step-from-zero-to-submission)
   - [Step 1: Coordinator creates the group repository](#step-1--coordinator-create-your-groups-repository-from-this-template)
   - [Step 2: Coordinator adds the group as collaborators](#step-2--coordinator-add-every-member-as-a-collaborator)
   - [Step 3: Everyone clones the repository](#step-3--everyone-accept-the-invitation-and-clone-the-repository)
   - [Step 4: Everyone sets up Python](#step-4--everyone-set-up-python-on-your-laptop)
   - [Step 5: Everyone makes a first commit](#step-5--everyone-make-your-first-commit-contributionsmd)
   - [Step 6: Work through the notebook, passing the baton](#step-6--work-through-the-notebook-passing-the-baton)
   - [Step 7: Build the Streamlit app](#step-7--app-lead-complete-the-streamlit-app)
   - [Step 8: Write the report and AI-use statement](#step-8--everyone-write-the-report-and-the-ai-use-statement)
   - [Step 9: Final checks](#step-9--coordinator-final-checks)
   - [Step 10: Submit your work](#step-10--coordinator-submit-your-work)
6. [How you will be marked](#6-how-you-will-be-marked)
7. [Rules for using AI](#7-rules-for-using-ai)
8. [Getting help](#8-getting-help)

---

## 1. The project in one minute

Your group is a team of data scientists working with the Nasarawa State Agricultural Development Programme. You have received a **messy survey of 2,436 yam farms** across all 13 LGAs, and your job is to answer:

> **Which farm practices are associated with higher yam yield, and can we predict a farm's yield *before* harvest?**

You will use **everything from the workshop**, in this order:

```
 raw messy CSV ──► audit ──► clean ──► explore ──► test hypotheses ──► regression ──► machine learning ──► figures ──► Streamlit app ──► report
   (Part 1)        (1)       (2)        (3)          (4)                 (5)             (6)                (7)          (8)              (9)
```

Almost everything is set up for you:
- 📓 **`notebooks/group_project.ipynb`** walks you through every step. Each exercise has a **hint**, a **hidden answer** you can open if you're stuck, and an automatic **✅ check**.
- 🖥️ **`app/streamlit_app.py`** is a finished app with **8 small TODOs** (most are one line).
- 📝 **`report/GROUP_REPORT.md`** is a report template with a heading and prompts for every section.

> 💬 **This project is designed to be achievable.** If you followed the workshop, you can do this. If you get stuck, open the hint. If you are still stuck, open the answer, **make sure you understand it**, and keep going. Ask in the WhatsApp group early, not on the last day.

> ⚠️ **The data is synthetic** (simulated for teaching). It looks realistic but must **not** be cited as evidence about real farms. See [`data/README.md`](data/README.md).

---

## 2. Deadlines

| Milestone | Deadline (WAT) | What should be on GitHub |
|---|---|---|
| **M1: Set-up** | **Wednesday 11 November 2026** | Group repo created · all 5 members added and accepted · everyone has cloned it · every member has pushed their row in `CONTRIBUTIONS.md` |
| **M2: Data** | **Tuesday 17 November 2026** | Parts 1–3 of the notebook done (audit, cleaning, EDA) |
| **M3: Analysis** | **Sunday 22 November 2026** | Parts 4–7 done (tests, regression, machine learning, figures) · model saved |
| **🏁 Final submission** | **Friday 27 November 2026, 11:59 pm** | App finished · report and AI-use statement written · submission issue opened ([Step 10](#step-10--coordinator-submit-your-work)) |

Milestones aren't marked separately. They're there to keep your group on track, because the work is passed from one member to the next.

---

## 3. Your group and your roles

You were put into **groups of 5** at random (balanced so that every group has a mix of experience). Your group number and members were shared on WhatsApp.

Agree on these **five roles** in your first group chat. Each role "owns" some parts of the notebook, but **everyone should understand the whole project**, and you should help each other.

| Role | Owns | Main tasks |
|---|---|---|
| **Member 1: Coordinator + Data lead** | Parts 1–2 | Creates the GitHub repo and adds everyone (Steps 1–2) · audits and cleans the data · keeps the group on schedule · submits the final link |
| **Member 2: Visualisation lead** | Parts 3 and 7 | Exploratory charts · publication-ready figures and tables |
| **Member 3: Statistics lead** | Parts 4–5 | t-tests, chi-square test, regression, interpretation |
| **Member 4: Machine-learning lead** | Part 6 | Model comparison, leakage check, final model, saving the model |
| **Member 5: App lead** | Parts 8–9 | Streamlit app · puts the report together · final reproducibility check |

> 💡 **Who should be the coordinator?** The WhatsApp message suggests one person per group (the member with the most prior experience, listed first). The group can choose someone else. The coordinator doesn't have to do the most work; they just keep things moving.

---

## 4. What's in this repository

```
nsuk-ds-group-project/
├── README.md                      ← you are here (instructions + your group's project summary at the top)
├── CONTRIBUTIONS.md               ← every member records what they did (Step 5)
├── requirements.txt               ← Python packages to install
├── data/
│   ├── README.md                  ← data dictionary: what every column means
│   ├── raw/nasarawa_yam_survey_synthetic.csv   ← the messy survey (NEVER edit by hand)
│   └── processed/                 ← the clean data is saved here by Part 2
├── notebooks/
│   ├── group_project.ipynb        ← ⭐ THE MAIN NOTEBOOK: Parts 0–9
│   └── scratch/                   ← your private practice copies (not uploaded to GitHub)
├── src/project_tools.py           ← helper functions (checks, figure style, model saving). No need to edit
├── app/streamlit_app.py           ← ⭐ the Streamlit app with 8 TODOs
├── figures/                       ← figures saved by the notebook (PNG + PDF)
├── results/                       ← tables saved by the notebook (CSV)
├── models/                        ← the trained model + model card (used by the app)
├── report/GROUP_REPORT.md         ← ⭐ your written report (template)
├── docs/
│   ├── TEAM_WORKFLOW.md           ← how to share ONE notebook between 5 people without conflicts
│   ├── TROUBLESHOOTING.md         ← fixes for common errors
│   ├── RUBRIC.md                  ← the full marking scheme
│   └── AI_USE_STATEMENT.md        ← declare how you used AI (required)
├── scripts/                       ← facilitator tools (data generator, notebook builder). You can ignore these
└── .github/ISSUE_TEMPLATE/        ← the submission form used in Step 10
```

---

## 5. Step-by-step: from zero to submission

### Before you start: what you need

Every member needs these (they're the same as for the workshop; see the workshop's `docs/SETUP.md` if you need to reinstall):

- [ ] A **GitHub account**. Know your **username** (e.g. `praise-mimi`), not just your email.
- [ ] **Python 3.12 or newer**, **VS Code** (with the *Python* and *Jupyter* extensions) and **Git** installed
- [ ] Git told who you are. Run this once in a terminal, using the **same email as your GitHub account**:
  ```bash
  git config --global user.name "Your Full Name"
  git config --global user.email "the-email-you-use-on-github@example.com"
  ```
  *(If the email doesn't match, GitHub won't count your commits as yours, and commits are how we see who contributed.)*
- [ ] **Send your GitHub username to your coordinator** on WhatsApp.

---

### Why "Use this template" and not "Fork"?

You'll make your group's copy with GitHub's **Use this template** button, **not** *Fork*. Here's why:

| | **Use this template** ✅ | Fork ❌ |
|---|---|---|
| Gives your group its **own independent repo** | Yes | No, it stays linked to the original |
| Can be made **private** | Yes | No, forks of a public repo must be public |
| Clean history that shows **only your group's commits** | Yes | No, it includes all the facilitator's commits |
| Risk of accidentally sending changes back to the original | None | You can open pull requests to the original by mistake |

Only **one person per group (the coordinator)** creates the repository. Everyone else gets access as a **collaborator**, so the whole group works in **one shared repository**.

---

### Step 1 · Coordinator: create your group's repository from this template

1. Sign in to GitHub and open **https://github.com/isichei-nnamdi/nsuk-ds-group-project**
2. Click the green **Use this template** button (top-right) → **Create a new repository**.
3. Fill in the form:
   - **Owner:** your own account
   - **Repository name:** `nsuk-ds-group-XX`, where `XX` is your **two-digit group number**, e.g. `nsuk-ds-group-03`
   - **Description:** `NSUK DS Workshop 2026 group project: yam yield in Nasarawa State`
   - **Visibility:** **Public** (recommended: easiest for marking and for sharing as a portfolio piece; the data is synthetic, so there is nothing confidential)
     - If you choose **Private**, you **must** also add `isichei-nnamdi` as a collaborator in Step 2, or we can't mark it.
   - Leave **Include all branches** unticked.
4. Click **Create repository**. After a few seconds you'll see your own copy at `https://github.com/YOUR-USERNAME/nsuk-ds-group-XX`.
5. **Copy this link** and post it in your group chat.

---

### Step 2 · Coordinator: add every member as a collaborator

1. In **your group's repository**, click **⚙️ Settings** (top menu; if you can't see it, click `…` first).
2. In the left menu click **Collaborators** (on newer GitHub: **Collaborators and teams**). GitHub may ask for your password.
3. Click **Add people**, type a member's **GitHub username**, select them, and click **Add … to this repository**.
4. Repeat for **all four** other members. *(Private repo? Also add `isichei-nnamdi`.)*
5. Each member now shows as **Pending invite** until they accept.

> ⏰ **Invitations expire after 7 days.** If someone misses it, remove them and invite them again.

---

### Step 3 · Everyone: accept the invitation and clone the repository

**3a. Accept the invitation.** Check your email for *"… invited you to collaborate"*, or go to **https://github.com/notifications**, or open the repo link the coordinator posted. Click **Accept invitation**. *(The coordinator skips this, because they already own the repo.)*

**3b. Clone (download) the repository in VS Code.**

1. Open **VS Code** → press **Ctrl + Shift + P** (Mac: **Cmd + Shift + P**) → type **Git: Clone** → Enter.
2. Paste your group's repo link (e.g. `https://github.com/coordinator-username/nsuk-ds-group-03.git`) → Enter.
3. Choose a folder to save it in (e.g. **Documents**) → **Select as Repository Destination**.
4. Click **Open** when VS Code asks. If asked *"Do you trust the authors?"*, click **Yes**.

*Prefer the terminal?*
```bash
cd Documents
git clone https://github.com/coordinator-username/nsuk-ds-group-03.git
cd nsuk-ds-group-03
code .
```

> 🔐 The first time you **push**, a window will ask you to sign in to GitHub. Choose **Sign in with your browser** and approve it. This is normal.

---

### Step 4 · Everyone: set up Python on your laptop

Open the VS Code terminal (**View → Terminal**, or **Ctrl + `**). Make sure it's in your project folder (the prompt should end in `nsuk-ds-group-XX`). Then run:

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You'll know it worked when your prompt starts with **`(.venv)`**. Installing takes 2–5 minutes.

> ❗ **"running scripts is disabled on this system"?** Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, type `Y`, then try activating again.
> More fixes are in [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).

**Then open the notebook:** click `notebooks/group_project.ipynb` → top-right **Select Kernel** → **Python Environments** → choose **.venv**. Run the first code cell (Part 0.1). You should see your Python version and no red errors. 🎉

> 🔁 **Every time you come back to the project:** open the folder in VS Code, activate the environment (`.venv\Scripts\Activate.ps1`), and run **`git pull`** before you do anything else.

---

### Step 5 · Everyone: make your first commit (`CONTRIBUTIONS.md`)

This is your practice commit, and it proves that everyone can push. **Do this before Milestone 1.**

1. `git pull` (to get your teammates' rows first).
2. Open **`CONTRIBUTIONS.md`** and fill in **your own row only** (name, GitHub username, role). Save (**Ctrl + S**).
3. In the terminal:
   ```bash
   git add CONTRIBUTIONS.md
   git commit -m "Add <your name> to CONTRIBUTIONS"
   git push
   ```
   *(Or use the **Source Control** panel on the left of VS Code: type the message → **✓ Commit** → **Sync Changes**.)*
4. If `git push` is **rejected** because someone pushed before you, simply run `git pull`, then `git push` again.

✅ **Milestone 1 is done when:** all 5 names appear in `CONTRIBUTIONS.md` on GitHub, each pushed by that member.

---

### Step 6 · Work through the notebook, passing the baton

The notebook is **one file shared by five people**. If two people edit it at the same time, Git can't merge the changes (notebooks are complicated files). So we use a simple rule:

> 🏃 **The baton rule: only ONE person edits `group_project.ipynb` at a time.** When you finish your part, you commit, push, and **hand the baton** to the next person on WhatsApp.

| Order | Who has the baton | Parts | Commit message | Then tell… |
|---|---|---|---|---|
| 1 | Member 1 (Data lead) | 0, 1, 2 | `Parts 1-2: data audit and cleaning` | Member 2 |
| 2 | Member 2 (Visualisation lead) | 3 | `Part 3: exploratory data analysis` | Member 3 |
| 3 | Member 3 (Statistics lead) | 4, 5 | `Parts 4-5: hypothesis tests and regression` | Member 4 |
| 4 | Member 4 (ML lead) | 6 | `Part 6: machine learning model` | Members 2 and 5 |
| 5 | Member 2 (Visualisation lead) | 7 | `Part 7: publication figures and tables` | Member 5 |
| 6 | Member 5 (App lead) | 8, 9 | `Final submission` | Everyone |

**While you wait for the baton, you are NOT idle.** Every member should:
- **Practise ahead in a private copy.** Copy the notebook into `notebooks/scratch/` (e.g. `notebooks/scratch/praise.ipynb`). Files in `scratch/` are **never uploaded** to GitHub, so you can experiment freely, try the exercises for your part, and help teammates with theirs. When you get the baton, `git pull`, then type (or paste) your finished cells into the real notebook.
- **Member 5** can start the Streamlit app (TODOs 1–3 need no model) and the report template straight away, because those are separate files.
- **Everyone** can write their section of `report/GROUP_REPORT.md`, but agree who pushes when, just like with the notebook.

**When you have the baton:**
```bash
git pull                                  # 1. get the latest version FIRST
# 2. open the notebook, click "Run All", then complete your TODOs
# 3. check every ✅ in your part
git add .
git commit -m "Part 3: exploratory data analysis"
git push                                  # 4. upload
# 5. post on WhatsApp: "Part 3 pushed ✅ Member 3, the baton is yours"
```

📖 The full workflow, with what to do if something goes wrong (e.g. a **merge conflict**), is in **[`docs/TEAM_WORKFLOW.md`](docs/TEAM_WORKFLOW.md)**. Please read it once before you start.

#### What each part asks you to do

| Part | You will… | Look for |
|---|---|---|
| **0 Setup** | Check the environment; type your group name and members | `GROUP_NAME`, `TEAM` |
| **1 Audit** | Load the data; count missing values, duplicates, spelling variants, text-numbers, impossible values; find the 2 **leaky** columns; fill in the audit table | `df_raw` |
| **2 Clean** | Drop duplicates; fix LGA names; standardise Yes/No, gender and month; convert text to numbers; turn -999 into missing; remove impossible values; drop rows with no yield; save the clean CSV | `df` |
| **3 EDA** | Histogram of yield; yield by LGA; practices boxplots; correlation heatmap; curved rainfall effect; gender comparison; write your findings; one AI-generated chart | charts |
| **4 Tests** | Welch t-test (staking) with CI and Cohen's *d*; chi-square (cooperative × credit) with Cramér's V; t-test for gender (you write it); optional ANOVA | APA sentences |
| **5 Regression** | Fit a multiple regression; save a tidy coefficient table; check assumptions; add squared terms; explain what happens to the gender gap; AI interpretation, then verify | `ols`, `coef_table` |
| **6 ML** | Choose features without leakage; train/test split; compare 4 models with 5-fold CV; show the leakage trap; final test; feature importance; **save the model** | `models/` |
| **7 Figures** | Table 1 (descriptives); Figure 1 (bar chart with 95% CIs); Figure 2 (coefficient plot); figure checklist | `figures/`, `results/` |
| **8 App** | Run the Streamlit app and complete its TODOs | `app/streamlit_app.py` |
| **9 Finish** | Report, AI statement, contributions, **Restart → Run All**, final push | `report/` |

> 🆘 **Stuck on a TODO?** (1) Read the error's **last line**. (2) Open **💡 Hint**. (3) Open **🔓 Show the answer**, but read it line by line until you could explain it to a classmate. (4) Ask your group. (5) Ask in the workshop WhatsApp group with a **screenshot of the error**.

---

### Step 7 · App lead: complete the Streamlit app

1. Make sure the ML lead has pushed Part 6, then `git pull`. You should now have `models/yam_yield_model.joblib` and `models/model_card.json`.
2. In the terminal (with `.venv` active), from the project folder:
   ```bash
   streamlit run app/streamlit_app.py
   ```
   Your browser opens at `http://localhost:8501`.
3. Open `app/streamlit_app.py` in VS Code. Work through **TODO 1 → TODO 8** in order. Each one has a 💡 hint, usually the exact line to type or uncomment.

   | TODO | What you add | Where it appears |
   |---|---|---|
   | 1 | Your group name | Title |
   | 2 | Member names | Sidebar |
   | 3 | A one-sentence description | Under the title |
   | 4 | `model.predict(...)`: **the actual prediction** | Predict tab |
   | 5 | Show the prediction with `st.metric` | Predict tab |
   | 6 | Expected total harvest (yield × farm size) | Predict tab |
   | 7 | A dropdown (`st.selectbox`) to pick a comparison | Explore tab |
   | 8 | The model's R², MAE and RMSE | About tab |

4. After each TODO: **save** (Ctrl + S) → in the browser click **Rerun** (or press **R**) → check that it works.
5. Take **3 screenshots** (one per tab), save them in `figures/` (e.g. `app_predict.png`) and use them in the report.
6. Stop the app with **Ctrl + C** in the terminal. Commit and push.

⭐ **Stretch (optional, bonus credit):** deploy the app for free. Go to **https://share.streamlit.io** → *Sign in with GitHub* → **Create app** → choose your repo, branch `main`, file `app/streamlit_app.py` → **Deploy**. Paste the link at the top of this README.

---

### Step 8 · Everyone: write the report and the AI-use statement

- **`report/GROUP_REPORT.md`** has a heading and guiding questions for every section. Each member drafts the section for their own part, and Member 5 joins them together and checks the flow. **Target: 1,500–2,500 words** plus figures and tables.
  - Put figures in like this: `![Figure 1: Yam yield by seed source and staking](../figures/fig1_yield_by_seed_and_staking.png)`
  - **Every number in the report must come from your notebook.** Check them!
- **`docs/AI_USE_STATEMENT.md`**: state honestly which AI tools you used, for what, and how you checked the output. Using AI is **allowed**; not declaring it is not.
- **`CONTRIBUTIONS.md`**: each member updates their own row with what they actually did.
- Fill in the **📌 About our project** section at the top of this README.

---

### Step 9 · Coordinator: final checks

Go through this list together on a call before you submit:

- [ ] `git pull` → open the notebook → **Restart** → **Run All**. **No red errors**, and every check is **✅**.
- [ ] `figures/` contains fig1–fig4 (PNG + PDF); `results/` contains table1–table3 (CSV); `models/` contains the model and model card.
- [ ] `streamlit run app/streamlit_app.py` works and all 8 TODOs are done.
- [ ] Every 📝 **Write** cell in the notebook has your own text (no blank `Finding 1:` left).
- [ ] `report/GROUP_REPORT.md` is complete, with figures showing and numbers matching the notebook.
- [ ] `docs/AI_USE_STATEMENT.md` and `CONTRIBUTIONS.md` are filled in.
- [ ] The **📌 About our project** section at the top of this README is filled in.
- [ ] On GitHub, go to **Insights → Contributors**: **every member has commits**.
- [ ] Everything is pushed: `git status` says *"nothing to commit, working tree clean"* and *"Your branch is up to date with 'origin/main'"*.

---

### Step 10 · Coordinator: submit your work

Submission is done **on GitHub**, by opening an *issue* in the **assignment** repository (not your group's repo):

1. Go to **https://github.com/isichei-nnamdi/nsuk-ds-group-project/issues/new/choose**
2. Next to **📦 Group submission**, click **Get started**.
3. Title: **`Group XX submission`** (e.g. `Group 03 submission`).
4. Fill in the form: your **repository link**, your **app link** (if deployed), every member's name and GitHub username, and tick the checklist.
5. Click **Submit new issue**. Then **post the issue link in your group chat** so everyone can see it was submitted.

⏰ **Deadline: Friday 27 November 2026, 11:59 pm (WAT).** We mark the last commit pushed **before the deadline**. Commits after the deadline are ignored unless you agreed an extension with the facilitator.

---

## 6. How you will be marked

| Area | Marks |
|---|---|
| Repository set-up & collaboration (template used, all members collaborate, clear commits) | 15 |
| Data audit & cleaning (Parts 1–2) | 15 |
| Exploratory data analysis (Part 3) | 10 |
| Hypothesis testing (Part 4) | 10 |
| Regression & interpretation (Part 5) | 10 |
| Machine learning & leakage (Part 6) | 15 |
| Publication-ready figures & tables (Part 7) | 5 |
| Streamlit app (Part 8) | 10 |
| Report quality & interpretation | 5 |
| Reproducibility & responsible AI (Run All works; AI statement) | 5 |
| **Total** | **100** |
| ⭐ Bonus: app deployed online, or a well-done stretch exercise | up to +5 |

Full details of what earns full marks are in **[`docs/RUBRIC.md`](docs/RUBRIC.md)**.

> 👥 **Individual contribution matters.** Normally every member gets the group mark. A member with **no commits** and no contribution recorded may receive a lower individual mark.

---

## 7. Rules for using AI

✅ **Allowed and encouraged:** asking AI to explain an error, explain code, suggest a chart, improve your wording, or check your interpretation, as practised in the workshop.

❗ **Your responsibilities:**
- **Verify everything.** AI often gets numbers, signs and units wrong, and overstates causation.
- **Send AI your code, column names or result tables, never the raw data** (good habit for real research data).
- **Never let AI invent references.** Check every citation exists.
- **Declare your use** in `docs/AI_USE_STATEMENT.md`.
- You must be able to **explain any code** in your repository if asked.

---

## 8. Getting help

1. **Hints and answers** inside the notebook (under every TODO).
2. **[`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md)**: Git, VS Code, Python and Streamlit problems and their fixes.
3. **[`docs/TEAM_WORKFLOW.md`](docs/TEAM_WORKFLOW.md)**: pulling, pushing, the baton, and fixing merge conflicts.
4. **Your group**, then the **workshop WhatsApp group**. Always include: what you were doing, a **screenshot of the full error**, and what you have already tried.
5. **Ask the facilitator on GitHub:** open an issue with the **🙋 Ask for help** template at
   https://github.com/isichei-nnamdi/nsuk-ds-group-project/issues/new/choose

---

<sub>Data: synthetic, generated by `scripts/make_yam_data.py` (seed 2611). Notebook generated by `scripts/build_notebook.py`. Workshop: Python for Data Science in Academic Research, Nasarawa State University, Keffi, 30–31 October 2026.</sub>
