---
tags:
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/customer_targeting_(e-commerce)
  - business_area/hr
  - business_area/hybris_product_recommendations_(digital)
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/newbuild
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/propel_targeted_offers_(cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/supply_chain_optimization
  - business_area/win-on-waste_(hotel_operations)
  - project/advanced_modeling_development
  - project/asset_management_expansion
  - project/automated_pricing_expansion
  - project/booking_propensity_models
  - project/calendar_recommender_development
  - project/casino_spend_analysis
  - project/category_gapping_optimization_3.0
  - project/cococay_integration_and_guardrails
  - project/enhanced_negative_feedback_alerts
  - project/forecasting_pipeline_expansion
  - project/historical_data_integration
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/mycruise_product_recommender_testing
  - project/offer_personalization_enhancement
  - project/spi-guided_track_optimization
  - project/workforce_planning_tool
  - summarized
  - weekly_update
date: "2026-04-03"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - 2026-04-03

## Proud

### Marine Insights Analytics Platform (Marine Operations)

**Date:** 2026-04-03
**Business Area:** Marine Insights Analytics Platform (Marine Operations)
**Business Project:** Asset Management Expansion

**Achievements:**
. Teams identified all impacted pipelines ahead of the cutoff, replaced legacy ACS-based access with a Microsoft-supported Graph API authorization model, and coordinated with IAM and Platform Engineering to explicitly grant site-level permissions to service principals, preventing hard outages across Revenue Management, IBP, Power BI refreshes, and promotion execution workflows during a peak planning period.

**Focus Areas:**
Teams are focusing on monitoring post-migration stability, tightening permission governance, and standardizing this access pattern so future platform deprecations do not create similar enterprise-wide failure risk.

**Raw Update:**
. Teams identified all impacted pipelines ahead of the cutoff, replaced legacy ACS-based access with a Microsoft-supported Graph API authorization model, and coordinated with IAM and Platform Engineering to explicitly grant site-level permissions to service principals, preventing hard outages across Revenue Management, IBP, Power BI refreshes, and promotion execution workflows during a peak planning period. Teams are focusing on monitoring post-migration stability, tightening permission governance, and standardizing this access pattern so future platform deprecations do not create similar enterprise-wide failure risk.

---

### AXIOM

**Date:** 2026-04-03
**Business Area:** AXIOM
**Business Project:** Enhanced Negative Feedback Alerts

**Achievements:**
Generative-AI SEATs (Hotel Ops, Consumer Insights): Teams delivered a Miami Port Operations email report and presented it to Port Services leadership, prompting a request to expand coverage to all turn ports and scale recurring operational insight delivery. Teams also enhanced the Abandoned Cart dashboard with new disruption topics (political unrest/war), standardized travel-agency naming in word clouds, added weekly/monthly trend toggles for booking factors and completion rates, and selectively translated only non-English comments to improve signal quality without inflating processing cost.

**Focus Areas:**
Teams are focusing on persisting port-report outputs into a Databricks table for Power BI consumption (so analysts don’t have to replicate pipeline logic) and improving metadata/embedding architecture choices to support scalable search, clustering, and classification across unstructured feedback.

**Raw Update:**
Generative-AI SEATs (Hotel Ops, Consumer Insights): Teams delivered a Miami Port Operations email report and presented it to Port Services leadership, prompting a request to expand coverage to all turn ports and scale recurring operational insight delivery. Teams also enhanced the Abandoned Cart dashboard with new disruption topics (political unrest/war), standardized travel-agency naming in word clouds, added weekly/monthly trend toggles for booking factors and completion rates, and selectively translated only non-English comments to improve signal quality without inflating processing cost. Teams are focusing on persisting port-report outputs into a Databricks table for Power BI consumption (so analysts don’t have to replicate pipeline logic) and improving metadata/embedding architecture choices to support scalable search, clustering, and classification across unstructured feedback.

---

### Customer Targeting (E-Commerce)

**Date:** 2026-04-03
**Business Area:** Customer Targeting (E-Commerce)
**Business Project:** Booking Propensity Models

**Achievements:**
Critically, teams unlocked a high-impact EDA insight by combining booking propensity with uplift modeling, revealing that ~21% of consumers are “persuadable”, guests who sit below the booking threshold in base models but cross it once incremental lift is considered, creating a clear, data-backed path to tighter targeting, higher conversion efficiency, and reduced offer waste. Teams also completed a major QA modernization of the production pipeline and unblocked clickstream scalability by aggressively pruning ingestion to ~30 essential fields and standing up the first checkpoint table, enabling session-level feature development without overwhelming infrastructure. Expedition campaigns while remaining future-ready for CDP and Adobe Clickstream migration.

**Focus Areas:**
Teams are focusing on validating the minimum durable clickstream feature set, backtesting a January cohort using a three-month booking horizon, integrating app and web signals into propensity scoring, and expanding the same uplift-driven targeting framework to SSC marketing to support near-term Classic vs.

**Raw Update:**
Critically, teams unlocked a high-impact EDA insight by combining booking propensity with uplift modeling, revealing that ~21% of consumers are “persuadable”, guests who sit below the booking threshold in base models but cross it once incremental lift is considered, creating a clear, data-backed path to tighter targeting, higher conversion efficiency, and reduced offer waste. Teams also completed a major QA modernization of the production pipeline and unblocked clickstream scalability by aggressively pruning ingestion to ~30 essential fields and standing up the first checkpoint table, enabling session-level feature development without overwhelming infrastructure. Teams are focusing on validating the minimum durable clickstream feature set, backtesting a January cohort using a three-month booking horizon, integrating app and web signals into propensity scoring, and expanding the same uplift-driven targeting framework to SSC marketing to support near-term Classic vs. Expedition campaigns while remaining future-ready for CDP and Adobe Clickstream migration.

---

### NewBuild

**Date:** 2026-04-03
**Business Area:** NewBuild

**Achievements:**
Teams deployed a fully working Newbuild Enterprise Observatory AI application to a demo-ready state by fixing remaining bugs and implementing performance enhancements, improving stakeholder readiness for review and adoption.

**Focus Areas:**
Teams are focusing on packaging the demo into structured stakeholder workflows (including feedback capture) and validating the path to broader user access without degrading performance or governance controls.

**Raw Update:**
Teams deployed a fully working Newbuild Enterprise Observatory AI application to a demo-ready state by fixing remaining bugs and implementing performance enhancements, improving stakeholder readiness for review and adoption. Teams are focusing on packaging the demo into structured stakeholder workflows (including feedback capture) and validating the path to broader user access without degrading performance or governance controls.

---

### PCP Pricing Automation (RCI/CEL)

**Date:** 2026-04-03
**Business Area:** PCP Pricing Automation (RCI/CEL)
**Business Project:** Automated Pricing Expansion

**Achievements:**
Teams delivered an end-to-end mass promotion writeback capability to Hybris with the required auditing controls in place, enabling governed, repeatable deployment of promotions without manual setup and turning pricing/promotion recommendations into an executable revenue lever at scale. Teams also expanded promotional automation by adding shipboard promotions to the SharePoint intake sheet and code, updating SharePoint integration logic to the newer version, correcting sailing-tag extraction to preserve underscores (preventing malformed promo conditions), and generating 24 test/control sailing pairs (48 sailings) to enable a Beverage PRE A/B test focused on 7N Caribbean and short Caribbean sailings in Summer 2026.

**Focus Areas:**
Teams are focusing on production rollout with Onboard Revenue teams, operational governance and monitoring for automated promo submission/approval cycles, and executing the Beverage PRE test plan using the paired-sailing framework.

**Raw Update:**
Teams delivered an end-to-end mass promotion writeback capability to Hybris with the required auditing controls in place, enabling governed, repeatable deployment of promotions without manual setup and turning pricing/promotion recommendations into an executable revenue lever at scale. Teams also expanded promotional automation by adding shipboard promotions to the SharePoint intake sheet and code, updating SharePoint integration logic to the newer version, correcting sailing-tag extraction to preserve underscores (preventing malformed promo conditions), and generating 24 test/control sailing pairs (48 sailings) to enable a Beverage PRE A/B test focused on 7N Caribbean and short Caribbean sailings in Summer 2026. Teams are focusing on production rollout with Onboard Revenue teams, operational governance and monitoring for automated promo submission/approval cycles, and executing the Beverage PRE test plan using the paired-sailing framework.

---

### PROPEL Targeted Offers (CEL)

**Date:** 2026-04-03
**Business Area:** PROPEL Targeted Offers (CEL)
**Business Project:** Offer Personalization Enhancement

**Achievements:**
Teams delivered a Q1 performance report with improved interpretability and surfaced the top blockers to executive confidence: charter sailings materially distort uplift and should be excluded by default, and Internet/Photo revenue gaps due to tagging issues materially understate total uplift (with Internet dropping beginning in January and Photo absent since January 2025). Teams also clarified that the control definition shifted when awareness offers became fleetwide, and reported that—excluding Internet and charter distortions—January showed a positive directional signal with APD uplift of approximately $0.91 driven primarily by beverage and gaming, but reconciliation gaps remain between APD and total dollars.

**Focus Areas:**
Teams are focusing on rebuilding uplift calculations starting at the sailing level, closing revenue-tagging gaps with data engineering, and reconciling APD-to-dollar math so category and total views are decision-grade.

**Raw Update:**
Teams delivered a Q1 performance report with improved interpretability and surfaced the top blockers to executive confidence: charter sailings materially distort uplift and should be excluded by default, and Internet/Photo revenue gaps due to tagging issues materially understate total uplift (with Internet dropping beginning in January and Photo absent since January 2025). Teams also clarified that the control definition shifted when awareness offers became fleetwide, and reported that—excluding Internet and charter distortions—January showed a positive directional signal with APD uplift of approximately $0.91 driven primarily by beverage and gaming, but reconciliation gaps remain between APD and total dollars. Teams are focusing on rebuilding uplift calculations starting at the sailing level, closing revenue-tagging gaps with data engineering, and reconciling APD-to-dollar math so category and total views are decision-grade.

---

### Contact Center Optimization & Automation (RCI/CEL)

**Date:** 2026-04-03
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - CTI (RCI & CEL)

**Achievements:**
Teams aligned RCI and CEL leadership that booking tracks are the primary control surface for revenue performance—tracks must reflect SPI-informed “ideal pacing,” remain dynamically consistent with demand forecasts (persistent divergence is treated as a modeling/assumption problem, not a business preference), and be coordinated with pricing to correct pace without value-destructive rate moves; teams reinforced that early-window guidance is most reliable and track targets must flex by sailing elasticity, group impacts, and booking position rather than applying one curve universally. Teams also quantified track gaps and executed fleet-scale optimization, including DP optimization, showing the business curve averaging ~11.4% builds away from optimal (MAE 0.11), with ~13% deviation under heavier-penalty error (RMSE 0.13) and a +4.9% forward bias versus optimal pacing (bias 0.049), plus an SPI factor yield PoC model indicating more far-out baseloading could be worth roughly ~$20 APD if reconciled with pricing and capacity constraints.

**Focus Areas:**
Teams are focusing on tightening SPI integration as a dynamic, booking-state-aware signal at the right granularity, closing the remaining reconciliation between capacity, pricing actions, and the optimized track shapes so recommendations are executable for near-term yield decisions.

**Raw Update:**
Teams aligned RCI and CEL leadership that booking tracks are the primary control surface for revenue performance—tracks must reflect SPI-informed “ideal pacing,” remain dynamically consistent with demand forecasts (persistent divergence is treated as a modeling/assumption problem, not a business preference), and be coordinated with pricing to correct pace without value-destructive rate moves; teams reinforced that early-window guidance is most reliable and track targets must flex by sailing elasticity, group impacts, and booking position rather than applying one curve universally. Teams also quantified track gaps and executed fleet-scale optimization, including DP optimization, showing the business curve averaging ~11.4% builds away from optimal (MAE 0.11), with ~13% deviation under heavier-penalty error (RMSE 0.13) and a +4.9% forward bias versus optimal pacing (bias 0.049), plus an SPI factor yield PoC model indicating more far-out baseloading could be worth roughly ~$20 APD if reconciled with pricing and capacity constraints. Teams are focusing on tightening SPI integration as a dynamic, booking-state-aware signal at the right granularity, closing the remaining reconciliation between capacity, pricing actions, and the optimized track shapes so recommendations are executable for near-term yield decisions.

---

### Supply Chain Optimization

**Date:** 2026-04-03
**Business Area:** Supply Chain Optimization
**Business Project:** CocoCay Integration and Guardrails

**Achievements:**
Teams delivered significant reliability and cost improvements by refactoring an 8,000+ line monolith notebook into a 9-notebook orchestrated architecture that reduced weekly runtime by ~5 hours and enables faster recovery by rerunning only failed steps rather than the full pipeline. Teams also migrated SharePoint read/write across 20+ notebooks to Graph API with end-to-end testing (protecting weekly operational runs), enhanced CocoCay demand modeling with 1-year/2-year lag features plus high-variance product tracking for before/after evaluation, and improved order-creation logic by integrating a live SharePoint file and MIN-PAR criteria to increase shipboard confidence in “actual quantity needed” outputs.

**Focus Areas:**
Teams are focusing on completing finance-tool refactor data validation, standardizing SSC bid-data ingestion across 50+ source files with inconsistent header/subheader patterns, and tightening workspace/environment hygiene so production jobs are isolated from development changes that can interrupt scheduled runs.

**Raw Update:**
Teams delivered significant reliability and cost improvements by refactoring an 8,000+ line monolith notebook into a 9-notebook orchestrated architecture that reduced weekly runtime by ~5 hours and enables faster recovery by rerunning only failed steps rather than the full pipeline. Teams also migrated SharePoint read/write across 20+ notebooks to Graph API with end-to-end testing (protecting weekly operational runs), enhanced CocoCay demand modeling with 1-year/2-year lag features plus high-variance product tracking for before/after evaluation, and improved order-creation logic by integrating a live SharePoint file and MIN-PAR criteria to increase shipboard confidence in “actual quantity needed” outputs. Teams are focusing on completing finance-tool refactor data validation, standardizing SSC bid-data ingestion across 50+ source files with inconsistent header/subheader patterns, and tightening workspace/environment hygiene so production jobs are isolated from development changes that can interrupt scheduled runs.

---

## Excited

### Contact Center Optimization & Automation (RCI/CEL)

**Date:** 2026-04-03
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Workforce Planning Tool

**Achievements:**
Teams calibrated and validated the Workforce Planning staffing model across Loyalty and Star lines of business, then executed a full all-LOB run and pushed model-derived FTE outputs into the application to replace legacy staffing inputs, improving decision confidence and reducing manual recalculation risk. Teams also hardened the app by adding three critical planning inputs (service level target, average patience time, average answer speed), fixing save logic to automatically adapt when new fields are added, and upgrading the underlying weekly/monthly forecast tables to more accurate sources.

**Focus Areas:**
Teams are focusing on building a 30-minute-granularity Erlang A model and moving to a self-service “run your own FTE” experience so planners can simulate staffing impacts directly in the app without manual scenario reruns.

**Raw Update:**
Teams calibrated and validated the Workforce Planning staffing model across Loyalty and Star lines of business, then executed a full all-LOB run and pushed model-derived FTE outputs into the application to replace legacy staffing inputs, improving decision confidence and reducing manual recalculation risk. Teams also hardened the app by adding three critical planning inputs (service level target, average patience time, average answer speed), fixing save logic to automatically adapt when new fields are added, and upgrading the underlying weekly/monthly forecast tables to more accurate sources. Teams are focusing on building a 30-minute-granularity Erlang A model and moving to a self-service “run your own FTE” experience so planners can simulate staffing impacts directly in the app without manual scenario reruns.

---

### Customer Lifetime Value (Corporate Planning)

**Date:** 2026-04-03
**Business Area:** Customer Lifetime Value (Corporate Planning)
**Business Project:** Casino Spend Analysis

**Achievements:**
Teams completed an end-to-end validation overhaul that reconciles the table journey against multiple finance and revenue sources, producing a comprehensive workbook spanning core measures (PCDs, Pax, NTR, OBR, APD) plus supplemental measures (distinct sailings, age distribution, group sizes, deployment mix, and book-to-sail density), materially strengthening trust in planning outputs. Teams also advanced competitive and long-range planning support by validating and building visuals for an MSC compendium/fleet view and producing segmented cuts for a 2040 vision analysis, including state-level sourcing distributions and fly/drive segmentation to sharpen demand scenario planning.

**Focus Areas:**
Teams are focusing on completing full 2025 actuals validation to enable the final CLV pipeline rerun and finalizing the competitive fleet capacity visuals used in strategic planning narratives.

**Raw Update:**
Teams completed an end-to-end validation overhaul that reconciles the table journey against multiple finance and revenue sources, producing a comprehensive workbook spanning core measures (PCDs, Pax, NTR, OBR, APD) plus supplemental measures (distinct sailings, age distribution, group sizes, deployment mix, and book-to-sail density), materially strengthening trust in planning outputs. Teams also advanced competitive and long-range planning support by validating and building visuals for an MSC compendium/fleet view and producing segmented cuts for a 2040 vision analysis, including state-level sourcing distributions and fly/drive segmentation to sharpen demand scenario planning. Teams are focusing on completing full 2025 actuals validation to enable the final CLV pipeline rerun and finalizing the competitive fleet capacity visuals used in strategic planning narratives.

---

### HR

**Date:** 2026-04-03
**Business Area:** HR

**Achievements:**
Teams advanced an HR demand forecasting initiative by drafting a sCAR to replace an Excel-based workforce planning workflow with an automated planning tool spanning ~750 positions and ~100,000 crew members across brands, targeting faster refresh cadence, improved auditability, and earlier staffing risk identification. The current workflow consumes ~7–12 hours every two weeks across data assembly and manual adjustment cycles. Leadership direction is to position this as a full CAR with clear scope, capitalizable asset definition, and success criteria rather than an exploratory side effort.

**Focus Areas:**
Teams are focusing on tightening MVP scope versus an over-broad deliverable list, validating data readiness and ownership with People Analytics/Data Engineering, and finalizing mid-April submission materials with explicit forecast-vs-actual validation and dependency mitigation.

**Raw Update:**
Teams advanced an HR demand forecasting initiative by drafting a sCAR to replace an Excel-based workforce planning workflow with an automated planning tool spanning ~750 positions and ~100,000 crew members across brands, targeting faster refresh cadence, improved auditability, and earlier staffing risk identification. The current workflow consumes ~7–12 hours every two weeks across data assembly and manual adjustment cycles. Leadership direction is to position this as a full CAR with clear scope, capitalizable asset definition, and success criteria rather than an exploratory side effort. Teams are focusing on tightening MVP scope versus an over-broad deliverable list, validating data readiness and ownership with People Analytics/Data Engineering, and finalizing mid-April submission materials with explicit forecast-vs-actual validation and dependency mitigation.

---

### Hybris Product Recommendations (Digital)

**Date:** 2026-04-03
**Business Area:** Hybris Product Recommendations (Digital)
**Business Project:** MyCruise Product Recommender Testing

**Achievements:**
Teams expanded the Apriori “frequently bought together” recommender to new product categories in dev and built a Databricks Apps + Next.js simulator to visually test recommendation API outputs, while documenting that missing front-end/model telemetry currently blocks controlled A/B testing and production observability.

**Focus Areas:**
Teams are focusing on resolving database throughput constraints with the platform team, securing an instrumentation path to identify which models are live and which front-end experiences call them, and completing production integration for the expanded Apriori outputs and Calendar experience.

**Raw Update:**
Teams expanded the Apriori “frequently bought together” recommender to new product categories in dev and built a Databricks Apps + Next.js simulator to visually test recommendation API outputs, while documenting that missing front-end/model telemetry currently blocks controlled A/B testing and production observability. Teams are focusing on resolving database throughput constraints with the platform team, securing an instrumentation path to identify which models are live and which front-end experiences call them, and completing production integration for the expanded Apriori outputs and Calendar experience.

---

### Marine Insights Analytics Platform (Marine Operations)

**Date:** 2026-04-03
**Business Area:** Marine Insights Analytics Platform (Marine Operations)
**Business Project:** Historical Data Integration

**Achievements:**
Teams aligned external and internal partners on two high-impact paths: a proof of concept to take over legacy Eniram IoT server capabilities and a plan to replace a legacy energy management application with MIAP as a real-time onboard streaming and ML-enriched application, with early targeting discussions tied to a 2027 ship timeline and associated funding path. Teams also progressed foundational platform work by extracting historical Hull Performance Platform tag data into downstream Silver tables, continuing REST API cost-management implementation, fixing a long-failing deployment-profile ETL job in production, and expanding core pipelines (including adding SSC ships into a foundational pipeline and exposing additional SFOC figures via the MIAP API).

**Focus Areas:**
Teams are focusing on completing the API cost-management changes, redesigning Silver analytics where source partitioning gaps exist, and hardening the data connection between platform and MIAP application rendering to reduce failures and improve speed.

**Raw Update:**
Teams aligned external and internal partners on two high-impact paths: a proof of concept to take over legacy Eniram IoT server capabilities and a plan to replace a legacy energy management application with MIAP as a real-time onboard streaming and ML-enriched application, with early targeting discussions tied to a 2027 ship timeline and associated funding path. Teams also progressed foundational platform work by extracting historical Hull Performance Platform tag data into downstream Silver tables, continuing REST API cost-management implementation, fixing a long-failing deployment-profile ETL job in production, and expanding core pipelines (including adding SSC ships into a foundational pipeline and exposing additional SFOC figures via the MIAP API). Teams are focusing on completing the API cost-management changes, redesigning Silver analytics where source partitioning gaps exist, and hardening the data connection between platform and MIAP application rendering to reduce failures and improve speed.

---

### Revenue Management Automation (CEL)

**Date:** 2026-04-03
**Business Area:** Revenue Management Automation (CEL)
**Business Project:** Category Gapping Optimization 3.0

**Achievements:**
Teams progress on our “actual price paid” alignment analysis showing PRE’s uncapped price-change direction generally matches expected commercial actions across demand conditions (increase/hold when demand is strong, cautious moves when wins are replacement-driven, and decreases when demand underperforms), strengthening confidence that recommendations are directionally consistent at multiple rollups. Teams also advanced Category Gapping 3.0 by incorporating business-defined objectives (pricing tiers to reach desired booking shares rather than pure revenue maximization) and tightening the model behavior using confidence-interval filtering so only statistically meaningful step changes inform optimization, reducing volatility and improving interpretability.

**Focus Areas:**
Teams are focusing on backtesting the updated gapping framework for stability and integrating the agreed objective function into the optimization pipeline for controlled validation with business stakeholders.

**Raw Update:**
Teams progress on our “actual price paid” alignment analysis showing PRE’s uncapped price-change direction generally matches expected commercial actions across demand conditions (increase/hold when demand is strong, cautious moves when wins are replacement-driven, and decreases when demand underperforms), strengthening confidence that recommendations are directionally consistent at multiple rollups. Teams also advanced Category Gapping 3.0 by incorporating business-defined objectives (pricing tiers to reach desired booking shares rather than pure revenue maximization) and tightening the model behavior using confidence-interval filtering so only statistically meaningful step changes inform optimization, reducing volatility and improving interpretability. Teams are focusing on backtesting the updated gapping framework for stability and integrating the agreed objective function into the optimization pipeline for controlled validation with business stakeholders.

---

### Revenue Management Automation (RCI)

**Date:** 2026-04-03
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** SPI-guided Track Optimization

**Achievements:**
Teams progressed on our major “Sailing Environment” foundations by completing and validating Bronze and Silver layers, including append-only booking and pricing change logs, a unified sailing universe, a booking pace spine with frozen days-to-departure snapshots, and current/historical pricing tables that eliminate repeated downstream joins and enable fast, consistent analytics. Teams also (a) worked on the 7N Caribbean basket model building an end-to-end POC—pace feature engineering, decision-tree basket assignment, velocity corridor computation (P25/P50/P75), and five-category action signals (Discount/Monitor/On Track/Hold/Raise Price)—and (b) executed dynamic programming track optimization for the full fleet through April 2028 with persisted/versioned outputs to support audit and comparison.

**Focus Areas:**
Teams are focusing on using these delivered foundations to drive repeatable track/pace decisioning, validating Category Gapping outputs for production readiness, and expanding sailing-environment coverage and recalibration cadence as new markets and products are onboarded.

**Raw Update:**
Teams progressed on our major “Sailing Environment” foundations by completing and validating Bronze and Silver layers, including append-only booking and pricing change logs, a unified sailing universe, a booking pace spine with frozen days-to-departure snapshots, and current/historical pricing tables that eliminate repeated downstream joins and enable fast, consistent analytics. Teams also (a) worked on the 7N Caribbean basket model building an end-to-end POC—pace feature engineering, decision-tree basket assignment, velocity corridor computation (P25/P50/P75), and five-category action signals (Discount/Monitor/On Track/Hold/Raise Price)—and (b) executed dynamic programming track optimization for the full fleet through April 2028 with persisted/versioned outputs to support audit and comparison. Teams are focusing on using these delivered foundations to drive repeatable track/pace decisioning, validating Category Gapping outputs for production readiness, and expanding sailing-environment coverage and recalibration cadence as new markets and products are onboarded.

---

### Win-on-Waste (Hotel Operations)

**Date:** 2026-04-03
**Business Area:** Win-on-Waste (Hotel Operations)
**Business Project:** Forecasting Pipeline Expansion

**Achievements:**
Teams delivered a new specialty pipeline architecture with enhanced feature engineering and outlier detection specifically targeting the most- and least-consumed items by ship venue, improving forecast robustness where skew and sparsity are highest. Teams also created a comprehensive accuracy report using NAE (Normalized Absolute Error) with decile-based consumption volume analysis versus a simple moving-average baseline across the last three itineraries, feeding Power BI to enable stakeholder-facing dashboards and ship/venue-specific distributions, and executed focused unit testing on Interport ETL joins plus a production hotfix to the bar forecasting pipeline in response to a ship-raised incident.

**Focus Areas:**
Teams are focusing on scaling the accuracy reporting into consistent stakeholder distributions, completing deeper interport validation, and rolling the specialty pipeline improvements into broader venue coverage for sustained forecast-quality uplift.

**Raw Update:**
Teams delivered a new specialty pipeline architecture with enhanced feature engineering and outlier detection specifically targeting the most- and least-consumed items by ship venue, improving forecast robustness where skew and sparsity are highest. Teams also created a comprehensive accuracy report using NAE (Normalized Absolute Error) with decile-based consumption volume analysis versus a simple moving-average baseline across the last three itineraries, feeding Power BI to enable stakeholder-facing dashboards and ship/venue-specific distributions, and executed focused unit testing on Interport ETL joins plus a production hotfix to the bar forecasting pipeline in response to a ship-raised incident. Teams are focusing on scaling the accuracy reporting into consistent stakeholder distributions, completing deeper interport validation, and rolling the specialty pipeline improvements into broader venue coverage for sustained forecast-quality uplift.

---

## Concerned

### Hybris Product Recommendations (Digital)

**Date:** 2026-04-03
**Business Area:** Hybris Product Recommendations (Digital)
**Business Project:** Calendar Recommender Development

**Focus Areas:**
Teams surfaced a critical Postgres scaling bottleneck where Calendar recommendation loads take 20–25 minutes per table and can fail when dev and prod jobs overlap on a shared database, creating a direct reliability risk for deployment cadence and experimentation. We need help from Platform Engineering to resolve.

**Raw Update:**
Teams surfaced a critical Postgres scaling bottleneck where Calendar recommendation loads take 20–25 minutes per table and can fail when dev and prod jobs overlap on a shared database, creating a direct reliability risk for deployment cadence and experimentation. We need help from Platform Engineering to resolve.

---

### Marine Insights Analytics Platform (Marine Operations)

**Date:** 2026-04-03
**Business Area:** Marine Insights Analytics Platform (Marine Operations)
**Business Project:** Advanced Modeling Development

**Achievements:**
Teams experienced a preventable platform disruption when Databricks compute clusters failed to start in two DA2I development workspaces (dev-da2i-dbricks and dev-da2i-alpha-dbricks), causing early-morning job failures for IBP, Contact Center, WoW, and E-Commerce Customer Targeting pipelines, while other environments continued to run normally. The issue was traced to uncoordinated platform changes tied to a managed-identity security update that unintentionally disrupted storage access, highlighting that production-critical workloads are still exposed to instability when development environments are modified without isolation or change controls.

**Focus Areas:**
Teams will be focusing on enforcing strict separation between development and production workloads, moving all production jobs into isolated prod environments, tightening platform change-management expectations with Platform Engineering, and hardening workspace governance so future security or infrastructure changes cannot interrupt business-critical pipelines.

**Raw Update:**
Teams experienced a preventable platform disruption when Databricks compute clusters failed to start in two DA2I development workspaces (dev-da2i-dbricks and dev-da2i-alpha-dbricks), causing early-morning job failures for IBP, Contact Center, WoW, and E-Commerce Customer Targeting pipelines, while other environments continued to run normally. The issue was traced to uncoordinated platform changes tied to a managed-identity security update that unintentionally disrupted storage access, highlighting that production-critical workloads are still exposed to instability when development environments are modified without isolation or change controls. Teams will be focusing on enforcing strict separation between development and production workloads, moving all production jobs into isolated prod environments, tightening platform change-management expectations with Platform Engineering, and hardening workspace governance so future security or infrastructure changes cannot interrupt business-critical pipelines.

---

_Source: 20260403 - Weekly Matt & Rafeh Update.docx_