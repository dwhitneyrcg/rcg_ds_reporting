---
tags:
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
  - project/a_b_testing_framework
  - project/beverage_package_optimization
  - project/booking_propensity_models
  - project/category_gapping_optimization_3.0
  - project/cltv-drivers_model_development
  - project/cococay_integration_and_guardrails
  - project/division-level_medallia_reports
  - project/enhanced_for_you_recommendations
  - project/forecasting_pipeline_expansion
  - project/hvac_diagnostics_&_anomaly_detection
  - project/offer_template_expansion
  - project/pre_4.0_elasticity_enhancements
  - project/workforce_planning_tool
  - summarized
  - weekly_update
date: "2026-02-06"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - 2026-02-06

## Proud

### Marine Insights Analytics Platform (Marine Operations)

**Date:** 2026-02-06
**Business Area:** Marine Insights Analytics Platform (Marine Operations)
**Business Project:** HVAC Diagnostics & Anomaly Detection

**Achievements:**
DS Team identified ~200 kW savings were identified on a monitored ship pending stability confirmation. Also advanced the rolling-horizon power-plant optimizer, created hull-coating degradation baselines, added shore-power support, improved SFOC anomaly detection, and stood up an initial fuel-forecast pipeline using sensor data. Multiple AHU/ETL defects were fixed, dynamic model start logic was tuned.

**Focus Areas:**
Teams are focusing on battery-integration approaches, LNG-optimizer fixes influencing fuel forecasts, and requirements for the HVAC diagnostic agent.

**Raw Update:**
DS Team identified ~200 kW savings were identified on a monitored ship pending stability confirmation. Also advanced the rolling-horizon power-plant optimizer, created hull-coating degradation baselines, added shore-power support, improved SFOC anomaly detection, and stood up an initial fuel-forecast pipeline using sensor data. Multiple AHU/ETL defects were fixed, dynamic model start logic was tuned. Teams are focusing on battery-integration approaches, LNG-optimizer fixes influencing fuel forecasts, and requirements for the HVAC diagnostic agent.

---

### PCP Pricing Automation

**Date:** 2026-02-06
**Business Area:** PCP Pricing Automation
**Business Project:** Beverage Package Optimization

**Achievements:**
DS Team delivered sailing lists for subsequent Royal Beach Club pricing tests, updated optimization routines to incorporate Royal Beach Club–Beverage bundles (embedding bundle price/demand into objective functions) and productionized end-to-end CRF creation for preview and published promos. A 10,000+ shore-excursion taxonomy was delivered to underpin category-level pricing analytics for CEL.

**Focus Areas:**
Teams are focusing on prepping a Targeted Offers use-case to test Digital’s 1:1 Writeback capability, QA and production push for the bundle-aware optimizer, and Waterpark pricing elasticity analysis.

**Raw Update:**
DS Team delivered sailing lists for subsequent Royal Beach Club pricing tests, updated optimization routines to incorporate Royal Beach Club–Beverage bundles (embedding bundle price/demand into objective functions) and productionized end-to-end CRF creation for preview and published promos. A 10,000+ shore-excursion taxonomy was delivered to underpin category-level pricing analytics for CEL. Teams are focusing on prepping a Targeted Offers use-case to test Digital’s 1:1 Writeback capability, QA and production push for the bundle-aware optimizer, and Waterpark pricing elasticity analysis.

---

### PROPEL Targeted Offers (CEL)

**Date:** 2026-02-06
**Business Area:** PROPEL Targeted Offers (CEL)
**Business Project:** Offer Template Expansion

**Achievements:**
Team fixed spend-get and FreePlay/Free Gift display defects, rewrote configuration write-paths to Databricks to eliminate drops during full config refresh, and added Art offers to the new template to expand category coverage. Support was extended to 62 additional ports with improved missing-port logging, broadening addressable inventory and stabilizing fleetwide deployment.

**Focus Areas:**
Teams are focusing on diagnosing the makeover over-allocation issue and completing port rollout validation before scaling further.

**Raw Update:**
Team fixed spend-get and FreePlay/Free Gift display defects, rewrote configuration write-paths to Databricks to eliminate drops during full config refresh, and added Art offers to the new template to expand category coverage. Support was extended to 62 additional ports with improved missing-port logging, broadening addressable inventory and stabilizing fleetwide deployment. Teams are focusing on diagnosing the makeover over-allocation issue and completing port rollout validation before scaling further.

---

### Revenue Management Automation (RCI)

**Date:** 2026-02-06
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** PRE 4.0 Elasticity Enhancements

**Achievements:**
The PRE pricing optimization is now live in production, shifting from point‑elasticity approximations to direct demand‑forecast optimization. This materially reduces outlier price recommendations and positions RM to consider loosening pricing caps. Last week, Celebrity PRE price uploads were migrated off ADF and decoupled from Oracle; this week, RCI workflows completed the same transition, creating a single, unified price‑upload process for both brands.

**Raw Update:**
The PRE pricing optimization is now live in production, shifting from point‑elasticity approximations to direct demand‑forecast optimization. This materially reduces outlier price recommendations and positions RM to consider loosening pricing caps. Last week, Celebrity PRE price uploads were migrated off ADF and decoupled from Oracle; this week, RCI workflows completed the same transition, creating a single, unified price‑upload process for both brands.

---

### Revenue Management Automation (SSC)

**Date:** 2026-02-06
**Business Area:** Revenue Management Automation (SSC)
**Business Project:** A/B Testing Framework

**Achievements:**
Team delivered a voyage- and farecode-specific business-rule framework so PRE can run the upper-cabin A/B test without disrupting the current test; PRE was refactored to centralize controls and improve readability, and a unit-testing harness for the universal A/B framework was initiated with synthetic data.

**Focus Areas:**
Teams are focusing on expanding unit tests, hardening rules in recurring PRE jobs, and preparing the upper-cabin A/B test execution.

**Raw Update:**
Team delivered a voyage- and farecode-specific business-rule framework so PRE can run the upper-cabin A/B test without disrupting the current test; PRE was refactored to centralize controls and improve readability, and a unit-testing harness for the universal A/B framework was initiated with synthetic data. Teams are focusing on expanding unit tests, hardening rules in recurring PRE jobs, and preparing the upper-cabin A/B test execution.

---

### Supply Chain Optimization

**Date:** 2026-02-06
**Business Area:** Supply Chain Optimization
**Business Project:** CocoCay Integration and Guardrails

**Achievements:**
Team completed GitHub migration with Copilot code-review integration, created an order-creation snapshot for Beyond procurement, expanded data through February 2025, and delivered venue-level predictions plus four new order calculations.

**Focus Areas:**
Teams are focusing on automating “new-ship” classification with a 3-month limit, sister-ship itinerary comparisons with guardrails for destination changes, and fixing a January reporting edge case with conditional logic.

**Raw Update:**
Team completed GitHub migration with Copilot code-review integration, created an order-creation snapshot for Beyond procurement, expanded data through February 2025, and delivered venue-level predictions plus four new order calculations. Teams are focusing on automating “new-ship” classification with a 3-month limit, sister-ship itinerary comparisons with guardrails for destination changes, and fixing a January reporting edge case with conditional logic.

---

### Win-on-Waste (Hotel Operations)

**Date:** 2026-02-06
**Business Area:** Win-on-Waste (Hotel Operations)
**Business Project:** Forecasting Pipeline Expansion

**Achievements:**
Team shipped a cold-start pipeline module to handle last-minute itinerary changes, preserving forecast quality under tight timelines. Effect-size and paradox analyses (Cohen’s d, Cliff’s Delta, Simpson’s Paradox) exposed meaningful segment-level differences during holidays that were masked in aggregates.

**Focus Areas:**
Teams are focusing on clustering-based segmentation in the interport pipeline to improve forecast accuracy.

**Raw Update:**
Team shipped a cold-start pipeline module to handle last-minute itinerary changes, preserving forecast quality under tight timelines. Effect-size and paradox analyses (Cohen’s d, Cliff’s Delta, Simpson’s Paradox) exposed meaningful segment-level differences during holidays that were masked in aggregates. Teams are focusing on clustering-based segmentation in the interport pipeline to improve forecast accuracy.

---

## Excited

### AXIOM

**Date:** 2026-02-06
**Business Area:** AXIOM
**Business Project:** Division-Level Medallia Reports

**Achievements:**
Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal): DS Team integrated Azure batch processing for metadata extraction, prepared division-level topics for Silversea emails, and sent draft detractor reports to RCI/CEL brands. A critical bug in the NPS-Drivers pipeline was fixed, and three years of port-level weather data were integrated to strengthen topic and sentiment context.

**Focus Areas:**
Teams are focusing on finalizing weekly Guest Strategy email automation, enhancing the Royal Beach Club recap with dashboard data, investigating Medallia discrepancies blocking port reports, and advancing the NPS target-setting pipeline.

**Raw Update:**
Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal): DS Team integrated Azure batch processing for metadata extraction, prepared division-level topics for Silversea emails, and sent draft detractor reports to RCI/CEL brands. A critical bug in the NPS-Drivers pipeline was fixed, and three years of port-level weather data were integrated to strengthen topic and sentiment context. Teams are focusing on finalizing weekly Guest Strategy email automation, enhancing the Royal Beach Club recap with dashboard data, investigating Medallia discrepancies blocking port reports, and advancing the NPS target-setting pipeline.

---

### Contact Center Optimization & Automation

**Date:** 2026-02-06
**Business Area:** Contact Center Optimization & Automation
**Business Project:** Workforce Planning Tool

**Achievements:**
CCAS Team secured system access and completed onboarding for two hires, delivered Cresta pilot dashboard updates with performance analysis, and demoed a GenAI IVR prototype with improved intents and multi-agent orchestration. Development work progressed on Copilot migration and Guest Profile API integration. Workforce Planning Forecasting results by the DS Team showed >5% monthly improvement for North America and a stakeholder presentation was delivered.

**Focus Areas:**
Teams are focusing on building Cresta data governance (ERD, ETLs), IVR-to-SMS deflection, UAT for Copilot agents, and workforce-planning enhancements including Celebrity dataset build-out.

**Raw Update:**
CCAS Team secured system access and completed onboarding for two hires, delivered Cresta pilot dashboard updates with performance analysis, and demoed a GenAI IVR prototype with improved intents and multi-agent orchestration. Development work progressed on Copilot migration and Guest Profile API integration. Workforce Planning Forecasting results by the DS Team showed >5% monthly improvement for North America and a stakeholder presentation was delivered. Teams are focusing on building Cresta data governance (ERD, ETLs), IVR-to-SMS deflection, UAT for Copilot agents, and workforce-planning enhancements including Celebrity dataset build-out.

---

### Customer Lifetime Value (Corporate Planning)

**Date:** 2026-02-06
**Business Area:** Customer Lifetime Value (Corporate Planning)
**Business Project:** CLTV-Drivers Model Development

**Achievements:**
DS Team received all required datasets from Revenue Planning and pivoted to a demand forecasting model with confidence scores; competitor and internal benchmark data were cleaned and validated, and baseline modeling initiated alongside macroeconomic indicator tests.

**Focus Areas:**
Teams are focusing on integrating macro indicators, benchmarking the baseline, and continuing alignment with Planning and Analytics.

**Raw Update:**
DS Team received all required datasets from Revenue Planning and pivoted to a demand forecasting model with confidence scores; competitor and internal benchmark data were cleaned and validated, and baseline modeling initiated alongside macroeconomic indicator tests. Teams are focusing on integrating macro indicators, benchmarking the baseline, and continuing alignment with Planning and Analytics.

---

### Customer Targeting (E-Commerce)

**Date:** 2026-02-06
**Business Area:** Customer Targeting (E-Commerce)
**Business Project:** Booking Propensity Models

**Achievements:**
DS Team ingested the latest Epsilon data (adding two spend categories), completed the Booking Status feature now included across predictions, and implemented caching that materially improved performance. Defects affecting the audience calculator, model insights, and training reports were resolved.

**Focus Areas:**
Teams are focusing on restoring sailing-propensity dashboards and refining ETL and data-ingestion strategy for upcoming features.

**Raw Update:**
DS Team ingested the latest Epsilon data (adding two spend categories), completed the Booking Status feature now included across predictions, and implemented caching that materially improved performance. Defects affecting the audience calculator, model insights, and training reports were resolved. Teams are focusing on restoring sailing-propensity dashboards and refining ETL and data-ingestion strategy for upcoming features.

---

### Hybris Product Recommendations (Digital)

**Date:** 2026-02-06
**Business Area:** Hybris Product Recommendations (Digital)
**Business Project:** Enhanced For You Recommendations

**Achievements:**
DS Team improving association-rule accuracy by segmenting on meta-product code; due to sparse baskets, graph-based approaches (bipartite graphs, community detection) are being explored to increase relevance and discovery.

**Focus Areas:**
Teams are focusing on graph-based modeling experiments and lightweight exposure attribution via a pixel for test measurement.

**Raw Update:**
DS Team improving association-rule accuracy by segmenting on meta-product code; due to sparse baskets, graph-based approaches (bipartite graphs, community detection) are being explored to increase relevance and discovery. Teams are focusing on graph-based modeling experiments and lightweight exposure attribution via a pixel for test measurement.

---

### Revenue Management Automation (CEL)

**Date:** 2026-02-06
**Business Area:** Revenue Management Automation (CEL)
**Business Project:** Category Gapping Optimization 3.0

**Achievements:**
Team presented price-optimization results with tighter bounds, implemented model substitution for Edge F, and aligned changes to PRE 4.0 data; they also advanced Category-Gapping 2.0/3.0 (method approved to allow APD deviation near true max revenue) and fixed pipeline issues to persist model predictions and features for performance tracking.

**Focus Areas:**
Teams are focusing on feature selection for Category-Gapping 3.0, revising track hit/miss logic using raw track asks, applying DART post-optimization, and validating the updated prediction tables in QA.

**Raw Update:**
Team presented price-optimization results with tighter bounds, implemented model substitution for Edge F, and aligned changes to PRE 4.0 data; they also advanced Category-Gapping 2.0/3.0 (method approved to allow APD deviation near true max revenue) and fixed pipeline issues to persist model predictions and features for performance tracking. Teams are focusing on feature selection for Category-Gapping 3.0, revising track hit/miss logic using raw track asks, applying DART post-optimization, and validating the updated prediction tables in QA.

---

_Source: 20260206 - Weekly Rafeh & Matt Updates.docx_