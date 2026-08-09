---
tags:
  - aagam_shah
  - atefeh_mahdavi
  - ayon_ghosh
  - bernard_kai_wittmaack
  - brendan_turpin
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/hr
  - business_area/hybris_product_recommendations_(digital)
  - business_area/loyalty_program_redesign
  - business_area/win-on-waste_(hotel_operations)
  - douglas_bedell
  - erick_alfaro
  - glen-erik_cortez
  - ignacio_villasmil
  - jesse_bausell
  - kartik_ullal
  - kevin_diaz
  - lamis_amer
  - mahshad_shariatnasab
  - michelle_manfrini
  - project/cltv-drivers_model_development
  - project/co-brand_credit_card_pilot
  - project/division-level_medallia_reports
  - project/enhanced_for_you_recommendations
  - project/improved_forecasting_accuracy
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/offer_to_cancel_(oftocx)_model_(rci_&_cel)
  - raw
  - reza_bahadori
  - weekly_update
date: "2025-05-16"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2025-05-16

## Update 1

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

- Working towards copilot migration contract and working to understand how to implement GenAI for the IVR. - Working with IT to identify a project manager for migration and get initial conversations going
- Working to get HCL vendor onboarded
-Working to get HCL T&M contracts
- Celebrity IVR updates: Disambig, river, new FAQs
- Royal IVR updates: Disambig, casino, new FAQs
- Updating IVR Reporting to have new implementation points.

### Raw Update

- Working towards copilot migration contract and working to understand how to implement GenAI for the IVR.
- Working with IT to identify a project manager for migration and get initial conversations going
- Working to get HCL vendor onboarded
-Working to get HCL T&M contracts
- Celebrity IVR updates: Disambig, river, new FAQs
- Royal IVR updates: Disambig, casino, new FAQs
- Updating IVR Reporting to have new implementation points.

---

## Update 2

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

- Casino and international forecasts
- Working with internationl team to take forecasts to convert them to insights for workforce planning
- Working with enterprise DS team to scale and standardize

### Raw Update

- Casino and international forecasts
- Working with internationl team to take forecasts to convert them to insights for workforce planning
- Working with enterprise DS team to scale and standardize

---

## Update 3

**Date:** 2025-05-16
**Business Area:** Loyalty
**Business Project:** Co-Brand Credit Card Pilot
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Prepared analysis on early peaking to PCP on both brands. Celebrity was previously done by Alex Correa's team, but I have taken this over and updated the outputs. Utililized Digital Data to get app user population.

### Raw Update

Prepared analysis on early peaking to PCP on both brands. Celebrity was previously done by Alex Correa's team, but I have taken this over and updated the outputs.
Utililized Digital Data to get app user population. Steerco suggested we could reach a larger population via app push notifications. The additional lift from app users based on clickstream data is not significant enough to increase testing feasibility or additional segments. Prepared additional analysis on status match guests, but this will not be shared during the steerco, as loyalty leadership wants to avoid the sensitive topic of status match without Kara's attendance. Updated cost of celebrity pilots to adjust AI inclusions, and updated Lauren. Discovered that too many guests were being tagged as AI and costs were overstated.

---

## Update 4

**Date:** 2025-05-16
**Business Area:** HR
**People:** Unidentified

### Summarized Update

CLV:
Finished Celebrity Driver analysis and segmentation. Had a working session with brand leadership (Brian, Scheiner and Craig) to present findings. They were excited about the findings, and are looking forward to implementing them throughout the business through pilots.

### Raw Update

CLV:
Finished Celebrity Driver analysis and segmentation. Had a working session with brand leadership (Brian, Scheiner and Craig) to present findings. They were excited about the findings, and are looking forward to implementing them throughout the business through pilots. We have begun a roadshow with several business groups to find additional use-cases.

---

## Update 5

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

- updated input query to booking level with some additional columns to test with (mainly just accessory columns to match on)
- theres good matches, but i think with like half the # of ids to match on (compared to inidividual passengers), along with the booking aggregation introducing more diversity in the data, i think it makes sense for me to put more effort in ensuring the matches are reasonable (been working on it/currently working on this)
- have an idea on including hard matching (tangentially) from yesterday's convo, since technically atm all the considered columns are all soft matched (since its all fed to PCA and then knn'd). havent worked on it yet, but i think its a fairly doable modification. basically just filter the cohorts to match on.

### Raw Update

- updated input query to booking level with some additional columns to test with (mainly just accessory columns to match on)
- theres good matches, but i think with like half the # of ids to match on (compared to inidividual passengers), along with the booking aggregation introducing more diversity in the data, i think it makes sense for me to put more effort in ensuring the matches are reasonable (been working on it/currently working on this)
- have an idea on including hard matching (tangentially) from yesterday's convo, since technically atm all the considered columns are all soft matched (since its all fed to PCA and then knn'd). havent worked on it yet, but i think its a fairly doable modification. basically just filter the cohorts to match on. just a matter of if we do want to go with doing this, so its not top of my list of priorities
- theres 11 booking ids (5 in 5/16 FR, 6 in 5/30 FR) i cant find details on in pilots_spend_index (which i was using to get the aformentioned accessory columns), which was odd, but minor.  removing them for now, but just noting it

---

## Update 6

**Date:** 2025-05-16
**Business Area:** Win-on-Waste
**Business Project:** Improved Forecasting Accuracy
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

WOW Updates 5-15-2025:
1) wow metrics in development
2) wow cold start PL in development
3) MDR and specialty improved PL developed
4) developed and tested to map change of schema in FPMS couchbase

### Raw Update

WOW Updates 5-15-2025:
1) wow metrics in development
2) wow cold start PL in development
3) MDR and specialty improved PL developed
4) developed and tested to map change of schema in FPMS couchbase

---

## Update 7

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]]

### Summarized Update

-HVAC area baseline updated for entire fleet
-Silver Nova added to service power area (features filtering/model tunning)
-Adventure model updated for service power area
-Service Power area baseline for entire fleet updated
-R&D on heat loss in pools - New Build
-R&D on Load Factor New Build

### Raw Update

-HVAC area baseline updated for entire fleet
-Silver Nova added to service power area (features filtering/model tunning)
-Adventure model updated for service power area
-Service Power area baseline for entire fleet updated
-R&D on heat loss in pools - New Build
-R&D on Load Factor New Build

---

## Update 8

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

Completed
-Added persisting of dataframes to 2 high-compute MIAP ETL tasks in attempt to improve fault tolerance for partitioned datasets when writing to a table
-Troubleshooted and remediated data gap for Eniram propulsion sensor on IC
-Added support for categorical features in ORBM library
-Performed feature engineering, EDA, and initial model development for Hull Degradation models (one model per coating type) in support of the Fuel Forecast project
-Had session with junior developer on development best practices and productionization of new workflow
In Progress (next week)
-Fine tuning, workflow creation, and applying best practices to Hull Degradation models

### Raw Update

Completed
-Added persisting of dataframes to 2 high-compute MIAP ETL tasks in attempt to improve fault tolerance for partitioned datasets when writing to a table
-Troubleshooted and remediated data gap for Eniram propulsion sensor on IC
-Added support for categorical features in ORBM library
-Performed feature engineering, EDA, and initial model development for Hull Degradation models (one model per coating type) in support of the Fuel Forecast project
-Had session with junior developer on development best practices and productionization of new workflow
In Progress (next week)
-Fine tuning, workflow creation, and applying best practices to Hull Degradation models

---

## Update 9

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

-fixed bug in power plant monthly report notebook, causing workflow to fail
-created new feature for count of running diesel engines to aid in EDA in other initiatives
-worked on adding mode_fuel_only{hfo, mgo, lng}_de tags, boolean tags for when all engines are running same type of fuel
-implemented fuel temp, flow, and engine room mapping YAML file for power plants.

### Raw Update

-fixed bug in power plant monthly report notebook, causing workflow to fail
-created new feature for count of running diesel engines to aid in EDA in other initiatives
-worked on adding mode_fuel_only{hfo, mgo, lng}_de tags, boolean tags for when all engines are running same type of fuel
-implemented fuel temp, flow, and engine room mapping YAML file for power plants.

---

## Update 10

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[mahshad_shariatnasab/overview_mahshad_shariatnasab|Mahshad Shariatnasab]]

### Summarized Update

-Visited IC ship
-Added AX, AT, BY to the boiler and GMO plots
-Fixed AHU plots issue for GMO for ML class
-Worked on adding LNG feature to the boiler model
-Worked on fixing issue of boiler model for IC and UT
-Detect 300kW power deviation on AHU for WN for Public, Stairs and Cabin

### Raw Update

-Visited IC ship
-Added AX, AT, BY to the boiler and GMO plots
-Fixed AHU plots issue for GMO for ML class
-Worked on adding LNG feature to the boiler model
-Worked on fixing issue of boiler model for IC and UT
-Detect 300kW power deviation on AHU for WN for Public, Stairs and Cabin

---

## Update 11

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

-I customized the logic of the ENIRAM API within the Databricks notebook. -I added widgets and conducted tests with all available vessels (total of 40). -Additionally, I analyzed 2 Gangway notebooks and reviewed the Corporate Data Modeling documentation.

### Raw Update

-I customized the logic of the ENIRAM API within the Databricks notebook.
-I added widgets and conducted tests with all available vessels (total of 40).
-Additionally, I analyzed 2 Gangway notebooks and reviewed the Corporate Data Modeling documentation.

---

## Update 12

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

# Siren
Call Transcripts Backfilling for Liveperson comparative analysis and monitoring
- All transcript topic classifications have been backfilled for 2025 up to May 12th. - Working with stakeholder to create queries to compare Liveperson to Contact Center.

### Raw Update

# Siren
Call Transcripts Backfilling for Liveperson comparative analysis and monitoring
- All transcript topic classifications have been backfilled for 2025 up to May 12th.
- Working with stakeholder to create queries to compare Liveperson to Contact Center.

---

## Update 13

**Date:** 2025-05-16
**Business Area:** Hybris Product Recommendations (Digital)
**Business Project:** Enhanced For You Recommendations
**People:** Unidentified

### Summarized Update

# Recommender
- Implemented upgrade to ForYou Recommender which allows frontend to request recommendations. This uses the existing ForYou recommender allowing for the frontend to request one or more categories with the API responding for products for each category.

### Raw Update

# Recommender
- Implemented upgrade to ForYou Recommender which allows frontend to request recommendations. This uses the existing ForYou recommender allowing for the frontend to request one or more categories with the API responding for products for each category.

---

## Update 14

**Date:** 2025-05-16
**Business Area:** Medallia
**Business Project:** Division-Level Medallia Reports
**People:** Unidentified

### Summarized Update

- Fixed existing GenAI pipelines to account for interport sailings. Survey responses for interport sailing should roll up to the Master sailing. - Need to fix formatting bug with Fleet level report email.

### Raw Update

- Fixed existing GenAI pipelines to account for interport sailings. Survey responses for interport sailing should roll up to the Master sailing.
- Need to fix formatting bug with Fleet level report email.

---

## Update 15

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

BKTOCX
- Sent test file to Siebel successfully. - Need to set up Siebel with a mapping to new incoming lead categories. Without setting up siebel with the mapping for Mireilles files - the incoming data is rejected.

### Raw Update

BKTOCX
- Sent test file to Siebel successfully.
- Need to set up Siebel with a mapping to new incoming lead categories. Without setting up siebel with the mapping for Mireilles files - the incoming data is rejected.

---

## Update 16

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

- INGESTION: Aligned with DE on setting up much improved process for data required at inference time. - SCORING: Need to make a final update to CTI pipeline to adjust for changes to Ingestion process. - PUSH TO PROD:  Coordinating with Platform and DE to set up Databricks Volume ALDS mount point for both Dev and Prod environments.

### Raw Update

- INGESTION: Aligned with DE on setting up much improved process for data required at inference time.
- SCORING: Need to make a final update to CTI pipeline to adjust for changes to Ingestion process.
- PUSH TO PROD:  Coordinating with Platform and DE to set up Databricks Volume ALDS mount point for both Dev and Prod environments. This will be the method of choice for pushing data back to Siebel.

---

## Update 17

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

- Created self serve Databricks Dashboard for Craig & team for Return Rate matrix.

### Raw Update

- Created self serve Databricks Dashboard for Craig & team for Return Rate matrix.

---

## Update 18

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Creating a step-by-step screenshot guide for navigating and using the Litigations app.

### Raw Update

Creating a step-by-step screenshot guide for navigating and using the Litigations app.

---

## Update 19

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Refining the presentation deck on app engagement analysis in preparation for review with Heather.

### Raw Update

Refining the presentation deck on app engagement analysis in preparation for review with Heather.

---

## Update 20

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Update for IBP:
Completed:
• Updated the Order Creation dataset to ensure that the demand forecasts used in the dataset are the voyage level demand forecasts which account for forecasted passengers rather than prorating the monthly demand forecasts using a straight allocation to each voyage. • Delivered on Cococay model to Yan, will deliver to Fanny next week unless she decides to change our meeting time. • Delivered on automated reports on consumption and spend, pending review from Lauren.

### Raw Update

Update for IBP:
Completed:
• Updated the Order Creation dataset to ensure that the demand forecasts used in the dataset are the voyage level demand forecasts which account for forecasted passengers rather than prorating the monthly demand forecasts using a straight allocation to each voyage.
• Delivered on Cococay model to Yan, will deliver to Fanny next week unless she decides to change our meeting time.
• Delivered on automated reports on consumption and spend, pending review from Lauren.
Working on:
• Investigating demand forecasts on Tilapia Fish in 2025 that are excessively high. Isolated the main erroneous forecast to Radiance of the Seas. We audited the SHAP values from May to April, where April was normal and May was excessively high. We found that there are two features driving the excessively high forecasts in May; NORMALIZED_CONSUMPTION_LAST_52WKS_STD and SEASONAL_NORMALIZED_CONSUMPTION_LAST_52WKS. The large jumps in SHAP values for these features are not due to a change in the underlying feature values—they are both still zero at prediction time.
Instead, the model’s internal mapping from input to output (i.e., the model’s coefficients or structure) must have changed dramatically—now, a zero value for these features is treated as a dominant positive predictor instead of a negative or neutral one.
o Solution to resolve is two-fold:
o Step 1: Implement monotonicity constraints for the following sets of predictors in the RCI / CCI Model (This work is Completed)
Feature Monotonicity Constraint Direction Rationale
CONSUMPTION_LAST_4WKS, 4WKMA, etc.  Yes +1  More past use = should forecast more
NORMALIZED_CONSUMPTION variants Yes +1  More normalized demand = more forecast
SEASONAL_NORMALIZED_CONSUMPTION variants  Yes +1  More seasonal normalized = more forecast
PAX, FCST_PAX, PAX_*WKMA  Yes +1  More passengers -> more consumption
o Step 2: Add new guardrail on all forecasts where if the current model training date month has a demand forecast for the prediction month/year that is over 100% from the prior model training date month for the given prediction month to cap the current model training date’s prediction at max 100% increase in the forecast from prior month (work in process)
o We have communicated to the business our plan to resolve and that the vast majority of forecasts in May can be relied upon as the code hasn’t changed from April to May, rather this situation was an isolated event due to model training anomaly.
• Fixing workflows for uniform rci/cci and medical rci/cci to be able to run different model types for best forecast (to be completed potentially tomorrow or early next week).
• Uniforms Silversea completed guardrails process and will continue on this soon.
• Generated a high level reports on all models but want to fix the format and implement the use of AI as talked about in our lunch and learn meeting this week.
Pending:
• Silversea and celebrity will be needed soon
• Merging all three brands and fixing the categories will be needed soon

---

## Update 21

**Date:** 2025-05-16
**Business Area:** Customer Lifetime Value (Corporate Planning)
**Business Project:** CLTV-Drivers Model Development
**People:** Unidentified

### Summarized Update

- work on fixing on-premise server, since the dashboard runs there and it stoped working. Also research in moving the dashboard to databricks apps (streamlit)
- support business on questions related to epsilon and models behavior.

### Raw Update

- work on fixing on-premise server, since the dashboard runs there and it stoped working. Also research in moving the dashboard to databricks apps (streamlit)
- support business on questions related to epsilon and models behavior.

---

## Update 22

**Date:** 2025-05-16
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** Unidentified

### Summarized Update

BKTOCX:
LEADS Scoring ETL for all lead types
1. Royal (6): BKTOCX, OFTOCX_CC, OFTOCX_WEB, CX, PGR_DIRECT_GROUPS, PGR_DIRECT_WEB
2. Celebrity (8): BKTOCX, CX_ONBOARD, CX, BKTOCX_ONBOARD, OFTOCX_WEB, OFTOCX_CC, PGR_DIRECT_WEB, PGR_DIRECT_GROUPS.

### Raw Update

BKTOCX:
LEADS Scoring ETL for all lead types
1.       Royal (6): BKTOCX, OFTOCX_CC, OFTOCX_WEB, CX, PGR_DIRECT_GROUPS, PGR_DIRECT_WEB
2.       Celebrity (8): BKTOCX, CX_ONBOARD, CX, BKTOCX_ONBOARD, OFTOCX_WEB, OFTOCX_CC, PGR_DIRECT_WEB, PGR_DIRECT_GROUPS.
A. Load and preprocess the data for all the lead types for Royal and Celebrity.
1.       Build a child notebook that takes parameters such as 'lead_type' and 'Brand', and saves a dataframe for each lead type.
2.       Build a parent notebook that is fed by different parameters to execute the child notebook.
B. Get the features engineering of all the lead types for Royal and Celebrity
1.       Build a child notebook that takes parameters such as dataset for each lead type, output file name
2.       Build a parent notebook that is fed by different parameters to execute the feature engineering child notebook.
C.ETL process for LEADS Scoring of each lead type for Royal
3.  Build a child notebook with functions that take parameters such as lead type, brand, table name, model name, data path, and probability threshold.
4.  Construct a parent notebook that calls all the functions of the child notebook, feeding in parameters related to each lead type.
5.  Scored leads are saved in the Unity Catalogue.
6.  Map the output to the required format, the results are saved in CSV format.
7.  Scored leads are split into Sval, Hval, Mval, and Lval.
8.  Build function to write scored leads to an SFTP (SSH File Transfer Protocol) location, which runs only if there are leads to score.
9.  Reviewed the name of the CSV file that will be written to the SFTP location.
Before: cvp_lead_load_da2i_prod_{lead_type}_Leads_SVAL_{model}_{current_date}_{Brand}.csv
Next: (cvp_lead_load_da2i_{lead_type}_SVAL_{model}_{date}_{time_hour}_{Brand}_test.csv")
Now:cvp_lead_load_da2i_{lead_type}_SVAL_{model}_{date}_{time_hour}_{Brand}_stage.csv"
10. Reviewed the contain the dropped files.
11. With the teams, we performed testing to SFTP location successfully
NEXT: ETL process for LEADS Scoring of each lead type for Celebrity (Expect to finish by Tuesday)
NEXT: Monitor the ETL for each lead type (expect to finish by next week)
1.       At each run, we saved a reference dataset
2.       From the reference dataset, we count the number of leads to be score
3.       If there is no lead to score, then lead_dataset to be score is not updated
4.       Otherwise, we updated the lead dataset
NEXT : Control of the sequence ID for each lead type (expect to finish by next week)
1-       The dataset is pulled based on the last saved sequence ID
2-       The lead dataset is not updated if the number of leads to score is zero (actually if reference  dataset = 0)
Pipeline Refresh and Data Alignment: Ongoing with Kiana and Erick.

---

## Update 23

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

We had our Workforce Planning meeting with Jason Atkerson on 05/14/2025 at 2:30 p.m. The main take away from this meeting are:
-          A workforce planning simulation is needed
-          Goal: get a better accurate staffing number for the contact center
-          Service level: 80% of call answer within 40 seconds
-          Key driver: minimizing the abandoned rate
-          There is an existing process that accounts for call volume, AHT and shrinkage
-          Next meeting is planning to go through the excel file to understand the context of the existing process and identify the next steps. -          Scope: North America

### Raw Update

We had our Workforce Planning meeting with Jason Atkerson on 05/14/2025 at 2:30 p.m.
The main take away from this meeting are:
-          A workforce planning simulation is needed
-          Goal: get a better accurate staffing number for the contact center
-          Service level: 80% of call answer within 40 seconds
-          Key driver: minimizing the abandoned rate
-          There is an existing process that accounts for call volume, AHT and shrinkage
-          Next meeting is planning to go through the excel file to understand the context of the existing process and identify the next steps.
-          Scope: North America

---

## Update 24

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

RCI | SPI Factor | EDA on GTY to Lead Gap and #GTY cabins
o This week I focused on doing EDA to understand the interaction between GTY_Lead_Gap Perc and SPI Scores, and trying to understand benchmarks for good SPI sailings. o Feature engineering: I created a new variable that captures the interaction between GTY Price and bookings, as well as Lead Price and bookings at a Weeks to Sail (WTS) level. o Next Steps: I will run an XGBoost model to assess the importance of these factors on SPI scores and to establish appropriate benchmarks
o Challenges Faced: During quality checks, I discovered that for some weeks, there were bookings for GTYs and Leads, but the pricing was set to 0.

### Raw Update

RCI | SPI Factor | EDA on GTY to Lead Gap and #GTY cabins
o This week I focused on doing EDA to understand the interaction between GTY_Lead_Gap Perc and SPI Scores, and trying to understand benchmarks for good SPI sailings.
o Feature engineering: I created a new variable that captures the interaction between GTY Price and bookings, as well as Lead Price and bookings at a Weeks to Sail (WTS) level.
o Next Steps: I will run an XGBoost model to assess the importance of these factors on SPI scores and to establish appropriate benchmarks
o Challenges Faced: During quality checks, I discovered that for some weeks, there were bookings for GTYs and Leads, but the pricing was set to 0. I resolved this by removing 'Direct Off-Tariff' from the channel column in the VCAP data. These are ECR or ECCR

---

## Update 25

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

RCI | Overselling | Model Training Code uses MLFlow to log model to env_catalog
•  Status: This ticket is complete as of 5/15/2025
• To validate the model, I created a simulation example that forecasts cancellations forward — allowing us to evaluate how the model performs in a real-world setting. • I compared the predicted cancellation probabilities against actual historical outcomes over time. • The output of model is survival curves, which shows how the probability of non-cancellation changes as the sailing date nears.

### Raw Update

RCI | Overselling | Model Training Code uses MLFlow to log model to env_catalog
•  Status: This ticket is complete as of 5/15/2025
• To validate the model, I created a simulation example that forecasts cancellations forward — allowing us to evaluate how the model performs in a real-world setting.
• I compared the predicted cancellation probabilities against actual historical outcomes over time.
• The output of model is survival curves, which shows how the probability of non-cancellation changes as the sailing date nears. In addition, I evaluated model performance using accuracy metrics specific to survival analysis, including the concordance index (C-index), the time-dependent AUC curve, and the Brier score. These metrics help assess how well the model ranks cancellation risk and predicts survival probabilities.

---

## Update 26

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

• Outlier Removal:
Applied a 2.5 standard deviation rule within each group defined by (meta_product, cat_class) to remove extreme observations and clean the data. • Feature Engineering:
Created categorical features: ship_class, rdss_product_code, bin_str, sailing_season_2, rdss_product_group_1, sailing_nights_bin_1. Engineered numeric features: wts, peak_season_flag, sail_month, holiday_flag, weekend_sailing_flag, sail_nights.

### Raw Update

• Outlier Removal:
Applied a 2.5 standard deviation rule within each group defined by (meta_product, cat_class) to remove extreme observations and clean the data.
• Feature Engineering:
Created categorical features: ship_class, rdss_product_code, bin_str, sailing_season_2, rdss_product_group_1, sailing_nights_bin_1.
Engineered numeric features: wts, peak_season_flag, sail_month, holiday_flag, weekend_sailing_flag, sail_nights.
Applied target encoding to categorical variables.
• Model Training:
Built models across multiple booking windows with weekly bin sizes of 1, 5, 10, and 20.
For each (meta_product_code, cat_class), executed polynomial feature expansion (degree 2) and used StandardScaler for normalization.
• Demand Elasticity Analysis:
Calculated point price elasticity via a 3% synthetic price increase to evaluate demand responsiveness.
Visualized key findings; integrated with MLflow for tracking models, parameters, metrics, and artifacts.

---

## Update 27

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

CEL/RCI:
- Identified systematic bias in SPI scoring model for both brands using XGBoost regressor trained on SPI scores and SHAP to rank feature importance. - Additional normalization by rdss product code and sailing nights significantly reduced bias in most meta product, but more surgical approach needs to be taken for Europe based on port groupings. - Story stays qualitatively the same for sailing management targets gleaned so far from SPI scores (e.g., push off-peak booking curve further out).

### Raw Update

CEL/RCI:
- Identified systematic bias in SPI scoring model for both brands using XGBoost regressor trained on SPI scores and SHAP to rank feature importance.
- Additional normalization by rdss product code and sailing nights significantly reduced bias in most meta product, but more surgical approach needs to be taken for Europe based on port groupings.
- Story stays qualitatively the same for sailing management targets gleaned so far from SPI scores (e.g., push off-peak booking curve further out).

---

## Update 28

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

- Produced data-driven sailing baskets based on correlated residuals for sailing volume from RCI elasticity model
- Overall agreement between heuristically labeled baskets and data-driven baskets is strong, with >80% overlap for all major meta products.

### Raw Update

- Produced data-driven sailing baskets based on correlated residuals for sailing volume from RCI elasticity model
- Overall agreement between heuristically labeled baskets and data-driven baskets is strong, with >80% overlap for all major meta products.

---

## Update 29

**Date:** 2025-05-16
**Business Area:** Hybris Product Recommendations (Digital)
**Business Project:** Enhanced For You Recommendations
**People:** Unidentified

### Summarized Update

- Guidance for un-basketed sailings comes solely from SPI targets as opposed to weighted combination of SPI and historical sailing basket booked positions.

### Raw Update

- Guidance for un-basketed sailings comes solely from SPI targets as opposed to weighted combination of SPI and historical sailing basket booked positions.

---

## Update 30

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[douglas_bedell/overview_douglas_bedell|Douglas Bedell]]

### Summarized Update

CEL | FIT Re-berthing
o               Category correction coded. Data to business for validation. o               Occupancy correction coded.

### Raw Update

CEL | FIT Re-berthing
o               Category correction coded. Data to business for validation.
o               Occupancy correction coded. Data to business for validation.
o               5/13 Revenue planning has provided Celebrity PlusGrade data. Incorporated into process code

---

## Update 31

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Rebirthing Ticket: Douglas has been working on the rebirthing ticket, which is on schedule to be completed by the end of the month. He is currently fine-tuning the work and expects to have it ready by the end of the week. Category Correction: Douglas is working on category correction and moving output data.

### Raw Update

.
Rebirthing Ticket: Douglas has been working on the rebirthing ticket, which is on schedule to be completed by the end of the month. He is currently fine-tuning the work and expects to have it ready by the end of the week.
.
Category Correction: Douglas is working on category correction and moving output data. He discussed the need to move tables and perform validation, which may roll over to June.
.
Subtasks: Douglas will add subtasks as he progresses, and some tasks may roll over to June depending on the speed of completion.

---

## Update 32

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[jesse_bausell/overview_jesse_bausell|Jesse Bausell]]

### Summarized Update

SSC | PRE | Design PRE A/B Test
A/B testing: voyage selection
o This week I led a project to find cryptic SSC re-bookings that could be costing SSC revenue. I also further scoped out A/B testing with SSC Revenue and Business teams. We planned expanding A/B testing to multiple sailings areas (e.g., Alaska, Mediterranean, and Caribbean), and how best to compare these sailings to each other - despite their differences.

### Raw Update

SSC | PRE | Design PRE A/B Test
A/B testing: voyage selection
o This week I led a project to find cryptic SSC re-bookings that could be costing SSC revenue. I also further scoped out A/B testing with SSC Revenue and Business teams. We planned expanding A/B testing to multiple sailings areas (e.g., Alaska, Mediterranean, and Caribbean), and how best to compare these sailings to each other - despite their differences.

---

## Update 33

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

• CEL | GTY-LEAD 2.0
o Minor updates made to sailing data as requested by business. o Visualizations created for analyst training. • CEL | GTY-LEAD 3.0
o Currently using higher level models for lower-upper, upper-deluxe, lower-deluxe that are at ship-class, cat-class, WTS level.

### Raw Update

• CEL | GTY-LEAD 2.0
o Minor updates made to sailing data as requested by business.
o Visualizations created for analyst training.
• CEL | GTY-LEAD 3.0
o Currently using higher level models for lower-upper, upper-deluxe, lower-deluxe that are at ship-class, cat-class, WTS level. Models are trained on bookings that are one of the two tiers for each gap. Instead, will shift to include bookings that are either first tier and all above (such as format for gty-lead). This will allow for more variability in the data and provides a stronger basis for nested approach sued on optimization. Also, will include a "lead type" feature in model as was done for gty-lead to differentiate when customer trades up from a lower to an upper or deluxe, for example.
o Finalized first version of optimization. Considers all possible combinations in a cat-class that could include gty, lower, upper, deluxe. AM making updates to trade-up models that will require changes to optimization code. Updates in progress. Meeting with business next week to review initial results and receive feedback.
• RCI | GTY-LEAD 3.0
o Similar updates must be made to RCI models. Currently using higher level models that are at ship-class, cat-class, WTS level. Models are trained on bookings that are one of the two tiers for each gap. Instead, will shift to include bookings that are either first tier and all above (such as format for gty-lead). This will allow for more variability in the data and provides a stronger basis for nested approach sued on optimization. Also, will include a "lead type" feature in model as was done for gty-lead to differentiate when customer trades up from a base to bronze or silver, for example.
o Initial version of optimization completed. Considers all possible combinations in a cat-class that could include gty, base, bronze, silver. Will review with business at next meeting. This optimization will need to be updated as the trade-up models are changed.
o Awaiting business response to set up results review.

---

## Update 34

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

CEL | Elasticity Upgrades | Testing WTS binning based on booked volume
• Status: This ticket is complete as of 5/14/2025
• Deliverables:
1. Tested WTS binning logic separately for each product: SHORT CARIBBEAN, 7N CARIBBEAN, EUROPE, and ALASKA. Looked at booking volume patterns and used smaller bins where bookings were high, and larger bins where bookings were low or rare.

### Raw Update

CEL | Elasticity Upgrades | Testing WTS binning based on booked volume
• Status: This ticket is complete as of 5/14/2025
• Deliverables:
1.  Tested WTS binning logic separately for each product: SHORT CARIBBEAN, 7N CARIBBEAN, EUROPE, and ALASKA.
Looked at booking volume patterns and used smaller bins where bookings were high, and larger bins where bookings were low or rare.
2.  For EUROPE and ALASKA, used a mix of bin sizes based on WTS windows:
• Larger bins (15 or 10) closer to sailing (0–35 WTS),
• Smaller bins (5) in peak demand range (35–55 WTS),
• Larger bins again (10–15) for the far-out WTS (55–105).
This pattern worked well for both.
3.  Applied the same binning logic to 7N CARIBBEAN after trying other custom logics that didn’t help.
Metrics stayed stable—no gains but no loss in model performance.
4.  For SHORT CARIBBEAN, found a custom binning setup that gave better R².
Used a combination of bin sizes:
• 0–10 WTS (10),
• 10–35 WTS (5),
• 35–55 WTS (10),
• 55–105 WTS (20).
• QQ plot didn’t change, but R2 improved.
5.  Used PySpark instead of SQL because SQL queries were taking too long to run.
PySpark made it easier and faster to test different binning setups.
6.  Planning to apply the same binning logic to VPS pricing next.
Need to find out how the VPS price column is pulled in the pipeline before proceeding.
• Potential future issue: None

---

## Update 35

**Date:** 2025-05-16
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

These tasks for pushing to production have been delayed and pushed back due to new dependent additional adjustments to the optimization for making the price recommendations. These need to be completed before it is ready to move to production. Demand Penalty Weights in Optimization:
Added penalty weights based on historical demand variability to prevent over-optimistic demand targets.

### Raw Update

These tasks for pushing to production have been delayed and pushed back due to new dependent additional adjustments to the optimization for making the price recommendations. These need to be completed before it is ready to move to production.
1.   Demand Penalty Weights in Optimization:
Added penalty weights based on historical demand variability to prevent over-optimistic demand targets. Calculated z-scores and CDFs for demand distributions; implemented three methods, with the first—multiplying weekly demand rate by penalty weights—yielding the best, more realistic results for revenue optimization.
2.  Inclusion of Target Revenues from OBR:
Integrated OBR’s target revenue figures into the optimization as additional penalty weights to align price and demand recommendations with expected revenue targets. Also adjusted constraints on demand and price variances to better match historical distributions and expectations.

---

## Update 36

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[kartik_ullal/overview_kartik_ullal|Kartik Ullal]]

### Summarized Update

CEL | PERKS/NO PERKS AB TEST | Monitoring Analysis 2.0
Merge 2024 test and 2025 test data for analysis
• Merged 2024 All included test and 2025 All Included test to see if the groups performed the same overall or if we need to change the gaps between perks no perks. • This analysis confirmed both the findings in 2025 test and 2024 test. The difference in gaps depend on Meta and Season (Peak/Offpeak).

### Raw Update

CEL | PERKS/NO PERKS AB TEST | Monitoring Analysis 2.0
Merge 2024 test and 2025 test data for analysis
• Merged 2024 All included test and 2025 All Included test to see if the groups performed the same overall or if we need to change the gaps between perks no perks.
• This analysis confirmed both the findings in 2025 test and 2024 test. The difference in gaps depend on Meta and Season (Peak/Offpeak). Europe can have higher gaps for Perks based on the test.
Add Itinerary/Port to data and do the analysis for Europe.
Perform analysis on Sailing Year and Trf/T4 for each Meta and Season
• Added Sailing Year analysis for 7N Caribbean and Alaska, to see how the trade up has been affected for the year 2025 and 2026 seperately.
• Added anlaysis for Trf/T4 sailings for 7n Caribbean and Short Caribbean.
• Added Itinerary, Port and Percent of Sea days analysis for Europe to determine whether there is difference in trade up for gaps. Less number of sea days would mean that All Included not much beneficial.

---

## Update 37

**Date:** 2025-05-16
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Model Testing and Validation on all sailings where p(d) model is trained
• Dynamic Programming Optimization:
Fine-tuned the logic by running on finer granularity (every 5 WTS, bkgs increasing in steps of 2 within bounds) on two sample 7N Caribbean sailings. Improved memoization caching for efficiency and added a penalty term for overbooking (currently arbitrary, pending sensitivity analysis). • Presentation Preparation:
Worked on a PowerPoint presentation scheduled for tomorrow’s business review.

### Raw Update

Model Testing and Validation on all sailings where p(d) model is trained
• Dynamic Programming Optimization:
Fine-tuned the logic by running on finer granularity (every 5 WTS, bkgs increasing in steps of 2 within bounds) on two sample 7N Caribbean sailings. Improved memoization caching for efficiency and added a penalty term for overbooking (currently arbitrary, pending sensitivity analysis).
• Presentation Preparation:
Worked on a PowerPoint presentation scheduled for tomorrow’s business review.
• Revenue Lift Observations (SY-2024-03-09 sailing):
Compared models:
• LP/NLP: 8.44% uplift
• DP: 8.07% uplift
(Note: Price elasticity model tends to underpredict prices)
• Sampling-based greedy approach: 40.32% uplift (unrealistically high, as it overfills the ship at 40 WTS; needs model adjustments).
• Model Adjustments & Findings:
At WTS 40 and 10, used mean and std of booked percentage to anchor cumulative bookings—this will be incorporated into the model.
The greedy approach predicts point estimates for price, then samples residuals to maximize revenue; validation of this method is pending.

---

## Update 38

**Date:** 2025-05-16
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)
**People:** Unidentified

### Summarized Update

• Exploratory Data Analysis (EDA):
Currently focused on incorporating demand uncertainty into the optimization; progress limited this week. • Demand Normalization Approach:
Computed exposure-based demand by analyzing bookings relative to the number of weeks a price was offered. This involved, for each combination of meta, ship_code, sail_month, cat_class, and wts_10_bins:
• Discretizing prices and calculating total bookings at each price point
• Dividing bookings by the number of weeks the price was available to differentiate between no bookings and no price offerings
• Visualization & Insights:
Created heatmaps illustrating booking density across prices and wts bins.

### Raw Update

• Exploratory Data Analysis (EDA):
Currently focused on incorporating demand uncertainty into the optimization; progress limited this week.
• Demand Normalization Approach:
Computed exposure-based demand by analyzing bookings relative to the number of weeks a price was offered. This involved, for each combination of meta, ship_code, sail_month, cat_class, and wts_10_bins:
• Discretizing prices and calculating total bookings at each price point
• Dividing bookings by the number of weeks the price was available to differentiate between no bookings and no price offerings
• Visualization & Insights:
Created heatmaps illustrating booking density across prices and wts bins.
For example, on 7N Caribbean, SY in February (non-holiday), similar booking densities at 60 WTS were observed for APD prices ranging between 160 and 210.
This understanding supports more informed pricing strategies aimed at maximizing revenue without reducing booking rates.

---

## Update 39

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

EXCITED:

### Raw Update

EXCITED:

---

## Update 40

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Performed feature engineering, EDA, and initial model development for Hull Degradation models (one model per coating type). PROPEL OBR (Alejandro):
Developed and deployed Feature Store for both categories and product classes in dev. This includes features metadata, timeseries data and timestamps to start tracking drift and measure models against a holdout dataset.

### Raw Update

Performed feature engineering, EDA, and initial model development for Hull Degradation models (one model per coating type).
PROPEL OBR (Alejandro):
Developed and deployed Feature Store for both categories and product classes in dev. This includes features metadata, timeseries data and timestamps to start tracking drift and measure models against a holdout dataset.
Developed Model promotion framework to manage and retrain all propel models (+160 models).
Added Spend/Save campaign new logo in propel vouchers.
In progress: Streamline of PowerBI dataset refresh process to be done right after offers generation.

---

## Update 41

**Date:** 2025-05-16
**Business Area:** Unclassified
**People:** [[glen-erik_cortez/overview_glen-erik_cortez|Glen-Erik Cortez]]

### Summarized Update

PROUD:
RMA (Eswar):
Unity Catalog Migration:
moved all historical outputs from oracle into Unity Catalog to enable removal of the oracle tables, including REVOREO.TAP_CEL_SUITES_ARCHIVE, REVOREO.CEL_CT_ARCHIVE, REVOREO.CEL_TAP_T4_OUTLIER_LOG, REVOREO.CEL_GROUPS_ARCHIVE, and REVOREO.SINGLES_TAP_LOGGING. Updated the code to ensure that, moving forward, results are appended to these tables in UC, thereby eliminating the need for write-backs to Oracle. Data Validation Framework:
Created a script to extract all tables used within a project, facilitating the application of data validation checks and providing insight into the tables involved prior to execution.

### Raw Update

PROUD:
RMA (Eswar):
Unity Catalog Migration:
moved all historical outputs from oracle into Unity Catalog to enable removal of the oracle tables, including REVOREO.TAP_CEL_SUITES_ARCHIVE, REVOREO.CEL_CT_ARCHIVE, REVOREO.CEL_TAP_T4_OUTLIER_LOG, REVOREO.CEL_GROUPS_ARCHIVE, and REVOREO.SINGLES_TAP_LOGGING.
Updated the code to ensure that, moving forward, results are appended to these tables in UC, thereby eliminating the need for write-backs to Oracle.
Data Validation Framework:
Created a script to extract all tables used within a project, facilitating the application of data validation checks and providing insight into the tables involved prior to execution.
Operations Support:
Resolved QA ADF pipeline deployment failures caused by improper deletion of obsolete pipelines and failure to modify or delete references to these pipelines.
Developed a Databricks workflow that triggers automatically upon file arrival to streamline data processing.
Deployed the TAP_SUITE_CHANGES and TAP_SUITES_UPLOAD workflows to QA and production environments via Asset Bundles.
Monitored CI/CD deployment release runs across ADF, Databricks repositories, and Bundle releases.
Collaborated on and managed pull requests across all rev_mgmt repositories.
MIAP (Brendan)
Improved fault tolerance of 2 high-compute MIAP ETL tasks
Troubleshooted and remediated data gap for Eniram propulsion sensor on IC
Added support for categorical features in ORBM library
Trained junior developer on development best practices and productionization of new workflow
RCGGPT/TechGPT (Eswar):
Plan to add Claude Sonnet model into TechGPT.
Evaluation of cost metrics and request volumes to understand cost consumptions and usage.
GenAI (Alejandro):
In progress: HR Job Description and Standardization Tool development on CoE Sharepoint site.
AI/ML Catalog (Javier):
Continued development of custom metrics for code quality for databricks projects.
Began exploring cost-related data for metrics.
eCommerce (Javier):
Met with Microsoft and eCommerce team to troubleshoot latency issues.
"""

---

_Source: 20250516 - Raw Weekly Rafeh and Matter Reporting (Raw).docx_