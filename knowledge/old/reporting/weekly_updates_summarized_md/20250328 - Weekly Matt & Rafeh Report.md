---
tags:
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/customer_targeting_(e-commerce)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/propel_targeted_offers_(cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/revenue_management_automation_(ssc)
  - business_area/supply_chain_optimization
  - project/a_b_testing_framework
  - project/booking_propensity_models
  - project/cltv-drivers_model_development
  - project/division-level_medallia_reports
  - project/expedition_forecasting_with_silversea_automation
  - project/gty-lead_fare_optimization_model
  - project/gty-lead_fare_optimization_model_3.0
  - project/lead_prioritization_-_bk2cx_(rci_&_cel)
  - project/marine_safety_analytics
  - project/perfect_day_product_pricing
  - project/propel_targeted_offers_deployment
  - project/spend-to-save_pilot_analysis
  - summarized
  - weekly_update
date: "2025-03-28"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - 2025-03-28

## Proud

### E-Commerce

**Date:** 2025-03-28
**Business Area:** E-Commerce
**Business Project:** Booking Propensity Models

**Achievements:**
DS team has completed enhancements to the E-Commerce Marketing Campaign Uplift Models, which forecasts how much booking propensity incrementally changes after E-Commerce targets individuals with marketing campaigns. We have shared model with key business stakeholders and completed integrating the model into Databricks Genie. Actively working on productionizing Uplift model, investigating new onboard datasets to improve PCP targeting models, and integrating Epsilon demographic + spend data into Databricks Genie.

**Raw Update:**
DS team has completed enhancements to the E-Commerce Marketing Campaign Uplift Models, which forecasts how much booking propensity incrementally changes after E-Commerce targets individuals with marketing campaigns. We have shared model with key business stakeholders and completed integrating the model into Databricks Genie. Actively working on productionizing Uplift model, investigating new onboard datasets to improve PCP targeting models, and integrating Epsilon demographic + spend data into Databricks Genie.

---

### Marine Operations

**Date:** 2025-03-28
**Business Area:** Marine Operations
**Business Project:** Marine Safety Analytics

**Achievements:**
DS + DE teams met with GMO Marine Safety Team (Jan Solum) and discussed expanding MIAP program into Marine Safety domain. Teams identified usefulness in building a risk forecasting model for Safety Incidents based on a ship's recent history and current environmental conditions. Teams also completed tag mapping for AHU Supply Fan Speed and Energy Recovery Wheels for 7 ships, updated HVAC/Hotel/Machinery & Service Power models for 5 ships, deployed MIAP IoT Data Flows for 2 ships, troubled-shooted non-deterministic behavior in MIAP forecasting models, identified data changes from different vendors, and investigating energy deviations on 4 ships.

**Raw Update:**
DS + DE teams met with GMO Marine Safety Team (Jan Solum) and discussed expanding MIAP program into Marine Safety domain. Teams identified usefulness in building a risk forecasting model for Safety Incidents based on a ship's recent history and current environmental conditions. Teams also completed tag mapping for AHU Supply Fan Speed and Energy Recovery Wheels for 7 ships, updated HVAC/Hotel/Machinery & Service Power models for 5 ships, deployed MIAP IoT Data Flows for 2 ships, troubled-shooted non-deterministic behavior in MIAP forecasting models, identified data changes from different vendors, and investigating energy deviations on 4 ships.

---

### Medallia

**Date:** 2025-03-28
**Business Area:** Medallia
**Business Project:** Division-Level Medallia Reports

**Achievements:**
DS team held first STEERING call this week with constructive feedback on prioritizing future deliveries from business leadership teams (i.e. RCI/CEL Consumer Insights and Hotel Operations Teams). Focus will be on business teams testing new Medallia Databricks App who will provide constructive feedback back to the DS team. Also presented a demo of the new Databricks App to the RCI Consumer Insights teams with highly positive feedback and next steps will be to present the Databricks App to Kara.

**Raw Update:**
DS team held first STEERING call this week with constructive feedback on prioritizing future deliveries from business leadership teams (i.e. RCI/CEL Consumer Insights and Hotel Operations Teams). Focus will be on business teams testing new Medallia Databricks App who will provide constructive feedback back to the DS team. Also presented a demo of the new Databricks App to the RCI Consumer Insights teams with highly positive feedback and next steps will be to present the Databricks App to Kara.

---

### PROPEL

**Date:** 2025-03-28
**Business Area:** PROPEL
**Business Project:** PROPEL Targeted Offers Deployment

**Achievements:**
Awareness offers are now live on Celebrity Ascent, which enable business teams to create targeted awareness offers without including discounts. MLOps delivered adjustments to PROPEL offers output, enhancements to offer assignments logics, and trouble-shooted production challenges over last weekend. DS + MLOPs teams has discussions with BCG team on upcoming AI modeling work for upcoming PCP Targeted Offers project.

**Raw Update:**
Awareness offers are now live on Celebrity Ascent, which enable business teams to create targeted awareness offers without including discounts. MLOps delivered adjustments to PROPEL offers output, enhancements to offer assignments logics, and trouble-shooted production challenges over last weekend. DS + MLOPs teams has discussions with BCG team on upcoming AI modeling work for upcoming PCP Targeted Offers project.

---

### Supply Chain

**Date:** 2025-03-28
**Business Area:** Supply Chain
**Business Project:** Expedition Forecasting with Silversea Automation

**Achievements:**
DS Team delivered a RCI/CEL Order Creation Dataset, which segments our monthly AI demand forecasts for each ship down to the voyage-level based on the container load date contained in the Master Load schedule. Team also developed documentation for Silversea consumption/forecasting data to ensure clarity and consistency for internal users and developed baseline error metrics for Medical demand forecasting models. Actively working on enhancements to SSC/RCI/CEL demand forecast models using improved feature selection and tuned hyperparameters.

**Focus Areas:**
Team will be formally presenting the work next week to Supply Chain leaders, but we have already received positive feedback.

**Raw Update:**
DS Team delivered a RCI/CEL Order Creation Dataset, which segments our monthly AI demand forecasts for each ship down to the voyage-level based on the container load date contained in the Master Load schedule. Team will be formally presenting the work next week to Supply Chain leaders, but we have already received positive feedback. Team also developed documentation for Silversea consumption/forecasting data to ensure clarity and consistency for internal users and developed baseline error metrics for Medical demand forecasting models. Actively working on enhancements to SSC/RCI/CEL demand forecast models using improved feature selection and tuned hyperparameters.

---

### Revenue Management (RCI)

**Date:** 2025-03-28
**Business Area:** Revenue Management (RCI)
**Business Project:** GTY-Lead Fare Optimization Model

**Achievements:**
DS Team delivered ADA compliance automation to berth accessible guarantee bookings, while MLOPs developed a new Databricks framework that makes it easier for RM teams to directly ingest new data tables into Unity Catalog from ADF. Also completed a rigorous SPI analysis into key sailing management factors that identify highly profitable sailings and shared with business teams this week. Early results show that listed standard (and T4) prices can counterintuitively be higher for worse performing sailings, and future analysis needs to be extended to include paid prices. This analysis will be used to develop best practices and inform future SPI modeling. DS team actively working on delivering elasticity enhancements, GTY-lead optimization models, and T4 Testing Design, while MLOPs is working to deliver critical Deployment/Validation enhancements.

**Raw Update:**
DS Team delivered ADA compliance automation to berth accessible guarantee bookings, while MLOPs developed a new Databricks framework that makes it easier for RM teams to directly ingest new data tables into Unity Catalog from ADF. Also completed a rigorous SPI analysis into key sailing management factors that identify highly profitable sailings and shared with business teams this week. Early results show that listed standard (and T4) prices can counterintuitively be higher for worse performing sailings, and future analysis needs to be extended to include paid prices. This analysis will be used to develop best practices and inform future SPI modeling. DS team actively working on delivering elasticity enhancements, GTY-lead optimization models, and T4 Testing Design, while MLOPs is working to deliver critical Deployment/Validation enhancements.

---

## Excited

### CLTV

**Date:** 2025-03-28
**Business Area:** CLTV
**Business Project:** CLTV-Drivers Model Development

**Achievements:**
DS Team shared CLTV datasets with E-Commerce teams, who plan to integrate LTV data into the E-Commerce Booking Recommendation Engine.

**Focus Areas:**
After constructive conversations with Corporate Planning, DS team is actively developing a PoC CLTV-drivers models to help business teams identify additional profitable consumer segments.

**Raw Update:**
DS Team shared CLTV datasets with E-Commerce teams, who plan to integrate LTV data into the E-Commerce Booking Recommendation Engine. After constructive conversations with Corporate Planning, DS team is actively developing a PoC CLTV-drivers models to help business teams identify additional profitable consumer segments.

---

### Contact Center

**Date:** 2025-03-28
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - BK2CX (RCI & CEL)

**Achievements:**
DS Team actively validating BK2CX lead prioritization scoring pipeline to debug productionization issues and now monitoring daily lead scoring performance (i.e. 4-12k leads for RCI and 1-3k leads for CEL). CCAS team working on Cresta AB Testing pilot (finalizing testing population and visualizing testing KPIs on a new BI dashboard), call forecasting + workforce planning for International and Casino, and on new designs+updates to RCI/CEL Conversational IVR.

**Raw Update:**
DS Team actively validating BK2CX lead prioritization scoring pipeline to debug productionization issues and now monitoring daily lead scoring performance (i.e. 4-12k leads for RCI and 1-3k leads for CEL). CCAS team working on Cresta AB Testing pilot (finalizing testing population and visualizing testing KPIs on a new BI dashboard), call forecasting + workforce planning for International and Casino, and on new designs+updates to RCI/CEL Conversational IVR.

---

### Loyalty

**Date:** 2025-03-28
**Business Area:** Loyalty
**Business Project:** Spend-to-Save Pilot Analysis

**Achievements:**
DS Team continued to refine pilot success criteria metrics for Spend-for-Reward Loyalty Pilot, which includes an expectation that the pilot will increase onboard spend for all guests and not just guests redeeming their FCC.

**Raw Update:**
DS Team continued to refine pilot success criteria metrics for Spend-for-Reward Loyalty Pilot, which includes an expectation that the pilot will increase onboard spend for all guests and not just guests redeeming their FCC.

---

### PCP Pricing Automation

**Date:** 2025-03-28
**Business Area:** PCP Pricing Automation
**Business Project:** Perfect Day Product Pricing

**Achievements:**
DS team working on an exploratory analysis for optimizing pricing for Beverage packages and planning to share results with business teams today. Pricing automation for Beverage products being prioritized due to being a high-margin product and concerns about secular decline for alcohol.

**Raw Update:**
DS team working on an exploratory analysis for optimizing pricing for Beverage packages and planning to share results with business teams today. Pricing automation for Beverage products being prioritized due to being a high-margin product and concerns about secular decline for alcohol.

---

### Revenue Management (CEL)

**Date:** 2025-03-28
**Business Area:** Revenue Management (CEL)
**Business Project:** GTY-Lead Fare Optimization Model 3.0

**Achievements:**
DS team fine-tuned FIT Berthing logic based on business feedback and reviewed Mandatory Occupancy Automation requirements with business for both singles and T4 (triples/quads) inventory. DS + MLOPs teams actively working on delivering elasticity enhancements, GTY-lead optimization models, SPI enhancements, and T4 Testing Design.

**Raw Update:**
DS team fine-tuned FIT Berthing logic based on business feedback and reviewed Mandatory Occupancy Automation requirements with business for both singles and T4 (triples/quads) inventory. DS + MLOPs teams actively working on delivering elasticity enhancements, GTY-lead optimization models, SPI enhancements, and T4 Testing Design.

---

### Revenue Management (SSC)

**Date:** 2025-03-28
**Business Area:** Revenue Management (SSC)
**Business Project:** A/B Testing Framework

**Achievements:**
DS team working on a continuous learning framework that will enable seamless AB testing for upcoming PRE pilots. The new framework will also make it easier to evaluate the effectiveness of future PRE enhancements.

**Raw Update:**
DS team working on a continuous learning framework that will enable seamless AB testing for upcoming PRE pilots. The new framework will also make it easier to evaluate the effectiveness of future PRE enhancements.

---

_Source: 20250328 - Weekly Matt & Rafeh Report.docx_