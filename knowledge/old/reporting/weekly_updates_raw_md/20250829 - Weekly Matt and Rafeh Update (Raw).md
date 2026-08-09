---
tags:
  - aagam_shah
  - alejandro_aristizabal-sanchez
  - arya_cheeti
  - atefeh_mahdavi
  - ayon_ghosh
  - brendan_turpin
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/hybris_product_recommendations_(digital)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/propel_targeted_offers_(cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/supply_chain_optimization
  - business_area/win-on-waste_(hotel_operations)
  - caleb_sharkey
  - camila_aichele
  - cihan_ulus
  - erick_alfaro
  - glen-erik_cortez
  - ignacio_villasmil
  - kartik_ullal
  - kevin_diaz
  - lamis_amer
  - mehdi_assefi
  - michelle_manfrini
  - project/advanced_modeling_development
  - project/automated_pricing_expansion
  - project/automation_upgrades
  - project/casino_spend_analysis
  - project/category_gapping_optimization_3.0
  - project/cltv-drivers_model_development
  - project/co-brand_credit_card_pilot
  - project/cococay_integration_and_guardrails
  - project/dart_logic_integration
  - project/division-level_medallia_reports
  - project/gty-lead_fare_optimization_model
  - project/gty-lead_fare_optimization_model_3.0
  - project/historical_data_integration
  - project/hvac_diagnostics_&_anomaly_detection
  - project/improved_forecasting_accuracy
  - project/marine_safety_analytics
  - project/measurement_refinement
  - project/mycruise_product_recommender_testing
  - project/pre_4.0_elasticity_enhancements
  - raw
  - reza_bahadori
  - srilekha_reddy_madupu
  - weekly_update
date: "2025-08-29"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2025-08-29

## Update 1

**Date:** 2025-08-29
**Business Area:** Medallia
**Business Project:** Division-Level Medallia Reports
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

Teams are focusing on items from last week addressing NPS discrepancies with Medallia (and our source data), backfilling guest log data for 2025, developing ship division-specific reporting tools, and completing topic classification for SilverSea service emails to optimize SNOW ticket templates.

### Raw Update

Teams are focusing on items from last week addressing NPS discrepancies with Medallia (and our source data), backfilling guest log data for 2025, developing ship division-specific reporting tools, and completing topic classification for SilverSea service emails to optimize SNOW ticket templates.

---

## Update 2

**Date:** 2025-08-29
**Business Area:** Hybris Product Recommendations (Digital)
**Business Project:** MyCruise Product Recommender Testing
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

Teams are continuing testing. DS Team & Digitall wrapping up the add-to-cart A/B test for MyCruise Recommender, showing early results of 15% (web) and 25% (app) click-through rates. Digital is compiling final conversion/revenue findings.

### Raw Update

Teams are continuing testing. DS Team & Digitall wrapping up the add-to-cart A/B test for MyCruise Recommender, showing early results of 15% (web) and 25% (app) click-through rates. Digital is compiling final conversion/revenue findings.

---

## Update 3

**Date:** 2025-08-29
**Business Area:** Customer Lifetime Value
**Business Project:** Casino Spend Analysis
**People:** [[caleb_sharkey/overview_caleb_sharkey|Caleb Sharkey]]

### Summarized Update

Ben & Caleb:
Customer Lifetime Value (CLV)
• Completed/Delivered:
o Presented Erick’s comment classification and Medallia analysis to the CLV team; aligned on integration value. • In Progress:
o Integrating Medallia-derived comment classification into the CLV dataset (scoping and approach).

### Raw Update

Ben & Caleb:
Customer Lifetime Value (CLV)
• Completed/Delivered:
o Presented Erick’s comment classification and Medallia analysis to the CLV team; aligned on integration value.
• In Progress:
o Integrating Medallia-derived comment classification into the CLV dataset (scoping and approach).

---

## Update 4

**Date:** 2025-08-29
**Business Area:** Customer Lifetime Value
**Business Project:** CLTV-Drivers Model Development
**People:** [[caleb_sharkey/overview_caleb_sharkey|Caleb Sharkey]]

### Summarized Update

Carlos
E Commerce Customer Targeting
• Completed/Delivered:
o Generated and cached waterfall and feature importance/contribution plots in the dashboard. • In Progress:
o Adding Shapley value computation and plots for ensembled models (pending dashboard integration):
 PHML (booking_propensity * spend), using the MShap library, similar to prior work on (bp * destination_propensity). Uplift metric: (booking_propensity_treatment_true - booking_propensity_treatment_false).

### Raw Update

Carlos
E Commerce Customer Targeting
• Completed/Delivered:
o Generated and cached waterfall and feature importance/contribution plots in the dashboard.
• In Progress:
o Adding Shapley value computation and plots for ensembled models (pending dashboard integration):
 PHML (booking_propensity * spend), using the MShap library, similar to prior work on (bp * destination_propensity).
 Uplift metric: (booking_propensity_treatment_true - booking_propensity_treatment_false).
Carlos
E Commerce Customer Targeting
• Next Steps:
o Integrate Shapley computations/plots into the dashboard for PHML and uplift models and validate results with stakeholders.
Mirielle
Contact Center: Lead Prioritization
BKTOCX — Back to Production
• Completed/Delivered:
o Production pipeline setup coordinated with Chandra (Aug 27, 2025 at 8:00 PM).
o Backups for all Siebel lead loads (CCI and RCI brands) using:
 SVAL_Path: /dbfs/mnt/adls/datascience/bktocx/rci_predictions/cvp_lead_load_da2i_{lead_type}SVAL{model}{current_date}{time_hour}_{Brand}.csv
 HVAL_Path: /dbfs/mnt/adls/datascience/bktocx/rci_predictions/cvp_lead_load_da2i_{lead_type}HVAL{model}{current_date}{time_hour}_{Brand}.csv
 MVAL_Path: /dbfs/mnt/adls/datascience/bktocx/rci_predictions/cvp_lead_load_da2i_{lead_type}MVAL{model}{current_date}{time_hour}_{Brand}.csv
 LVAL_Path: /dbfs/mnt/adls/datascience/bktocx/rci_predictions/cvp_lead_load_da2i_{lead_type}LVAL{model}{current_date}{time_hour}_{Brand}.csv
o Automated job failure notifications configured to:
 mfeudjio@rccl.com, cthatipalli@rccl.com, atomszay@rccl.com, bfowler@rccl.com, cgonzalezandarcio@rccl.com
o Production pipelines running:
 LEADS_SCORING_CELEBRITY_8_27_2025
 LEADS_SCORING_ROYAL_8_27_2025
 LEADS_SCORING_CELEBRITY_RIVER_GALAP_8_27_2025
Mirielle
Contact Center: Lead Prioritization
• Next Steps:
o Monitor the production pipeline through Wednesday, Sep 3, 2025.
Mirielle
Contact Center:
Workforce Planning – Staffing Model Development
• Completed/Delivered:
o Continued buildout of app sections for data visualization, call forecasting, and FTE forecasting across all LOBs.
o Held Tuesday feedback session on app development.
• In Progress:
o Implementing app functionality for user adjustments to call volume and saving results.
Mirielle
Contact Center:
Workforce Planning – Staffing Model Development
• Next Steps:
o Add a new app section to capture key assumptions:
 AHT
 In office shrinkage
 Out of office shrinkage
 Abandon target
o Collaborate with Eswar to enable Jason Atkerson’s access to the app.
Ben & Camila
IBP: Supply Chain
Silversea
• Completed/Delivered:
o Delivered Silversea Order Creation dataset using the new voyage demand forecast. Allocates demand to sailings where product loading is possible; if one or more sailings cannot be loaded, days of unmet demand until the next loading are allocated to the prior sailing where the product is loaded. Joined new order template data with voyage and voyage demand forecast data.
• Next Steps:
o Validate allocations with business stakeholders and refine if needed.

---

## Update 5

**Date:** 2025-08-29
**Business Area:** Supply Chain
**Business Project:** CocoCay Integration and Guardrails
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Uniforms
• Completed/Delivered:
o Delivered to Yan a new weekly process with a ship+product model to ensure no join errors with consumption history. After model completion, joined cost center and contract length (days) and adjusted the first consumption value across ship+product+cost center+contract length combinations. Introduced variability using ratio = crew * consumption / sum(crew).

### Raw Update

Uniforms
• Completed/Delivered:
o Delivered to Yan a new weekly process with a ship+product model to ensure no join errors with consumption history. After model completion, joined cost center and contract length (days) and adjusted the first consumption value across ship+product+cost center+contract length combinations. Introduced variability using ratio = crew * consumption / sum(crew).
• In Progress/Pending:
o Add job_code and job_description columns to the adjusted table. Current challenge: table checkpointing is slow; delivered the initial version without these columns to meet timeline. Will attempt checkpoint again with job fields.
o Add modified product names to the new process so adjustments apply to this model version as well.
Ben & Camila
IBP: Supply Chain
PRD Silver Tracking
• Completed/Delivered:
o Delivered to Ben and Yan: process to check max date for tables in prd_silver.ibp against (current date − 3 days); if max date is older than 3 days, throw an error and send a notification to Ben and Yan.
• In Progress/Pending:
o Currently only tracking the consumption and spend reports. Plan to expand coverage to all relevant tables, which will require identifying appropriate date columns for consistency.
Ben & Camila
IBP: Supply Chain
Cococay
• Completed/Delivered:
o Delivered to Yan updated backtested dates incorporating new consumption values.
New Ship Automation
• Completed/Delivered:
o Delivered to Fanny: fixed weekend error that blocked delivery of new ships and brand substitutions; Ben confirmed pipeline success. We are on time to deliver Legend of the Seas demand forecast as required.
Cihan
Onboard Revenue
• Completed/Delivered:
o Presented latest EDA results to stakeholders and collected feedback.
o EDA completed.
• Next Steps:
o Prepare and deliver presentation of findings to Gang.
Cihan
Digital: App Reviews Project
• Completed/Delivered:
o Met with Jaime and reviewed the latest analysis results.
o Completed topic classification review.
• Next Steps:
o Deploy the topic classification model to production so the Digital team can begin using app reviews data.

---

## Update 6

**Date:** 2025-08-29
**Business Area:** Project Axiom
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Cihan
Digital: App Reviews Project
Guest Services Chatbot Project
• Completed/Delivered:
o Attended vendor meeting with Eunha’s team. • In Progress/Issues:
o Vendor-side issue with ST data is blocking data integration into the model and updates to chatbot dashboards. • Next Steps:
o Await vendor resolution of ST data issue; proceed with model integration and dashboard refresh immediately after.

### Raw Update

Cihan
Digital: App Reviews Project
Guest Services Chatbot Project
• Completed/Delivered:
o Attended vendor meeting with Eunha’s team.
• In Progress/Issues:
o Vendor-side issue with ST data is blocking data integration into the model and updates to chatbot dashboards.
• Next Steps:
o Await vendor resolution of ST data issue; proceed with model integration and dashboard refresh immediately after.

---

## Update 7

**Date:** 2025-08-29
**Business Area:** WoW
**Business Project:** Improved Forecasting Accuracy
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

Key Features of the MDR V1 Pipeline:
The pipeline simultaneously trains thousands of models on two different data sources: POS data and Xdining data. Each data source undergoes separate feature engineering. Forecasts from both the POS models and Xdining models are combined using a stacked modeling approach.

### Raw Update

Key Features of the MDR V1 Pipeline:
The pipeline simultaneously trains thousands of models on two different data sources: POS data and Xdining data. Each data source undergoes separate feature engineering.
Forecasts from both the POS models and Xdining models are combined using a stacked modeling approach. Thousands of stacked models are trained in parallel on the outputs of the initial models.
At the end of the pipeline, a rules engine evaluates the forecasts from the three model types (POS, Xdining, and stacked) and selects the best forecast based on recent accuracy metrics. This selection is optimized for the upcoming itinerary of the ship.
The model accounts for menu rotation by estimating the likelihood that a recipe will be repeated, especially if the scheduled menu rotation is disrupted.
The pipeline addresses the cold start problem for ships deployed on new itineraries with no prior deployment history. For example, the ship GR was deployed in Southeast Asia with Chinese recipes, a scenario not previously encountered.
Extensive support and communication with executive chefs from all 28 ships as part of FPMS roll out
Impact:
This new pipeline improved forecast accuracy by approximately 60% compared to the existing MDR pipeline.
The improvement applies to about 92% of the recipes across the MDR fleetwide.
This approach has positioned us well to deliver more reliable demand forecasts and support operational planning across diverse and evolving itineraries.

---

## Update 8

**Date:** 2025-08-29
**Business Area:** CEL Revenue Management
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

• This week, I focused on rewriting the MTRB code to allow data appending every three months (pending discussion of this rule with the business team). I also developed a framework to export the output to a SharePoint file for analysts to review and update, then read the modified file to apply changes to the baskets. Additionally, I created a method to run the MTRB code weekly with logging, and implemented a similar SharePoint process to support this workflow.

### Raw Update

• This week, I focused on rewriting the MTRB code to allow data appending every three months (pending discussion of this rule with the business team). I also developed a framework to export the output to a SharePoint file for analysts to review and update, then read the modified file to apply changes to the baskets. Additionally, I created a method to run the MTRB code weekly with logging, and implemented a similar SharePoint process to support this workflow.
RCI  Revenue Management | Comparison Analysis between Web Based and Original Baskets
• This week I worked on getting the web baskets for RCI for the analysis to compare them with the actual baskets

---

## Update 9

**Date:** 2025-08-29
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

• Get Historical Price Change Recommendations
• . In the PRE pipeline, recommendations are generated using the pre.temp_track table, which includes all future sailings and extends through February 2027. This table also contains historical data dating back to 2023.

### Raw Update

• Get Historical Price Change Recommendations
• . In the PRE pipeline, recommendations are generated using the pre.temp_track table, which includes all future sailings and extends through February 2027. This table also contains historical data dating back to 2023.
• However, the new model lacked historical price recommendations due to the absence of prior runs. As a result, the final recommendation table did not include earlier history.
• To address this, historical recommendations were generated separately using a dedicated process for validation. This leveraged both pre.temp_track and prd_silver.revstrat.future_fit_track, applying seasonal logic (PEAK/OFFPEAK) to calculate rolling window values. These records are stored in a new table:
• dev_revenue_mgmt_bu.pre_rci_intermed.pre_elasticity_recs_4_0_hist
• This ensures historical continuity and supports validation of the new model’s performance.

---

## Update 10

**Date:** 2025-08-29
**Business Area:** PCP Pricing Automation
**Business Project:** Automated Pricing Expansion
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

RCI | Productionize the Automated Hybris Promo UploadBy 8/21/25:
the SharePoint was created in order to streamline the automated promo uploads from OBR team strategy (independent of the PRE)
a PRE-driven automation of promo uploads was coded. testing was started for this which highlighted some bugs that the digital team identified and needed to fix
automated promo uploads from OBR team strategy (independent of the PRE) was also coded in a very robust & dynamic manner. this has not been tested yet, but is expected to be tested after the bugs with the PRE-driven automation are fixed by the other team
conversations were had with both brands (RCI + CEL) to determine some of the useful business rules that can be used to implement some cross joins on the PRE-driven promo uploads.

### Raw Update

RCI | Productionize the Automated Hybris Promo UploadBy 8/21/25:
the SharePoint was created in order to streamline the automated promo uploads from OBR team strategy (independent of the PRE)
a PRE-driven automation of promo uploads was coded. testing was started for this which highlighted some bugs that the digital team identified and needed to fix
automated promo uploads from OBR team strategy (independent of the PRE) was also coded in a very robust & dynamic manner. this has not been tested yet, but is expected to be tested after the bugs with the PRE-driven automation are fixed by the other team
conversations were had with both brands (RCI + CEL) to determine some of the useful business rules that can be used to implement some cross joins on the PRE-driven promo uploads. this would result in things such as additional X% off for loyalty members, casino members, or pax of certain cabin classes. this has not been coded yet, but the business knowledge/rules were learned in order to code this upgraded version of the PRE-drive promo upload automation

---

## Update 11

**Date:** 2025-08-29
**Business Area:** Loyalty
**Business Project:** Co-Brand Credit Card Pilot
**People:** [[kartik_ullal/overview_kartik_ullal|Kartik Ullal]], [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

LOYALTY | Credit Card Pilot
• Status: This ticket is complete as of 08/28/2025
• Deliverables:
• This was for Ad Hoc analysis for Credit Card Pilot. Calculated the dollar value for each credit card, acquisition rates for active and non active members and also calculated the total number of guests that would move from tier 2 to 3 based on benefits received. • Potential future issue: None

### Raw Update

LOYALTY | Credit Card Pilot
• Status: This ticket is complete as of 08/28/2025
• Deliverables:
• This was for Ad Hoc analysis for Credit Card Pilot. Calculated the dollar value for each credit card, acquisition rates for active and non active members and also calculated the total number of guests that would move from tier 2 to 3 based on benefits received.
• Potential future issue: None

---

## Update 12

**Date:** 2025-08-29
**Business Area:** RCI Revenue Management
**Business Project:** Automation Upgrades
**People:** Unidentified

### Summarized Update

This project required an incredible amount of sleuthing and problem solving. The ultimate solution was a clever workaround a AS400 system shortcoming (not keying two key inventory tables in sync) that only became apparent as we’ve scaled up inventory automation. • This ticket is now complete as of August 29, 2025.

### Raw Update

This project required an incredible amount of sleuthing and problem solving. The ultimate solution was a clever workaround a AS400 system shortcoming (not keying two key inventory tables in sync) that only became apparent as we’ve scaled up inventory automation.
• This ticket is now complete as of August 29, 2025.
• What I did:
• Completed analysis of improper limit settings.
• Identified the data lag caused by AS400 updates to the ICGTLD table.
• Rescheduled automation processes to run at safer times to avoid issues from the lag.
• Met with IT, who agreed to run their internal cleanup processes more than once daily.
• Met with RCI and presented findings and recommendations.
• Collaborations:
• Aarish Salam Memon and I met with Donna’s team, who agreed to run inventory cleanup more frequently. This will help improve the accuracy of GTY automation.
• RCI also agreed to align their processing times with Celebrity’s schedule.
• Changes implemented:
• Moved FIT berthing from 6:30 AM to 9:30 PM to better align with AS400 cleanup macros.
• Added a 2:30 AM replenishment run to generate cleaner limits based on accurate booked/offered counts.
• Results:
• Updates worked well—clean runs with no lingering issues.
• No delays or future risks identified.

---

## Update 13

**Date:** 2025-08-29
**Business Area:** CEL Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model 3.0
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

• - Explored new features. LAF feature was not significant. Category type leads to more successful result.

### Raw Update

• - Explored new features. LAF feature was not significant. Category type leads to more successful result. WTS bins are now more granular at 5 week groupings, which better fits business uses. Models are also trained on all weeks of data now, not filtering to 12-50 weeks anymore as was previously done. There is better data now for far out bookings so we can output recommendation on those sailings.
• - Models are also trained on all weeks of data now, not filtering to 12-50 weeks anymore as was previously done. There is better data now for far out bookings so we can output recommendation on those sailings. This increases the WTS bins used in the optimization.
• - Backtested all 2.0 and 3.0 model for both brands. Model performance is constant across splits.
• - Dug into specific finalized sailings to compare “optimal” performance with actual booking behavior. Calculated NTR, booking shares, posted prices for all weeks. Analyzed historical, current posted, and optimal gaps between all tiers. Created meta and ship-class level plots to present to business as well as visuals comparing average gaps in place vs. recommended.

---

## Update 14

**Date:** 2025-08-29
**Business Area:** RCI Revenue Management
**Business Project:** DART Logic Integration
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Create bkg thresholds (ranges) at 20 and 40 wts and integrate this into the optimization logic
• Generated bkg thresholds at 20 and 40 WTS at the meta-ship code - sail month - cat class level. upper and lower bounds are based on 10th and 90th percentiles. These are used in the optimization to ensure that the optimal cum bks at 20 and 40 WTS are in line with what the business has been observing historically.

### Raw Update

Create bkg thresholds (ranges) at 20 and 40 wts and integrate this into the optimization logic
• Generated bkg thresholds at 20 and 40 WTS at the meta-ship code - sail month - cat class level. upper and lower bounds are based on 10th and 90th percentiles. These are used in the optimization to ensure that the optimal cum bks at 20 and 40 WTS are in line with what the business has been observing historically.
• My observation → In some cases the range is too large / too tight (as shown below). If it is large, the optimal solution does not vary. In the case of tight bounds, in many cases the solution is infeasible. The reason is because when considering the bounds imposed on the weekly bkgs, it could happen that for example the aggregation of LBs up to the 20 or 40 WTS is less than the imposed threshold, or the cum UB is > the imposed threshold at 20 or 40 WTS.
• This requires further investigation for the infeasibility.
• When more accurate UBs on the weekly bkgs are considered based on the shared demand, I will revisit these thresholds. For this, I will close this ticket for now - will open a new one in Sept.
• Create Data-Driven Bkg waves instead of the hard-coded ones. Integrate these into the optimization logic
• https://royal-it.atlassian.net/browse/RMA-4458

---

## Update 15

**Date:** 2025-08-29
**Business Area:** CEL Revenue Management
**Business Project:** Category Gapping Optimization 3.0
**People:** [[srilekha_reddy_madupu/overview_srilekha_reddy_madupu|Srilekha Reddy Madupu]]

### Summarized Update

Need to investigate transformation functions for CEL
• Summary: Transformation Testing & Model Selection
• Status: Complete as of August 28, 2025
• Key Findings:
• Tested multiple transformation methods (grouped and ungrouped); some meta-category classes were missing due to sparse data in certain groupings. • Removing transformations allowed the pipeline to run cleanly, consistently selecting static bin A over spline binning. • Why Spline Binning Fails:
• Sparse demand: Most bins have 0–3 bookings.

### Raw Update

Need to investigate transformation functions for CEL
• Summary: Transformation Testing & Model Selection
• Status: Complete as of August 28, 2025
• Key Findings:
• Tested multiple transformation methods (grouped and ungrouped); some meta-category classes were missing due to sparse data in certain groupings.
• Removing transformations allowed the pipeline to run cleanly, consistently selecting static bin A over spline binning.
• Why Spline Binning Fails:
• Sparse demand: Most bins have 0–3 bookings.
• Limited price variation: Prices stay within a narrow range (~$100–$150).
• Low data density: Especially in far-out bins, making spline estimates unstable.
• No clear demand-price trend: Scatter plots show weak or no relationship.
• Conclusion:
• Spline binning adds complexity without improving model fit.
• Static bin A is preferred due to its stability and better R² performance under current data conditions.

---

## Update 16

**Date:** 2025-08-29
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model
**People:** Unidentified

### Summarized Update

Feature Store:
Identified tables generated by feature store and which ones are being used in which RMA project so Data Engineering can focus only on the tables that are actually in use. Updated fs_daily_inv_avail_features_GENERATE pipeline, by adding ship_adt_class_v4 query. OBR:
Implementing Sharepoint connection in OBR project
Updated OBR drink package Optimization workflow and reduced 2hrs of run time.

### Raw Update

Feature Store:
Identified tables generated by feature store and which ones are being used in which RMA project so Data Engineering can focus only on the tables that are actually in use.
Updated fs_daily_inv_avail_features_GENERATE pipeline, by adding ship_adt_class_v4 query.
OBR:
Implementing Sharepoint connection in OBR project
Updated OBR drink package Optimization workflow and reduced 2hrs of run time.
Operations:
Pause pre_ssc_uploads workflow
Debug PRE pipeline and fix package issues.
Updating Databricks Linked service using latest DBR in PRE_Pipeline2_MainRun notebook in ADF
PR reviews and monitoring CI/CD deployment pipelines
PRE:
Help in committing changes to PRE elasticity model and deploy those changes
Parametrize elasticity model notebook and modifying cluster configurations and make sure developers able to run updated elasticity model package.
Data Validation Framework:
Update the data validation package with latest changes made, and currently applying this to TAP SUITES project.
Knowledge transfer sessions on SPI and MTRB projects

---

## Update 17

**Date:** 2025-08-29
**Business Area:** PROPEL
**Business Project:** Measurement Refinement
**People:** [[glen-erik_cortez/overview_glen-erik_cortez|Glen-Erik Cortez]], [[alejandro_aristizabal-sanchez/overview_alejandro_aristizabal-sanchez|Alejandro Aristizabal-Sanchez]]

### Summarized Update

Generated AdHoc offers for testing. Simulated 2 years of voyages to study control vs test distributions. Proposed 4 measurement methods:
Difference in means (bootstrapping CIs, Welch t-test for variance)
Aggregation-based (sample weights, fixed effects)
Regression (simple and with category interactions)
Causal modeling

### Raw Update

Generated AdHoc offers for testing.
Simulated 2 years of voyages to study control vs test distributions.
Proposed 4 measurement methods:
Difference in means (bootstrapping CIs, Welch t-test for variance)
Aggregation-based (sample weights, fixed effects)
Regression (simple and with category interactions)
Causal modeling

---

## Update 18

**Date:** 2025-08-29
**Business Area:** MIAP
**Business Project:** HVAC Diagnostics & Anomaly Detection
**People:** [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]]

### Summarized Update

• Completed the implementation of new logic for deviation and baseline calculation across the entire fleet, completing the hotel and service power areas. • Began modifying existing scripts for feature calculation and results computation to enable parallelization of workflows per ship. This reduces calculation time and resource usage.

### Raw Update

• Completed the implementation of new logic for deviation and baseline calculation across the entire fleet, completing the hotel and service power areas.
• Began modifying existing scripts for feature calculation and results computation to enable parallelization of workflows per ship. This reduces calculation time and resource usage. HVAC is the first area to demonstrate proof of implementation, with hotel, machinery, and service power areas to follow.
• Prepared and presented the first biweekly presentation to the team and the Senior Director of AI & Analytics, covering the new AHU anomaly detection model, reporting, and savings.
• Fixed a bug in GMO plots for ships with no data in AHU analytics.

---

## Update 19

**Date:** 2025-08-29
**Business Area:** MIAP
**Business Project:** Marine Safety Analytics
**People:** [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

• Attended Support Check-in call with Capgemini team; discussed recent job failures and job monitoring statistics
• Helped Maritime Safety engineer deploy changes to Lloyd's Register pipeline; decoupled Sea Event tasks into standalone pipeline to avoid race condition with dependent file arrival
• Performed root cause analysis on issues with Star of the Seas Propulsion data; identified spelling differences that caused filter problems with certain voyage phases; identified missing Eniram voyage phase mapping; switched to use new "common features" table for fallback voyage phase calculation
• Fixed bug in marine-analytics Python package related to Fuel Forecast API 'util' folder not being recognized as a package
• Worked with MIAP Data Engineer to troubleshoot errors and discuss strategies when requesting data from the Eniram API
• Worked with MIAP Data Science Analyst to identify root cause of location errors on Star of the Seas (no negative signs on lat/long, missing tag to determine direction from equator/prime meridian)
• Helped MIAP Data Engineer with troubleshooting Asset Bundle deployment errors
Created ALS Compressor Power Feature notebook; performed EDA and began experimenting with base model.

### Raw Update

• Attended Support Check-in call with Capgemini team; discussed recent job failures and job monitoring statistics
• Helped Maritime Safety engineer deploy changes to Lloyd's Register pipeline; decoupled Sea Event tasks into standalone pipeline to avoid race condition with dependent file arrival
• Performed root cause analysis on issues with Star of the Seas Propulsion data; identified spelling differences that caused filter problems with certain voyage phases; identified missing Eniram voyage phase mapping; switched to use new "common features" table for fallback voyage phase calculation
• Fixed bug in marine-analytics Python package related to Fuel Forecast API 'util' folder not being recognized as a package
• Worked with MIAP Data Engineer to troubleshoot errors and discuss strategies when requesting data from the Eniram API
• Worked with MIAP Data Science Analyst to identify root cause of location errors on Star of the Seas (no negative signs on lat/long, missing tag to determine direction from equator/prime meridian)
• Helped MIAP Data Engineer with troubleshooting Asset Bundle deployment errors
Created ALS Compressor Power Feature notebook; performed EDA and began experimenting with base model.

---

## Update 20

**Date:** 2025-08-29
**Business Area:** MIAP
**Business Project:** Advanced Modeling Development
**People:** Unidentified

### Summarized Update

Completed modeling on 17 ships, added them to GMO app model diagnostics
Documented data issues with ships not added to modeling workflow
fixed issues with ships without vps reports
updated fuel tag configs for ships using LNG
added star to power plant analytics

### Raw Update

Completed modeling on 17 ships, added them to GMO app model diagnostics
Documented data issues with ships not added to modeling workflow
fixed issues with ships without vps reports
updated fuel tag configs for ships using LNG
added star to power plant analytics

---

## Update 21

**Date:** 2025-08-29
**Business Area:** MIAP
**Business Project:** Marine Safety Analytics
**People:** [[arya_cheeti/overview_arya_cheeti|Arya Cheeti]]

### Summarized Update

• Fixed workflow problems for HVACR specifically for the ships [ML,SM,CS,IN]
• Fixed bugs relating to propulsion navigation hull analytics, Star had no data voyage phase data relating to maneuvering . • Found a problem with longitude and latitude data with Star
• Implemented a quick fix by adding a negative sign before the longitude values, this fix will work till 2027 as per the chartering. Star will only be sailing in quadrants of negative longitude till 2027.

### Raw Update

• Fixed workflow problems for HVACR specifically for the ships [ML,SM,CS,IN]
• Fixed bugs relating to propulsion navigation hull analytics, Star had no data voyage phase data relating to maneuvering .
• Found a problem with longitude and latitude data with Star
• Implemented a quick fix by adding a negative sign before the longitude values, this fix will work till 2027 as per the chartering. Star will only be sailing in quadrants of negative longitude till 2027. This has been added to the exceptions notebook for common features.
• Added a feature called flagged to safety analytics dataset which flags an incident if it occurred during a scheduled work order
• Added explorer of the seas to HVAC and Chiller
Creating a flow diagram on confluence for the order of deployment of ship components (HVAC, machinery, etc)

---

## Update 22

**Date:** 2025-08-29
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** Unidentified

### Summarized Update

This Week-
• Worked on the Eniram code for 10-minute aggregation and corrected previous implementations to accurately extract the required columns from metadata. • Developed a new Silver table for Eniram, along with a new Eniram Silver notebook. • Tested data in the Eniram IoT table to ensure all necessary tags for the Enriched, Port, and Leg tables are present and correct.

### Raw Update

This Week-
• Worked on the Eniram code for 10-minute aggregation and corrected previous implementations to accurately extract the required columns from metadata.
• Developed a new Silver table for Eniram, along with a new Eniram Silver notebook.
• Tested data in the Eniram IoT table to ensure all necessary tags for the Enriched, Port, and Leg tables are present and correct.
• Progressed on deploying the workflows and notebooks to the production environment.
Next Week's Focus
• Replace the old Eniram Silver notebook with the new version and verify data accuracy across all dashboards.
Complete the deployment of all Eniram-related workflows

---

## Update 23

**Date:** 2025-08-29
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** [[mehdi_assefi/overview_mehdi_assefi|Mehdi Assefi]]

### Summarized Update

• Performed additional feature engineering to extract missing values from the training data. Improved accuracy for both models targeting weights under 1000kg and above 1000 kg. • Created the meta model by stacking the base models to make the final prediction.

### Raw Update

• Performed additional feature engineering to extract missing values from the training data. Improved accuracy for both models targeting weights under 1000kg and above 1000 kg.
• Created the meta model by stacking the base models to make the final prediction.
• Transformed the SY test data to match the trained models to perform prediction.
I will continue working to wrap up the regression model and also to generalize the model as a tool as part of the AI agent.

---

_Source: 20250829 - Weekly Matt and Rafeh Update (Raw).docx_