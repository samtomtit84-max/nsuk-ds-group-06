# 📊 Marking rubric (100 marks + up to 5 bonus)

We mark the **last commit pushed before the deadline**: we clone your repository, open the notebook, click **Restart → Run All**, run the app, and read the report.

| Area | Marks | Full marks | Half marks | Few or no marks |
|---|---|---|---|---|
| **1. Repository & collaboration** | 15 | Created with *Use this template*, named `nsuk-ds-group-XX`; all 5 members are collaborators and **every member has meaningful commits**; clear commit messages; README top section and `CONTRIBUTIONS.md` complete | Most members commit; some vague messages; README partly filled | One person did all the commits; README not filled; fork or ZIP upload instead of the template |
| **2. Audit & cleaning** (Parts 1–2) | 15 | All TODOs correct with ✅; audit table complete with counts; every problem fixed in code; clean data saved; leaky columns identified | Most steps done; audit table incomplete | Cleaning missing or done by editing the CSV by hand |
| **3. EDA** (Part 3) | 10 | All charts produced and readable; 3–5 specific findings **with numbers**; gender question answered thoughtfully; AI chart tested and checked | Charts done, findings vague ("yield varies") | Charts missing; no written findings |
| **4. Hypothesis tests** (Part 4) | 10 | t-tests and chi-square correct; effect sizes and CIs reported; APA sentences completed; association ≠ causation recognised | Tests run but not reported properly | Tests missing or misinterpreted |
| **5. Regression** (Part 5) | 10 | Model fitted with all required terms; coefficient table saved; assumptions discussed; squared terms compared; gender-gap question answered correctly; AI interpretation **verified and corrected** | Model fitted; little interpretation | Model missing or interpretation wrong (e.g. causal claims) |
| **6. Machine learning** (Part 6) | 15 | No leaky features; proper train/test split; 4 models compared with CV and a baseline; leakage trap explained in your own words; test metrics interpreted in plain words; model saved | Model works but explanation thin | Leaky features used; no baseline; no test set |
| **7. Figures & tables** (Part 7) | 5 | Table 1 and Figures 1–4 saved (PNG + PDF), labelled with units, used in the report with captions | Saved but not used or captioned | Missing |
| **8. Streamlit app** (Part 8) | 10 | Runs without errors; all 8 TODOs done; screenshots in the report | Runs; some TODOs missing | Doesn't run |
| **9. Report** | 5 | Complete, clear, 1,500–2,500 words; numbers match the notebook; limitations discussed (including that the data is synthetic) | Some sections thin | Missing or mostly copied from AI without checking |
| **10. Reproducibility & responsible AI** | 5 | **Restart → Run All** works top to bottom; `AI_USE_STATEMENT.md` is honest and specific | Small errors on Run All; vague AI statement | Notebook doesn't run; no AI statement |
| ⭐ **Bonus** | +5 | App deployed on Streamlit Community Cloud **and/or** a stretch exercise done well (e.g. `src/cleaning.py` function, ANOVA interpreted, extra app tab) | | |

### Individual marks
Normally every member receives the group mark. We look at **GitHub → Insights → Contributors** and at `CONTRIBUTIONS.md`. A member with **no commits and no recorded contribution** may receive a reduced individual mark. If someone in your group isn't responding, tell the facilitator **before** the deadline.

### Academic integrity
Groups may help each other with *errors and concepts*, but each group's notebook, report and app must be its own work. Using the notebook's built-in answers is allowed. **Copying another group's report or interpretation is not.**
