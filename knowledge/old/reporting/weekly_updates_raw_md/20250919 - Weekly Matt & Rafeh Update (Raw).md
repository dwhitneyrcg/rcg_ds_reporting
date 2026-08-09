---
tags:
  - aagam_shah
  - alejandro_aristizabal-sanchez
  - atefeh_mahdavi
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/customer_targeting_(e-commerce)
  - business_area/hybris_product_recommendations_(digital)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/propel_targeted_offers_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/supply_chain_optimization
  - caleb_sharkey
  - camila_aichele
  - carlos_gonzalez_andarcio
  - cihan_ulus
  - erick_alfaro
  - gaurav_godawat
  - ignacio_villasmil
  - lamis_amer
  - mert_ersoz
  - michelle_manfrini
  - parimala_kettymuthu
  - project/automated_pricing_expansion
  - project/beverage_package_optimization
  - project/casino_spend_analysis
  - project/cococay_integration_and_guardrails
  - project/enhanced_negative_feedback_alerts
  - project/expansion_of_medallia_reporting
  - project/expedition_forecasting_with_silversea_automation
  - project/inventory_optimization_for_silversea
  - project/itinerary_recommender_development
  - project/lead_prioritization_-_bk2cx_(rci_&_cel)
  - project/nps-to-spend_modeling
  - project/nps_drivers_analysis_for_alert_system
  - project/offer_template_expansion
  - project/offer_to_cancel_(oftocx)_model_(rci_&_cel)
  - project/perfect_day_product_pricing
  - project/promotional_workflow_automation
  - project/segmentation_and_personalization_updates
  - project/spi-guided_track_optimization
  - raw
  - weekly_update
date: "2025-09-19"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2025-09-19

## Update 1

**Date:** 2025-09-19
**Business Area:** Supply Chain Optimization
**Business Project:** Inventory Optimization for Silversea
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

MIAP
Deployed new workflows for Machinery and Service Power in production, resulting in runtime reduction to approximately one-third to one-half of the previous duration. Implemented new logic for deviation and expected power calculations in Machinery and Service Power areas. Diagnosed and fixed the bugs in related plots in GMO app.

### Raw Update

MIAP
Deployed new workflows for Machinery and Service Power in production, resulting in runtime reduction to approximately one-third to one-half of the previous duration.
Implemented new logic for deviation and expected power calculations in Machinery and Service Power areas.
Diagnosed and fixed the bugs in related plots in GMO app.
Developing automatic baseline definition for propulsion and hull performance versus drydock per ship. The dataset has been created and proof of concept is underway. 

Brendan Turpin:
MIAP
Identified jobs with partial failures that are not sending email notifications: tested addition of new task for all pipelines that forces a failure notification in the case of "Success with Failure" in Databricks (e.g., if 3 ships fail in one step, we still want to process all subsequent steps for the succeeding ships, but still expect a failure overall at the end of the process so the support team can be notified).
Scheduled script to delete MIAP model versions older than 30 days in production; confirmed that we reduced the number of model versions in Databricks by 17.5% of the maximum capacity
Deployed and tested MIAP Databricks cost anomaly detection job in QA - encountered issue where SQL statement is unable to start and hangs indefinitely - working with Glen-Erik to open incident with Databricks support
Completed ALS Compressor Power Model and integrated into the Fuel Forecast API
Provided MLOps support to various team members

Will Borges:
MIAP
Completed Implementation of STG Models
Completed Implementation of GTG Models
Fixed issue with power plant results affecting 14 ships preventing Service power from being
correctly calculated and preventing data monitoring.


Arya Cheeti:
MIAP
worked on adding safety analytics to GMO app. 
Added graphs for fire, lopps and lsa events.
Found problems in work flow relating to sea events.
created gold safety analytics tables for all sea events and a table with all 3 events.

Ramu Sirusanagandla:
MIAP
This Week's Achievements:
Provided Meyer Turku with access to the requested list of tags.
Addressed changes in the Eniram API, which included new limitations set by the vendor.
Developed and implemented the necessary logic adjustments to handle these changes.
Completed testing to ensure data quality remains consistent.
Engaged with the Safety Culture team to discuss data quality issues, provided a demo on current data collection, collected feedback, and documented requirements.
Next week:
Move Silver Eniram notebook to the QA environment and performed testing to ensure proper functionality.
Move Safety Culture data to prod and deploy workflow as well.
Mehdi Assefi:
Worked to finalize embedding of the regression tool to the AI Agent.
Met with the new build team and discussed the results, also discussed the idea of the new project with the them.
Worked to prepare the test case showing the performance of the regression model comparing to the previous version which uses the vector search.
Started EDA on the new project using the sample data provided.

Mahshad Shariatnasab:
MIAP
Worked on IN anomaly with the Cda engineering team.
Worked on the grid optimization problem and created a data cleaning notebook; still facing some issues.
Handled missing data for AD, IC, and AT.
Investigated QN data issues related to service power.
Assisted a teammate in debugging code for GMP.
Helped a teammate set up an API.
Identified that the SY ventilation fan room setpoint can be adjusted to improve efficiency; currently exploring whether it is worth contacting the ship.

---

## Update 2

**Date:** 2025-09-19
**Business Area:** Customer Lifetime Value
**Business Project:** Casino Spend Analysis
**People:** [[caleb_sharkey/overview_caleb_sharkey|Caleb Sharkey]]

### Summarized Update

NPS-to-spend model: Built an OLS model to estimate impact of Likelihood to Recommend and sentiment on next-cruise spend (R² = 0.18). Observed non-intuitive negative coefficients on change in LTR in all segments except infrequent cruisers; indicates need for further feature/segment refinement. Casino customer validation: Identified flaws in casino-guest tagging logic (credited_meta_channel='casino' and casino_cabin_transfer>0 not aligned with source-of-truth flags).

### Raw Update

NPS-to-spend model: Built an OLS model to estimate impact of Likelihood to Recommend and sentiment on next-cruise spend (R² = 0.18). Observed non-intuitive negative coefficients on change in LTR in all segments except infrequent cruisers; indicates need for further feature/segment refinement.
Casino customer validation: Identified flaws in casino-guest tagging logic (credited_meta_channel='casino' and casino_cabin_transfer>0 not aligned with source-of-truth flags). After joining to “true casino” PAX IDs, found even lower spend and value index than previously measured. Meeting scheduled with Jordan and Austin to align on business logic and methodology.
Product journey analysis (CEL new-to-cruise): Developed comprehensive journey analysis; early insight suggests Alaska and Europe are stronger first products for long-term value. Addressing low sample sizes when slicing. Produced a stakeholder-ready deck (bar plots, heatmaps, network/venn visuals) for Jordan.
Data enablement: Secured Revenue Planning table access for cross-referenced cabins, enabling linkage of previously hidden group connections.

---

## Update 3

**Date:** 2025-09-19
**Business Area:** Customer Lifetime Value
**Business Project:** NPS-to-Spend Modeling
**People:** [[caleb_sharkey/overview_caleb_sharkey|Caleb Sharkey]]

### Summarized Update

Executive briefings: Present CLV use cases to CEL leadership (Michael and Laura) on 9/22 and 9/24, including targeted offers by persona, DMA, and wealth tiers. Data/model enhancements: Create new column for cabin cross-reference linkages; continue NPS–spend/value modeling to resolve coefficient directionality; adjust indirect cost logic to be RCI-experience specific. Quality automation: Stand up automated checks to validate PAX, PCD, and NTR counts.

### Raw Update

Executive briefings: Present CLV use cases to CEL leadership (Michael and Laura) on 9/22 and 9/24, including targeted offers by persona, DMA, and wealth tiers.
Data/model enhancements: Create new column for cabin cross-reference linkages; continue NPS–spend/value modeling to resolve coefficient directionality; adjust indirect cost logic to be RCI-experience specific.
Quality automation: Stand up automated checks to validate PAX, PCD, and NTR counts.

---

## Update 4

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Digital App Analysis
Guest Services Chatbot (Owner: Eunha Kim)
Pending UI enhancements: Add a “star” indicator to the average adoption-rate plot and update dashboard color scheme to Royal Caribbean brand guidelines.

### Raw Update

Digital App Analysis
Guest Services Chatbot (Owner: Eunha Kim)
Pending UI enhancements: Add a “star” indicator to the average adoption-rate plot and update dashboard color scheme to Royal Caribbean brand guidelines.

---

## Update 5

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Digital App Analysis
App Reviews (Owner: Jaime Stoelar)
Handover and research: Schedule share-out to transfer the notebook and ensure team maintainability; begin work on Qualtrics surveys with Jaime’s team.

### Raw Update

Digital App Analysis
App Reviews (Owner: Jaime Stoelar)
Handover and research: Schedule share-out to transfer the notebook and ensure team maintainability; begin work on Qualtrics surveys with Jaime’s team.

---

## Update 6

**Date:** 2025-09-19
**Business Area:** Customer Targeting
**Business Project:** Itinerary Recommender Development
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]]

### Summarized Update

Itinerary Recommender: Implementing feature engineering (pending EDA completion and full integration due to partial data availability). Search and analytics tooling: Reviewing Genie performance post internal model update and researching open-source alternative vanna.ai. Developer productivity: Exploring local Databricks development with VS Code dev_containers; configuring and testing cursor.ai.

### Raw Update

Itinerary Recommender: Implementing feature engineering (pending EDA completion and full integration due to partial data availability).
Search and analytics tooling: Reviewing Genie performance post internal model update and researching open-source alternative vanna.ai.
Developer productivity: Exploring local Databricks development with VS Code dev_containers; configuring and testing cursor.ai.

---

## Update 7

**Date:** 2025-09-19
**Business Area:** Supply Chain
**Business Project:** Expedition Forecasting with Silversea Automation
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

ADF pipeline productionization: Parameterized notebooks for dev/prod environments; testing in progress. With Glen-Erik’s support, established environment-variable patterns for portability. Unity Catalog/data access blocker: Temporarily reverted from Service Principal job clusters to interactive compute due to DE datasets not registered in Unity Catalog (some tables are file pointers).

### Raw Update

ADF pipeline productionization: Parameterized notebooks for dev/prod environments; testing in progress. With Glen-Erik’s support, established environment-variable patterns for portability.
Unity Catalog/data access blocker: Temporarily reverted from Service Principal job clusters to interactive compute due to DE datasets not registered in Unity Catalog (some tables are file pointers). DE committed on 9/18 to prioritize proper registration so we can return to Job Compute with Service Principal. Note: This remains a production vulnerability until resolved.

---

## Update 8

**Date:** 2025-09-19
**Business Area:** Supply Chain
**Business Project:** Expedition Forecasting with Silversea Automation
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Inventory planning (RCI/CEL): Calculated min/max PAR levels using average consumption (annual/monthly) and demand; filtered for next 6 months of future shipment dates. Inventory planning (SSC): Completed analogous min/max PAR calculation (using delivery_date). SSC order creation – actual quantity needed: Built a unified dataset joining shipboard inventory, PAR, inbound orders, and voyage demand; computes days-to-delivery, imputes gaps, and adjusts allocations to derive actual quantity needed.

### Raw Update

Inventory planning (RCI/CEL): Calculated min/max PAR levels using average consumption (annual/monthly) and demand; filtered for next 6 months of future shipment dates.
Inventory planning (SSC): Completed analogous min/max PAR calculation (using delivery_date).
SSC order creation – actual quantity needed: Built a unified dataset joining shipboard inventory, PAR, inbound orders, and voyage demand; computes days-to-delivery, imputes gaps, and adjusts allocations to derive actual quantity needed.
Uniforms forecasting:
Current models: Ship+Item; Ship+Item+Cost Center+Contract Length (days).
Newly created and monitoring: Ship+Modified Item (simple first-word grouping) and with Cost Center+Contract Length (days).
In development: Enhanced Modified Item grouping using multi-word normalization (e.g., “SHIRT 100% COTTON …” variants collapsed to “SHIRT 100% COTTON”), with and without Cost Center+Contract Length.
SSC inventory depletion: Replaced SharePoint Excel source with Yan’s table path due to stale updates; improved reliability.
Medical: Updated passenger count to include crew (guest+crew). Pipeline run starts tomorrow; accuracy to be assessed on run.
Finance automation: Building price-per-passenger metric from historical consumption and passenger counts to forecast future PPP using known future loads; refining final calculation method.
Pending
Add Silversea expedition items to Ben’s SSC pipeline.
Model reporting workflow: Add messages summarizing MdAPE over time, accuracy trends, and table paths for unpivoted demand and backtests per model.

---

## Update 9

**Date:** 2025-09-19
**Business Area:** PCP Pricing Automation
**Business Project:** Perfect Day Product Pricing
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Completed: Received cross-brand (CEL/RCI) product matching file; generated detailed product descriptions using OpenAI models; created paired product codes for cross-brand consistency; tested multiple prompt/model strategies to identify category/subcategory labels; labeled Alaska products. In Progress: Finalizing the most accurate OpenAI labeling approach after multi-model testing. Elasticity Modeling – Waterpark Project (Owners: Gang & Rafa)
Completed: Brainstormed with Kevin and Ignacio; incorporated agreed feature set; completed data cleaning and preprocessing for elasticity modeling.

### Raw Update

Completed: Received cross-brand (CEL/RCI) product matching file; generated detailed product descriptions using OpenAI models; created paired product codes for cross-brand consistency; tested multiple prompt/model strategies to identify category/subcategory labels; labeled Alaska products.
In Progress: Finalizing the most accurate OpenAI labeling approach after multi-model testing.
Elasticity Modeling – Waterpark Project (Owners: Gang & Rafa)
Completed: Brainstormed with Kevin and Ignacio; incorporated agreed feature set; completed data cleaning and preprocessing for elasticity modeling.
In Progress: Feature engineering to improve predictive accuracy and model performance.

---

## Update 10

**Date:** 2025-09-19
**Business Area:** Medallia
**Business Project:** Expansion of Medallia Reporting
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

Modified email graphics & plots to only show data for the most recent 5 sailings
Added additional disclaimers to Medallia email
Approval from CEL leadership to send fleet-wide emerging negative topic report once a month
Previously we were ignoring "short comments". We are now backfilling short
comments to include in the NPS reporting.

### Raw Update

Modified email graphics & plots to only show data for the most recent 5 sailings
Added additional disclaimers to Medallia email
Approval from CEL leadership to send fleet-wide emerging negative topic report once a month
Previously we were ignoring "short comments". We are now backfilling short
comments to include in the NPS reporting.

---

## Update 11

**Date:** 2025-09-19
**Business Area:** AXIOM
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

Initial evaluation of gpt-4o-mini models ability to summarize and label Guest Logs data is underwhelming. As a result we are upgrading the model to gpt-5-nano. We also need to perform a cleaning on the source data of the existing business topics/subtopics which are used in conjuction with the guest log itself to determine the resulting AI topics and entities.

### Raw Update

Initial evaluation of gpt-4o-mini models ability to summarize and label Guest Logs data is underwhelming.
As a result we are upgrading the model to gpt-5-nano.
We also need to perform a cleaning on the source data of the existing business topics/subtopics which are used in conjuction with the guest log itself to determine the resulting AI topics and entities.

---

## Update 12

**Date:** 2025-09-19
**Business Area:** MyCruise Recommender
**Business Project:** Segmentation and Personalization Updates
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

The eye brows recommendations went live last week. We've identified a silent bug in production which causes a large number of requests to fail. This is due to misalignment on product category descriptions that are available in the backend and what the frontend is requesting.

### Raw Update

The eye brows recommendations went live last week. We've identified a silent bug in production which causes a large number of requests to fail. This is due to misalignment on product category descriptions that are available in the backend and what the frontend is requesting. We are working on a mapping document to route frontend requests to the right backend fields.
ALS model retrained/deployed with new granular product categories
Segmentation clustering model registered (MLflow), segments applied in model retrain
Enable API tracing feature in databricks which allows us to track inputs to the API and track failures.

---

## Update 13

**Date:** 2025-09-19
**Business Area:** Contact Center
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

Conversions over the last 2 weeks are showing abnormally high conversion at the lowest deciles
We are introducing a wide range of new features to smooth out the conversions
We are working on an independent model for Celebrity

### Raw Update

Conversions over the last 2 weeks are showing abnormally high conversion at the lowest deciles
We are introducing a wide range of new features to smooth out the conversions
We are working on an independent model for Celebrity

---

## Update 14

**Date:** 2025-09-19
**Business Area:** AXIOM
**Business Project:** Enhanced Negative Feedback Alerts
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[gaurav_godawat/overview_gaurav_godawat|Gaurav Godawat]]

### Summarized Update

Completed:
Feature list updated per feedback (added/removed entries)
Hierarchical linear modeling implemented and tested
Regression output EDA (swarm/scatter plots)
Lasso regression rerun with updated data

### Raw Update

Completed:
Feature list updated per feedback (added/removed entries)
Hierarchical linear modeling implemented and tested
Regression output EDA (swarm/scatter plots)
Lasso regression rerun with updated data

---

## Update 15

**Date:** 2025-09-19
**Business Area:** AXIOM
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[gaurav_godawat/overview_gaurav_godawat|Gaurav Godawat]]

### Summarized Update

In Progress:
Advanced modeling approaches integrating numeric/topics/Ngrams
Dashboard upgrades: grouping features, correlation analyses
Extract/update latest data for analysis templates

### Raw Update

In Progress:
Advanced modeling approaches integrating numeric/topics/Ngrams
Dashboard upgrades: grouping features, correlation analyses
Extract/update latest data for analysis templates

---

## Update 16

**Date:** 2025-09-19
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** SPI-guided Track Optimization
**People:** Unidentified

### Summarized Update

Completed SPI track adjustments and currently working on FIT track target setting. Identified active notebooks list which are running in production via ADF, and also using featurestore tables. Transitioned feature store management to Data Engineering

### Raw Update

Completed SPI track adjustments and currently working on FIT track target setting.
Identified active notebooks list which are running in production via ADF, and also using featurestore tables.
Transitioned feature store management to Data Engineering

---

## Update 17

**Date:** 2025-09-19
**Business Area:** PROPEL
**Business Project:** Offer Template Expansion
**People:** [[alejandro_aristizabal-sanchez/overview_alejandro_aristizabal-sanchez|Alejandro Aristizabal-Sanchez]]

### Summarized Update

Calculation with real data of uplift at category level, including aggregation-based methods, confidence intervals, and regression with fixed effects and interactions. Results were shared with business stakeholders, and implementation is expected in the coming weeks. Initial development phase of additional offer templates, covering the first design sketches and adjustments to the current pipeline.

### Raw Update

Calculation with real data of uplift at category level, including aggregation-based methods, confidence intervals, and regression with fixed effects and interactions. Results were shared with business stakeholders, and implementation is expected in the coming weeks.
Initial development phase of additional offer templates, covering the first design sketches and adjustments to the current pipeline.

---

## Update 18

**Date:** 2025-09-19
**Business Area:** Supply Chain
**Business Project:** CocoCay Integration and Guardrails
**People:** Unidentified

### Summarized Update

Parameterized the datascience catalog (153 files with over 1500 changes). This parameterization process is now automated so future projects will be easier to do. Created an intermediate CICD to deploy prod to dev with some pre-work separation of dev and prod within dev.

### Raw Update

Parameterized the datascience catalog (153 files with over 1500 changes).  This parameterization process is now automated so future projects will be easier to do.
Created an intermediate CICD to deploy prod to dev with some pre-work separation of dev and prod within dev. And created the databricks cicd deployment to prod.
The biggest areas left to complete the separation is the shared ADF environment since it is used by many projects.
Other Data Science Projects:
Cleaning up Data Science dev workspace workflows, replacing them to job computes

---

## Update 19

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

RCI Rev Mgt: ADA Event Driven Berthing
3:28 PM – Started developing an automated reporting mechanism that will send daily status updates to a Teams channel. 3:26 PM – Met with Eddie to discuss workflow requirements for on-demand processing:
On-demand process should not include logging or reporting to avoid excessive reporting. The existing process will be updated to generate a single daily report summarizing berthing successes and failures.

### Raw Update

RCI Rev Mgt: ADA Event Driven Berthing
3:28 PM – Started developing an automated reporting mechanism that will send daily status updates to a Teams channel.
3:26 PM – Met with Eddie to discuss workflow requirements for on-demand processing:
On-demand process should not include logging or reporting to avoid excessive reporting.
The existing process will be updated to generate a single daily report summarizing berthing successes and failures.

---

## Update 20

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

CEL Rev Mgt: ADA ADF to Databricks
ADA-accessible berthing process has been successfully transitioned from Azure Data Factory (ADF) to Databricks, completing the migration effort. Live production testing confirmed stability and accuracy of the new Databricks implementation. Supporting infrastructure, including parameterized YAML configurations, has been prepared and submitted for ML Ops review.

### Raw Update

CEL Rev Mgt: ADA ADF to Databricks
ADA-accessible berthing process has been successfully transitioned from Azure Data Factory (ADF) to Databricks, completing the migration effort.
Live production testing confirmed stability and accuracy of the new Databricks implementation.
Supporting infrastructure, including parameterized YAML configurations, has been prepared and submitted for ML Ops review.
The Databricks job replicates the original ADF workflow, including wait logic, and has been validated in development without errors.
No delays or risks were reported; the initiative was completed on schedule and without issues.

---

## Update 21

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

CEL Rev Mgt | CAT-GAP 3.0
Fleet-Level Modeling Finalized: Completed fleet-wide results and a medical sailing example to compare RDSS groups. Additional analysis at ship-class and meta levels has also been delivered. Model Enhancements: Adjusted CAT-GAP 2.0 models to correct overpredictions in EG Australia and SL Asia.Expanded model inputs to include all occupancy levels for more accurate category-gapping.

### Raw Update

CEL Rev Mgt | CAT-GAP 3.0
Fleet-Level Modeling Finalized: Completed fleet-wide results and a medical sailing example to compare RDSS groups. Additional analysis at ship-class and meta levels has also been delivered.
Model Enhancements: Adjusted CAT-GAP 2.0 models to correct overpredictions in EG Australia and SL Asia.Expanded model inputs to include all occupancy levels for more accurate category-gapping.
Data & Prediction Updates: Models retrained using data through April 2025 to forecast future sailings.Booking data from April onward aggregated to evaluate performance (average price, tradeup, tier share).Residual analysis conducted to identify prediction gaps and areas needing adjustment.

---

## Update 22

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

RCI Rev Mgt | CAT-GAP 3.0
Stakeholder Engagement: RCI manager unavailable this week; follow-up scheduled for Tuesday.Alexa provided positive feedback on gap recommendations, which are within target range. Operational Adjustments: Sailing data recalibrated to reflect availability based on retention metrics

### Raw Update

RCI Rev Mgt | CAT-GAP 3.0
Stakeholder Engagement: RCI manager unavailable this week; follow-up scheduled for Tuesday.Alexa provided positive feedback on gap recommendations, which are within target range.
Operational Adjustments: Sailing data recalibrated to reflect availability based on retention metrics

---

## Update 23

**Date:** 2025-09-19
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - BK2CX (RCI & CEL)
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Tested multiple modeling approaches to improve pricing recommendations and track shapes. Found that using probability-of-demand (p(d)) models yields more realistic pricing. Integrated DART logic based on a 3-week moving average to smooth out unexplained price spikes at the sailing-category level.

### Raw Update

Tested multiple modeling approaches to improve pricing recommendations and track shapes. Found that using probability-of-demand (p(d)) models yields more realistic pricing.
Integrated DART logic based on a 3-week moving average to smooth out unexplained price spikes at the sailing-category level.
Revised optimization logic to compute prices using the p(d) model rather than elasticity-based calculations.
Prepared stakeholder presentation explaining why reliance on elasticities alone can lead to faulty pricing recommendations.
Running optimization on larger sample sets to identify edge cases and investigate infeasibility issues (e.g., null values in cumulative bookings).

---

## Update 24

**Date:** 2025-09-19
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

In Progress: Comparing optimal tracks against FIT-generated tracks for future sailings and SPI-based tracks for historical sailings. Quantifying revenue lift (or dip) from optimal tracks and investigating cases where business-generated tracks outperform due to constraints like booking bounds.

### Raw Update

In Progress: Comparing optimal tracks against FIT-generated tracks for future sailings and SPI-based tracks for historical sailings. Quantifying revenue lift (or dip) from optimal tracks and investigating cases where business-generated tracks outperform due to constraints like booking bounds.

---

## Update 25

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

RCI Rev Mgt: PRE 4.0:
Identified ~1,100 records where DART implementation led to negative price recommendations due to large residuals. In such cases, the original prediction is retained. Next Steps: Continue optimization validation, refine logic to handle edge cases, and finalize comparative revenue analysis.

### Raw Update

RCI Rev Mgt: PRE 4.0:
Identified ~1,100 records where DART implementation led to negative price recommendations due to large residuals. In such cases, the original prediction is retained.
Next Steps: Continue optimization validation, refine logic to handle edge cases, and finalize comparative revenue analysis.

---

## Update 26

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

CEL Rev Mgt | TESTING | Finalized Testing
Worked on creating a streamlined process to analyze and visualize feature importance from model backtesting results. Focused on extracting original, interpretable features by filtering out complex interaction and polynomial features. Developed aggregation methods to summarize feature importance by meta product code and cat_classes for clearer insights.

### Raw Update

CEL Rev Mgt | TESTING | Finalized Testing
Worked on creating a streamlined process to analyze and visualize feature importance from model backtesting results.
Focused on extracting original, interpretable features by filtering out complex interaction and polynomial features.
Developed aggregation methods to summarize feature importance by meta product code and cat_classes for clearer insights.
Created multiple visualization techniques including bar plots for top and low importance features, and heatmaps to show overall patterns.
Built summary reports to quickly identify key drivers and weak features within each category.
Enabled easy comparison across different product codes and categories to support informed, data-driven decisions.
Improved transparency and communication of model insights through simple, user-friendly charts and summaries.
Removed the features weekend_sailing_flag, holiday_flag, and peak_season_flag as they only capture broad, high-level patterns. Currently focusing on developing features that represent more granular data

---

## Update 27

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

RCI rev mgt: PRE
Finalized the stakeholder presentation for the Look Back / Look Forward analysis, incorporating Week-to-Date (WTD) expectations and occupancy data across both RCI and CEL. Used the RCI PRE 4.0 model to enable an apples-to-apples comparison with CEL. Conducted quality control checks to ensure data accuracy and consistency in the analysis.

### Raw Update

RCI rev mgt: PRE
Finalized the stakeholder presentation for the Look Back / Look Forward analysis, incorporating Week-to-Date (WTD) expectations and occupancy data across both RCI and CEL. Used the RCI PRE 4.0 model to enable an apples-to-apples comparison with CEL.
Conducted quality control checks to ensure data accuracy and consistency in the analysis.

---

## Update 28

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

RCI rev mgt: PRE
In Progress:
Elasticity Analysis (RCI | CEL): Initiated a cross-brand analysis to identify high- and low-demand periods using elasticity metrics. Collected elasticity data across sailings and began comparing similar sailings within baskets to isolate demand-driving factors. Next Steps: Finalize elasticity comparisons and document findings.

### Raw Update

RCI rev mgt: PRE
In Progress:
Elasticity Analysis (RCI | CEL): Initiated a cross-brand analysis to identify high- and low-demand periods using elasticity metrics. Collected elasticity data across sailings and began comparing similar sailings within baskets to isolate demand-driving factors.
Next Steps: Finalize elasticity comparisons and document findings.

---

## Update 29

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

RCI rev mgt: MTRB
MTRB Enhanced Updates (RCI): Blocked pending business validation of deployment logic; awaiting feedback from Tristan. Web Basket Analysis: Paused; replicating Celebrity’s basket analysis for RCI.

### Raw Update

RCI rev mgt: MTRB
MTRB Enhanced Updates (RCI): Blocked pending business validation of deployment logic; awaiting feedback from Tristan.
Web Basket Analysis: Paused; replicating Celebrity’s basket analysis for RCI.

---

## Update 30

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

CEL rev mgt: MTRB
Next Steps:
CEL MTRB Updates: Awaiting business approval on the method for calculating new deployments into the table. All other components are production-ready. Follow up with Tristan and business stakeholders to unblock deployment logic.

### Raw Update

CEL rev mgt: MTRB
Next Steps:
CEL MTRB Updates: Awaiting business approval on the method for calculating new deployments into the table. All other components are production-ready.
Follow up with Tristan and business stakeholders to unblock deployment logic.
Resume basket analysis once upstream dependencies are resolved.

---

## Update 31

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

RCI Rev Mgt: PRE4.0 Update
Completed:
Conducted a comparative analysis of the Celebrity and RCI pricing models, focusing on the impact of stabilizing constants in the price change equation. Key Findings:
In the RCI model, extreme values were significantly higher (43.62%) without stabilization. Even with a fixed norm, 14.51% of rows remained extreme.

### Raw Update

RCI Rev Mgt: PRE4.0 Update
Completed:
Conducted a comparative analysis of the Celebrity and RCI pricing models, focusing on the impact of stabilizing constants in the price change equation.
Key Findings:
In the RCI model, extreme values were significantly higher (43.62%) without stabilization. Even with a fixed norm, 14.51% of rows remained extreme.
Refined Approach:
Developed a variable norm strategy that dynamically adjusts the stabilizing constant per row based on the magnitude of the price change.
Introduced a weighted cap system to ensure smoother, bounded price adjustments across all rows.
This method prevents collapse of values near zero (a limitation of fixed norms) while maintaining control over volatility.

---

## Update 32

**Date:** 2025-09-19
**Business Area:** Unclassified
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

CEL Rev Mgt: PRE4.0 Update
Completed:
Conducted a comparative analysis of the Celebrity and RCI pricing models, focusing on the impact of stabilizing constants in the price change equation. Key Findings:
In the Celebrity model, applying a fixed norm reduced extreme price changes from 16.68% to 1.13% of rows. Refined Approach:
Developed a variable norm strategy that dynamically adjusts the stabilizing constant per row based on the magnitude of the price change.

### Raw Update

CEL Rev Mgt: PRE4.0 Update
Completed:
Conducted a comparative analysis of the Celebrity and RCI pricing models, focusing on the impact of stabilizing constants in the price change equation.
Key Findings:
In the Celebrity model, applying a fixed norm reduced extreme price changes from 16.68% to 1.13% of rows.
Refined Approach:
Developed a variable norm strategy that dynamically adjusts the stabilizing constant per row based on the magnitude of the price change.
Introduced a weighted cap system to ensure smoother, bounded price adjustments across all rows.
This method prevents collapse of values near zero (a limitation of fixed norms) while maintaining control over volatility.
Next Steps:
Integrate the variable norm strategy into production modeling workflows and validate its performance across brands.

---

## Update 33

**Date:** 2025-09-19
**Business Area:** PCP Pricing Automation
**Business Project:** Beverage Package Optimization
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

Implemented a buffer delay in the optimization routine to address intermittent data availability. This resolves a critical issue where optimization outputs for beverage packages were inconsistently missing due to table updates occurring during runtime.

### Raw Update

Implemented a buffer delay in the optimization routine to address intermittent data availability. This resolves a critical issue where optimization outputs for beverage packages were inconsistently missing due to table updates occurring during runtime.

---

## Update 34

**Date:** 2025-09-19
**Business Area:** PCP Pricing Automation
**Business Project:** Automated Pricing Expansion
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

Progress: Ignacio has successfully tested promotions in dev generated from the mass promotion tool. Digital is working through confirmation that all conditions provided are being applied. So far everything is looking good there.

### Raw Update

Progress: Ignacio has successfully tested promotions in dev generated from the mass promotion tool. Digital is working through confirmation that all conditions provided are being applied. So far everything is looking good there.
Next Steps: Test promos that match some of the live promos as opposed to dummy data. Gaby and Vic to create promos with the tool for UX testing.

---

## Update 35

**Date:** 2025-09-19
**Business Area:** PCP Pricing Automation
**Business Project:** Promotional Workflow Automation
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

Ignacio has also successfully extracted the existing promotions in hybris and formatted them to match the mass promotion setup. This will allow us to test promotions reflecting the way the team is currently using Hybris, while also providing additional visibility on live promos. Details:
PRE-driven cross-joined promotion uploads successfully tested in QA, integrating PRE outputs with granular business rules.

### Raw Update

Ignacio has also successfully extracted the existing promotions in hybris and formatted them to match the mass promotion setup. This will allow us to test promotions reflecting the way the team is currently using Hybris, while also providing additional visibility on live promos.
Details:
PRE-driven cross-joined promotion uploads successfully tested in QA, integrating PRE outputs with granular business rules.
SharePoint-driven promotion upload templates prepared for production, with locked fields and dropdowns to streamline OBR team input.
SharePoint-driven uploads undergoing testing in lower environments, with a focus on robustness and edge-case handling.
Extracted and reverse-engineered promotions from the Hybris system into a format compatible with SharePoint input, enabling OBR teams to reference and replicate existing promotions.
Next Steps: Continue testing with real-world inputs and finalize automation workflows for production deployment.

---

_Source: 20250919 - Weekly Matt & Rafeh Update (Raw).docx_