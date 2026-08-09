---
tags:
  - aagam_shah
  - atefeh_mahdavi
  - ayon_ghosh
  - bao_le
  - bernard_kai_wittmaack
  - brendan_turpin
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/hybris_product_recommendations_(digital)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/revenue_management_automation_(ssc)
  - business_area/royalone_community_(digital)
  - business_area/supply_chain_optimization
  - business_area/win-on-waste_(hotel_operations)
  - caleb_sharkey
  - camila_aichele
  - cihan_ulus
  - david_martinez
  - erick_alfaro
  - gaurav_godawat
  - glen-erik_cortez
  - ignacio_villasmil
  - jesse_bausell
  - kartik_ullal
  - kevin_diaz
  - lamis_amer
  - mehdi_assefi
  - mert_ersoz
  - michelle_manfrini
  - parimala_kettymuthu
  - project/a_b_testing_framework
  - project/cococay_integration_and_guardrails
  - project/elasticity_model_enhancements_(pre4.0)
  - project/enhanced_for_you_recommendations
  - project/expedition_forecasting_with_silversea_automation
  - project/fleetwide_energy_monitoring
  - project/forecasting_pipeline_expansion
  - project/gty-lead_fare_optimization_model
  - project/gty-lead_fare_optimization_model_3.0
  - project/historical_data_integration
  - project/hvac_diagnostics_&_anomaly_detection
  - project/inventory_automation_(fit_reberthing_&_groups_processes)
  - project/inventory_optimization_for_silversea
  - project/lead_prioritization_-_bk2cx_(rci_&_cel)
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/marine_safety_analytics
  - project/nps_drivers_analysis_for_alert_system
  - project/perfect_day_product_pricing
  - project/pre_4.0_elasticity_enhancements
  - project/purchase_behavior_and_timing_insights
  - project/spend-to-save_pilot_analysis
  - project/spi-guided_track_optimization
  - project/uniforms_model_enhancements
  - project/workforce_planning_tool
  - raw
  - reza_bahadori
  - weekly_update
date: "2025-08-08"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2025-08-08

## Update 1

**Date:** 2025-08-08
**Business Area:** AXIOM
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

**In Progress**
- Ongoing enhancements: UI improvements for large data selections, and expanded filtering (voyage, booking channels, demographics, venues, NPS, promos, etc). - Preparing to add support for smarter large-context models (gpt4o-mini, gpt4.1-nano) to enable deeper analytics.

### Raw Update

**In Progress**
- Ongoing enhancements: UI improvements for large data selections, and expanded filtering (voyage, booking channels, demographics, venues, NPS, promos, etc).
- Preparing to add support for smarter large-context models (gpt4o-mini, gpt4.1-nano) to enable deeper analytics.

---

## Update 2

**Date:** 2025-08-08
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

**Completed**
- Model retraining and reproducibility process: now ensures consistent results across development and production Azure ML environments when using identical compute configurations. - Automated threshold mapping function integrated into CTI workflow—thresholds for lead categories are now applied dynamically, reducing manual coordination with Siebel team. - Refined probability range assignments for Royal and Celebrity brands, based on latest model outputs.

### Raw Update

**Completed**
- Model retraining and reproducibility process: now ensures consistent results across development and production Azure ML environments when using identical compute configurations.
- Automated threshold mapping function integrated into CTI workflow—thresholds for lead categories are now applied dynamically, reducing manual coordination with Siebel team.
- Refined probability range assignments for Royal and Celebrity brands, based on latest model outputs.
- Streamlined deployment and operations—model training can now be triggered via manual notebooks (not only via automated jobs) and asset bundle dependencies/ML Ops interactions reduced.
- Modified lead/quote views to support new river cruise logic; lead recategorization feature for Celebrity inference data delivered (with automated value reclassification).
- All recent process improvements and model retrainings for asset bundle handling, reproducibility and production consistency validated and delivered.

---

## Update 3

**Date:** 2025-08-08
**Business Area:** AXIOM
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

**In Progress**
- Incorporating feedback from Consumer Insights (Hannah/Christina): shifting reporting to use standard deviations from mean for feature metrics, instead of NPS point increments. - Validating and mapping feature lists to ensure all key drivers (including business-prioritized "holy 12") are captured. - Ongoing: confirm groupings for highly correlated features, and ship-level vs.

### Raw Update

**In Progress**
- Incorporating feedback from Consumer Insights (Hannah/Christina): shifting reporting to use standard deviations from mean for feature metrics, instead of NPS point increments.
- Validating and mapping feature lists to ensure all key drivers (including business-prioritized "holy 12") are captured.
- Ongoing: confirm groupings for highly correlated features, and ship-level vs. aggregate driver modeling logic.
- Building frameworks to separate driver importance models (predicting "likelihood to recommend") from threshold regression models (quantifying NPS impact).

---

## Update 4

**Date:** 2025-08-08
**Business Area:** AXIOM
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

**Completed**
- Updated, delivered prototype dashboard for driver analysis using normalized feature sets (delta from average) with stakeholder feedback incorporated. - Documented combined feature set and outlined multi-model (stacked) driver analysis approach; planned next steps to refresh all ship-level data per latest business mapping.

### Raw Update

**Completed**
- Updated, delivered prototype dashboard for driver analysis using normalized feature sets (delta from average) with stakeholder feedback incorporated.
- Documented combined feature set and outlined multi-model (stacked) driver analysis approach; planned next steps to refresh all ship-level data per latest business mapping.

---

## Update 5

**Date:** 2025-08-08
**Business Area:** MyCruise Recommender
**Business Project:** Enhanced For You Recommendations
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

**Completed**
- Unit testing now in place for all models; unit test now blocks new model deployments if unit tests fail. - Created an optimized class to make OpenAI Azure GenAI calls at scale with retry logic and output schema validation. - Recommendations went live for Digital on Friday 8/1.

### Raw Update

**Completed**
- Unit testing now in place for all models; unit test now blocks new model deployments if unit tests fail.
- Created an optimized class to make OpenAI Azure GenAI calls at scale with retry logic and output schema validation.
- Recommendations went live for Digital on Friday 8/1. Recommendations were left running over the weekend on a small 5% of traffic. I believe they left add-to-cart and PLP over the weekend
- Endpoint that can serve 3k recommendations a second
- every recommender is using some combination of purchase history or clickstream interaction history with three broad categories of recommendations:
(a) naive: trending 30 days, trending 7 days, new products, etc
(b) association rules: customers who bought x also bought y
(c) for you: collaborative filtering with clustering

---

## Update 6

**Date:** 2025-08-08
**Business Area:** Medallia
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

**In Progress**
- Expanding comparative and filter capabilities (e.g., state-level NPS comparisons, nationality insights for non-US vessels, and RDSS cohorting). - Adding new attributes and groupings (families, age, loyalty, casino, spend) to reporting workflows. - SilverSeas brand data integration and fleet-level report rollouts for stakeholders (Laura, Gaby, Celebrity brand).

### Raw Update

**In Progress**
- Expanding comparative and filter capabilities (e.g., state-level NPS comparisons, nationality insights for non-US vessels, and RDSS cohorting).
- Adding new attributes and groupings (families, age, loyalty, casino, spend) to reporting workflows.
- SilverSeas brand data integration and fleet-level report rollouts for stakeholders (Laura, Gaby, Celebrity brand).
- Working on a PRELIMINARY report 4 days after sailing that would be sent to ship board for more immediate feedback loop.

---

## Update 7

**Date:** 2025-08-08
**Business Area:** AXIOM
**People:** [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]], [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

**In Progress**
- Received mapped acronyms from business. Need to integrate into existing AI extraction pipeline.

### Raw Update

**In Progress**
- Received mapped acronyms from business. Need to integrate into existing AI extraction pipeline.

---

## Update 8

**Date:** 2025-08-08
**Business Area:** RoyalOne Community
**Business Project:** Purchase Behavior and Timing Insights
**People:** [[gaurav_godawat/overview_gaurav_godawat|Gaurav Godawat]]

### Summarized Update

**In Progress**
- Analyses in progress: deep-dive on the correlation between app engagement journey (pages/sessions) and pre-cruise purchases, segmented by meta product, booking timing, and spend. - Ongoing: summarizing first purchase category insights and related revenue/PPT to share with stakeholders (for review/next steps).

### Raw Update

**In Progress**
- Analyses in progress: deep-dive on the correlation between app engagement journey (pages/sessions) and pre-cruise purchases, segmented by meta product, booking timing, and spend.
- Ongoing: summarizing first purchase category insights and related revenue/PPT to share with stakeholders (for review/next steps).

---

## Update 9

**Date:** 2025-08-08
**Business Area:** RoyalOne Community
**Business Project:** Purchase Behavior and Timing Insights
**People:** [[gaurav_godawat/overview_gaurav_godawat|Gaurav Godawat]]

### Summarized Update

**Completed**
- Delivered in-depth exploration/box plots showing the timing and sequencing of pre-cruise purchases by product type, including demographic and behavioral signals.

### Raw Update

**Completed**
- Delivered in-depth exploration/box plots showing the timing and sequencing of pre-cruise purchases by product type, including demographic and behavioral signals.

---

## Update 10

**Date:** 2025-08-08
**Business Area:** Win-on-Waste
**Business Project:** Forecasting Pipeline Expansion
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

1) developing MDR - V1 models and pipeline
2) Fixed missing pax count and meta product code issue (stemming from source files) in Q control - windjammer Pipeline
3) Monitoring and generating accuracy reports of 4 pipelines launched on 8/1 (last week)

### Raw Update

1) developing MDR - V1 models and pipeline
2) Fixed missing pax count and meta product code issue (stemming from source files) in Q control - windjammer Pipeline
3) Monitoring and generating accuracy reports of 4 pipelines launched on 8/1 (last week)

---

## Update 11

**Date:** 2025-08-08
**Business Area:** MIAP
**Business Project:** Marine Safety Analytics
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

Revamping the MIAP WebApp to mimic the same data visuals as the GMO App. (The GMO App auto-generates data visuals from the MIAP API based on a plot layout definition file.)
Presented SeaEvents GenAI data analysis to Marine Safety leadership, receiving very positive feedback. The Safety team has made significant requests from our team; however, lack of capital is concerning for these non-revenue-generating projects.

### Raw Update

Revamping the MIAP WebApp to mimic the same data visuals as the GMO App. (The GMO App auto-generates data visuals from the MIAP API based on a plot layout definition file.)
Presented SeaEvents GenAI data analysis to Marine Safety leadership, receiving very positive feedback. The Safety team has made significant requests from our team; however, lack of capital is concerning for these non-revenue-generating projects.
Improved the Stability ChatBot Agent with an enhanced agent definition and updated the model to Claude 4.0.
This stat must be highlighted in the summary: Revised MIAP savings fuel savings to date to $5.65M or $1.55M for 2025, after bug fixes and closing tickets on SmartSheet issue tracker. Added missing fuel savings from SM energy audit as well.

---

## Update 12

**Date:** 2025-08-08
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** [[mehdi_assefi/overview_mehdi_assefi|Mehdi Assefi]]

### Summarized Update

Finalized the Random Forest (RF) and XGBoost (XGB) regressors and evaluated their performance on stability data. Constructed a test dataset using data from the "SYScopeMenu" table and performed predictions with the trained models. Converted the continuous target variable into categorical classes to facilitate classification tasks.

### Raw Update

Finalized the Random Forest (RF) and XGBoost (XGB) regressors and evaluated their performance on stability data.
Constructed a test dataset using data from the "SYScopeMenu" table and performed predictions with the trained models.
Converted the continuous target variable into categorical classes to facilitate classification tasks.
Developed classifiers for datasets with 5, 10, 20, 30, and 50 classes, employing equal-sized binning strategies for each.
Conducted evaluations of the classifiers using precision, recall, F1-score, and confusion matrices. Additionally, performed regression-style assessments by calculating the average values within each bin.
Confusion matrices look promising but still need improvement, hopefully by using more training data.

---

## Update 13

**Date:** 2025-08-08
**Business Area:** MIAP
**Business Project:** HVAC Diagnostics & Anomaly Detection
**People:** [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]]

### Summarized Update

Identified saving opportunities using the AHU anomaly model for the following ships. Ships are being contacted with reports including lists of AHUs and possible reasons:
Summit: 42 kW - accepted by the HVAC engineer (~18k $)
Millennium: 72 kW - accepted by the HVAC engineer (~30k $)
Harmony: 35 kW - contacted the HVAC engineer (~15k $)
Beyond: 20 kW - contacted the HVAC engineer (~8k $)
Quantum: 24 kW - contacted the HVAC engineer (~10k $)
Total savings: 193 kW (~81k $) if all are approved. Will update status accordingly.

### Raw Update

Identified saving opportunities using the AHU anomaly model for the following ships. Ships are being contacted with reports including lists of AHUs and possible reasons:
Summit: 42 kW - accepted by the HVAC engineer (~18k $)
Millennium: 72 kW - accepted by the HVAC engineer (~30k $)
Harmony: 35 kW - contacted the HVAC engineer (~15k $)
Beyond: 20 kW - contacted the HVAC engineer (~8k $)
Quantum: 24 kW - contacted the HVAC engineer (~10k $)
Total savings: 193 kW (~81k $) if all are approved. Will update status accordingly.
Updated pump power calculations/models and baselines for the Millennium Class.

---

## Update 14

**Date:** 2025-08-08
**Business Area:** MIAP
**Business Project:** Fleetwide Energy Monitoring
**People:** Unidentified

### Summarized Update

SM is saving 25 kW, and ML is saving 70 kW. We contacted the ship, and they resolved the initial issue; however, the deviation for ML is still ongoing. We should reach out again to review the drop and identify the root cause.

### Raw Update

SM is saving 25 kW, and ML is saving 70 kW. We contacted the ship, and they resolved the initial issue; however, the deviation for ML is still ongoing. We should reach out again to review the drop and identify the root cause.
Prepared a presentation covering ML, SM, IN, and AD to discuss with the engineering team. The goal is to pinpoint issues and explore further energy-saving opportunities.
For AD, there is a saving potential of 300 kW, and for IN, 220 kW. We held a meeting with HVAC engineers to investigate root causes. For IN, chilled water temperature setpoints appear problematic; for AD, the issue likely lies in the sequence control of the chillers.
Worked on adding ventilation fan ratio plots to the GMO dashboard. Encountered some access issues but successfully resolved and debugged them.
Worked on data issues for the ML class involving temperature data from the Eniram API and Valmet API. Also debugged problems for the GMO web.

---

## Update 15

**Date:** 2025-08-08
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** Unidentified

### Summarized Update

This week:
Worked on the MIAP ETL process, implementing intermediate result storage in a table to enable Spark to roll back and recompute in case of errors. Explored broadcast joins and repartitioning techniques for Silver Analytics, though further investigation is needed to optimize these processes. Updated data types and formats in Ignio for JDE, AMOS, and Crunchtime data.

### Raw Update

This week:
Worked on the MIAP ETL process, implementing intermediate result storage in a table to enable Spark to roll back and recompute in case of errors.
Explored broadcast joins and repartitioning techniques for Silver Analytics, though further investigation is needed to optimize these processes.
Updated data types and formats in Ignio for JDE, AMOS, and Crunchtime data. The Ignio team is currently receiving data daily.
Progressed on Safety Culture data for the Data Feeds category, which includes 22 endpoints. Working to retrieve data up to the Bronze level and have reached out to the team for additional inputs on incremental loading.
Eniram incremental and historical workflows are scheduled and running smoothly in QA.
Next week:
Need to move Eniram incremental to production.
Need to work on Safety Culture silver table data loading.

---

## Update 16

**Date:** 2025-08-08
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** Unidentified

### Summarized Update

Fixed data issues with VFR tags in ML/RD class. Implemented ADTK regression outlier removal in the overall model. Implemented CurveFit model as the base model for both individual and overall power plant models.

### Raw Update

Fixed data issues with VFR tags in ML/RD class.
Implemented ADTK regression outlier removal in the overall model.
Implemented CurveFit model as the base model for both individual and overall power plant models.
Testing new regressor outlier removal and CurveFit model in QA.

---

## Update 17

**Date:** 2025-08-08
**Business Area:** MIAP
**Business Project:** Marine Safety Analytics
**People:** [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

Removed email notifications for job failures in the MIAP QA environment. Changed all jobs in the MIAP QA environment to run weekly instead of daily. Refactored Fuel Forecast API code to improve reusability and define standards; 80% complete with reusable framework.

### Raw Update

Removed email notifications for job failures in the MIAP QA environment.
Changed all jobs in the MIAP QA environment to run weekly instead of daily.
Refactored Fuel Forecast API code to improve reusability and define standards; 80% complete with reusable framework.
Completed templatizing the model split functionality for reusability in models across ship areas for the Fuel Forecast API.
Reduced concurrency and increased worker cluster size in MIAP Machinery Analytics workflow to fix workflow failures caused by driver out-of-memory errors.
Cross-trained Maritime Safety developer on the new MIAP production deployment process and development best practices.
Helped Data Scientist troubleshoot MIAP API local development environment issues.
Met with the CAP support team to discuss expectations and establish a better communication and feedback loop.

---

## Update 18

**Date:** 2025-08-08
**Business Area:** Supply Chain Optimization
**Business Project:** Expedition Forecasting with Silversea Automation
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Next Steps
Complete Guardrails testing and obtain final sign-off for the new ship automation
Finalize uniforms feature engineering and apply results to all model versions
Complete Yan reviews for Silversea expeditions and inventory variance
Progress feature engineering rollout for next-generation demand models toward production readiness

### Raw Update

Next Steps
Complete Guardrails testing and obtain final sign-off for the new ship automation
Finalize uniforms feature engineering and apply results to all model versions
Complete Yan reviews for Silversea expeditions and inventory variance
Progress feature engineering rollout for next-generation demand models toward production readiness

---

## Update 19

**Date:** 2025-08-08
**Business Area:** Supply Chain Optimization
**Business Project:** Expedition Forecasting with Silversea Automation
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Expedition items for Silversea
Status: Delivered; awaiting review from Yan
Notes / Risk & Mitigation: Yan review timing could delay acceptance. Mitigation: align review schedule with Yan and secure quick sign-off; monitor review SLAs.

### Raw Update

Expedition items for Silversea
Status: Delivered; awaiting review from Yan
Notes / Risk & Mitigation: Yan review timing could delay acceptance. Mitigation: align review schedule with Yan and secure quick sign-off; monitor review SLAs.

---

## Update 20

**Date:** 2025-08-08
**Business Area:** Supply Chain Optimization
**Business Project:** Inventory Optimization for Silversea
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Silversea Unhealthy Inventory Variance
Status: Delivered; awaiting review from Yan
Notes / Risk & Mitigation: Yan review timing could delay remediation. Mitigation: coordinate review dates and escalate if delays arise.

### Raw Update

Silversea Unhealthy Inventory Variance
Status: Delivered; awaiting review from Yan
Notes / Risk & Mitigation: Yan review timing could delay remediation. Mitigation: coordinate review dates and escalate if delays arise.

---

## Update 21

**Date:** 2025-08-08
**Business Area:** Supply Chain Optimization
**Business Project:** Uniforms Model Enhancements
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Uniforms model cleaning
Status: In progress
Description: Working on the probatus section to evaluate more features and grouping columns by crew to identify the most predictive features; plan to apply these findings across all versions of the uniforms model
Next steps: Finalize feature set and propagate improvements across all versions
Notes / Risk & Mitigation: Additional feature selection and grouping work may extend timelines. Mitigation: lock a minimal viable feature set quickly and push improvements across all versions once features are confirmed.

### Raw Update

Uniforms model cleaning
Status: In progress
Description: Working on the probatus section to evaluate more features and grouping columns by crew to identify the most predictive features; plan to apply these findings across all versions of the uniforms model
Next steps: Finalize feature set and propagate improvements across all versions
Notes / Risk & Mitigation: Additional feature selection and grouping work may extend timelines. Mitigation: lock a minimal viable feature set quickly and push improvements across all versions once features are confirmed.

---

## Update 22

**Date:** 2025-08-08
**Business Area:** Supply Chain Optimization
**Business Project:** CocoCay Integration and Guardrails
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

New ship automation
Status: In progress
Description: Integrated the new ship code into ETL, Demand, and Guardrails for Ben’s HF&B model
Progress: ETL and Demand tests passed with no errors; Guardrails testing is halfway complete; Final review in progress
Next steps: Complete Guardrails testing and obtain final sign-off
Notes / Risk & Mitigation: Guardrails progress may impact the overall timeline. Mitigation: prioritize remaining guardrails test cases and align with stakeholders to secure timely final review.

### Raw Update

New ship automation
Status: In progress
Description: Integrated the new ship code into ETL, Demand, and Guardrails for Ben’s HF&B model
Progress: ETL and Demand tests passed with no errors; Guardrails testing is halfway complete; Final review in progress
Next steps: Complete Guardrails testing and obtain final sign-off
Notes / Risk & Mitigation: Guardrails progress may impact the overall timeline. Mitigation: prioritize remaining guardrails test cases and align with stakeholders to secure timely final review.

---

## Update 23

**Date:** 2025-08-08
**Business Area:** Supply Chain Optimization
**Business Project:** CocoCay Integration and Guardrails
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Brand substitutions
Status: In progress
Description: Updated the brand mapping in the Guardrails code
Next steps: Final review and sign-off
Notes / Risk & Mitigation: Final sign-off could face delays. Mitigation: escalate to owners for a firm sign-off date and communicate blockers early.

### Raw Update

Brand substitutions
Status: In progress
Description: Updated the brand mapping in the Guardrails code
Next steps: Final review and sign-off
Notes / Risk & Mitigation: Final sign-off could face delays. Mitigation: escalate to owners for a firm sign-off date and communicate blockers early.

---

## Update 24

**Date:** 2025-08-08
**Business Area:** Supply Chain Optimization
**Business Project:** CocoCay Integration and Guardrails
**People:** Unidentified

### Summarized Update

Feature Engineering for next-generation demand models (RCI/CCI) with Cursor Agentic AI
Status: In progress
Completed features:
Rolling Autocorrelation: TSFresh-style lag correlations for seasonality detection
Fourier Approximation: Trigonometric correlations for periodic pattern recognition
Change Point Detection: Variance ratio analysis for structural breaks
Trend Analysis: Rolling regression slopes for demand trajectory
Peak Detection: Rolling peak counting for consumption spikes
Complexity Analysis: Differences patterns for demand irregularity
Ship Class Learning: Cross-ship intelligence within the ship class and pattern recognition
Next steps:
Bayesian Ensemble: Multi-model ensemble with model evidence computation (Random Forest, GBT, Linear Regression, Decision Tree)
Cross-Validation: 5-fold CV for model evidence estimation
Uncertainty Quantification: Bayesian Model Averaging with credible confidence intervals
Model Evidence: Marginal likelihood computation
Posterior Weights: Automated model selection based on evidence
Complexity Penalties: Automatic Occam factor for model selection
SHAP Integration: Ready for explainability
Production Implementation: Scaling and performance readiness
Notes / Risk & Mitigation: Productionization and integration complexity introduce risk to on-time rollout. Mitigation: implement robust cross-validation (5-fold), model explainability (SHAP), and plan for phased production rollout with performance monitoring and rollback options.

### Raw Update

Feature Engineering for next-generation demand models (RCI/CCI) with Cursor Agentic AI
Status: In progress
Completed features:
Rolling Autocorrelation: TSFresh-style lag correlations for seasonality detection
Fourier Approximation: Trigonometric correlations for periodic pattern recognition
Change Point Detection: Variance ratio analysis for structural breaks
Trend Analysis: Rolling regression slopes for demand trajectory
Peak Detection: Rolling peak counting for consumption spikes
Complexity Analysis: Differences patterns for demand irregularity
Ship Class Learning: Cross-ship intelligence within the ship class and pattern recognition
Next steps:
Bayesian Ensemble: Multi-model ensemble with model evidence computation (Random Forest, GBT, Linear Regression, Decision Tree)
Cross-Validation: 5-fold CV for model evidence estimation
Uncertainty Quantification: Bayesian Model Averaging with credible confidence intervals
Model Evidence: Marginal likelihood computation
Posterior Weights: Automated model selection based on evidence
Complexity Penalties: Automatic Occam factor for model selection
SHAP Integration: Ready for explainability
Production Implementation: Scaling and performance readiness
Notes / Risk & Mitigation: Productionization and integration complexity introduce risk to on-time rollout. Mitigation: implement robust cross-validation (5-fold), model explainability (SHAP), and plan for phased production rollout with performance monitoring and rollback options.

---

## Update 25

**Date:** 2025-08-08
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - BK2CX (RCI & CEL)
**People:** Unidentified

### Summarized Update

Collaboration with Siebel Team
Status: Setting up all lead types for ingestion into Siebel; ongoing iterative testing with the Siebel team
Notes / Risk & Mitigation: Potential data-type discrepancies and ingestion failures could slow progress. Mitigation: continue iterative testing, document data lineage, and resolve data quality issues promptly.

### Raw Update

Collaboration with Siebel Team
Status: Setting up all lead types for ingestion into Siebel; ongoing iterative testing with the Siebel team
Notes / Risk & Mitigation: Potential data-type discrepancies and ingestion failures could slow progress. Mitigation: continue iterative testing, document data lineage, and resolve data quality issues promptly.

---

## Update 26

**Date:** 2025-08-08
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** Unidentified

### Summarized Update

Exploratory Data Analysis (EDA) to Support Lead Accuracy Investigation
Focus: Identify discrepancies between CXLD bookings shown in the revenue dashboard
Activities: Email EDA; Phone Number EDA; Lead Count by Type
Notes / Risk & Mitigation: Discrepancies in revenue dashboard data may persist. Mitigation: complete EDA findings, implement data quality checks, and adjust ingestion pipelines as needed.

### Raw Update

Exploratory Data Analysis (EDA) to Support Lead Accuracy Investigation
Focus: Identify discrepancies between CXLD bookings shown in the revenue dashboard
Activities: Email EDA; Phone Number EDA; Lead Count by Type
Notes / Risk & Mitigation: Discrepancies in revenue dashboard data may persist. Mitigation: complete EDA findings, implement data quality checks, and adjust ingestion pipelines as needed.

---

## Update 27

**Date:** 2025-08-08
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

Work Completed – Data Preprocessing
Updated and reviewed LOB mapping for Casino
Ran basic forecasts for all 13 LOBs (ongoing)
Met with Jason’s team regarding office shrinkage data
Notes / Risk & Mitigation: Office shrinkage data involves complex queries that require additional time. Mitigation: document requirements, prioritize high-impact queries, and pursue phased delivery.

### Raw Update

Work Completed – Data Preprocessing
Updated and reviewed LOB mapping for Casino
Ran basic forecasts for all 13 LOBs (ongoing)
Met with Jason’s team regarding office shrinkage data
Notes / Risk & Mitigation: Office shrinkage data involves complex queries that require additional time. Mitigation: document requirements, prioritize high-impact queries, and pursue phased delivery.

---

## Update 28

**Date:** 2025-08-08
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** Unidentified

### Summarized Update

Next Steps – WPS Staffing Model Development
4) Run the FTE model for all 13 LOBs using the basic call volume forecast
5) Build data visualizations and forecasting app section
Notes / Risk & Mitigation: The basic forecast is for app functionality and testing rather than precision; updated shrinkage data will be addressed later. Mitigation: clearly separate MVP features from future enhancements and track as phased deliverables. Note: APP Version 01 will not include updated office shrinkage data; this will be addressed later, as it is not currently a priority.

### Raw Update

Next Steps – WPS Staffing Model Development
4) Run the FTE model for all 13 LOBs using the basic call volume forecast
5) Build data visualizations and forecasting app section
Notes / Risk & Mitigation: The basic forecast is for app functionality and testing rather than precision; updated shrinkage data will be addressed later. Mitigation: clearly separate MVP features from future enhancements and track as phased deliverables.
Note: APP Version 01 will not include updated office shrinkage data; this will be addressed later, as it is not currently a priority. The basic forecast is primarily intended to support development and testing of the app’s functionality rather than high accuracy at this stage.

---

## Update 29

**Date:** 2025-08-08
**Business Area:** Unclassified
**People:** [[bao_le/overview_bao_le|Bao Le]], [[caleb_sharkey/overview_caleb_sharkey|Caleb Sharkey]]

### Summarized Update

Interns
Jamie Gonzalez, Bao Le, and Caleb Sharkey
Status: Capstone presentations completed; graduates of the Royal Caribbean Internship program
Next steps: All three offered full-time positions, starting 8/8

### Raw Update

Interns
Jamie Gonzalez, Bao Le, and Caleb Sharkey
Status: Capstone presentations completed; graduates of the Royal Caribbean Internship program
Next steps: All three offered full-time positions, starting 8/8

---

## Update 30

**Date:** 2025-08-08
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - BK2CX (RCI & CEL)
**People:** Unidentified

### Summarized Update

Outlook / Next Week Focus
Finalize Siebel lead ingestion configurations and resolve any remaining data ingestion issues
Complete FTE modeling for 13 LOBs and begin building visualizations and app components
Advance internship program toward full-time onboarding for the three graduates.

### Raw Update

Outlook / Next Week Focus
Finalize Siebel lead ingestion configurations and resolve any remaining data ingestion issues
Complete FTE modeling for 13 LOBs and begin building visualizations and app components
Advance internship program toward full-time onboarding for the three graduates.

---

## Update 31

**Date:** 2025-08-08
**Business Area:** PCP Pricing Automation
**Business Project:** Perfect Day Product Pricing
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Project OBR Revenue Analysis
◦ Completed exploratory data analysis (EDA) to uncover key insights:
▪ Analyzed participation rates for Cococay. ▪ Investigated differences between repeat vs. non-repeat customers.

### Raw Update

Weekly Update:
1. Project OBR Revenue Analysis
◦ Completed exploratory data analysis (EDA) to uncover key insights:
▪ Analyzed participation rates for Cococay.
▪ Investigated differences between repeat vs. non-repeat customers.
▪ Explored revenue patterns across cabin classes.
▪ Assessed booking channel performance on sales
▪ Conducted analysis of metaproduct data.
▪ Segmented customer behavior by age groups.

---

## Update 32

**Date:** 2025-08-08
**Business Area:** Unclassified
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Digital App Analysis
Project App Review with Digital Team
◦ Ran the second version of the topic classifier to refine topic and description analysis. ◦ Generated initial results from the updated model. ◦ Will schedule meeting with stakeholder (Jaime) to review findings and gather feedback.

### Raw Update

Digital App Analysis
Project App Review with Digital Team
◦ Ran the second version of the topic classifier to refine topic and description analysis.
◦ Generated initial results from the updated model.
◦ Will schedule meeting with stakeholder (Jaime) to review findings and gather feedback.

---

## Update 33

**Date:** 2025-08-08
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

Delivered the first iteration of PRE-Logic enhancements, analyzing look-back vs look-forward track variance as part of the PRE. The business wants to test several more iterations including week-to-date considerations and varied weekly weightings. There will be a follow-up with the business in a couple of weeks.

### Raw Update

Delivered the first iteration of PRE-Logic enhancements, analyzing look-back vs look-forward track variance as part of the PRE. The business wants to test several more iterations including week-to-date considerations and varied weekly weightings. There will be a follow-up with the business in a couple of weeks.

---

## Update 34

**Date:** 2025-08-08
**Business Area:** CEL Revenue Management
**Business Project:** Elasticity Model Enhancements (PRE4.0)
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

Delivered the first iteration of PRE-Logic enhancements, analyzing look-back vs look-forward track variance as part of the PRE. The business wants to test several more iterations including week-to-date considerations and varied weekly weightings. There will be a follow-up with the business in a couple of weeks.

### Raw Update

Delivered the first iteration of PRE-Logic enhancements, analyzing look-back vs look-forward track variance as part of the PRE. The business wants to test several more iterations including week-to-date considerations and varied weekly weightings. There will be a follow-up with the business in a couple of weeks.

---

## Update 35

**Date:** 2025-08-08
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]], [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Elasticity 4.0 was fully integrated into the pipeline, generating pricing recommendations that were validated by the team. Prices are in line with business expectations. However, during testing, we discovered that VPS data provided by revenue planning did not separate balconies and neighborhoods when calculating cat_class lafs.

### Raw Update

Elasticity 4.0 was fully integrated into the pipeline, generating pricing recommendations that were validated by the team. Prices are in line with business expectations. However, during testing, we discovered that VPS data provided by revenue planning did not separate balconies and neighborhoods when calculating cat_class lafs. We are making updates to the feature store to recalculate lafs properly from another VPS dataset provided at the category level.

---

## Update 36

**Date:** 2025-08-08
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Initial web-driven baskets were presented to Chris and Eddie. Next week's RMA alignment meeting will be focused on how best to integrate web-based baskets to existing business practices.

### Raw Update

Initial web-driven baskets were presented to Chris and Eddie. Next week's RMA alignment meeting will be focused on how best to integrate web-based baskets to existing business practices.

---

## Update 37

**Date:** 2025-08-08
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

Integrated cat-class doubles in gap optimization. testing is in progress for gty lead 3.0.

### Raw Update

Integrated cat-class doubles in gap optimization. testing is in progress for gty lead 3.0.

---

## Update 38

**Date:** 2025-08-08
**Business Area:** RCI Revenue Management
**Business Project:** SPI-guided Track Optimization
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

FIT Track Setting through SPI has greatly improved model fits after smoothing training data targets. Findings were shared with Nick who provided positive feedback on track targets with minimal changes to better account for holidays by reducing smoothing in surrounding holiday weeks.

### Raw Update

FIT Track Setting through SPI has greatly improved model fits after smoothing training data targets. Findings were shared with Nick who provided positive feedback on track targets with minimal changes to better account for holidays by reducing smoothing in surrounding holiday weeks.

---

## Update 39

**Date:** 2025-08-08
**Business Area:** CEL Revenue Management
**Business Project:** Inventory Automation (FIT Reberthing & GROUPS Processes)
**People:** Unidentified

### Summarized Update

Groups replenishment delivered to the business, now running daily at 7:15 in prod.

### Raw Update

Groups replenishment delivered to the business, now running daily at 7:15 in prod.

---

## Update 40

**Date:** 2025-08-08
**Business Area:** CEL Revenue Management
**Business Project:** Elasticity Model Enhancements (PRE4.0)
**People:** Unidentified

### Summarized Update

Backtesting framework presented to Anastasia and team, with positive feedback. This framework is being used to validate model improvements from inclusion of features from RCI model including booking wave flag and spline based binning.

### Raw Update

Backtesting framework presented to Anastasia and team, with positive feedback. This framework is being used to validate model improvements from inclusion of features from RCI model including booking wave flag and spline based binning.

---

## Update 41

**Date:** 2025-08-08
**Business Area:** CEL Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model 3.0
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

GTY-Lead 3.0 code improvements now have the optimization running in 10% of the time, making it feasible for production.

### Raw Update

GTY-Lead 3.0 code improvements now have the optimization running in 10% of the time, making it feasible for production.

---

## Update 42

**Date:** 2025-08-08
**Business Area:** CEL Revenue Management
**Business Project:** Elasticity Model Enhancements (PRE4.0)
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

SPI improvements have reduced some overfitting that existed in the base model. Next steps on SPI include relaxing some of the normalization that led to too much sparsity, and analyzing timing of model training surrounding Laura's policy changes. Worked with the business to better understand the web-based baskets and comparison to existing baskets for suites and MTRB.

### Raw Update

SPI improvements have reduced some overfitting that existed in the base model. Next steps on SPI include relaxing some of the normalization that led to too much sparsity, and analyzing timing of model training surrounding Laura's policy changes. Worked with the business to better understand the web-based baskets and comparison to existing baskets for suites and MTRB.

---

## Update 43

**Date:** 2025-08-08
**Business Area:** SSC Revenue Management
**Business Project:** A/B Testing Framework
**People:** [[jesse_bausell/overview_jesse_bausell|Jesse Bausell]]

### Summarized Update

PRE is now ready for use in an A/B test on ~80 sailing pairs. Gaining alignment with the business on 8/8 to begin test.

### Raw Update

PRE is now ready for use in an A/B test on ~80 sailing pairs. Gaining alignment with the business on 8/8 to begin test.

---

## Update 44

**Date:** 2025-08-08
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

Continued development of EDA on shoreX with an initial focus on the waterpark. Collaborated with the digital team to better understand some of the requirements on promotion upload file to be able to test on specific sailings and products. There is a current blocker with DE/Platform where data is not able to be uploaded to UC.

### Raw Update

Continued development of EDA on shoreX with an initial focus on the waterpark. Collaborated with the digital team to better understand some of the requirements on promotion upload file to be able to test on specific sailings and products. There is a current blocker with DE/Platform where data is not able to be uploaded to UC. Platform is working through resolution.

---

## Update 45

**Date:** 2025-08-08
**Business Area:** Loyalty
**Business Project:** Spend-to-Save Pilot Analysis
**People:** [[kartik_ullal/overview_kartik_ullal|Kartik Ullal]], [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Prepared an analysis on earn rate per point to ensure that point redemption from co-brand pilot does not exceed the earn rate from typical cruising behavior. Awaiting refreshed percentages from the bank on how many guests spend more than the threshold to refresh power analysis for each brand, because the first percentage was a combined view. Awaiting OBR data for spend to save analysis due to be provided on 8/8.

### Raw Update

Prepared an analysis on earn rate per point to ensure that point redemption from co-brand pilot does not exceed the earn rate from typical cruising behavior. Awaiting refreshed percentages from the bank on how many guests spend more than the threshold to refresh power analysis for each brand, because the first percentage was a combined view. Awaiting OBR data for spend to save analysis due to be provided on 8/8. Confirmed with RCI OBR team (Austin Schladant) that no data had been shared for validation thus far, a requirement for the updated data delivery.

---

## Update 46

**Date:** 2025-08-08
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]], [[david_martinez/overview_david_martinez|David Martinez]]

### Summarized Update

Met with Senior Stakeholders to strategically refine upcoming CAR requirements. Focused on ensuring that Mass Promotions Automation becomes a core requirement of the next CAR and the AI team can assist the OBR teams in streamlining the process. For the purposes of PCP Automation, Promotional discounts will be the key unlock for realizing all future pricing automation.

### Raw Update

Met with Senior Stakeholders to strategically refine upcoming CAR requirements.
Focused on ensuring that Mass Promotions Automation becomes a core requirement of the next CAR and the AI team can assist the OBR teams in streamlining the process.
For the purposes of PCP Automation, Promotional discounts will be the key unlock for realizing all future pricing automation. This is because of fundamental limitations in how often we can change the base-rate (which will usually be a price hike to ensure guests always have the perception of a discount)

---

## Update 47

**Date:** 2025-08-08
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[glen-erik_cortez/overview_glen-erik_cortez|Glen-Erik Cortez]]

### Summarized Update

Partition issue fix in to_fcst_current_date, to_fcst and max_rev notebooks for all drink packages, almost modifying 12 notebooks. Identified the root cause of tables producing no rows sometimes, as DE team is refreshing the tables under schema "cmrs_ods_score" multiple times a day, each time deleting these table and creating it again. When the workflow is running at that time, as table is showing no rows and throwing errors.

### Raw Update

Partition issue fix in to_fcst_current_date, to_fcst and max_rev notebooks for all drink packages, almost modifying 12 notebooks.
Identified the root cause of tables producing no rows sometimes, as DE team is refreshing the tables under schema "cmrs_ods_score" multiple times a day, each time deleting these table and creating it again. When the workflow is running at that time, as table is showing no rows and throwing errors. This is issue is bought up to DE team and advised them to do upsert or overwrite operation instead of delete & overwrite.
Help in providing code to achieve multiprocessing in GTY Leads project and reduce runtime of 3hrs.
Incorporating data validation framework to TAP SUITES project
Feature store queries review and discussion with DE team to migrate feature store tables to prd_gold catalog.
Added file arrival based trigger to TAP_CEL_Event_Driven and productionized the project.
PR reviews and monitoring CI/CD deployment pipelines

---

_Source: 20250808 - Weekly Rafeh & Matt Update (Raw).docx_