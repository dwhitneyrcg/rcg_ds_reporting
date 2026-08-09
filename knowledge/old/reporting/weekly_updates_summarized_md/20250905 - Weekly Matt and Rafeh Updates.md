---
tags:
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/propel_targeted_offers_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/supply_chain_optimization
  - project/hvac_diagnostics_&_anomaly_detection
  - project/inventory_optimization_for_silversea
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/measurement_refinement
  - project/nps_drivers_analysis_for_alert_system
  - project/spi-guided_track_optimization
  - summarized
  - weekly_update
date: "2025-09-05"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - 2025-09-05

## Proud

### Contact Center Optimization & Automation (RCI/CEL)

**Date:** 2025-09-05
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - CTI (RCI & CEL)

**Achievements:**
DS Team resolved two critical bugs in the CTI lead scoring system, stabilizing RCI conversion rates to align with historical performance.

**Focus Areas:**
Team is now monitoring model performance and experimenting with incorporating call transcripts into lead scoring.

**Raw Update:**
DS Team resolved two critical bugs in the CTI lead scoring system, stabilizing RCI conversion rates to align with historical performance. Team is now monitoring model performance and experimenting with incorporating call transcripts into lead scoring.

---

### AXIOM

**Date:** 2025-09-05
**Business Area:** AXIOM
**Business Project:** NPS Drivers Analysis for Alert System

**Achievements:**
Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal): DS Team delivered a preliminary Medallia report featuring enhanced demographic breakouts, including Nationalities, Generations, Load Factor, and family-specific aggregations. Discussions were held to refine department-specific reporting, automate guest log integration, and explore new use cases for email automation to address guest product inquiries.

**Focus Areas:**
Teams are focusing on deploying classifier models for production, adapting NPS driver thresholds for alerting, and advancing department-specific email customizations.

**Raw Update:**
Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal): DS Team delivered a preliminary Medallia report featuring enhanced demographic breakouts, including Nationalities, Generations, Load Factor, and family-specific aggregations. Discussions were held to refine department-specific reporting, automate guest log integration, and explore new use cases for email automation to address guest product inquiries. Teams are focusing on deploying classifier models for production, adapting NPS driver thresholds for alerting, and advancing department-specific email customizations.

---

### Marine Insights Analytics Platform (Marine Operations)

**Date:** 2025-09-05
**Business Area:** Marine Insights Analytics Platform (Marine Operations)
**Business Project:** HVAC Diagnostics & Anomaly Detection

**Achievements:**
DS/MLOps Team addressed two power deviations this week: a 875 kW HVAC power deviation on Icon and a 350 kW AHU power deviation on Wonder. Team also resolved critical bugs in Databricks systems, restoring production jobs and simplifying asset configurations. Other advancements include GTG model completion for LNG-powered ships and completing regression model enhancements for SY-revitalization weight predictions.

**Focus Areas:**
Teams are now improving ventilation anomaly detection, advancing stability modeling, and optimizing data transformations for predictive accuracy.

**Raw Update:**
DS/MLOps Team addressed two power deviations this week: a 875 kW HVAC power deviation on Icon and a 350 kW AHU power deviation on Wonder. Team also resolved critical bugs in Databricks systems, restoring production jobs and simplifying asset configurations. Other advancements include GTG model completion for LNG-powered ships and completing regression model enhancements for SY-revitalization weight predictions. Teams are now improving ventilation anomaly detection, advancing stability modeling, and optimizing data transformations for predictive accuracy.

---

### PROPEL Targeted Offers

**Date:** 2025-09-05
**Business Area:** PROPEL Targeted Offers
**Business Project:** Measurement Refinement

**Achievements:**
MLOps Teams deployed the capability to send awareness-only offers, ensuring program continuity even in scenarios without promotional budgets, and moved dynamic test-control into production, enhancing measurement precision while maintaining 100% offer coverage during sailings. Teams also provided operational support for the CEL fleet, adjusted offer deck configurations, and improved cluster data processing and memory usage. Active work includes further refinements to data shuffling techniques.

**Raw Update:**
MLOps Teams deployed the capability to send awareness-only offers, ensuring program continuity even in scenarios without promotional budgets, and moved dynamic test-control into production, enhancing measurement precision while maintaining 100% offer coverage during sailings. Teams also provided operational support for the CEL fleet, adjusted offer deck configurations, and improved cluster data processing and memory usage. Active work includes further refinements to data shuffling techniques.

---

### Supply Chain Optimization

**Date:** 2025-09-05
**Business Area:** Supply Chain Optimization
**Business Project:** Inventory Optimization for Silversea

**Achievements:**
DS Team revised SSC Order Creation code to prevent missing Delivery Date records through Q2 2026 and optimized the RCI/CEL Aggregate Bid pipeline, reducing runtime by 70% and ensuring error-free operations. Additional deliveries include updated RCI/CEL Order Creation columns for quantity calculations and initial development of Uniforms V1 with crew columns. Excited:
•Customer Lifetime Value (Corporate Planning): DS Team integrated GenAI-driven sentiment classifications from Medallia comments into ~25% of CLTV guest records. In a preliminary analysis, the team did not find a statistically meaningful relationship between guest sentiment and normalized cabin value (CLTV). •Customer Targeting (E-Commerce): DS Team restored access to critical email marketing tables, aligning on usage and confirming best practices to support more reliable data-driven customer targeting. •Hybris Product Recommendations (Digital): DS Team approved a request from Digital Engineering to adjust the MyCruise Recommender API caching layer, increasing the refresh rate to every 6 hours. •PCP Pricing Automation (RCI/CEL): DS Team presented an exploratory analysis to HotelOps Teams for Perfect Day Waterpark, recommending price adjustments based on cabin class, cruise departure location, and day type to optimize revenue opportunities. Team expanded elasticity model training for beverage packages included additional meta products. The updated timeline to complete writeback testing is before end-of-month and go-live in October. •Revenue Management Automation (CEL): DS/MLOps Teams finalized updates to Celebrity Re-Berthing Logging, improving inventory automation with revised schedules and enhanced logging for FIT GTY limits. Feature exploration for Category Gapping Optimization model was completed, introducing refined WTS bins and broader data coverage to enhance recommendations for far-out bookings. Teams finalized backtesting for the Elasticity Model, introducing prediction quality assessments and visualizations to enhance price elasticity performance evaluation.

**Focus Areas:**
Teams are now investigating pipeline bottlenecks for Uniforms, preparing for Private Destinations demand automation, and isolating issues with extended checkpoint durations. Teams are now working on predictive modeling to test for potential signals in cabin class-normalized values and further enrichment of Medallia-derived feedback for CLTV datasets. Team is now addressing a Siebel data source outage by identifying and integrating an alternative feed, enhancing ETL exception handling, and adding dependency plots for hybrid and uplift models to dashboards. Teams are now finalizing conversion and revenue impact analysis from the "Add-to-Cart" A/B test, which demonstrated strong click-through rates and significant stakeholder interest. Team is now developing an elasticity model for Perfect Day Waterpark, refining beverage package elasticity groupings, and completing promotions writeback testing with Digital. Teams are now addressing blockers for automating MTRB table updates and exploring dynamic modeling to address consistent over/under prediction for category gapping optimization.

**Raw Update:**
DS Team revised SSC Order Creation code to prevent missing Delivery Date records through Q2 2026 and optimized the RCI/CEL Aggregate Bid pipeline, reducing runtime by 70% and ensuring error-free operations. Additional deliveries include updated RCI/CEL Order Creation columns for quantity calculations and initial development of Uniforms V1 with crew columns. Teams are now investigating pipeline bottlenecks for Uniforms, preparing for Private Destinations demand automation, and isolating issues with extended checkpoint durations.
Excited:
•Customer Lifetime Value (Corporate Planning): DS Team integrated GenAI-driven sentiment classifications from Medallia comments into ~25% of CLTV guest records. In a preliminary analysis, the team did not find a statistically meaningful relationship between guest sentiment and normalized cabin value (CLTV). Teams are now working on predictive modeling to test for potential signals in cabin class-normalized values and further enrichment of Medallia-derived feedback for CLTV datasets.
•Customer Targeting (E-Commerce): DS Team restored access to critical email marketing tables, aligning on usage and confirming best practices to support more reliable data-driven customer targeting. Team is now addressing a Siebel data source outage by identifying and integrating an alternative feed, enhancing ETL exception handling, and adding dependency plots for hybrid and uplift models to dashboards.
•Hybris Product Recommendations (Digital): DS Team approved a request from Digital Engineering to adjust the MyCruise Recommender API caching layer, increasing the refresh rate to every 6 hours. Teams are now finalizing conversion and revenue impact analysis from the "Add-to-Cart" A/B test, which demonstrated strong click-through rates and significant stakeholder interest.
•PCP Pricing Automation (RCI/CEL): DS Team presented an exploratory analysis to HotelOps Teams for Perfect Day Waterpark, recommending price adjustments based on cabin class, cruise departure location, and day type to optimize revenue opportunities. Team expanded elasticity model training for beverage packages included additional meta products. Team is now developing an elasticity model for Perfect Day Waterpark, refining beverage package elasticity groupings, and completing promotions writeback testing with Digital. The updated timeline to complete writeback testing is before end-of-month and go-live in October.
•Revenue Management Automation (CEL): DS/MLOps Teams finalized updates to Celebrity Re-Berthing Logging, improving inventory automation with revised schedules and enhanced logging for FIT GTY limits. Feature exploration for Category Gapping Optimization model was completed, introducing refined WTS bins and broader data coverage to enhance recommendations for far-out bookings. Teams finalized backtesting for the Elasticity Model, introducing prediction quality assessments and visualizations to enhance price elasticity performance evaluation. Teams are now addressing blockers for automating MTRB table updates and exploring dynamic modeling to address consistent over/under prediction for category gapping optimization.

---

### Revenue Management Automation (RCI)

**Date:** 2025-09-05
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** SPI-guided Track Optimization

**Achievements:**
DS/MLOPs Teams finalized the design for a SPI Factor Model, incorporating dynamic levers and heuristic optimization approaches to improve sailing management decisions. Team validated elasticity models addressed pricing data anomalies. Active work includes ongoing testing for elasticity-based track optimizations and track optimization, PRE logic updates, productionizing updated VPS workflows, and refining the price adjustment formula based on elasticity principles.

**Raw Update:**
DS/MLOPs Teams finalized the design for a SPI Factor Model, incorporating dynamic levers and heuristic optimization approaches to improve sailing management decisions. Team validated elasticity models addressed pricing data anomalies. Active work includes ongoing testing for elasticity-based track optimizations and track optimization, PRE logic updates, productionizing updated VPS workflows, and refining the price adjustment formula based on elasticity principles.

---

_Source: 20250905 - Weekly Matt and Rafeh Updates.docx_