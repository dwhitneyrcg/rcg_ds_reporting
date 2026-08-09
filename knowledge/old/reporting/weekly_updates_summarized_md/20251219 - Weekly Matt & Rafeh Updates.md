---
tags:
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/revenue_management_automation_(ssc)
  - business_area/win-on-waste_(hotel_operations)
  - project/a_b_testing_framework
  - project/automated_pricing_expansion
  - project/beverage_package_optimization
  - project/casino_spend_analysis
  - project/division-level_medallia_reports
  - project/elasticity_model_enhancements_(pre4.0)
  - project/forecasting_pipeline_expansion
  - project/gty-lead_fare_optimization_model
  - project/historical_data_integration
  - project/nps_drivers_analysis_for_alert_system
  - project/perfect_day_product_pricing
  - project/pre_4.0_elasticity_enhancements
  - project/spi-guided_track_optimization
  - summarized
  - weekly_update
date: "2025-12-19"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - 2025-12-19

## Updates

### RCI Revenue Management

**Date:** 2025-12-19
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model

**Achievements:**
PRE
This week I executed PRE runs with the optimal track-reading methodology for CEL and RCI. While testing RCI in the dev environment, I found that changes to the track were not being reflected in price outputs. Investigation revealed the elasticity model was last trained in November, so the model could not produce up-to-date prices. To proceed, I calculated historical uncapped price changes for both CEL and RCI as an interim measure. Presented analysis to the RCI/CEL leadership with positive feedback. Highlighted where different look forward and look back windows yielded better adherence to track dependent on brand, wts, and meta product. Atefeh

**Focus Areas:**
Team will be testing these window methodologies next year to determine in practice what is the best window.

**Raw Update:**
PRE
This week I executed PRE runs with the optimal track-reading methodology for CEL and RCI. While testing RCI in the dev environment, I found that changes to the track were not being reflected in price outputs. Investigation revealed the elasticity model was last trained in November, so the model could not produce up-to-date prices. To proceed, I calculated historical uncapped price changes for both CEL and RCI as an interim measure.
Presented analysis to the RCI/CEL leadership with positive feedback. Highlighted where different look forward and look back windows yielded better adherence to track dependent on brand, wts, and meta product. Team will be testing these window methodologies next year to determine in practice what is the best window.
Atefeh

---

### RCI Revenue Management

**Date:** 2025-12-19
**Business Area:** RCI Revenue Management
**Business Project:** SPI-guided Track Optimization

**Achievements:**
Promotion Optimization (Track-based rules)
Grouped sailings into three rule buckets (reduce/remove promo; keep & adjust strength by track; lower promo).Compiled the results table for review and shared with Eddie (task ready to close pending sign-off). Jesse

**Raw Update:**
Promotion Optimization (Track-based rules)
Grouped sailings into three rule buckets (reduce/remove promo; keep & adjust strength by track; lower promo).Compiled the results table for review and shared with Eddie (task ready to close pending sign-off).
Jesse

---

### SSC Revenue Management

**Date:** 2025-12-19
**Business Area:** SSC Revenue Management
**Business Project:** A/B Testing Framework

**Achievements:**
Universal A/B Framework
Consistent with needs of the business, I have created a python class library for “greedy clustering”. This library optimizes A/B test subjects after they are matched with user-specified “hard constraints” (see last weeks update). Like the hard constraints’ library, these functions are specified and initialized using a yaml file. This yaml contains all soft constraint fields that must be optimized, as well as assigned weights for added importance. This code is universal, yet simple to maintain. It requires only two inputs and we should be able to incorporate it within a variety of different frameworks. Once I formally pass this framework to our team, we will be able to append additional “Gecko” matching capabilities to it. Evan

**Raw Update:**
Universal A/B Framework
Consistent with needs of the business, I have created a python class library for “greedy clustering”. This library optimizes A/B test subjects after they are matched with user-specified “hard constraints” (see last weeks update). Like the hard constraints’ library, these functions are specified and initialized using a yaml file. This yaml contains all soft constraint fields that must be optimized, as well as assigned weights for added importance. This code is universal, yet simple to maintain. It requires only two inputs and we should be able to incorporate it within a variety of different frameworks. Once I formally pass this framework to our team, we will be able to append additional “Gecko” matching capabilities to it.
Evan

---

### Revenue Management Automation (RCI)

**Date:** 2025-12-19
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** GTY-Lead Fare Optimization Model

**Achievements:**
SPI
Created classes for temporal feature engineering
Built a method for feature reduction checking co-linear features between subsets as it reduces
Built a method to deploy a package and use it in notebooks (reduces overhead)
Tested out synthetic data creation (decided against GAN)
Built outbound method to publish data
Finalized initial workbooks / dataset
Bootstrapped A/B test for AirSea completed and demonstrated for 2024 v 2025
Created a MLFlow method to save / load models automatically (including custom pipelines)
Evaluated additional external sources for SPI
Added additional endogenous features for SPI
Doug
CEL Revenue Management - Research Requests for Automation
1) Oracle Tables — Action Verification
Provided possible action to Data Engineering on how to check if Oracle tables have been actioned without having to rely on manual confirmation. Provided sample SQL on how to query Oracle system views for that information. 2) Celebrity FIT Berthing — XC Bookings
Celebrity FIT berthing failing to berth XC bookings
Resolution - Celebrity business rules
Celebrity has rules in place to not berth summer sailings outside of 120 DTS using relaxed mandatory occupancy restrictions. Sailing in question (EQ 6/11/26) is a summer sailing at 177 DTS. Process correctly skipped berthing subject bookings. Celebrity will revisit the rules with the product teams to see whether they want to relax current rules. Doug
RCI Revenue Management - Research Requests for Automation
3) RCG Replenishment — GTY Offered/Booked Counts (AS400)
RCG Replenishment - Product teams questioning changes in GTY offered and booked count changes in AS400 service history. Resolution - Service history records not related to automation. Activity timestamps occurred during times when automation does not run. Activity recorded for actions automation does not have privileges to perform (automation cannot alter GTY offered/booked counts). Activity users (GTY_RECALC, GTY_AUDIT) are not associated with automation. Most likely associated with IT synchronization process (RM_P_GTYU and RM_90XX). Recommended business contact AS400 team to confirm. Been researching different machine learning approaches and met with David + Eddie to determine the right modeling approach. Doug
RCI Revenue Management | Continuous A/B Testing Advisory
Functioning and Commits
Confirmation of ABTESTING-dbricks repo correct functioning and ability to commit code to qa and prd environments. Confirmed updates made by Eswar function correctly. Meeting — Review To-Date Progress, Q\&A
Meeting — Review Gekko Optimization
Michelle
CEL Revenue Management
AD HOC | CEL GTY-LEAD 2.0 / DART
- Presented changes to Anastasia and received approval. Pushed updates into production. - GTY bookings that were previously dropped due to Feature Store table issues are now being counted. Trade-ups are lower across the brand and predictions are much more accurate. Residuals have dropped by about 5%, meaning that the trade-up predictions are closer to the actuals. Recommended gaps have dropped an average of 3% across all sailings, with the largest decrease of 7% in Alaska. - The changes in data sources have made the models overall MUCH more accurate and the recommended gaps nearer business expectations. In progress of making the same data updates to RCI models as was done for CEL. This is a big enhancement and both brands will substantially benefit from the change. Michelle
CEL Revenue Management | Category-Gapping 3.0
- Met with business 12/16/25 to review updates. Presented adjusted weighting outputs. Slight tweaking needed to better match predictions proportions to actual bookings distributions. - Since category-gapping decisions are largely based on what cat-class the customer is considering. I am testing more granular models. Will compare modelling by ship-class, ship-class/meta, and ship-class/meta/cat-class. - Refactored all the datasets for 3.0 to not rely on FS availability. Same improvements as was done for 2.0 to better reflect the actual GTY and physical bookings coming in. Lamis
RCI Revenue Management - Pricing Optimization
Recalibrate Integration Windows (Beat/Miss & DART) and Release Weekly Results
The business requested minor modifications to some of the concepts integrated in the optimization. I had implemented these modifications and will close this sub-task upon confirmation from the team. RCI: Prepare presentation to stakeholders
Lamis
RCI Revenue Management - Pricing Optimization
CEL: Quantify Shared demand + Prepare presentation to Stakeholders
As agreed with SHs - the allocation of shared demand to sailing-level is based on the STLY of the proportion of bkgs of the total demand for the same ship code-sail month - cat class - WTS - meta product. This allocation is used to set up the upper bound on weekly bookings. To use this information to generate tracks for new deployments, there could be cases where this combination of meta-ship-month-cat class never exist. In this case, will fall back to the original methodology at the ship_class level based on the IQR of the weekly bookings. Some examples of the shared demand and shared demand allocations are shown below → the lb/ub(search space) is highlighted in yellow. Lekha

**Raw Update:**
SPI
Created classes for temporal feature engineering
Built a method for feature reduction checking co-linear features between subsets as it reduces
Built a method to deploy a package and use it in notebooks (reduces overhead)
Tested out synthetic data creation (decided against GAN)
Built outbound method to publish data
Finalized initial workbooks / dataset
Bootstrapped A/B test for AirSea completed and demonstrated for 2024 v 2025
Created a MLFlow method to save / load models automatically (including custom pipelines)
Evaluated additional external sources for SPI
Added additional endogenous features for SPI
Doug
CEL Revenue Management - Research Requests for Automation
1) Oracle Tables — Action Verification
Provided possible action to Data Engineering on how to check if Oracle tables have been actioned without having to rely on manual confirmation. Provided sample SQL on how to query Oracle system views for that information.
2) Celebrity FIT Berthing — XC Bookings
Celebrity FIT berthing failing to berth XC bookings
Resolution - Celebrity business rules
Celebrity has rules in place to not berth summer sailings outside of 120 DTS using relaxed mandatory occupancy restrictions.
Sailing in question (EQ 6/11/26) is a summer sailing at 177 DTS.
Process correctly skipped berthing subject bookings.
Celebrity will revisit the rules with the product teams to see whether they want to relax current rules.
Doug
RCI Revenue Management - Research Requests for Automation
3) RCG Replenishment — GTY Offered/Booked Counts (AS400)
RCG Replenishment - Product teams questioning changes in GTY offered and booked count changes in AS400 service history.
Resolution - Service history records not related to automation.
Activity timestamps occurred during times when automation does not run.
Activity recorded for actions automation does not have privileges to perform (automation cannot alter GTY offered/booked counts).
Activity users (GTY_RECALC, GTY_AUDIT) are not associated with automation.
Most likely associated with IT synchronization process (RM_P_GTYU and RM_90XX). Recommended business contact AS400 team to confirm.
Been researching different machine learning approaches and met with David + Eddie to determine the right modeling approach.
Doug
RCI Revenue Management | Continuous A/B Testing Advisory
Functioning and Commits
Confirmation of ABTESTING-dbricks repo correct functioning and ability to commit code to qa and prd environments. Confirmed updates made by Eswar function correctly.
Meeting — Review To-Date Progress, Q\&A
Meeting — Review Gekko Optimization
Michelle
CEL Revenue Management
AD HOC | CEL GTY-LEAD 2.0 / DART
- Presented changes to Anastasia and received approval. Pushed updates into production.
- GTY bookings that were previously dropped due to Feature Store table issues are now being counted. Trade-ups are lower across the brand and predictions are much more accurate. Residuals have dropped by about 5%, meaning that the trade-up predictions are closer to the actuals. Recommended gaps have dropped an average of 3% across all sailings, with the largest decrease of 7% in Alaska.
- The changes in data sources have made the models overall MUCH more accurate and the recommended gaps nearer business expectations.
In progress of making the same data updates to RCI models as was done for CEL. This is a big enhancement and both brands will substantially benefit from the change.
Michelle
CEL Revenue Management | Category-Gapping 3.0
- Met with business 12/16/25 to review updates. Presented adjusted weighting outputs. Slight tweaking needed to better match predictions proportions to actual bookings distributions.
- Since category-gapping decisions are largely based on what cat-class the customer is considering. I am testing more granular models. Will compare modelling by ship-class, ship-class/meta, and ship-class/meta/cat-class.
- Refactored all the datasets for 3.0 to not rely on FS availability. Same improvements as was done for 2.0 to better reflect the actual GTY and physical bookings coming in.
Lamis
RCI Revenue Management - Pricing Optimization
Recalibrate Integration Windows (Beat/Miss & DART) and Release Weekly Results
The business requested minor modifications to some of the concepts integrated in the optimization. I had implemented these modifications and will close this sub-task upon confirmation from the team.
RCI: Prepare presentation to stakeholders
Lamis
RCI Revenue Management - Pricing Optimization
CEL: Quantify Shared demand + Prepare presentation to Stakeholders
As agreed with SHs - the allocation of shared demand to sailing-level is based on the STLY of the proportion of bkgs of the total demand for the same ship code-sail month - cat class - WTS - meta product. This allocation is used to set up the upper bound on weekly bookings.
To use this information to generate tracks for new deployments, there could be cases where this combination of meta-ship-month-cat class never exist. In this case, will fall back to the original methodology at the ship_class level based on the IQR of the weekly bookings.
Some examples of the shared demand and shared demand allocations are shown below → the lb/ub(search space) is highlighted in yellow.
Lekha

---

### CEL Revenue Management

**Date:** 2025-12-19
**Business Area:** CEL Revenue Management
**Business Project:** Elasticity Model Enhancements (PRE4.0)

**Achievements:**
Completed integration of the updated elasticity + DART pipeline into the existing ingestion framework, resolved multiple debugging issues during code integration and ensuring smooth end-to-end execution. This means CEL has a comparable elasticity model now to RCI. Next year we will turn on DART for CEL. Performed model evaluation across all meta_product_codes, observing a drastic decrease in Median Absolute Percentage Error and achieving a consistent R² of 80% across all backtesting splits. Analyzed base vs. DART-adjusted predictions per sailing and confirmed that DART significantly improves prediction accuracy, with adjusted demand consistently closer to actuals than the base predictions
Compared Base elasticities vs DART adjusted elasticities observed more variation in the DART adjusted elasticity
Created some plots to compare the difference between base elasticities and DART adjusted elasticities and prepared a deck that shows the impact of DART on demand forecasting
Prepared this below deck and presented to Monica from CEL team
Ignacio

**Raw Update:**
Completed integration of the updated elasticity + DART pipeline into the existing ingestion framework, resolved multiple debugging issues during code integration and ensuring smooth end-to-end execution. This means CEL has a comparable elasticity model now to RCI. Next year we will turn on DART for CEL.
Performed model evaluation across all meta_product_codes, observing a drastic decrease in Median Absolute Percentage Error and achieving a consistent R² of 80% across all backtesting splits.
Analyzed base vs. DART-adjusted predictions per sailing and confirmed that DART significantly improves prediction accuracy, with adjusted demand consistently closer to actuals than the base predictions
Compared Base elasticities vs DART adjusted elasticities observed more variation in the DART adjusted elasticity
Created some plots to compare the difference between base elasticities and DART adjusted elasticities and prepared a deck that shows the impact of DART on demand forecasting
Prepared this below deck and presented to Monica from CEL team
Ignacio

---

### PCP Pricing Automation

**Date:** 2025-12-19
**Business Area:** PCP Pricing Automation
**Business Project:** Beverage Package Optimization

**Achievements:**
1 ) a model that needed improvements; the low elasticity value resulting from the waterpark elasticity model was expected based on the data, but it could be playing a part in the the max price constraint being reached with consistency. 2 ) code in the optimization that needed to be adjusted, improved, and/or debugged

Ignacio

**Raw Update:**
1 ) a model that needed improvements; the low elasticity value resulting from the waterpark elasticity model was expected based on the data, but it could be playing a part in the the max price constraint being reached with consistency.
2 ) code in the optimization that needed to be adjusted, improved, and/or debugged

Ignacio

---

### PCP Pricing Automation

**Date:** 2025-12-19
**Business Area:** PCP Pricing Automation
**Business Project:** Perfect Day Product Pricing

**Achievements:**
1 ) process of uploading this table to Salesforce (Erik has a code process of doing this; I can get some guidance from him on this)
2 ) saving this CRF table in Unity Catalog somewhere & granting access to Sophia (& others on the push notification side of marketing) for this Unity Catalog table. this will be required in order for that side of the marketing team to use the CRF table for notifications. (NOTE: promos can be removed from this CRF table once the END_DATE of the promo is reached)
Ignacio
PCP Pricing Automation - Draft the architecture of continuous AB testing (input framework, output framework, and architecture tying it all together)
1 ) Historical Table – on which initial Power Analysis will be run to determine required sample number
2 ) Viable Samples Table – on which Optimal Pairing will be run to extract the test-control pairs for the test (+ also for resampling of control groups that have suffered constraint drifts, SRM, etc)
3 ) Test-Control Pair Table – containing all most up-to-date performance metrics & results of the test & control groups in the test
4 ) Results Table – one centralized table with all the most up-to-date outcomes of all existing (and completed) A/B tests
Ignacio
PCP Pricing Automation - Create Gekko Optimization component of the AB testing framework
The Gekko Optimization function(s) were created & properly formatted based on the required inputs from the expected Greedy Clustering function outputs. It was designed & aligned with Jesse based on which variables will be needed to be passed from one to the other. This involved creation of several subfunctions all to be called/used in the main Gekko Optimization function. The expected parameters required from the config.yaml file were also set up. Once the Greedy Clustering & power Analysis components are finalized by Jesse, they can be incorporated into the Class & connected together end-to-end for a very functional AB testing framework
Ignacio
PCP Pricing Automation - Create SRM Classes within ABTest Framework class
The Sample Ratio Mismatch portion of the AB Testing Framework was created and added into the class. This will check for overall/generic mismatches in samples in the test along with specified mismatches in certain categorical categories (e.g. meta product code, ship class, sailing quarter). Ignacio

**Raw Update:**
1 ) process of uploading this table to Salesforce (Erik has a code process of doing this; I can get some guidance from him on this)
2 ) saving this CRF table in Unity Catalog somewhere & granting access to Sophia (& others on the push notification side of marketing) for this Unity Catalog table. this will be required in order for that side of the marketing team to use the CRF table for notifications. (NOTE: promos can be removed from this CRF table once the END_DATE of the promo is reached)
Ignacio
PCP Pricing Automation - Draft the architecture of continuous AB testing (input framework, output framework, and architecture tying it all together)
1 ) Historical Table – on which initial Power Analysis will be run to determine required sample number
2 ) Viable Samples Table – on which Optimal Pairing will be run to extract the test-control pairs for the test (+ also for resampling of control groups that have suffered constraint drifts, SRM, etc)
3 ) Test-Control Pair Table – containing all most up-to-date performance metrics & results of the test & control groups in the test
4 ) Results Table – one centralized table with all the most up-to-date outcomes of all existing (and completed) A/B tests
Ignacio
PCP Pricing Automation - Create Gekko Optimization component of the AB testing framework
The Gekko Optimization function(s) were created & properly formatted based on the required inputs from the expected Greedy Clustering function outputs. It was designed & aligned with Jesse based on which variables will be needed to be passed from one to the other. This involved creation of several subfunctions all to be called/used in the main Gekko Optimization function. The expected parameters required from the config.yaml file were also set up. Once the Greedy Clustering & power Analysis components are finalized by Jesse, they can be incorporated into the Class & connected together end-to-end for a very functional AB testing framework
Ignacio
PCP Pricing Automation - Create SRM Classes within ABTest Framework class
The Sample Ratio Mismatch portion of the AB Testing Framework was created and added into the class. This will check for overall/generic mismatches in samples in the test along with specified mismatches in certain categorical categories (e.g. meta product code, ship class, sailing quarter).
Ignacio

---

### PCP Pricing Automation

**Date:** 2025-12-19
**Business Area:** PCP Pricing Automation
**Business Project:** Automated Pricing Expansion

**Achievements:**
---- prd_silver.cmrc_ods_core.precruise_active_pricing
---- prd_silver.cmrc_ods_core.precruise_inventory
---- prd_silver.cmrc_ods_core.booking_transaction_order_entry
These were adjusted in FS & optimization code
Ayon Ghost

**Raw Update:**
---- prd_silver.cmrc_ods_core.precruise_active_pricing
---- prd_silver.cmrc_ods_core.precruise_inventory
---- prd_silver.cmrc_ods_core.booking_transaction_order_entry
These were adjusted in FS & optimization code
Ayon Ghost

---

### Win-on-Waste

**Date:** 2025-12-19
**Business Area:** Win-on-Waste
**Business Project:** Forecasting Pipeline Expansion

**Achievements:**
Pipeline schema changes
Updated downstream table schemas and pipeline checkpoints to be pipeline-specific and segregated by environment (prod / qa / dev). Benefit: improved isolation between environments, clearer lineage, and safer deployments/rollbacks. Fleet backup itinerary
Developed and tested a backup itinerary for each ship and each profit center across the fleet. Integrated the backup itinerary into the main pipeline to ensure continuity of reporting and processing to cater to sudden change in itinerary due to inclement weather. F&B support and forecasts
Continued regular support to the Chefs and F&B team, delivering forecast reports
Mert
MIAP
Started developing new Agentic AI app functionality using the MIAP API. Added data-trending functionality to the MIAP app to allow users to visualize high-frequency shipboard signals. Attended an AI workshop with GMO Energy / Safety / Asset / Strategy leaders. Reviewed the Cadentia AI solution for Newbuild. Arya
MIAP
Learning to use vector AI search for the Newbuild (NB) project. Refactored powerplant files for STG. Built a POC for a contract management tool for NB. Completed EDA on the azipod dataset. Fine-tuned STG models. Brendan
MIAP
Modified the hull-coating model framework to handle SeaQuantum Classic C (used by IC-class ships). Created interim ALS base and dynamic models for several ships so vessels with limited ALS usage can still be simulated. Modified the propulsion model framework to allow base model training periods to be missing ALS data. Updated the MIAP REST API to follow the new signature for voyage model simulation. Will
MIAP
Diagnosed issues with Eniram data affecting the hull-coating degradation model. Met with the GMO app team to request expanded functionality for Dynamic Filters. Tuned hyperparameters of the Pilot Fuel Ratio model. Reworked the base model for all pilot fuel ratio dynamic models. Met with Kimmo from GMO to diagnose pilot fuel ratio reading issues in UT data, which led to improved outlier detection for all pilot fuel models. Reza
MIAP
Diagnosed elevated speed generated by the digital twin platform during the voyage input generation step. Completed the first trial of fuel-forecasting performance comparison scripts covering both the past (FACTS) table and the future (ITINERARY). Parallelized the script from the second item at the leg level and began implementing a workflow for ship-level parallel computing. Mahshad
MIAP
Debugged OFB fuel consumption in the Digital Twin model and fixed the issue.

**Raw Update:**
Pipeline schema changes
Updated downstream table schemas and pipeline checkpoints to be pipeline-specific and segregated by environment (prod / qa / dev).
Benefit: improved isolation between environments, clearer lineage, and safer deployments/rollbacks.
Fleet backup itinerary
Developed and tested a backup itinerary for each ship and each profit center across the fleet.
Integrated the backup itinerary into the main pipeline to ensure continuity of reporting and processing to cater to sudden change in itinerary due to inclement weather.
F&B support and forecasts
Continued regular support to the Chefs and F&B team, delivering forecast reports
Mert
MIAP
Started developing new Agentic AI app functionality using the MIAP API.
Added data-trending functionality to the MIAP app to allow users to visualize high-frequency shipboard signals.
Attended an AI workshop with GMO Energy / Safety / Asset / Strategy leaders.
Reviewed the Cadentia AI solution for Newbuild.
Arya
MIAP
Learning to use vector AI search for the Newbuild (NB) project.
Refactored powerplant files for STG.
Built a POC for a contract management tool for NB.
Completed EDA on the azipod dataset.
Fine-tuned STG models.
Brendan
MIAP
Modified the hull-coating model framework to handle SeaQuantum Classic C (used by IC-class ships).
Created interim ALS base and dynamic models for several ships so vessels with limited ALS usage can still be simulated.
Modified the propulsion model framework to allow base model training periods to be missing ALS data.
Updated the MIAP REST API to follow the new signature for voyage model simulation.
Will
MIAP
Diagnosed issues with Eniram data affecting the hull-coating degradation model.
Met with the GMO app team to request expanded functionality for Dynamic Filters.
Tuned hyperparameters of the Pilot Fuel Ratio model.
Reworked the base model for all pilot fuel ratio dynamic models.
Met with Kimmo from GMO to diagnose pilot fuel ratio reading issues in UT data, which led to improved outlier detection for all pilot fuel models.
Reza
MIAP
Diagnosed elevated speed generated by the digital twin platform during the voyage input generation step.
Completed the first trial of fuel-forecasting performance comparison scripts covering both the past (FACTS) table and the future (ITINERARY).
Parallelized the script from the second item at the leg level and began implementing a workflow for ship-level parallel computing.
Mahshad
MIAP
Debugged OFB fuel consumption in the Digital Twin model and fixed the issue.

---

### MIAP

**Date:** 2025-12-19
**Business Area:** MIAP
**Business Project:** Historical Data Integration

**Achievements:**
Clear blockers for Zerobus access. Inspect the MIAP shared-cluster Spark UI to diagnose why workflows are taking longer and adjust cluster configuration as needed.▍
Ben & Camilla
1. Supply Chain / IBP
Business Impact & Strategy
Held a deep-dive session on the AI Demand / Forecast Model with Juan, Jessica, Connor, Yan, and Ben, covering how the model works and the reporting it provides. From this session, the AI forecast model indicates a 51M decentralized reinvestment opportunity over the past 10 months for Celebrity across Hotel, Food, and Beverage, with 35M attributable to Food. Juan and Laura have begun scoping a pilot using the Order Creation dataset to inform the 2026, 12-month budget for Beyond. If this pilot is successful, it is expected to roll out fleetwide. If Scaled to RCI, CEL, and SSC, this could be a huge $100M cost-saving opportunity
Ben & Camilla
1. Supply Chain / IBP
Data, Modeling, and Reporting Enhancements
Order Creation Filters (RCI/CCI):
Updated the max ship load date filter for RCI/CCI order creation to be dynamic, automatically picking up the next December (currently 2026-12). Warehouse–Port Accuracy:
Updated the warehouse-to-port mapping to use the first port at which the ship arrives, improving accuracy of where/when ships are docked. Approach validated with Marjolijn for better alignment with operational reality. HF&B / Cococay Integration:
HF&B is now running with Cococay for SharePoint files. Follow-up with Fanny is needed to confirm understanding and downstream usage. Demand Files & Data Quality:
Updated Demand Files with null package type; requires follow-up with Fanny to confirm treatment and any necessary corrections. Ben & Camilla
1. Supply Chain / IBP
Monitoring, Governance, and Analytics
Par Volatility Reporting (RCI/CCI):
Created an RCI/CCI min and max par volatility report to better understand inventory variability. Next step: review findings and implications with Yan. Table Freshness & Coverage:
Working on reading all created tables and their last updated date and pushing this as a Teams message for Yan and other stakeholders, enabling better oversight of data freshness. In parallel, working on reading all source tables from production silver and production gold to hand off to the DE team so they can verify they have recreated all critical tables in the new environment. Ben & Camilla
1. Supply Chain / IBP
Open Items / Pending
Data Quality & Inputs (Fanny):
Follow-up needed with Fanny on:
Missing LE in Container Load Date files. Incorrect historical and future predictions for one product due to conversion factors. Confirmation on handling of null package type in Demand Files. Confirmation on HF&B with Cococay SharePoint setup.

**Raw Update:**
Clear blockers for Zerobus access.
Inspect the MIAP shared-cluster Spark UI to diagnose why workflows are taking longer and adjust cluster configuration as needed.▍
Ben & Camilla
1. Supply Chain / IBP
Business Impact & Strategy
Held a deep-dive session on the AI Demand / Forecast Model with Juan, Jessica, Connor, Yan, and Ben, covering how the model works and the reporting it provides.
From this session, the AI forecast model indicates a 51M decentralized reinvestment opportunity over the past 10 months for Celebrity across Hotel, Food, and Beverage, with 35M attributable to Food.
Juan and Laura have begun scoping a pilot using the Order Creation dataset to inform the 2026, 12-month budget for Beyond.
If this pilot is successful, it is expected to roll out fleetwide.
If Scaled to RCI, CEL, and SSC, this could be a huge $100M cost-saving opportunity
Ben & Camilla
1. Supply Chain / IBP
Data, Modeling, and Reporting Enhancements
Order Creation Filters (RCI/CCI):
Updated the max ship load date filter for RCI/CCI order creation to be dynamic, automatically picking up the next December (currently 2026-12).
Warehouse–Port Accuracy:
Updated the warehouse-to-port mapping to use the first port at which the ship arrives, improving accuracy of where/when ships are docked.
Approach validated with Marjolijn for better alignment with operational reality.
HF&B / Cococay Integration:
HF&B is now running with Cococay for SharePoint files.
Follow-up with Fanny is needed to confirm understanding and downstream usage.
Demand Files & Data Quality:
Updated Demand Files with null package type; requires follow-up with Fanny to confirm treatment and any necessary corrections.
Ben & Camilla
1. Supply Chain / IBP
Monitoring, Governance, and Analytics
Par Volatility Reporting (RCI/CCI):
Created an RCI/CCI min and max par volatility report to better understand inventory variability.
Next step: review findings and implications with Yan.
Table Freshness & Coverage:
Working on reading all created tables and their last updated date and pushing this as a Teams message for Yan and other stakeholders, enabling better oversight of data freshness.
In parallel, working on reading all source tables from production silver and production gold to hand off to the DE team so they can verify they have recreated all critical tables in the new environment.
Ben & Camilla
1. Supply Chain / IBP
Open Items / Pending
Data Quality & Inputs (Fanny):
Follow-up needed with Fanny on:
Missing LE in Container Load Date files.
Incorrect historical and future predictions for one product due to conversion factors.
Confirmation on handling of null package type in Demand Files.
Confirmation on HF&B with Cococay SharePoint setup.

---

### Customer Lifetime Value (Corporate Planning)

**Date:** 2025-12-19
**Business Area:** Customer Lifetime Value (Corporate Planning)
**Business Project:** Casino Spend Analysis

**Achievements:**
SSC Finance Tool – Pending. Add realized savings (RCI/CCI) to the pipeline – Pending, to close the loop between AI recommendations and financial impact tracking. Cihan
PCP Pricing Automation
2.1 OBR Waterpark PRE
Owner: Gang Wang | Status: In Progress
Data Foundation Stabilized
Issues with view tables were resolved by the DE team. Replaced all temporary tables previously used in modeling and optimization with the corrected, stable tables. With the updated tables, received refreshed data and retrained the demand model. Current PRE Optimization Status
Completed the first version of the PRE optimization. The current optimization run consistently returns the upper-bound constraint. Initially suspected low price elasticity as the driver; however, after updating elasticity parameters, the issue persists. Next Steps
Meeting scheduled with Ignacio to review the optimization component in detail and diagnose the constraint behavior. Will present the first version of PRE to Jorge, ensuring he sees current capabilities and constraints as we refine the model. Cihan
PCP Pricing Automation
2.2 Alaska Shorex
Owners: Gaby & Alex Correa | Status: In Progress
Met with Alex and Gaby where Kevin presented his EDA findings on Alaska Shorex. Aligned on next steps for the Alaska Shorex work based on those insights (e.g., further analysis and modeling directions discussed in the session). More of a planning meeting of how we want to structure the analysis. Great feedback from Correa on how we’re looking at shoreX. So far we’ve been looking at booking window and commonly bundled products, but feedback is to layer in CLV profiles and costs. Cihan
Digital RoyalOne – Guest Services Chatbot (Contact Center)
Owner: Eunha Kim | Status: In Progress
Continued coordination with stakeholders to identify patterns for additional escalation types beyond the current coverage. Stakeholders are still working on defining these patterns, which are needed to expand and refine chatbot escalation logic and automation opportunities. Caleb
3. CLV (Customer Lifetime Value) & Celebrations
Strategic Wins
CLV CAR Approval
Jordan and Joey successfully presented the CLV CAR to the capital committee, resulting in formal approval. Caleb
3. CLV (Customer Lifetime Value) & Celebrations
Strategic Wins
Celebrations Insights
Presented to Cory on the “celebrations” segment. Identified that consumers who have celebrated are the “best versions of themselves”, spending ~$200 median more per cruise. The uplift is driven primarily by:
Premium product choices, and
Higher Onboard Revenue (OBR) spend, particularly in Food & Beverage and Shorex. Caleb
3. CLV (Customer Lifetime Value)
Data & Pipeline Extension to 2025

**Raw Update:**
SSC Finance Tool – Pending.
Add realized savings (RCI/CCI) to the pipeline – Pending, to close the loop between AI recommendations and financial impact tracking.
Cihan
PCP Pricing Automation
2.1 OBR Waterpark PRE
Owner: Gang Wang | Status: In Progress
Data Foundation Stabilized
Issues with view tables were resolved by the DE team.
Replaced all temporary tables previously used in modeling and optimization with the corrected, stable tables.
With the updated tables, received refreshed data and retrained the demand model.
Current PRE Optimization Status
Completed the first version of the PRE optimization.
The current optimization run consistently returns the upper-bound constraint.
Initially suspected low price elasticity as the driver; however, after updating elasticity parameters, the issue persists.
Next Steps
Meeting scheduled with Ignacio to review the optimization component in detail and diagnose the constraint behavior.
Will present the first version of PRE to Jorge, ensuring he sees current capabilities and constraints as we refine the model.
Cihan
PCP Pricing Automation
2.2 Alaska Shorex
Owners: Gaby & Alex Correa | Status: In Progress
Met with Alex and Gaby where Kevin presented his EDA findings on Alaska Shorex.
Aligned on next steps for the Alaska Shorex work based on those insights (e.g., further analysis and modeling directions discussed in the session).
More of a planning meeting of how we want to structure the analysis. Great feedback from Correa on how we’re looking at shoreX. So far we’ve been looking at booking window and commonly bundled products, but feedback is to layer in CLV profiles and costs.
Cihan
Digital RoyalOne – Guest Services Chatbot (Contact Center)
Owner: Eunha Kim | Status: In Progress
Continued coordination with stakeholders to identify patterns for additional escalation types beyond the current coverage.
Stakeholders are still working on defining these patterns, which are needed to expand and refine chatbot escalation logic and automation opportunities.
Caleb
3. CLV (Customer Lifetime Value) & Celebrations
Strategic Wins
CLV CAR Approval
Jordan and Joey successfully presented the CLV CAR to the capital committee, resulting in formal approval.
Caleb
3. CLV (Customer Lifetime Value) & Celebrations
Strategic Wins
Celebrations Insights
Presented to Cory on the “celebrations” segment.
Identified that consumers who have celebrated are the “best versions of themselves”, spending ~$200 median more per cruise.
The uplift is driven primarily by:
Premium product choices, and
Higher Onboard Revenue (OBR) spend, particularly in Food & Beverage and Shorex.
Caleb
3. CLV (Customer Lifetime Value)
Data & Pipeline Extension to 2025

---

### Revenue Management Automation (RCI)

**Date:** 2025-12-19
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** PRE 4.0 Elasticity Enhancements

**Achievements:**
. Other Inputs Updated:
OBR data has been updated. Customer attributes from v-all-brands / Epsilon have been updated. Will use 2024 as a proxy for Acquisition Costs until the 2025 report from Catalyst is available at EOQ1. Pipeline Readiness:
The CLV pipeline is prepared to rerun; once Ticket data is updated, we will only need to hit refresh to generate the 2025 CLV view. Caleb
3. CLV (Customer Lifetime Value)
Future Capability: Enhanced Celebration Tagging
The extended CLV data will allow us to leverage Consumer Insight’s new survey, which identifies ~1/3 of passengers as celebrators, compared to the ~3% sample in our prior work. This will enable us to:
Rerun the celebration analysis using richer, survey-based tagging. Expand tagging beyond Trade and call center data, giving a more complete and scalable view of celebrators across the customer base. Erick

**Raw Update:**
.
Other Inputs Updated:
OBR data has been updated.
Customer attributes from v-all-brands / Epsilon have been updated.
Will use 2024 as a proxy for Acquisition Costs until the 2025 report from Catalyst is available at EOQ1.
Pipeline Readiness:
The CLV pipeline is prepared to rerun; once Ticket data is updated, we will only need to hit refresh to generate the 2025 CLV view.
Caleb
3. CLV (Customer Lifetime Value)
Future Capability: Enhanced Celebration Tagging
The extended CLV data will allow us to leverage Consumer Insight’s new survey, which identifies ~1/3 of passengers as celebrators, compared to the ~3% sample in our prior work.
This will enable us to:
Rerun the celebration analysis using richer, survey-based tagging.
Expand tagging beyond Trade and call center data, giving a more complete and scalable view of celebrators across the customer base.
Erick

---

### Project Axiom

**Date:** 2025-12-19
**Business Area:** Project Axiom
**Business Project:** Division-Level Medallia Reports

**Achievements:**
Generative AI SEAT Medallia: Key Project Updates
Presented "Emerging Negative Topics" report to Laura Hodges and Kieth Lane on Dec 16th. Both very supportive of the partnership Hotel Ops & AI. Both are hoping to see impact in tracking and correcting operational problems using this report. Laura expressed interest in a Drivers model and would like a follow up if/when the model is ready to be shared. Laura also asked if we plan to apply our GenAI approach to other datasets. (The answer was of course yes! Voice360)
Erick

**Raw Update:**
Generative AI SEAT Medallia: Key Project Updates
Presented "Emerging Negative Topics" report to Laura Hodges and Kieth Lane on Dec 16th. Both very supportive of the partnership Hotel Ops & AI. Both are hoping to see impact in tracking and correcting operational problems using this report.
Laura expressed interest in a Drivers model and would like a follow up if/when the model is ready to be shared.
Laura also asked if we plan to apply our GenAI approach to other datasets. (The answer was of course yes! Voice360)
Erick

---

### Project Axiom

**Date:** 2025-12-19
**Business Area:** Project Axiom
**Business Project:** Division-Level Medallia Reports

**Achievements:**
Generative AI SEAT Medallia:
Meta Data Extraction
Meta data extraction for new Division level report is complete. Guest logs data needs to be cleaned prior to project kick off next year. The Topic classifier model uses traditional embeddings based techniques and an LLM to consolidate the disparate "one-off" topics into bins of topics that can be tracked in unison. Reporting
Port-of-call report: Ready to be delivered to business for any port that is requested. The biggest blocker is the data mismatch between Unity Catalog and Medallia. Silversea received their first AI email this week. Will be working to make improvements/modifications. Division level email templates are on track to be delivered by end of year (Distribution list for Fleet detractor report: Raimund Gschaider, Jocelyn Lloret, Joao Mendonca, Richard Nentwich, christos Karavos, Nayoung Kim, IVELIN HRISTOV, FERNANDO CRAVO JORGE, Andreas Zachariou). Extracted "Positive Shore Excursion Verbatims" by Shore Ex product for Digital. The idea is to add a new feature to app/mobile that emphasizes guest feedback for each excursion (i.e. "The scuba diving was incredible! I saw my first shark!")
The team is creating a process to label/identify safety related concerns based on Medallia guest feedback. For EACH survey that ties to ShoreX we extract any/all safety related sentences and share with Risk Management. Legal sent a one-off request to a broader group (including AI) to identify "pricing", "offers, "promotions" related mentions by guests across all channels (contact center, medallia, guest logs). We will work on identifying such mentions in Medallia data.

**Focus Areas:**
Our team is working on a hybrid classifier to clean up existing/legacy topics.

**Raw Update:**
Generative AI SEAT Medallia:
Meta Data Extraction
Meta data extraction for new Division level report is complete.
Guest logs data needs to be cleaned prior to project kick off next year. Our team is working on a hybrid classifier to clean up existing/legacy topics. The Topic classifier model uses traditional embeddings based techniques and an LLM to consolidate the disparate "one-off" topics into bins of topics that can be tracked in unison.
Reporting
Port-of-call report: Ready to be delivered to business for any port that is requested. The biggest blocker is the data mismatch between Unity Catalog and Medallia.
Silversea received their first AI email this week. Will be working to make improvements/modifications.
Division level email templates are on track to be delivered by end of year (Distribution list for Fleet detractor report: Raimund Gschaider, Jocelyn Lloret, Joao Mendonca, Richard Nentwich, christos Karavos, Nayoung Kim, IVELIN HRISTOV, FERNANDO CRAVO JORGE, Andreas Zachariou).
Extracted "Positive Shore Excursion Verbatims" by Shore Ex product for Digital. The idea is to add a new feature to app/mobile that emphasizes guest feedback for each excursion (i.e. "The scuba diving was incredible! I saw my first shark!")
The team is creating a process to label/identify safety related concerns based on Medallia guest feedback. For EACH survey that ties to ShoreX we extract any/all safety related sentences and share with Risk Management.
Legal sent a one-off request to a broader group (including AI) to identify "pricing", "offers, "promotions" related mentions by guests across all channels (contact center, medallia, guest logs). We will work on identifying such mentions in Medallia data.

---

### Medallia

**Date:** 2025-12-19
**Business Area:** Medallia
**Business Project:** NPS Drivers Analysis for Alert System

**Achievements:**
The team is creating an evaluation dataset to baseline Genies ability to respond to questions. If Genie is found to be capable of answering a broad spectrum of questions, it may be integrated to the Axiom web app. Modeling
Initial Booking level drivers model is slated for delivery by end of year. POC Drivers Webapp integration will be the final delivery of the year. AB testing framework is ready and will go under peer review. Glen-Erik
Propel
Enabled Holiday offers previously set to awareness-only
24/7 support during Holidays: Onboarded offshore team to provide L1 support over the Holidays and call me or Eswar if there are issues depending on the time of the issue (India time -> Eswar, US time -> Glen-Erik). 24/7 support long-term: provided final feedback for the Service Now form to start using that in January once all the notifications and cofnigurations are setup in service now. Moving away from email support. Debugging issues with offer selection, only shorex and shipex offers are being generated. Had to roll back code and input configurations over the weekend to get back to normal but the exact source of the issue is not yet identified. Eswar

**Focus Areas:**
Erick & Cristian
MyCruise Recommender
Project Updates
The team is working to finalize the prod postgres db to support ForYou Calendar recommendations.

**Raw Update:**
The team is creating an evaluation dataset to baseline Genies ability to respond to questions. If Genie is found to be capable of answering a broad spectrum of questions, it may be integrated to the Axiom web app.
Modeling
Initial Booking level drivers model is slated for delivery by end of year.
POC Drivers Webapp integration will be the final delivery of the year.
Erick & Cristian
MyCruise Recommender
Project Updates
The team is working to finalize the prod postgres db to support ForYou Calendar recommendations.
AB testing framework is ready and will go under peer review.
Glen-Erik
Propel
Enabled Holiday offers previously set to awareness-only
24/7 support during Holidays: Onboarded offshore team to provide L1 support over the Holidays and call me or Eswar if there are issues depending on the time of the issue (India time -> Eswar, US time -> Glen-Erik).
24/7 support long-term: provided final feedback for the Service Now form to start using that in January once all the notifications and cofnigurations are setup in service now. Moving away from email support.
Debugging issues with offer selection, only shorex and shipex offers are being generated. Had to roll back code and input configurations over the weekend to get back to normal but the exact source of the issue is not yet identified.
Eswar

---

### RCI Revenue Management

**Date:** 2025-12-19
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model

**Achievements:**
Refactoring
Refactored ssc_daily_ship_sdt_category_farecode_bookings query and reduced runtime from 27hrs to 35min. (currently validating results, before pushing the change to prd)
Productionized clear_promo_uploaded_OBR, CEL_price_promo_uploads_OBR, RCI_price_promo_uploads_OBR, GTY_Lead_CEL_model_reraining workflows
AB-testing project repo CI/CD setup and discussions on execution flow
Reviewing feature store tables Data Engineering is migrating and helping them clearing their doubts and provide table refresh times
Providing ML support debugging issues
Monitoring CI/CD deployments, PRs
Glen-Erik & Ayon
Win-on-Waste Project
Migrated and standardized WOW workflows using Databricks Asset Bundles, applying Databricks best practices such as job clusters, bundle-managed paths, and centralized permissions and notifications. Refactored the PL_WOW_Specialty_V1 and PL_WOW_MDR_V1 workflows. Validated workflow behavior in QA, created pull requests to highlight changes, and coordinated next steps for promotion to main and deployment to production. Identified and escalated service principal permission gaps affecting access to the prd_digital_bi catalog.

**Raw Update:**
Refactoring
Refactored ssc_daily_ship_sdt_category_farecode_bookings query and reduced runtime from 27hrs to 35min. (currently validating results, before pushing the change to prd)
Productionized clear_promo_uploaded_OBR, CEL_price_promo_uploads_OBR, RCI_price_promo_uploads_OBR, GTY_Lead_CEL_model_reraining workflows
AB-testing project repo CI/CD setup and discussions on execution flow
Reviewing feature store tables Data Engineering is migrating and helping them clearing their doubts and provide table refresh times
Providing ML support debugging issues
Monitoring CI/CD deployments, PRs
Glen-Erik & Ayon
Win-on-Waste Project
Migrated and standardized WOW workflows using Databricks Asset Bundles, applying Databricks best practices such as job clusters, bundle-managed paths, and centralized permissions and notifications.
Refactored the PL_WOW_Specialty_V1 and PL_WOW_MDR_V1 workflows.
Validated workflow behavior in QA, created pull requests to highlight changes, and coordinated next steps for promotion to main and deployment to production.
Identified and escalated service principal permission gaps affecting access to the prd_digital_bi catalog.

---

_Source: 20251219 - Weekly Matt & Rafeh Updates.docx_