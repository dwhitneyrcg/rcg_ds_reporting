---
tags:
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/newbuild
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - project/automated_pricing_expansion
  - project/division-level_medallia_reports
  - project/elasticity_model_enhancements_(pre4.0)
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/miap_phase_iv_development
  - project/pre_4.0_elasticity_enhancements
  - summarized
  - weekly_update
date: "2025-10-10"
type: "summarized_weekly_update"
---

# Weekly Update (Summarized) - 2025-10-10

## Proud

### Contact Center Optimization & Automation (RCI/CEL)

**Date:** 2025-10-10
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - CTI (RCI & CEL)

**Achievements:**
Teams completed OFTOCX modeling and feature engineering for Royal and Celebrity brands, with productionization initiated for Royal. The Workforce Planning tool's data refresh pipeline was delivered, enabling updated visualizations for North America, and a scoping kickoff for International Markets was conducted to define next steps.

**Focus Areas:**
Teams are now building the production pipeline for Royal's lead prioritization and enhancing Workforce Planning tool features, including historical LOB displays and baseline assumptions.

**Raw Update:**
Teams completed OFTOCX modeling and feature engineering for Royal and Celebrity brands, with productionization initiated for Royal. The Workforce Planning tool's data refresh pipeline was delivered, enabling updated visualizations for North America, and a scoping kickoff for International Markets was conducted to define next steps. Teams are now building the production pipeline for Royal's lead prioritization and enhancing Workforce Planning tool features, including historical LOB displays and baseline assumptions.

---

### Marine Insights Analytics Platform (Marine Operations)

**Date:** 2025-10-10
**Business Area:** Marine Insights Analytics Platform (Marine Operations)
**Business Project:** MIAP Phase IV Development

**Achievements:**
The MIAP Phase 4 CAR is being submitted today. The team delivered the Radiance and Millennium class power plant optimizers and completed the incinerator implementation within the Fuel Forecast API, aligning with fleet energy optimization goals. Compatibility updates to legacy energy monitoring code, along with anomaly investigations and coordination on hull coating activities, further enhanced monitoring reliability and propulsion accuracy. Active work includes cybersecurity improvements, anomaly resolutions, fuel forecast comparison platform development, and ongoing performance tuning for predictive analytics. Merge Recommendation Engine: The team delivered a Merge Recommendation Engine framework that validates Informatica’s proposed merges for high-value RCG customers using a hybrid AI approach—ML segmentation, vector similarity, LLM judgment, and business rules. Our recommender confidently recommended over 350K merges, validating more than 50% of Informatica’s suggestions, with Bijay’s MDM team in Manila manually reviewing results. While batch merging is currently paused due to a cross-reference issue under review by MDM/IT, the framework will prove critical in reducing error margins in customer record consolidation.

**Raw Update:**
The MIAP Phase 4 CAR is being submitted today. The team delivered the Radiance and Millennium class power plant optimizers and completed the incinerator implementation within the Fuel Forecast API, aligning with fleet energy optimization goals. Compatibility updates to legacy energy monitoring code, along with anomaly investigations and coordination on hull coating activities, further enhanced monitoring reliability and propulsion accuracy. Active work includes cybersecurity improvements, anomaly resolutions, fuel forecast comparison platform development, and ongoing performance tuning for predictive analytics.
Merge Recommendation Engine: The team delivered a Merge Recommendation Engine framework that validates Informatica’s proposed merges for high-value RCG customers using a hybrid AI approach—ML segmentation, vector similarity, LLM judgment, and business rules. Our recommender confidently recommended over 350K merges, validating more than 50% of Informatica’s suggestions, with Bijay’s MDM team in Manila manually reviewing results. While batch merging is currently paused due to a cross-reference issue under review by MDM/IT, the framework will prove critical in reducing error margins in customer record consolidation.

---

### PCP Pricing Automation (RCI/CEL)

**Date:** 2025-10-10
**Business Area:** PCP Pricing Automation (RCI/CEL)
**Business Project:** Automated Pricing Expansion

**Achievements:**
Teams completed enhancements to the automated promo upload workflow, including adding Qualifying Group Types conditions and fixing logic bugs for dining, loyalty, and casino promos, which were QA tested and deployed to production. Successful QA testing of promo uploads using Hybris extracts ensures readiness for P2-level implementation, with validation by digital teams confirming correct promo publishing. Teams are awaiting dashboard access approval to monitor errors from automated promo uploads, critical for ensuring robust writeback processes.

**Raw Update:**
Teams completed enhancements to the automated promo upload workflow, including adding Qualifying Group Types conditions and fixing logic bugs for dining, loyalty, and casino promos, which were QA tested and deployed to production. Successful QA testing of promo uploads using Hybris extracts ensures readiness for P2-level implementation, with validation by digital teams confirming correct promo publishing. Teams are awaiting dashboard access approval to monitor errors from automated promo uploads, critical for ensuring robust writeback processes.

---

### Revenue Management Automation (RCI)

**Date:** 2025-10-10
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** PRE 4.0 Elasticity Enhancements

**Achievements:**
Teams deployed GTY-LEAD 2.0 to production, enhancing sailing-level demand adjustments and optimizing pricing gaps for 64% of sailings. PRE 4.0 update, which includes elasticity enhanced recommendations and better pricing recommendation logic, was also deployed with new fallback logic to address zero track issues. The team did not observe any fall off in the quantity of recommendations being sent to AS400 (i.e. no noticeable affects on biz rules or analyst pause actions), and the error rate (stale, above threshold, etc.) and remained below our target of < 1% weekly.

**Focus Areas:**
Teams are now resolving flagged PRE recommendations, integrating occupancy data from VPS into PRE recommendations, enhancing the weekly demand estimation framework, and stabilizing CICD pipelines with Databricks Asset Bundles.

**Raw Update:**
Teams deployed GTY-LEAD 2.0 to production, enhancing sailing-level demand adjustments and optimizing pricing gaps for 64% of sailings. PRE 4.0 update, which includes elasticity enhanced recommendations and better pricing recommendation logic, was also deployed with new fallback logic to address zero track issues. The team did not observe any fall off in the quantity of recommendations being sent to AS400 (i.e. no noticeable affects on biz rules or analyst pause actions), and the error rate (stale, above threshold, etc.) and remained below our target of < 1% weekly. Teams are now resolving flagged PRE recommendations, integrating occupancy data from VPS into PRE recommendations, enhancing the weekly demand estimation framework, and stabilizing CICD pipelines with Databricks Asset Bundles.

---

### Revenue Management Automation (CEL)

**Date:** 2025-10-10
**Business Area:** Revenue Management Automation (CEL)
**Business Project:** Elasticity Model Enhancements (PRE4.0)

**Achievements:**
Teams completed the price upload refactor and Groups berthing transfer updates in Databricks after resolving technical issues, enabling faster inventory corrections and automation enhancements. Team also presented the new elasticity model (PRE4.0) to CEL Leadership, who approved its integration into CEL PRE after seeing a ~10% error reduction in Alaska 7N and Europe. Further iteration is needed for Short Caribbean and other smaller metas. Testing for the GTY-LEAD 2.0 model is in QA with significant progress made in improving CEL sailing predictions, particularly addressing demand variability across individual sailings. Teams are focused on refining elasticity model enhancements with dynamic features, resolving residual prediction errors in new demand models, and progressing on the Dual inventory optimization initiative.

**Raw Update:**
Teams completed the price upload refactor and Groups berthing transfer updates in Databricks after resolving technical issues, enabling faster inventory corrections and automation enhancements. Team also presented the new elasticity model (PRE4.0) to CEL Leadership, who approved its integration into CEL PRE after seeing a ~10% error reduction in Alaska 7N and Europe. Further iteration is needed for Short Caribbean and other smaller metas.  Testing for the GTY-LEAD 2.0 model is in QA with significant progress made in improving CEL sailing predictions, particularly addressing demand variability across individual sailings. Teams are focused on refining elasticity model enhancements with dynamic features, resolving residual prediction errors in new demand models, and progressing on the Dual inventory optimization initiative.

---

## Excited

### AXIOM

**Date:** 2025-10-10
**Business Area:** AXIOM
**Business Project:** Division-Level Medallia Reports

**Achievements:**
Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal): Teams aligned on metadata delivery for division-level reports, with a framework enabling scalability across unstructured datasets scheduled for early November. Fleet-wide NPS trends continue to improve, but the target-setting model is underperforming and being refined to address inaccurate forward estimations.

**Focus Areas:**
Teams are focusing on implementing the drivers model with a PoC dashboard and delivering division-specific Medallia reports in December.

**Raw Update:**
Generative-AI SEATs (Hotel Ops, Consumer Insights, Legal): Teams aligned on metadata delivery for division-level reports, with a framework enabling scalability across unstructured datasets scheduled for early November. Fleet-wide NPS trends continue to improve, but the target-setting model is underperforming and being refined to address inaccurate forward estimations. Teams are focusing on implementing the drivers model with a PoC dashboard and delivering division-specific Medallia reports in December.

---

### New Build

**Date:** 2025-10-10
**Business Area:** New Build

**Achievements:**
New AI solutions will be presented to Newbuild leadership at a workshop next week. Prior to the workshop, a survey to the entire Newbuild department will be sent out to collect AI use case ideas.

**Raw Update:**
New AI solutions will be presented to Newbuild leadership at a workshop next week. Prior to the workshop, a survey to the entire Newbuild department will be sent out to collect AI use case ideas.

---

_Source: 20251010 - Weekly Matt and Rafeh Updates.docx_