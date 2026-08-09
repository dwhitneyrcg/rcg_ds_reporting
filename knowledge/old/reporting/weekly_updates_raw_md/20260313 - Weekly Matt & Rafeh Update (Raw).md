---
tags:
  - aagam_shah
  - arya_cheeti
  - ayon_ghosh
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/customer_targeting_(e-commerce)
  - business_area/hybris_product_recommendations_(digital)
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/newbuild
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/propel_targeted_offers_(cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/supply_chain_optimization
  - business_area/win-on-waste_(hotel_operations)
  - caleb_sharkey
  - camila_aichele
  - carlos_gonzalez_andarcio
  - cristian_villamarin-villamil
  - erick_alfaro
  - evan_mcfall
  - glen-erik_cortez
  - ignacio_villasmil
  - jesse_bausell
  - lamis_amer
  - mahshad_shariatnasab
  - mert_ersoz
  - michelle_manfrini
  - project/asset_management_expansion
  - project/automated_pricing_expansion
  - project/beverage_package_optimization
  - project/booking_propensity_models
  - project/calendar_recommender_development
  - project/category_gapping_optimization_3.0
  - project/cross-brand_credit_card_strategy
  - project/forecasting_pipeline_expansion
  - project/gty-lead_fare_optimization_model
  - project/historical_data_integration
  - project/marine_safety_analytics
  - project/measurement_refinement
  - project/min_max_par-level_tools
  - project/nps_drivers_analysis_for_alert_system
  - project/offer_to_cancel_(oftocx)_model_(rci_&_cel)
  - project/pre_4.0_elasticity_enhancements
  - project/spi-guided_track_optimization
  - project/workforce_planning_tool
  - raw
  - reza_bahadori
  - weekly_update
date: "2026-03-13"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2026-03-13

## Update 1

**Date:** 2026-03-13
**Business Area:** E-Commerce
**Business Project:** Booking Propensity Models
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]]

### Summarized Update

The team fixed a join explosion bug in the ETL training pipeline, continued QA integration testing of refactored code, and advanced migration of MLflow registration to the Databricks Unity Catalog API. Table update functions were refactored to improve source-table visibility and refresh tracking while reducing runtime to about two minutes. For modeling, new Journey Score features were engineered from available web data, but deeper clickstream work remains blocked by missing business definitions and access gaps.

### Raw Update

The team fixed a join explosion bug in the ETL training pipeline, continued QA integration testing of refactored code, and advanced migration of MLflow registration to the Databricks Unity Catalog API. Table update functions were refactored to improve source-table visibility and refresh tracking while reducing runtime to about two minutes. For modeling, new Journey Score features were engineered from available web data, but deeper clickstream work remains blocked by missing business definitions and access gaps. EDA on app data showed promise for booking propensity, especially around total app interactions and post-voyage app usage, but also identified temporal leakage risk because app install timestamps are unavailable. A follow-up meeting is scheduled to resolve ID alignment for booking and web propensity joins, after which deeper analysis will continue. Catalog feature pull requests have been updated and are now awaiting approval.

---

## Update 2

**Date:** 2026-03-13
**Business Area:** Supply Chain
**Business Project:** Min/Max PAR-Level Tools
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Work focused on order creation and finance tool orchestration, overwrite accuracy, allocation logic, and model quality improvements. Min/Max Par was separated into its own orchestration step so it updates with new predictions, with follow-on work to improve volatility reporting and prevent redundant same-day refresh comparisons. Current-month overwrite logic improved materially, moving from roughly 50 percent correct coverage to about a 99 percent match rate, and ESG handling is being corrected to eliminate shipboard discrepancies.

### Raw Update

Work focused on order creation and finance tool orchestration, overwrite accuracy, allocation logic, and model quality improvements. Min/Max Par was separated into its own orchestration step so it updates with new predictions, with follow-on work to improve volatility reporting and prevent redundant same-day refresh comparisons.
Current-month overwrite logic improved materially, moving from roughly 50 percent correct coverage to about a 99 percent match rate, and ESG handling is being corrected to eliminate shipboard discrepancies. The importance of this is that when we update forecasts weekly, not all of the department-level forecasts were updating. This bug has been fixed.
Finance-tool enhancements to add Actual Cost Center and Actual GL Account are in progress, but catalyst data and ALT_ADDRESS_2 formatting issues are still causing nulls and must be resolved upstream. Daily requisition analysis builds were advanced for both overwrite-based predictions and actual consumption-report sources, including sea versus port day logic, guest-count metrics, prior-year variance, and downstream output tables. Additional work progressed on override tracking, guest-count visibility in snapshot tables, APD and weighted cost movement logic, CocoCay monthly PCD fraction recalculation, and port/sea daily spend adjustment for future sailings.
Model enhancement work continues for Medical AI after diagnostics confirmed severe under-prediction bias, extreme sparsity, and strong record-count sensitivity. The remediation plan includes new feature engineering, bias correction, threshold adjustment, and more granular correction by subcategory and record-count bucket. For Silversea crew count modeling, Fidelio was integrated into validations but exposed material contract-calculation discrepancies, so the team is escalating upstream data quality issues while simplifying the path to Phase 2 with more practical interim models. Beyond Pilot work also advanced: future-voyage consumption allocation logic was aligned with stakeholders, the weekly model training date migration was scoped across 12 notebooks for targeted productionization on 3/21, refactoring of the largest notebook is continuing in a sequential validation approach, and the Beyond Master Order Template comparison table was delivered and is now being revalidated after feedback.

---

## Update 3

**Date:** 2026-03-13
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

The Workforce Planning application for North America was expanded to include Celebrity, creating a unified app for Royal and Celebrity. Users can now select brand from the home screen and route into the appropriate brand-specific experience. Celebrity currently supports historical data visualization, with forecasting to follow in a future phase.

### Raw Update

The Workforce Planning application for North America was expanded to include Celebrity, creating a unified app for Royal and Celebrity. Users can now select brand from the home screen and route into the appropriate brand-specific experience. Celebrity currently supports historical data visualization, with forecasting to follow in a future phase. Workforce planning is still in QA, not in production. For International and Casino, the team refined the strategy for user adjustments to forecasted call volume, including both market-level alpha adjustments and a market-plus-LOB framework that must preserve total market forecast consistency. The team also completed the disaggregation methodology from market to brand to department using recent and prior-year proportions to support more stable downstream staffing and planning. The next step is building the adjustment workflow into the application.
Raw Reporting
Workforce Planning – North America (Celebrity)
This week, we successfully updated the Workforce Planning App to include the Celebrity view. We now have a unified Workforce Planning platform for North America, with both Royal and Celebrity accessible within a single application.
The updated home screen allows users to select the brand they want to work with. After selection, users are automatically routed to the appropriate brand-specific section, where all relevant modules are displayed.
For Celebrity:
Only historical data visualization is available at this stage.
The forecasting module has not yet been implemented and will be added in a future phase.
Completed this week:
Home page integration for Celebrity
Celebrity data visualization section within the app
Workforce Planning – International and Casino –
Managing Adjustments to Forecasted Call Volume in the International & Casino Application
Meeting: Met with Nico to refine the adjustment strategy and confirm the design direction.
Strategic Framework 1: Market-Level Forecast Adjustment
Concept: Users view the raw forecast at the market level and apply alpha multipliers (scaling factors) to adjust each market independently. Adjusted outcomes are saved as versioned snapshots for tracking and comparison. This approach allows for Market-level flexibility without introducing inconsistencies at lower levels
Strategic Framework 2: Market and LOB-Level Adjustment – The Core Challenge
The Constraint: The sum of all department (LOB) forecasts within a market must always equal the total market forecast.
This creates a conservation rule:
If one department is adjusted upward, another must decrease to maintain balance.
Any LOB-level adjustment must remain mathematically tied to the market total.
This is the main complexity in supporting LOB-level adjustments in the app while keeping the forecast internally consistent.
Call Forecast Disaggregation Process: Market → Brand → Department (LOB)
The Nico team generates the International call volume forecast at the market level across 11 markets. However, Workforce Planning requires deeper granularity at both brand and department (LOB) levels.
To disaggregate the forecast, we calculated distribution proportions (%) at three levels:
Market – share across all international markets
Market × Brand – brand mix within each market
Market × Department (LOB) – LOB mix within each market
Methodology:
Compared the most recent 3 full months with the same 3 months last year to identify trends
Applied a blended average of both periods for stability
Defaulted to recent-only proportions where historical data is unavailable
Used the final proportions to break down the market-level forecast into Brand and LOB detail
This ensures a stable, trend-aware distribution model that supports downstream staffing and planning needs.

Next Steps
Developing the app section for call volume forecast adjustments, incorporating the market → brand → LOB flow and the constraint logic.

---

## Update 4

**Date:** 2026-03-13
**Business Area:** CLV
**Business Project:** Cross-Brand Credit Card Strategy
**People:** [[caleb_sharkey/overview_caleb_sharkey|Caleb Sharkey]]

### Summarized Update

The team supported the MSC deep dive through visualizations on port control, normalized pricing, and commercial capability research. Work also began on cleaning and transforming competitor pricing data from bots, which is important for measuring the competitive environment but requires careful validation against SEC-reported competitor revenue, delicate imputation across 20+ brands and five sail years, and strict matching to confirmed deployed sailings because the source data is incomplete and noisy.

### Raw Update

The team supported the MSC deep dive through visualizations on port control, normalized pricing, and commercial capability research. Work also began on cleaning and transforming competitor pricing data from bots, which is important for measuring the competitive environment but requires careful validation against SEC-reported competitor revenue, delicate imputation across 20+ brands and five sail years, and strict matching to confirmed deployed sailings because the source data is incomplete and noisy.

---

## Update 5

**Date:** 2026-03-13
**Business Area:** RCI Revenue Management
**People:** Unidentified

### Summarized Update

Eswar & Javier
RCI Revenue Management

### Raw Update

Eswar & Javier
RCI Revenue Management

---

## Update 6

**Date:** 2026-03-13
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Reviewed PRE output data validation process
Updated the framework to accommodate additional checks needed
Ops Support: (Eswar)
Productionized CEL T4 track workflow
Evaluating strategy in Hosting stating Web app vs docker based solution for a  RM application
PR review and CI/CD monitoring
Automated Code Review: (Javier)
Refined dashboard for monthly review
SQL logic to reflect the latest repository issue snapshot. Implemented logic to handle duplicate violations correctly. Built measures for issue counts by rule_code at the latest selected date.

### Raw Update

Reviewed PRE output data validation process
Updated the framework to accommodate additional checks needed
Ops Support: (Eswar)
Productionized CEL T4 track workflow
Evaluating strategy in Hosting stating Web app vs docker based solution for a  RM application
PR review and CI/CD monitoring
Automated Code Review: (Javier)
Refined dashboard for monthly review
SQL logic to reflect the latest repository issue snapshot.
Implemented logic to handle duplicate violations correctly.
Built measures for issue counts by rule_code at the latest selected date.
Prevented fallback to older snapshots when the latest has zero issues.
Presented in RMA monthly reviews (Glen-Erik, Eswar & Javier)

---

## Update 7

**Date:** 2026-03-13
**Business Area:** PROPEL
**Business Project:** Measurement Refinement
**People:** [[glen-erik_cortez/overview_glen-erik_cortez|Glen-Erik Cortez]]

### Summarized Update

Measurements: (Javier)
Mapped offer categories to obr_total_revenue categories to link offers to specific purchase history. Developed a methodology to generate APDs and KPIs for A/B testing, supported by purchase-lag and revenue attribution logic. Run_time vs offer_time logic bug in scheduling and folder write: (Santiago)
Investigated how these two variables interact.

### Raw Update

Measurements: (Javier)
Mapped offer categories to obr_total_revenue categories to link offers to specific purchase history.
Developed a methodology to generate APDs and KPIs for A/B testing, supported by purchase-lag and revenue attribution logic.
Run_time vs offer_time logic bug in scheduling and folder write: (Santiago)
Investigated how these two variables interact. Discovered a few band-aids that avoid most of these issues but make the process and troubleshooting confusing.
Documented current approach & planned to add additional safeguard to avoid errors/mistakes in the process leaving current process intact rather than refactoring entirely and having to fix historical data and dashboards.

---

## Update 8

**Date:** 2026-03-13
**Business Area:** PCP Pricing Automation
**Business Project:** Automated Pricing Expansion
**People:** [[glen-erik_cortez/overview_glen-erik_cortez|Glen-Erik Cortez]]

### Summarized Update

Aligned new contract allowing different notifications & takeover messaging, while also removing many unused fields and renaming others for end to end transparency. Developed plan to test in prod with dummy sailing.

### Raw Update

Aligned new contract allowing different notifications & takeover messaging, while also removing many unused fields and renaming others for end to end transparency.
Developed plan to test in prod with dummy sailing.

---

## Update 9

**Date:** 2026-03-13
**Business Area:** MyCruise Recommender
**Business Project:** Calendar Recommender Development
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[cristian_villamarin-villamil/overview_cristian_villamarin-villamil|Cristian Villamarin-Villamil]]

### Summarized Update

Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app. Recommendations Engine (Cristian V.)
Business Presentation: Presented recommender system to Gang and Rafael Toro — well received with increased stakeholder interest. Multiple team members reached out privately asking about recommendations.

### Raw Update

Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app.
Recommendations Engine (Cristian V.)
Business Presentation: Presented recommender system to Gang and Rafael Toro — well received with increased stakeholder interest. Multiple team members reached out privately asking about recommendations. Next steps being prioritized with Taylor.
Graph-Based Model: Development ~80% complete. Calendar recommendations API fully deployed and operational. Discussion on reserving top 1-2 recommendation spots for business-priority products (Royal Beach Club, new destinations) to address cold-start problem for high-investment owned products.
Affinity Groups: Agreed to use business-defined consumer segments as the starting point, with DS enhancing granularity — balancing model performance with business alignment.

---

## Update 10

**Date:** 2026-03-13
**Business Area:** Project Axiom
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data. Meta Data Extraction
Open-Ended Topic Extraction Pipeline (David M.): Migrated batch processing code to new repo with reusable utility functions. Improving open-ended topic extraction prompts based on prior feedback.

### Raw Update

AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.
Meta Data Extraction
Open-Ended Topic Extraction Pipeline (David M.): Migrated batch processing code to new repo with reusable utility functions. Improving open-ended topic extraction prompts based on prior feedback. Grok model may not be permitted by Infosec (partner-hosted by X AI); GPT-5 nano identified as Azure-compliant fallback if needed.
Guest Logs Categorization (David M.): Reviewing 20 Crown & Anchor misclassification examples — most errors stem from missing subcategories in the new schema rather than model failures. Awaiting business feedback from Alessio to add missing categories.
Reporting
Axiom Power BI Dashboard (Danusio G.): Removed brand filters to include Celebrity and Silversea alongside Royal Caribbean. Refactored queries into structured scripts for maintainability. Implementing Alessio's feedback: replacing right-side visuals on Trends/Topics/Analytics tab with a diagnostic table showing NPS, demographic breakdown, and filtered comments by topic and sailing. "Trends, Topics and Analytics" tab now set as primary.
ShoreX Safety Email (Danusio G.): Iterated on classifier based on Eduardo's feedback to reduce false positives. Implementing Melissa's additional suggestions. Exploring use of ship-specific venue context data to improve LLM onboard vs. shore excursion classification accuracy.
GSO Safety Report (Danusio G.): Confirmed monthly cadence on the 15th. Refactoring to a four-level classification system, reporting only Level 3/4 incidents to reduce false positives.
Port Email (Rodrigo B.): Investigating port data discrepancies — sharing evidence and queries with Alex. Port mapping is missing from the Medallia table in Databricks; engineering support required to resolve.
Abandoned Cart Dashboard (Rodrigo B.): Final version published with demographics page, weekly behavior page, and exclusive selection filters for multiple-choice questions as requested by Pia.
Port Appeal Survey Data Extraction (Rodrigo B.): Extracted current-year survey data; prior years unavailable due to survey visibility restrictions. Mapping complex multi-choice questions and preparing table with example join views for Uri (CEL Consumer Insights).
Target Calculation Methodology (Rodrigo B.): Completed. All guest strategy metrics validated within ±0.1 threshold except one metric (0.6 difference) still under investigation. Weekly Power BI dashboard scheduled to run Monday mornings.
Modeling
Medallia Keyword Correlation Tool (Osvaldo V.): Integrated into Axiom webapp with multi-keyword search and wildcard regex search across all comments (not just topic keywords). Switched data source to "bullet points" table for expanded filtering by loyalty and demographics. Embedding-based similarity paused until a shared vector store is available. Addressing slow API data retrieval by implementing local caching on Lambda.
Drivers Model (Osvaldo V.): New regression model deployed in MLflow with LTR as target. OFE (Overall Family Experience) analysis completed — split into score groups and analyzed demographics; only minor differences found across age and passenger segments, not the strong bias initially suspected.
Blockers:
Grok model governance: pending Infosec approval (partner-hosted, not Azure-native). GPT-5 nano as fallback.
Port mapping missing from Medallia in Databricks — requires engineering support.
Guest Logs classification accuracy dependent on business feedback to add missing categories.

---

## Update 11

**Date:** 2026-03-13
**Business Area:** Win-on-Waste
**Business Project:** Forecasting Pipeline Expansion
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

MDR Pipeline & Modeling Enhancements
Completed a major overhaul of feature engineering in the MDR pipeline. Introduced a layered feature strategy:
Ship-based features (primary)
Class-based features (fallback when ship data unavailable)
Meta product code–based features (final fallback)
With the layers above  added moving averages across multiple windows and residuals from monthly averages, scaled by the current voyage load factor to better capture operational dynamics. Performed a complete redesign of the modeling function, introducing selective masking to enable multiple models within the same group, implemented efficiently using Pandas UDFs.

### Raw Update

1. MDR Pipeline & Modeling Enhancements
Completed a major overhaul of feature engineering in the MDR pipeline.
Introduced a layered feature strategy:
Ship-based features (primary)
Class-based features (fallback when ship data unavailable)
Meta product code–based features (final fallback)
With the layers above  added moving averages across multiple windows and residuals from monthly averages, scaled by the current voyage load factor to better capture operational dynamics.
Performed a complete redesign of the modeling function, introducing selective masking to enable multiple models within the same group, implemented efficiently using Pandas UDFs.
Integration testing is currently in progress.
2. Orchestration & Operational Gap Handling
Redesigned the orchestrator to integrate an outlier control module.
This module specifically addresses operational gaps, including previously identified issues with next-day closing orders, which were:
Raised earlier with the F&B Operational Excellence team
Properly reported and documented
The goal is to ensure forecast robustness despite known operational inconsistencies.
3. PLU Data Consistency & Reporting
Initiated research on PLU list discrepancies between Q Control and CrunchTime, with the objective of maintaining a single, consistent source of truth that also feeds the Windjammer pipeline.
Delivered PLU mismatch reports for both Specialty and MDR, highlighting:
Items planned and assigned in menus but not served or not correctly keyed in POS
Items served or keyed in POS but not planned or not part of the menu matrix
Reports are generated per day, providing actionable visibility to operations.
4. FPMS Adoption & Evidence of Usage
Chefs have been actively using the FPMS app and its embedded forecasts for over a year.
Clear proof of adoption exists via ServiceNow tickets, which are consistently raised when:
Forecast deviations exceed expectations
Issues occur at individual item and venue levels
These tickets are welcomed, as they represent direct human feedback that is systematically incorporated to improve model accuracy and reliability.
5. Key Concern: Stakeholder Alignment & Perception/ Change Management Risk
A challenge has emerged due to late involvement of a key operational stakeholder (Chef Gary, based in London), who:
Was not involved during development, implementation, or rollout, despite repeated efforts by the product team
Is now required to drive adoption among chefs as an end user
The lack of early engagement has led to misalignment in expectations, and recent feedback has begun to negatively impact perceptions of the FPMS app and forecast among end users.
This presents a reputational and adoption risk, driven primarily by communication gaps and organizational dynamics, rather than product performance or adoption evidence.
6. FPMS & AI Team Forward Plan
The FPMS and AI teams are focused on both technical excellence and transparency:
Accuracy Improvements
Ongoing overhaul aims to reduce daily maximum variance from ~20% to materially lower levels.
Performance Transparency & Reporting
Planned rollout of:
Historical aggregated reports comparing forecast vs. actual consumption over recent months
Ongoing performance reporting (daily or weekly), individualized per venue
Reports will be shared directly with ship-level chefs, and copied to:
Chef Gary
Relevant stakeholders
Product and AI teams
This ensures objective, data-driven visibility into forecast performance and supports alignment across all stakeholders.

---

## Update 12

**Date:** 2026-03-13
**Business Area:** CEL Revenue Management
**People:** Unidentified

### Summarized Update

CEL \ PERKS \ Additional DS Analyses + March Readout \ MAR
3/9/2026
Status: This ticket is complete as of 03/06/2026
Deliverables:
Estimated revenue gain if recommendations are actioned: 2026 = $1M, 2027 = $3M, 2028 = $5M
Supporting Excel workbooks finalized. Future testing considerations:
Larger gaps
Longer testing period for far booking window
Initial soft matching on sailing prices and monitor price drift during test
Validation of Revenue Planning holiday flags if including holiday sailings in test
Delays: None. Potential future issue: None.

### Raw Update

CEL \ PERKS \ Additional DS Analyses + March Readout \ MAR
3/9/2026
Status: This ticket is complete as of 03/06/2026
Deliverables:
Estimated revenue gain if recommendations are actioned: 2026 = $1M, 2027 = $3M, 2028 = $5M
Supporting Excel workbooks finalized.
Future testing considerations:
Larger gaps
Longer testing period for far booking window
Initial soft matching on sailing prices and monitor price drift during test
Validation of Revenue Planning holiday flags if including holiday sailings in test
Delays: None.
Potential future issue: None.

---

## Update 13

**Date:** 2026-03-13
**Business Area:** CEL Rev Mgmt
**Business Project:** Category Gapping Optimization 3.0
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Lamis
CEL Rev Mgmt Track Optimization
Generated optimal tracks for all active sailings - cat classes. Took 2 hrs 30 mins without distributed processing. Will be working next on optimizing this further.

### Raw Update

Lamis
CEL Rev Mgmt Track Optimization
Generated optimal tracks for all active sailings - cat classes. Took 2 hrs 30 mins without distributed processing. Will be working next on optimizing this further. Working on analyzing the generated optimal tracks: (1) Comparing them against business tracks (2) Identifying any fall-offs and investigating the causes (0.6% of the fleet - cat class fell off). Identified 2 reasons for these fall offs: (1) No demand curves exist (2) the capacity to target is less than or greater than the lower or upper bounds which makes the problem infeasible. identified few cases to discuss with the business tomorrow. Prepared a presentation for business stakeholders tomorrow with results of these validations and comparisons.

---

## Update 14

**Date:** 2026-03-13
**Business Area:** RCI Rev Mgmt
**Business Project:** SPI-guided Track Optimization
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Lamis
RCI Rev Mgmt Track Optimization
Started this week working on running the scaling approach to RCI starting with generating the demand curves - making code adjustments for the DP optimization to run on both brands. This task will continue for the next week. Worked on preparing a presentation on track and price optimization projects to the DS team.

### Raw Update

Lamis
RCI Rev Mgmt Track Optimization
Started this week working on running the scaling approach to RCI starting with generating the demand curves - making code adjustments for the DP optimization to run on both brands. This task will continue for the next week. Worked on preparing a presentation on track and price optimization projects to the DS team.

---

## Update 15

**Date:** 2026-03-13
**Business Area:** RCI Rev Mgmt
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[jesse_bausell/overview_jesse_bausell|Jesse Bausell]]

### Summarized Update

SSC PRE \ Upper-level Suites
Design AB test for upper-level suites
3/5/2026
Data Science has begun examining behavior between upper level categories based on information provided by Revenue Team
SSC PRE \ Compute PRE Metrics
3/12/2026
I am de-prioritizing this task for now. My priority is to complete the ab test before I leave for the military on 3/27.

### Raw Update

SSC PRE \ Upper-level Suites
Design AB test for upper-level suites
3/5/2026
Data Science has begun examining behavior between upper level categories based on information provided by Revenue Team
SSC PRE \ Compute PRE Metrics
3/12/2026
I am de-prioritizing this task for now. My priority is to complete the ab test before I leave for the military on 3/27.

---

## Update 16

**Date:** 2026-03-13
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

CEL RM GTY-LEAD Updates
Conducted analysis of APD lifts for Brian Rosenthal
o Recalculated revenue based on observed tradeups and actual gaps implemented. o Compared to optimal gaps and predicted revenue
o Illustrates the effects of GTY-LEAD 2.0 updates and how it has improved predictions as well and lifted APDs across all products
CEL product managers approved 2.0 updates, testing in QA and pushing to production today. Met with RCI stakeholders and presented all 2.0 updates that have been made to CEL’s projects.

### Raw Update

CEL RM GTY-LEAD Updates
Conducted analysis of APD lifts for Brian Rosenthal
o Recalculated revenue based on observed tradeups and actual gaps implemented.
o Compared to optimal gaps and predicted revenue
o Illustrates the effects of GTY-LEAD 2.0 updates and how it has improved predictions as well and lifted APDs across all products
CEL product managers approved 2.0 updates, testing in QA and pushing to production today.
Met with RCI stakeholders and presented all 2.0 updates that have been made to CEL’s projects. Team approved making the same changes to RCI’s project to align codebases.

---

## Update 17

**Date:** 2026-03-13
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

RCI RM Category-Gapping 3.0
Category-Gapping 3.0 Progress
Met with RCI team to discuss tier groupings, decided on recategorizing based on achieved prices instead of using current tiers that were hardcoded based on room characteristics by the business. I will be working on reworking the tiers to then be approved by the team. Built out initial optimization code.

### Raw Update

RCI RM Category-Gapping 3.0
Category-Gapping 3.0 Progress
Met with RCI team to discuss tier groupings, decided on recategorizing based on achieved prices instead of using current tiers that were hardcoded based on room characteristics by the business. I will be working on reworking the tiers to then be approved by the team.
Built out initial optimization code.
o DP optimization with piecewise linearization
o Single WTS bin → optimal price gaps between tiers that maximize revenue for that week
o Week’s demand comes from track and current LAF as baseline price
o Created grid of all possible feature combinations to search
o If testing a gap that falls between grid points, interpolate smoothly to estimate realistic tier shares
When optimizing for future WTS:
Capacity safeguards
Compute expected bookings per tier = weekly demand × predicted tier share
Reject any price plan where Lower / Upper / Premium exceed available inventory. GTY is allowed to exceed.
Revenue = (GTY_bookings × GTY_price) + (Lower_bookings × Lower_price) + (Upper_bookings × Upper_price) + (Premium_bookings × Premium_price)
Output: optimal gaps, the final prices, predicted probabilities, bookings by tier, and expected revenue for that week.
Currently addressing why the gaps 2 and 3 are hitting upper limit
o Predicted shares do not decrease as sharply as necessary so optimal revenue is found at highest gaps, however this is not business optimal
o Need more realistic share declining at higher premium / upper

---

## Update 18

**Date:** 2026-03-13
**Business Area:** PCP Pricing Automation
**Business Project:** Beverage Package Optimization
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

EDA on the different bev packages, WTS bins, seasonality, & other potential features
EDA process was complete analyzing several factors and obtaining valuable insights. WTS Bins were identified for both Classic & Premium package, and the bins definitely vary across the two products a bit. They even vary depending on the version of the package (21+ domestic vs 18+ international).This helped identify the WTS Binning strategy and the Feature Store was updated appropriately with these changes.

### Raw Update

EDA on the different bev packages, WTS bins, seasonality, & other potential features
EDA process was complete analyzing several factors and obtaining valuable insights. WTS Bins were identified for both Classic & Premium package, and the bins definitely vary across the two products a bit. They even vary depending on the version of the package (21+ domestic vs 18+ international).This helped identify the WTS Binning strategy and the Feature Store was updated appropriately with these changes. Elasticities were also analyzed across metas and the different WTS bins for both beverage packages. Lastly, some of the common price gaps were analyzed across classic & premium, along with all the variations of premium representing bundles and/or upgrades from classic to premium. These analyzed price gaps help obtain useful insights that can later be used in the optimization routine. In addition, the distributions of prices & volume of bookings were analyzed for the two packages and how it may vary by ship class, meta, & WTS bin.
Recurring meetings with Business Team (PREs, CRF Automation, etc) & DE Team (Mass Promo Table & Targeted Offers)
An update was given to Jorge regarding the changes made for the RBC beverage bundles. The new approach helped resolve some of the biases that led to bad outputs. The new results are much better, with the only caveat being SHORT CARIBBEAN sailings not showing much price variation (this could possibly be due to the statistical and data-driven insights for SHORT CARIBBEAN RBC sailings still having limited data and therefore leading to biased outputs for that specific meta. More data will only help improve the ratios used to adjust for RBC bundles.
A meeting with Gaby helped plan next steps for testing soon, with the intent to (1) test all conditions & (2) test what the limit of sailings per promo is. This can help simplify the promo upload procedure by being able to avoid complex SAILING TAG creations as long as the Hybris system will be able to handle PRE outputs in the future that will group together a large number of sailings under the same discount promo for a particular product. We also discussed plans to A/B test beverage soon, which could also include the use of a new FCST target revenue, now being +5% STLY instead of the other created FCST target revenue.
Adhoc meetings & help regarding OBR
A meeting was had with Aagam to go over some A/B testing concepts, in this case particularly focused on power analysis. The same meeting is also planned to be had with Anaand. Both will be conducting their own A/B tests so discussions are being had sharing my knowledge and insights on the tools to be used.

---

## Update 19

**Date:** 2026-03-13
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

CRF Automation Progress and Updates
Update:
This week, I temporarily de-prioritized the CRF Automation work to focus on the dashboard enhancements and the A La Carte testing efforts. I will be re-prioritizing CRF Automation starting next week, when I plan to meet with the team to showcase the progress made so far and discuss the additional inputs needed to move the process forward. I’ve completed the calculation of the final price points for the RBC Alc Pass, RBC Non-Alc Pass, and RBC DX Pass in accordance with the business rules.

### Raw Update

CRF Automation Progress and Updates
Update:
This week, I temporarily de-prioritized the CRF Automation work to focus on the dashboard enhancements and the A La Carte testing efforts. I will be re-prioritizing CRF Automation starting next week, when I plan to meet with the team to showcase the progress made so far and discuss the additional inputs needed to move the process forward.
I’ve completed the calculation of the final price points for the RBC Alc Pass, RBC Non-Alc Pass, and RBC DX Pass in accordance with the business rules. Since the process relies on the previous week’s discount percentage, and there is currently no table capturing that historical data, I’m working with the team to design and implement a table that will store weekly discounts for future processing.
I also identified that sailings beginning in January 2027 were missing base prices for these passes. This impacted the workflow because the sailing date range for this CRF spans from today through the next 365 days. I’ve been coordinating with the business team to ensure these base prices are added so the process can run as expected.
I also added additional checks based on the discussions with business to set guardrails for the CRF process, these involve –
setting caps on the price changes
cap on the gap between the Alc and the Non Alc pass
DX + RBC Bundle Price: Confirms the bundle price is calculated correctly.
Implied RBC Price: Ensures the guest-perceived RBC price stays above ~$30 and below the standalone Alcohol Pass price.
Implied vs. Alcohol Pass: Verifies the implied RBC price is always lower than the standalone Alcohol Pass price.
Bundle Discount vs. Pass Discount: Checks that the bundle discount is ideally higher than the pass discount, with limited exceptions.
Alcohol & Non-Alcohol Discount Changes: Reviews discount movements between sales periods for expected variation.
DX vs. Bundle: Ensures the bundle discount is always higher than the Deluxe discount.
Next Steps and Blockers
Null Handling
2027 Sailings:
Some 2027 rows still return nulls; need business support to update the source table so automation can run cleanly.
90+ Window Metas:
LONG CAR, CARIBNE, REPOS, and BERMUDA show nulls; proposing to classify them by sail-night similarity (short vs. 7N) pending business confirmation.
Last Week’s Discount:
This value is still manually sourced. Once a table is created to store weekly discounts, I can fully automate the dependency; for the first run, I can manually read it from SharePoint.
RCI | OBR | RBC Dashboard
RBC Dashboard Updates
This week I focused on the following:
Corrected the aggregated counts used in the dashboard’s underlying data build.
Added new parameters for ship class and meta product code, and refactored the associated queries accordingly.
Began developing an additional dashboard to help the team analyze historical booking patterns across multiple parameters. I have already integrated the necessary data and built the structure; publishing is the next step.
Incorporated customer age data to support the business team in identifying which segments are over/under indexing.
Next Steps
Plan to introduce cat-class–level parameters into the dashboard, enabling the business team to better understand how different cat-class customer segments align with specific offerings.

---

## Update 20

**Date:** 2026-03-13
**Business Area:** NewBuild
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

Started development of the Newbuild API to host a custom agent using FastAPI and Azure Container Apps. Fully completed the foundational framework and authentication mechanism. Began development of the Chatbot web app for the Newbuild Enterprise Observatory using Next.js and FastAPI.

### Raw Update

Started development of the Newbuild API to host a custom agent using FastAPI and Azure Container Apps.
Fully completed the foundational framework and authentication mechanism. Began development of the Chatbot web app for the Newbuild Enterprise Observatory using Next.js and FastAPI.
Completed the authentication mechanism and major portions of the GUI.
Identified several security vulnerabilities in MLflow and worked with Databricks and InfoSec to remediate them.
Met with the Newbuild i95 Product team and provided an update on the progress of the AI solution. Mala will prepare a roadmap presentation to be shared with Hani.
Received the list of required tables on the i95 platform for Databricks integration and am working with the Data Engineering team on the integration.

---

## Update 21

**Date:** 2026-03-13
**Business Area:** Marine
**Business Project:** Asset Management Expansion
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

Met with the Asset Management team and obtained access to the historical AWS SQL Server used as an analytics data warehouse. Retrieved all stored procedures and views related to AMOS and JDE. Downloaded the files and, with the help of GenAI, extracted the list of missing JDE tables required to complete the consumables SQL query.

### Raw Update

Met with the Asset Management team and obtained access to the historical AWS SQL Server used as an analytics data warehouse. Retrieved all stored procedures and views related to AMOS and JDE. Downloaded the files and, with the help of GenAI, extracted the list of missing JDE tables required to complete the consumables SQL query. These tables now reside in the new Oracle Fusion platform and do not have the same fields as the legacy JDE tables. Working with Data Engineering to identify the required data.
Met with the Koja cabin automation system provider, along with InfoSec and IT, to review the data access project for the Spectrum pilot.
Met with IT, Newbuild, and the Decarbonization team regarding the replacement of Meyer Turku’s Energy Management System (MEMS) with MIAP for Icon of the Seas, funded through Newbuild. The MEMS solution was developed by the shipyard to provide real-time onboard energy analytics. MIAP would replace this system as a real-time solution running onboard. Pending approval and support from Edith to secure the capital funding needed to start the project next year.

---

## Update 22

**Date:** 2026-03-13
**Business Area:** MIAP
**Business Project:** Asset Management Expansion
**People:** Unidentified

### Summarized Update

Worked on MIAP production ETL fixes by updating Key Vault references and correcting code issues. All tasks are functioning except for the deployment profile. Continued migration of DNV and Lloyd pipelines to the DE workspace.

### Raw Update

Worked on MIAP production ETL fixes by updating Key Vault references and correcting code issues. All tasks are functioning except for the deployment profile.
Continued migration of DNV and Lloyd pipelines to the DE workspace.
Created a sample load process for PEPLINK into a temporary table.
Added OFB to the MIAP app and identified required table changes for full data availability.
Deployed the gangway workflow to production using asset bundles and successfully loaded data into the production pax_crew table.
Informed the Newbuild team after the production data load was completed.
Next Week
Productionize Lloyd once the new secret is received.
Work on ENIRAM-related tasks.
Continue cost-division work based on vendor response times.

---

## Update 23

**Date:** 2026-03-13
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** [[mahshad_shariatnasab/overview_mahshad_shariatnasab|Mahshad Shariatnasab]]

### Summarized Update

Fixed a bug in the HVAC and AHU agents. Worked on the chiller agent. Addressed data issues for the boiler.

### Raw Update

Fixed a bug in the HVAC and AHU agents.
Worked on the chiller agent.
Addressed data issues for the boiler.

---

## Update 24

**Date:** 2026-03-13
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** Unidentified

### Summarized Update

Fixed workflow errors in the power plant. Fixed workflow errors in fuel analytics. Working on FACTS web app integration.

### Raw Update

Fixed workflow errors in the power plant.
Fixed workflow errors in fuel analytics.
Working on FACTS web app integration.
Updated shore power logic so configuration is passed to the power plant model through voyage inputs, allowing multiple legs to be run at once.
Fixed tag-mapping issues with Allure OTS that caused negative service power.
Fixed broken power plant analytics figures in the web app to improve SFOC analytics.
Fixed Snyk vulnerabilities in the rcg-online-residual-boosting and rcg-digital-twin packages.
Added support for a demand-rounding step in the miap-rest-api and web app.
Identified potential SFOC deviations on WN, SL, SI, and RF; currently investigating validity.

---

## Update 25

**Date:** 2026-03-13
**Business Area:** MIAP
**Business Project:** Marine Safety Analytics
**People:** [[arya_cheeti/overview_arya_cheeti|Arya Cheeti]]

### Summarized Update

Refining power plant predictions in the digital twin simulation. Added RA to hotel and service power. Identified potential fuel savings on Wonder of the Seas.

### Raw Update

Refining power plant predictions in the digital twin simulation.
Added RA to hotel and service power.
Identified potential fuel savings on Wonder of the Seas.
Fixed issues in the MIAP analytics pipeline.

---

## Update 26

**Date:** 2026-03-13
**Business Area:** MIAP
**Business Project:** Marine Safety Analytics
**People:** [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]]

### Summarized Update

Fixed a bug in the digital twin fuel platform and added incinerator fuel consumption. Presented in the monthly AI & Analytics department project meeting. Diagnosed the root cause of negative total service power on Allure.

### Raw Update

Fixed a bug in the digital twin fuel platform and added incinerator fuel consumption.
Presented in the monthly AI & Analytics department project meeting.
Diagnosed the root cause of negative total service power on Allure.
Updated the service power baseline for ship RD.
Working on a sailing-level fuel forecast comparison script.

---

## Update 27

**Date:** 2026-03-13
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model
**People:** [[evan_mcfall/overview_evan_mcfall|Evan McFall]]

### Summarized Update

Positive Feed back from stakeholders on the Factors Model PoC. This is really outstanding and “cracked the nut”
Factor Models
Visualizations finalized for v1 release
Updated segmentation parameters to inspect individual factors and their relationship to SPI
Histogram and band views implemented with range overlays per feature
Initial portal created with multi-method display
SPI distribution surfaced by week-to-sail across histogram, bands, and scatter views
Nine filter dropdowns added across Fleet & Product and Time Period groups with client-side filtering and live sailing count
Dynamic feature addition with independent filter sets and consistent global SPI thresholds across groups
Confounding and interaction effect evaluation completed
Assessed variable interactions from initial factor set
Identified and created initial framework to include these with future modeling attempts
AB Testing / Code Standardization
Package creator and query creator completed
.whl finalized and validated in notebooks

### Raw Update

Positive Feed back from stakeholders on the Factors Model PoC. This is really outstanding and “cracked the nut”
Factor Models
Visualizations finalized for v1 release
Updated segmentation parameters to inspect individual factors and their relationship to SPI
Histogram and band views implemented with range overlays per feature
Initial portal created with multi-method display
SPI distribution surfaced by week-to-sail across histogram, bands, and scatter views
Nine filter dropdowns added across Fleet & Product and Time Period groups with client-side filtering and live sailing count
Dynamic feature addition with independent filter sets and consistent global SPI thresholds across groups
Confounding and interaction effect evaluation completed
Assessed variable interactions from initial factor set
Identified and created initial framework to include these with future modeling attempts
AB Testing / Code Standardization
Package creator and query creator completed
.whl finalized and validated in notebooks

---

_Source: 20260313 - Weekly Matt & Rafeh Update (Raw).docx_