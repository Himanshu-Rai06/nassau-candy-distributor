# Supply Chain Analytics — Nassau Candy Distributor

> End-to-end supply chain analytics project: exploratory data analysis, predictive modelling, route clustering, and a factory reassignment simulation engine — published as a research paper and deployed as an interactive Streamlit dashboard.

[![Streamlit App](https://img.shields.io/badge/Live%20Dashboard-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://candy-distributor-dashboard.streamlit.app/)
[![Research Paper](https://img.shields.io/badge/Research%20Paper-ResearchGate-00CCBB?logo=researchgate&logoColor=white)](https://www.researchgate.net/publication/409277043_Supply_Chain_Analytics_for_Nassau_Candy_Distributor)
[![DOI](https://img.shields.io/badge/DOI-10.13140%2FRG.2.2.19915.35364-blue)](https://doi.org/10.13140/RG.2.2.19915.35364)
[![Python](https://img.shields.io/badge/Python-3.12.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)

---

## Overview

Nassau Candy Distributor operates a multi-factory distribution network across the United States and Canada. Products are currently assigned to factories using static legacy rules, leading to suboptimal shipping distances, elevated lead times, and margin pressure from avoidable logistics costs.

This project addresses those gaps by building a data-driven decision framework that moves from raw order data to actionable factory reassignment recommendations — with every step quantified and explainable.

**Dataset:** 10,194 order records · 15 products · 5 factories · 4 sales regions · 2024–2025

---

## Key Findings

- Lead time is primarily driven by **order year** (r = 0.72), not factory or region — a structural finding that rules out simple route adjustments as a fix.
- **Lot's O' Nuts and Wicked Choccy's** handle 96.5% of all orders and are classified as Congested Routes across all regions.
- **The Other Factory** is the fastest factory in the network (avg. 1,267 days) but handles only 1% of total order volume — a critical underutilisation.
- The simulation engine identifies The Other Factory as the **universally optimal reassignment destination** for all 13 active products.
- Projected impact: **534,218 cumulative operational days saved** with negligible profit-margin impact (Δ < 0.05%).

---

## Methodology

```
Raw Data → Cleaning & Feature Engineering → EDA → Correlation Analysis
       → Predictive Modelling (LR / RF / GBR) → Route & Product Clustering
       → Scenario Simulation Engine → Ranked Recommendations
```

| Stage | Method | Key Output |
|---|---|---|
| Feature Engineering | Haversine distance, lead time derivation | 25-column enriched dataset |
| Predictive Modelling | Linear Regression, Random Forest, Gradient Boosting | Linear Regression selected (R² = 0.53) |
| Route Clustering | K-Means, K=5 (Silhouette = 0.4119) | 5 route categories: Optimised → Bottleneck |
| Product Clustering | K-Means, K=3 (Silhouette = 0.3861) | Fast & Profitable / Average / Slow & Risky |
| Simulation Engine | Deviation-adjusted lead time prediction | 60 scenarios across 13 products |
| Scoring | Weighted composite (60% speed / 30% margin / 10% volume) | Ranked reassignment recommendations |

---

## Repository Structure

```
nassau-candy-distributor/
│
├── data/
│   ├── nassau_clean.csv          # Cleaned dataset with engineered features
│   ├── recommendations.csv       # Final ranked reassignment recommendations
│   ├── route_clusters.csv        # Route-level clustering results
│   └── product_clusters.csv      # Product-level clustering results
│
├── app.py                        # Streamlit dashboard (5 pages)
├── requirements.txt              # Python dependencies
├── runtime.txt                   # Python runtime for deployment
├── config.toml                   # Streamlit configuration
│
└── Nassau_Candy_Supply_Chain_Analytics.pptx   # Slide deck summary
```

---

## Dashboard

The live dashboard is deployed on Streamlit Community Cloud and comprises five pages:

| Page | Description |
|---|---|
| 📊 Overview | Network KPIs, lead time distribution, factory volume, heatmap |
| 🏭 Factory Optimiser | Select a product and simulate predicted lead time across all factories |
| 🔀 What-If Scenario | Custom reassignment simulation with adjustable optimisation priority |
| 🏆 Recommendations | Ranked reassignment table, days saved, priority scores |
| ⚠️ Risk & Impact Panel | Profit margin safety assessment and risk classification per product |

**Live:** [candy-distributor-dashboard.streamlit.app](https://candy-distributor-dashboard.streamlit.app/)

---

## Research Paper

The full research paper (9 sections, 3 appendices) is published on ResearchGate.

**Citation:**

> Rai, H. (2026). *Supply chain analytics for Nassau Candy Distributor: Exploratory data analysis, operational insights, and factory reassignment recommendations*. ResearchGate. https://doi.org/10.13140/RG.2.2.19915.35364

**DOI:** [10.13140/RG.2.2.19915.35364](https://doi.org/10.13140/RG.2.2.19915.35364)

---

## Running Locally

```bash
# Clone the repository
git clone https://github.com/Himanshu-Rai06/nassau-candy-distributor.git
cd nassau-candy-distributor

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run app.py
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core analysis |
| pandas 2.2.2 | Data manipulation |
| numpy 2.0.2 | Numerical computation, Haversine implementation |
| scikit-learn | ML models, clustering, scaling, evaluation |
| matplotlib 3.10 · seaborn 0.13 | EDA visualisations |
| Plotly | Interactive dashboard charts |
| Streamlit | Dashboard framework and deployment |
| Google Colab | Analysis environment |
| LaTeX | Research paper typesetting |

---

## Author

**Himanshu Rai** · Data Science Intern  
[GitHub](https://github.com/Himanshu-Rai06)

---

*Dataset provided as part of a data science internship programme.*
