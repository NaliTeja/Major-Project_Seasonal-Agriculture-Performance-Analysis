"""
Seasonal Agriculture Performance Analysis
VOIS AICTE Major Project

Run:
    python seasonal_agriculture_analysis.py

Outputs:
    outputs/seasonal_summary.csv
    outputs/crop_summary.csv
    outputs/*.png
    data/cleaned_seasonal_agriculture_data.csv
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "seasonal_agriculture_performance_dataset.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
print(f"Original shape: {df.shape}")
print(f"Duplicate rows: {df.duplicated().sum()}")
print("\nMissing values before cleaning:")
print(df.isna().sum()[df.isna().sum() > 0])

# Season-wise median imputation for the three numeric fields with missing values.
for col in ["Rainfall_mm", "Soil_Moisture_pct", "Yield_Tonnes_Ha"]:
    df[col] = df.groupby("Season")[col].transform(lambda s: s.fillna(s.median()))

df = df.drop_duplicates().reset_index(drop=True)
df.to_csv(ROOT / "data" / "cleaned_seasonal_agriculture_data.csv", index=False)

season_order = ["Kharif", "Rabi", "Zaid"]
summary = df.groupby("Season").agg(
    Records=("Farm_ID", "count"),
    Avg_Yield_Tonnes_Ha=("Yield_Tonnes_Ha", "mean"),
    Avg_Revenue_INR=("Revenue_INR", "mean"),
    Avg_Cost_INR=("Total_Cost_INR", "mean"),
    Avg_Profit_INR=("Profit_INR", "mean"),
    Median_Profit_INR=("Profit_INR", "median"),
    Avg_Water_Efficiency=("Water_Efficiency_t_per_1000m3", "mean"),
    Avg_Disease_Pest_Risk=("Disease_Pest_Risk_pct", "mean"),
).reindex(season_order).reset_index()
summary.to_csv(OUT / "seasonal_summary.csv", index=False)

crop_summary = df.groupby("Crop").agg(
    Records=("Farm_ID", "count"),
    Avg_Yield_Tonnes_Ha=("Yield_Tonnes_Ha", "mean"),
    Avg_Profit_INR=("Profit_INR", "mean"),
    Avg_Revenue_INR=("Revenue_INR", "mean"),
).sort_values("Avg_Yield_Tonnes_Ha", ascending=False).reset_index()
crop_summary.to_csv(OUT / "crop_summary.csv", index=False)

# One-way ANOVA tests the null hypothesis that season means are equal.
profit_groups = [df.loc[df["Season"] == s, "Profit_INR"] for s in season_order]
yield_groups = [df.loc[df["Season"] == s, "Yield_Tonnes_Ha"] for s in season_order]
profit_anova = f_oneway(*profit_groups)
yield_anova = f_oneway(*yield_groups)

print("\nSeasonal summary:")
print(summary.round(2).to_string(index=False))
print(f"\nProfit ANOVA: F={profit_anova.statistic:.3f}, p={profit_anova.pvalue:.6g}")
print(f"Yield ANOVA: F={yield_anova.statistic:.3f}, p={yield_anova.pvalue:.6g}")

numeric_corr = df.select_dtypes(include=np.number).corr()["Yield_Tonnes_Ha"].drop("Yield_Tonnes_Ha")
print("\nTop correlations with yield:")
print(numeric_corr.sort_values(key=abs, ascending=False).head(8).round(3))

print("\nAnalysis completed successfully.")
