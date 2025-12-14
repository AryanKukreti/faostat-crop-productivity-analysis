# Global Agricultural Productivity & Food Security Analysis (FAOSTAT, 1961–2023)

## Overview

This project analyzes global agricultural production, land use, and crop productivity using FAOSTAT data published by the Food and Agriculture Organization of the United Nations. The analysis spans more than six decades (1961–2023) and covers over 240 countries and 300+ crops.

The objective is to understand long-term productivity trends, yield dynamics, structural data limitations, and emerging risks to global food security. The project emphasizes methodological rigor, defensible data-cleaning decisions, and policy-relevant insights.

## Business & Research Objectives

* Measure long-term trends in global crop production, harvested area, and yields.
* Distinguish productivity gains driven by land expansion versus yield improvement.
* Identify structurally missing data versus true reporting gaps.
* Compare productivity trajectories across crops, countries, and regions.
* Highlight food security vulnerabilities driven by yield stagnation or volatility.

## Data Source

* **FAOSTAT Crop Production Database** (1961–2023)
* Original data provided in wide format (one column per year).
* Reshaped into a tidy, long format to enable scalable time-series analysis.

## Data Engineering Pipeline

1. **Raw Data Ingestion**

   * CSV files are ingested into a PostgreSQL database using an automated Python ingestion script.
   * Each file is stored as a dedicated table for transparency and reproducibility.

2. **Reshaping & Metric Construction**

   * Data is transformed from wide to long format.
   * Only three crop-relevant elements are retained:

     * Production
     * Area harvested
     * Yield

3. **Analysis-Ready Dataset**

   * A unified metrics table is constructed at the (Area × Item × Year) level.
   * Over 1.5 million observations retained after filtering.

## Data Quality & Methodology

* Missing values are treated as **structural**, reflecting FAOSTAT reporting rules rather than data errors.
* Yield is only reported when both production and area harvested are available.
* No blind imputation is performed prior to trend analysis.
* Biologically impossible yield outliers (>200,000 hg/ha) are removed to preserve analytical validity.

These steps ensure all downstream analyses are statistically defensible and agriculturally realistic.

## Exploratory Data Analysis (EDA)

Key EDA findings include:

* Production, area harvested, and yield exhibit strong right-skewed distributions driven by global and regional aggregates.
* Reporting coverage is stable from 1961–1989 and expands significantly after 1990 due to geopolitical changes and improved reporting.
* Recent years (2022–2023) show lower coverage due to FAOSTAT update cycles rather than systemic data loss.

## Global Trends (1961–2021)

* **Production** increased from ~280 million tonnes to over 1 billion tonnes.
* **Harvested area** expanded gradually, indicating limited land-driven growth.
* **Yield** improved substantially, confirming intensification as the dominant driver of output growth.

These patterns reflect the long-term impact of the Green Revolution, mechanization, improved seed varieties, and fertilizer adoption.

## Crop-Level Insights

* Cereals, sugar crops, roots and tubers, and vegetables dominate global production volumes.
* Maize, rice, and wheat remain central pillars of global food security.
* Yield trajectories vary widely across crops, revealing uneven technological diffusion and climate sensitivity.

## Country-Level Performance Highlights

* **Maize**: The United States leads globally, with China showing the fastest long-term improvement.
* **Wheat**: China, France, and Russia exhibit strong productivity growth; climate volatility affects Canada and Australia.
* **Rice**: East and Southeast Asia demonstrate sustained yield improvements driven by modernization and irrigation.

## Statistical Validation

Formal hypothesis testing confirms that modern crop yields are significantly higher than historical baselines. For example:

* Maize yields increased sharply from the 1960s to the 2010s, with extremely strong statistical significance (p ≪ 0.001).

This validates that observed improvements reflect structural change rather than noise.

## Food Security & Risk Analysis

* Regions such as Sub-Saharan Africa, the Sahel, MENA, and Small Island Developing States face persistent vulnerability.
* Key drivers include low yields, high climate volatility, and slow productivity growth.
* Yield inequality between high-income and low-income regions continues to widen.

## Tools & Technologies

* **Python**: pandas, numpy, matplotlib, seaborn
* **SQL / PostgreSQL**: data ingestion and storage
* **Jupyter Notebooks**: analysis, EDA, and visualization
* **FAOSTAT**: authoritative global agricultural data source

## Repository Structure

```
├── data/                         # Raw FAOSTAT CSV files
├── code_ingestion.py             # PostgreSQL ingestion pipeline
├── basicimport.ipynb             # Initial data loading and reshaping
├── EDA.ipynb                     # Exploratory data analysis
├── data_aggregation.ipynb        # Metrics construction & aggregation
├── Business_Questions.ipynb      # Analytical questions & insights
├── Global_Agri_Consulting_Report_Bullets.docx
└── extracted.txt                 # Cleaned narrative summary
```

## Strategic Recommendations

* Accelerate yield growth in climate-vulnerable regions through targeted R&D investment.
* Expand climate-resilient seed adoption and irrigation infrastructure.
* Reduce global yield inequality through technology transfer and capacity building.
* Strengthen early-warning systems to manage climate-driven production volatility.

## Conclusion

Global agricultural productivity has improved dramatically over the past six decades, driven primarily by yield gains rather than land expansion. However, widening yield gaps and rising climate risks pose serious challenges to global food security.

This project demonstrates how rigorous data engineering, careful treatment of missingness, and long-horizon analysis can produce insights that are both statistically sound and policy-relevant.
