"""
Generate the group project's SYNTHETIC dataset: a smallholder YAM farm survey
across the 13 LGAs of Nasarawa State, Nigeria.

Every value is simulated. It is NOT real survey data and must never be cited
as evidence about real farms. The relationships built in below are loosely
based on agronomy for white yam (Dioscorea rotundata) in the Guinea savanna,
so the patterns the groups find will "make sense", but the numbers are made up.

Problems are injected on purpose so that groups practise everything from the
workshop (and a few new things):
  * duplicated survey entries
  * LGA spelling variants, extra spaces, lowercase
  * Yes/No and Male/Female written several different ways
  * planting month written as "Feb", "February", "feb", "02"
  * fertiliser stored as text with "not recorded" / "nil" entries
  * money stored as text with a naira sign and commas ("N1,250,000")
  * -999 used as a "missing" code for rainfall
  * missing values and impossible values (age 150, a 260 ha "smallholder" farm)
  * two LEAKY columns measured after harvest (revenue, number of tubers)

Facilitators: run from the repository root
    python scripts/make_yam_data.py
The seed is fixed, so the file is identical every time.
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 2611
N_FARMS = 2400
N_DUPLICATES = 36
OUT_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "nasarawa_yam_survey_synthetic.csv"

LGAS = [
    "Akwanga", "Awe", "Doma", "Karu", "Keana", "Keffi", "Kokona",
    "Lafia", "Nasarawa", "Nasarawa Eggon", "Obi", "Toto", "Wamba",
]
# Southern LGAs (Doma, Awe, Keana, Obi, Lafia) are the main yam belt, so more farms there
LGA_WEIGHTS = np.array([7, 9, 11, 5, 8, 4, 6, 11, 7, 8, 9, 8, 7], dtype=float)
MONTHS = ["December", "January", "February", "March", "April"]


def simulate(rng: np.random.Generator) -> pd.DataFrame:
    n = N_FARMS
    lga = rng.choice(LGAS, size=n, p=LGA_WEIGHTS / LGA_WEIGHTS.sum())
    lga_effect = dict(zip(LGAS, rng.normal(0, 0.9, size=len(LGAS))))

    gender = rng.choice(["Male", "Female"], n, p=[0.72, 0.28])
    female = gender == "Female"
    farmer_age = rng.normal(44, 11, n).clip(18, 82).round()
    years_farming = (farmer_age - 16 - rng.integers(0, 14, n)).clip(1, None)
    household_size = rng.poisson(6.5, n).clip(1, 20)
    education = rng.choice(["No formal education", "Primary", "Secondary", "Tertiary"], n, p=[0.22, 0.33, 0.32, 0.13])

    # Women in the survey farm smaller plots and have less access to credit, extension
    # and staking materials. Gender has NO direct effect on yield below, so any raw gender
    # gap is explained by access to resources (a confounding story for the regression).
    farm_size = (rng.lognormal(mean=0.25, sigma=0.6, size=n) * np.where(female, 0.7, 1.0)).round(2)
    cooperative = rng.random(n) < (0.42 - 0.12 * female)
    credit = rng.random(n) < (0.20 + 0.22 * cooperative - 0.12 * female)
    extension_visits = rng.poisson(0.9 + 1.5 * cooperative - 0.5 * female, n)

    seed_source = rng.choice(["Own saved setts", "Local market", "ADP / NGO", "Certified seed yam"], n,
                             p=[0.46, 0.30, 0.14, 0.10])
    sett_weight_g = rng.normal(np.where(seed_source == "Certified seed yam", 330, 270), 55).clip(100, 600).round(0)
    mound_density = rng.normal(10000, 1800, n).clip(5000, 16000).round(-1)
    staking = rng.random(n) < (0.48 + 0.15 * cooperative - 0.18 * female)
    fertilizer = (rng.gamma(2.2, 55, n) * (rng.random(n) < 0.8) + 50 * credit).round(1)
    organic_manure = rng.random(n) < 0.36
    intercropped = rng.random(n) < 0.55
    weeding = rng.choice([1, 2, 3, 4], n, p=[0.12, 0.38, 0.38, 0.12])
    planting_month = rng.choice(MONTHS, n, p=[0.10, 0.22, 0.33, 0.25, 0.10])
    soil_type = rng.choice(["Sandy loam", "Loam", "Clay loam", "Sandy"], n, p=[0.38, 0.27, 0.20, 0.15])
    rainfall = rng.normal(1260, 210, n).round(1)
    pest = rng.choice(["Absent", "Low", "Moderate", "High"], n, p=[0.28, 0.40, 0.23, 0.09])
    market_km = rng.gamma(2.0, 6.0, n).round(1)
    year = rng.choice([2021, 2022, 2023, 2024, 2025], n)

    seed_bonus = pd.Series(seed_source).map({"Own saved setts": 0, "Local market": 0.3, "ADP / NGO": 1.3,
                                             "Certified seed yam": 2.2}).to_numpy()
    month_bonus = pd.Series(planting_month).map({"December": 0.7, "January": 0.9, "February": 0.6,
                                                 "March": 0.0, "April": -1.1}).to_numpy()
    soil_bonus = pd.Series(soil_type).map({"Sandy loam": 0.6, "Loam": 0.9, "Clay loam": 0.0, "Sandy": -0.9}).to_numpy()
    pest_penalty = pd.Series(pest).map({"Absent": 0, "Low": 0.6, "Moderate": 1.9, "High": 3.6}).to_numpy()
    edu_bonus = pd.Series(education).map({"No formal education": 0, "Primary": 0.15, "Secondary": 0.3,
                                          "Tertiary": 0.4}).to_numpy()

    yield_t = (
        5.5
        + seed_bonus
        + 1.6 * staking
        + 0.012 * np.minimum(fertilizer, 300)            # diminishing returns above 300 kg/ha
        + 0.8 * organic_manure
        - 0.7 * intercropped
        + 0.55 * np.minimum(weeding, 3)                   # a 4th weeding adds nothing
        - 6e-8 * (mound_density - 10500) ** 2             # too few or too many mounds both hurt
        + 0.004 * (sett_weight_g - 270)
        - 1.3e-5 * (rainfall - 1300) ** 2                  # too little or too much rain hurts
        + month_bonus + soil_bonus - pest_penalty + edu_bonus
        + 0.25 * extension_visits
        + 0.04 * np.minimum(years_farming, 25)
        + np.array([lga_effect[x] for x in lga])
        + rng.normal(0, 1.5, n)
    ).clip(1.5).round(2)

    price_per_tonne = rng.normal(520_000, 60_000, n)       # naira per tonne at the farm gate
    revenue = (yield_t * farm_size * price_per_tonne).round(-3)
    tubers = (yield_t * 1000 / rng.normal(2.1, 0.25, n).clip(1.2)).round(-1)  # tubers per ha, ~2 kg each

    yn = lambda a: np.where(a, "Yes", "No")  # noqa: E731
    return pd.DataFrame({
        "farm_id": [f"NYS-{i:05d}" for i in range(1, n + 1)],
        "survey_year": year,
        "lga": lga,
        "farmer_age": farmer_age,
        "gender": gender,
        "education_level": education,
        "household_size": household_size,
        "years_farming": years_farming,
        "farm_size_ha": farm_size,
        "seed_source": seed_source,
        "sett_weight_g": sett_weight_g,
        "mound_density_per_ha": mound_density,
        "planting_month": planting_month,
        "staking": yn(staking),
        "fertilizer_kg_per_ha": fertilizer,
        "organic_manure": yn(organic_manure),
        "intercropped": yn(intercropped),
        "weeding_count": weeding,
        "soil_type": soil_type,
        "rainfall_mm": rainfall,
        "pest_disease_level": pest,
        "extension_visits": extension_visits,
        "cooperative_member": yn(cooperative),
        "access_to_credit": yn(credit),
        "distance_to_market_km": market_km,
        "tubers_harvested_per_ha": tubers,
        "harvest_revenue_naira": revenue,
        "yield_t_per_ha": yield_t,
    })


def make_messy(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    df = df.copy()
    n = len(df)

    def pick(frac):
        return rng.choice(n, size=int(frac * n), replace=False)

    # LGA spellings
    for i in pick(0.06):
        df.loc[i, "lga"] = df.loc[i, "lga"].lower()
    for i in pick(0.05):
        df.loc[i, "lga"] = " " + df.loc[i, "lga"] + "  "
    for name, variants, p in [("Nasarawa Eggon", ["Nasarawa Eggon", "Nasarawa-Eggon", "N/Eggon"], [0.7, 0.2, 0.1]),
                              ("Nasarawa", ["Nasarawa", "Nassarawa"], [0.85, 0.15]),
                              ("Akwanga", ["Akwanga", "Akwaga"], [0.9, 0.1])]:
        mask = df["lga"] == name
        df.loc[mask, "lga"] = rng.choice(variants, size=mask.sum(), p=p)

    # Yes/No and Male/Female written several ways
    variants = {"Yes": ["Yes", "yes", "Y", "YES", "yes "], "No": ["No", "no", "N", "NO", " no"]}
    for col in ["staking", "organic_manure", "intercropped", "cooperative_member", "access_to_credit"]:
        for i in pick(0.12):
            df.loc[i, col] = rng.choice(variants[df.loc[i, col]])
    gender_variants = {"Male": ["M", "male", "MALE"], "Female": ["F", "female", "FEMALE"]}
    for i in pick(0.10):
        df.loc[i, "gender"] = rng.choice(gender_variants[df.loc[i, "gender"]])

    # Planting month in mixed formats
    short = {"December": "Dec", "January": "Jan", "February": "Feb", "March": "Mar", "April": "Apr"}
    number = {"December": "12", "January": "01", "February": "02", "March": "03", "April": "04"}
    for i in pick(0.15):
        df.loc[i, "planting_month"] = short[df.loc[i, "planting_month"]]
    for i in pick(0.06):
        df.loc[i, "planting_month"] = df.loc[i, "planting_month"].lower()
    for i in pick(0.04):
        m = df.loc[i, "planting_month"]
        if m in number:
            df.loc[i, "planting_month"] = number[m]

    # Numbers stored as text
    df["fertilizer_kg_per_ha"] = df["fertilizer_kg_per_ha"].astype(object)
    for i in pick(0.03):
        df.loc[i, "fertilizer_kg_per_ha"] = rng.choice(["not recorded", "nil", "-"])
    df["harvest_revenue_naira"] = df["harvest_revenue_naira"].astype(object)
    for i in pick(0.25):
        v = df.loc[i, "harvest_revenue_naira"]
        df.loc[i, "harvest_revenue_naira"] = f"N{v:,.0f}" if rng.random() < 0.5 else f"₦{v:,.0f}"

    # Missing values
    for col, frac in [("soil_type", 0.05), ("rainfall_mm", 0.035), ("farmer_age", 0.03), ("extension_visits", 0.05),
                      ("education_level", 0.025), ("sett_weight_g", 0.06), ("distance_to_market_km", 0.04),
                      ("household_size", 0.02), ("yield_t_per_ha", 0.015)]:
        df.loc[pick(frac), col] = np.nan
    df.loc[pick(0.012), "rainfall_mm"] = -999          # "missing" code used by some enumerators

    # Impossible values (data-entry errors)
    df.loc[pick(0.003), "farmer_age"] = 150
    df.loc[pick(0.003), "farmer_age"] = 6
    for i in pick(0.005):
        df.loc[i, "farm_size_ha"] = df.loc[i, "farm_size_ha"] * 100   # decimal point slipped
    df.loc[pick(0.003), "mound_density_per_ha"] = 0
    df.loc[pick(0.002), "yield_t_per_ha"] = 0                         # recorded before harvest

    # Duplicated survey entries
    dupes = df.sample(N_DUPLICATES, random_state=SEED)
    df = pd.concat([df, dupes], ignore_index=True)
    return df.sample(frac=1, random_state=SEED).reset_index(drop=True)


def main() -> None:
    rng = np.random.default_rng(SEED)
    df = make_messy(simulate(rng), rng)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False, encoding="utf-8")
    print(f"Wrote {len(df)} rows x {df.shape[1]} columns to {OUT_PATH}")


if __name__ == "__main__":
    main()
