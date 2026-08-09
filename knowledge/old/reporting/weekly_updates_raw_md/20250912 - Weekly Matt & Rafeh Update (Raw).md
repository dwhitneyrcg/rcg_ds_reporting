---
tags:
  - aagam_shah
  - arya_cheeti
  - atefeh_mahdavi
  - ayon_ghosh
  - brendan_turpin
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/revenue_management_automation_(ssc)
  - business_area/supply_chain_optimization
  - business_area/win-on-waste_(hotel_operations)
  - camila_aichele
  - erick_alfaro
  - gaurav_godawat
  - ignacio_villasmil
  - jesse_bausell
  - kartik_ullal
  - kevin_diaz
  - lamis_amer
  - mahshad_shariatnasab
  - mehdi_assefi
  - michelle_manfrini
  - parimala_kettymuthu
  - project/advanced_modeling_development
  - project/category_gapping_optimization_3.0
  - project/choice_benefits_pilot
  - project/cococay_integration_and_guardrails
  - project/fare_code_unbundling
  - project/forecasting_pipeline_expansion
  - project/gty-lead_fare_optimization_model
  - project/historical_data_integration
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/marine_safety_analytics
  - project/miap_operating_efficiency_enhancements
  - project/miap_phase_iv_development
  - project/nps_drivers_analysis_for_alert_system
  - project/perfect_day_product_pricing
  - project/pre_4.0_elasticity_enhancements
  - project/spi-guided_track_optimization
  - project/spi_scoring_upgrades
  - raw
  - reza_bahadori
  - srilekha_reddy_madupu
  - weekly_update
date: "2025-09-12"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2025-09-12

## Update 1

**Date:** 2025-09-12
**Business Area:** Win-on-Waste
**Business Project:** Forecasting Pipeline Expansion
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

Provided extensive support to all 26 ships during FPMS rollout. Implemented multiple hotfixes in MDR across all modeling utilities to correct forecast inaccuracies, addressing both inflated and low item forecasts by centering predictions around average consumption while accounting for real and random patterns in historical data. Applied code optimizations in key modules to reduce processing time and improve pipeline efficiency.

### Raw Update

Provided extensive support to all 26 ships during FPMS rollout.
Implemented multiple hotfixes in MDR across all modeling utilities to correct forecast inaccuracies, addressing both inflated and low item forecasts by centering predictions around average consumption while accounting for real and random patterns in historical data.
Applied code optimizations in key modules to reduce processing time and improve pipeline efficiency.
Conducted technical briefings with chefs to demonstrate how geographic location data was leveraged to enhance forecast

---

## Update 2

**Date:** 2025-09-12
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** Unidentified

### Summarized Update

Context: The following work was motivated by a failure this week in production, where Lead Prioritization failed on Tuesday and was down 9 hours due to the job being run on a Data Scientist’s work cluster and a perfect storm that the user account was temporarily disabled due to a Data Scientist’s international travel and near a restricted zone (Nigeria). Alignment: No production jobs on personal compute; all production compute must use Databricks Job Clusters managed by a Service Principal. Access: Glen-Erik is provisioning Databricks Service Principal access; ADF pipelines already use Service Principal via Managed Service Identity.

### Raw Update

Context: The following work was motivated by a failure this week in production, where Lead Prioritization failed on Tuesday and was down 9 hours due to the job being run on a Data Scientist’s work cluster and a perfect storm that the user account was temporarily disabled due to a Data Scientist’s international travel and near a restricted zone (Nigeria).
Alignment: No production jobs on personal compute; all production compute must use Databricks Job Clusters managed by a Service Principal.
Access: Glen-Erik is provisioning Databricks Service Principal access; ADF pipelines already use Service Principal via Managed Service Identity.
Version control: Follow-up scheduled with Glen-Erik to adopt Databricks Asset Bundles for pipeline change management.
Adoption: All team members are either on Job Clusters or actively migrating.
Update: Supply Chain ADF Job Cluster test failed due to Unity Catalog access to dev_datascience; working with Glen-Erik to resolve.
Next: Parameterize table read/write code with environment variables to enable promotion to prod without code edits.
Ben & Camila
Supply Chain / IBP
Completed:
Delivered spend regions to Yan (derive country from first two letters of city code; map to region via pycountry-convert).
RCI/CEL order creation: corrected inbound orders and consumption calculations to reflect actual quantities needed.
Added CocoCay to HF&B reports; results will flow when Ben runs the pipeline.

---

## Update 3

**Date:** 2025-09-12
**Business Area:** Supply Chain
**Business Project:** CocoCay Integration and Guardrails
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Cihan
PCP Pricing Automation (Onboard Revenue)
Completed:
Demand model feature identification; feature store updated with WTS bins specific to waterpark demand. Waterpark repeater analysis for Royal Product:
Finding: ~14% of waterpark guests are repeaters, stable over time. Context: No evidence of a decline in repeater participation post-Hideaway Beach opening.

### Raw Update

Cihan
PCP Pricing Automation (Onboard Revenue)
Completed:
Demand model feature identification; feature store updated with WTS bins specific to waterpark demand.
Waterpark repeater analysis for Royal Product:
Finding: ~14% of waterpark guests are repeaters, stable over time.
Context: No evidence of a decline in repeater participation post-Hideaway Beach opening.
Cihan
PCP Pricing Automation (Onboard Revenue)
In progress:
Elasticity model for Water Park: feature engineering and data preparation.
Next:
Schedule and conduct brainstorming with Dave and Kevin on elasticity approach.
Build and validate the elasticity model based on workshop outcomes.
Cihan
Digital App (Community One)
Completed:
Classifier model deployed to production.
Developed ai_classify_rcg() advanced classification agent:
Supports user-selected models (e.g., OpenAI).
Accepts topic descriptions.
Constrains outputs to provided labels and mitigates hallucinations.
Adoption: Digital team is using the agent for ad hoc topic classification.
Next:
Meet with Jaime’s team to share the notebook and ensure maintainability.
Begin Qualtrics survey work with Jaime’s team.
Cihan
Digital App (Community One) — Guest Services Chatbot
Completed:
Validated metrics presented by Eunha to Star HD.
Next:
Add Star to the average chatbot adoption-rate visualization.
Update dashboard color scheme to align with Royal Caribbean brand.
Carlos
E-Commerce Customer Targeting
Completed:
Resolved Genie permissions error.
Expanded Databricks Consumer Dashboard (more decile options; optimized refresh rate).
Upgraded Databricks runtime 13.3 → 16.4 for reporting; resolved SHAP library conflicts (0.41.0 → 0.46.0).
Created and shared MLflow model management snippets.
Carlos
E-Commerce Customer Targeting
In progress:
Cost optimization of train/predict pipelines (route ingestion/reporting to lower-cost clusters).
Update production pipelines to comply with new Job Cluster policy.
Next:
Meet with e-commerce data science to integrate itinerary recommender into marketing models and plan the consumer transition-cause study.
Ben & Caleb
Customer Lifetime Value (CLV)
Completed:
Normalized value vs. LTR and sentiment analysis:
Within-category z-scoring of VALUE_INDEX_CABIN by CABIN_CATEGORY_CODE to create NORM_VALUE_CABIN.
LTR bucketing (Promoter 9–10; Passive 7–8; Detractor else).
Topic explosion; limited to top 50 topics.
Uplift (Promoter − Detractor) on NORM_VALUE_CABIN with n≥1,000 per class; Welch’s t-tests for top positives (p=0.27–0.68; not significant).
Pearson correlations between SENTIMENT_SCORE and NORM_VALUE_CABIN with n≥1,000; r≈0 to 0.051 (negligible).
Interpretation: Effect sizes are very small; topic sentiment is not a meaningful predictor of normalized cabin value at the topic–experience level. CASINO shows consistent negative uplift (detractors higher normalized value) and merits separate validation.
Prepared C-suite deck for Celebrity (Mon 9/15) focusing on 2–3 high-performing cohorts, including behaviors, summary stats (product/shorex preferences, DMA, NPS drivers, seasonality, value index), and associated marketing targeting strategies.
Ben & Caleb
Customer Lifetime Value (CLV)
In progress:
Combine Oracle and Alpha Databricks systems using Marimo notebooks; enhance connections; deepen understanding of casino flag, cabin linking, OBR categories.
Adjust logic inconsistencies for RCI cruise experience, casino cabin transfer, and casino flagging.
Develop automated checks for PAX, PCDs, and NTR.
Mirielle
Contact Center Lead Prioritization
Completed/In progress:
BKTOCX outbound lead scoring: Resolved ~7-hour production block by migrating compute off a personal account (with Eswar).
OFTOCX: Feature engineering for Royal and Celebrity is progressing.
Workforce Planning: Implementing save/edit functionality in the Streamlit app to persist user inputs and modified results.
Ben & Carlos
Customer Targeting (Journey Orchestration)
Completed:
Held calls with Salesforce regarding Journey Orchestration for guests; Ben also met with Salesforce individually on 9/11.
In progress:
Pending call with Braze.
Salesforce to schedule a follow-up call in two weeks with one of their contact center experts to explore leveraging their AI solutions (e.g., AgentForce) in the Contact Center.
Next:
Attend Salesforce follow-up; assess fit and integration considerations.
Proceed with Braze discussion once scheduled.

---

## Update 4

**Date:** 2025-09-12
**Business Area:** Loyalty
**Business Project:** Choice Benefits Pilot
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]], [[kartik_ullal/overview_kartik_ullal|Kartik Ullal]]

### Summarized Update

Kartik presented initial findings on choice benefits to the Steerco. Early signs point to a lift in bookings for the treatment groups, but it is still too early to determine statistical significance. SteerCo has decided to test both CC spend and CC acquisition for the next pilot, although the data will not support a statistically significant test on acquisition due to low historic acquisition rates.

### Raw Update

Kartik presented initial findings on choice benefits to the Steerco. Early signs point to a lift in bookings for the treatment groups, but it is still too early to determine statistical significance. SteerCo has decided to test both CC spend and CC acquisition for the next pilot, although the data will not support a statistically significant test on acquisition due to low historic acquisition rates. POS data is still in UAT testing with the business. CEL UAT is progressing and close to completion. Will be following up with RCI today. The tier simulator is in progress of refactoring. This week the inputs to the simulator have been adjusted to reflect data corrections discovered during pilot testing. The next step on the simulator is configuring the tier calculator to use tier progression from the existing program, rather than the proposed spend based program.

---

## Update 5

**Date:** 2025-09-12
**Business Area:** PCP Pricing Automation
**Business Project:** Perfect Day Product Pricing
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]], [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

We are still facing challenges getting promotion/pricing uploads tested in hybris lower environments. DS teams have built the data to digital requirements, but data is falling off. The working hypothesis is that there is an error in the Kafka transmission.

### Raw Update

We are still facing challenges getting promotion/pricing uploads tested in hybris lower environments. DS teams have built the data to digital requirements, but data is falling off. The working hypothesis is that there is an error in the Kafka transmission. Ignacio is working closely with digital and DE teams to resolve this quickly. In the meantime, he is also working closely with the business teams to make mass promotions simpler from a UX perspective. This week we met with Alex Correa to discuss Alaska ShoreX products. Cihan will be starting with a labeling and clustering exercise to simplify the data and draw initial insights. I will be presenting a shoreX playbook for discussion with the business in next week's alignment meeting. This playbook will center on business unlocks including bundling, SKU rationalization, pricing strategies accounting for substitutable demand with baskets, customer economics and targeting among others.

---

## Update 6

**Date:** 2025-09-12
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

Erick
Axiom - Medallia Reporting Automation
- Last week the team introduced the new Preliminary email report for both the ship/shoreside audience. Since then there have been 10+ users that have been added to the distribution including (Jay Schneider, Ed Artiles, and other VP/Directors). - Up until now the Medallia meta data extraction process has only processed survey responses greater than 100 characters.

### Raw Update

Erick
Axiom - Medallia Reporting Automation
- Last week the team introduced the new Preliminary email report for both the ship/shoreside audience. Since then there have been 10+ users that have been added to the distribution including (Jay Schneider, Ed Artiles, and other VP/Directors). 
- Up until now the Medallia meta data extraction process has only processed survey responses greater than 100 characters. This week we started processing shorter responses (actively backfilling data, once complete will include in the reporting pipelines). 
- Received greenlight from Evan on new email format for Celebrity to highlight top 5 newly trending negative topics. This report is pending a few tweaks. Evan wants the a draft copy of the report early next week to see what August would have looked like. This report will be sent once a month.

---

## Update 7

**Date:** 2025-09-12
**Business Area:** Medallia
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[gaurav_godawat/overview_gaurav_godawat|Gaurav Godawat]]

### Summarized Update

Erick and Christian
PCP Product Recommendations 
- Several new initiatives are being explored including productionizing all parts of the existing recommender pipeline, implementing a Lakebase backend in prepartion of real time data updates, working on logic to implement product weighting based on business rules, and planning discussion on recommendations for non revenue products for the calendar.

### Raw Update

Erick and Christian
PCP Product Recommendations 
- Several new initiatives are being explored including productionizing all parts of the existing recommender pipeline, implementing a Lakebase backend in prepartion of real time data updates, working on logic to implement product weighting based on business rules, and planning discussion on recommendations for non revenue products for the calendar.

---

## Update 8

**Date:** 2025-09-12
**Business Area:** MIAP
**Business Project:** Advanced Modeling Development
**People:** [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]]

### Summarized Update

Deployed new workflows for Hotel and HVAC in production, resulting in runtime reduction to approximately one-third to one-half of the previous duration. Implemented new logic for deviation and expected power calculations in HVAC and Hotel areas. Completed development of parallel pipeline for Machinery area and successfully tested it in QA; deployment to production is planned next.

### Raw Update

Deployed new workflows for Hotel and HVAC in production, resulting in runtime reduction to approximately one-third to one-half of the previous duration.
Implemented new logic for deviation and expected power calculations in HVAC and Hotel areas.
Completed development of parallel pipeline for Machinery area and successfully tested it in QA; deployment to production is planned next.
Initiated automatic baseline definition for hull performance as requested by Nicola.

---

## Update 9

**Date:** 2025-09-12
**Business Area:** MIAP
**Business Project:** Advanced Modeling Development
**People:** [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

Created report of MIAP models and versions across all catalogs in Databricks
Created presentation on DynaTorch, our in-house built Dynamic Modeling framework, for bi-weekly sync with Dave
Attended mentorship circle meeting
Created script to delete models versions older than 30 days to prevent our Databricks account from going over the maximum limit of model versions; deleted around ~20k unnecessary model versions
Troubleshot multi-faceted issue with access to the MIAP REST API in GMO Prod
Resolved access issue with the Crosser job in Databricks; made changes to asset bundle to prevent this job from being executed in QA
Provided support to various members of the MIAP team, assisting with merge conflicts, mismatches between environments, code reviews, etc.

### Raw Update

Created report of MIAP models and versions across all catalogs in Databricks
Created presentation on DynaTorch, our in-house built Dynamic Modeling framework, for bi-weekly sync with Dave
Attended mentorship circle meeting
Created script to delete models versions older than 30 days to prevent our Databricks account from going over the maximum limit of model versions; deleted around ~20k unnecessary model versions
Troubleshot multi-faceted issue with access to the MIAP REST API in GMO Prod
Resolved access issue with the Crosser job in Databricks; made changes to asset bundle to prevent this job from being executed in QA
Provided support to various members of the MIAP team, assisting with merge conflicts, mismatches between environments, code reviews, etc.

---

## Update 10

**Date:** 2025-09-12
**Business Area:** MIAP
**Business Project:** Advanced Modeling Development
**People:** Unidentified

### Summarized Update

Implemented stg model configuration in power plant
Testing implementation of STG models
Working on fix to outlier removal method causing issues in STG models. Current outlier removal method removes too many values not leaving enough for modeling
Documenting issues with both STG and GTG models

### Raw Update

Implemented stg model configuration in power plant
Testing implementation of STG models
Working on fix to outlier removal method causing issues in STG models. Current outlier removal method removes too many values not leaving enough for modeling
Documenting issues with both STG and GTG models

---

## Update 11

**Date:** 2025-09-12
**Business Area:** MIAP
**Business Project:** Marine Safety Analytics
**People:** [[arya_cheeti/overview_arya_cheeti|Arya Cheeti]]

### Summarized Update

Reconfigured chiller analytics features and results to be able to handle null value cases to prevent divide by zero errors
Found a period in explorers data of null values and configured analytics to work alongside this
Added explorer of the seas to all the analytics config files, tested and pushed to prd
Worked on improving the accuracy of work order classifier
Fixed data saving bugs with fire incident classifier
Built graphs in GMO app for safety incidents
Replaced all analytics folders with new model search code
Added fire_safety_incidents in azure data storage

### Raw Update

Reconfigured chiller analytics features and results to be able to handle null value cases to prevent divide by zero errors
Found a period in explorers data of null values and configured analytics to work alongside this
Added explorer of the seas to all the analytics config files, tested and pushed to prd
Worked on improving the accuracy of work order classifier
Fixed data saving bugs with fire incident classifier
Built graphs in GMO app for safety incidents
Replaced all analytics folders with new model search code
Added fire_safety_incidents in azure data storage

---

## Update 12

**Date:** 2025-09-12
**Business Area:** MIAP
**Business Project:** MIAP Phase IV Development
**People:** Unidentified

### Summarized Update

This Week -
Worked on the new Silver Eniram notebook, tested it in the development environment, and collaborated with the MLOps engineer to resolve blockers in QA. Addressed the fix for the MIAP API, which was causing data delivery issues for all vendors. Granted permissions to the Wärtsilä team for accessing the MIAP API.

### Raw Update

This Week -
Worked on the new Silver Eniram notebook, tested it in the development environment, and collaborated with the MLOps engineer to resolve blockers in QA.
Addressed the fix for the MIAP API, which was causing data delivery issues for all vendors.
Granted permissions to the Wärtsilä team for accessing the MIAP API.
Discussed all recent implementations for the MIAP API and Silver Analytics Notebook, including the addition of checkpointing mechanisms to enhance reliability.
Investigated issues with the Eniram API, which is not functioning as expected from the server side. Tested various scenarios and reached out to the Eniram team for assistance.
Next Week's Focus-
Resolve the ongoing Eniram API issues.
Move the new Silver Eniram notebook to QA and verify if all dashboards are populating correctly.
Fix issues identified in the QA environment, deploy updates to the MIAP API and Silver Analytics notebooks, and conduct thorough testing in QA.

---

## Update 13

**Date:** 2025-09-12
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[mehdi_assefi/overview_mehdi_assefi|Mehdi Assefi]]

### Summarized Update

Fully integrated the regressor with the AI Agent for Symphony Revamp Analysiss. Managed to extract features from vector search tool, mapped the "space", "items", "material", and "location" features to consistent clusters with the regressor. applied consistent encoder to the clusters, and made the regressor work properly with the resulted input.

### Raw Update

Fully integrated the regressor with the AI Agent for Symphony Revamp Analysiss.
Managed to extract features from vector search tool, mapped the "space", "items", "material", and "location" features to consistent clusters with the regressor. applied consistent encoder to the clusters, and made the regressor work properly with the resulted input.
I am working to run tests to compare the results and also making further improvements on the predictions.

---

## Update 14

**Date:** 2025-09-12
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** [[mahshad_shariatnasab/overview_mahshad_shariatnasab|Mahshad Shariatnasab]]

### Summarized Update

Worked on a grid optimization problem to find the best itinerary for ships and ports based on various constraints. Implemented the solution in Python and conducted testing. Created plots for ventilation fans on all ships to help identify anomalies in machinery.

### Raw Update

Worked on a grid optimization problem to find the best itinerary for ships and ports based on various constraints. Implemented the solution in Python and conducted testing.
Created plots for ventilation fans on all ships to help identify anomalies in machinery.
Assisted a teammate in troubleshooting their code and data issues in the table.

---

## Update 15

**Date:** 2025-09-12
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]], [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Made continued progress to integration of elasticity 4.0, correcting the price change calculation to properly account for linear model outputs and point elasticities.

### Raw Update

Made continued progress to integration of elasticity 4.0, correcting the price change calculation to properly account for linear model outputs and point elasticities.

---

## Update 16

**Date:** 2025-09-12
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]], [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Track Optimization:
Applied a version of DART to elasticity 4.0 for volume forecasts. However, further work is required to fully integrate DART in elasticities. The new demand model is being used for track optimization and track shapes are closely matching business generated tracks, but there are necessary improvements to the pricing recommendations including accounting for residual errors.

### Raw Update

Track Optimization:
Applied a version of DART to elasticity 4.0 for volume forecasts. However, further work is required to fully integrate DART in elasticities. The new demand model is being used for track optimization and track shapes are closely matching business generated tracks, but there are necessary improvements to the pricing recommendations including accounting for residual errors.

---

## Update 17

**Date:** 2025-09-12
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]], [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Updated the analysis by using the following: 4.0 model for elasticities for RCI, using all occupancies for both CEL and RCI, using the WTD expectations for the analysis, and analyzing the booking window where we beat or miss track consistently

### Raw Update

Updated the analysis by using the following: 4.0 model for elasticities for RCI, using all occupancies for both CEL and RCI, using the WTD expectations for the analysis, and analyzing the booking window where we beat or miss track consistently

---

## Update 18

**Date:** 2025-09-12
**Business Area:** RCI Revenue Management
**Business Project:** SPI-guided Track Optimization
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Initial EDA results are continuing to be shared with business teams. The current focus is on analyzing cancellations by WTS with respect to booking time. Using SPI outputs we are analyzing track recommendations by meta and quarter vs current track and how we built in 24 and 25.

### Raw Update

Initial EDA results are continuing to be shared with business teams. The current focus is on analyzing cancellations by WTS with respect to booking time. Using SPI outputs we are analyzing track recommendations by meta and quarter vs current track and how we built in 24 and 25.

---

## Update 19

**Date:** 2025-09-12
**Business Area:** RCI Revenue Management
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

Sent over results for the entire fleet to Eddie for review last week. Met with Alexa on Tuesday, still awaiting feedback.

### Raw Update

Sent over results for the entire fleet to Eddie for review last week. Met with Alexa on Tuesday, still awaiting feedback.

---

## Update 20

**Date:** 2025-09-12
**Business Area:** CEL Revenue Management
**Business Project:** SPI Scoring Upgrades
**People:** [[srilekha_reddy_madupu/overview_srilekha_reddy_madupu|Srilekha Reddy Madupu]]

### Summarized Update

Developed a more sensitive way to build WTS bins so that bins can be more precise during the prime booking window. This was a requirement from the business as they thought the spline based windows were too large and not capturing true price demand relationships, since pricing could be updated many times in the old windows. Kevin
CEL Revenue Management: SPI:
Actively investigating over-normalization of SPI scoring model.

### Raw Update

Developed a more sensitive way to build WTS bins so that bins can be more precise during the prime booking window. This was a requirement from the business as they thought the spline based windows were too large and not capturing true price demand relationships, since pricing could be updated many times in the old windows.
Kevin
CEL Revenue Management: SPI:
Actively investigating over-normalization of SPI scoring model.

---

## Update 21

**Date:** 2025-09-12
**Business Area:** CEL Revenue Management
**Business Project:** Category Gapping Optimization 3.0
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

Presented to the three product teams and all managers aligned on implementation. 3.0 will use all occupancies and net availability. Europe manager requested an additional view of a Med vs North sailing.

### Raw Update

Presented to the three product teams and all managers aligned on implementation. 3.0 will use all occupancies and net availability. Europe manager requested an additional view of a Med vs North sailing. Caribbean manager requested a comparison of a 6 vs 8 night sailing.

---

## Update 22

**Date:** 2025-09-12
**Business Area:** CEL Revenue Management
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

Sent MTRB baskets to Tristan for review, everything looked good except some new deployments weren’t picked up due to issues in the ICLSMD table. As a workaround, we’ll manually update the deployment table in DB with each new deployment. Waiting on Tristan to upload the table so I can run the analysis.

### Raw Update

Sent MTRB baskets to Tristan for review, everything looked good except some new deployments weren’t picked up due to issues in the ICLSMD table. As a workaround, we’ll manually update the deployment table in DB with each new deployment. Waiting on Tristan to upload the table so I can run the analysis. Plan to push to PRD next week. This will create static baskets while proposing changes to the baskets based on new data.

---

## Update 23

**Date:** 2025-09-12
**Business Area:** SSC Revenue Management
**Business Project:** Fare Code Unbundling
**People:** [[jesse_bausell/overview_jesse_bausell|Jesse Bausell]]

### Summarized Update

Considerable code refactoring to make the pipeline more robust and stable. Added configurations for different modeling algorithms based on sailing segments. The pipeline now fully accounts for new fare codes to ensure stability after cutover

### Raw Update

Considerable code refactoring to make the pipeline more robust and stable. Added configurations for different modeling algorithms based on sailing segments. The pipeline now fully accounts for new fare codes to ensure stability after cutover

---

_Source: 20250912 - Weekly Matt & Rafeh Update (Raw).docx_