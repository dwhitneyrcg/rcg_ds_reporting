---
tags:
  - aagam_shah
  - arya_cheeti
  - atefeh_mahdavi
  - brendan_turpin
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/customer_targeting_(e-commerce)
  - business_area/hybris_product_recommendations_(digital)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/supply_chain_optimization
  - camila_aichele
  - carlos_gonzalez_andarcio
  - cihan_ulus
  - erick_alfaro
  - gaurav_godawat
  - ignacio_villasmil
  - kartik_ullal
  - kevin_diaz
  - lamis_amer
  - mahshad_shariatnasab
  - mehdi_assefi
  - mert_ersoz
  - michelle_manfrini
  - parimala_kettymuthu
  - project/ada-accessible_berthing_migration
  - project/advanced_modeling_development
  - project/asset_management_expansion
  - project/automated_pricing_expansion
  - project/automation_upgrades
  - project/co-brand_credit_card_pilot
  - project/dart_logic_integration
  - project/division-level_medallia_reports
  - project/enhanced_for_you_recommendations
  - project/enhanced_negative_feedback_alerts
  - project/expedition_forecasting_with_silversea_automation
  - project/gty-lead_fare_optimization_model_3.0
  - project/historical_data_integration
  - project/hvac_diagnostics_&_anomaly_detection
  - project/inventory_automation_(fit_reberthing_&_groups_processes)
  - project/lead_prioritization_-_bk2cx_(rci_&_cel)
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/marine_safety_analytics
  - project/miap_operating_efficiency_enhancements
  - project/offer_to_cancel_(oftocx)_model_(rci_&_cel)
  - project/pre_4.0_elasticity_enhancements
  - project/uplift_models
  - raw
  - reza_bahadori
  - srilekha_reddy_madupu
  - weekly_update
date: "2025-08-22"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2025-08-22

## Update 1

**Date:** 2025-08-22
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - BK2CX (RCI & CEL)
**People:** Unidentified

### Summarized Update

Collaborating with the Siebel team to ensure accurate lead ingestion for both Royal and Celebrity. Monitoring key data-quality metrics: phone number format, output file format, min/max sequence_id, and lead counts across both systems. Built a separate process to handle River Cruise and Galapagos Cruise (SVAL) feeds; expected output files are loading into the Siebel system.

### Raw Update

Collaborating with the Siebel team to ensure accurate lead ingestion for both Royal and Celebrity.
Monitoring key data-quality metrics: phone number format, output file format, min/max sequence_id, and lead counts across both systems.
Built a separate process to handle River Cruise and Galapagos Cruise (SVAL) feeds; expected output files are loading into the Siebel system.
Conducted additional testing this week; ongoing validation of file loads into Siebel continues.

---

## Update 2

**Date:** 2025-08-22
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** Unidentified

### Summarized Update

Updated and reviewed the LOB mapping for Casino. Ran basic call volume forecasts for all LOBs. Executed FTE model runs for all LOBs based on the basic call volume forecasts.

### Raw Update

Updated and reviewed the LOB mapping for Casino.
Ran basic call volume forecasts for all LOBs.
Executed FTE model runs for all LOBs based on the basic call volume forecasts.
Continued development of app sections for data visualization, call forecasting, and FTE forecasting across all LOBs.
Scheduled a feedback session for next Tuesday to gather input on the in-progress app development.

---

## Update 3

**Date:** 2025-08-22
**Business Area:** Customer Targeting
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]]

### Summarized Update

Attended finalist presentations from Braze, Salesforce, and SAP. Provided additional feedback to Matt and David via Teams on 8/21.

### Raw Update

Attended finalist presentations from Braze, Salesforce, and SAP.
Provided additional feedback to Matt and David via Teams on 8/21.

---

## Update 4

**Date:** 2025-08-22
**Business Area:** Customer Lifetime Value
**People:** Unidentified

### Summarized Update

Stakeholders initially requested ingesting all ~1,400 Medallia columns; after discussion, the CLV team will provide a narrowed, defined set of columns.

### Raw Update

Stakeholders initially requested ingesting all ~1,400 Medallia columns; after discussion, the CLV team will provide a narrowed, defined set of columns. Awaiting that list.

---

## Update 5

**Date:** 2025-08-22
**Business Area:** Customer Targeting
**Business Project:** Uplift Models
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]]

### Summarized Update

Fixed a dev dashboard issue affecting new dependency plots (matplotlib state was not being cleared between page renders). Improved dashboard performance by generating and caching dependency plots automatically upon the weekly data update. Trained stakeholders on best practices for using uplift models.

### Raw Update

Fixed a dev dashboard issue affecting new dependency plots (matplotlib state was not being cleared between page renders).
Improved dashboard performance by generating and caching dependency plots automatically upon the weekly data update.
Trained stakeholders on best practices for using uplift models.
Participated in Journey Orchestration RFP meetings.

---

## Update 6

**Date:** 2025-08-22
**Business Area:** Supply Chain
**Business Project:** Expedition Forecasting with Silversea Automation
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]], [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Added a Price Prediction column to the Finance Tool using a six-stage approach to estimate likely product prices per ship based on historical consumption and purchase order data. Corrected the Finance Tool to use the archival demand forecast table (instead of version history), resolving an error caused by platform-side cleanup and reducing future pipeline risk. Silversea order creation: Allocated monthly demand forecasts to the voyage level using PCD forecasts; conducted extensive validation and confirmed the dataset is valid.

### Raw Update

Added a Price Prediction column to the Finance Tool using a six-stage approach to estimate likely product prices per ship based on historical consumption and purchase order data.
Corrected the Finance Tool to use the archival demand forecast table (instead of version history), resolving an error caused by platform-side cleanup and reducing future pipeline risk.
Silversea order creation: Allocated monthly demand forecasts to the voyage level using PCD forecasts; conducted extensive validation and confirmed the dataset is valid.
Cococay: Rerunning backtests so the challenger model’s 12-month average reflects the July 2025 improvements; reprocessing coverage for Jan 2024–Jun 2025.
Uniform: Testing new consumption data incorporating crew columns; current forecasting horizon weeks are insufficient—continuing work. Will review the product cost column noted by Yan; expect alignment once consumption data is approved.
Automated reports: Identified inconsistencies in the spend report versus the Hyperion table; Yan (Supply Chain) engaged Vikas (Data Engineering) to reconcile and ensure matching data.
New ship automation and brand substitutions: Running the updated pipeline to support Legend of the Seas and brand substitutions; validating execution so Fanny can proceed.
Pending: SSC order creation; update RCI/CCI order creation per new calculation methodology (reviewing the meeting recording and Yan’s email).

---

## Update 7

**Date:** 2025-08-22
**Business Area:** PCP Pricing Automation
**Business Project:** Automated Pricing Expansion
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

ShoreX Pricing Recommendation Engine: Met with stakeholders to present the latest EDA results and gather feedback. Developed and shared new EDA plots summarizing last week’s findings for visibility and tracking. Planning to complete the EDA phase and present findings to Gang (OBR Leadership) next week.

### Raw Update

ShoreX Pricing Recommendation Engine: Met with stakeholders to present the latest EDA results and gather feedback. Developed and shared new EDA plots summarizing last week’s findings for visibility and tracking.
Planning to complete the EDA phase and present findings to Gang (OBR Leadership) next week.

---

## Update 8

**Date:** 2025-08-22
**Business Area:** Project Axiom
**Business Project:** Enhanced Negative Feedback Alerts
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Received and incorporated feedback from Jaime to update topic descriptions. Tested the model with the updated descriptions and validated results. Ran the model and produced new classification results; will share with Jaime and conduct a final review.

### Raw Update

Received and incorporated feedback from Jaime to update topic descriptions.
Tested the model with the updated descriptions and validated results.
Ran the model and produced new classification results; will share with Jaime and conduct a final review.
Upon approval, will deploy the model to production.

---

## Update 9

**Date:** 2025-08-22
**Business Area:** Project Axiom
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Updated guest log data. Awaiting updated chatbot data; once available, will add “Star” to the existing dashboards.

### Raw Update

Updated guest log data.
Awaiting updated chatbot data; once available, will add “Star” to the existing dashboards.

---

## Update 10

**Date:** 2025-08-22
**Business Area:** MIAP
**Business Project:** Asset Management Expansion
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

*Mert was invited to join Asset Management workshop with GMO leaders in Houston and discussed collaboration opportunities with American Beurre of Shipping
*Working on enhanced version of RD class power plant optimizer

### Raw Update

*Mert was invited to join Asset Management workshop with GMO leaders in Houston and discussed collaboration opportunities with American Beurre of Shipping
*Working on enhanced version of RD class power plant optimizer

---

## Update 11

**Date:** 2025-08-22
**Business Area:** MIAP
**Business Project:** Marine Safety Analytics
**People:** Unidentified

### Summarized Update

This Week's Highlights
Worked on fixing issues in the Safety Culture Data Feeds category; data is now loading correctly into the Silver layer. I’ve requested the product owner to review the data. Analyzed values required for other Safety Culture categories and reached out to the Safety Culture team for additional input.

### Raw Update

This Week's Highlights
Worked on fixing issues in the Safety Culture Data Feeds category; data is now loading correctly into the Silver layer. I’ve requested the product owner to review the data.
Analyzed values required for other Safety Culture categories and reached out to the Safety Culture team for additional input.
Deployed the Ignio workflow to Production, which is now running smoothly.
Added checkpointing logic for Silver analytics, reducing the failure rate. Confirmed it’s functioning well in Dev. Connected with the MLOps engineer to demonstrate this and to gain access for operations in QA.
Conducted analysis on the weather station API and performed minor tests.
Worked on port utilization data, completed all initial requirements, and provided access to the Data Science team in QA Silver Catalog for data verification.
Addressed missing Eniram tag listings on the new API and am developing a notebook to dynamically call the respective Silver tables.

---

## Update 12

**Date:** 2025-08-22
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** Unidentified

### Summarized Update

Next Week's Focus
Complete the remaining Eniram work. Implement enhancements on the MIAP API for improved performance.

### Raw Update

Next Week's Focus
Complete the remaining Eniram work.
Implement enhancements on the MIAP API for improved performance.

---

## Update 13

**Date:** 2025-08-22
**Business Area:** MIAP
**Business Project:** Asset Management Expansion
**People:** [[mahshad_shariatnasab/overview_mahshad_shariatnasab|Mahshad Shariatnasab]]

### Summarized Update

Updated service power and hotel baseline. Worked on the deviation for CS and had a meeting with the HVAC engineering team to discuss it. The engineering team has contacted the ship regarding multiple sensor and energy management issues; we are still awaiting their response.

### Raw Update

Updated service power and hotel baseline.
Worked on the deviation for CS and had a meeting with the HVAC engineering team to discuss it. The engineering team has contacted the ship regarding multiple sensor and energy management issues; we are still awaiting their response.
Investigated deviations in SC and EG machinery and consulted with the engineering team to identify the issues.
Addressed the WN deviation in public spaces for AHUs and sent a report with my comments on the source of the deviation, which is about 120 kW.
Worked on the SI deviation in AHUs, approximately 100 kW, and sent an email regarding the AHU units showing abnormalities.
Found deviations in IC (200 kW) and AT (100 kW) and am still investigating the causes.
Updated the OFB model and added AD to it, resolving a previous issue.

---

## Update 14

**Date:** 2025-08-22
**Business Area:** MIAP
**Business Project:** HVAC Diagnostics & Anomaly Detection
**People:** [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]]

### Summarized Update

Implemented new logic for calculating deviation in power consumption and baselines for HVAC and Hotel areas. Both have been thoroughly tested and passed sanity checks. Next, the same updates will be applied to Service Power and Machinery, scheduled for tomorrow.

### Raw Update

Implemented new logic for calculating deviation in power consumption and baselines for HVAC and Hotel areas. Both have been thoroughly tested and passed sanity checks. Next, the same updates will be applied to Service Power and Machinery, scheduled for tomorrow.
Enhanced the anomaly detection class ANCHOR by adding an independent HP filter to support new plots in the GMO App.
Updated all plots in the GMO App affected by the revised deviation and baseline calculation logic across all areas.

---

## Update 15

**Date:** 2025-08-22
**Business Area:** MIAP
**Business Project:** Marine Safety Analytics
**People:** [[arya_cheeti/overview_arya_cheeti|Arya Cheeti]]

### Summarized Update

Successfully integrated Star of the Seas into both the MIAP analytics and the GMO web app.

### Raw Update

Successfully integrated Star of the Seas into both the MIAP analytics and the GMO web app.

---

## Update 16

**Date:** 2025-08-22
**Business Area:** MIAP
**Business Project:** Advanced Modeling Development
**People:** [[mehdi_assefi/overview_mehdi_assefi|Mehdi Assefi]]

### Summarized Update

Completed Dataset Preparation: Finalized the dataset using the SY scope menu data for the weight category prediction task (classification). Successfully trained and evaluated the model on this dataset. Enhanced Regression Modeling: Improved the regression model by segmenting the dataset based on target value ranges and developing separate models for each segment to better handle data imbalance.

### Raw Update

Completed Dataset Preparation: Finalized the dataset using the SY scope menu data for the weight category prediction task (classification). Successfully trained and evaluated the model on this dataset.
Enhanced Regression Modeling: Improved the regression model by segmenting the dataset based on target value ranges and developing separate models for each segment to better handle data imbalance.
Prediction Dataset Preparation: Extracted and aligned prediction data from the SY scope menu with the training dataset to ensure consistency and accuracy in model inference.
Stakeholder Engagement: Met with stakeholders to present model results and gathered valuable feedback and insights for further refinement.
Ongoing Work: Currently working on integrating the separate regression models into a unified framework to streamline predictions across the full target range.

---

## Update 17

**Date:** 2025-08-22
**Business Area:** MIAP
**Business Project:** Advanced Modeling Development
**People:** Unidentified

### Summarized Update

Fuel Forecasting: Fixed data issues blocking individual modeling on NV, OY, EX, and UT and completed data tag mapping for new MFMs on QN class. Added Diesel Engine FAT Data for ST to our database. Continuing to work on fixing data issues blocking power plant model development for other ships in the fleet.

### Raw Update

Fuel Forecasting: Fixed data issues blocking individual modeling on NV, OY, EX, and UT and completed data tag mapping for new MFMs on QN class.
Added Diesel Engine FAT Data for ST to our database.
Continuing to work on fixing data issues blocking power plant model development for other ships in the fleet.

---

## Update 18

**Date:** 2025-08-22
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

Added comprehensive logging to the MIAP Fuel Forecast API library. Created a Databricks notebook for validating Fuel Forecast API total propulsion power predictions. Provided MLOps support to team members, including:
Helping the Data Engineer with troubleshooting API requests, performance tuning, etc.

### Raw Update

Added comprehensive logging to the MIAP Fuel Forecast API library.
Created a Databricks notebook for validating Fuel Forecast API total propulsion power predictions.
Provided MLOps support to team members, including:
Helping the Data Engineer with troubleshooting API requests, performance tuning, etc.
Assisting the Data Science Analyst with REST API environment setup, debugging, and deployment processes.
Completed and executed test cases for Fuel Forecast API; remediated all bugs identified during test execution.
Made improvements to Fuel Forecast API:
Caching of drydock data and ALS utilization data to improve performance.
Added hull degradation rate as an optional parameter.
Added option to force base model usage.
Enhanced ALS utilization lookup to find the most recent non-null quarter usage for each ship.

---

## Update 19

**Date:** 2025-08-22
**Business Area:** Medallia
**Business Project:** Division-Level Medallia Reports
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

- Met with Steering leadership to present last month worth of project updates and to receive feedback. Also addressed two key data quality concerns which were identified as (A) Data Engineering specific (B) Misunderstanding of how we are aggregating data. - Met with key stakeholders (Alessio & Melissa) to discuss next steps on RCI emails.

### Raw Update

- Met with Steering leadership to present last month worth of project updates and to receive feedback. Also addressed two key data quality concerns which were identified as (A) Data Engineering specific (B) Misunderstanding of how we are aggregating data.
- Met with key stakeholders (Alessio & Melissa) to discuss next steps on RCI emails. Will be focusing on create a shipboard division specific report (i.e. Housekeeping, Guest Services, Entertainment, etc.)
- Prepared heatmaps for key Figgis presentation (aggregate multi-sailing data, 2025-08-22).
- Introduced new PRELIMINARY Medallia report to be sent out 4-days post return date designed specifically for shipboard staff.
- Extended the AI Data Extraction process to include SilverSeas.
- Several updates to Guest Logs pipeline which is actively backfilling data for 2025 (improved Context Engineering and replaced multithreaded API calls with async API calls).

---

## Update 20

**Date:** 2025-08-22
**Business Area:** MyCruise Recommender
**Business Project:** Enhanced For You Recommendations
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

- Add-to-cart AB test will complete Thursday 8/28. Early indications show 20% (web) 50% (app) click through rate for recommended products and 2% incremental revenue. - Once AB test for add-to-cart is complete the add-to-cart feature will be turned off.

### Raw Update

- Add-to-cart AB test will complete Thursday 8/28. Early indications show 20% (web) 50% (app) click through rate for recommended products and 2% incremental revenue.
- Once AB test for add-to-cart is complete the add-to-cart feature will be turned off. If results continue to show revenue lift after testing period - the integration of recommendations will be harded on the website (as long as staffing permits).
- PLP AB test will soon follow next.
- Discussions around Calendar and Daily Planner recommendations will start 8/22.

---

## Update 21

**Date:** 2025-08-22
**Business Area:** Unclassified
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[gaurav_godawat/overview_gaurav_godawat|Gaurav Godawat]]

### Summarized Update

### Digital App Analysis
- Refining app analysis queries and journey dataset logic to focus on category-specific actions. - Understanding category mix of first purchases. - Enhanced analysis and curation for first-purchase category findings.

### Raw Update

### Digital App Analysis
- Refining app analysis queries and journey dataset logic to focus on category-specific actions.
- Understanding category mix of first purchases.
- Enhanced analysis and curation for first-purchase category findings.
- Updated journey datasets (filtering, joining logic) for more accurate precruise spend signals.
- Resolved duplicate session issue when journeys cross calendar days (2025-08-21).

---

## Update 22

**Date:** 2025-08-22
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

- Ongoing monitoring of CTI model performance – conversion, category accuracy, ongoing reporting. - Concerned: Results still show lackluster conversion performance. Teams are evaluating why conversion is so poor relative to performance compared against 2020-2024 model.

### Raw Update

- Ongoing monitoring of CTI model performance – conversion, category accuracy, ongoing reporting.
- Concerned: Results still show lackluster conversion performance. Teams are evaluating why conversion is so poor relative to performance compared against 2020-2024 model.

---

## Update 23

**Date:** 2025-08-22
**Business Area:** Unclassified
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

### Ad-hoc
- New request by SilverSeas to deliver one-time topic classification of service request emails. Topic classifications will be used to create optimal SNOW ticket templates.

### Raw Update

### Ad-hoc
- New request by SilverSeas to deliver one-time topic classification of service request emails. Topic classifications will be used to create optimal SNOW ticket templates.

---

## Update 24

**Date:** 2025-08-22
**Business Area:** CEL Revenue Management
**Business Project:** Inventory Automation (FIT Reberthing & GROUPS Processes)
**People:** Unidentified

### Summarized Update

•Status: This ticket is complete as of 08/20/2025
•Coordinated with data engineering for refresh of ICGTLD table to remove duplicates caused by whitespace being added to Celebrity’s single-character categories W, X, Y and Z. •Duplicate identification and prevention code added to Celebrity automation to allow processes to complete successfully if duplicates ever are reintroduced in the data.

### Raw Update

•Status: This ticket is complete as of 08/20/2025
•Coordinated with data engineering for refresh of ICGTLD table to remove duplicates caused by whitespace being added to Celebrity’s single-character categories W, X, Y and Z.
•Duplicate identification and prevention code added to Celebrity automation to allow processes to complete successfully if duplicates ever are reintroduced in the data.

---

## Update 25

**Date:** 2025-08-22
**Business Area:** CEL Revenue Management
**Business Project:** ADA-Accessible Berthing Migration
**People:** Unidentified

### Summarized Update

•Status: This ticket is complete as of 08/20/2025
•Celebrity FIT Re-berthing in production. Weekly run scheduled for Sundays at 2pm.

### Raw Update

•Status: This ticket is complete as of 08/20/2025
•Celebrity FIT Re-berthing in production. Weekly run scheduled for Sundays at 2pm.

---

## Update 26

**Date:** 2025-08-22
**Business Area:** CEL Revenue Management
**Business Project:** Inventory Automation (FIT Reberthing & GROUPS Processes)
**People:** Unidentified

### Summarized Update

•Status: This ticket is complete as of 08/07/2025
•Celebrity guarantee group replenishment in production with daily run occurring at 7:15am daily.

### Raw Update

•Status: This ticket is complete as of 08/07/2025
•Celebrity guarantee group replenishment in production with daily run occurring at 7:15am daily.

---

## Update 27

**Date:** 2025-08-22
**Business Area:** RCI Revenue Management
**Business Project:** Automation Upgrades
**People:** Unidentified

### Summarized Update

•Australia price upload separation deployed successfully into production. Run on 8/19/25 processed Australia price recs as designed.

### Raw Update

•Australia price upload separation deployed successfully into production. Run on 8/19/25 processed Australia price recs as designed.

---

## Update 28

**Date:** 2025-08-22
**Business Area:** CEL Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model 3.0
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

•Met with business 8/19/25. Shared analysis of example actual sailing performance versus predicted (prices, booking shares, demand). Currently conducting further back testing on all 2.0 and 3.0 models.

### Raw Update

•Met with business 8/19/25. Shared analysis of example actual sailing performance versus predicted (prices, booking shares, demand). Currently conducting further back testing on all 2.0 and 3.0 models. Will meet with CEL team again later this week to hear their feedback on results.
•Testing more granular wts bins for 3.0 optimization. CEL team likes 5 wk bins for result table to see track at that level. Also exploring using booked position to build dynamic wts bins.
•Increased training data to include sailing over 50 weeks out now that gty’s have been open further out and there is sufficient data.
•Completed analysis on historical gty-lead, lower-above, upper-deluxe gaps. Bounded optimization to reasonable range for each tier.
•Backtesting all 2.0 and 3.0 models.

---

## Update 29

**Date:** 2025-08-22
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)
**People:** Unidentified

### Summarized Update

•Backtesting all 2.0 and 3.0 models.

### Raw Update

•Backtesting all 2.0 and 3.0 models.

---

## Update 30

**Date:** 2025-08-22
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

•Booking waves were initially created based on the booking week of year (WOY). However, since sailings can span multiple years, a specific WOY might represent a wave in one year but not in another. To address this inconsistency, a stakeholder suggested two possible improvements:
•Base the booking wave on the WTS (Wave Time Series) instead of WOY.

### Raw Update

•Booking waves were initially created based on the booking week of year (WOY). However, since sailings can span multiple years, a specific WOY might represent a wave in one year but not in another. To address this inconsistency, a stakeholder suggested two possible improvements:
•Base the booking wave on the WTS (Wave Time Series) instead of WOY.
•Include both the year and the booking WOY to distinguish waves across years.
•Work on implementing one of these solutions is planned for the remainder of this week or next week.

---

## Update 31

**Date:** 2025-08-22
**Business Area:** Unclassified
**People:** [[srilekha_reddy_madupu/overview_srilekha_reddy_madupu|Srilekha Reddy Madupu]]

### Summarized Update

CEL | TESTING | Testing New set of features on CEL Elasticity model, Backtesting Framework
•Status: Completed as of August 21, 2025. •Deliverables:
•Developed a comprehensive PowerPoint presentation for the Biweekly RMA team meeting to showcase progress on the backtesting framework. •Presented the business use case, emphasizing the problems addressed and the value added to analytics.

### Raw Update

CEL | TESTING | Testing New set of features on CEL Elasticity model, Backtesting Framework
•Status: Completed as of August 21, 2025.
•Deliverables:
•Developed a comprehensive PowerPoint presentation for the Biweekly RMA team meeting to showcase progress on the backtesting framework.
•Presented the business use case, emphasizing the problems addressed and the value added to analytics.
•Defined the framework’s scope, key functionalities, and its alignment with broader organizational initiatives.
•Explained the limitations of traditional cross-validation for time series data and justified the use of time series cross-validation.
•Demonstrated the framework’s workflow, including data flow, model training/testing, and result generation.
•Incorporated feedback on the codebase to enhance efficiency, modularity, and adaptability.
•Outlined the high-level delivery process, including milestones, testing phases, and system integration points.
•Clarified the project timeline and outlined next steps for deployment and ongoing support.

---

## Update 32

**Date:** 2025-08-22
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

•Weekly Updates: (08/14/2025 - 08/20/2025)
•Changing Data Sources: Changed the data source to capture bookings from vcap_extreme to vcap_daily_snapshot. Additionally, I used feature stores table just as a backup to calculating the bookings for the analysis. •Iterating for different methods to read in the track:
•Applied multiple methodologies, weighted, blended weighted, look forward weighted look forward, blended WTD etc with different weights that would help us get the lowest error possible.

### Raw Update

•Weekly Updates: (08/14/2025 - 08/20/2025)
•Changing Data Sources: Changed the data source to capture bookings from vcap_extreme to vcap_daily_snapshot. Additionally, I used feature stores table just as a backup to calculating the bookings for the analysis.
•Iterating for different methods to read in the track:
•Applied multiple methodologies, weighted, blended weighted, look forward weighted look forward, blended WTD etc with different weights that would help us get the lowest error possible.
•Developed an analysis at a cat_class, meta_product, peak/off peak season to see what methodology gives us the lowest error possible
•Deliverable: Developed a presentation to present both the business teams at Royal and CEL. (link)
•Next Steps: (Need to create a new ticket)
•Based on the feedback from the business, I need to prorate the WTD track and calculate the error metrics again
•Incorporate all the occupancies for the track instead of just double

---

## Update 33

**Date:** 2025-08-22
**Business Area:** RCI Revenue Management
**Business Project:** DART Logic Integration
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

Recreating the VPS Pricing Dataset at a Category-Level using VCAP is crucial for delivering updated pricing elasticities models that account for active promotions. We do not have enough data for the historical VPS Pricing Data. •New VPS Dataset Finalized and Validated
•A refined VPS dataset was created and validated with key stakeholders, incorporating pricing and discount logic.

### Raw Update

Recreating the VPS Pricing Dataset at a Category-Level using VCAP is crucial for delivering updated pricing elasticities models that account for active promotions. We do not have enough data for the historical VPS Pricing Data.
•New VPS Dataset Finalized and Validated
•A refined VPS dataset was created and validated with key stakeholders, incorporating pricing and discount logic. The dataset is stored under dev_revenue_mgmt_bu.feature_stores.ship_sdt_catclass_wtsbin_aggs_v4 and is ready for integration into analytical workflows.
•Enhanced Price Calculation Logic for Demand Analysis
•VPS prices were calculated using a conditional formula based on promotion type, incorporating base fare, port tax, and occupancy-specific discounts. The minimum VPS price per ship, sailing date, read date, and category class was extracted to assess demand sensitivity to low-price availability.
•Integrated Pricing and Booking Data for Insight Generation
•Booking data was aggregated using the new_bk_bkg field from the occupancy table and joined with VPS pricing data. This alignment enables analysis of how pricing influences booking behavior across different sailings and category classes.

---

## Update 34

**Date:** 2025-08-22
**Business Area:** PCP Pricing Automation
**Business Project:** Automated Pricing Expansion
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

RCI | Productionize the Automated Hybris Promo Uploads
•the SharePoint was created in order to streamline the automated promo uploads from OBR team strategy (independent of the PRE)
•a PRE-driven automation of promo uploads was coded. testing was started for this which highlighted some bugs that the digital team identified and needed to fix

### Raw Update

RCI | Productionize the Automated Hybris Promo Uploads
•the SharePoint was created in order to streamline the automated promo uploads from OBR team strategy (independent of the PRE)
•a PRE-driven automation of promo uploads was coded. testing was started for this which highlighted some bugs that the digital team identified and needed to fix

---

## Update 35

**Date:** 2025-08-22
**Business Area:** PCP Pricing Automation
**Business Project:** Automated Pricing Expansion
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

• Automated promo uploads from OBR team strategy (independent of the PRE) was also coded in a very robust & dynamic manner. this has not been tested yet, but is expected to be tested after the bugs with the PRE-driven automation are fixed by the other team
•Conversations were had with both brands (RCI + CEL) to determine some of the useful business rules that can be used to implement some cross joins on the PRE-driven promo uploads. this would result in things such as additional X% off for loyalty members, casino members, or pax of certain cabin classes.

### Raw Update

• Automated promo uploads from OBR team strategy (independent of the PRE) was also coded in a very robust & dynamic manner. this has not been tested yet, but is expected to be tested after the bugs with the PRE-driven automation are fixed by the other team
•Conversations were had with both brands (RCI + CEL) to determine some of the useful business rules that can be used to implement some cross joins on the PRE-driven promo uploads. this would result in things such as additional X% off for loyalty members, casino members, or pax of certain cabin classes. this has not been coded yet, but the business knowledge/rules were learned in order to code this upgraded version of the PRE-drive promo upload automation

---

## Update 36

**Date:** 2025-08-22
**Business Area:** Loyalty
**Business Project:** Co-Brand Credit Card Pilot
**People:** [[kartik_ullal/overview_kartik_ullal|Kartik Ullal]], [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

•Status: This ticket is complete as of 08/21/2025
•Deliverables:
•Created a matched design consumer list for the choice benefits loyalty pilot. Matched them based on demographic data and propensity scores for booking a cruise. Sent the data to the data engineering and ecommerce team so they could work on it for the test.

### Raw Update

•Status: This ticket is complete as of 08/21/2025
•Deliverables:
•Created a matched design consumer list for the choice benefits loyalty pilot. Matched them based on demographic data and propensity scores for booking a cruise. Sent the data to the data engineering and ecommerce team so they could work on it for the test.
However, choice benefit pilot will likely be delayed because data engineering is struggling migrating data from alpha to SFMC
Create Consumer List for Celebrity High Value and Low value menus for both brands
•Updated new consumer list by fixing filters and cross checking each brand and loyalty tier ranks are matching.
Find base acquisition rates for CC and conduct power analysis
•Calculated acquisition rates for inactive guests, specifically targeting credit card holders who haven’t sailed in the past three years.
•Cross-checked metrics and validated filters to ensure accuracy and relevance of the analysis.
•Aligned data sources and logic to support strategic insights into reactivation opportunities for dormant consumers.

---

_Source: 20250822 - Weekly Rafeh & Matt Updates (Raw).docx_