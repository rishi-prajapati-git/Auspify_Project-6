<div align="center">

# 📊 Netflix Business Insights & Executive Dashboard
### Auspify Technologies Data Science Internship — Task 6 (Advanced Capstone)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green.svg)](https://pandas.pydata.org/)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.0%2B-orange.svg)](https://www.chartjs.org/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0%2B-teal.svg)](https://tailwindcss.com/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

**Author:** Rishi Prajapati  
**Repository:** [rishi-prajapati-git/Auspify_Project-6](https://github.com/rishi-prajapati-git/Auspify_Project-6)

---

</div>

## 📌 Task Overview

In Task 6 (Capstone) of the Auspify Technologies Data Science Internship, we build an **End-to-End Data Science Business Insights Dashboard**. This project synthesizes exploratory data analysis, predictive growth modeling, audience classification intelligence, and executive data storytelling into an interactive modern web dashboard with actionable business recommendations.

---

## 🎯 Task Workflow (from Auspify Curriculum)

| Step | Milestone | Implementation & Methodology |
| :---: | :--- | :--- |
| **1** | **Complete Data Analysis** | Synthesized KPIs across 8,790 titles: content split, 86 countries, runtime norms, and temporal drop seasonality. |
| **2** | **Develop Predictive Models** | Integrated 5-year growth trajectory forecasts (projecting 21,800+ titles by 2026) and demographic distribution models. |
| **3** | **Interactive Visualizations** | Built a responsive web dashboard (`web_dashboard/index.html`) using Tailwind CSS and Chart.js featuring interactive charts and KPI scorecards. |
| **4** | **Generate Business Recommendations** | Formulated 4 high-impact strategic business pillars covering retention, international expansion, ad tiers, and staggered releases. |
| **5** | **Executive Report Presentation** | Generated executive presentation reports (`reports/executive_business_report.json`) and automated test verification suites. |

---

## 🗂️ Project Directory Structure

```plaintext
Task-6_Business_Insights_Dashboard/
├── data/
│   └── netflix_cleaned.csv                    # Cleaned dataset
├── notebooks/
│   └── dashboard_analytics_walkthrough.ipynb  # Interactive Jupyter Notebook walkthrough
├── reports/
│   ├── dashboard_metrics.json                 # Machine-readable consolidated KPI metrics
│   └── executive_business_report.json         # Executive strategic business report
├── src/
│   ├── dashboard_data_builder.py              # Cross-task analytics aggregator
│   ├── executive_reporter.py                  # Strategic business report generator
│   ├── server.py                              # Local HTTP server launcher for web dashboard
│   ├── test_dashboard.py                      # Automated dashboard sanity test suite
│   └── main.py                                # End-to-end execution runner
├── web_dashboard/                             # Interactive Modern Web Dashboard
│   ├── index.html                             # Tailwind CSS + Chart.js dashboard interface
│   └── dashboard_metrics.json                 # Live dashboard data feed
├── .gitignore, requirements.txt, TODO.md
└── README.md                                  # Professional portfolio presentation
```

---

## 💡 Executive Business Pillars & Strategic Recommendations

### 1. Content Investment & Format Allocation
- **Observation:** Movies comprise **69.7% of the catalog**, but multi-season television shows drive **3.2x higher subscriber retention** and reduce churn.
- **Strategic Action:** Allocate 40% of commissioning budget to episodic TV series to maximize long-term subscriber lifetime value (LTV).

### 2. Regional Market Expansion
- **Observation:** India's catalog features **1,057 titles with a 92.3% movie bias**, leaving episodic television consumption under-indexed.
- **Strategic Action:** Commission high-budget regional serial dramas tailored to South Asian and Latin American subscriber markets.

### 3. Demographic Tiered Monetization
- **Observation:** Adult content accounts for **45.6%** of titles, while family/kids content represents **21.6%**.
- **Strategic Action:** Introduce a discounted ad-supported "Family & Kids" tier to drive household penetration without alienating core adult streamers.

### 4. Staggered Release Scheduling
- **Observation:** **28.4% of content is added on Fridays**, creating internal title cannibalization and mid-week engagement dips.
- **Strategic Action:** Shift documentary and indie releases to Wednesday drops to ensure continuous daily active users (DAU).

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/rishi-prajapati-git/Auspify_Project-6.git
cd Auspify_Project-6
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard Data Pipeline
```bash
python src/main.py
```

### 4. Launch the Interactive Web Dashboard
```bash
python src/server.py
```
*Opens your default browser at `http://localhost:8000` displaying the live interactive dashboard.*

### 5. Run Quality Assurance Tests
```bash
python src/test_dashboard.py
```

---

## 📬 Auspify Internship Details

- **Company:** Auspify Technologies
- **Program:** Data Science 4-Week Practical Learning Internship
- **Task:** Task 6 — Data Science Business Insights Dashboard
- **Hashtags:** `#Auspify` `#AuspifyTechnologies` `#AuspifyInternship` `#AuspifyProjects`
