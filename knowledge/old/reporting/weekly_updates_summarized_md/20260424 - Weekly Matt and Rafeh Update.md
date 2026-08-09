---
tags:
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/customer_targeting_(e-commerce)
  - business_area/hr
  - business_area/hybris_product_recommendations_(digital)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/propel_targeted_offers_(cel)
  - business_area/supply_chain_optimization
  - business_area/win-on-waste_(hotel_operations)
  - project/advanced_modeling_development
  - project/cltv-drivers_model_development
  - project/division-level_medallia_reports
  - project/enhanced_for_you_recommendations
  - project/enhanced_hf&b_demand_modelling
  - project/forecasting_pipeline_expansion
  - project/loyalty_simulator_framework
  - project/measurement_refinement
  - project/offer_to_cancel_(oftocx)_model_(rci_&_cel)
  - project/perfect_day_product_pricing
  - project/workforce_planning_tool
  - summarized
  - weekly_update
date: "2026-04-24"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - 2026-04-24

## Updates

### AXIOM

**Date:** 2026-04-24
**Business Area:** AXIOM
**Business Project:** Division-Level Medallia Reports

**Achievements:**
Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal):
Delivered multiple reliability and quality fixes across Voice 360 and Medallia email streams, including resolution of venue hallucination issues, safety-comment drop-offs, and missing pre-meeting deliverables, materially improving trust in fleet-wide executive communications. Enhanced Port Email and Safety Email content consistency and indicator clarity while closing known data and prompt-engineering gaps. Teams are tightening safety guardrails, persisting all LLM outputs for retrospective QA, and extending Target Setting beyond satisfaction into onboard revenue forecasting.

**Raw Update:**
Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal):
Delivered multiple reliability and quality fixes across Voice 360 and Medallia email streams, including resolution of venue hallucination issues, safety-comment drop-offs, and missing pre-meeting deliverables, materially improving trust in fleet-wide executive communications. Enhanced Port Email and Safety Email content consistency and indicator clarity while closing known data and prompt-engineering gaps. Teams are tightening safety guardrails, persisting all LLM outputs for retrospective QA, and extending Target Setting beyond satisfaction into onboard revenue forecasting.

---

### Contact Center Optimization & Automation (RCI/CEL)

**Date:** 2026-04-24
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Workforce Planning Tool

**Achievements:**
Delivered the first end-to-end, production-scale call-volume forecasting pipeline across International and Casino markets, including full backtesting and identification of underperforming markets requiring tuning, validating readiness for workforce-planning integration. Extended the same orchestration to North America Celebrity and Royal, enabling finer LOB-level splits to improve staffing precision. Teams are finalizing market and LOB fine-tuning, updating the Workforce Planning app, and building dependency datasets for advanced simulation.

**Raw Update:**
Delivered the first end-to-end, production-scale call-volume forecasting pipeline across International and Casino markets, including full backtesting and identification of underperforming markets requiring tuning, validating readiness for workforce-planning integration. Extended the same orchestration to North America Celebrity and Royal, enabling finer LOB-level splits to improve staffing precision. Teams are finalizing market and LOB fine-tuning, updating the Workforce Planning app, and building dependency datasets for advanced simulation.

---

### Customer Targeting (E-Commerce)

**Date:** 2026-04-24
**Business Area:** Customer Targeting (E-Commerce)

**Achievements:**
Accelerated journey scoring model readiness by adding new classification features for web visits and materializing a reduced clickstream checkpoint table (raw clickstream compressed into ~60 high-value columns) designed to preserve the behavioral detail stakeholders ask for while improving usability and performance. Identified the key session-level columns needed to categorize clickstream activity—including indicators that detect device/browser shifts within a session—which improves explainability of “why a visit scored the way it did.” Also initiated governance work to validate that protected consumer classes are excluded from targeting segmentation. Teams are continuing HMM experimentation, completing audit validation, and aligning on Silversea model migration requirements.

**Raw Update:**
Accelerated journey scoring model readiness by adding new classification features for web visits and materializing a reduced clickstream checkpoint table (raw clickstream compressed into ~60 high-value columns) designed to preserve the behavioral detail stakeholders ask for while improving usability and performance. Identified the key session-level columns needed to categorize clickstream activity—including indicators that detect device/browser shifts within a session—which improves explainability of “why a visit scored the way it did.” Also initiated governance work to validate that protected consumer classes are excluded from targeting segmentation. Teams are continuing HMM experimentation, completing audit validation, and aligning on Silversea model migration requirements.

---

### Customer Lifetime Value (Corporate Planning)

**Date:** 2026-04-24
**Business Area:** Customer Lifetime Value (Corporate Planning)
**Business Project:** CLTV-Drivers Model Development

**Achievements:**
Completed executive-level metric validation using competitive fleet models, ensuring accuracy of CLV figures surfaced in senior leadership materials. Streamlined and documented the CLV ETL pipeline to formalize data requirements and improve long-term maintainability.

**Focus Areas:**
Teams are preparing a formal pull request and finalizing handoff documentation.

**Raw Update:**
Completed executive-level metric validation using competitive fleet models, ensuring accuracy of CLV figures surfaced in senior leadership materials. Streamlined and documented the CLV ETL pipeline to formalize data requirements and improve long-term maintainability. Teams are preparing a formal pull request and finalizing handoff documentation.

---

### HR

**Date:** 2026-04-24
**Business Area:** HR

**Achievements:**
Produced an initial draft CAM Capital Authorization Request anchored on enterprise demand planning and forecasting as foundational capabilities. This is a narrowing of scope after a key stakeholder decision by Angela Smith who rejected including an in-house workforce scheduling tool due to write-off risk given the possibility of adopting an off-the-shelf solution. Angela Smith’s decision to defer workforce scheduling creates a near-term dependency on GenAI CoE capacity and leaves an open strategic question on whether planning tools converge or fragment across CAM. Teams are refining scope sequencing, capitalization assumptions, and run-rate constraints to align with cost comfort thresholds (sub-$750K/year preference).

**Raw Update:**
Produced an initial draft CAM Capital Authorization Request anchored on enterprise demand planning and forecasting as foundational capabilities. This is a narrowing of scope after a key stakeholder decision by Angela Smith who rejected including an in-house workforce scheduling tool due to write-off risk given the possibility of adopting an off-the-shelf solution. Angela Smith’s decision to defer workforce scheduling creates a near-term dependency on GenAI CoE capacity and leaves an open strategic question on whether planning tools converge or fragment across CAM. Teams are refining scope sequencing, capitalization assumptions, and run-rate constraints to align with cost comfort thresholds (sub-$750K/year preference).

---

### Loyalty Program Redesign

**Date:** 2026-04-24
**Business Area:** Loyalty Program Redesign
**Business Project:** Loyalty Simulator Framework

**Achievements:**
Initiated loyalty simulator modernization with a concrete phased plan that ties scope, timing, and resourcing to business needs: retrofit RCI/CEL first to reflect current program mechanics, extend to SSC next with dedicated capacity, then transition into an ongoing scenario-analysis capability for future loyalty changes. Early delivery this week was an improved sailing-guest simulator that better predicts cabin category choice and a roadmap to shift the booking propensity model from sailing-level to category-level so outputs mirror how the program operates in practice. Teams are testing the newly integrated simulator model variations and researching improved pairing logic that matches guests to sailings based on probable trip length and historical behavior.

**Raw Update:**
Initiated loyalty simulator modernization with a concrete phased plan that ties scope, timing, and resourcing to business needs: retrofit RCI/CEL first to reflect current program mechanics, extend to SSC next with dedicated capacity, then transition into an ongoing scenario-analysis capability for future loyalty changes. Early delivery this week was an improved sailing-guest simulator that better predicts cabin category choice and a roadmap to shift the booking propensity model from sailing-level to category-level so outputs mirror how the program operates in practice. Teams are testing the newly integrated simulator model variations and researching improved pairing logic that matches guests to sailings based on probable trip length and historical behavior.

---

### Marine Insights Analytics Platform (Marine Operations)

**Date:** 2026-04-24
**Business Area:** Marine Insights Analytics Platform (Marine Operations)
**Business Project:** Advanced Modeling Development

**Achievements:**
Delivered actionable energy insights by identifying ~200kW savings opportunities in AHU areas for specific ships and engaging vessels with detailed findings, making the work directly operational rather than analytical-only. Also increased MIAP product and modeling robustness by completing a full app refactor (Next.js / FastAPI / Tailwind) and aligning that MIAP can replace embedded MIAP visualizations and export tooling in the GMO app, simplifying the user experience by redirecting users to a single canonical app. Integrated the FACTS model pipeline into the web app and implemented fallback logic to force FACTS when ships lack valid individual generator models, reducing “missing model” operational gaps. Teams are integrating the FACTS flow into the digital twin test pipeline to extend visibility into SSC ships, refining chiller and propulsion models (including outlier handling and accuracy improvements), and continuing platform performance work (e.g., partitioning improvements for Postgres reads).

**Raw Update:**
Delivered actionable energy insights by identifying ~200kW savings opportunities in AHU areas for specific ships and engaging vessels with detailed findings, making the work directly operational rather than analytical-only. Also increased MIAP product and modeling robustness by completing a full app refactor (Next.js / FastAPI / Tailwind) and aligning that MIAP can replace embedded MIAP visualizations and export tooling in the GMO app, simplifying the user experience by redirecting users to a single canonical app. Integrated the FACTS model pipeline into the web app and implemented fallback logic to force FACTS when ships lack valid individual generator models, reducing “missing model” operational gaps. Teams are integrating the FACTS flow into the digital twin test pipeline to extend visibility into SSC ships, refining chiller and propulsion models (including outlier handling and accuracy improvements), and continuing platform performance work (e.g., partitioning improvements for Postgres reads).

---

### Product Recommendations

**Date:** 2026-04-24
**Business Area:** Product Recommendations
**Business Project:** Enhanced For You Recommendations

**Achievements:**
Delivered material production readiness improvements by confirming a dedicated Postgres production instance and deploying ForYou API expansion that reduced memory pressure (95% → 52%) while adding calendar + recommendations synergies at the ETL layer—improving reliability for scaled traffic. Increased recommender model quality by completing Bayesian cross-validation optimization with a temporal split (forces forward generalization) and disabling two problematic features that were driving empty recommendations, reducing “no-result” guest experiences. Achieved a step-change in product clustering throughput and QA quality by shifting to a single one-shot GPT-5 Nano batch classification approach (large context), cutting QA disagreement (~30% → ~11%), and teeing up re-ranking as the next strategic lane by incorporating propensity scores rather than bloating base-model complexity. Teams are expanding clustering beyond ShoreX, sourcing historical catalog data, and building explainability artifacts for business users.

**Raw Update:**
Delivered material production readiness improvements by confirming a dedicated Postgres production instance and deploying ForYou API expansion that reduced memory pressure (95% → 52%) while adding calendar + recommendations synergies at the ETL layer—improving reliability for scaled traffic. Increased recommender model quality by completing Bayesian cross-validation optimization with a temporal split (forces forward generalization) and disabling two problematic features that were driving empty recommendations, reducing “no-result” guest experiences. Achieved a step-change in product clustering throughput and QA quality by shifting to a single one-shot GPT-5 Nano batch classification approach (large context), cutting QA disagreement (~30% → ~11%), and teeing up re-ranking as the next strategic lane by incorporating propensity scores rather than bloating base-model complexity. Teams are expanding clustering beyond ShoreX, sourcing historical catalog data, and building explainability artifacts for business users.

---

### PCP Pricing Automation (RCI/CEL)

**Date:** 2026-04-24
**Business Area:** PCP Pricing Automation (RCI/CEL)
**Business Project:** Perfect Day Product Pricing

**Achievements:**
Delivered multiple high-impact advancements this week. First advanced the unified “apps” strategy by aligning architecture and standing up containers for a consolidated front end spanning pricing recommendations, mass promotions, and targeted offers—this shifts the program from point solutions to a scalable platform the business can actually operate. The targeted offers UI received very positive feedback because it shows business users exactly what the guest will see, which is critical for adoption and governance of 1:1 experiences. Delivered a v1 Mass Promotions app (internally reviewed and ready to present) and materially enhanced the Targeted Offers app with validations, request logging (so users can view/clone prior submissions), and writeback to Unity Catalog across environments—improving auditability and operational reuse. Executed real production testing for the targeted-offers pilot (Android/iOS with synthetic bookings), confirmed notification + takeover messaging works, and isolated concrete defects (stale pricing cache edge case; takeover imagery on Android; CEL name/personalization still not working), turning “it doesn’t work” into an explicit fix list. Teams are finalizing Terms & Conditions population, improving takeover image quality, resolving Royal Android issues, and progressing business requirements for scaling tests (suppression, offer bank, prioritization rules) alongside legal alignment for future testing.

**Raw Update:**
Delivered multiple high-impact advancements this week. First advanced the unified “apps” strategy by aligning architecture and standing up containers for a consolidated front end spanning pricing recommendations, mass promotions, and targeted offers—this shifts the program from point solutions to a scalable platform the business can actually operate. The targeted offers UI received very positive feedback because it shows business users exactly what the guest will see, which is critical for adoption and governance of 1:1 experiences. Delivered a v1 Mass Promotions app (internally reviewed and ready to present) and materially enhanced the Targeted Offers app with validations, request logging (so users can view/clone prior submissions), and writeback to Unity Catalog across environments—improving auditability and operational reuse. Executed real production testing for the targeted-offers pilot (Android/iOS with synthetic bookings), confirmed notification + takeover messaging works, and isolated concrete defects (stale pricing cache edge case; takeover imagery on Android; CEL name/personalization still not working), turning “it doesn’t work” into an explicit fix list. Teams are finalizing Terms & Conditions population, improving takeover image quality, resolving Royal Android issues, and progressing business requirements for scaling tests (suppression, offer bank, prioritization rules) alongside legal alignment for future testing.

---

### PROPEL Targeted Offers

**Date:** 2026-04-24
**Business Area:** PROPEL Targeted Offers
**Business Project:** Measurement Refinement

**Achievements:**
Aligned stakeholders on the SSC sCAR pilot framing in response to new fare structures, clarifying guest behavior, revenue levers, and shore-excursion credit economics to de-risk future investment. For CEL, completed building a robust measurement framework sharing with business for QA and scheduling fixes to support reliable test/control attribution. Teams are hardening the measurement framework for production and preparing submission for SSC PROPEL sCAR.

**Raw Update:**
Aligned stakeholders on the SSC sCAR pilot framing in response to new fare structures, clarifying guest behavior, revenue levers, and shore-excursion credit economics to de-risk future investment. For CEL, completed building a robust measurement framework sharing with business for QA and scheduling fixes to support reliable test/control attribution. Teams are hardening the measurement framework for production and preparing submission for SSC PROPEL sCAR.

---

### Contact Center Optimization & Automation (RCI/CEL)

**Date:** 2026-04-24
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)

**Achievements:**
Improved automation stability and business trust by closing multiple high-priority process defects (including a time-zone logging discrepancy and a re-berthing automation scheduling conflict) and by delivering “how the system works” walkthroughs to make downstream effects understandable to stakeholders who rely on automation outputs. Also completed significant enhancements across baskets, track optimization, and demand-model sensitivity analysis, and materially improving interpretability of pricing recommendations. Delivered Category-Gapping and basket frameworks validated in Dev and QA with deterministic pricing signals. CEL stakeholders aligned that SPI-based booked-position benchmarking is the right anchor for promo decisions (apples-to-apples across sailings), while also explicitly deciding not to use SPI price ranges directly, shifting focus toward average prices derived from comparable builds. Teams are extending track optimization work (including sensitivity/uncertainty analysis and bounded price curve logic), refining promo/GTY datasets to quantify gaps and trade-up behavior, and continuing process hardening to prevent cross-process payload interference.

**Raw Update:**
Improved automation stability and business trust by closing multiple high-priority process defects (including a time-zone logging discrepancy and a re-berthing automation scheduling conflict) and by delivering “how the system works” walkthroughs to make downstream effects understandable to stakeholders who rely on automation outputs. Also completed significant enhancements across baskets, track optimization, and demand-model sensitivity analysis, and materially improving interpretability of pricing recommendations. Delivered Category-Gapping and basket frameworks validated in Dev and QA with deterministic pricing signals. CEL stakeholders aligned that SPI-based booked-position benchmarking is the right anchor for promo decisions (apples-to-apples across sailings), while also explicitly deciding not to use SPI price ranges directly, shifting focus toward average prices derived from comparable builds. Teams are extending track optimization work (including sensitivity/uncertainty analysis and bounded price curve logic), refining promo/GTY datasets to quantify gaps and trade-up behavior, and continuing process hardening to prevent cross-process payload interference.

---

### Supply Chain Optimization

**Date:** 2026-04-24
**Business Area:** Supply Chain Optimization
**Business Project:** Enhanced HF&B Demand Modelling

**Achievements:**
Delivered timely IBP improvements that support the BY Pilot that directly improve forecast realism and reduce operational misses: enhanced the supply consumption ratio approach using recent-voyage weighting (category-specific weights) and added a non-zero floor to prevent “zero consumption” predictions for historically ordered items—reducing stockout risk driven by modeling artifacts. Closed a major reporting delivery by implementing two additional automated spend report variants requested by stakeholders and finalizing naming convention changes via merged PRs, then moving the story to Done based on expected completion. Teams are debugging consolidated finance demand/actuals tables, validating downstream model performance impacts for uniforms ratio corrections and combinatorial features, and iterating on the beverage product-name label extraction POC based on stakeholder guidance (dataset source, taxonomy naming, active-products filtering, and next-phase rollups)

**Raw Update:**
Delivered timely IBP improvements that support the BY Pilot that directly improve forecast realism and reduce operational misses: enhanced the supply consumption ratio approach using recent-voyage weighting (category-specific weights) and added a non-zero floor to prevent “zero consumption” predictions for historically ordered items—reducing stockout risk driven by modeling artifacts. Closed a major reporting delivery by implementing two additional automated spend report variants requested by stakeholders and finalizing naming convention changes via merged PRs, then moving the story to Done based on expected completion. Teams are debugging consolidated finance demand/actuals tables, validating downstream model performance impacts for uniforms ratio corrections and combinatorial features, and iterating on the beverage product-name label extraction POC based on stakeholder guidance (dataset source, taxonomy naming, active-products filtering, and next-phase rollups)

---

### Win-on-Waste (Hotel Operations)

**Date:** 2026-04-24
**Business Area:** Win-on-Waste (Hotel Operations)
**Business Project:** Forecasting Pipeline Expansion

**Achievements:**
Reduced unnecessary compute spend and improved reliability by implementing a smart gating module that skips interport runs when no interport sailings exist, while still running both pipelines when interport + regular sailings are present within a 7-day horizon—this is cost control without sacrificing coverage. Prevented forecast duplication and data contamination by adding upstream validation that detects duplicate sailings incorrectly labeled as both interport and regular and deterministically keeps the correct record. Restored forecast completeness by fixing critical issues across 139 bar venues, and completed end-to-end integration testing for the Interport Specialty pipeline with a planned production deployment aligned to operational deployment rules. Teams are building a configuration-driven flexible meal-period framework to enable operational hour changes without code releases and beginning GenAI Genie + knowledge base discussions for next phases while scaling down resourcing.

**Raw Update:**
Reduced unnecessary compute spend and improved reliability by implementing a smart gating module that skips interport runs when no interport sailings exist, while still running both pipelines when interport + regular sailings are present within a 7-day horizon—this is cost control without sacrificing coverage. Prevented forecast duplication and data contamination by adding upstream validation that detects duplicate sailings incorrectly labeled as both interport and regular and deterministically keeps the correct record. Restored forecast completeness by fixing critical issues across 139 bar venues, and completed end-to-end integration testing for the Interport Specialty pipeline with a planned production deployment aligned to operational deployment rules. Teams are building a configuration-driven flexible meal-period framework to enable operational hour changes without code releases and beginning GenAI Genie + knowledge base discussions for next phases while scaling down resourcing.

---

_Source: 20260424 - Weekly Matt and Rafeh Update.docx_