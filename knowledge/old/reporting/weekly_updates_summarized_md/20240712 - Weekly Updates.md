---
tags:
  - business_area/customer_targeting_(e-commerce)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/revenue_management_automation_(ssc)
  - business_area/supply_chain_optimization
  - project/booking_propensity_models
  - project/cococay_integration_and_guardrails
  - project/enhanced_hf&b_demand_modelling
  - project/fleetwide_energy_monitoring
  - project/gty-lead_fare_optimization_model_3.0
  - project/loyalty_simulator_framework
  - project/pre_4.0_elasticity_enhancements
  - project/pricing_recommendation_engine_(pre)_automation
  - summarized
  - weekly_update
date: "2024-07-12"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - 2024-07-12

## Proud

### Revenue Management (RCI)

**Date:** 2024-07-12
**Business Area:** Revenue Management (RCI)
**Business Project:** PRE 4.0 Elasticity Enhancements

**Achievements:**
Delivered elasticity-based track optimization algorithm for RCI that optionally penalizes demand within final payment. Team also delivered minor enhancements to (a) berthing automation that fixed corrupted bookings from s one-time manual de-berthing process used in Manilla (fixing 1,500 bookings) and (b) PRE to improve business rules and guardrails based on business feedback.

**Raw Update:**
Delivered elasticity-based track optimization algorithm for RCI that optionally penalizes demand within final payment. Team also delivered minor enhancements to (a) berthing automation that fixed corrupted bookings from s one-time manual de-berthing process used in Manilla (fixing 1,500 bookings) and (b) PRE to improve business rules and guardrails based on business feedback.

---

### Marine Operations

**Date:** 2024-07-12
**Business Area:** Marine Operations
**Business Project:** Fleetwide Energy Monitoring

**Achievements:**
Deployed several new capabilities: (a) Utopia IoT pipeline on Alpha Platform enabling the team to begin adapting energy monitoring solutions for Utopia, (b) enhanced MIAP Data & Analytics API to production via Azure Container Apps to improve API response time, (c) an adaptable YAML-based configuration framework to streamline the process of updating Data Visualizations on the MIAP web-app.

**Raw Update:**
Deployed several new capabilities: (a) Utopia IoT pipeline on Alpha Platform enabling the team to begin adapting energy monitoring solutions for Utopia, (b) enhanced MIAP Data & Analytics API to production via Azure Container Apps to improve API response time, (c) an adaptable YAML-based configuration framework to streamline the process of updating Data Visualizations on the MIAP web-app.

---

### Supply Chain

**Date:** 2024-07-12
**Business Area:** Supply Chain
**Business Project:** Enhanced HF&B Demand Modelling

**Achievements:**
Completed building 41,000 pilot Demand Forecasting Models for Silversea to forecast consumption across 8,700 unique HF&B products. Next steps will be business validation of the forecast and inclusion of guard-rails.

**Raw Update:**
Completed building 41,000 pilot Demand Forecasting Models for Silversea to forecast consumption across 8,700 unique HF&B products. Next steps will be business validation of the forecast and inclusion of guard-rails.

---

### Supply Chain

**Date:** 2024-07-12
**Business Area:** Supply Chain
**Business Project:** CocoCay Integration and Guardrails

**Achievements:**
Productionized price scraping tool that automates the collection of spec/commodity prices used for inflation analysis across 19 websites. Tool substantially reduces time spent on a highly manual process and combines pricing data for all products in a sole data table. All products were previously maintained on standalone excel sheets.

**Raw Update:**
Productionized price scraping tool that automates the collection of spec/commodity prices used for inflation analysis across 19 websites. Tool substantially reduces time spent on a highly manual process and combines pricing data for all products in a sole data table. All products were previously maintained on standalone excel sheets.

---

## Excited

### Loyalty Program Redesign

**Date:** 2024-07-12
**Business Area:** Loyalty Program Redesign
**Business Project:** Loyalty Simulator Framework

**Achievements:**
The new algorithm will enable the MIAP team to identify anomalies and prioritize the most important insights to surface to shipboard engineers on the MIAP web-app. The team expects to reuse this tool in Supply Chain and Revenue Management.

**Focus Areas:**
The new intern, Arya, has successfully developed a new change-point detection algorithm framework and next steps are to include in the MIAP Python package.

**Raw Update:**
The new intern, Arya, has successfully developed a new change-point detection algorithm framework and next steps are to include in the MIAP Python package. The new algorithm will enable the MIAP team to identify anomalies and prioritize the most important insights to surface to shipboard engineers on the MIAP web-app. The team expects to reuse this tool in Supply Chain and Revenue Management.

---

### E-Commerce

**Date:** 2024-07-12
**Business Area:** E-Commerce
**Business Project:** Booking Propensity Models

**Achievements:**
Finished integration of Epsilon Spending data into Booking Propensity/Guest Spending Models. The new spending features positively impact the AI forecasts and E-Commerce is excited to productionize the enhanced models soon.

**Raw Update:**
Finished integration of Epsilon Spending data into Booking Propensity/Guest Spending Models. The new spending features positively impact the AI forecasts and E-Commerce is excited to productionize the enhanced models soon.

---

### Loyalty

**Date:** 2024-07-12
**Business Area:** Loyalty
**Business Project:** Loyalty Simulator Framework

**Achievements:**
Team integrated cost & utilization data from the E-Commerce team into the Loyalty Simulator and adjusting the Loyalty Simulator to make future-looking simulations more realistic.

**Raw Update:**
Team integrated cost & utilization data from the E-Commerce team into the Loyalty Simulator and adjusting the Loyalty Simulator to make future-looking simulations more realistic.

---

### Revenue Management (SSC)

**Date:** 2024-07-12
**Business Area:** Revenue Management (SSC)
**Business Project:** Pricing Recommendation Engine (PRE) Automation

**Achievements:**
Actively developing a geospatial clustering algorithm to cluster sailings based on geographical simulator.

**Focus Areas:**
The team will use this tool to determine how to segment booking data to build demand forecasts for the Pricing Recommendation Engine.

**Raw Update:**
Actively developing a geospatial clustering algorithm to cluster sailings based on geographical simulator. The team will use this tool to determine how to segment booking data to build demand forecasts for the Pricing Recommendation Engine.

---

### Revenue Management (CEL)

**Date:** 2024-07-12
**Business Area:** Revenue Management (CEL)
**Business Project:** GTY-Lead Fare Optimization Model 3.0

**Achievements:**
CEL’s first inventory automation process, GTY Replenishment, is delivered and ready to be turned on when CEL begins a new AB Test to optimize GTY / Lead Pricing. Digital NLP/GenAI Use-Cases: Had constructive dialogues with Digital & Digital Engineering teams on prioritizing future AI use-cases for Royal Community & Marketplace.

**Raw Update:**
CEL’s first inventory automation process, GTY Replenishment, is delivered and ready to be turned on when CEL begins a new AB Test to optimize GTY / Lead Pricing.
Digital NLP/GenAI Use-Cases: Had constructive dialogues with Digital & Digital Engineering teams on prioritizing future AI use-cases for Royal Community & Marketplace.

---

### E-Commerce

**Date:** 2024-07-12
**Business Area:** E-Commerce
**Business Project:** Booking Propensity Models

**Achievements:**
Team completed a review of the impact on Epsilon spend data and discovered that guests with Epsilon spend data have 1.5x greater chance to book. As such, the team is excluding Epsilon spend for calculating booking propensity (but still using the data for forecasting future spend). enhancements to the Dashboard Calculator and integration of a watchlist/favorites data for combining AI model outputs together).

**Focus Areas:**
The team is actively enhancing the Streamlit Dashboard to enable the E-Commerce teams to more easily use the targeting models (i.e.

**Raw Update:**
Team completed a review of the impact on Epsilon spend data and discovered that guests with Epsilon spend data have 1.5x greater chance to book. As such, the team is excluding Epsilon spend for calculating booking propensity (but still using the data for forecasting future spend). The team is actively enhancing the Streamlit Dashboard to enable the E-Commerce teams to more easily use the targeting models (i.e. enhancements to the Dashboard Calculator and integration of a watchlist/favorites data for combining AI model outputs together).

---

_Source: 20240712 - Weekly Updates.docx_