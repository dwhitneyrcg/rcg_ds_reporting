---
tags:
  - aagam_shah
  - ayon_ghosh
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/customer_targeting_(e-commerce)
  - business_area/hybris_product_recommendations_(digital)
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/propel_targeted_offers_(cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/revenue_management_automation_(ssc)
  - business_area/supply_chain_optimization
  - business_area/win-on-waste_(hotel_operations)
  - caleb_sharkey
  - camila_aichele
  - carlos_gonzalez_andarcio
  - cristian_villamarin-villamil
  - erick_alfaro
  - glen-erik_cortez
  - ignacio_villasmil
  - jesse_bausell
  - lamis_amer
  - mert_ersoz
  - michelle_manfrini
  - project/beverage_package_optimization
  - project/booking_propensity_models
  - project/casino_spend_analysis
  - project/category_gapping_optimization_3.0
  - project/cococay_integration_and_guardrails
  - project/division-level_medallia_reports
  - project/enhanced_for_you_recommendations
  - project/fare_code_unbundling
  - project/forecasting_pipeline_expansion
  - project/gty-lead_fare_optimization_model_3.0
  - project/historical_data_integration
  - project/miap_operating_efficiency_enhancements
  - project/nps_drivers_analysis_for_alert_system
  - project/offer_template_expansion
  - project/pre_4.0_elasticity_enhancements
  - project/workforce_planning_tool
  - raw
  - weekly_update
date: "2026-02-13"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2026-02-13

## Update 1

**Date:** 2026-02-13
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

MIAP
This Week
Added Modbus source-load logic to the existing shipboard code and successfully deployed the changes to Production. Worked on migrating the Sea Events and VPS ETL jobs, including updating dependencies from Bronze to Silver tables in the Mariner workspace. Completed the initial proof of concept (PoC) for Honeywell data and loaded the data into the respective tables.

### Raw Update

MIAP
This Week
Added Modbus source-load logic to the existing shipboard code and successfully deployed the changes to Production.
Worked on migrating the Sea Events and VPS ETL jobs, including updating dependencies from Bronze to Silver tables in the Mariner workspace.
Completed the initial proof of concept (PoC) for Honeywell data and loaded the data into the respective tables.
Next Week
Investigate and resolve the Production failure in the MIAP ETL pipeline.
Gather business requirements for Honeywell and update the logic accordingly.

---

## Update 2

**Date:** 2026-02-13
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** Unidentified

### Summarized Update

Fixed bug where shore power is greater than 0 when not available
Fixed bug affecting feasibility of optimization when shore power cap is higher than total MCR
Working on adding new metrics to shore power and adding to Web App

### Raw Update

Fixed bug where shore power is greater than 0 when not available
Fixed bug affecting feasibility of optimization when shore power cap is higher than total MCR
Working on adding new metrics to shore power and adding to Web App

---

## Update 3

**Date:** 2026-02-13
**Business Area:** Project Axiom
**Business Project:** Division-Level Medallia Reports
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data. ### Meta Data Extraction
- Divisions Meta Data Framework (David M.): Added auto incremental ID column to production tables. Batch processing code nearly complete and entering testing.

### Raw Update

AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.
### Meta Data Extraction
- Divisions Meta Data Framework (David M.): Added auto incremental ID column to production tables. Batch processing code nearly complete and entering testing. New division aspect mapping tables created with model version and execution date columns for traceability.
- Bullet Points Migration (David M.): Remains blocked pending Erick's confirmation of new topics. Batch process code is ready to execute once input is received.
### Reporting
- GSO Safety Email (Danusio G.): New safety email requirements received from Melissa (Global Security). Email will split into Onboard (priority) and Shorex sections using LLM-based two-step classification.
- Voice of Detractor Fleet Report (David M.): Weekly Fleet detractor report emails delivered successfully for all 3 brands (sent every Monday). Pending stakeholder follow up on the final distribution list.
- RBC Recap Email Enhancement (Rodrigo B.): Improved existing RBC email report to include quantification of negative topic mentions.
- Guest Strategy Email (Rodrigo B.): Weekly Guest Strategy Email delivered successfully for Gang Wang & Hotel Operations teams (sent every Sunday). Positive feedback from stakeholder with minor suggestions for improvement provided. Pending stakeholder sign off

---

## Update 4

**Date:** 2026-02-13
**Business Area:** Project Axiom
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data. ### Modeling
- NPS Drivers Model (Osvaldo V.): Proposed feature clustering using correlation distances to reduce redundancy of Medallia survey features and improve interpretability. Proposed a new model trained on negative-data-only.

### Raw Update

AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.
### Modeling
- NPS Drivers Model (Osvaldo V.): Proposed feature clustering using correlation distances to reduce redundancy of Medallia survey features and improve interpretability. Proposed a new model trained on negative-data-only.
- Drivers Streamlit SHAP POC (Osvaldo V.): Merged Royal and Celebrity APIs into a single consolidated endpoint. Front-end integration with Axiom platform planned for Friday workshop.
- Medallia Keyword Correlation Tool (Osvaldo V.): New task assigned to develop a generalized tool for filtering Medallia comments by keywords and correlating with KPIs. Using previous weather-sentiment analysis as foundation.
- Weather API Data (Danusio G.): Automated daily job running at 6:00 AM. Preparing sailing-level data query to enable integration with the Drivers Model pipeline.
- Guest Logs Classifier (David M.): Erick requested access to David's code and data to address concerns raised by stakeholder Alessio. David sharing code and results for review.

---

## Update 5

**Date:** 2026-02-13
**Business Area:** Project Axiom
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data. ### Project AI Pivot (Qualtrics Topic Extraction)
Self-labeling framework for automatic topic discovery from survey data. - Qualtrics Abandon Cart Emerging Topic Detection (Danusio G.): Presented trending topic framework with semantic similarity and moving averages for emerging topic detection.

### Raw Update

AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.
### Project AI Pivot (Qualtrics Topic Extraction)
Self-labeling framework for automatic topic discovery from survey data.
- Qualtrics Abandon Cart Emerging Topic Detection (Danusio G.): Presented trending topic framework with semantic similarity and moving averages for emerging topic detection. Running backtest analysis for Seven Night Caribbean product to evaluate framework.
- Qualtrics Abandon Cart LLM Topic Extraction (Rodrigo B.): Created a topic dashboards by week and product. Identified recurring Friday peak patterns. Preparing visuals for stakeholder presentation.
- Power BI Dashboard (Danusio G.): VDI access granted to be able to develop and deploy for Power BI dashboards. Deployed Axiom dashboard to Data Science Premium workspace.

---

## Update 6

**Date:** 2026-02-13
**Business Area:** MyCruise Recommender
**Business Project:** Enhanced For You Recommendations
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[cristian_villamarin-villamil/overview_cristian_villamarin-villamil|Cristian Villamarin-Villamil]]

### Summarized Update

Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app. ### Recommendations Engine (Cristian V.)
- Graph-Based Recommendations: Shifting to graph based recommendations and precomputing and storing recommendations in Postgres. Achieved high precision on holdout sets for some meta products.

### Raw Update

Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app.
### Recommendations Engine (Cristian V.)
- Graph-Based Recommendations: Shifting to graph based recommendations and precomputing and storing recommendations in Postgres. Achieved high precision on holdout sets for some meta products. Exploring .
- Axiom Recommendations Frontend Tab: New task to implement a frontend tab in the Axiom web app connecting to the existing recommendations API. Planned for the Friday GitHub Copilot workshop.
- Missing Royal Beach Club Product Recommendations in Dev: Bug found in dev API endpoint - resolved. Prod unaffected.

---

## Update 7

**Date:** 2026-02-13
**Business Area:** Win-on-Waste
**Business Project:** Forecasting Pipeline Expansion
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

Weekly Update – February 13, 2026
1. Demand Segmentation Framework – Development Completed
The clustering-based demand segmentation pipeline for Interport models has been fully developed and is pending validation/testing. The segmentation logic classifies each trading day into High Demand, Regular Demand, or Low Demand categories based on a multi-factor feature set, including:
Historical consumption patterns
Day of week effects
Month/seasonality trends
Demographic attributes
Geolocation variables
Holiday indicators
Proximity to holidays and special events
Based on this classification, the pipeline automatically filters and routes historical observations into the appropriate demand-specific training datasets.

### Raw Update

Weekly Update – February 13, 2026
1. Demand Segmentation Framework – Development Completed
The clustering-based demand segmentation pipeline for Interport models has been fully developed and is pending validation/testing. The segmentation logic classifies each trading day into High Demand, Regular Demand, or Low Demand categories based on a multi-factor feature set, including:
Historical consumption patterns
Day of week effects
Month/seasonality trends
Demographic attributes
Geolocation variables
Holiday indicators
Proximity to holidays and special events
Based on this classification, the pipeline automatically filters and routes historical observations into the appropriate demand-specific training datasets. This enables separate model training for high, regular, and low demand regimes, improving forecast sensitivity and reducing regime-mixing bias.
Testing and performance validation are the next steps.

---

## Update 8

**Date:** 2026-02-13
**Business Area:** Win-on-Waste
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

Weekly Update – February 13, 2026
2. POS Operational Data Quality Issue – Mitigation Module Developed
We identified a recurring operational process gap across the fleet affecting POS consumption data integrity:
Items consumed on Day T are frequently closed in the POS system on Day T+1. The POS dataset does not contain a marker distinguishing true same-day consumption from next-day administrative closures.

### Raw Update

Weekly Update – February 13, 2026
2. POS Operational Data Quality Issue – Mitigation Module Developed
We identified a recurring operational process gap across the fleet affecting POS consumption data integrity:
Items consumed on Day T are frequently closed in the POS system on Day T+1.
The POS dataset does not contain a marker distinguishing true same-day consumption from next-day administrative closures.
This creates artificial volatility in daily consumption signals (e.g., 600 units on Day T followed by 2 units on Day T+1).
This pattern introduces extreme fluctuations in the time series, leading models to regress toward the mean and produce biased forecasts (e.g., stabilizing toward mid-range values instead of capturing true demand spikes).
Actions Taken:
F&B Operations have been formally notified.
A fleet-wide memo has been issued to reinforce correct POS closing procedures.
From a data science standpoint, we have developed an outlier-detection and filtering module that:
Identifies likely administrative carryover anomalies.
Flags and removes these distortions from model training datasets.
Preserves genuine high-demand signals while eliminating artificial volatility.
Development of the mitigation module is complete. Testing and validation against historical scenarios are pending.

---

## Update 9

**Date:** 2026-02-13
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Complete segmentation model testing and backtesting. Validate anomaly-filtering logic impact on forecast accuracy. Quantify uplift in model stability and error reduction.

### Raw Update

Complete segmentation model testing and backtesting.
Validate anomaly-filtering logic impact on forecast accuracy.
Quantify uplift in model stability and error reduction.

---

## Update 10

**Date:** 2026-02-13
**Business Area:** Supply Chain
**Business Project:** CocoCay Integration and Guardrails
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Highlight: Order Creation Dataset Recovery - Beyond Critical Path
Project Catalyst introduced a breaking change to our Order Creation table over the weekend. Ben identified on Saturday that the Ship Code and Voyage Number columns from Crunchtime datasets contained a new voyage number format that could not be mapped to the original voyage numbers used by Revenue Planning. This meant we could not join the Master Load Schedule to the Cruise Profile dataset, as our production prd_silver.ibp.master_load_schedule table still referenced the old voyage numbers — directly threatening the active Beyond pilot.

### Raw Update

Highlight: Order Creation Dataset Recovery - Beyond Critical Path
Project Catalyst introduced a breaking change to our Order Creation table over the weekend. Ben identified on Saturday that the Ship Code and Voyage Number columns from Crunchtime datasets contained a new voyage number format that could not be mapped to the original voyage numbers used by Revenue Planning. This meant we could not join the Master Load Schedule to the Cruise Profile dataset, as our production prd_silver.ibp.master_load_schedule table still referenced the old voyage numbers — directly threatening the active Beyond pilot.
Ben and Camila led the rapid response:
Ben created a temporary mapping table as an immediate stopgap while coordinating with the Catalyst team.
Connor, Yan, Ben, and Camila held an urgent call with the Catalyst team to communicate the severity given the live Beyond pilot. The Catalyst team disclosed a previously unknown table containing Master Load Schedule data with the new voyage numbers.
Ben validated the new Catalyst table and discovered significant differences in column values and voyage inconsistencies compared to our production master_load_schedule table.
To protect data integrity, the team retained the existing prd_silver.ibp.master_load_schedule table and implemented a targeted join to the new Catalyst table solely to retrieve the new voyage number, then joined it back to the master load schedule.
The approach has been fully validated by comparing the new Order Creation dataset against the pre-Catalyst dataset. A backup table was created pre-Catalyst as a permanent validation reference to prevent loss from data engineering vacuum operations.
The Data Engineering team has been briefed and is now working to create a blended table merging the Catalyst shipfin table with the existing prd_silver.ibp.master_load_schedule, with their own data validation in progress.

---

## Update 11

**Date:** 2026-02-13
**Business Area:** Supply Chain
**Business Project:** CocoCay Integration and Guardrails
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Beyond Pilot — Ongoing Data Pipeline Development (Camila)
Supply Name Consumption Ratios:
Resolved an issue where live consumption values were missing because supply name values were not populated for consumption prior to the current date. New supply name values only appeared after the current date, which prevented accurate live consumption calculation. The fix was implemented and validated in time for Paige's demo.

### Raw Update

Beyond Pilot — Ongoing Data Pipeline Development (Camila)
Supply Name Consumption Ratios:
Resolved an issue where live consumption values were missing because supply name values were not populated for consumption prior to the current date. New supply name values only appeared after the current date, which prevented accurate live consumption calculation. The fix was implemented and validated in time for Paige's demo.
Snapshot Table:
Purchase/production order snapshot table now captures a static view of future one-month data only, scoped appropriately rather than overall data.
Baseline Table:
Consolidated table built from end-of-month run data for consistent reference.
Backup Baseline Table:
All weekly run values for the baseline table are now uploaded to Azure Blob Storage. This enables comparison across runs so that if predictions ever look off, we can replace specific values with data from prior runs.
Scorecard Table:
Purchase order: Added live spend report information, now running daily for the most accurate results for Laura.
Production order: Added live consumption report information, now running daily for the most accurate results for Laura.
Actual Quantity Needed vs. Spend Report:
Investigating alignment between spend report create dates and actual quantity needed refresh data. Planning to create a consolidated table with actual quantity needed (including backups) where the refresh date is not a single overwritten value on every run. The original baseline table will be adjusted to address this.
Master Notebook:
Creating a single master notebook to orchestrate all necessary tables sequentially to ensure smooth, reliable execution for the Beyond pilot.

---

## Update 12

**Date:** 2026-02-13
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

Workforce Planning -- North America (Royal)
LOB & Skill Mapping
Current LOB mapping relied solely on skill field, breaking whenever skills/splits were updated
Redesigned with Darren and Gustavo to use department + sub-department + skill name combination
New structure automatically reflects future system changes for long-term maintainability
Call Forecasting & Backtesting
Computed monthly backtesting call volume dataset and refresh process for MAPE display (forecast vs. actual)
Gives stakeholders visibility into forecasting performance to guide upcoming adjustments
Next step: Integrate backtesting results into the application UI
Headcount Modeling
Refreshed hourly call volume proportions (2025-04-01 to 2025-09-30)
Source table prd_silver.mkrpops.cms_interval_stats_all not yet refreshed upstream; using average proportions by LOB as interim
Reviewing hourly call volume proportion dataset required to run headcount model
Working with Darren to confirm office hours (opening/closing times) as essential model input

### Raw Update

Workforce Planning -- North America (Royal)
LOB & Skill Mapping
Current LOB mapping relied solely on skill field, breaking whenever skills/splits were updated
Redesigned with Darren and Gustavo to use department + sub-department + skill name combination
New structure automatically reflects future system changes for long-term maintainability
Call Forecasting & Backtesting
Computed monthly backtesting call volume dataset and refresh process for MAPE display (forecast vs. actual)
Gives stakeholders visibility into forecasting performance to guide upcoming adjustments
Next step: Integrate backtesting results into the application UI
Headcount Modeling
Refreshed hourly call volume proportions (2025-04-01 to 2025-09-30)
Source table prd_silver.mkrpops.cms_interval_stats_all not yet refreshed upstream; using average proportions by LOB as interim
Reviewing hourly call volume proportion dataset required to run headcount model
Working with Darren to confirm office hours (opening/closing times) as essential model input

---

## Update 13

**Date:** 2026-02-13
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

Workforce Planning -- North America (Celebrity)
Darren's team provided target LOB list
Augusto shared Power BI report with Celebrity call volume and skill numbers
Ongoing iterative LOB mapping alignment between Augusto, Darren, Gustavo, and broader team
Additional features being computed to finalize mapping
Next: Cross-validation working session with Darren/NA team (tomorrow), collect office hours/shrinkage/baseline data, update app with Celebrity historical call volume
Workforce Planning -- International & Casino
Brendan set up repository, Nico provided URL: intlfcst.rccl.com
Next step: Migrate existing code and begin testing

### Raw Update

Workforce Planning -- North America (Celebrity)
Darren's team provided target LOB list
Augusto shared Power BI report with Celebrity call volume and skill numbers
Ongoing iterative LOB mapping alignment between Augusto, Darren, Gustavo, and broader team
Additional features being computed to finalize mapping
Next: Cross-validation working session with Darren/NA team (tomorrow), collect office hours/shrinkage/baseline data, update app with Celebrity historical call volume
Workforce Planning -- International & Casino
Brendan set up repository, Nico provided URL: intlfcst.rccl.com
Next step: Migrate existing code and begin testing

---

## Update 14

**Date:** 2026-02-13
**Business Area:** Customer Targeting
**Business Project:** Booking Propensity Models
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]]

### Summarized Update

Consumer Dashboard
Began development of low-level consumer dashboard showing individual consumer features, historical behaviors, and propensity scores across all models
Epsilon Feature Evaluation
Completed full run-through of new Epsilon features; consolidated into Excel showing benefit and rationale
Compared new features against existing to minimize redundancy
Epsilon Data Transformation
Started transformation of Epsilon data and historical snapshots using Min-Max scaling
Blocker: New Epsilon features only ~1 month old; 6-month window required. Preparing data for ingestion so it is ready when the window is met
Bug Fixes
Fixed CEL uplift models incorrectly referencing RCI target columns
Fixed model name validation/generation function error
Fixed Epsilon data ingestion error causing missing data
Fixed zero-division error in SMAPE computation
Code Quality
Removed credentials from repo
Added SQL injection prevention
Extracted duplicated code into reusable functions
Fixed typos, replaced deprecated function calls
Added type hints to all functions
New Capabilities
Added cross-validation option to model training and feature selection
Added unit tests
Added staging environment support (dev, qa, prd)

### Raw Update

Consumer Dashboard
Began development of low-level consumer dashboard showing individual consumer features, historical behaviors, and propensity scores across all models
Epsilon Feature Evaluation
Completed full run-through of new Epsilon features; consolidated into Excel showing benefit and rationale
Compared new features against existing to minimize redundancy
Epsilon Data Transformation
Started transformation of Epsilon data and historical snapshots using Min-Max scaling
Blocker: New Epsilon features only ~1 month old; 6-month window required. Preparing data for ingestion so it is ready when the window is met
Bug Fixes
Fixed CEL uplift models incorrectly referencing RCI target columns
Fixed model name validation/generation function error
Fixed Epsilon data ingestion error causing missing data
Fixed zero-division error in SMAPE computation
Code Quality
Removed credentials from repo
Added SQL injection prevention
Extracted duplicated code into reusable functions
Fixed typos, replaced deprecated function calls
Added type hints to all functions
New Capabilities
Added cross-validation option to model training and feature selection
Added unit tests
Added staging environment support (dev, qa, prd)

---

## Update 15

**Date:** 2026-02-13
**Business Area:** Customer Lifetime Value
**Business Project:** Casino Spend Analysis
**People:** [[caleb_sharkey/overview_caleb_sharkey|Caleb Sharkey]]

### Summarized Update

Received final model input data: media spend, lead sourcing, web funnel entries
Aligned on approach to gauge outputs at two aggregation levels (cabin mix and ship) to assess cabin mix assumptions
Finalizing data cleaning for model inputs with clean mappings across external Excels and internal Delta tables
Merging cruise industry cabin class mix by ship using fuzzy matching (messy ship names)
Documenting full process with GitHub Copilot: executive overview, workplan, technical workflow, data sourcing, assumptions table
Cihan
PCP Pricing Automation
Alaska Shore Excursions Dashboard (Gang & Rafa)
Built comprehensive Databricks dashboard with 20+ visualizations using complex SQL
Includes: revenue/bookings by category (2024 vs 2025), guest product distribution, category/product pair analysis, cumulative bookings vs days to sail, yield curves, bundled products, price trends, daily yield by category, deviation histograms
Presented to Rafa, Alex, Ivaylo, Anastasiia -- approved with requests for cost analysis, inventory analysis, and expansion beyond Alaska
Waterpark PRE (Gang Wang)
Presented price-demand EDA to Jorge and Anastasia
Proposed A/B test at different price points
Stakeholders recommended simple naive method: adjust price based on whether monthly revenue meets target
Second meeting held to finalize target revenue for pricing
Current avg price ~$60 should support elasticity modeling; prior ~$100 price point was too high (appeared inelastic)

### Raw Update

Received final model input data: media spend, lead sourcing, web funnel entries
Aligned on approach to gauge outputs at two aggregation levels (cabin mix and ship) to assess cabin mix assumptions
Finalizing data cleaning for model inputs with clean mappings across external Excels and internal Delta tables
Merging cruise industry cabin class mix by ship using fuzzy matching (messy ship names)
Documenting full process with GitHub Copilot: executive overview, workplan, technical workflow, data sourcing, assumptions table
Cihan
PCP Pricing Automation
Alaska Shore Excursions Dashboard (Gang & Rafa)
Built comprehensive Databricks dashboard with 20+ visualizations using complex SQL
Includes: revenue/bookings by category (2024 vs 2025), guest product distribution, category/product pair analysis, cumulative bookings vs days to sail, yield curves, bundled products, price trends, daily yield by category, deviation histograms
Presented to Rafa, Alex, Ivaylo, Anastasiia -- approved with requests for cost analysis, inventory analysis, and expansion beyond Alaska
Waterpark PRE (Gang Wang)
Presented price-demand EDA to Jorge and Anastasia
Proposed A/B test at different price points
Stakeholders recommended simple naive method: adjust price based on whether monthly revenue meets target
Second meeting held to finalize target revenue for pricing
Current avg price ~$60 should support elasticity modeling; prior ~$100 price point was too high (appeared inelastic)

---

## Update 16

**Date:** 2026-02-13
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

https://royal-it.atlassian.net/browse/RMA-5305?focusedCommentId=1263122
Calculated the track based on the hypothesised methodology. Methodology: It is a blended method, where we look at track 3 weeks in the future and projected pax build 3 weeks historically and the closer weeks are weighted higher and the average of that is considered as the track for the week to smooth out the track ask. Using the new track method, I simulated this week’s PRE runs for B, I, and O cat-classes, comparing the current and hypothesized approaches to observe differences in price changes.

### Raw Update

https://royal-it.atlassian.net/browse/RMA-5305?focusedCommentId=1263122
Calculated the track based on the hypothesised methodology.
Methodology: It is a blended method, where we look at track 3 weeks in the future and projected pax build 3 weeks historically and the closer weeks are weighted higher and the average of that is considered as the track for the week to smooth out the track ask.
Using the new track method, I simulated this week’s PRE runs for B, I, and O cat-classes, comparing the current and hypothesized approaches to observe differences in price changes.
To gain a primary understanding of how the price changes are affected I first looked at the histogram of price change % spread for both the different methods and based on the chart, came to a conclusion that the newer method (blended 3 week weighted avg) is more centered towards 0, indicating that the price changes are more spread across the center and we will not see any major fluctuations in pricing.
To analyze the shift more precisely, I created a cross tab to track how price changes move between the two methods. This revealed that the spread of price changes has narrowed—for example, price changes that previously ranged between -0.75% and -0.5% have now tightened to around -0.25%, and so forth.
RCI | PRE Dynamic Caps 2.0
This week I focused on getting the correct T3 pricing to solve the QUAD Floor Variance subtask. Earlier quad floor variance was not dynamic, now we have updated it to consider the T3 pricing for that sailing, additionally ensured that the quad floor variance only applies to quad occupancies and not doubles.
Additionally, I focused on creating the automated sharepoint such that we have individual rows for each ship-sailingdate-catclass-occupancy, instead of having one list of fixed limits for all the sailings. This would enable us to manually change caps for any individual sailing that are doing good/bad based on the business.
Third, I focused on removing the wts dependency in the process.

---

## Update 17

**Date:** 2026-02-13
**Business Area:** CEL Revenue Management
**Business Project:** Category Gapping Optimization 3.0
**People:** Unidentified

### Summarized Update

Status: This ticket is complete as of 2/12/2026
Deliverables:
The changes have been validated in QA and approved by Monica from Celebrity. Once we deploy to production, the tables will begin saving y_preds correctly in the history tables, along with all the columns needed for future price optimization run. CEL Revenue Management | Elasticity Model Health Check Dashboard
Data gathering for Dashboard
Met with Monica to understand dashboard requirements for tracking price changes, elasticity impact, forecasted demand (y_pred), and model accuracy, with the goal of improving historical model-performance visibility.

### Raw Update

Status: This ticket is complete as of 2/12/2026
Deliverables:
The changes have been validated in QA and approved by Monica from Celebrity. Once we deploy to production, the tables will begin saving y_preds correctly in the history tables, along with all the columns needed for future price optimization run.
CEL Revenue Management | Elasticity Model Health Check Dashboard
Data gathering for Dashboard
Met with Monica to understand dashboard requirements for tracking price changes, elasticity impact, forecasted demand (y_pred), and model accuracy, with the goal of improving historical model-performance visibility.
Reviewed all relevant tables and identified that price_changes_elasticity_hist was missing y_pred values from June onward, even though weekly price changes and elasticities were present; fixed the issue and pushed the correction to production.
Investigated an overwritten table that previously contained y_pred history; attempted to recover past versions with Eswar, but encountered data-type mismatches (bin_length) across versions, making historical recovery infeasible.
Revised the approach by joining the elasticity model output table with the price changes history table to consolidate raw price changes, elasticities, and y_pred using keys: ship_code, sailing_date, read_date, cabin_category_class_code.
Identified a read_date calculation issue in the model output table (derived as sailing_date − bin_end × 7 days), causing misalignment with the Friday-based read_dates used in price changes notebook table working on correcting this logic to align read_dates and enable consistent joins

---

## Update 18

**Date:** 2026-02-13
**Business Area:** PCP Pricing Automation
**Business Project:** Beverage Package Optimization
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

RCI | OBR | Drink Package PRE for Bundles
Add additional improvements to the optimization routine accounting for the effect from RBC-beverage bundles
The main changes to be enhanced in the optimization routine are:
Make price and demand ratio of solo beverage bookings vs. bundle beverage bookings more demand driven for the particular sailing be optimized
For both price and demand, adjust the backup business knowledge driven assumptions to be more dynamic and data driven rather than with hard coded business rules (this well help automatically fix drifts in these trends in the future). OBR | Hybris | E2E Final Promo Automation Testing in Production
Delayed while additional things need to be debugged from Digital/Product team & the final approval process procedure is finished for the workflow.

### Raw Update

RCI | OBR | Drink Package PRE for Bundles
Add additional improvements to the optimization routine accounting for the effect from RBC-beverage bundles
The main changes to be enhanced in the optimization routine are:
Make price and demand ratio of solo beverage bookings vs. bundle beverage bookings more demand driven for the particular sailing be optimized
For both price and demand, adjust the backup business knowledge driven assumptions to be more dynamic and data driven rather than with hard coded business rules (this well help automatically fix drifts in these trends in the future).
OBR | Hybris | E2E Final Promo Automation Testing in Production
Delayed while additional things need to be debugged from Digital/Product team & the final approval process procedure is finished for the workflow.

---

## Update 19

**Date:** 2026-02-13
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** Unidentified

### Summarized Update

Separate RCI pause uploads from price uploads | FEB
Status: This ticket is complete as of 02/06/2026
Deliverables:
Pause table loading from Oracle separated from price upload pipeline. All requirements satisfied. RCI: Transfer price upload process from ADF to Databricks
Status: This ticket is complete as of 02/06/2026
Deliverables:
PRE price upload moved into Databricks job pipeline.

### Raw Update

Separate RCI pause uploads from price uploads | FEB
Status: This ticket is complete as of 02/06/2026
Deliverables:
Pause table loading from Oracle separated from price upload pipeline. All requirements satisfied.
RCI: Transfer price upload process from ADF to Databricks
Status: This ticket is complete as of 02/06/2026
Deliverables:
PRE price upload moved into Databricks job pipeline. Australia processes at noon and non-Australia processes at 7:30pm on Tuesdays
In Progress
Dual: Schedule RCI and Celebrity to run sequentially | FEB
Dual: Combine RCI and Celebrity price upload into single table | FEB

---

## Update 20

**Date:** 2026-02-13
**Business Area:** CEL Revenue Management
**Business Project:** Category Gapping Optimization 3.0
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

Category-Gapping 2.0
Final approach used: Allowed APD to deviate by 1% from true max revenue. Team requested minimum 3% gap on all sailings. Output is being reviewed by business.

### Raw Update

Category-Gapping 2.0
Final approach used: Allowed APD to deviate by 1% from true max revenue. Team requested minimum 3% gap on all sailings.
Output is being reviewed by business.
Category-Gapping 3.0
Presented updates to CEL business on 2/10/26. Approved pricing calculations (bundled cost per person). Team is pleased with current progress but has requests for next meeting:
Back tested sailing examples.
Combined approach where GTY decision is a trade-up choice using the 2.0 model and the EBM Classifier only includes the physical tiers.
Features:
No preference between laf-tier vs tier-tier gaps.
Strong emphasis on availability features.
Further exploration of SPI features.
Trained models for ship/meta/cat-class, ship/meta, ship/cat-class, ship, meta, cat-class. Saw strongest signals at brand and ship-class aggregations. As models become more granular, there is sparser data.
Current focus is feature selection. Following Evan’s framework, I have added:
GTY booked %
Deployment length
Days at sea
Holidays during length of sailing
Spending score for sailing
Next steps:
Continue testing features and feature selection methods.
Output sailing examples for business team.
Align RCI with CEL progress as my focus has been on CEL models.

---

## Update 21

**Date:** 2026-02-13
**Business Area:** CEL Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model 3.0
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Run Price Optimization Model + Compare Recommendations
Did an initial run on the week of Jan 26th,  presented results to the business and received their feedback. Implemented their feedback and completed another run based on this week (the week of Feb. Generated comparative report and has a meeting with the business tomorrow to discuss the results and receive their feedback.

### Raw Update

Run Price Optimization Model + Compare Recommendations
Did an initial run on the week of Jan 26th,  presented results to the business and received their feedback. Implemented their feedback and completed another run based on this week (the week of Feb. 9th). Generated comparative report and has a meeting with the business tomorrow to discuss the results and receive their feedback.
Generalize_the_Model_PWL_function
I completed the codebase for this task in standardized, bi-branded, and class object format. It takes 5-8 mins in average to process for each ship_code. Currently optimizing for speed of processing by experimenting different parallelization/repartitioning settings. Also, experimenting with writing long-format tables (to avoid 2 array type columns). This may take 1-2 more story points.

---

## Update 22

**Date:** 2026-02-13
**Business Area:** SSC Revenue Management
**Business Project:** Fare Code Unbundling
**People:** [[jesse_bausell/overview_jesse_bausell|Jesse Bausell]]

### Summarized Update

SSC Revenue teams request to revert prices back to their status two weeks ago. To expedite this process (so Revenue doesn't have to resubmit manually), SSC Revenue team has provided a list of price recommendations to revert. I am creating a modified version of PRE code that is designed to take these changes and insert them into the reservation system.

### Raw Update

SSC Revenue teams request to revert prices back to their status two weeks ago. To expedite this process (so Revenue doesn't have to resubmit manually), SSC Revenue team has provided a list of price recommendations to revert. I am creating a modified version of PRE code that is designed to take these changes and insert them into the reservation system.

---

## Update 23

**Date:** 2026-02-13
**Business Area:** PROPEL
**Business Project:** Offer Template Expansion
**People:** [[glen-erik_cortez/overview_glen-erik_cortez|Glen-Erik Cortez]]

### Summarized Update

Offer templates: Presented new offer template to OBR team and aligned changes needed in configurations on their side. (Glen-Erik)
Measurements Dashboard (Javier & Glen-Erik)
Optimization: met with JC to troubleshoot measurements dashboard and received guidance on areas for improvement that the OBR team should address. Using aggregate tables and incremental refreshes.

### Raw Update

Offer templates: Presented new offer template to OBR team and aligned changes needed in configurations on their side. (Glen-Erik)
Measurements Dashboard (Javier & Glen-Erik)
Optimization: met with JC to troubleshoot measurements dashboard and received guidance on areas for improvement that the OBR team should address. Using aggregate tables and incremental refreshes. The additional dynamic test/control measurement charts also need to be redone without python code. (Glen-Erik)
Missing categories: investigated why there are missing categories in the dashboard. Redoing the python chart and data will likely fix this issue. (Javier)
Uplift measurements logic: investigated current logic to understand and document metrics in place for dynamic test/control (Javier)
Solstice Deck Plan update: learned process to update deck plans. The plans provided by OBR must be complemented by a housekeeping file that is not yet ready to map the stateroom attendant section to a stack of offers.  (Glen-Erik)
Investigated how to add Park West logic replicating Effy targeting. Most of it can be done with minimal changes, like targeting high spenders (top 5 percentile) and/or people that spend more than 1K onboard. Targeting AI / RO, honeymoon is easy as well. Targeting past purchasers would require more custom logic that should really be generalized to be "past purchaser of current product" and "past purchaser of current product category" rather than "past effy collector" and adding "past park west collector". (Javier & Glen-Erik)
Support: Trained offshore team on how to regenerate offers when necessary. (Glen-Erik)
Hiring: new contractor to support PROPEL should be joining soon, extended an offer, pending start date.

---

## Update 24

**Date:** 2026-02-13
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** Unidentified

### Summarized Update

SPI: (Eswar)
Separated project from feature store. Setup all CI/CD for the new SPI repo & productionized workflows via bundles. Migrated Databricks Asset Bundle standardizations to QA, unfortunately there was naming bug that deployed the workflows to the wrong place creating duplicates and we had to roll back those changes.

### Raw Update

SPI: (Eswar)
Separated project from feature store.
Setup all CI/CD for the new SPI repo & productionized workflows via bundles.
Migrated Databricks Asset Bundle standardizations to QA, unfortunately there was naming bug that deployed the workflows to the wrong place creating duplicates and we had to roll back those changes. Should be ready to redeploy next week. (Javier, Eswar, Glen-Erik)
Data Governance: Aligned architectural process to marry the Data Validation Framework with the Data Governance checks, starting with stopping pipelines from running if critical tables are outdated. Raising silent failures must be transparently communicated to the development and business teams in advance because the more rules (beyond outdated critical tables) we add, the higher the likelihood that a process will fail when it shouldn't (false positive). The business must approve and validate these automated decisions to stop pipelines. (Glen-Erik)
Support: (Eswar)
Restored PRE Lite using historical data versions for Data Scientists to build visualizations upon.
Deploying new code and assisting with code conflicts and issues.

---

## Update 25

**Date:** 2026-02-13
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[glen-erik_cortez/overview_glen-erik_cortez|Glen-Erik Cortez]]

### Summarized Update

There are ongoing failures in MIAP pipelines. Some are known issues, others are bugs that could have been avoided running in QA which is currently off. Hiring: contract to hire passed interviews with Glen-Erik & Eswar, and Mert & Brendan.

### Raw Update

There are ongoing failures in MIAP pipelines. Some are known issues, others are bugs that could have been avoided running in QA which is currently off.
Hiring: contract to hire passed interviews with Glen-Erik & Eswar, and Mert & Brendan. Needs approval from David on budget. Pending take home as well.

---

_Source: 20260213 - Weekly Matt and Rafeh Updates (Raw).docx_