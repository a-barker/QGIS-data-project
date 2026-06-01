# SNAP Benefit Risk Analysis



SNAP (formerly Food Stamps) is a critical lifeline for households that struggle to cover grocery costs. Economic downturns hit certain communities harder — and those same communities tend to recover more slowly. This project aims to identify the characteristics of food-insecure households so that support can be directed where it is most needed during periods of financial stress. A prior spatial analysis flagged San Juan County, NM as a hotspot of *increasing* SNAP usage and Cherry County, NE as a cold spot of *decreasing* SNAP usage. This study compares New Mexico and Nebraska using SNAP data from 2007 and 2017.



A few notes on scope:

1. Analysis is at the state level, which is the lowest granularity available in the SNAP Quality Control datasets.

2. 2007 captures household characteristics before the financial crisis; 2017 captures households that remained on SNAP a decade later during a period of economic growth. Together they offer a window into persistent vulnerability — relevant context for understanding food insecurity during COVID-19.



---



## Problem Statement



What characteristics define food-insecure communities? By training a model on those characteristics, I can generate a risk profile for states that may be vulnerable to spikes in food insecurity.



---



## Target Variable & Model



The target variable is `CAT_ELIG` (SNAP eligibility), standardized across both years as:

- `0` = Not Eligible

- `1` = Eligible



The dataset started with nearly 800 features. After handling nulls and removing highly correlated features, 31 predictors remained alongside the target — 32 columns total.



I prioritized model interpretability over raw accuracy so the coefficients driving predictions would be visible. After evaluating several options, I settled on a Voting Ensemble combining Random Forest, Gradient Boost, and Bagging Classifiers.



---



## Data Sources



- **SNAP data**: USDA [SNAP Quality Control Datasets](https://www.fns.usda.gov/resource/snap-quality-control-data)

- **State boundaries**: US Census Bureau [Carto Boundary Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html)



Data dictionaries are in the reports folder for [2007](reports/07_DataDict.pdf) and [2017](reports/17_DataDict.pdf). One practical note: both dictionaries were produced by the same contractor (Mathematica), but formatting inconsistencies between years caused problems when converting the 2017 PDF to CSV — unusual whitespace and layout differences required manual intervention that the 2007 file did not.



---



## Workflow



1. Split the raw data into four subsets: New Mexico 2007, New Mexico 2017, Nebraska 2007, Nebraska 2017.

2. Addressed missing data across all four datasets.

3. Ran correlation analysis against `CAT_ELIG` within each feature category defined in the technical documentation: Unit Demographics, Unit Countable Income, Unit Countable Assets, Unit Expenses and Deductions, and Person-level Characteristics and Income (persons 1–16).

4. Combined the final 31 features + target across all four datasets into one unified dataset for modeling.

5. Trained the Voting Ensemble; cross-validated accuracy reached **95%**.

6. Used `sklearn.treeinterpreter` to extract the most influential features driving predictions.



---



## Key Findings



Housing security is the strongest predictor of SNAP eligibility. The four most impactful features all relate to housing costs and deductions:

- **FSSLTDED** and **SHELDED** reflect how much a household pays for housing.

- **FSTOTDED** and **FSSTDDE2** are allowable housing-related deductions.



---



## Next Steps



1. Layer in geographic data — HUD GIS resources, food pantry locations, and county-level SNAP dependency rates — to identify specific areas where intervention would have the greatest impact.

2. Publish results to an interactive web map (e.g., Leaflet.js) for broader accessibility.



---



## Project Files



**Notebooks:**

[1_EDA](1_EDA.ipynb) | [2_Correlations](2_Correlations.ipynb) | [3_Model](3_Model.ipynb) | [4_Predictions](4_Predictions.ipynb) | [5_Insights](5_Insights.ipynb)



**Folders:**

[Data](data) | [Python Code](python_code) | [Images](images)



**Other:** [Final Model](final_model.sav)



---



## Resources

- [SNAP Quality Control Datasets](https://www.fns.usda.gov/resource/snap-quality-control-data)

- [HUD GIS Tools](https://www.hudexchange.info/programs/coc/gis-tools/)