"""
🍠 Yam Yield Predictor: your group's Streamlit app.

HOW TO RUN (from the project folder, with your .venv activated):
    streamlit run app/streamlit_app.py

Most of the app is already written. Your job (App lead, with help from the group)
is to complete TODO 1 to TODO 8 below. Each TODO has a 💡 hint, usually the exact
line to type. The app runs even before you finish, and tells you which TODO is next.

How to work:
    1. Do ONE TODO, save the file (Ctrl + S).
    2. In the browser, click "Rerun" (top-right) or press R. Check that it works.
    3. Move on to the next TODO.
    If the page shows a red error, read the LAST line of the error, fix that line, save, rerun.

Before the app can predict, the ML lead must run Part 6 of the notebook so that
models/yam_yield_model.joblib and models/model_card.json exist (then git push / git pull).
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.project_tools import MODEL_PATH, PROCESSED_PATH, TARGET, load_model  # noqa: E402

st.set_page_config(page_title="Yam Yield Predictor", page_icon="🍠", layout="wide")


# ============================================================================
# TODO 1: Type your group name between the quotes, e.g. "Group 03"
# ============================================================================
GROUP_NAME = "Group ___"

# ============================================================================
# TODO 2: Type the names of the five members of your group
# ============================================================================
TEAM = [
    "Member 1 name (Data lead)",
    "Member 2 name (Visualisation lead)",
    "Member 3 name (Statistics lead)",
    "Member 4 name (ML lead)",
    "Member 5 name (App lead)",
]


# --- Loading the model and data (done for you) -------------------------------
# @st.cache_... means "load once, then reuse", so the app stays fast.
@st.cache_resource
def get_model():
    return load_model()


@st.cache_data
def get_data():
    return pd.read_csv(PROCESSED_PATH)


def nice(column: str) -> str:
    """Turn a column name like 'farm_size_ha' into a label like 'Farm size ha'."""
    return column.replace("_", " ").capitalize()


WHOLE_NUMBER_COLUMNS = {"weeding_count", "extension_visits", "household_size", "farmer_age", "years_farming"}


# --- Page title and sidebar --------------------------------------------------
st.title(f"🍠 Yam Yield Predictor · {GROUP_NAME}")

# ============================================================================
# TODO 3: Add a one-sentence description of the app under the title.
# 💡 Hint: delete the # at the start of the next line and change the text if you like
# ============================================================================
# st.caption("Predicts the yam yield (tonnes per hectare) of a farm in Nasarawa State from its practices. Trained on SYNTHETIC data for teaching.")

with st.sidebar:
    st.header("👥 Our team")
    for member in TEAM:
        st.write("•", member)
    st.divider()
    st.info("NSUK Python for Data Science Workshop 2026 · group project. "
            "The data are **synthetic**, so do not use this app for real farm decisions.")

if not MODEL_PATH.exists() or not PROCESSED_PATH.exists():
    st.warning("No trained model or clean data found yet. The ML lead must run Parts 2 and 6 of the notebook "
               "and push the files. Then run `git pull` and refresh this page.")
    st.stop()

model, card = get_model()
data = get_data()

tab_predict, tab_explore, tab_about = st.tabs(["🔮 Predict one farm", "📊 Explore the data", "ℹ️ About the model"])


# ============================================================================
# TAB 1: Predict the yield of one farm
# ============================================================================
with tab_predict:
    st.subheader("Describe the farm")
    st.write("Change the values below, then click **Predict yield**. "
             "The boxes are built automatically from `models/model_card.json`.")

    inputs = {}
    with st.form("farm_inputs"):
        st.markdown("**Numbers**")
        columns = st.columns(3)
        for i, col in enumerate(card["numeric_features"]):
            low, median, high = card["numeric_ranges"][col]
            if col in WHOLE_NUMBER_COLUMNS:
                step, value = 1.0, float(round(median))
            else:
                step, value = (1.0 if high - low > 20 else 0.1), float(round(median, 1))
            inputs[col] = columns[i % 3].number_input(nice(col), min_value=float(low), max_value=float(high),
                                                      value=value, step=step)

        st.markdown("**Categories**")
        columns = st.columns(3)
        for i, col in enumerate(card["categorical_features"]):
            inputs[col] = columns[i % 3].selectbox(nice(col), card["categories"][col])

        submitted = st.form_submit_button("Predict yield", type="primary")

    if submitted:
        farm = pd.DataFrame([inputs])       # one row = this farm
        prediction = None

        # ====================================================================
        # TODO 4: Use the model to predict the yield of this farm.
        # model.predict(...) returns a list with one number in it; [0] takes that number.
        # 💡 Hint: delete the # at the start of the next line
        # ====================================================================
        # prediction = float(model.predict(farm)[0])

        if prediction is None:
            st.info("👋 Complete **TODO 4** in `app/streamlit_app.py` to see the prediction.")
        else:
            average = float(data[TARGET].mean())
            c1, c2, c3 = st.columns(3)

            # ================================================================
            # TODO 5: Show the prediction as a big number with c1.metric(label, value, change)
            # 💡 Hint: c1.metric("Predicted yield", f"{prediction:.1f} t/ha", f"{prediction - average:+.1f} t/ha vs average")
            # ================================================================


            # ================================================================
            # TODO 6: Show the expected TOTAL harvest of this farm in tonnes.
            # Total harvest = predicted yield (t/ha) x farm size (ha) = prediction * inputs["farm_size_ha"]
            # 💡 Hint: c2.metric("Expected harvest for this farm", f"{prediction * inputs['farm_size_ha']:.1f} tonnes")
            # ================================================================


            c3.metric("Typical error (test MAE)", f"± {card['test_metrics']['MAE']:.1f} t/ha")

            # "What if" chart (done for you): change ONE input, keep the others fixed
            st.markdown("#### What if this farm used a different amount of fertiliser?")
            low, _, high = card["numeric_ranges"]["fertilizer_kg_per_ha"]
            grid = pd.DataFrame([inputs] * 40)
            grid["fertilizer_kg_per_ha"] = np.linspace(low, high, 40)
            grid["predicted_yield_t_per_ha"] = model.predict(grid)
            st.line_chart(grid, x="fertilizer_kg_per_ha", y="predicted_yield_t_per_ha")
            st.caption("All other inputs are held fixed. This shows what the model learned. "
                       "It does not prove cause and effect.")


# ============================================================================
# TAB 2: Explore the clean data
# ============================================================================
with tab_explore:
    st.subheader("How does yield differ between groups of farms?")
    group_col = None

    # ========================================================================
    # TODO 7: Let the user choose which column to compare, using a dropdown.
    # 💡 Hint: delete the # at the start of the next line
    # ========================================================================
    # group_col = st.selectbox("Compare average yield by", card["categorical_features"], format_func=nice)

    if group_col is None:
        st.info("👋 Complete **TODO 7** in `app/streamlit_app.py` to show the chart.")
    else:
        summary = (data.groupby(group_col)[TARGET].agg(["count", "mean", "median"])
                   .sort_values("mean").round(2))
        st.bar_chart(summary["mean"], horizontal=True, x_label="Mean yield (t/ha)", y_label=nice(group_col))
        st.dataframe(summary, width="stretch")

    with st.expander("See the first 200 rows of the clean data"):
        st.dataframe(data.head(200), width="stretch")


# ============================================================================
# TAB 3: About the model (the "model card")
# ============================================================================
with tab_about:
    st.subheader("Model card")
    m = card["test_metrics"]
    c1, c2, c3 = st.columns(3)

    # ========================================================================
    # TODO 8: Show the model's three test-set scores with st.metric.
    # 💡 Hint: type these three lines (without the #):
    #   c1.metric("R² (test set)", f"{m['R2']:.2f}")
    #   c2.metric("MAE", f"{m['MAE']:.2f} t/ha")
    #   c3.metric("RMSE", f"{m['RMSE']:.2f} t/ha")
    # ========================================================================


    st.write(f"**Model:** {card['model']} · **Trained on:** {card['n_training_rows']} farms · "
             f"**Trained at:** {card['trained_at']} · scikit-learn {card['scikit_learn']}")
    st.write("**Features used:**", ", ".join(card["numeric_features"] + card["categorical_features"]))
    st.warning(card["data_note"])
    with st.expander("Full model card (models/model_card.json)"):
        st.json(card)


# ============================================================================
# ⭐ STRETCH (optional): extend the app with AI
# Ask your AI assistant, with this file open:
#   "In this Streamlit app, add a fourth tab called 'LGA ranking' that shows a bar chart
#    and a table of the mean yield per LGA from `data`, sorted from highest to lowest."
# Read the code it suggests BEFORE pasting it in. Do you understand every line?
# ============================================================================
