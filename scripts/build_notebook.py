"""
Build the group-project starter notebook from the cell definitions below.

Facilitators only. Run from the repository root:
    python scripts/build_notebook.py                      # -> notebooks/group_project.ipynb (starter)
    python scripts/build_notebook.py --solution OUT.ipynb  # -> a fully completed answer key

Every exercise is written once as (starter code, answer code). The starter
notebook gets the starter code plus a collapsible hint and answer; the
--solution notebook gets the answer code so it can be run top to bottom to
test that every exercise works.
"""

import argparse
from pathlib import Path
from textwrap import dedent

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
STARTER_PATH = ROOT / "notebooks" / "group_project.ipynb"
SOLUTION = False


def _clean(text):
    return dedent(text).strip("\n").rstrip()


def md(text):
    return [nbf.v4.new_markdown_cell(_clean(text))]


def code(text):
    return [nbf.v4.new_code_cell(_clean(text))]


def todo(starter, answer, hint):
    """An exercise: a code cell plus a collapsible hint and answer."""
    cells = code(answer if SOLUTION else starter)
    cells += md(f"""
<details><summary>💡 <b>Hint</b> (click to open)</summary>

{_clean(hint)}

</details>
<details><summary>🔓 <b>Show the answer</b> (try it yourself first!)</summary>

```python
{_clean(answer)}
```

</details>
""")
    return cells


def build():
    cells = []
    add = cells.extend

    # =========================================================================
    # TITLE
    # =========================================================================
    add(md("""
    # 🍠 Group Project: What drives yam yield in Nasarawa State?
    ### NSUK Python for Data Science Workshop 2026 · Group project notebook

    In this project your group will take a **messy survey dataset** all the way to a **working web app**, using every
    skill from the workshop:

    | Part | What you do | Workshop skill | Suggested owner |
    |---|---|---|---|
    | 0 | Set up and introduce your team | VS Code, Python, notebooks | Everyone |
    | 1 | **Audit** the raw data: find every problem | pandas, data audit | Member 1 (Data lead) |
    | 2 | **Clean** the data, one step at a time | pandas, data cleaning | Member 1 (Data lead) |
    | 3 | **Explore** the data with charts | EDA, seaborn | Member 2 (Visualisation lead) |
    | 4 | **Test** hypotheses (t-test, chi-square) | scipy, effect sizes | Member 3 (Statistics lead) |
    | 5 | **Explain** yield with multiple regression | statsmodels | Member 3 (Statistics lead) |
    | 6 | **Predict** yield with machine learning, avoid leakage, save the model | scikit-learn | Member 4 (ML lead) |
    | 7 | Make **publication-ready** figures and tables | matplotlib | Member 2 (Visualisation lead) |
    | 8 | Build the **Streamlit app** | Streamlit | Member 5 (App lead) |
    | 9 | Write up, AI-use statement, reproducibility check | Responsible AI, Git | Member 5 + everyone |

    ### How this notebook works
    - Cells marked **✍️ TODO** are for you to complete. Replace every `____` blank (four underscores) with your code.
    - Under every TODO there is a **💡 Hint** and a **🔓 Show the answer** box. Try first, then open the hint, and only then the answer. **Using the answer is allowed**, but make sure you understand every line, because you will be asked to explain your work.
    - After most TODOs there is a **check cell**. It prints ✅ when you are right, or ❌ with a tip.
    - If you see `NameError: name '____' is not defined`, you still have a blank to fill in.
    - Cells marked **📝 Write** need a few sentences in a Markdown cell (double-click the cell to edit it).
    - Run the cells **in order, from top to bottom**. If things get confusing, use **Restart → Run All**.

    > ⚠️ **The data is synthetic.** It was simulated for teaching and imitates a yam farm survey. It is **not** real
    > data and must not be cited as evidence about real farms. See `data/README.md`.

    > 🤝 **Teamwork rule:** only **one person edits and pushes this notebook at a time** (the "baton"). Read
    > `docs/TEAM_WORKFLOW.md` before you start.
    """))

    # =========================================================================
    # PART 0
    # =========================================================================
    add(md("""
    ---
    ## Part 0 · Setup (everyone)
    ### 0.1 Check your environment
    Select the kernel from your `.venv` (top-right of the notebook: **Select Kernel → Python Environments → .venv**), then run the next cell.
    You should see your Python version and no errors.
    """))
    add(code("""
    import sys
    from pathlib import Path

    # Find the project folder (the one containing src/), so this works from notebooks/,
    # from notebooks/scratch/ or from the project folder itself, then make src/ importable
    ROOT = next(p for p in [Path.cwd(), *Path.cwd().parents] if (p / "src" / "project_tools.py").exists())
    sys.path.insert(0, str(ROOT))

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats
    import statsmodels.formula.api as smf

    from src.project_tools import (RAW_PATH, PROCESSED_PATH, RESULTS_DIR, MODEL_PATH, TARGET, RANDOM_STATE,
                                   check, set_publication_style, save_figure, save_model)

    set_publication_style()
    pd.set_option("display.max_columns", 40)
    RESULTS_DIR.mkdir(exist_ok=True)

    print("Python", sys.version.split()[0], "| pandas", pd.__version__)
    print("Project folder:", ROOT)
    print("Outcome (target) variable:", TARGET)
    """))
    add(md("""
    ### 0.2 ✍️ TODO: Introduce your group
    Fill in your group number and the names of your members with their roles. This is shown in your app later.
    """))
    add(todo(
        starter='''
        GROUP_NAME = "Group ____"          # e.g. "Group 03"

        TEAM = {
            "Member 1 (Data lead)": "____",
            "Member 2 (Visualisation lead)": "____",
            "Member 3 (Statistics lead)": "____",
            "Member 4 (ML lead)": "____",
            "Member 5 (App lead)": "____",
        }
        ''',
        answer='''
        GROUP_NAME = "Group 00"

        TEAM = {
            "Member 1 (Data lead)": "Ada Example",
            "Member 2 (Visualisation lead)": "Bala Example",
            "Member 3 (Statistics lead)": "Chika Example",
            "Member 4 (ML lead)": "Dauda Example",
            "Member 5 (App lead)": "Esther Example",
        }
        ''',
        hint="""
        Here `____` is inside quotes, so it is just text. Replace it with your real group number and names,
        for example `GROUP_NAME = "Group 03"`. Keep the quotes!
        """,
    ))
    add(code("""
    check("Group name filled in", "____" not in GROUP_NAME, "Replace ____ with your group number")
    check("All five members filled in", all("____" not in name for name in TEAM.values()), "Type each member's name")
    """))

    # =========================================================================
    # PART 1
    # =========================================================================
    add(md("""
    ---
    ## Part 1 · Audit the raw data (Member 1)
    > **Golden rule:** never edit the raw file by hand. Every change happens in code, so anyone can repeat it.

    A data audit means *looking for problems before fixing anything*. Write down everything you find, because
    you will fix each problem in Part 2 and report it in your write-up.

    ### 1.1 ✍️ TODO: Load the raw data
    The file path is already stored in the variable `RAW_PATH`. Load it into a DataFrame called `df_raw`.
    """))
    add(todo(
        starter='''
        df_raw = ____
        print(df_raw.shape)
        df_raw.head()
        ''',
        answer='''
        df_raw = pd.read_csv(RAW_PATH)
        print(df_raw.shape)
        df_raw.head()
        ''',
        hint="Use `pd.read_csv(...)` and put `RAW_PATH` inside the brackets.",
    ))
    add(code("""
    check("Raw data loaded: 2,436 rows and 28 columns", df_raw.shape == (2436, 28),
          "Did you use pd.read_csv(RAW_PATH)?")
    """))
    add(md("""
    ### 1.2 What type is each column?
    Run the cells below. Look at the **Dtype** column: numbers should be `float64` or `int64`. Which columns
    *should* be numbers but are stored as text (`object` or `str`)?
    """))
    add(code("df_raw.info()"))
    add(code("df_raw.describe().T.round(2)"))
    add(md("""
    ### 1.3 ✍️ TODO: Missing values
    Count the missing values in each column, from most to least.
    """))
    add(todo(
        starter='''
        missing = df_raw.____.sum().sort_values(ascending=False)
        missing_pct = (missing / len(df_raw) * 100).round(1)

        pd.DataFrame({"n_missing": missing, "percent": missing_pct}).query("n_missing > 0")
        ''',
        answer='''
        missing = df_raw.isna().sum().sort_values(ascending=False)
        missing_pct = (missing / len(df_raw) * 100).round(1)

        pd.DataFrame({"n_missing": missing, "percent": missing_pct}).query("n_missing > 0")
        ''',
        hint="`df.isna()` gives True where a value is missing. `.sum()` then counts the Trues in each column.",
    ))
    add(code("""
    check("Missing values counted", missing.sum() == df_raw.isna().sum().sum(), "Use df_raw.isna().sum()")
    """))
    add(md("""
    ### 1.4 ✍️ TODO: Duplicate rows
    The same farm was sometimes entered twice. Count the rows that are exact copies of an earlier row.
    """))
    add(todo(
        starter='''
        n_duplicates = df_raw.____.sum()
        print("Duplicate rows:", n_duplicates)
        ''',
        answer='''
        n_duplicates = df_raw.duplicated().sum()
        print("Duplicate rows:", n_duplicates)
        ''',
        hint="`df.duplicated()` marks each row that is a copy of an earlier one. Add `.sum()` to count them.",
    ))
    add(code("""check("Duplicates found", n_duplicates == 36, "Use df_raw.duplicated().sum()")"""))
    add(md("""
    ### 1.5 Inconsistent categories
    There are only **13 LGAs** in Nasarawa State. How many different spellings does the data contain?
    """))
    add(code("""
    print("Different LGA spellings:", df_raw["lga"].nunique())
    df_raw["lga"].value_counts()
    """))
    add(md("""
    ✍️ **TODO:** Run the cell below and look at the text columns. Write down every inconsistency you see
    (e.g. `"M"` and `"male"` and `"MALE"` all mean the same thing).
    """))
    add(code("""
    for col in ["gender", "planting_month", "staking", "organic_manure", "intercropped",
                "cooperative_member", "access_to_credit", "seed_source", "soil_type", "pest_disease_level"]:
        print(f"--- {col} ---")
        print(df_raw[col].value_counts(dropna=False).to_dict())
    """))
    add(md("""
    > 💡 `repr()` shows hidden spaces: `" Doma  "` is not the same as `"Doma"` to a computer. Try
    > `print([repr(x) for x in df_raw["lga"].unique()[:20]])`.

    ### 1.6 ✍️ TODO: Numbers stored as text
    `fertilizer_kg_per_ha` and `harvest_revenue_naira` should be numbers. Let's find the values that stop them
    from being numbers. The fertiliser version is done for you. Copy the idea for revenue.
    """))
    add(todo(
        starter='''
        # Fertiliser (done for you): which values can NOT be turned into a number?
        as_number = pd.to_numeric(df_raw["fertilizer_kg_per_ha"], errors="coerce")
        bad_fert = df_raw.loc[as_number.isna() & df_raw["fertilizer_kg_per_ha"].notna(), "fertilizer_kg_per_ha"]
        print("Fertiliser text values:", bad_fert.unique())

        # Revenue: do the same for "harvest_revenue_naira"
        as_number = pd.to_numeric(df_raw["____"], errors="coerce")
        bad_rev = df_raw.loc[as_number.isna() & df_raw["____"].notna(), "____"]
        print("Revenue values that are text:", len(bad_rev))
        print(bad_rev.head(10).tolist())
        ''',
        answer='''
        # Fertiliser (done for you): which values can NOT be turned into a number?
        as_number = pd.to_numeric(df_raw["fertilizer_kg_per_ha"], errors="coerce")
        bad_fert = df_raw.loc[as_number.isna() & df_raw["fertilizer_kg_per_ha"].notna(), "fertilizer_kg_per_ha"]
        print("Fertiliser text values:", bad_fert.unique())

        # Revenue: do the same for "harvest_revenue_naira"
        as_number = pd.to_numeric(df_raw["harvest_revenue_naira"], errors="coerce")
        bad_rev = df_raw.loc[as_number.isna() & df_raw["harvest_revenue_naira"].notna(), "harvest_revenue_naira"]
        print("Revenue values that are text:", len(bad_rev))
        print(bad_rev.head(10).tolist())
        ''',
        hint="""
        Replace each `____` with the column name `harvest_revenue_naira`. `errors="coerce"` turns anything
        that is not a number into NaN, so "was not missing before, but is NaN after converting" = a text problem.
        """,
    ))
    add(code("""check("Revenue text values found", len(bad_rev) > 500, "Use the column harvest_revenue_naira in all three blanks")"""))
    add(md("""
    ### 1.7 ✍️ TODO: Impossible values
    Some values cannot be true: a farmer aged 150, a 260-hectare *smallholder* farm, rainfall of **-999 mm**
    (some enumerators typed -999 for "don't know"). Count them.
    """))
    add(todo(
        starter='''
        print("Age above 90 or below 15:", ((df_raw["farmer_age"] > 90) | (df_raw["farmer_age"] < 15)).sum())
        print("Farm larger than 50 ha:  ", (df_raw["farm_size_ha"] > ____).sum())
        print("Rainfall coded -999:     ", (df_raw["rainfall_mm"] == ____).sum())
        print("Mound density of 0:      ", (df_raw["mound_density_per_ha"] == 0).sum())
        print("Yield of 0 t/ha:         ", (df_raw["yield_t_per_ha"] == 0).sum())
        ''',
        answer='''
        print("Age above 90 or below 15:", ((df_raw["farmer_age"] > 90) | (df_raw["farmer_age"] < 15)).sum())
        print("Farm larger than 50 ha:  ", (df_raw["farm_size_ha"] > 50).sum())
        print("Rainfall coded -999:     ", (df_raw["rainfall_mm"] == -999).sum())
        print("Mound density of 0:      ", (df_raw["mound_density_per_ha"] == 0).sum())
        print("Yield of 0 t/ha:         ", (df_raw["yield_t_per_ha"] == 0).sum())
        ''',
        hint="The first blank is the number `50`, the second is `-999`. A comparison gives True/False, and `.sum()` counts the Trues.",
    ))
    add(md("""
    ### 1.8 ⚠️ Leaky columns: think before you model
    Two columns are only known **after** the harvest:
    - `harvest_revenue_naira`: money from selling the harvest (calculated from yield × farm size × price)
    - `tubers_harvested_per_ha`: number of tubers dug up

    If you want to **predict** yield before harvest, these columns would be "cheating". Remember this for Part 6.

    ### 1.9 📝 Write: your audit summary
    Double-click this cell and complete the table. You will reuse it in your report.

    | Problem | Columns affected | How many rows? | How we will fix it |
    |---|---|---|---|
    | Duplicate rows | all | | drop them |
    | Inconsistent spelling / spaces | lga | | |
    | Yes/No written many ways | | | |
    | Male/Female written many ways | gender | | |
    | Month written many ways | planting_month | | |
    | Numbers stored as text | | | |
    | -999 used as a missing code | rainfall_mm | | |
    | Impossible values | | | |
    | Missing values | | | leave for the model pipeline to fill (Part 6) |
    | Leaky columns | | | never use as model features |
    """))

    # =========================================================================
    # PART 2
    # =========================================================================
    add(md("""
    ---
    ## Part 2 · Clean the data (Member 1)
    We fix problems **one at a time** on a copy called `df`, and check each step. `df_raw` is never changed.

    > 🧠 **We do NOT fill in (impute) missing values here.** Filling them using the whole dataset would leak
    > information from the test set. The model pipeline fills them in Part 6, using the training data only.
    """))
    add(code("""
    df = df_raw.copy()
    df.columns = df.columns.str.strip().str.lower()   # tidy column names, just in case
    print("Starting with", df.shape)
    """))
    add(md("### 2.1 ✍️ TODO: Remove duplicate rows"))
    add(todo(
        starter='''
        df = df.____
        print(df.shape)
        ''',
        answer='''
        df = df.drop_duplicates()
        print(df.shape)
        ''',
        hint="The method is `drop_duplicates()`. Do not forget the brackets `()`.",
    ))
    add(code("""check("Duplicates removed: 2,400 rows left", len(df) == 2400 and df.duplicated().sum() == 0, "Use df.drop_duplicates()")"""))
    add(md("""
    ### 2.2 ✍️ TODO: Fix the LGA names
    Three things are wrong: extra spaces, wrong capital letters and spelling variants. `.str.strip()` removes
    spaces, `.str.title()` makes `"doma"` into `"Doma"`, and `.replace(...)` fixes the spellings.
    Complete the dictionary of spelling fixes using what you found in 1.5.
    """))
    add(todo(
        starter='''
        LGA_FIXES = {
            "Nasarawa-Eggon": "Nasarawa Eggon",
            "N/Eggon": "____",
            "Nassarawa": "____",
            "____": "Akwanga",
        }

        df["lga"] = df["lga"].str.strip().str.title().replace(LGA_FIXES)
        print(df["lga"].nunique(), "LGAs")
        df["lga"].value_counts()
        ''',
        answer='''
        LGA_FIXES = {
            "Nasarawa-Eggon": "Nasarawa Eggon",
            "N/Eggon": "Nasarawa Eggon",
            "Nassarawa": "Nasarawa",
            "Akwaga": "Akwanga",
        }

        df["lga"] = df["lga"].str.strip().str.title().replace(LGA_FIXES)
        print(df["lga"].nunique(), "LGAs")
        df["lga"].value_counts()
        ''',
        hint="""
        The dictionary reads `"wrong spelling": "correct spelling"`. Look at the value counts from 1.5:
        which LGA is misspelled as **Akwaga**?
        """,
    ))
    add(code("""
    OFFICIAL_LGAS = {"Akwanga", "Awe", "Doma", "Karu", "Keana", "Keffi", "Kokona", "Lafia",
                     "Nasarawa", "Nasarawa Eggon", "Obi", "Toto", "Wamba"}
    check("Exactly the 13 official LGAs", set(df["lga"]) == OFFICIAL_LGAS,
          f"Still wrong: {set(df['lga']) - OFFICIAL_LGAS}")
    """))
    add(md("""
    ### 2.3 ✍️ TODO: Standardise the Yes/No columns
    Turn `"Y"`, `"yes "`, `"YES"`... into `"Yes"`, and `"N"`, `" no"`, `"NO"`... into `"No"`.
    The trick: strip spaces and make everything lowercase **first**, so you only need four entries in the dictionary.
    """))
    add(todo(
        starter='''
        YES_NO_COLUMNS = ["staking", "organic_manure", "intercropped", "cooperative_member", "access_to_credit"]
        YES_NO_MAP = {"yes": "Yes", "y": "Yes", "____": "No", "____": "No"}

        for col in YES_NO_COLUMNS:
            df[col] = df[col].str.strip().str.lower().map(YES_NO_MAP)

        df[YES_NO_COLUMNS].apply(pd.Series.value_counts)
        ''',
        answer='''
        YES_NO_COLUMNS = ["staking", "organic_manure", "intercropped", "cooperative_member", "access_to_credit"]
        YES_NO_MAP = {"yes": "Yes", "y": "Yes", "no": "No", "n": "No"}

        for col in YES_NO_COLUMNS:
            df[col] = df[col].str.strip().str.lower().map(YES_NO_MAP)

        df[YES_NO_COLUMNS].apply(pd.Series.value_counts)
        ''',
        hint="After `.str.lower()`, the 'No' variants are `\"no\"` and `\"n\"`.",
    ))
    add(code("""
    check("Yes/No columns contain only 'Yes' and 'No'",
          all(set(df[c].unique()) == {"Yes", "No"} for c in YES_NO_COLUMNS),
          "Did any value turn into NaN? Then a spelling is missing from YES_NO_MAP")
    """))
    add(md("### 2.4 ✍️ TODO: Standardise gender\nUse exactly the same idea as 2.3. This time *you* write the whole dictionary."))
    add(todo(
        starter='''
        GENDER_MAP = {____}

        df["gender"] = df["gender"].str.strip().str.lower().map(GENDER_MAP)
        df["gender"].value_counts(dropna=False)
        ''',
        answer='''
        GENDER_MAP = {"male": "Male", "m": "Male", "female": "Female", "f": "Female"}

        df["gender"] = df["gender"].str.strip().str.lower().map(GENDER_MAP)
        df["gender"].value_counts(dropna=False)
        ''',
        hint='You need four entries: `"male"`, `"m"`, `"female"` and `"f"`. Each maps to `"Male"` or `"Female"`.',
    ))
    add(code("""check("Gender is only 'Male' or 'Female'", set(df["gender"].unique()) == {"Male", "Female"}, "Check GENDER_MAP")"""))
    add(md("""
    ### 2.5 ✍️ TODO: Standardise the planting month
    The months appear as `"February"`, `"Feb"`, `"feb"` and even `"02"`. A neat trick: lowercase, then keep only
    the **first three characters** (`.str[:3]`). Then `"February"`, `"Feb"` and `"feb"` all become `"feb"`.
    """))
    add(todo(
        starter='''
        MONTH_MAP = {
            "dec": "December", "12": "December",
            "jan": "January",  "01": "January",
            "feb": "February", "02": "February",
            "mar": "March",    "03": "March",
            "apr": "April",    "04": "April",
        }

        df["planting_month"] = df["planting_month"].astype(str).str.strip().str.lower().str[:____].map(MONTH_MAP)
        df["planting_month"].value_counts(dropna=False)
        ''',
        answer='''
        MONTH_MAP = {
            "dec": "December", "12": "December",
            "jan": "January",  "01": "January",
            "feb": "February", "02": "February",
            "mar": "March",    "03": "March",
            "apr": "April",    "04": "April",
        }

        df["planting_month"] = df["planting_month"].astype(str).str.strip().str.lower().str[:3].map(MONTH_MAP)
        df["planting_month"].value_counts(dropna=False)
        ''',
        hint="`.str[:3]` keeps the first 3 characters. So the blank is the number `3`.",
    ))
    add(code("""
    check("Planting month has the 5 full month names",
          set(df["planting_month"].unique()) == {"December", "January", "February", "March", "April"},
          "Check the number inside .str[:____]")
    """))
    add(md("""
    ### 2.6 ✍️ TODO: Turn text into numbers
    - **Fertiliser:** `pd.to_numeric(..., errors="coerce")` turns `"not recorded"`, `"nil"` and `"-"` into NaN.
    - **Revenue:** first remove `N`, `₦` and commas with `.str.replace(...)`, then convert.
    - **Rainfall:** replace the code `-999` with `np.nan` (a proper missing value).
    """))
    add(todo(
        starter='''
        df["fertilizer_kg_per_ha"] = pd.to_numeric(df["fertilizer_kg_per_ha"], errors="____")

        df["harvest_revenue_naira"] = pd.to_numeric(
            df["harvest_revenue_naira"].astype(str).str.replace(r"[N₦,]", "", regex=True),
            errors="coerce",
        )

        df["rainfall_mm"] = df["rainfall_mm"].replace(____, np.nan)

        df[["fertilizer_kg_per_ha", "harvest_revenue_naira", "rainfall_mm"]].describe().round(1)
        ''',
        answer='''
        df["fertilizer_kg_per_ha"] = pd.to_numeric(df["fertilizer_kg_per_ha"], errors="coerce")

        df["harvest_revenue_naira"] = pd.to_numeric(
            df["harvest_revenue_naira"].astype(str).str.replace(r"[N₦,]", "", regex=True),
            errors="coerce",
        )

        df["rainfall_mm"] = df["rainfall_mm"].replace(-999, np.nan)

        df[["fertilizer_kg_per_ha", "harvest_revenue_naira", "rainfall_mm"]].describe().round(1)
        ''',
        hint="""
        The first blank is the word `coerce` (it is already in quotes). The second blank is the number `-999`.
        `r"[N₦,]"` is a *regular expression* meaning "any one of the characters N, ₦ or comma".
        """,
    ))
    add(code("""
    check("Fertiliser is numeric", pd.api.types.is_numeric_dtype(df["fertilizer_kg_per_ha"]), "Use pd.to_numeric(..., errors='coerce')")
    check("Revenue is numeric", pd.api.types.is_numeric_dtype(df["harvest_revenue_naira"]), "Run the revenue lines")
    check("No more -999 rainfall", (df["rainfall_mm"] == -999).sum() == 0, "Use .replace(-999, np.nan)")
    """))
    add(md("""
    ### 2.7 ✍️ TODO: Remove impossible values
    We decide on a **valid range** for some columns, and set anything outside it to missing (NaN).
    Add a valid range for yield: anything below **0.5 t/ha** or above **40 t/ha** is a data-entry error.
    """))
    add(todo(
        starter='''
        VALID_RANGES = {
            "farmer_age": (15, 90),
            "farm_size_ha": (0.05, 50),
            "mound_density_per_ha": (2000, 25000),
            "yield_t_per_ha": (____, ____),
        }

        for col, (low, high) in VALID_RANGES.items():
            outside = ~df[col].between(low, high) & df[col].notna()
            print(f"{col}: {outside.sum()} impossible values set to NaN")
            df.loc[outside, col] = np.nan
        ''',
        answer='''
        VALID_RANGES = {
            "farmer_age": (15, 90),
            "farm_size_ha": (0.05, 50),
            "mound_density_per_ha": (2000, 25000),
            "yield_t_per_ha": (0.5, 40),
        }

        for col, (low, high) in VALID_RANGES.items():
            outside = ~df[col].between(low, high) & df[col].notna()
            print(f"{col}: {outside.sum()} impossible values set to NaN")
            df.loc[outside, col] = np.nan
        ''',
        hint="Write the two numbers: `(0.5, 40)`. `~` means NOT, so `~df[col].between(low, high)` means *outside* the range.",
    ))
    add(code("""
    check("Ages are all between 15 and 90", df["farmer_age"].dropna().between(15, 90).all(), "Run the loop above")
    check("Yields of 0 removed", (df["yield_t_per_ha"] == 0).sum() == 0, "Did you add the yield range (0.5, 40)?")
    """))
    add(md("""
    ### 2.8 ✍️ TODO: Drop rows with no outcome
    A farm without a yield value cannot be used to study yield. Drop those rows (only those!).
    """))
    add(todo(
        starter='''
        df = df.dropna(subset=[____]).reset_index(drop=True)
        print("Final clean data:", df.shape)
        ''',
        answer='''
        df = df.dropna(subset=[TARGET]).reset_index(drop=True)
        print("Final clean data:", df.shape)
        ''',
        hint="The outcome column name is stored in the variable `TARGET` (no quotes needed).",
    ))
    add(code("""
    check("No missing yields", df[TARGET].notna().all(), "Use df.dropna(subset=[TARGET])")
    check("About 2,360 farms left", 2300 < len(df) < 2400, "Drop ONLY rows where the yield is missing")
    """))
    add(md("### 2.9 Before and after, then save the clean data"))
    add(code("""
    before_after = pd.DataFrame({
        "raw": [len(df_raw), df_raw["lga"].nunique(), df_raw["gender"].nunique(), df_raw["planting_month"].nunique(),
                df_raw["fertilizer_kg_per_ha"].dtype, int(df_raw.duplicated().sum())],
        "clean": [len(df), df["lga"].nunique(), df["gender"].nunique(), df["planting_month"].nunique(),
                  df["fertilizer_kg_per_ha"].dtype, int(df.duplicated().sum())],
    }, index=["rows", "LGA spellings", "gender spellings", "month spellings", "fertiliser dtype", "duplicates"])
    display(before_after)

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print("Saved clean data to", PROCESSED_PATH.relative_to(ROOT))
    """))
    add(md("""
    > ⭐ **Stretch (optional):** move all the cleaning steps into one function `clean_yam_data(df_raw)` inside a
    > new file `src/cleaning.py`, like we did in the workshop. Then `df = clean_yam_data(df_raw)` repeats all of
    > Part 2 in one line. Ask your AI assistant to help, then check that the result is identical:
    > `clean_yam_data(df_raw).equals(df)`.

    ### 💾 Member 1: commit and pass the baton
    ```bash
    git add .
    git commit -m "Parts 1-2: data audit and cleaning"
    git push
    ```
    Then tell your group on WhatsApp: *"Parts 1–2 pushed. Member 2, you have the notebook."*
    """))

    # =========================================================================
    # PART 3
    # =========================================================================
    add(md("""
    ---
    ## Part 3 · Exploratory data analysis (Member 2)
    > Start by pulling your teammate's work: `git pull`. Then run all the cells above (**Run All**).

    EDA means *looking* at the data before testing anything. Every chart should answer a question.
    ### 3.1 ✍️ TODO: What does the outcome look like?
    """))
    add(todo(
        starter='''
        print(df[TARGET].describe().round(2))

        fig, ax = plt.subplots()
        sns.histplot(____, bins=40, kde=True, ax=ax)
        ax.set(xlabel="Yam yield (t/ha)", ylabel="Number of farms", title="Distribution of yam yield")
        plt.show()
        ''',
        answer='''
        print(df[TARGET].describe().round(2))

        fig, ax = plt.subplots()
        sns.histplot(df[TARGET], bins=40, kde=True, ax=ax)
        ax.set(xlabel="Yam yield (t/ha)", ylabel="Number of farms", title="Distribution of yam yield")
        plt.show()
        ''',
        hint="Give `sns.histplot` the yield column: `df[TARGET]`.",
    ))
    add(md("""
    📝 *Is the distribution roughly symmetric? Are there outliers? What is a "typical" yield?*

    ### 3.2 ✍️ TODO: Yield across LGAs
    Make a summary table of yield for each LGA: number of farms, mean, median and standard deviation.
    """))
    add(todo(
        starter='''
        lga_summary = (df.groupby("____")[TARGET]
                         .agg(["count", "mean", "median", "std"])
                         .sort_values("mean", ascending=False)
                         .round(2))
        lga_summary
        ''',
        answer='''
        lga_summary = (df.groupby("lga")[TARGET]
                         .agg(["count", "mean", "median", "std"])
                         .sort_values("mean", ascending=False)
                         .round(2))
        lga_summary
        ''',
        hint='Group by the LGA column: `df.groupby("lga")`.',
    ))
    add(code("""check("One row per LGA", len(lga_summary) == 13, 'Group by "lga"')"""))
    add(code("""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    sns.boxplot(data=df, x="lga", y=TARGET, order=lga_summary.index, color="#56B4E9", ax=ax)
    ax.set(xlabel="", ylabel="Yield (t/ha)", title="Yam yield by LGA (sorted by mean)")
    ax.tick_params(axis="x", rotation=45)
    plt.show()
    """))
    add(md("""
    ### 3.3 ✍️ TODO: Farm practices
    Which practices go with higher yields? First compare the mean yield of farms that **stake** their yam vines
    with those that do not.
    """))
    add(todo(
        starter='''
        staking_means = df.groupby("____")[TARGET].mean().round(2)
        staking_means
        ''',
        answer='''
        staking_means = df.groupby("staking")[TARGET].mean().round(2)
        staking_means
        ''',
        hint='Group by `"staking"` and take the `.mean()` of the yield.',
    ))
    add(code("""check("Staked farms have a higher mean yield", staking_means["Yes"] > staking_means["No"], 'Group by "staking"')"""))
    add(md("Now look at six practices at once. This cell is complete, just run it and study the plots."))
    add(code("""
    practices = {
        "staking": ["No", "Yes"],
        "seed_source": ["Own saved setts", "Local market", "ADP / NGO", "Certified seed yam"],
        "organic_manure": ["No", "Yes"],
        "intercropped": ["No", "Yes"],
        "pest_disease_level": ["Absent", "Low", "Moderate", "High"],
        "planting_month": ["December", "January", "February", "March", "April"],
    }
    fig, axes = plt.subplots(2, 3, figsize=(13, 7.5))
    for ax, (col, order) in zip(axes.flat, practices.items()):
        sns.boxplot(data=df, x=col, y=TARGET, order=order, color="#56B4E9", ax=ax)
        ax.set(title=col.replace("_", " ").capitalize(), xlabel="", ylabel="Yield (t/ha)")
        ax.tick_params(axis="x", rotation=30)
    plt.tight_layout()
    plt.show()
    """))
    add(md("### 3.4 ✍️ TODO: Correlations between numeric variables"))
    add(todo(
        starter='''
        numeric_cols = ["yield_t_per_ha", "fertilizer_kg_per_ha", "rainfall_mm", "mound_density_per_ha",
                        "sett_weight_g", "weeding_count", "extension_visits", "years_farming",
                        "farm_size_ha", "distance_to_market_km", "tubers_harvested_per_ha"]

        corr = df[numeric_cols].____()

        fig, ax = plt.subplots(figsize=(8, 6.5))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0, vmin=-1, vmax=1, ax=ax)
        ax.set_title("Correlation between numeric variables")
        plt.show()
        ''',
        answer='''
        numeric_cols = ["yield_t_per_ha", "fertilizer_kg_per_ha", "rainfall_mm", "mound_density_per_ha",
                        "sett_weight_g", "weeding_count", "extension_visits", "years_farming",
                        "farm_size_ha", "distance_to_market_km", "tubers_harvested_per_ha"]

        corr = df[numeric_cols].corr()

        fig, ax = plt.subplots(figsize=(8, 6.5))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0, vmin=-1, vmax=1, ax=ax)
        ax.set_title("Correlation between numeric variables")
        plt.show()
        ''',
        hint="The method that computes correlations is `.corr()`.",
    ))
    add(md("""
    👀 Look at `tubers_harvested_per_ha`: its correlation with yield is very high. Why? (Hint: Part 1.8.)

    Rainfall shows almost **no correlation** with yield. Does that mean rain does not matter? Run the next cell.
    """))
    add(code("""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    sns.regplot(data=df, x="fertilizer_kg_per_ha", y=TARGET, lowess=True, ax=axes[0],
                scatter_kws={"alpha": 0.2, "s": 10}, line_kws={"color": "#D55E00"})
    sns.regplot(data=df, x="rainfall_mm", y=TARGET, lowess=True, ax=axes[1],
                scatter_kws={"alpha": 0.2, "s": 10}, line_kws={"color": "#D55E00"})
    axes[0].set(xlabel="Fertiliser (kg/ha)", ylabel="Yield (t/ha)", title="Yield vs fertiliser")
    axes[1].set(xlabel="Rainfall (mm)", ylabel="Yield (t/ha)", title="Yield vs rainfall")
    plt.tight_layout()
    plt.show()
    """))
    add(md("""
    💡 Correlation only measures **straight-line** relationships. Rainfall has a **curved** (hill-shaped)
    relationship: too little *and* too much rain both reduce yield. Keep this in mind for Part 5.

    ### 3.5 ✍️ TODO: Do men and women get different yields?
    Compare mean yield, farm size, fertiliser and extension visits by gender, and the share with access to credit.
    """))
    add(todo(
        starter='''
        by_gender = df.groupby("____")[[TARGET, "farm_size_ha", "fertilizer_kg_per_ha", "extension_visits"]].mean().round(2)
        display(by_gender)

        # Share of each gender with access to credit, staking, and cooperative membership (rows add to 100%)
        for col in ["access_to_credit", "staking", "cooperative_member"]:
            display((pd.crosstab(df["gender"], df[col], normalize="index") * 100).round(1))
        ''',
        answer='''
        by_gender = df.groupby("gender")[[TARGET, "farm_size_ha", "fertilizer_kg_per_ha", "extension_visits"]].mean().round(2)
        display(by_gender)

        # Share of each gender with access to credit, staking, and cooperative membership (rows add to 100%)
        for col in ["access_to_credit", "staking", "cooperative_member"]:
            display((pd.crosstab(df["gender"], df[col], normalize="index") * 100).round(1))
        ''',
        hint='Group by `"gender"`.',
    ))
    add(md("""
    📝 **Write:** women in this survey get slightly lower yields. Looking at the tables above, can you think of
    a reason that is **not** about gender itself? (We will test this idea with regression in Part 5.)

    ### 3.6 📝 Write: your key EDA findings
    Double-click and write **3 to 5 bullet points** describing what you found. Use numbers.
    - Finding 1:
    - Finding 2:
    - Finding 3:

    ### 3.7 🤖 AI exercise: one more chart
    Ask your AI assistant (ChatGPT, Gemini, Copilot, Claude...):
    > *"I have a pandas DataFrame `df` with columns `lga`, `staking` (Yes/No) and `yield_t_per_ha`. Write seaborn
    > code for a bar chart of mean yield by LGA, with bars split by staking, sorted by overall mean yield."*

    Paste the code below and run it. ✅ **Check:** do the numbers on the chart match `lga_summary`? Do you
    understand every line? Only send the AI your **column names**, never your data.
    """))
    add(code("# 🤖 Paste and test the AI-generated code here\n"))
    add(md("""
    ### 💾 Member 2: commit and pass the baton
    `git add .` → `git commit -m "Part 3: exploratory data analysis"` → `git push` → tell Member 3 on WhatsApp.
    """))

    # =========================================================================
    # PART 4
    # =========================================================================
    add(md("""
    ---
    ## Part 4 · Hypothesis testing (Member 3)
    > `git pull` first, then **Run All**.

    ### 4.1 Research question and hypotheses
    > **RQ:** Which farm practices are associated with higher yam yield among smallholder farmers in Nasarawa State?
    >
    > **H1:** Farms that stake their yam vines have a higher mean yield than farms that do not.
    >
    > **H2:** Cooperative members are more likely to have access to credit.
    >
    > **H3:** Mean yield differs between male and female farmers.

    ### 4.2 ✍️ TODO: H1, Welch's t-test (staking)
    Welch's t-test compares two means without assuming the groups have equal variances. We also report the
    **difference**, its **95% confidence interval** and **Cohen's d** (effect size), because reviewers want to
    know *how big* the effect is, not just whether *p* < 0.05.
    """))
    add(todo(
        starter='''
        staked = df.loc[df["staking"] == "Yes", TARGET]
        not_staked = df.loc[df["staking"] == "____", TARGET]

        t, p = stats.ttest_ind(____, ____, equal_var=False)       # Welch's t-test

        diff = staked.mean() - not_staked.mean()
        se = np.sqrt(staked.var() / len(staked) + not_staked.var() / len(not_staked))
        ci_low, ci_high = diff - 1.96 * se, diff + 1.96 * se
        cohens_d = diff / np.sqrt((staked.var() + not_staked.var()) / 2)

        print(f"Staked:     n = {len(staked)}, mean = {staked.mean():.2f} t/ha")
        print(f"Not staked: n = {len(not_staked)}, mean = {not_staked.mean():.2f} t/ha")
        print(f"Difference = {diff:.2f} t/ha (95% CI {ci_low:.2f} to {ci_high:.2f}), "
              f"Welch t = {t:.2f}, p = {p:.3g}, Cohen's d = {cohens_d:.2f}")
        ''',
        answer='''
        staked = df.loc[df["staking"] == "Yes", TARGET]
        not_staked = df.loc[df["staking"] == "No", TARGET]

        t, p = stats.ttest_ind(staked, not_staked, equal_var=False)       # Welch's t-test

        diff = staked.mean() - not_staked.mean()
        se = np.sqrt(staked.var() / len(staked) + not_staked.var() / len(not_staked))
        ci_low, ci_high = diff - 1.96 * se, diff + 1.96 * se
        cohens_d = diff / np.sqrt((staked.var() + not_staked.var()) / 2)

        print(f"Staked:     n = {len(staked)}, mean = {staked.mean():.2f} t/ha")
        print(f"Not staked: n = {len(not_staked)}, mean = {not_staked.mean():.2f} t/ha")
        print(f"Difference = {diff:.2f} t/ha (95% CI {ci_low:.2f} to {ci_high:.2f}), "
              f"Welch t = {t:.2f}, p = {p:.3g}, Cohen's d = {cohens_d:.2f}")
        ''',
        hint='The second group is `"No"`. The t-test compares the two groups: `stats.ttest_ind(staked, not_staked, equal_var=False)`.',
    ))
    add(code("""check("t-test done and staking is significant", p < 0.05 and diff > 0, "Compare staked with not_staked")"""))
    add(md("""
    **📝 Report it in APA style** (fill in the numbers from the output):
    > Farms that staked their vines had a higher mean yield than farms that did not (difference = *__* t/ha,
    > 95% CI [*__*, *__*]), Welch's *t* = *__*, *p* *__*, Cohen's *d* = *__*.

    Cohen's *d*: about 0.2 is small, 0.5 medium, 0.8 large.

    ### 4.3 ✍️ TODO: H2, chi-square test of independence
    Both variables are **categorical** (Yes/No), so we use a chi-square test on a cross-table.
    **Cramér's V** is the effect size (0 = no association, 1 = perfect).
    """))
    add(todo(
        starter='''
        table = pd.crosstab(df["cooperative_member"], df["____"])
        display(table)
        display((pd.crosstab(df["cooperative_member"], df["access_to_credit"], normalize="index") * 100).round(1))

        chi2, p_chi, dof, expected = stats.chi2_contingency(____)
        cramers_v = np.sqrt(chi2 / (table.values.sum() * (min(table.shape) - 1)))

        print(f"chi2({dof}) = {chi2:.2f}, p = {p_chi:.3g}, Cramér's V = {cramers_v:.2f}")
        ''',
        answer='''
        table = pd.crosstab(df["cooperative_member"], df["access_to_credit"])
        display(table)
        display((pd.crosstab(df["cooperative_member"], df["access_to_credit"], normalize="index") * 100).round(1))

        chi2, p_chi, dof, expected = stats.chi2_contingency(table)
        cramers_v = np.sqrt(chi2 / (table.values.sum() * (min(table.shape) - 1)))

        print(f"chi2({dof}) = {chi2:.2f}, p = {p_chi:.3g}, Cramér's V = {cramers_v:.2f}")
        ''',
        hint='The second column is `"access_to_credit"`. Then give the cross-table `table` to `stats.chi2_contingency(...)`.',
    ))
    add(code("""check("Chi-square test done", p_chi < 0.05, "Pass the cross-table to stats.chi2_contingency")"""))
    add(md("""
    ### 4.4 ✍️ TODO: H3, gender. Now you write it!
    Copy the t-test from 4.2 and change it to compare **male** and **female** farmers. Name your p-value `p_gender`
    and the difference `diff_gender` (male minus female).
    """))
    add(todo(
        starter='''
        male = ____
        female = ____

        t_gender, p_gender = ____
        diff_gender = ____

        print(f"Male mean = {male.mean():.2f}, female mean = {female.mean():.2f}, "
              f"difference = {diff_gender:.2f} t/ha, t = {t_gender:.2f}, p = {p_gender:.3g}")
        ''',
        answer='''
        male = df.loc[df["gender"] == "Male", TARGET]
        female = df.loc[df["gender"] == "Female", TARGET]

        t_gender, p_gender = stats.ttest_ind(male, female, equal_var=False)
        diff_gender = male.mean() - female.mean()

        print(f"Male mean = {male.mean():.2f}, female mean = {female.mean():.2f}, "
              f"difference = {diff_gender:.2f} t/ha, t = {t_gender:.2f}, p = {p_gender:.3g}")
        ''',
        hint="""
        Follow 4.2 exactly, but use the `gender` column with `"Male"` and `"Female"`.
        `male = df.loc[df["gender"] == "Male", TARGET]`
        """,
    ))
    add(code("""check("Gender t-test done", 0 < p_gender < 0.05 and diff_gender > 0, "Compare male and female yields with stats.ttest_ind")"""))
    add(md("""
    ⚠️ **Association is not causation.** The t-test says women's yields are slightly lower *on average*. It does
    **not** say why. In Part 3.5 you saw that women have less access to credit, staking and extension. Part 5
    checks whether the gap remains after we account for those.

    ### 4.5 ⭐ Stretch (optional): more than two groups, one-way ANOVA
    Does mean yield differ between the four **seed sources**? With more than two groups, use ANOVA.
    """))
    add(code("""
    groups = [g[TARGET].values for _, g in df.groupby("seed_source")]
    f_stat, p_anova = stats.f_oneway(*groups)
    print(f"One-way ANOVA: F = {f_stat:.2f}, p = {p_anova:.3g}")
    df.groupby("seed_source")[TARGET].agg(["count", "mean", "std"]).round(2).sort_values("mean")
    """))

    # =========================================================================
    # PART 5
    # =========================================================================
    add(md("""
    ---
    ## Part 5 · Multiple regression: *explaining* yield (Member 3)
    A t-test looks at one factor at a time. **Multiple regression** estimates the effect of each factor
    *while holding the others constant*. We use `statsmodels`, which gives a full table for your thesis.

    In the formula, `C(column, Treatment('X'))` means "this is a category, compare every level with `X`".

    ### 5.1 ✍️ TODO: Fit the model
    The formula has most terms already. **Add three more:** seed source (reference `'Own saved setts'`),
    pest/disease level (reference `'Absent'`) and gender (reference `'Male'`).
    """))
    add(todo(
        starter='''
        formula = (
            "yield_t_per_ha ~ fertilizer_kg_per_ha + rainfall_mm + mound_density_per_ha + sett_weight_g"
            " + weeding_count + extension_visits"
            " + C(staking, Treatment('No')) + C(organic_manure, Treatment('No')) + C(intercropped, Treatment('No'))"
            " + C(planting_month, Treatment('March')) + C(soil_type, Treatment('Clay loam'))"
            " + C(access_to_credit, Treatment('No'))"
            # TODO: add seed_source, pest_disease_level and gender on the next lines, e.g.
            # " + C(seed_source, Treatment('Own saved setts'))"
            ____
        )
        ols = smf.ols(formula, data=df).fit()
        print(f"Rows used: {int(ols.nobs)} of {len(df)} (rows with any missing value are dropped, so report this!)")
        ols.summary()
        ''',
        answer='''
        formula = (
            "yield_t_per_ha ~ fertilizer_kg_per_ha + rainfall_mm + mound_density_per_ha + sett_weight_g"
            " + weeding_count + extension_visits"
            " + C(staking, Treatment('No')) + C(organic_manure, Treatment('No')) + C(intercropped, Treatment('No'))"
            " + C(planting_month, Treatment('March')) + C(soil_type, Treatment('Clay loam'))"
            " + C(access_to_credit, Treatment('No'))"
            " + C(seed_source, Treatment('Own saved setts'))"
            " + C(pest_disease_level, Treatment('Absent'))"
            " + C(gender, Treatment('Male'))"
        )
        ols = smf.ols(formula, data=df).fit()
        print(f"Rows used: {int(ols.nobs)} of {len(df)} (rows with any missing value are dropped, so report this!)")
        ols.summary()
        ''',
        hint="""
        Replace `____` with three lines of text, each starting with a space and a plus sign, for example:

            " + C(seed_source, Treatment('Own saved setts'))"
            " + C(pest_disease_level, Treatment('Absent'))"
            " + C(gender, Treatment('Male'))"

        Python joins strings that sit next to each other inside brackets, so no `+` is needed *between* the strings.
        """,
    ))
    add(code("""
    check("Formula includes seed source, pest level and gender",
          all(term in formula for term in ["C(seed_source", "C(pest_disease_level", "C(gender"]),
          "Add the three C(...) terms")
    check("Model explains a good share of the variation (R² > 0.4)", ols.rsquared > 0.4, "Did the model fit?")
    """))
    add(md("""
    **How to read the table:** each `coef` is the change in yield (t/ha) for a one-unit change in that variable,
    holding the others constant. For categories, it is the difference from the reference level. `P>|t|` is the
    p-value, and `[0.025 0.975]` is the 95% confidence interval.

    ### 5.2 ✍️ TODO: A tidy coefficient table for your report
    """))
    add(todo(
        starter='''
        coef_table = pd.DataFrame({
            "coef": ols.params,
            "ci_low": ols.conf_int()[0],
            "ci_high": ols.conf_int()[1],
            "p_value": ols.pvalues,
        }).round(3)

        coef_table.to_csv(RESULTS_DIR / "____")
        coef_table
        ''',
        answer='''
        coef_table = pd.DataFrame({
            "coef": ols.params,
            "ci_low": ols.conf_int()[0],
            "ci_high": ols.conf_int()[1],
            "p_value": ols.pvalues,
        }).round(3)

        coef_table.to_csv(RESULTS_DIR / "table2_regression_coefficients.csv")
        coef_table
        ''',
        hint='Give the file a clear name, e.g. `"table2_regression_coefficients.csv"`.',
    ))
    add(code("""check("Coefficient table saved", any(RESULTS_DIR.glob("*regression*.csv")), "Name the file table2_regression_coefficients.csv")"""))
    add(md("### 5.3 Check the assumptions before you believe the results"))
    add(code("""
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    axes[0].scatter(ols.fittedvalues, ols.resid, alpha=0.3, s=10)
    axes[0].axhline(0, color="black", lw=1)
    axes[0].set(xlabel="Fitted values", ylabel="Residuals", title="Residuals vs fitted")
    stats.probplot(ols.resid, dist="norm", plot=axes[1])
    axes[1].set_title("Normal Q-Q plot of residuals")
    plt.tight_layout()
    plt.show()
    """))
    add(md("""
    - **Residuals vs fitted:** you want a shapeless cloud around 0. A curve means a relationship is not a straight line.
    - **Q-Q plot:** points close to the line mean the residuals are roughly normal.

    ### 5.4 ✍️ TODO: Improve the model with curved (squared) terms
    In 3.4 you saw that rainfall has a hill-shaped effect. Add **squared** terms for rainfall and mound density.
    We centre them first (subtract a typical value) so the numbers stay readable. Does adjusted R² improve?
    """))
    add(todo(
        starter='''
        formula2 = formula + " + I((rainfall_mm - 1260)**2) + I((mound_density_per_ha - ____)**2)"
        ols2 = smf.ols(formula2, data=df).fit()

        print(f"Adjusted R², original model: {ols.rsquared_adj:.3f}")
        print(f"Adjusted R², with squares:   {ols2.rsquared_adj:.3f}")
        ols2.params.filter(like="**2")
        ''',
        answer='''
        formula2 = formula + " + I((rainfall_mm - 1260)**2) + I((mound_density_per_ha - 10000)**2)"
        ols2 = smf.ols(formula2, data=df).fit()

        print(f"Adjusted R², original model: {ols.rsquared_adj:.3f}")
        print(f"Adjusted R², with squares:   {ols2.rsquared_adj:.3f}")
        ols2.params.filter(like="**2")
        ''',
        hint="Use a typical mound density such as `10000` (close to the mean). `I(...)` tells statsmodels to do the maths inside.",
    ))
    add(code("""check("Squared terms improve adjusted R²", ols2.rsquared_adj > ols.rsquared_adj, "Add both squared terms to formula2")"""))
    add(md("""
    A **negative** coefficient on a squared term means the curve is hill-shaped: there is a best amount, and
    going above or below it lowers yield.

    ### 5.5 📝 Write: what happened to the gender gap?
    Find the row `C(gender, Treatment('Male'))[T.Female]` in the table. Compare it with the raw difference in 4.4.
    """))
    add(code("""
    gender_term = "C(gender, Treatment('Male'))[T.Female]"
    print(f"Raw gap (t-test, female minus male):     {-diff_gender:.2f} t/ha, p = {p_gender:.3f}")
    print(f"Adjusted gap (regression, female - male): {ols2.params[gender_term]:.2f} t/ha, "
          f"95% CI [{ols2.conf_int().loc[gender_term, 0]:.2f}, {ols2.conf_int().loc[gender_term, 1]:.2f}], "
          f"p = {ols2.pvalues[gender_term]:.3f}")
    """))
    add(md("""
    📝 *Once we hold practices and resources constant, is there still a significant gender gap? What does this
    suggest for policy (e.g. credit, extension and staking materials for women farmers)? Remember the data is
    synthetic, so phrase it as "in this dataset".*

    ### 5.6 🤖 AI exercise: interpret, then verify
    Paste the **coefficient table** (not the data) into your AI assistant:
    > *"Interpret this regression table for the results chapter of an MSc thesis in plain academic English. The
    > outcome is yam yield in tonnes per hectare. Mention the direction, size and 95% confidence interval of each
    > statistically significant effect, and state the limitations of observational survey data."*

    ✅ **Check every number** in the AI's paragraph against your table. AI tools often get signs or units wrong and
    overstate causation ("staking *causes*..."). Fix any mistakes before using it in your report.

    ### 💾 Member 3: commit and pass the baton
    `git add .` → `git commit -m "Parts 4-5: hypothesis tests and regression"` → `git push` → tell Member 4.
    """))

    # =========================================================================
    # PART 6
    # =========================================================================
    add(md("""
    ---
    ## Part 6 · Machine learning: *predicting* yield (Member 4)
    > `git pull` first, then **Run All**.

    Regression (Part 5) *explains*. Machine learning *predicts*: given a new farm's practices **before harvest**,
    what yield should we expect?

    ### 6.1 ✍️ TODO: Choose the features (and avoid leakage!)
    Fill in the two **leaky** columns from Part 1.8. The check makes sure none of them sneak into the features.
    """))
    add(todo(
        starter='''
        LEAKY_COLUMNS = ["____", "____"]     # known only AFTER harvest

        NUMERIC_FEATURES = [
            "farmer_age", "household_size", "years_farming", "farm_size_ha", "sett_weight_g",
            "mound_density_per_ha", "fertilizer_kg_per_ha", "weeding_count", "rainfall_mm",
            "extension_visits", "distance_to_market_km",
        ]
        CATEGORICAL_FEATURES = [
            "lga", "gender", "education_level", "seed_source", "planting_month", "staking",
            "organic_manure", "intercropped", "soil_type", "pest_disease_level",
            "cooperative_member", "access_to_credit",
        ]
        FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
        print(len(FEATURES), "features")
        ''',
        answer='''
        LEAKY_COLUMNS = ["harvest_revenue_naira", "tubers_harvested_per_ha"]     # known only AFTER harvest

        NUMERIC_FEATURES = [
            "farmer_age", "household_size", "years_farming", "farm_size_ha", "sett_weight_g",
            "mound_density_per_ha", "fertilizer_kg_per_ha", "weeding_count", "rainfall_mm",
            "extension_visits", "distance_to_market_km",
        ]
        CATEGORICAL_FEATURES = [
            "lga", "gender", "education_level", "seed_source", "planting_month", "staking",
            "organic_manure", "intercropped", "soil_type", "pest_disease_level",
            "cooperative_member", "access_to_credit",
        ]
        FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
        print(len(FEATURES), "features")
        ''',
        hint="The two columns measured after harvest are `harvest_revenue_naira` and `tubers_harvested_per_ha`.",
    ))
    add(code("""
    check("Leaky columns named", set(LEAKY_COLUMNS) == {"harvest_revenue_naira", "tubers_harvested_per_ha"}, "See Part 1.8")
    check("No leaky column, ID or target in FEATURES", not set(FEATURES) & set(LEAKY_COLUMNS + ["farm_id", TARGET]), "Remove them")
    """))
    add(md("""
    ### 6.2 ✍️ TODO: Lock away a test set first
    Keep **20%** of farms as a test set. It stays untouched until the very end.
    """))
    add(todo(
        starter='''
        from sklearn.model_selection import train_test_split

        X, y = df[FEATURES], df[TARGET]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=____, random_state=RANDOM_STATE)
        print(f"Train: {len(X_train)} farms   Test: {len(X_test)} farms")
        ''',
        answer='''
        from sklearn.model_selection import train_test_split

        X, y = df[FEATURES], df[TARGET]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)
        print(f"Train: {len(X_train)} farms   Test: {len(X_test)} farms")
        ''',
        hint="20% is written as `0.2`.",
    ))
    add(code("""check("20% test set", abs(len(X_test) / len(X) - 0.2) < 0.01, "Use test_size=0.2")"""))
    add(md("""
    ### 6.3 The preprocessing pipeline (complete, just run it)
    This fills missing values, scales numbers and one-hot encodes categories. Because it sits **inside** the
    pipeline, it is re-learned on each training fold, so no information leaks from the test data.
    """))
    add(code("""
    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler


    def build_preprocessor(numeric=NUMERIC_FEATURES, categorical=CATEGORICAL_FEATURES):
        numeric_steps = Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
        categorical_steps = Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                                      ("encode", OneHotEncoder(handle_unknown="ignore"))])
        return ColumnTransformer([("num", numeric_steps, numeric), ("cat", categorical_steps, categorical)])


    build_preprocessor()
    """))
    add(md("""
    ### 6.4 ✍️ TODO: Compare models with 5-fold cross-validation
    Add a **random forest** to the list of candidate models. Always include a **baseline**: a model is only useful
    if it clearly beats "just predict the average". *(This cell may take a minute.)*
    """))
    add(todo(
        starter='''
        from sklearn.model_selection import KFold, cross_validate
        from sklearn.dummy import DummyRegressor
        from sklearn.linear_model import LinearRegression
        from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor

        candidates = {
            "Baseline (predict the mean)": DummyRegressor(),
            "Linear regression": LinearRegression(),
            "Random forest": ____(n_estimators=200, min_samples_leaf=3, random_state=RANDOM_STATE, n_jobs=-1),
            "Gradient boosting": HistGradientBoostingRegressor(random_state=RANDOM_STATE),
        }
        cv = KFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

        rows = []
        for name, model in candidates.items():
            pipe = Pipeline([("preprocess", build_preprocessor()), ("model", model)])
            scores = cross_validate(pipe, X_train, y_train, cv=cv, scoring=["r2", "neg_mean_absolute_error"])
            rows.append({"model": name,
                         "R2 (mean)": scores["test_r2"].mean(), "R2 (sd)": scores["test_r2"].std(),
                         "MAE (mean, t/ha)": -scores["test_neg_mean_absolute_error"].mean()})

        cv_results = pd.DataFrame(rows).set_index("model").round(3)
        cv_results.to_csv(RESULTS_DIR / "table3_model_comparison_cv.csv")
        cv_results
        ''',
        answer='''
        from sklearn.model_selection import KFold, cross_validate
        from sklearn.dummy import DummyRegressor
        from sklearn.linear_model import LinearRegression
        from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor

        candidates = {
            "Baseline (predict the mean)": DummyRegressor(),
            "Linear regression": LinearRegression(),
            "Random forest": RandomForestRegressor(n_estimators=200, min_samples_leaf=3, random_state=RANDOM_STATE, n_jobs=-1),
            "Gradient boosting": HistGradientBoostingRegressor(random_state=RANDOM_STATE),
        }
        cv = KFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

        rows = []
        for name, model in candidates.items():
            pipe = Pipeline([("preprocess", build_preprocessor()), ("model", model)])
            scores = cross_validate(pipe, X_train, y_train, cv=cv, scoring=["r2", "neg_mean_absolute_error"])
            rows.append({"model": name,
                         "R2 (mean)": scores["test_r2"].mean(), "R2 (sd)": scores["test_r2"].std(),
                         "MAE (mean, t/ha)": -scores["test_neg_mean_absolute_error"].mean()})

        cv_results = pd.DataFrame(rows).set_index("model").round(3)
        cv_results.to_csv(RESULTS_DIR / "table3_model_comparison_cv.csv")
        cv_results
        ''',
        hint="The blank is the model's name, which is already imported: `RandomForestRegressor`.",
    ))
    add(code("""
    check("Four models compared", len(cv_results) == 4, "Add the random forest")
    check("Best model beats the baseline", cv_results["R2 (mean)"].max() > cv_results.loc["Baseline (predict the mean)", "R2 (mean)"] + 0.2, "")
    """))
    add(md("""
    📝 *Which model has the best mean R²? Is the difference between the top models bigger than their standard
    deviation (sd)? If not, they are practically equally good.* Don't be surprised if **linear regression**
    wins: when the relationships are fairly simple, a simple model can beat a complex one. Simpler is also
    easier to explain in your thesis.

    ### 6.5 ✍️ TODO: ⚠️ The leakage trap
    A colleague says: *"Add `tubers_harvested_per_ha`. It makes the model much better!"* Let's see what happens.
    """))
    add(todo(
        starter='''
        leaky_feature = "____"
        leaky_numeric = NUMERIC_FEATURES + [leaky_feature]

        leaky_pipe = Pipeline([("preprocess", build_preprocessor(numeric=leaky_numeric)),
                               ("model", HistGradientBoostingRegressor(random_state=RANDOM_STATE))])
        leaky_scores = cross_validate(leaky_pipe, df.loc[X_train.index, leaky_numeric + CATEGORICAL_FEATURES],
                                      y_train, cv=cv, scoring="r2")
        leaky_r2 = leaky_scores["test_score"].mean()

        print(f"R² WITH the leaky feature: {leaky_r2:.3f}   (looks amazing...)")
        print(f"R² without it:             {cv_results.loc['Gradient boosting', 'R2 (mean)']:.3f}")
        ''',
        answer='''
        leaky_feature = "tubers_harvested_per_ha"
        leaky_numeric = NUMERIC_FEATURES + [leaky_feature]

        leaky_pipe = Pipeline([("preprocess", build_preprocessor(numeric=leaky_numeric)),
                               ("model", HistGradientBoostingRegressor(random_state=RANDOM_STATE))])
        leaky_scores = cross_validate(leaky_pipe, df.loc[X_train.index, leaky_numeric + CATEGORICAL_FEATURES],
                                      y_train, cv=cv, scoring="r2")
        leaky_r2 = leaky_scores["test_score"].mean()

        print(f"R² WITH the leaky feature: {leaky_r2:.3f}   (looks amazing...)")
        print(f"R² without it:             {cv_results.loc['Gradient boosting', 'R2 (mean)']:.3f}")
        ''',
        hint='Use the column name `"tubers_harvested_per_ha"`.',
    ))
    add(code("""check("Leakage demonstrated (R² jumps)", leaky_r2 > cv_results["R2 (mean)"].max() + 0.1, 'Use "tubers_harvested_per_ha"')"""))
    add(md("""
    📝 **Write:** why is the "amazing" model useless for a farmer who wants a prediction **before** harvest?
    (Number of tubers is only known when you dig them up, and yield ≈ tubers × average tuber weight.)
    **If a result looks too good to be true, check for leakage.**

    ### 6.6 Final evaluation on the untouched test set (complete, just run it)
    We pick the model with the best cross-validated R², train it on all training data, and test it **once**.
    """))
    add(code("""
    from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error

    best_name = cv_results["R2 (mean)"].idxmax()
    final_pipeline = Pipeline([("preprocess", build_preprocessor()), ("model", candidates[best_name])])
    final_pipeline.fit(X_train, y_train)

    y_pred = final_pipeline.predict(X_test)
    test_metrics = {"MAE": mean_absolute_error(y_test, y_pred),
                    "RMSE": root_mean_squared_error(y_test, y_pred),
                    "R2": r2_score(y_test, y_pred)}
    print(f"Chosen model: {best_name}")
    print({k: round(v, 3) for k, v in test_metrics.items()})

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.scatter(y_test, y_pred, alpha=0.4, s=12)
    lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
    ax.plot(lims, lims, color="black", lw=1, ls="--", label="Perfect prediction")
    ax.set(xlabel="Actual yield (t/ha)", ylabel="Predicted yield (t/ha)",
           title=f"{best_name}: test R² = {test_metrics['R2']:.2f}")
    ax.legend()
    save_figure(fig, "fig3_predicted_vs_actual")
    plt.show()
    """))
    add(md("""
    📝 *In plain words: "On farms the model has never seen, its predictions are typically off by about __ t/ha (MAE)."*

    ### 6.7 Which features matter? (permutation importance, complete, just run it)
    """))
    add(code("""
    from sklearn.inspection import permutation_importance

    perm = permutation_importance(final_pipeline, X_test, y_test, n_repeats=5, random_state=RANDOM_STATE, n_jobs=-1)
    importance = (pd.DataFrame({"feature": FEATURES, "importance": perm.importances_mean, "sd": perm.importances_std})
                  .sort_values("importance"))

    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.barh(importance["feature"].str.replace("_", " "), importance["importance"], xerr=importance["sd"], color="#0072B2")
    ax.set(xlabel="Drop in R² when the feature is shuffled", title="Permutation feature importance (test set)")
    save_figure(fig, "fig4_feature_importance")
    plt.show()
    """))
    add(md("""
    ⚠️ *Important to the model* does **not** mean *causes yield*. Importance describes the model, not the world.

    ### 6.8 ✍️ TODO: Save the model for the app
    `save_model(...)` saves the pipeline **and** a *model card* (`models/model_card.json`) that the Streamlit
    app uses to build its input boxes. Fill in the blanks.
    """))
    add(todo(
        starter='''
        save_model(
            final_pipeline,
            test_metrics,
            X_train,
            numeric_features=NUMERIC_FEATURES,
            categorical_features=____,
            group_name=____,
            notes=f"Chosen by 5-fold CV ({best_name})",
        )
        ''',
        answer='''
        save_model(
            final_pipeline,
            test_metrics,
            X_train,
            numeric_features=NUMERIC_FEATURES,
            categorical_features=CATEGORICAL_FEATURES,
            group_name=GROUP_NAME,
            notes=f"Chosen by 5-fold CV ({best_name})",
        )
        ''',
        hint="Use the variables `CATEGORICAL_FEATURES` and `GROUP_NAME` (no quotes).",
    ))
    add(code("""check("Model saved", MODEL_PATH.exists(), "Run save_model(...) above")"""))
    add(md("""
    ### 💾 Member 4: commit and pass the baton
    `git add .` → `git commit -m "Part 6: machine learning model"` → `git push` → tell Member 2 (figures)
    **and** Member 5 (the app can now load your model).
    """))

    # =========================================================================
    # PART 7
    # =========================================================================
    add(md("""
    ---
    ## Part 7 · Publication-ready figures and tables (Member 2)
    > `git pull` first, then **Run All**.

    A publication-ready figure has: labelled axes **with units**, no chart junk, a colour-blind-safe palette,
    **300 dpi**, and is saved as PNG (for Word) **and** PDF (for LaTeX). `set_publication_style()` and
    `save_figure()` (from `src/project_tools.py`) do most of this for you.

    ### 7.1 ✍️ TODO: Table 1, descriptive statistics
    Most papers start with a table describing the sample. Make one comparing staked and non-staked farms.
    """))
    add(todo(
        starter='''
        table1_vars = [TARGET, "fertilizer_kg_per_ha", "farm_size_ha", "weeding_count", "extension_visits"]

        table1 = df.groupby("____")[table1_vars].agg(["mean", "std"]).round(2).T
        table1.to_csv(RESULTS_DIR / "table1_descriptives_by_staking.csv")
        table1
        ''',
        answer='''
        table1_vars = [TARGET, "fertilizer_kg_per_ha", "farm_size_ha", "weeding_count", "extension_visits"]

        table1 = df.groupby("staking")[table1_vars].agg(["mean", "std"]).round(2).T
        table1.to_csv(RESULTS_DIR / "table1_descriptives_by_staking.csv")
        table1
        ''',
        hint='Group by `"staking"`.',
    ))
    add(code("""check("Table 1 saved", (RESULTS_DIR / "table1_descriptives_by_staking.csv").exists(), "Run the cell above")"""))
    add(md("""
    ### 7.2 ✍️ TODO: Figure 1, yield by seed source and staking
    A grouped bar chart of mean yield with **95% confidence intervals**.
    """))
    add(todo(
        starter='''
        seed_order = ["Own saved setts", "Local market", "ADP / NGO", "Certified seed yam"]

        fig, ax = plt.subplots(figsize=(7, 4.2))
        sns.barplot(data=df, x="____", y=TARGET, hue="____", order=seed_order,
                    errorbar=("ci", 95), capsize=0.1, ax=ax)
        ax.set(xlabel="Source of seed yam", ylabel="Mean yield (t/ha), 95% CI",
               title="Yam yield by seed source and staking")
        ax.legend(title="Staking")
        save_figure(fig, "fig1_yield_by_seed_and_staking")
        plt.show()
        ''',
        answer='''
        seed_order = ["Own saved setts", "Local market", "ADP / NGO", "Certified seed yam"]

        fig, ax = plt.subplots(figsize=(7, 4.2))
        sns.barplot(data=df, x="seed_source", y=TARGET, hue="staking", order=seed_order,
                    errorbar=("ci", 95), capsize=0.1, ax=ax)
        ax.set(xlabel="Source of seed yam", ylabel="Mean yield (t/ha), 95% CI",
               title="Yam yield by seed source and staking")
        ax.legend(title="Staking")
        save_figure(fig, "fig1_yield_by_seed_and_staking")
        plt.show()
        ''',
        hint='`x="seed_source"` and `hue="staking"`.',
    ))
    add(md("""
    ### 7.3 Figure 2, regression coefficient (forest) plot (complete, just run it)
    A coefficient plot is often clearer than a long regression table. We show the **categorical** effects
    (which are all in t/ha, so they can be compared).
    """))
    add(code("""
    plot_df = coef_table[coef_table.index.str.startswith("C(")].copy()
    plot_df.index = (plot_df.index
                     .str.replace(r"C\\((\\w+), Treatment\\('[^']+'\\)\\)\\[T\\.(.+)\\]", r"\\1 = \\2", regex=True)
                     .str.replace("_", " "))
    plot_df = plot_df.sort_values("coef")

    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.errorbar(plot_df["coef"], plot_df.index,
                xerr=[plot_df["coef"] - plot_df["ci_low"], plot_df["ci_high"] - plot_df["coef"]],
                fmt="o", color="#0072B2", ecolor="#56B4E9", capsize=3)
    ax.axvline(0, color="black", lw=1)
    ax.set(xlabel="Difference in yield (t/ha) vs reference level, 95% CI",
           title="Farm practices associated with yam yield")
    save_figure(fig, "fig2_regression_coefficients")
    plt.show()
    """))
    add(md("""
    ### 7.4 ✅ Figure checklist
    Before using a figure in your report, tick each box (double-click to edit `[ ]` → `[x]`):
    - [ ] Every axis has a label **with units**
    - [ ] The title (or caption) says what the figure shows
    - [ ] Colours are readable in black-and-white and by colour-blind readers
    - [ ] Saved as PNG and PDF in `figures/` (check the folder!)
    - [ ] The figure is referred to in `report/GROUP_REPORT.md` with a caption

    ### 💾 Member 2: commit and pass the baton
    `git add .` → `git commit -m "Part 7: publication figures and tables"` → `git push` → tell Member 5.
    """))

    # =========================================================================
    # PART 8
    # =========================================================================
    add(md("""
    ---
    ## Part 8 · The Streamlit app (Member 5)
    The app is in **`app/streamlit_app.py`**. Most of it is written for you. Open it in VS Code and complete the
    **TODO 1 to TODO 8** lines (each has a hint). The app runs even before you finish, and tells you which TODO
    to do next.

    1. Make sure the model exists (run the check below). If not, `git pull` (Member 4 should have pushed it).
    2. In the VS Code terminal, from the **project folder**, run:
       ```bash
       streamlit run app/streamlit_app.py
       ```
    3. Your browser opens the app. Each time you save the file, click **Rerun** in the browser (or press `R`).
    4. Press `Ctrl + C` in the terminal to stop the app.

    📸 Take screenshots of your finished app for the report (save them in `figures/`).
    """))
    add(code("""
    check("Model file exists for the app", MODEL_PATH.exists(), "Run Part 6 (or git pull) first")
    check("Clean data exists for the app", PROCESSED_PATH.exists(), "Run Part 2 (or git pull) first")
    """))
    add(md("""
    ⭐ **Stretch (optional):** deploy the app for free on [Streamlit Community Cloud](https://share.streamlit.io):
    sign in with GitHub → **Create app** → choose your group repository → main file `app/streamlit_app.py` →
    **Deploy**. Put the link in your README.

    ---
    ## Part 9 · Finish and submit (Member 5 leads, everyone helps)
    1. **Report:** complete `report/GROUP_REPORT.md` (each member writes the section for their part).
    2. **AI-use statement:** complete `docs/AI_USE_STATEMENT.md` honestly.
    3. **Contributions:** every member fills in their row in `CONTRIBUTIONS.md`.
    4. **Reproducibility check:** in this notebook click **Restart** → **Run All**. Every cell must run without
       errors from top to bottom, and every check should show ✅.
    5. **Final commit:**
       ```bash
       git add .
       git commit -m "Final submission"
       git push
       ```
    6. **Submit** your repository link as described in the README (section *Submit your work*).

    🎉 **Well done!** You have taken raw, messy data all the way to a tested model and a working app, as a team,
    under version control. That is the full research data science workflow.
    """))
    add(code("""
    print(f"{GROUP_NAME}: final summary")
    print(f"  Clean farms analysed: {len(df)}")
    print(f"  Staking effect (t-test): {diff:.2f} t/ha, p = {p:.3g}, d = {cohens_d:.2f}")
    print(f"  Regression adjusted R²: {ols2.rsquared_adj:.3f}")
    print(f"  Best ML model: {best_name}, test R² = {test_metrics['R2']:.3f}, MAE = {test_metrics['MAE']:.2f} t/ha")
    print("  Files in figures/:", sorted(p.name for p in (ROOT / "figures").glob("*.png")))
    print("  Files in results/:", sorted(p.name for p in RESULTS_DIR.glob("*.csv")))
    """))
    return cells


def main():
    global SOLUTION
    parser = argparse.ArgumentParser()
    parser.add_argument("--solution", metavar="PATH", help="write a completed answer-key notebook to PATH instead")
    args = parser.parse_args()
    SOLUTION = bool(args.solution)
    path = Path(args.solution) if args.solution else STARTER_PATH

    nb = nbf.v4.new_notebook()
    nb.cells = build()
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    nb.metadata["language_info"] = {"name": "python"}
    path.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(nb, path)
    print(f"Wrote {path} ({len(nb.cells)} cells)")


if __name__ == "__main__":
    main()
