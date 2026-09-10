# Seasonal Agriculture Performance Analysis

## VOIS AICTE Major Project

### 1. Project Overview
This project analyzes agricultural activities across **Kharif, Rabi and Zaid seasons** to identify meaningful patterns in yield, revenue, profit, water efficiency, environmental conditions and disease/pest risk.

The analysis follows the supplied project brief: explore and clean the data, compare seasons, investigate relationships, apply statistical/visualization techniques, interpret evidence and develop data-driven recommendations.

### 2. Dataset
- Rows: **4,000**
- Columns: **28**
- Seasons: Kharif, Rabi, Zaid
- Main analytical outcomes: Yield, Revenue, Cost, Profit, Water Efficiency and Disease/Pest Risk

### 3. Data Cleaning
The raw dataset contains missing values in:
- Rainfall: 48
- Soil Moisture: 40
- Yield: 32

These numeric missing values are filled using the **median within the corresponding season**, which preserves seasonal context. Duplicate rows are also checked and removed if present.

### 4. Key Findings
- Kharif has the highest average yield among the three seasons in this dataset.
- Kharif has the highest average revenue and average profit.
- Zaid has the lowest average profit and the lowest average water-efficiency measure.
- A one-way ANOVA indicates a statistically significant difference in mean profit across seasons (p < 0.001).
- A one-way ANOVA does **not** provide evidence of a statistically significant difference in mean yield across seasons at the 5% level (p = 0.2116).
- Yield has its strongest observed linear correlation with `Water_Efficiency_t_per_1000m3` (r = 0.913) in the cleaned dataset.

> Correlation is an association, not proof of causation. Results describe this dataset and should not be treated as universal agricultural rules.

### 5. Project Structure
```text
Seasonal_Agriculture_Performance_Analysis/
├── data/
│   ├── seasonal_agriculture_performance_dataset.csv
│   └── cleaned_seasonal_agriculture_data.csv
├── notebook/
│   └── Seasonal_Agriculture_Performance_Analysis.ipynb
├── outputs/
│   ├── seasonal_summary.csv
│   ├── crop_summary.csv
│   └── *.png
├── seasonal_agriculture_analysis.py
├── requirements.txt
└── README.md
```

### 6. How to Run
```bash
pip install -r requirements.txt
python seasonal_agriculture_analysis.py
```

To open the notebook:
```bash
jupyter notebook notebook/Seasonal_Agriculture_Performance_Analysis.ipynb
```

### 7. Technology Stack
Python, Pandas, NumPy, Matplotlib, SciPy and Jupyter Notebook.

### 8. Project Deliverables
The repository contains the cleaned dataset, reproducible analysis script, notebook, CSV summaries and presentation-ready visualizations.
