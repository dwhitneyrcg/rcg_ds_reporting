---
tags:
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_targeting_(e-commerce)
  - business_area/hybris_product_recommendations_(digital)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/revenue_management_automation_(cel)
  - business_area/supply_chain_optimization
  - project/booking_propensity_models
  - project/enhanced_for_you_recommendations
  - project/enhanced_hf&b_demand_modelling
  - project/fleetwide_energy_monitoring
  - project/gty-lead_fare_optimization_model_3.0
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/loyalty_simulator_framework
  - project/offer_to_cancel_(oftocx)_model_(rci_&_cel)
  - summarized
  - weekly_update
date: "2024-08-02"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - 2024-08-02

## Excited

### E-Commerce

**Date:** 2024-08-02
**Business Area:** E-Commerce

**Achievements:**
Evaluating the opportunity to share Digital Product Recommendations API with the Email-Marketing Team to centralize Web/Email marketing around a single product recommendation engine. GenAI Use-Cases: Begun discussions on pilot GenAI use-cases with the Hotel Operations (RCI) & Databricks to summarize text from Medallia survey data. Also exploring opportunities to assist the Legal teams with data extraction and potential uses for NLP (GenAI) and the Deployment teams with data mapping, harmonization, cleaning and other potential uses for NLP (GenAI).

**Raw Update:**
Evaluating the opportunity to share Digital Product Recommendations API with the Email-Marketing Team to centralize Web/Email marketing around a single product recommendation engine.
GenAI Use-Cases: Begun discussions on pilot GenAI use-cases with the Hotel Operations (RCI) & Databricks to summarize text from Medallia survey data. Also exploring opportunities to assist the Legal teams with data extraction and potential uses for NLP (GenAI) and the Deployment teams with data mapping, harmonization, cleaning and other potential uses for NLP (GenAI).

---

### Revenue Management Automation (CEL)

**Date:** 2024-08-02
**Business Area:** Revenue Management Automation (CEL)
**Business Project:** GTY-Lead Fare Optimization Model 3.0

**Achievements:**
Evaluating the opportunity to leverage AI and customer data to forecast compensation amount for guests with issues, which could establish more consistency, recognize repeated guest patterns, and tie compensation amounts to forecasted outcomes (e.g. NPS, return rates, and future spend). Today nearly $80-100M is spent across CEL & RCI for guest recovery accounts. Mert
Deployed Quantum shipboard IoT data flow to production. Successful proof of concept for sending Python generated emails from DataBricks with embedded plots and attachments. Working towards real-time alerting mechanism. Met with Chief Meteorologist Craig to deploy real time alerts for ships experiencing high winds (over 50 knots) and dangeruous list. Updated dynamic IRR model of Clarent Energy Retrofit Program tool to integrate finance forecasts from GMO App. Working towards completing fleetwide service power baselines. Productionized MIAP Data Export tool on GMO WebApp and shared with entire GMO department and Newbuild stakeholders (over 150 people). Productionized Silversea Carbon Indensity Indicator model
Productionizing Delta Live Table for realtime MIAP data feed. Jake
07_31_2024_RM_Solutions_DA2I - Copy.pptx
CEL
Recently Completed
  GTY-Replenishment Code Release
  Move Elasticity Models to Feature Store (Standardized Bookings & Price Dataset)
  Candidate Final Stage Interviews
In Progress
  T4 Test Results Analysis
  Elasticity Model Addt’l Granularities (ALASKA, EUROPE, CARIB)
  PRE Variance-to-Track Rework & Dashboard
To Begin
  APD Track
  Basket CoV Analysis (CEL YTD + Historical Revenue Analysis + RCI YTD)
  Basket Logic in Track Updates (MTRB)
  GTY-Lead Test Results
  GTY-Lead Trade-Up Models
RCI
Recently Completed
  PRE Stale Prices Code Fixes, using Live Pricing in PL3
  Alignment with Biz on more Data Driven GTY REPL Rules
  Candidate Final Stage Interviews
  PRE Logs & Logging Code Cleanup
In Progress
  Additional Interviews
  Brand + Minor Meta Elasticities (To use in Track Opt)
  PRE Code Updates and Refactoring (Biz Rules, Old Accenture Code)
  SPI Model Development (Business Factors)
To Begin
  Additional Elasticity Model Upgrades (MLFlow, Re-Training, Metrics)
  SPI Model Development (Management Factors)
SSC
Recently Completed
  Analysis of Historical Booking Patterns (Area, Subarea, Seasonality)
  Reading on Industry Research for feasible methods of elasticity & demand modeling for SSC
  Story Refinement & Generation for PRE Elasticity Models (Choice Models)
In Progress
  MVP Code for SSC PRE
  Feature Engineering for Elasticity Models
  Fit initial regressions for Elasticity Models by Area + Additional Granularities
To Begin
  BPO: P2P vs D2D
  BPO: Category Gapping
PCP
Recently Completed
  Interviews for Candidates
In Progress
  Story and release refinement for Pricing Automation and Track Optimization asks. Formalizing Digital Asks into structured document to present. To Begin
  Initial Exploratory Data Analysis and spikes to support story refinement
  Meet with Digital team to review and prioritize asks of Azure --> Hybris Upload
Ben:
GSCBP
Enhancing Business Demand Forecasts by Training Models up to Last Day of Current Month:
Update
:
In progress of code refactoring to keep two sets of models for each product/ship combination. One will be trained with a back-tested month for reporting MAPE, the other set will train all data up to last date of current month. All business reports including the finance reconciliation tool are being migrated to the set of models that train up to the last day of the previous month. Pending Tasks
: All code refactoring to update the Finance Reconciliation Tool has been completed and the pipeline with the new code changes started this morning. Monitoring results and will adjust code as needed after testing and validating the new outputs. Need to still confirm other reporting (beyond Finance Tool) is performing as intended, and update code if necessary. Uniform Demand Modeling:
Update
:
Modifying code to correct for forecasting data being eliminated from dataset due to an adjusted join. Pending Tasks
: In process of validating results and will reconnect with Camila on status when she returns on 8/5. E-Commerce
Update
:
Added spend+bp model combination to the dashboard calculator. Improve bp+nbo models combination calculator with business suggestions: add  count in percent , fix error in query.

**Raw Update:**
Evaluating the opportunity to leverage AI and customer data to forecast compensation amount for guests with issues, which could establish more consistency, recognize repeated guest patterns, and tie compensation amounts to forecasted outcomes (e.g. NPS, return rates, and future spend). Today nearly $80-100M is spent across CEL & RCI for guest recovery accounts.
Mert
Deployed Quantum shipboard IoT data flow to production.
Successful proof of concept for sending Python generated emails from DataBricks with embedded plots and attachments. Working towards real-time alerting mechanism.
Met with Chief Meteorologist Craig to deploy real time alerts for ships experiencing high winds (over 50 knots) and dangeruous list.
Updated dynamic IRR model of Clarent Energy Retrofit Program tool to integrate finance forecasts from GMO App.
Working towards completing fleetwide service power baselines.
Productionized MIAP Data Export tool on GMO WebApp and shared with entire GMO department and Newbuild stakeholders (over 150 people).
Productionized Silversea Carbon Indensity Indicator model
Productionizing Delta Live Table for realtime MIAP data feed.
Jake
07_31_2024_RM_Solutions_DA2I - Copy.pptx
CEL
Recently Completed
  GTY-Replenishment Code Release
  Move Elasticity Models to Feature Store (Standardized Bookings & Price Dataset)
  Candidate Final Stage Interviews
In Progress
  T4 Test Results Analysis
  Elasticity Model Addt’l Granularities (ALASKA, EUROPE, CARIB)
  PRE Variance-to-Track Rework & Dashboard
To Begin
  APD Track
  Basket CoV Analysis (CEL YTD + Historical Revenue Analysis + RCI YTD)
  Basket Logic in Track Updates (MTRB)
  GTY-Lead Test Results
  GTY-Lead Trade-Up Models
RCI
Recently Completed
  PRE Stale Prices Code Fixes, using Live Pricing in PL3
  Alignment with Biz on more Data Driven GTY REPL Rules
  Candidate Final Stage Interviews
  PRE Logs & Logging Code Cleanup
In Progress
  Additional Interviews
  Brand + Minor Meta Elasticities (To use in Track Opt)
  PRE Code Updates and Refactoring (Biz Rules, Old Accenture Code)
  SPI Model Development (Business Factors)
To Begin
  Additional Elasticity Model Upgrades (MLFlow, Re-Training, Metrics)
  SPI Model Development (Management Factors)
SSC
Recently Completed
  Analysis of Historical Booking Patterns (Area, Subarea, Seasonality)
  Reading on Industry Research for feasible methods of elasticity & demand modeling for SSC
  Story Refinement & Generation for PRE Elasticity Models (Choice Models)
In Progress
  MVP Code for SSC PRE
  Feature Engineering for Elasticity Models
  Fit initial regressions for Elasticity Models by Area + Additional Granularities
To Begin
  BPO: P2P vs D2D
  BPO: Category Gapping
PCP
Recently Completed
  Interviews for Candidates
In Progress
  Story and release refinement for Pricing Automation and Track Optimization asks.
  Formalizing Digital Asks into structured document to present.
To Begin
  Initial Exploratory Data Analysis and spikes to support story refinement
  Meet with Digital team to review and prioritize asks of Azure --> Hybris Upload
Ben:
GSCBP
Enhancing Business Demand Forecasts by Training Models up to Last Day of Current Month:
Update
:
In progress of code refactoring to keep two sets of models for each product/ship combination. One will be trained with a back-tested month for reporting MAPE, the other set will train all data up to last date of current month. All business reports including the finance reconciliation tool are being migrated to the set of models that train up to the last day of the previous month.
Pending Tasks
: All code refactoring to update the Finance Reconciliation Tool has been completed and the pipeline with the new code changes started this morning. Monitoring results and will adjust code as needed after testing and validating the new outputs. Need to still confirm other reporting (beyond Finance Tool) is performing as intended, and update code if necessary.
Uniform Demand Modeling:
Update
:
Modifying code to correct for forecasting data being eliminated from dataset due to an adjusted join.
Pending Tasks
: In process of validating results and will reconnect with Camila on status when she returns on 8/5.
E-Commerce
Update
:
Added spend+bp model combination to the dashboard calculator.
Improve bp+nbo models combination calculator with business suggestions: add  count in percent , fix error in query.

---

### Contact Center Optimization & Automation (RCI/CEL)

**Date:** 2024-08-02
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - CTI (RCI & CEL)

**Achievements:**
Avoid removing negative samples from validation data for more accurate metrics,
code cleaning,
Replace options to sample individual tables by group sampling during feature engineering (ie: take out rows not in booking table)
replace decile by quantile in models training report (ie 10->100 bins)
Progress in watchlist/favorites  data ingestion into the models (first results  should be ready tomorrow)
Pending Tasks:
Continue with the integration of watchlist/favorites  data. Improve Audience Sizing Calculator metrics and oracle queries (currently for alpha only)
Loyalty
Update
:
Validation of guest simulation with latest future ship deployment simulation
Updated guest simulation scenario with pre-Covid spend sourcing
Erick Updates: 
  WoW
  - Developed new approach towards the MDR pipeline, now able to match the probable actual menu assortments with complex and inconsistent MDR operating hours and meal periods. Exploratory analyis on Dominant menu assortments by Volume and by Name to understand how much historical data can be used. Loyalty 
  - Implemented the Loyalty Tiering Simulator to be compatible with Sailed Nights. - Added Casino to the Loyalty Simulator aggregations to satisfy future analytics requirements. Digital 
  Product Recommendations
  - Met with frontend dev team to align on expected outputs from the recommendations API. - Aligned with business on potential options for future advanced recommendations. We are pending a decision on the exact algorithm & strategy for personalized recommendations. - Developed and demoed a proof-of-concept AI-Search for PCP (similar to Cruise search). GS Bot:
  - Deployed the GS Chat Topic classifier and shared with Stakeholder
  - Finalized and delivered Topic Classification Dashboard with Stakeholder

  Guest Logs Analytics
  - Updated Guest Log scoring logic

  Onboard Revenue (CEL)
  - Met with business the share intial NPS targets for 2025. Scaling forecasting to set targets for over a dozen Medallia customer satisfaction metrics
New Use Cases: 
  E-Commerce (Email Marketing)
  - Met with stakeholders to share the Digital Recommendations API and discuss opportunities to collaborate. - Looking to centralize Recommendations for Web and Email marketing around a singular recommendations engine. Legal (Shey Seara)
  - We are exploring an opportunity to assist the Legal teams with data extraction and potential uses for NLP (GenAI). Deployment (Brooke Gonzalez) 
  - We are exploring an opportunity to assist the Deployment teams with data mapping, harmonizationm, cleaning and potential uses for NLP (GenAI).

**Raw Update:**
Avoid removing negative samples from validation data for more accurate metrics,
code cleaning,
Replace options to sample individual tables by group sampling during feature engineering (ie: take out rows not in booking table)
replace decile by quantile in models training report (ie 10->100 bins)
Progress in watchlist/favorites  data ingestion into the models (first results  should be ready tomorrow)
Pending Tasks:
Continue with the integration of watchlist/favorites  data.
Improve Audience Sizing Calculator metrics and oracle queries (currently for alpha only)
Loyalty
Update
:
Validation of guest simulation with latest future ship deployment simulation
Updated guest simulation scenario with pre-Covid spend sourcing
Erick Updates: 
  WoW
  - Developed new approach towards the MDR pipeline, now able to match the probable actual menu assortments with complex and inconsistent MDR operating hours and meal periods. Exploratory analyis on Dominant menu assortments by Volume and by Name to understand how much historical data can be used.
Loyalty 
  - Implemented the Loyalty Tiering Simulator to be compatible with Sailed Nights. 
  - Added Casino to the Loyalty Simulator aggregations to satisfy future analytics requirements.
Digital 
  Product Recommendations
  - Met with frontend dev team to align on expected outputs from the recommendations API. 
  - Aligned with business on potential options for future advanced recommendations. We are pending a decision on the exact algorithm & strategy for personalized recommendations. 
  - Developed and demoed a proof-of-concept AI-Search for PCP (similar to Cruise search).
GS Bot:
  - Deployed the GS Chat Topic classifier and shared with Stakeholder
  - Finalized and delivered Topic Classification Dashboard with Stakeholder

  Guest Logs Analytics
  - Updated Guest Log scoring logic

  Onboard Revenue (CEL)
  - Met with business the share intial NPS targets for 2025.
Scaling forecasting to set targets for over a dozen Medallia customer satisfaction metrics
New Use Cases: 
  E-Commerce (Email Marketing)
  - Met with stakeholders to share the Digital Recommendations API and discuss opportunities to collaborate. 
  - Looking to centralize Recommendations for Web and Email marketing around a singular recommendations engine.
Legal (Shey Seara)
  - We are exploring an opportunity to assist the Legal teams with data extraction and potential uses for NLP (GenAI).
Deployment (Brooke Gonzalez) 
  - We are exploring an opportunity to assist the Deployment teams with data mapping, harmonizationm, cleaning and potential uses for NLP (GenAI).

---

## Updates

### Product Recommendations

**Date:** 2024-08-02
**Business Area:** Product Recommendations
**Business Project:** Enhanced For You Recommendations

**Achievements:**
Developed and demoed a proof-of-concept LLM-powered natural-language search for PCP products (similar to Cruise Search). Aligned on expected outputs from the Product Recommendations Engine MVP (for trending, popular, and new items) and more advanced personalization. Deployed GS Chat Topic Classifier and finalized Topic Classification Dashboard with business stakeholders.

**Raw Update:**
Developed and demoed a proof-of-concept LLM-powered natural-language search for PCP products (similar to Cruise Search). Aligned on expected outputs from the Product Recommendations Engine MVP (for trending, popular, and new items) and more advanced personalization. Deployed GS Chat Topic Classifier and finalized Topic Classification Dashboard with business stakeholders.

---

### Customer Targeting

**Date:** 2024-08-02
**Business Area:** Customer Targeting
**Business Project:** Booking Propensity Models

**Achievements:**
Completed User enhancements for the Campaign Dashboard Calculator based on business feedback, which will help business teams use the team’s customer targeting models (based on booking propensity/lifetime spend forecasts).

**Focus Areas:**
Next steps are to improve audience sizing calculator metrics and continue with integration of watchlist/favorites data.

**Raw Update:**
Completed User enhancements for the Campaign Dashboard Calculator based on business feedback, which will help business teams use the team’s customer targeting models (based on booking propensity/lifetime spend forecasts). Next steps are to improve audience sizing calculator metrics and continue with integration of watchlist/favorites data.

---

### Revenue Management Automation (CEL)

**Date:** 2024-08-02
**Business Area:** Revenue Management Automation (CEL)

**Achievements:**
Developed and shared initial 2025 NPS Targets.

**Focus Areas:**
Next steps are to scale forecasts against set business targets for a dozen Medallia customer satisfaction metrics.

**Raw Update:**
Developed and shared initial 2025 NPS Targets. Next steps are to scale forecasts against set business targets for a dozen Medallia customer satisfaction metrics.

---

### Loyalty

**Date:** 2024-08-02
**Business Area:** Loyalty
**Business Project:** Loyalty Simulator Framework

**Achievements:**
Implemented the Loyalty Tiering Simulator to be compatible with Sailing Nights and analyzed differences with Spend-Based approach and integrated casino spend into the Loyalty Simulator to satisfy future business requirements.

**Focus Areas:**
Next steps are to incorporate Silversea booking data into the Loyalty Simulator Model.

**Raw Update:**
Implemented the Loyalty Tiering Simulator to be compatible with Sailing Nights and analyzed differences with Spend-Based approach and integrated casino spend into the Loyalty Simulator to satisfy future business requirements.  Next steps are to incorporate Silversea booking data into the Loyalty Simulator Model.

---

### Marine Operations

**Date:** 2024-08-02
**Business Area:** Marine Operations
**Business Project:** Fleetwide Energy Monitoring

**Achievements:**
Completed deployment for Silversea Carbon Intensity Indicator model, Quantum shipboard IoT data flow, Delta Live Table for realtime MIAP data feed, and MIAP Data Export tool on GMO WebApp.

**Focus Areas:**
Next steps are to complete fleetwide service power baselines, real-time alerting, and working with Chief Meteorologist Craig to deploy real time alerts for ships experiencing high winds (over 50 knots) or dangerous listing.

**Raw Update:**
Completed deployment for Silversea Carbon Intensity Indicator model, Quantum shipboard IoT data flow, Delta Live Table for realtime MIAP data feed, and MIAP Data Export tool on GMO WebApp. Next steps are to complete fleetwide service power baselines, real-time alerting, and working with Chief Meteorologist Craig to deploy real time alerts for ships experiencing high winds (over 50 knots) or dangerous listing.

---

### Contact Center Optimization & Automation (RCI/CEL)

**Date:** 2024-08-02
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)

**Achievements:**
Completed code release of GTY-Replenishment (CEL), upgraded elasticity models to use Feature Stores (CEL), updated PRE Stale Price Code Fixes (RCI), PRE Logging Code Cleanup (RCI) and a detailed analysis on historical booking patterns for building demand forecasts (SSC). Team is close to hiring a large number of new Data Scientists to support ongoing capital projects for pricing automation.

**Raw Update:**
Completed code release of GTY-Replenishment (CEL), upgraded elasticity models to use Feature Stores (CEL), updated PRE Stale Price Code Fixes (RCI), PRE Logging Code Cleanup (RCI) and a detailed analysis on historical booking patterns for building demand forecasts (SSC). Team is close to hiring a large number of new Data Scientists to support ongoing capital projects for pricing automation.

---

### Supply Chain

**Date:** 2024-08-02
**Business Area:** Supply Chain
**Business Project:** Enhanced HF&B Demand Modelling

**Achievements:**
Updated HF&B demand forecasting pipelines to train separate models for performance evaluation and business reporting, enabling demand forecasts for business reporting to benefit from consumption data up to the last day of the current month. Developed a new approach towards forecasting consumption in Main Dining Room for WoW that probabilistically matches actual menu packages used by shipboard chefs regardless of the planned menu (based on Itinerary Day).

**Focus Areas:**
Next steps are to update the Finance Reconciliation Tool with the new demand forecasts and continue development of Uniform Demand Forecasts.

**Raw Update:**
Updated HF&B demand forecasting pipelines to train separate models for performance evaluation and business reporting, enabling demand forecasts for business reporting to benefit from consumption data up to the last day of the current month. Developed a new approach towards forecasting consumption in Main Dining Room for WoW that probabilistically matches actual menu packages used by shipboard chefs regardless of the planned menu (based on Itinerary Day). Next steps are to update the Finance Reconciliation Tool with the new demand forecasts and continue development of Uniform Demand Forecasts.

---

_Source: 20240802 - Weekly Rafeh Update.docx_