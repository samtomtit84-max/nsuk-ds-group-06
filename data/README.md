# Data

## `raw/nasarawa_yam_survey_synthetic.csv`

> ⚠️ **Synthetic data, for teaching only.** Every value is simulated by `scripts/make_yam_data.py`
> (fixed random seed 2611). It imitates a smallholder **white yam** farm survey across the 13 LGAs of Nasarawa
> State, 2021–2025. The relationships are loosely based on yam agronomy so the results "make sense", but it is
> **not** real survey data and must not be cited as evidence about real farms.

**Size:** 2,436 rows × 28 columns. One row = one farm in one survey season (before cleaning, some rows are duplicates).

The file contains **deliberate data-quality problems** for Parts 1–2: duplicate rows, LGA spelling variants and
stray spaces, Yes/No and Male/Female written several ways, planting months written as `"Feb"`, `"february"` or `"02"`,
numbers stored as text (`"not recorded"`, `"nil"`, `"N1,250,000"`), `-999` used as a missing-value code,
ordinary missing values, and impossible values (age 150, a 260 ha "smallholder" farm, zero mounds, zero yield).

### Data dictionary

| Column | Type | Description |
|---|---|---|
| `farm_id` | text | Farm identifier (`NYS-00001` …) |
| `survey_year` | integer | Season surveyed (2021–2025) |
| `lga` | category | Local Government Area (13 official LGAs) |
| `farmer_age` | number | Age of the farmer (years) |
| `gender` | category | Male / Female |
| `education_level` | category | No formal education / Primary / Secondary / Tertiary |
| `household_size` | integer | Number of people in the household |
| `years_farming` | number | Farming experience (years) |
| `farm_size_ha` | number | Area under yam (hectares) |
| `seed_source` | category | Where the seed yams (setts) came from: Own saved setts / Local market / ADP / NGO / Certified seed yam |
| `sett_weight_g` | number | Average weight of the seed yam pieces planted (grams) |
| `mound_density_per_ha` | number | Number of yam mounds (heaps) per hectare |
| `planting_month` | category | Month of planting: December – April |
| `staking` | Yes/No | Vines trained up stakes (improves light interception) |
| `fertilizer_kg_per_ha` | number | NPK fertiliser applied (kg/ha) |
| `organic_manure` | Yes/No | Animal manure or compost applied |
| `intercropped` | Yes/No | Yam grown together with another crop (e.g. maize, sorghum) |
| `weeding_count` | integer | Number of weedings during the season (1–4) |
| `soil_type` | category | Sandy loam / Loam / Clay loam / Sandy |
| `rainfall_mm` | number | Seasonal rainfall (mm). `-999` = not recorded |
| `pest_disease_level` | category | Nematodes / scale insects / anthracnose: Absent / Low / Moderate / High |
| `extension_visits` | integer | Visits from extension officers this season |
| `cooperative_member` | Yes/No | Member of a farmers' cooperative |
| `access_to_credit` | Yes/No | Received a loan or input credit this season |
| `distance_to_market_km` | number | Distance from the farm to the nearest yam market (km) |
| `tubers_harvested_per_ha` | number | Number of tubers harvested per hectare. ⚠️ **Measured after harvest, so it leaks the outcome** |
| `harvest_revenue_naira` | number (stored as text) | Money from selling the harvest (₦). ⚠️ **Calculated from yield, so it leaks the outcome** |
| `yield_t_per_ha` | number | 🎯 **Outcome**: yam yield (tonnes per hectare) |

To regenerate the file (facilitators): `python scripts/make_yam_data.py`

## `processed/yam_survey_clean.csv`

Created by **Part 2** of the notebook. It **is** committed to Git in this project, because the Streamlit app needs
it (including on Streamlit Community Cloud). If you change the cleaning, re-run Part 2 and commit the new file.

## Golden rules
- **Never edit `raw/` by hand.** Every change happens in code, so it can be repeated.
- Never paste the dataset into an AI tool. Share column names, code or result tables instead. (Not a problem
  with synthetic data, but it's the habit you need for real research data.)
