**Douglas Bedell**

**CEL**** ****RevMgmt**** - ****T4 A/B Testing – Setup, Monitoring, and Evaluation**

Transformed approved sailing lists into formats usable by monitoring notebooks and resolved clustering discrepancies with the brand.

Performed booking ETL from test start through current date and reviewed early results with stakeholders.

Extended monitoring metrics to include true T4 revenue and APD calculated at the passenger level.

Completed initial monitoring setup and shared outputs with the business; early trends look favorable with tests continuing to run.

**Srilekha Reddy Madupu**

**CEL ****Rev ****Mgmt**** - ****Feedback ****From**** CEL Team on Actual Price Paid Analysis**

**Actual Price Paid – Celebrity Feedback Integration**

Presented SPI-based booked-position benchmarks to Celebrity stakeholders and aligned on their use as promotion guidance at a granular grouping and weeks-to-sail level.

Agreed not to use SPI price ranges directly due to external pricing influences.

Identified that promotions primarily impact GTY pricing by widening GTY-to-lead gaps.

Defined next steps focused on enhancing the GTY-lead dataset to better analyze gap behavior and trade-up probability.

**Michelle Manfrini**

**RCI Rev ****Mgmt**** ****| Category-Gapping 3.0**
- Met with business and presented all 3.0 updates. Reviewed modelling approach (using 2.0 and 3.0 outputs combined, curve smoothing, data driven gap increments). Team is aligned.
- Also reviewed optimization approach where gaps are recommended based on availability:
1. Calculate remaining capacity per tier and available shares from group and cat-class.
2. Calculate index from remaining within tier and remaining in cat-class. Capped at 1.5.
3. Calculate optimal booking share as index by remaining from total. This provides “optimal” shares per tier based on what is available in order to price cabins to sell where we desire.
4. Apply weighted Euclidean distance formula to match desired output to closest match in lookup table.
5. Of the feasible matches, output the combination resulting in the highest revenue.
- Team agreed with approach but will review revenue formula to confirm method works for RCI.
- All 2.0 updates were approved. Pushed changes and currently testing in QA. Will be in PRD by end of week is all goes well.
- Applied isotonic (monotonic) regression as a post processing step on the lookup tables, not during model training. Ensures predicted booking shares move in the correct direction as price gaps increase, while making the smallest possible adjustment to the original model predictions. Runs fully distributed in Spark (no pandas, no Arrow), so it scales across all metas and static key combinations in parallel.

**Michelle Manfrini**

**CEL Rev ****Mgmt**** | Category-Gapping 3.0**
Adjusted model outputs based on last week’s feedback:
Changed rules to follow a strict waterfall where GTY’s first flow to Lower, Upper, and then Premium only if less expensive tiers are filled.
Adjusted models to better identify this demand at low gaps but still drop as sharply as necessary is prices increase.
Applied isotonic regression–based post processing step for the lookup tables to enforce consistent behavior in the model outputs.
Team is reviewing gap recommendations. Initial feedback is positive.
CEL would like to implement DART before moving to optimizing at a category level or for the full length of the sailing. In the process of building out this framework.
o Created dataset with actual tier shares per sailing for the past month. Since I am splitting out bookings per tier, it might be necessary to aggregate for the past 2 months in order to have more data.
o This “DART” approach must also integrate the residuals for the original 2.0 models. Framework first adjusts the 2.0 predictions and separately adjusts the 3.0 predictions based on the physical residuals.
o Shares are normalized to ensure they still sum to 1.
o Residuals must be calculated post-hoc and not as a feature in the model because team wants to adjust predictions based on individual sailing performance. Including this as part of the optimization will allow the recommendations to shift in near real time whereas model retraining would take longer to pick up on sailings that are under/overperforming.

**Lamis Amer**

**RCI Rev ****Mgmt****: ****Track Optimization – KPI Comparison, Failure Root Causes, and Stabilization – Full close out notes for April effort**

(preview below)

**2nd stage optimization: Smoothing MILP Model:****	****	**
After running the DP model on the entire fleet - the followings were observed:

The week over week change in track ask (optimal) fluctuate too much. While this could be optimal, it does not reflect the business operations. an example shown below

To constraint the optimization to minimize the WoW deviations, in DP this means changing the state of the model to memorize the past week’s decision - this will expand the size of the problem by a lot.

Alternatively, I developed** another layer of MILP optimization model **that runs on the DP optimal solution to smooth the weekly track ask while minimizing the deviation from the DP weekly optimal solution + minimizing the WoW change in track ask.

This approach will not generate a global optimal - but near-optimal solution. It is however, very fast takes an increment of a second to run of a single sailing not adding a lot of extra time on the DP run (one a run on the entire fleet is completed will evaluate the overall time).

Based on back-and-forth discussion and feedback from the stakeholder we have been refining the smoothing parameters so that certain peaks are maintained.
After smoothing the optimal bkgs - the prices are recomputed at the smoothed bookings.

**Treating and Processing the Price-Demand Curves**

The demand curves generated for each sailing, class, wts and booked position are based on the raw predictions of the model at different price points.

Sometimes these curves follow an unrealistic pattern of demand (like demand increasing as price increases) specially very far out (example shown below) - or certain peaks are observed / demand decreases, increases then decreases, etc. which is also what is expected by the biz.

I performed a multi-step treatment for these curves as follows:

1.      Extend bkgs range to cover bounds​ using linear extrapolation from the maximum bkgs predicted.

2.      Fitted monotonically decreasing Isotonic Regression Function​

3.      ​Bounding the price changes at +/- 30% overall increase/decrease from current base price point. This range (+/-30%) is estimated based on the analysis of historical price changes across completed sailings.

4.      To smooth-out the uniform price-demand relations at the tails of each curve - I applied rolling window smoothing - resulting in the curve bordered in yellow in the fig below

**Uncertainty Analysis and Prediction Model Error Analysis**

The biz stakeholders are very concerned about the way track optimization behaves given unknown behavior of the demand prediction model. I ran uncertainty and sensitivity analysis as follows:

**a. Uncertainty Analysis**

Analyzed the error performance of the model by looking into the probability of over vs underprediction for each group of ship_code, meta_product, peak season, and cat class.

Analyzed the error pct when over predicting and when underpredicting by calculating SMAPE error metric.

For each sailing, class and WTS estimated the most probable range for the error as the weighted average of the error pct as follows:
**min_error**** **= (probability of over prediction at this WTS * 10th %ile of error pct at this WTS)+(probability of under prediction at this WTS * 10th %ile of error pct at this WTS)
**max_error**** **= (probability of over prediction at this WTS * 90th %ile of error pct at this WTS)+(probability of under prediction at this WTS * 90th %ile of error pct at this WTS)
**median_error**** **= (probability of over prediction at this WTS * 50th %ile of error pct at this WTS)+(probability of under prediction at this WTS * 50th %ile of error pct at this WTS)

An example on the prediction error pct and how changes for ship: SI - class: I - Europe in August. At 16 WTS error pct ranges from -2.5% to 101% and the median is at 43%

**Evan ****McFall**

**RCI ****RevMgmt****: ****DUAL Demand Forecast – Macro Economic + Search Interest**

**Comments:**

·       **Apr**** ****24**** ****2026**** ****11:30**** ****AM** – Integrated external macroeconomic datasets into the demand forecast pipeline, including Consumer Pricing and Sensitivity (FRED), spending capability metrics, ~20 macro indicators, and search interest data with weekly query-level breakdowns. Data is dynamic and available by term and region.

**DUAL Demand Forecast – External Data Automation**

**Comments:**

·       **Apr**** ****30**** ****2026**** ****7:35**** ****AM** – Completed automated scraping and publishing for Page Hits data. Finalized Market Volatility and Gas Prices pipelines. Built meta/regional sentiment pipeline using Cruise Critic data. Delivered documentation covering all external data sources, scraping logic, transformations, and publishing steps. Completed regression modeling, lagged features, model MVP testing, and key pipeline refactoring activities.

**Demand Model**

Established MVP for week ahead forecast improving metrics across the board against original and interim model (~22%)

Built initial framework around data ETL changes for new UC tables and finalized queries for clickstream data

Began work on capacity and identified issues with existing queries

Created binned weight tuning method to evaluate underlying binned sample distribution parameter optimization

Standardized pipeline for external data queries

**SPI ****Factor Models**

Began evaluation of integration / use case for SPI with track optimization

Working closely with Lamis on integration of new demand model and SPI guardrails testing

** **

**Aagam Shah**

**PCP Pricing Automation**** | OBR | RBC Business Rules Driven (Passes and Waterpark) PRE v1**

**Updates:**

Baseline Historical Demand Curves: Instead of relying on the past three months of data, we are now using 2023 and 2024 booking data for Waterpark excursions and general Nassau (NAS) Shore Excursions to construct baseline booking curves for Waterpark and RBC, respectively. The objective is to capture the underlying natural demand patterns. In contrast, pricing in 2025 and 2026 has been adjusted frequently, which distorts observed booking behavior and prevents an accurate representation of true demand.

Previously they were just aggregated at a meta_product_code level, now I have captured demand at a meta_product_code, month level

Peer Identification: Previously, peers were grouped solely based on the same meta product code. We now define peers more granularly by incorporating phase (splitting Short Caribbean into 3N and 4N/5N), meta product code, and ship class, resulting in a more precise and comparable peer grouping.

Before comparing the peers, now we first look at page views across peers and then identify sailings where there could be a views issue and our first pass would be at increasing pageviews before changing the prices.

Instead of looking at a sailing score now I am just looking at total penetration and comparing it across peers

Final price is now anchored at the new price calculated based on track

Presentation with stakeholders: Presented my findings to the stakeholders need to validate the recs with them

**Neila ****Bennamane**

**CEL Rev ****Mgmt****: ****DUAL BASKETS Application Build**

Completed delivery of the Basket & Corridor Pricing Signal viewer application, providing RM analysts direct visibility into pricing signals without requiring Databricks access.

Application supports all 31 fleets across RCI Ocean, Celebrity Ocean, and Celebrity River, including floor-mode fleets.

Delivered four analyst-focused views: Signal Overview, Basket Explorer, Corridor Charts, and Drift Monitoring.

Presented the application to Royal and Celebrity stakeholders; functionality is complete and pending production publishing by MLOps and Platform teams in early May.

**DUAL BASKETS – Caribbean, Europe, Alaska, Inter****-Caribbean**

Closed out all basket models for Caribbean (Long, Short, 7N), Europe, Alaska, and Inter-Caribbean sailings.

Delivered standardized booking-pace matrices (360–30 DTD), sailing trait matrices, decision-tree peer grouping, contiguous operational baskets, and P25/P50/P75 velocity corridors.

Automated weekly pricing signal generation and confirmed end-to-end validation against notebook logic.

Conducted brand walkthroughs with RCI and Celebrity; all segments delivered with no open items remaining.

**DUAL | GOLD | Sailing Environment**

**Status: This ticket is complete as of 04/27/2026**

**Deliverables:**
Automated Gold-layer sailing environment pipeline has been built and delivered, replacing one-off notebook analysis with production-ready, weekly pricing signals. Key deliverables include: Gold-layer transformations for basket assignment, corridor percentile signals (P25/P50/P75), and pricing action outputs; automated weekly refresh of sailing-level signals across multiple segments (7N Caribbean, Short Caribbean, Europe, Alaska, etc) for both RCI and CEL brands; end-to-end validation of pipeline outputs against original notebook results; and presentation of signals to RCI on 04/15/2026, with CEL presentation completed on 04/29/2026. Every in-scope sailing receives a single pricing signal (Booked Behind / Booked Ahead / Hold / Monitor). All metrics have been composed; drift will update on a weekly and broader quarterly basis. The job pipeline has been fully created. Improvement metrics are pending evaluation as time goes on.

**Delays:** None.

**Potential future issue:** None.

** **

Ayon Ghosh

**WOW Weekly Update – 5/1**

**Interport**** Specialty Pipeline – Production Deployment:**
Successfully developed, tested, and deployed the **Interport**** Specialty pipeline** to production. A gating mechanism now dynamically detects whether interport voyages exist in the next **7 days** and triggers the pipeline only when needed, optimizing compute usage and avoiding unnecessary runs.

**Interport**** MDR – In Progress:**
Development is underway for the **Interport**** MDR pipeline**, incorporating similar architectural complexity and a **demand****-regime****-aware forecasting modeling stack** to ensure consistency and accuracy with existing MDR forecasts.

**Flexible Operating Hours – Productionized:**
Implemented and deployed a **configuration****-driven flexible operating****-hours framework** for specialty restaurants. Operating hour changes can now be applied **without code changes**, using widget-based JSON configuration. The pipeline automatically parses turn-day, sea-day, and port-day hours within a dedicated processing block, providing significant operational flexibility.

**All****-Day Forecast Capability:**
Developed and deployed **all****-day forecasting** for Specialty restaurants and MDR, running alongside existing **meal****-period****-specific forecasts**, enabling broader operational visibility and planning.

**Critical Profit Center Mapping Issue Identified:**
Discovered multiple incorrect **profit center ID mappings**, where duplicate IDs were shared between bars and specialty pipelines. This was silently overwriting forecasts in the FPMS application. The issue has been documented and escalated to the business team for correction, preventing downstream forecast integrity issues.

**Forecast Accuracy Review with Business Leadership:**
Presented the **forecast accuracy report** to Paul, who expressed strong satisfaction—particularly with the **MDR accuracy levels**. As a next step, the business team will provide ship-level contacts so that **daily forecast accuracy reports** can be distributed directly, helping to bolster confidence among ship chefs and operations teams.

Bao

**E-Commerce Customer Target**

**Primary Accomplishments:**

Continued further development in feature audit notebook identifying key features that put protected classes at risk. Audit identified various key features related to personal data and many are derived from epsilon data. Will soon send list of key risk features to David for further audit.

Finalized app feature integration code and code is now integrated into models in production.

Began development of clickstream features for booking propensity model. Clickstream data was originally fitted more for journey scoring model but has been reframed.

Finalized comparative analysis report and post back test analysis. All the research has been consolidated into a document for ecommerce stakeholders to review. Document also holds recommendations as to how we can approach this POC solely using the booking propensity model.

**Next Steps**

Continue audit research, identify uplift model usage and ensure that it is not actively being used for discriminatory pricing.

Support carlos in the development of journey scoring clustering model.

Experiment with performance tradeoff by removing protected class features/change the features to be binned(or reformatted) to not be a risk.

Carlos A.

**E-Commerce ****Customer Targeting****:**

Develop unsupervised algorithm to encode and segment consumer journey. It produce a 0.5 silhouette score and segments that are interpretable and meaningful to the business.

Train model to predict/assign Journey kind/segment to consumers. (Pending to compute stage of the consumer inside his journey or missing steps for booking completion)

Camila

**Supply Chain: **

In progress:

Medical Demand Forecast Model Enhancement: about 30 iterations and none have been able to beat the current accuracy of the model in production. Will continue iterating.

Phase 6 of supply name/venue breakdown: added sister ship and ship class fallback. Not enough improvement when focused on Beyond. Will likely see more of an accuracy improvement for newer ships such as Xcel. Will continue iterating.

Completed:

Debugging low prediction for food accounts. There was missing GL numbers which made food products be allocated to a different department.

Cleaned SSC Finance Tool code. There were previously inflated values due to picking up unit cost for items using ssc shipboard inventory table. The fix now derives unit cost directly from the consumption report at the last step instead of the previously corrupted unit cost. This has been validated that it is the correct direction to go.

Daily Breakdown Phase 5: Implements an 8 level port-hours fallback chain for daily spend allocation. Uses the same core architecture as P3 (ship code mapping, order snapshot join, voyage itinerary expansion) but adds a multi-tier fallback: when a product/ship/day combination lacks a consumption ratio from the primary strategy, it cascades through progressively broader pools (same port-hours bucket, same length bucket, same day type, etc.) until a ratio is found. Includes EXCLUDE_FOR_FOOD_COST handling to filter out venue categories excluded from food cost calculations.

Daily Breakdown Phase 6: everything Phase 5 has but with account level structure to be able to find which products are food accounts (this is because it was recently discovered that some beverage category items are charged to food accounts)

Supply Daily Breakdown PCD Adjustments: was created and added to the ORDER_CREATION_MASTER_NOTEBOOK pipeline under FINANCE_TOOL_TIER4. This notebook adjusts supply daily breakdown values based on PCD data

Supply Name/Venue Level Breakdown Phase 3:

Uses an appearance-gated lagged approach with conditional all time gap-fill.

Parameters: MIN_APPEARANCES=2, SN_COVERAGE_THRESHOLD=0.80, ALLTIME_DAMPEN_FACTOR=0.08, RATIO_FLOOR_THRESHOLD=0.02.

This strategy requires a product to appear in at least 2 prior sailings before trusting its lagged ratio, with a coverage threshold of 80% of sailing nights before gap-filling with the all time ratio.

Normalize Ratio Repair: Added a Step 7 repair mechanism for groups where gating/flooring removed every effective ratio. When a voyage/product group's ratios no longer sum to ~1.0, the fix cascades through two fallback levels:

(1) use the all time supply-name split for that ship/product, re-normalized to sum to 1.0, or

(2) if no all time ratio exists, split evenly across the supply names present in the group.

Ben F.
Supply Chain:

**Weekly Status — Apr 24–30, 2026**

**Finance Tracking Tool Refactor** (PRs #294, #295, #297): removed 50GB partition misconfig, added persist/broadcast, made NB09 proration recompute idempotent. Row-level parity vs. production monolith pending.

**Full IBP Code Refactor:**

**Table-suffix refactor (T02–T28)**: 28+ notebooks across RCI/CCI, SSC, and Supply now widget-driven with AC-DC-1 SSO safety guards on DEEP CLONE / archive ops. Parity harness extended for multi-schema + segmentation.

**Why this matters**: This code helps set the stage for refactoring other parts of IBP Code allowing for us to test the refactored code against production tables so we don’t overwrite production tables allowing for validation comparioson.

**New Revenue Forecast Daily Table** (PRs #334, #336–#340): new daily pipeline overlaying PCD actuals from pax channel revenue with revenue planning forecast data from prd_gold.ibp.reveneue_forecast which is a view from EDSSP

**Silversea Demand Model Rebuild**: Feature engineering of 289 features complete. Feature selection underway.

**SharePoint Graph API**: legacy Office365 replaced (#253); Enhancements made on upload/download hardened with timeouts, retry, and 2h wall-clock budget (#290, #310, #321) to prevent new intermittent issue of writing to sharepoint operations never completing.

**Next week**: Finance Tracking Tool refactor validation continued, continued refactoring of rest of IBP code, continued work on Silversea demand model rebuild.

**Nicolas**

**Supply Chain:**
**Project: RCI/CCI HF&B Order Creation Dashboard MLS Discrepancies**
[DOE-1725] IBP | RCI/CCI HF&B Order Creation Dashboard MLS Discrepancies - Jira

Completed:

**Source-level voyage comparison**: Compared voyage numbers across the two MLS sources and found only 1 common voyage in the raw (unfiltered) data, confirming significant divergence between them. Built out voyage_no extraction logic in SQL to enable a proper join.

**DBR version troubleshooting**: Traced PySpark errors in the validation notebook to a DBR version mismatch between the interactive cluster and the Job DBR, then re-ran the notebook on the matching version to silence the errors.

**Validation ****notebook**** rebuild**: Started from scratch on the testing modifications, diagnostics, and source/target comparisons so that outputs could be compared reliably, working through Copilot-introduced errors along the way.

**Cluster bottleneck escalation**: Flagged the cluster downgrade requirement to Camila, noting it forces a restart of all ongoing work every time the notebook runs, and requested a dedicated cluster or job compute.

Ongoing:

**Awaiting Yan's email reply**: Pausing validation work until Yan responds to the email regarding the single-voyage dashboard finding, after which findings will be escalated to Paolo and team for additional input.

**Notebook simplification**: Considering a less involved validation approach given the notebook has grown to ~300 cells and is difficult to run end-to-end reliably.

**Project: Beverage Product Name Label Extraction (AI POC)**
[DOE-1669] IBP | Remove labels from beverage product names - Jira

Completed:

**Phase 2 scoping**: Met to define Phase 2 deliverables: attributes including CATEGORY_LABEL, nano categorization (NANOCATEGORY_NAME), spend/consumption-related columns, and UOM (with anticipated cross-brand inconsistencies).

**Procurement item master investigation**: Began mapping the market field from prd_silver.ibp.procurement_market_master to Yan's mapping file, identified misaligned values, then determined a proper mapping is feasible using downstream values and planned to implement SharePoint download logic to support it.

**Source table clarification**: Confirmed no difference in distinct products between qa_gold.ibp.procurement_item_master and prd_gold.ibp.procurement_item_master, and questioned the rationale for defaulting to QA.

Ongoing:

**Comprehensive ETL build**: After clarifying specs with Yan, building out the ETL to create a comprehensive table delivering an updated version of the first draft sent to Matt's team, targeting delivery by Monday.

**Project: SSC Uniforms Model — Ratio Feature Corrections**
[DOE-1644] IBP | Review Aggregate Calculations for Gender/Generation Ratios - Jira

Completed:

**Code generation review and push**: Reviewed Copilot-generated code for the planned changes (bi-monthly spine, gap-fill via rolling averages, broadened report-date-to-voyage association window) and pushed updates.

**Third run execution**: Continued executing the third model run through the notebook, working through code that was introduced and Copilot implementation errors.

**End-to-end pipeline run (Crew_Count_ETL.py, ****)**: Successfully ran through Crew_Count_ETL.py and ETL.py, leaving only SSC_Demand_Model_Consolidated_SHAP.py to finalize the integration.

Ongoing:

**Final SHAP model run (SSC_Demand_Model_Consolidated_SHAP.py)**: Running SSC_Demand_Model_Consolidated_SHAP.py to finalize integration of both the combinatorial ratios and gap-filled report dates, and monitoring the performance improvement before closing out the stories.

**Project: SSC Uniforms Model — Combinatorial Gender/Generation Ratios**
[DOE-1645] IBP | Introduce Combinatorial Gender/Generation Ratios for Uniforms - Jira

Completed:

**Pre-filling applied to combinatorial ratios**: Merged the gap-filling aggregation branch from DOE-1644 and applied the pre-filling logic to the combinatorial ratios, readying them for the third training run.

Ongoing:

**Impact validation**: Awaiting the third model run results to evaluate the combined effect of combinatorial ratios and gap-filled report dates on model performance.

**Project: Automated Spend Report & Consumption Fix**
[DOE-1565] IBP | Automated Spend Report and Consumption Fix - Jira

Completed:

**Yearly folder structure**: Identified the need to create yearly folders for each report type and modify the upload code to target the respective yearly directories.

Ongoing:

**Folder creation and code update**: Implementing the yearly folder structure and modifying the report automation code to upload reports to their respective yearly folders.

**Project: Spend Report Data Quality**
[DOE-1582] IBP | Spend Report Data Quality - Jira

Ongoing:

**Transfer Pair escalation**: Raised the Transfer Pair issue to Yan and awaiting her review on the email to determine the best course of action.

Mirielle T.

**Contact Center:**** **Call Volume Forecasting — Status Update

1. International & Casino Call Volume Forecasting

2. North America Call Volume Forecasting — Celebrity

Work Completed

Completed fine-tuning for unstable markets and LOBs to reach an acceptable forecast accuracy, targeting a MAPE of approximately 10% where feasible.

Focused fine-tuning efforts on the following:

International markets: France, Spain, Brazil, Italy, Ireland (IRS), Germany

North America — Celebrity LOBs: CASINO_SALES, CASINO_SERVICES, CO_SALES, CO_SERVICE,
PCP_SALES, PCP_SERVICE, WEB_BOOKING_SERVICE, CVP_GROUP_SALES, CXC_INBOUND, CXC_RETREAT

Fine-Tuning Activities

1. Synthetic Forecast Skeleton (Phase 1 / Phase 2)
The forecast is anchored on a synthetic baseline built from historical data. The growth-rate window is configurable, with tier-aware defaults (3 / 6 / 9 months for stable / moderate / unstable markets).

2. History Cleaning Options
Market-level controls were applied to improve forecast stability:

Enable/disable outlier removal, with adjustable confidence intervals.

Enable/disable smoothing of the synthetic series, with its own CI band.

Define custom outlier date ranges to explicitly handle known anomalies (spikes or dips).

Enable/disable trend features (LOWESS) for noisy markets where trend signals amplify noise rather than capture signal.

3. Hyperparameter Control
Two levels of model tuning were applied:

Tier-default profiles applied automatically based on market stability.

Model-specific overrides (model_param_overrides) layered on top when additional tuning was required.

Application Updates

Updated the Workforce Planning app with all finalized call-volume forecasts.

Followed up with Nico and the team regarding the latest updates.

Followed up with Augusto on the Celebrity call-volume forecast data.

WHY NEXT STEP: ONE RCG CALL VOLUME FORECAST (Q4)

The key limitation of the current approach is that it remains analyst-driven. For unstable markets in particular, forecasts require repeated manual tuning cycles, and those settings can drift over time as market behavior changes. This makes the process difficult to scale across a larger portfolio or to support a frequent refresh cadence.

The next step is therefore to move from a manual forecasting workflow to an automated pipeline. The goal is to operationalize the process so forecasts can run on a schedule, automatically tune per market against defined acceptance criteria, continuously monitor performance, and escalate to human review only when necessary. This transition will allow the forecasting capability to scale, remain consistent, and more effectively support downstream workforce-planning and simulation use cases.

Mirielle T.

**Contact Center:**** **Workforce Planning — North America (Royal)

Advanced App Simulation

Next Steps

Build the dependency datasets required for the Advanced App Simulation (Royal).

Build the dependency functions supporting the Advanced App Simulation logic.

Erlang A Headcount Modeling (Royal)

Next Steps

Calibrate daily call-volume forecasts to align with 30-minute intervals.

Test and validate the Erlang A model at 30-minute granularity to ensure accuracy and stability.

Call Volume Forecasting — April 30, 2026 (Summary)

Completed fine-tuning for International & Casino markets and North America Celebrity LOBs, targeting an acceptable forecast accuracy (≈10% MAPE where feasible). Improvements focused on unstable markets through adjustments to the synthetic forecast baseline, history cleaning (outliers, smoothing, trend controls), and tier-aware hyperparameter tuning.

All finalized call-volume forecasts have been integrated into the Workforce Planning app, with follow-ups completed with key stakeholders.

The main limitation remains that forecasting is analyst-driven, which does not scale well for unstable markets or frequent refreshes. The recommended next step is to move toward an automated forecasting pipeline with scheduled runs, auto-tuning, monitoring, and exception-based human review.

In parallel, next steps include building dependencies for the Advanced App Simulation (Royal) and validating the Erlang A model at 30-minute granularity.

Caleb**
**CLV Update

In Progress

Engaging in ongoing collaboration with Data Solutions to productionize the CLV table, providing comprehensive documentation of the end-to-end pipeline architecture and defining specifications for the final deliverable

Configuring a CLV Genie Space populated with curated SQL expressions, example queries, and standard operating procedure documentation — enabling non-technical stakeholders to perform ad-hoc CLV analysis independently while streamlining workflows for SQL-proficient users

Supporting Corporate Strategy on the Cost of Sale initiative, evaluating potential routing strategies for alternative distribution channels

Completed

Validated current CLV input tables against raw source data from Oracle and VCAP to confirm pipeline integrity

Identified and communicated known data quality issues to Revenue Planning, specifically around channel mapping logic that shifted with the ingestion of 2025 data — a change with downstream implications for indirect cost allocation and, consequently, personalized consumer indexing

Anand Shah

PCP Pricing Automation

1. Shore Excursion Classification Pipeline — Completed & Delivered Built and ran the full automated shore excursion classification pipeline using a 3-pass LLM consensus methodology (Azure OpenAI gpt-4o-mini) with strict taxonomy enforcement against Nick Kosmo's 6 main categories / 21 valid pairs. Implemented a rules-first pre-filtering optimization that matched 81.4% of tours via keyword rules, sending only 1,300 tours through the 3-call A/B/C classification engine. Classified 8,447 tours at 100% resolution (zero unresolved) with mean confidence 0.952 and 86.7% HIGH confidence band. Ran a comprehensive Deliverable QA audit across 6 phases — all 21 taxonomy pairs valid, only 247 QA-flagged tours (2.9%). The final classification was submitted to Celebrity business for analytics usage. All proper checkpoints were applied to the categorization pipeline, which is ready to be put into automation. Will sync with Eshwar to set up the automation for product classification with a proper alerting system in place.

2. Waterpark A/B Testing (ZH01) — Dashboard Planning Submitted all sailing pairs last week as business is gradually applying new prices to test sailings. In discussions with business and teammates to plan and build a new A/B Test dashboard. The dashboard will show bookings, passes purchased, revenue, penetration, etc., reflecting the difference in principal KPIs between test and control sailings.

3. Celebrity ShoreX Analytics Dashboarding Synced with Alex from Celebrity to spearhead new analytics on shorex product sales — understanding, analyzing, and extracting insights from historical transactional data. Building a Commercial Engine Dashboard covering Price Elasticity Analysis, Booking & Cancellation Behavior, and Digital/Conversion Funnel for various shorex segments. Additionally, mocked dashboards for Behavior and Strategy of ShoreX Products including Purchase Frequency Distribution, Demand Segmentation, and Cluster Affinity views.

4. Sailing Classification & Clustering Algorithm Working with Aagam and Ignacio on a sailing classification and clustering algorithm where sailings will be classified into various buckets for use in track. This week performed EDA on sailing characteristics that can be utilized as features to classify sailings based on their booking behavior, OBR purchases, ShoreX purchases, booking window, etc. — which will eventually be used in track optimization of various sailings.

Upcoming Next Week:

·       Sync with Eshwar to set up product classification automation and alerting

·       Begin building the Waterpark A/B Test dashboard with team

·       Continue Celebrity ShoreX Commercial Engine dashboard development with Alex

·       Refine sailing clustering features and build initial classification model with Aagam and Ignacio

Kevin D.

PCP Pricing Automation

Successfully co-presented the Casino real-time CAR to the Capital Committee this week with Onboard Revenue and IT. Positive Feedback. Updated the analytics ahead of the presentation.

David Whitney

HR

Updated the CAM HR CAR to eliminate the Workforce Planning Component, updated financial stats, and included the delivery timeline phases for the CAR. Had to haggle with Data Engineering to keep CAR costs down. Gabrielle was initially firm that DE wanted to 2x increase the allocations for DE, but we made a more modest increase consistent with the new pod DS/GenAI/DE pod structure we are using in New Build.

Dave met with the technical teams today, and we’ve incorporated a roadmap into the memo that clearly outlines the expected 2026 and 2027 milestones. As part of that discussion, we shifted incremental resourcing toward Data Engineering to support the committed delivery scope, with a negligible impact to the overall CAR ask. The 12-month delivery plan is now structured into two phases across three parallel workstreams:

**Core Phase 1 (Q3–Q4 2026)** **establishes the foundational data infrastructure and core automation capabilities.** This includes ingesting and managing JDE Crew data with historical snapshots, migrating existing Excel-based planning workflows into a repeatable, automated process on αPlatform, and delivering an initial enterprise demand planning application with staffing outlooks and variance reporting.

**AI-Enabling Phase 2 (Q1–Q2 2027)** **builds on this foundation with AI****-driven enhancements across each workstream. **This includes integration of Sea Track and any additional operational data sources, deployment of machine-learning forecasts for position-level demand, contingency, and crew eligibility, and the introduction of conversational AI agents that enable planners to query policies, surface staffing gaps, and run scenario simulations using natural language.

Eddie B., Anneke

SSC Rev Mgmt:

For SSC RM, we had a conversation about implementing more complex business rules and incorporating business team feedback into an enhanced PRE Algorithm for them (being developed and tested), as well as sending a list of sailings to include voyages in 2027 not being covered by current PRE for review and addition

Their leadership is strongly encouraging them to be adopters; very different from the experience I've heard with them beforehand

Adrien in particular wants to start making bigger price changes and add layers of complexity we have in other brands. Me and Kevin were talking about how we want to handle it when Jesse comes back. Very different environment and level of visibility (like actual reports) from when he left it

Eddie B.

RCI Rev Mgmt

**Track Optimization:** So I've been sitting on the Track Smoothing until it gets pushed to production. Huge side quest on identifying how whacky RCI’s booking tracks really are, then smoothing them (Chris is implementing our recommendations). I think it'd be helpful to have time where we talk about some of these things. Your calendar is SLAMMED but it'd be valuable to have some sort of dialogue so you know what's up. Happy to type it out to save you the time and we can do ad hoc conversations on some of these. Entirely up to you. This same track smoothing exercise I am repurposing the data inputs to run it for CEL. Anastasia seems under the impression they don't need it, but her team was enthusiastic it was being looked into

**KPI Tracking:** Individually I also delivered a barebones dashboard that breaks down PRE recommendations to the Rev Strategy team on directionality PRE recommendations and what actually happened, with detailed information and examples. Part of that Goldner EDA / wild goose chase

**Category Gapping Leadership Sync:**

Updating Leadership next week on our Category Gapping strategy. I know we are getting a little long in the year for some of these deliverables and we want to start pushing things. The Tier Category Gapping is in a place that we believe is ready for production (on CEL side). They get in the habit of overextending the feedback loop, so I am coming into next week's update with the "feedback and continuous improvement is great and all but we have more than an MVP ready and need to start gathering learnings / benefits from the work". I've noticed that the CEL team LOVES the feedback loop a little too much. Perfect in the way of good sort of thinking

**"You ****Choose,**** We Choose" Upsell Strategy**

**Core objective:** maximize revenue within cabin category classes based on cabin premiums and booking distribution

**2025 estimated revenue uplift: $115M** ($75M RCI + $40M CEL); **2026 target: $23M–$35M** additional (a **20–30% increase** on existing uplift)

The model predicts trade-up behavior from GTY to Lead physical cabins, moving the entire category stack accordingly

**Primary KPI: Cat Class Spread Index (****CCSI)** — higher CCSI correlates directly with higher net ticket revenue

**Category Gapping Model — Improvements & Expansion**

**Recent enhancements** include DART (accounting for recent trends), ship class/product granularity, quad recommendations for RCI, and a trade-up encouragement rule

**Massive combinatorial complexity** drives the technical challenge: GTY-Lead alone involves **600K combinations per run**; expanding to full category tiers explodes to **540M combinations**, and full category-level gapping reaches **486 billion combinations** per run

The **2.0 model** runs 3× per week; tier-level processing takes ~2 hours for CEL alone

**Brand-Specific Approaches**

**Celebrity Cruises** uses **Category Maintenance** — pre-set category premiums maintained by automation, with the initial GTY–Lead gap provided by CG 2.0

**Royal Caribbean** uses **Category Tier Gapping** — the model runs at category tier levels, with the rest of the stack following rules informed by tier optimization

Both brands receive the initial GTY–Lead gap from CG 2.0, but diverge in how they manage the remainder of the stack

**Path to Full Stack Optimization**

**Tier-level optimization** accounts for inventory needs, dynamic trends, and trade-up encouragement to sailing-specific best outcomes

**Business rule integration** layers availability- and trend-based category-level changes on top of gap-specific rules

**Full booking curve optimization** is the end goal — charging dynamically based on projected future demand — but is currently **blocked until track optimization** is complete

Getting from tiers down to individual categories relies on **business rules** rather than full model expansion, given computational constraints

**Key Takeaways**

**Category Gapping is the revenue engine** behind the tri-branded upsell strategy, with proven uplift in the hundreds of millions and clear growth targets for 2026

**Computational scale is the primary technical barrier** — the jump from 600K to 486B combinations requires a pragmatic blend of model optimization and business rules

**Brand differentiation matters** — RCI and CEL follow distinct paths (tier gapping vs. maintenance), both feeding from the same CG 2.0 foundation

David Whitney, Mert Ersoz

Newbuild

Developed a strong presentation deck for NewBuild leadership (Harri, Alfredo). Presented the Enterprise AI Observatory to the Head of Newbuild and received positive feedback. Next steps will be to build a 5-year plan and develop a CAR with NewBuild. The material included:

**The Vision: Why Newbuild Needs Purpose-Built AI**

**Newbuild operates in a uniquely complex environment** — design-phase data is incomplete, evolving, and spread across SharePoint, email, vendor systems, and tribal knowledge. Generic tools like Copilot or Claude can't reason across this complexity.

**68% of shipbuilding firms** have adopted digital transformation, and **80%** view it as critical for competitive advantage — positioning Newbuild as an ideal proving ground.

**The Observatory is a "glass box" intelligence layer** — unlike generic AI "black boxes," it delivers auditable, citation-backed answers grounded in verified internal documents, with deep semantic context that learns from every project.

**What's Being Built**

**A natural-language AI platform** where Newbuild team members ask plain-English questions and get precise, cited answers from across fragmented data sources — turning hours of document hunting into seconds.

**Key capabilities** include a unified knowledge layer across SharePoint archives, a multi-agent architecture for complex engineering and contractual queries, role-based security, and scalability across ships, yards, and lifecycle stages.

**Cross-brand knowledge unification** — RCI, Celebrity, and Silversea documentation becomes queryable in one place, preserving institutional knowledge and accelerating onboarding.

**Pilot Status & Architecture**

**~95% complete**, targeting mid-Q2 2026 delivery. The AI engine is **100%** done; the web app and document ingestion are at **95%**.

**Fully built in-house** on RCG Azure — no vendor dependencies. Stack includes Next.js frontend, FastAPI backend, LangGraph engine, Azure AI Search, and Databricks.

**10 enterprise data sources** identified: Newbuild SharePoint and SQM Policy are **fully indexed**; i95 Platform and guest complaints are **in progress**; shipyard systems (Meyer Turku, Chantiers, Fincantieri) are **planned/negotiating**.

**Cost & Build-vs-Buy Analysis**

**In-house is significantly cheaper**: **$27–32K/week** vs. a vendor's **$47K/week** (40–45% savings), with RCG-owned IP and continuous improvement rather than a one-off pilot.

**2026 delivery run-rate**: **$1.4–1.7M**; post-delivery maintenance drops to **$0.9–1.2M annually**.

**Core team** includes a Sr. Data Scientist, Sr. GenAI Engineer, and Sr. Data Engineer, supplemented by a scaling team for 2026.

**Broader RCG AI Ecosystem**

**$60M invested in AI & Data since COVID**, delivering **$550M EBITDA to date**, projecting **+$340M annually in 2026** and growing to **$600M by 2030**.

**AI tools already deployed across RCG**: CorAssist (Contact Center), TranslateHub, Medallia SEAT, SQM Policy Author, and PolicyAssist — with several more in testing.

**AI workbenches available**: Copilot Chat (free, ~12K users), M365 Copilot ($30/mo, ~1,550 users), Claude Enterprise ($40/mo, 235 users), and Gemini (in negotiations).

**Scaling programs** include an AI Ambassador Program (51 ambassadors), AI Academy, and a GenAI Center of Excellence at ai.rccl.com.

**What Leadership Is Being Asked For**

**Designate 5–10 pilot users** from across Newbuild teams for structured feedback after launch.

**Executive engagement with shipyards** (Meyer Turku, Chantiers, Fincantieri) to negotiate data access.

**Visible executive sponsorship** to drive cross-team adoption.

**Full project funding decision** (~$1.2–1.5M) based on pilot results to move from PoC to enterprise platform.

**Key Takeaways**

**This is a strategic investment, not a short-term ****ask** — the Observatory is designed to become the foundation for how Newbuild operates long-term, with potential to benchmark for the entire cruising industry.

**The pilot is nearly complete** and built entirely in-house, giving RCG full IP ownership and a **40–45% cost advantage** over vendor alternatives.

**RCG's broader AI portfolio is already delivering massive returns** ($550M EBITDA), and the Observatory extends this proven playbook into Newbuild's uniquely complex domain.

**The critical path now runs through leadership** — pilot users, shipyard data access, sponsorship, and a funding decision are the four gates to scaling.

Mert:
MIAP
Presented the Digital Twin model solution to the Fuel Finance team for the first time and received very positive feedback. Our teams will now be working much more closely. We have largely completed most of the scope, and we agreed to deliver one ship class every two weeks to the Fuel Finance team, during which we will tune the model parameters.
Reviewed F&B Databricks Genie use cases with the IT Shipboard team at their request, in preparation for a presentation to Jason.
Held the monthly GMO AI review. We agreed that the MIAP app is not a fully standalone application, and all content currently duplicated within the GMO app will be taken down. We will be granting access to a larger group across the fleet and shoreside. These agreements follow significant refactoring work on the MIAP app, and the GMO team was impressed with the new look and structure.
Met with the AVP of Navigation, Captain Henrik, and the Senior Manager of Safety, Francisco, to collaborate (“vibe code”) on the MIAP app under our supervision. Captain Henrik will be building Project Polaris, which will help visualize the global port data vetting process. This effort can later be handed over to the Data Governance team to oversee the corporate port/berth database. Francisco has started building Genie-based AI agents for Safety, is embedding them into the MIAP app, and is also helping improve the app’s overall look and feel.
Met with the Head of Asset Management, Patrick, who agreed to fund a Senior Data Scientist for 6–8 months, with additional funding planned for next year. This role will be funded through the existing AMOS CAR this year and will support foundational work for predictive maintenance. We will begin by migrating all Asset Management Power BI dashboards into the MIAP app.
Started developing a YAML-based pipeline that allows the Fuel Finance team to easily edit forecast parameters for the Digital Twin model.

Mahshad:
MIAP
Investigated deviations on OV, CS, and SM HVAC systems; discussed findings with the engineering team and are still awaiting contact with the ships.
Worked on the VY HVAC model.
Addressed data issues in the OFB ST model.
Attended the deployment meeting.
Fixed chiller pipeline issues.
Resolved several plotting issues in the MIAP app.
Added the COP model plot and re-enabled the HVAC agent; improved the HVAC agent prompt for better presentation.

Ram:
MIAP
Analyzed request counts and query patterns, focusing on request frequency and size, and met with Wärtsilä to explore potential improvements on the RCG side as well as changes in approach on the Wärtsilä side.
Worked on REST API dashboard queries, which are also used for vendor chargebacks.
With support from the platform team, identified that serverless compute costs were higher than expected. Further analysis revealed that a compute change had resulted in duplicate rows; the query was corrected accordingly.
Planning to meet with Alejandro from the platform team next week to validate cost calculations and prioritize any required changes.
Was on leave for two days due to a doctor’s appointment.

Arya:
MIAP
Worked on building endpoints for the SORA app.
Focused on SFOC curve tuning, primarily for Quantum-class ships.
Contributed to the Digital Twin presentation.
Met with Data Engineering to demonstrate how Databricks failure monitoring can be implemented through Teams.
Worked on ST-related job failures and removed IC as the reference ship, as sufficient data is now available.

***Cristian V., David M., Osvaldo V., ******Danusio****** G., Rodrigo B., Erick A.***

**PCP**** ****MyCruise**** Recommender**

**Infrastructure / Postgres & API *****(Cristian V.)***

**ForYou**** coverage migration is now closed out.** Last week's API expansion (memory 95% → 52%) is now formally **Completed** — Cristian confirmed all recommendations are served from Postgres rather than API memory, eliminating the 42% empty-response rate on same-port requests. The same migration cleared the long-open **ranking_policy**** attribute error** *(Completed)* as a side effect.

**A/B testing path settled.** Last week we were waiting on Lance for the Apigee front-end signal; this week the investigation is **Completed** — the use-case parameter will arrive inside dataframe_records per the Databricks model-serving schema. Cristian is adding API-level logging so the team can verify Lance's parameter the moment engineering wires it up.

**Hard-coded product slots ****progressing****:** the database table is now implemented and the control panel will drive it. Awaiting full integration so business-priority products (e.g., Royal Beach Club) can be pinned to top recommendation slots regardless of model output.

**ALS Improvements *****(David M.)******: ******ALS is a collaborative filtering algorithm used to recommend products based on customer behavior patterns, not product rules.****** ******Learns from user–product interactions (views, clicks, purchases)******, f******inds hidden patterns such as “customers like you also bought…******, and a******lternates between optimizing: user preferences****** and ******product affinities****** ******(hence Alternating Least Squares)***

***Why Hybris uses ALS:***

***Scales well to large catalogs and high transaction volumes***

***Handles sparse data (most users haven’t bought most products)***

***Produces personalized recommendations without manual rules***

***Typical Hybris use cases:****** ******“Recommended for you”******, ******“Customers also bought”******, ******Cross******-sell / upsell on PDP, cart, checkout***

***Key limitation (important for exec context):****** ******ALS is behavior******-driven, not context******-aware******
→ It does not ******understand:****** real******-time intent******, ******constraints (inventory, margin, substitution logic)******, ******business rules unless layered separately***

**Deliveries:**

**Re-ranking lane confirmed last week is now the active workstream.** The entry-point notebook David built last week is ready for cluster swap-in by Osvaldo and Danusio.

**Training-time optimization continues to compound:** ALS training reduced from **15 min → 12 min** this week via dataframe caching and pre-computing popular items, on top of last week's 4x Bayesian rewrite.

**LLM Reasoning Capture *****(new track)*****:** David confirmed that the LLM reasoning can be captured programmatically which means any summarization capabilities can be traced back to understand how the LLM/agent made a specific decision.

**Product Clustering *****(Osvaldo V.)***

**Last week's GPT-5 Nano result (30% → 11% disagreement) improved further** to **9.9%** this week using GPT-5.4 mini and shorter 2–3 word category names. Active-products clustering is effectively converged and now in a holding pattern pending downstream evaluation through David's recommender.

**Last week's catalog-coverage gap is now scoped as a discrete deliverable.** David's training table covers ~96K rows (37K Shorex) but Osvaldo's categorization only covers the ~6K active products. A separate task was opened to **rebuild the categorization including historical (inactive) products active any time since 2026-01-01** and re-cluster the expanded set. Risk Erick flagged: historical products may lack descriptions; he has a fallback table ready if blocking.

**Schema-alignment with David's recommender** is in progress — Osvaldo got one ALS experiment to run end-to-end (~20–30 min) with the new product clusters.

**Geographic visualization** *(Completed)*: top-10 categories per port plotted using port coordinates. Follow-up: building an interactive **D3.js map with zoom** rendered inside Databricks via displayHTML(...), seeded from Erick's demo snippet.

**Guest Segmentation *****(******Danusio****** G.)***

**Phase 2 cluster work is now being evaluated downstream.** Following last week's MLflow-instrumented Phase 2 setup, Danusio is running the ALS training notebook against the new booking-clusters table this week — only fitting ALS, not refitting clusters.

**Cluster-explainability:** *(In progress)*

**Apriori**** Model *****(Rodrigo B.)***

**Last week's offline-harness plan ****has converged**** on a multi-model approach.** The CF + CF-by-product + Apriori combination achieves **100% coverage** and improves all metrics; small carts (1–2 items) are where it adds the most.

This week the focus shifted to **generating pre-computed recommendation tables** modeled on Cristian's table format, so the combination strategy can be served from a precomputed lookup rather than computed at request time.

***Erick A., Rodrigo B., ******Danusio****** G***

**Project Axiom — Voice 360**

**Email Reports **

**Rodrigo ****B. —**** Port Email**

**Last week's venue-misclassification fix is now closed.** The replacement function was expanded across David's full venues JSON *(Completed)*. Matt's Tuesday workshop happened with Erick attending in person.

Open work continues on filtering reporting_topics_deep comments to only those specifically mentioning the port — reduces noise in percentage calculations.

**Rodrigo ****B. —**** Shorex Email** *(new track this week)*

Two new tracks opened: (1) **rebuilding metrics off the dream table** (instead of all records-with-comments) and tightening the LLM summary prompt; (2) sending a sample of the input comment table to **Anne Marie for input-quality review** before further prompt iteration.

**Rodrigo ****B. —**** Closeouts**

**Gratuity Topic Analysis for Alessio** *(Completed)*

**Danusio**** ****G. —**** Shorex ETL**

**Exception handling shipped** *(Completed)*: Failures in one notebook can no longer block downstream notebooks in the pipeline.

**LLM Reasoning Capture** *(**Danusio** G., David M.)*: parallel research tracks confirmed reasoning can be captured programmatically. Planned application: GSO and Shorex pipelines (Danusio) and the recommender (David). Business flagged as high-leverage for explainability.

Picking up from last week: Eduardo reviewed Danusio's shorex-keyword integration, sent suggestions (all implemented), verified coverage against his hazard list (most already covered, two missing words added).

**Regression for Drivers of Port Satisfaction *****(Rodrigo B.)***

**Medallia Score Regression for Matt** *(in progress)*: Pursuing **sailing-level aggregation** (mean per factor per sailing) for a simple regression to satisfy Matt's request, with the caveat that the result will be statistically weak.

**Symphony of the Seas Dry Dock Research *****(Erick A.)***

**Symphony of the Seas Dry Dock proposal** *(Completed, 24-hour turnaround)*: at Gang Wang's request, Axiom analyzed 80,000+ Medallia consumer-survey comments for Symphony, producing a comprehensive pain-point report (plumbing, pool, stateroom, and more) that fed directly into the Dry Dock proposal. Matt Denesuk has heard Figgis and other RCI leaders praising this report unreservedly!

**Symphony external-source deep-dive** *(Completed, 24-hour turnaround)*: Gang's follow-up — building on the port-level forum scraping capability prototyped last week, this expanded to Cruise Critic reviews, Cruise Critic forums, Trip Advisor reviews, and Reddit. Comprehensive Symphony pain-point report delivered to senior leadership.

**Target Setting / Onboard Revenue Forecasting *****(Erick A.)***

**Last week's framework extension is now a v1 model ready for ****broader-team**** review next week.** Data shape clarified: one row per ship + sail date + market with revenue split by category (INTERNET, SHOREX, DINING, etc.). v1 forecasts **total revenue by category** (sum across all markets). MAPEs: **Internet sub-20, Dining sub-20, Shorex ~30–40**. Market-level forecasts are noticeably harder and deferred to a follow-up.

Stakeholder: **Gang Wang (Hotel Operations)** — feeds Track revenue planning

Ignacio V.

PCP Pricing Automation

CEL Beverage PRE/DM (2-Phase Modeling w/ MNL & Clickstream)

The notebooks for Garrett’s modeling & optimizations were shared with me. They are being studied thoroughly to better understand all the detailed steps and nuances behind the approach. Areas of improvement are being identified & planned next steps are being brainstormed for providing a v1 of the CEL PRE/DM.

RCI | Hybris | Automate Waterpark Promo Uploads

There have been attempts at copying over the waterpark price recs from Oracle from the business team, but the unoptimized view table is leading to a lot of issues when trying to read from it. I am staying in contact with Jorge to see if an alternative accessible table can be provided.

RCI | Create Piecewise Linear PRE optimization for Current WTS Only

Some initial exploration of this was started. Meetings were had with Lamis to walk through this strategy and try brainstorming how it would be used in the PCP/OBR side. However, due to shifting priorities to the MNL model being explored with CEL using clickstream data, this was deprioritized.

RCI | Replicate, clean, and improve Track from business team

Some work was started on replicating and improving the track used by the business team, primarily involving grouping by meta, sail nights, month, ship class, and WTS, followed by taking into account demographic data to (loyalty, casino, US pax, and age groups) take into account the addressable population. The plan is to create better groupings with a reasonable threshold for number of samples to map back to from STLY (avoiding small number of sailings per group). This was started but to be done by someone else as my priority has shifted to the Linear Piecewise PRE development for OBR.

Recurring Business Meetings & OBR DS Meetings

meetings were had with the business team to share v2 of promo automation, including the added AND group functionality for sailing tags, NAME automation for internal tracking of how work is split in promo uploads, and the new table storing copies of all batches of promos uploaded through automation (with the exact same format as the sheet for easy copy-pasting and also with a timestamp corresponding to the time of the workflow upload run)

meeting had with Alex, Gaby, and Garrett regarding next steps on CEL Bev PRE, focusing on exploring a new MNL model combined with a model for predicting pageviews, taking a new approach to a PRE/DM that incorporates clickstream, data. Importance was placed on treating different customer segments differently, and having the price recs result in different targeted prices for different customer segments on the same cruise (e.g. cat class, market, loyalty, age, etc)

David Whitney, Glen-Erik

SSC PROPEL

*  **SSC PROPEL ****sCAR**** Refinement**: This week included active iteration on the **SSC PROPEL exploratory ****sCAR**, including executive-level positioning of ShoreX growth economics under *The Luxury of Choice* and clarification that a **full CAR will follow completion of the exploratory ****sCAR**** phase**.

*  **Financial**** Narrative Alignment**: SSC leadership feedback focused on **tightening revenue framing and long****-term value articulation** (take rate, margin expansion, and average spend growth), ensuring the sCAR memo is aligned with investor- and capital-committee expectations.

Glen-Erik C, Doug. B, Javier, Santiago

CEL PROPEL

Current conversations on PROPEL (CEL) with Alex Correa, Glen-Erik, and Doug are centered on a growing concern that **Q1 performance cannot yet be credibly measured or defended**, despite PROPEL being live. CEL leadership is increasingly uncomfortable advancing decisions, messaging, or scale without **finalized, test/control****-clean uplift measurements** that clearly explain what portion of Q1 performance is attributable to PROPEL versus noise, business rule changes, or offer contamination. As Q1 has closed, the absence of decision-grade measurements is now viewed as a credibility and governance risk rather than a technical timing issue.

From the delivery side, Glen-Erik has been explicit that the lack of Q1 numbers is **intentional, not accidental**. Measurement logic is being re-worked to ensure sailing-level attribution is production-grade, offer overlap and contamination are addressed, and results will not require later back-casting or retraction. The team is prioritizing stabilizing measurement foundations before publishing results, even though this delays Q1 readouts, to avoid undermining long-term trust in PROPEL’s reported impact once results start informing executive and financial decisions.

Doug’s involvement has focused on the **resourcing and prioritization implications** of this measurement gap. With a disproportionate amount of senior DS/ML capacity being pulled into measurement hardening, the absence of Q1 results has become a **gating issue** for decisions on staffing, roadmap acceleration, and further CEL enhancements. Across all conversations, the shared implicit position is that **PROPEL should not be treated as fully “run****-the****-business” for CEL until Q1 uplift can be clearly explained, defended, and consistently reproduced moving forward**.
