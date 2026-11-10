"""
Helper tools for the group project, so the notebook can focus on the analysis.

You do NOT need to edit this file. The notebook and the Streamlit app import it:

    from src.project_tools import RAW_PATH, check, set_publication_style, save_figure

What is in here:
    * folder paths (data, figures, results, models)
    * check(...)                  prints ✅ or ❌ after each TODO, so you know you got it right
    * set_publication_style()     the 300-dpi, colour-blind-safe figure style from the workshop
    * save_figure(fig, name)      saves a figure as PNG (for Word) and PDF (for LaTeX)
    * save_model(...) / load_model()   save the trained pipeline plus a "model card" for the app
"""

import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np

# --- Folders -----------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "nasarawa_yam_survey_synthetic.csv"
PROCESSED_PATH = ROOT / "data" / "processed" / "yam_survey_clean.csv"
FIGURES_DIR = ROOT / "figures"
RESULTS_DIR = ROOT / "results"
MODELS_DIR = ROOT / "models"
MODEL_PATH = MODELS_DIR / "yam_yield_model.joblib"
MODEL_CARD_PATH = MODELS_DIR / "model_card.json"

TARGET = "yield_t_per_ha"
RANDOM_STATE = 42

# Colour-blind-safe palette (Okabe & Ito), the same one used in the workshop
PALETTE = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9", "#F0E442", "#000000"]


# --- Self-checks ---------------------------------------------------------------
def check(label: str, condition, hint: str = "") -> bool:
    """Print a tick if `condition` is True, otherwise a cross and a hint.

    Used after each TODO in the notebook. A ❌ does not break anything: read the
    hint, fix your code above, and run both cells again.
    """
    try:
        ok = bool(condition)
    except Exception as err:  # e.g. comparing something that does not exist yet
        ok, hint = False, f"{hint} (check raised: {err})"
    print(("✅ " if ok else "❌ ") + label + ("" if ok or not hint else f"\n   💡 {hint}"))
    return ok


# --- Figures -------------------------------------------------------------------
def set_publication_style(font_size: int = 11) -> None:
    plt.rcParams.update({
        "figure.figsize": (6.5, 4.0),   # fits a single journal column / A4 thesis page
        "figure.dpi": 110,
        "savefig.dpi": 300,             # most journals ask for at least 300 dpi
        "savefig.bbox": "tight",
        "font.size": font_size,
        "axes.titlesize": font_size + 1,
        "axes.labelsize": font_size,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "legend.frameon": False,
        "axes.prop_cycle": plt.cycler(color=PALETTE),
    })


def save_figure(fig, name: str, formats=("png", "pdf")) -> list:
    """Save a figure in several formats into figures/: PNG for Word, PDF (vector) for LaTeX."""
    FIGURES_DIR.mkdir(exist_ok=True)
    paths = []
    for fmt in formats:
        path = FIGURES_DIR / f"{name}.{fmt}"
        fig.savefig(path)
        paths.append(path)
    print("Saved:", ", ".join(p.name for p in paths))
    return paths


# --- Model saving --------------------------------------------------------------
def save_model(pipeline, metrics: dict, X_train, numeric_features: list, categorical_features: list,
               group_name: str = "", notes: str = "") -> None:
    """Save the fitted pipeline and a small 'model card' that describes it.

    The Streamlit app reads the model card to build its input boxes automatically
    (it uses the ranges and categories seen in the training data).
    """
    MODELS_DIR.mkdir(exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH, compress=3)

    import sklearn  # imported here so this file loads quickly

    card = {
        "group": group_name,
        "model": type(pipeline.named_steps["model"]).__name__,
        "target": TARGET,
        "numeric_features": list(numeric_features),
        "categorical_features": list(categorical_features),
        "test_metrics": {k: float(v) for k, v in metrics.items()},
        "n_training_rows": int(len(X_train)),
        "numeric_ranges": {
            col: [float(np.nanmin(X_train[col])), float(np.nanmedian(X_train[col])), float(np.nanmax(X_train[col]))]
            for col in numeric_features
        },
        "categories": {col: sorted(X_train[col].dropna().astype(str).unique().tolist()) for col in categorical_features},
        "trained_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "python": platform.python_version(),
        "scikit_learn": sklearn.__version__,
        "data_note": "Trained on SYNTHETIC teaching data. Do not use for real farm decisions.",
        "notes": notes,
    }
    MODEL_CARD_PATH.write_text(json.dumps(card, indent=2), encoding="utf-8")
    size_mb = MODEL_PATH.stat().st_size / 1e6
    print(f"Saved {MODEL_PATH.name} ({size_mb:.1f} MB) and {MODEL_CARD_PATH.name}")


def load_model():
    """Return (pipeline, model_card) saved by save_model()."""
    return joblib.load(MODEL_PATH), json.loads(MODEL_CARD_PATH.read_text(encoding="utf-8"))
