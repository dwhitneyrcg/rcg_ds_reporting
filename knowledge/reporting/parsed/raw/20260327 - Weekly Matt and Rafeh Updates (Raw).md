**Douglas Bedell**

**RCI**** Revenue Management**** | Inventory Automation Elevated ICGTLD Limits | MAR**

o   **Status**: This ticket is complete as of **03/23/2026**

o   **Deliverables**:

o   Analysis of historical replenishment actions show RCI suffering the same issue that was detected in Celebrity’s process in Aug 2025.

o   When berthing occurs, AS400 does not immediately update outstanding GTY offered and booked counts. This housekeeping occurs each evening between 10pm and 2am in the RM_90 IT processes.

o   To take advantage of AS400 internals, FIT berthing was moved from 6am to 9:50pm daily. Once berthing occurs, AS400 cleans the ICGTLD table afterwards. An additional replenishment run was added for 2am daily which sets limits using the corrected booked and offered counts.

o   Validated successful runs occurred following process updates.

**Michelle Manfrini**

**CEL Revenue Management: Category Gapping**

Team requested additional features to be tested and added. This involved calculated new columns in training data, retraining models, created predicted grids with new features. The more features added, the more the grid will explode therefore it is important to only add columns that truly add meaningful signals to the model.

**Michelle Manfrini**

**RCI Revenue Management: Category Gapping**

Testing updated RCI notebooks in dev and validating results. Will confirm outputs are approved by business before testing in qa.

** **

**Ignacio Villasmil**

**PCP Pricing Automation**** | Hybris | Modify table of extracted promos from Hybris**

**Comment (Mar 25, 2026) – Ignacio Villasmil**

**Status**: This ticket is complete as of **03/25/2025**

**Deliverables**:
The tables were modified to remove duplicate rows present for promos in Hybris. In addition, for promos with status PUBLISHED, only the highest version number is being kept; older versions are filtered out for clarity.

**Delays**: None

**Nest steps**: None

**Jesse Bausell**

**SSC Revenue Management**

**SSC Handoff** – I have had a series of meetings this week to prepare for my upcoming leave of absence for military training. I have met with members of the Data Science team (as designated by my managers) who will be responsible for advancing SSC data analytics in my absence. I have informed my stakeholders of my upcoming absence, taken their feedback for future projects, and provided instructions to everybody who will be involved in running SSC analytics over the upcoming month. I will be available meet with stakeholders and my colleagues and stakeholders on Friday if they need me.

**Compute PRE Metrics** – Per the request of SSC stakeholders, I computed up to date PRE performance metrics with the help of SSC Revenue Teams. Metrics include ab-test KPIs (e.g., revenue for PRE vs. non-PRE sailings), number of price points impacted by PRE recommendations, and percentage of price recommendations accepted by SSC Revenue Analysts.

**Upper Suite AB Test** – I am in the process of designing an ab test for mid-range upper-level SSC suites. I will pass off my progress to Eddie on Friday.

**Aagam Shah**

**PCP Pricing Automation**** | OBR | AB Test Analysis (Low Price Sailings)**

**Comment (Mar 26, 2026) – Aagam Shah**

This week I completed the following:

**Data Extraction and prep:** Gathered the data for alcoholic and non-alcoholic passes for all 12 test sailings, including associated revenue metric (penetration rate and revenue uplift). I also developed a customer-level view incorporating datapoints such as category class, Group/FIT designation, loyalty tier, and age, providing a granular view of the impact of price change on each of these segments.

**Statistical Significance and Impact Analysis:** Ran a statistical significance test (one sided stratafied permutation test) that gave the following results:

Penetration Rates:

Control mean: 10.5131%

Test mean: 13.1525%

Abs lift: 2.64%

Rel lift: 25.11%

I further did an analysis to see the lift of penetration rate across cat-clases, loyalty tiers, age groups, cruise frequency, Group vs FIT

**first test on RBC with lower prices is showing a 30% lift in penetration and a 13% lift in revenue. This is a big WIN and will likely be presented up to Michael Bailey.**

**Presentation:** Developed a presentation to showcase the results of the test to the leadership team.
Have a stakeholder meeting tomorrow (03/27/2026) to showcase the results of the analysis.

**Aagam Shah**

**PCP Pricing Automation**** | OBR | RBC Dashboard v2**

·       **(Mar 23, 2026) – Aagam Shah**

**Blocker:** The keys to access the data have expired and cannot make changes to the tables. Raised a ticket to the platform team to solve the issue.

·       **(Mar 26, 2026) – Aagam Shah**

This week I focused on the following:

o   **Analysis of Bundles and Passes:** Provided my recommendations on how to target customers for RBC Passes and RBC Bundles along with the context

o   **Minor Tweaks from v1:** Completed the minor tweaks based on stakeholder feedback (re-ordering loyalty tier columns, renaming a few charts)

o   **Data Fixes:** During the update process, I traced the failure back to inaccurate data in a few tables feeding customer age and loyalty tier. I identified the problematic records, addressed the data quality issues, and implemented a fix to ensure the dashboard calculates the customer age successfully and considers all customers

David Whitney

RCI Revenue management

Problem: Not trying to make a big deal of it, but the AI/data teams are faced with potential loss of Sharepoint access starting next Thursday with Azure ACS retirement (). This will effect **all** production pipelines for Data and AI teams that regularly share and ingest Sharepoint data for our business stakeholders. This would particularly impact Revenue Management. I've been making noise **for 1.5 years** on the ACS retirement topic, informing Ajeet and requesting a permanent solution. The Data Science and ML Engineering team do have a GraphAPI solution and we have shared with other teams, but we are working with the IAM team (Nathan Huckabee) and Platform Engineering (Carlos & Marcio) to ensure this solution has the right read/write access.

Wanted you to be aware and I'll include in my weekly. We "should" have this all fixed by next week, but it's a blood-bath if it doesn't and will bring down a lot of pipelines. Trying to make sure this doesn't happen. I informed Moez and mobilizing to see if I can help James, Ajeet, and Pascale get everything to IM to minimize the potential impact.

David Whitney

IBP Supply Chain

Based on this week's IBP Senior Steering Meeting, there is still ongoing misalignment between GMO (Operations), Supply Chain, and the IBP Finance Transformation teams. In particular, IBP and Supply Chain are not fully aligned with execution levels below our senior stakeholders (Jessica, Jim, and Brian Sorensen). Teams under Jim Wells, including Brian Voldsgaard’s group in Supply Chain, as well as Patrick van Zandwijk's team under Brian Sorenson in GMO, have raised substantive concerns about the current state of AMOSX data. Addressing these gaps will require meaningful data remediation, and if not managed carefully, could introduce operational risk to achieving GMO cost-savings this year.

To make progress while we work through the broader data issues, the initial focus will be on consumable products that do not require complex ISO-based data tag mapping of raw material components to GMO physical assets (e.g., HVAC, engines, azipods, boilers). This should allow IBP and GMO to partner more effectively in the near term and identify actionable cost-saving opportunities, while we continue to improve overall alignment and data readiness. I have also asked that both Matt Denesuk and Moez Hassan are included in future. IBP Steering Meetings.

David Whitney

IBP Supply Chain

There is some continued misalignment around roles and responsibilities for rebuilding the AMOSX data on AlphaPlatform, largely driven by ambiguity between what constitutes core AMOSX data versus downstream “operational” datasets. In practice, some teams have viewed the blue AMOSX datasets as operational, while others consider them core GMO datasets. The Data Science team has been working to facilitate alignment across the working groups as we sort this out.

Ultimately, Charlie Sebelle, as the AMOSX business owner in GMO (under Patrick), is the authority on the business domain logic that underpins the SQL used to rebuild the AMOSX views, with Mert supporting that effort. While a subset of these views is required for IBP, the AMOSX datasets themselves are enterprise assets intended to support both GMO and IBP initiatives. My understanding from Pascale is that these datasets would live in the Marine environment and be exposed to IBP teams. Ownership for rebuilding the core AMOSX datasets on AlphaPlatform still needs to be formally assigned by Data Engineering, after which the data must be validated by Charlie or a trusted delegate.

We are aligned that subsequent operational views built on top of the core AMOSX datasets sit with Gabriele’s team; however, responsibility for the core datasets themselves remains to be finalized. I understand Yan has engaged with Charlie’s team on queries, and Gabriele’s team has rebuilt several key tables, but we need clarity from Charlie on overall intent and next steps.

To address this, I’m setting up working sessions with Charlie and Patrick to capture GMO’s perspective, followed by a joint discussion with Yan, Charlie, and Data Engineering leadership to align clearly on ownership, scope, and sequencing. As of yesterday, alignment was not fully established even within Data Engineering, though PI planning took place and Pascale was planning to drive clarity.

Either way, we will get to a shared understanding across teams and provide clear direction on who is responsible for what—and when—as we continue to improve alignment and execution.

Glen-Erik & Javier

PROPEL (CEL)

**Key Business Concern (Alex / Rafeh):**

The PROPEL measurement and dashboard capability is materially behind expectations, with no reliable read on performance as the quarter closes. Despite prior alignment on timelines and minimum requirements, progress has been slow and overly complex, resulting in a lack of usable results and eroding confidence that the program is being adequately supported in its current “maintenance” phase post-CapEx.

More specifically:

**Urgency & missed timelines:** The agreed deadline has already slipped, and with Q1 ending, there is still no functional measurement output beyond theoretical demos. This creates risk to leadership confidence and storytelling around PROPEL’s contribution to a strong OBR quarter.

**Over****-engineering vs. delivery:** There is concern that the team is “reinventing the wheel” by introducing unnecessary complexity (e.g., highly customized control logic), rather than restoring a working, pragmatic measurement solution that meets core business needs.

**Clear minimum requirements not met:** At a minimum, the business needs the ability to measure conversion and lift overall, by business area, and across key passenger segments (demographics, propensity deciles, etc.), even if multiple methodologies are required due to changes in test/control design.

**Loss of prior capability:** A previously working measurement approach (built before the control framework change) broke in January due to data flow and performance issues, and its repair stalled after key personnel changes, leaving a two-month gap with no replacement.

**Resourcing and leverage concerns:** While confidence in Glen-Erik remains high, there is concern that he is not getting sufficient leverage or support—particularly from Javier—to move from design to execution.

**Broader structural question:** This situation is surfacing a recurring issue around what “maintenance” looks like once a program moves out of active build mode, and whether current operating models are sufficient to sustain critical capabilities like measurement.

**Bottom line:**** **The business believes PROPEL has a strong success story, especially given Q1 performance, but that story is at risk without timely, credible measurement. The ask is to quickly reset, simplify where needed, reassess support and cadence, and get back to delivering tangible results—without discounting the strong partnership built to date.

**Meeting Highlights (How DS+ML Engineering are fixing this):**

**New Methodology: **The new PROPEL measurement methodology evaluates impact at the **offer****-category level** and only counts **purchases made after a guest is first exposed to an offer**, ensuring true apples-to-apples attribution. Guests are classified as **test (discount offer)**, **control (awareness offer)**, or **organic** (purchases made before any relevant offer or with no exposure), and only post-exposure purchases in the **same category as the offer** are included in uplift calculations. Results are normalized using **passenger cruise days (PCDs)** so uplift reflects weighted economic impact rather than simple averages, allowing aggregation across ships, categories, and time periods. This approach removes prior over-attribution caused by counting unrelated or pre-offer spend, supports cleaner comparisons between awareness and discount strategies, and enables more actionable, category-level insights while still rolling up to a defensible top-line view of financial impact.

**Analysis of Offer Impact Methodologies:** Glen-Erik, David, and Nelson discussed the differences between the old and new methodologies for measuring the financial impact of offers, focusing on how purchases are attributed to test and control groups and the implications for interpreting uplift and revenue results.

**Financial Impact and Uplift Calculation:** David pressed for a clear, top-line financial metric to communicate Propel's performance, prompting Glen-Erik and Nelson to outline how uplift is calculated and how it can be converted into revenue figures for leadership reporting.

**Preparing for Leadership Presentation:** David guided the team on how to frame the results for an upcoming leadership meeting, stressing the importance of a positive financial narrative and readiness to defend the methodology if results are less favorable.

**Action Items and Next Meeting Planning:** The group agreed on specific next steps, including generating revenue-based charts and refining baseline definitions, and scheduled a follow-up meeting to review progress and finalize the leadership presentation.

**Follow-up tasks**

**Financial Impact Calculation: **Calculate and present the total revenue impact of Propel by converting uplift metrics into dollar values for all ships and categories, including a quarterly summary for leadership review. (Javier, Glen-Erik)

**Baseline Comparison Analysis: **Identify and prepare a baseline group of guests who were eligible for offers but did not receive either a test or awareness offer, and compare their results to current test and control groups. (Glen-Erik)

**Historical Data Comparison: **Calculate the total revenue using the old methodology/table for 2025 data to enable comparison with the new approach. (Glen-Erik)

**Meeting Scheduling: **Schedule and confirm a follow-up meeting for Monday at 10:30 AM to review results and prepare the presentation for leadership. (Glen-Erik)

Ayon Ghosh

**WOW Update – 3/27**

**Cold Start Architecture:**
Successfully developed and integrated all modules for a new cold-start architecture, including support for entirely new ships with no historical data, while preserving existing use cases. This redesign improves efficiency and reduces runtime and compute load by approximately **50%**. Integration testing is currently ongoing.

**Bar Forecast Pipeline Fix:**
Resolved a major issue in the Bar forecasting pipeline affecting **150-bar forecasts across ships**, restoring accuracy and stability.

**Expanded Forecast Planning:**
Planning to launch a new **all****-day forecasting framework** for each venue, ship type, and menu. Development is scheduled to begin next week. The ALL day forecast is a total forecast independent of meal period forecast that we developed ...this will be applicable for all recipes/ all venues/ all ships. this will be a guidance of all day consumption in advance.

**Interport Models & Pipeline:**
Ongoing code review and finalization of interport models and associated pipelines to ensure robustness and production readiness.

**PLU Mismatch Report:**
Successfully deployed the PLU Mismatch report and conducted a detailed walkthrough with stakeholders. Currently incorporating feedback and refinements based on business team recommendations.

Ben Fowler & Camila

**IBP ****Supply Chain:**

**Delivered PowerPoint slides for Shipboard visit on Beyond on 3/29 showing the impact of using all consumption data up to date of pipeline run (rather than only through end of last month) on products where consumption in the current month spiked and how the mid month consumption data correctly raises future demand forecasts on select products with spiking recent consumption on Beyond. Also analyzed model accuracy by voyages and overall on Beyond and provided an overview of features considered and included in feature selection.**

**Validated the new refactored code in our largest notebook is now correctly aligned with production code. Productionizing the refactored code which provides following benefits:**

**About 3 hours compute time. **

**Easier to maintain and read. Refactored about 9000 lines of code into 9 notebooks all which work cleanly. **

**The orchestrator notebook of the 9 notebooks has memory built in where if any of the 9 notebooks were to fail, a code change can be made in the failing notebook and when the orchestrator notebook is restarted, the successfully completed notebooks will not rerun provided this is done within 24 hours of the original run, to allow for production code edits without wasting compute time.**

**Future Work: Have found Photon compute cluster will likely reduce compute time by more than 2x on 3 of the 9 notebooks. Now that the code is broken up, we can target Photon on the code that has greater than 2x compute time benefit, reducing compute cost and further increasing code efficiency.**

**Future Spend Phase 3 **

**Created future spend per day phase 3 that allocates daily procurement spend at the product level by joining demand forecasts with purchase order data, enriching with GL accounts, cost centers, and department codes from consumption records**

**Added day-type multiplier: spend allocation now differentiates between SEA and PORT days so that each day type gets weighted spending rather than a uniform average**

**Added DEPARTMENT_CODE to join keys: previous joins on product/ship/voyage alone were producing inflated (duplicated) spend values when the same product appeared under multiple departments; adding the department key eliminated the Cartesian expansion**

**Added actual consumption reconciliation from consumption report: for FUTURE (beyond) sailings, the CALC table now pulls real daily consumption (LIVE_QTY, VALUE_RECONCILE) from the consumption checkpoint table keyed on (LOCATION_NAME, BEGIN_DATE, PRODUCT_NAME_NUMBER, reconcile_day), so those columns reflect what was actually consumed on each specific day. PAST rows retain their original per-day actuals from P3**

**Added voyage-level AI predictions from snapshot_live: for PAST (already-sailed) rows, TOTAL_VOYAGE_DEMAND and Total_AI_Prediction_Value are now sourced from order_creation_snapshot_live (the model's actual prediction before the voyage sailed) and distributed proportionally across days using normalized DAY_MULTIPLIER, so they sum exactly to the voyage-level forecast. FUTURE rows keep P3's original multiplier-based prediction. snapshot_live is scoped to P3 voyages only to prevent cross-ship row explosion**

**Added prediction redistribution to align with consumption days: for FUTURE products that already have actual consumption recorded, predictions are redistributed proportionally to the days where consumption occurred (weighted by LIVE_QTY), so that day-level prediction vs actual comparison is meaningful. Products with no consumption yet keep the original DAY_MULTIPLIER distribution**

**Added non-consumed product rows: products that the AI model predicted but were never consumed (not present in P3) are now included in CALC. These rows are cross-joined with a clean voyage itinerary (built via groupBy to avoid product-specific DAY_TYPE/DAY_MULTIPLIER duplication), assigned DAY_TYPE='non_consumption' and equal 1/TOTAL_VOYAGE_DAYS distribution, with VALUE_RECONCILE=0 and LIVE_QTY=0. Added after the consumption join to prevent spurious matches**

**Dropped GL_NUMBER, GL_DESCRIPTION, DEPARTMENT_CODE, DEPARTMENT_NAME, and ALT_ADDRESS2 from the CALC output: these detail columns are now handled downstream in the scorecard enrichment rather than carried through at the per-day-per-department grain. Aggregated product consumption across departments to product/day grain to ensure CALC captures consumption from ALL departments**

**Production Order Scorecard **

**Rewrote GL account enrichment logic: replaced the old simple fallback join with a voyage-aware approach: GL accounts and cost centers are now resolved per (LOCATION_NAME, PRODUCT_NAME_NUMBER, BEGIN_DATE) instead of just product, ensuring each voyage gets its correct GL. Added parsing of ALT_ADDRESS2 field to extract ACTUAL_COST_CENTER and ACTUAL_GL_ACCOUNT from dot-delimited address strings, with regex guards for various address formats**

**Added consumption deduplication after the outer join with consumption_df: when multiple baseline rows (e.g. different MICROCATEGORY) match the same consumption row, the outer join duplicated VALUE_RECONCILE, CONSUMPTION, and LIVE_QTY. Added a window-based rank by (UNIQUE_ID, DEPARTMENT_CODE) ordered by TOTAL_VOYAGE_DEMAND desc, keeping consumption values only on the first row to prevent double-counting**

**Override Tracking **

**Rewrote override_tracking to derive its sailing date range from the override baseline table: instead of filtering for completed voyages (SAILING_END_DATE < current_date), it now reads the min(SAILING_DATE) and max(END_DATE) from the override baseline table and filters the source data to that range, aligning the override calculation with exactly the sailings present in the baseline**

**Scoped override tracking to BEYOND only: added an explicit filter for LOCATION_NAME == "BEYOND" so override dollar calculations focus on the target ship**

**Replaced the Python UDF-based threshold labeling with native PySpark when/otherwise: the old approach used a Python UDF (get_threshold_label) to bucket override percentages into threshold levels; replaced it with a chain of when() conditions (20%, 15%, 10%, 5%, 0%, NO OVERRIDE) which is faster and avoids Python serialization overhead**

**Order Creation Pipeline Orchestration **

**Fixed midnight scheduling constraint: adjusted the time-window check that gates pipeline runs so it no longer blocks executions that start near midnight UTC**

**Removed vacuum guard: the pipeline had a temporary vacuum guard (preventing Delta table VACUUM during runs) that was no longer needed**

**Created GET_ACTIVE_RUNS: a new orchestration notebook that queries Databricks for active/running jobs, used to prevent duplicate pipeline executions**

**Refactored CHECKPOINT_INTERMEDIATE_TABLES: moved 285 lines of checkpoint logic out into dedicated notebooks, keeping it focused on table materialization only**

**Updated dependent_last_updated_date_tables: adjusted table dependency tracking to reflect the new notebook structure**

**Daily Requisition Analysis **

**Removed product number filter and scoped to future sailings: the requisition analysis was previously running against all historical data; refactored to filter only for BEYOND itinerary dates, reducing compute and focusing on actionable requisitions**

**Removed UOM (Unit of Measure) from output: removing it reduced row counts and simplified joins with the scorecard**

**Added actual quantity reconciliation: for future sailing dates that already have partial consumption recorded, the analysis now nets out actuals from the requisition forecast to avoid double counting**

**SSC Finance Tool **

**Created SSC (Silversea) version of HISTORICAL_MODEL_TRAINING_DATES_VOYAGE_DEMAND: converted the RCI/CCI historical model training date logic to work with SSC's different table schemas and voyage structures**

**Created SSC version of Weighted_Average_Cost_Tracker_Step_2: adapted the RCI/CCI version for SSC's procurement data model**

**Step 3A: Consumption & Voyage Data Integration **

**Created and debugged the SSC Weighted Average Cost Tracker Step 3A notebook, which reads the Step 2 forecast parquet, loads SSC consumption records from prd_gold.ibp.ssc_consumption_report, joins them to voyage data for historical sailing context, deduplicates, filters to pre-forecast dates, and unions the result with the forecast base. Six bugs were identified and fixed including column alignment, deduplication logic, and date filtering.**

**Step 3B: PCD Proration & Revenue Calendar **

**Created and debugged the SSC Weighted Average Cost Tracker Step 3B notebook, which takes the 3A checkpoint, joins sailing schedule data, processes remaining unmatched consumption (1.1M rows), maps ship codes, aggregates PCD and Forecast PCD from ssc_voyage_data_and_forecast, prorates voyage-level demand into monthly calendar buckets, and assigns Revenue Year/Month. Eight fixes plus two additional bugs were resolved.**

**Order Creation - Actual Quantity Needed **

**Updated guest count parameters in RCI_CEL_ORDER_CREATION_EQUATION: refreshed the hardcoded guest capacity numbers to reflect current fleet configuration**

**Finance Tool Step 3 **

**Added DAX equivalent calculated columns to Weighted_Average_Cost_Tracker_Step_3: materialized CT_AccountCharged_calc, ActualGL_Charged_calc, and Brand_Adj_calc in the consolidated table (that has been previously computed and understood by stakeholders in Power BI DAX), wrapped enrichment in try/except with row-****count guard to catch join inflation, and commented out debug display() calls (HOWEVER it won't error out the pipeline to avoid any issues). **

**Fixed ALT_ADDRESS2 null-value handling: the otherwise() clause in the cost center parsing was failing when ALT_ADDRESS2 was null. I then simplified the condition to handle nulls gracefully (removed 14 lines of overly complex logic, replaced with 1 clean condition)  **

Ben Fowler & Camila

**IBP Supply Chain:**

**Project: IBP / Data Operations Engineering****
[DOE-1241] IBP | SSC Crew Count Forecast Model | Phase 2 - Jira****
**

**Completed:**

**Crew count normality assessment (SCD dataset): Performed exploratory data analysis showing that most ships exhibit i.i.d. normally distributed crew counts, with borderline cases explained by low sample sizes and operational constraints, motivating a simplified distribution-based modeling approach.**

**Fleet-wide modeling recommendation: Proposed adopting a single i.i.d. normal framework across ships to simplify the pipeline, align with domain constraints, and avoid overfitting time-series models where no temporal structure was detected.**

**Reporting inconsistencies dashboard: Published a Databricks dashboard highlighting reporting gaps, jumps in crew counts, overlaps between uniform and Fidelio sources, and intra-source variation to make data-quality issues visible to stakeholders.**

**Ongoing:**

**Source evaluation and anomaly handling: Continuing investigation into Fidelio-based crew counts, including normality tests, outlier detection, and ramp-up period handling on a per****-ship basis, to decide how best to treat non****-normal behavior.**

**Data pipeline stabilization: Continuing to refine a “temporary” crew count solution while the team gains clarity on upstream reporting processes, with an emphasis on understanding the business function generating the data rather than over-relying on statistical models.**

**Stakeholder alignment: Coordinating with upstream data owners and stakeholders (e.g., Dom, Paolo, Eleonora, broader team) to clarify how crew data is produced and to document findings for the IBP model design.**

Ben Fowler & Camila

**IBP Supply Chain:**

**Project: IBP | Purchase Order (MOT) Metrics****
[DOE-1185] IBP | Purchase Order (MOT) Metrics - Jira****
**

**Completed:**

**MOT validation pipeline enhancements (MOT_Value_Comparison): Implemented a standalone validation notebook for MOT and embedded inline checks (grain uniqueness, cross****-join size, lookback correctness, NULL integrity, etc.) directly into the main MOT comparison pipeline so validations run automatically during execution.**

**Performance verification of validations: Confirmed that the added validation sections complete within a few seconds each and do not materially impact end****-to****-end pipeline runtime.**

**MOT metrics correction rollout: Addressed inconsistencies in MOT calculations caused by non****-current code on the master branch, implemented corrections requested by stakeholders, and generated an updated MOT metrics dataset for downstream users.**

**Documentation updates (validation section): Extended the existing documentation to include a clear validation section describing how MOT values are checked during pipeline execution, ensuring future transparency and easier troubleshooting..**

Ben Fowler & Camila

**IBP Supply Chain:**

**Project: IBP | Region Mapping / Central America Rollup****
[DOE-1275] IBP | Create an additional column to map Central America to North America - Jira****
**

**Completed:**

**Stabilization of validation logic: Removed unnecessary or overly strict validations that were causing failures without adding meaningful protection, simplifying the path to a stable deployment of the region****-mapping changes.**

**Ongoing:**

**Notification integration for region anomalies: Preparing Teams notifications to alert regional stakeholders when inconsistencies in region reporting are detected so that issues can be addressed promptly without manual monitoring.**

Ben Fowler & Camila

**IBP Supply Chain:**

**Project: IBP | SSC Crew Count / Data Sources****
[DOE-1342] IBP | Crew Count Decision: uniform table vs. fidelio table (which is more stable to create a forecast) - Jira****
**

**Completed:**

**Crew count data quality investigation: Analyzed Fidelio and uniform-based crew count sources, documenting gaps, jumps, overlaps, and variability, and surfaced these via a dedicated dashboard to ground the source****-of****-truth decision in observed behavior.**

**Ongoing:**

**Source-of-truth decision for forecasting: Continuing to evaluate which source (uniform vs. Fidelio) provides the most stable and accurate foundation for the crew count forecast, using dashboard insights and ship-level statistics to guide the decision.**

Ben Fowler & Camila

**IBP Supply Chain:**

**Project: Table Reference Discovery / SSC Supply Chain Codebase****
[DOE-1317] Table References Script - Jira****
**

**Completed:**

**Table reference extraction experiment (MLflow - Databricks): Designed and configured an MLflow-backed experiment that captures JSON-structured logic and conditions for identifying prd_gold and prd_silver table references across the DA2I-RCG_SUPPLY_CHAIN codebase, using a curated CSV of unique tables as input.**

**Noise reduction in reference logic: Iteratively refined the detection rules by removing read/write-related logic and other patterns that were generating false positives, improving the precision of table reference extraction.**

**Pull request delivery for table reference script: Implemented and delivered the table references script, opened a pull request against the supply-chain repository, and completed the merge after review so the capability is available for downstream work.**

**Caleb**

**CLV + Demand Model**

**Completed:**

Validated the updated fleet model's forecasted APCDs by year, brand, corporation, and ship count -- taking note of key errors to then fix

Utilizing the validated fleet model and port information from Destination Intelligence, created several visuals and slide decks detailing the growth of MSC throughout the world through 2035

**In Progress:**

Preparing a data handoff to share the demand model's ETL pipeline and data sources with Eddie's team to begin their work on sailing environment

Continuing to validate the 2025 CLV table, noting essential areas of improvement before fulling rerunning pipeline for shareable version

Mirielle

Contact Center:
**Weekly Report – March 26, 2026**

**Workforce Planning – North America (Royal).**

**Meeting with Darren to review the App / Updated the App with feedback.**

**1. Built a Real-Time Forecast Accuracy Calculation (MAPE)**

Previously, forecast accuracy (MAPE — Mean Absolute Percentage Error) came from a pre-computed database table. We replaced that with a **dynamic, on-demand calculation** that compares actual vs. forecasted call volumes month by month.

**2. Added Automated Forecast Recommendations**

We introduced a **recommendation panel** beside the MAPE chart. It interprets the latest month’s accuracy and suggests what to do:

If accuracy is strong (≤5% error), it confirms the forecast is reliable.

If accuracy is weak (e.g., 25%+ error), it highlights the issue and suggests a specific correction factor.

**Why it matters:** Instead of just presenting numbers, the system now gives planners actionable insights — functioning like a co-pilot that helps guide forecast adjustment decisions.

**3. Introduced Multi****-LOB Forecast Views and Adjustments**

Two major enhancements now support **multiple Lines of Business (LOBs) simultaneously**:

**Actual vs. Forecast** now aggregates call volumes across all selected LOBs for a unified view.

A new **Multi****-LOB Forecast Adjustment** page allows planners to adjust the combined forecast and save those changes — complete with audit trails, tier logic, and per-LOB breakdowns.

**Why it matters:** Many planning decisions are made at a combined level (e.g., Casino sales + Casino Service). This removes the need to adjust each LOB separately and manually sum results.

**Workforce Planning – International and Casino – App Design**

**Call Volume Forecast Simulation (For Development & Testing)**

We implemented this forecast simulation as a **Plan B** to keep the project moving forward.
At the time, we were waiting for Nico’s team to provide the official call volume forecast built by Xavier or their team. we moved ahead with an alternative approach.

**Why We Built It: **We needed a reliable way to **build, test, and validate** all application features that depend on forecasted call volumes. This includes**: **accuracy checks,** **forecast adjustments,** **visualizations,** **and the full save-and-approval workflow.

**App page Call Volume Forecast**

**What we designed:**
A page that displays predicted call volumes for each market and department, alongside actual call volumes from the same months in the previous year.

**What it does for the team:**

Provides a 3-month forward view of expected call volume

Includes a forecast accuracy indicator (MAPE) to show how the model has performed recently

Allows filtering by region and market, brand, and department

**Why it matters:**  Planners can quickly identify anomalies. If the forecast diverges from historical patterns or recent accuracy is low, the team can investigate early—long before staffing decisions are finalized.

**App page Forecast Adjustment Page (Market Level)**

**What we designed:** A tool that lets planners apply a controlled adjustment (alpha factor) to the total market-level forecast.

**What it does for the team:**

Provides a slider to adjust the forecast up or down and instantly see the impact

Displays a bar chart comparing original vs. adjusted forecasts with last year’s actuals

Summarizes exactly how many calls the adjustment adds or removes each month

**Why it matters:**
Models cannot anticipate promotions, policy shifts, outages, or market-specific events. This feature allows planners to incorporate their knowledge in a structured way. Every adjustment is saved with an explanation, ensuring full transparency for auditors and leadership.

**App page Forecast Adjustment Page (Department / LOB Level)**

**What we designed:**
A tool for breaking down the adjusted market-level forecast across departments.

**What it does for the team:**

Loads the previously saved market-level adjustment

Provides an editable grid of department percentages that must total 100%

Shows the impact of the revised distribution on monthly call volumes

Displays the original vs. adjusted splits for clear comparison

**Why it matters: **Even if the overall market total is correct, the departmental mix can shift—e.g., one product line may grow faster than others. This workflow lets planners refine those distributions without relying on the data science team.

**App page Assumptions**

**What we designed:**
A centralized place to record staffing model inputs such as AHT, shrinkage, and abandon rate targets.

**What it does for the team:**

Offers sliders with predefined ranges to prevent invalid entries

Allows selection of the months the assumptions apply to

Captures who made the update, when, and why

Provides a preview before saving

**Why it matters:**
These assumptions have a direct effect on staffing needs. For example, increasing AHT from 500 to 600 seconds can significantly raise required headcount. Having a standardized, auditable repository ensures that all planning decisions are based on consistent and reviewable assumptions.

**The Save System (Used Across All Pages)**

All pages follow a unified, controlled workflow for saving data:

**Three-tier structure** — Draft, Preview, and Final, each with separate passcodes to ensure proper review.

**Overwrite + Backup logic** — The “live” table is overwritten with each update, while a backup table captures every revision for full historical traceability.

**Metadata on every row** — Each save includes user, timestamp, tier, and the planner’s explanatory comment.

This provides a lightweight but reliable approval process without needing additional software.

**App Review and Feedback.**

We held two working sessions with **Nico and the team** to review the Workforce Planning application.

**Session Overview**

Walked the team through each section of the app

Explained how to read each chart and visualization

Reviewed how slicing works across **Market, Brand, and LOB**

Demonstrated how the **alpha adjustment slice** is applied

Walked through the full process for data saving and passcode handling

**Team Feedback & Action Items**

The team provided several valuable suggestions:

Add **tables** to visualize the **call volume proportion split** at each level (Market, Brand, and LOB)

Remove or consolidate certain LOBs (such as *River* and others) — to be confirmed with the team

Display the **sum of LOB****-level adjustments in red** when they exceed the total market volume

Re-introduce **historical call volume from the same period last year** in the call-volume adjustment section of the app

**Key Update** Successfully deployed the application image to the **Azure Dev environment (Container App)**.   Access requires permission, which can be granted by **Brendan**.

**Next Steps**: Review the Application to incorporate the Team Feedback.

Carlos & Bao

E-Commerce:
**Accomplishments:**

Completed holistic comparison of PA Booking Propensity vs Web Booking Propensity models

Demonstrated the models are statistically independent (correlation: -0.069, zero shared features) and measure complementary dimensions of consumer intent

Built a dual-score decisioning framework showing naively targeting all "Low" consumers wastes 43–93% of offers on passive or already-loyal audiences

Proposed a surgical targeting approach focusing offers on the 3–21% of consumers with highest expected incrementality

Developed stakeholder-ready PowerPoint with supporting visualizations (heatmaps, quadrant analysis, segment breakdowns) and recommendation tables

Completed documentation for app data analysis and compiled into a Word doc for stakeholder review

Developed ingestion code for app data features so that once approved, app data can be seamlessly integrated into our models

**Blockers:**

Clickstream data processing at scale has been challenging — consumer-ID-joined checkpoint table continues to fail after hours-long runs despite optimizations, partitioning strategies, and cluster tuning

Narrowed dataset from 1,000+ columns to 292 key features (~75% reduction) and reduced row count by 3.5x (16B → 3B rows)

Remaining challenge is persisting the 3B-row table to a checkpoint without failure

Currently iterating on further optimizations and smaller chunk-based writes to complete this table

Kevin Diaz and David Whitney

PCP Pricing Automation

We have secured approval from Ernie and Legal for the narrowly defined pilot use-cases to test the 1:1 Targeted Offers Pipeline with Digital/E-Commerce/Data Engineering (see below). Future use-cases will be run by Ernie and gradually will develop an offer bank that may approve broader use-cases (but for now will be case-by-case).

# **RCI Promo:**

- **Product:** Deluxe Beverage package

- **Discount:** Increase dependent on the prevailing discount of the sailing chosen

- **Population:**

- 50 randomized cabins from one IC sailing

- **Eligibility Criteria:**

Low casino and CAS loyalty tier (all guests in cabin)

US Market

No Beverage purchased in cabin

Non-GTY

- **Feedback:**

- No AI and Just Business-Rules (Randomized)

- Randomized population will receive the discount.

- If target population is more specific, more questions will be asked and require additional review.

- As we build an offer bank, we will initially start with targeted recommendations from Legal, but later will develop a more general approval framework.

# **CEL Promo:**

- **Product:** Unlimited Specialty Dining

- Sell unlimited to all specialty dining discounts

- **Discount:** 40% off the base price

- **Population:**

- One BY Sailing

- **Eligibility criteria:**

Celebrating a birthday or anniversary

Identifying that you have purchased fewer than one dining cover.

- **Feedback:**

- Will use existing database of birthday or anniversary information (like Loyalty).

- Using their consumer-specific data to determine eligibility to determine a target group population but not setting the price.

- CEL has previously used the 40% discount in mass promotions.

Erick & Cristian

**PCP Product Recommendations: M****yCruise Recommender *****(Cristian V.)***

The team is shifting focus to support recommendation tasks in the coming week. Work splits into two tracks: iteratively improving models and evaluating model performance.

**ForYou Coverage Fix & Apriori Expansion** *(Cristian V.)*: Supporting deployment of new Calendar Recommender. Continuing Apriori expansion across product categories with deployed re-ranking policies (margin, revenue, diversity). AB test analysis paused - will rerun once Calendar is live.

**Model Improvements**: Scoping out work on fallback recommendations, improved guest and product clustering. These clusters will feed into the ALS model — the team will also explore alternative models beyond ALS and potential ensemble approaches.

**Online Tracking**: Scoping out work on how to build Recommendations monitor that would be owned by DS team.

**Recommender Visualization Tool**: Will build a playground demo tool to bring recommendations to life — displaying recommendations in an interface with images and descriptions.

**Recommendation Analytics**: Building a robust analytics layer to make the recommendation engine transparent — mapping out what is being recommended, to whom, and how margin weighting affects the final output. Goal is to move away from black-box recommendations.

**Team Support**: David, Erick, Osvaldo, and Rodrigo will begin contributing to the above recommendation tasks in the coming week.

Erick:

**Project Axiom — Voice 360**

**Axiom Power BI *****(Danusio G.)***

**General Medallia Facts Tab**: Building out a new analytics tab with general Medallia segmentation and correlation insights (e.g., detractors write longer comments, comment patterns by brand/country) to establish key Medallia facts.

**Dashboard Data Refactoring**: Refactoring queries to pull demographics (pax count, kids count, load factor) from the reporting_topics table using a simpler DISTINCT approach — replacing the previous complex multi-table joins.

**Silversea Stakeholder Feedback**: Showed latest dashboard version to Silversea stakeholders — they responded positively to the current layout. Minor design refinements (card positioning, whitespace) noted for backlog.

**Email Reports *****(Danusio G., Rodrigo B., Erick A.)***

**GSO Safety Email** *(Danusio G.)*: Key fixes: (1) added sail nights count to the top of the report, (2) improved keyword matching for Injury & Medical Mentions to eliminate false positives (e.g., "peeling paint" no longer triggers "pain") and added AI validation to filter non-genuine safety concerns, (3) fixed positive/negative mention counts to only show counts when summary content was actually produced, (4) consolidated Top Segments so a single comment tagged across multiple hazard/location/cause dimensions no longer generates repetitive duplicate cards. Also ensured summary bullets read as summaries rather than raw guest comments.

**Port Email** *(Rodrigo B.)*: Created the first Miami port email, expanding scope beyond Corporate Strategy to now include Port Operations as a stakeholder. Port Operations will likely want to receive port emails for all turn ports.

**Guest Strategy Email** *(Rodrigo B.)*: Identified a critical ETL concern — Medallia survey data appears to only update ~7 days after sailing return dates instead of daily, causing metric discrepancies with Medallia's own reporting. Escalating to data engineering (Luiz/Kiana) as this affects all production pipelines. Short-term mitigation: adjusting the scheduled email time to 7 AM to capture the latest data refresh.

**RBC Email & Dashboard** *(Rodrigo B.)*: Automated weekly Monday pipeline now sends the email (Gang Wang, Dotan Ben Horin, Sean Tracy, Linken Dsouza, and Carly Montanti) and simultaneously refreshes the RBC dashboard.

**Meta Data Extraction *****(David M.)***

**Databricks Asset Bundles**: Configuration file created and tested successfully in the dev environment. Working on environment-specific variables for dev vs. prod. Configured failure email alerts to Erick and David. **Blocker**: Needs Databricks tokens/secrets created in GitHub for the pipeline to authenticate (Erick to create). Exploring GitHub Actions vs. Azure DevOps for production auto-deployment on merge to main.

**Embeddings Pipeline**: Integrating quantized embeddings as the final step of the metadata generation pipeline (topics → bullet points → divisions → open-ended → embeddings → vector store).

**Abandoned Cart Dashboard *****(Rodrigo B.)***

QAD 39 (new question) now available in tables and being integrated into the pipeline. Dashboard improvements in progress: fixed naming, added count cards. Met with stakeholder to review the latest version and collected new requirements including weekly/monthly trend widgets (booking factors, reasons for not completing, completion trends), demographic label sorting, response counts per widget, new topics (war/political unrest, flight delays), cruise experience filters, comment translation, and OTA word cloud grouping.

Erick

Contact Center: **Project Webfunnel Lead Scoring**

**Lead Scoring pipeline fix** *(Erick A.)*: Current pipeline broke due to a permissions change preventing Databricks from connecting to ADLS. Short-term fix pending Marcio (Platform) support to restore connectivity. Erick is rewriting the lead scoring pipeline from scratch for long term solution.

Erick

Hotel Operations: **New Use Cases**

**Crew Ranking** *(Erick A.)*: New use case scoped this week. Business currently ranks hotel directors across all ships using a manual Excel model. Erick has replicated the Excel logic in Python as a first step. Next phase: connect the pipeline to Databricks source data instead of reading from Excel. Rodrigo will support once more details are shared.

David Whitney, Erick Alfaro, and Ben Fowler

HR Use-Cases

**Crew Demand Forecasting** *(Erick A.)*: Follow-up emails sent to John Makan (CAM planning) documenting current understanding and initial questions.

**CAM ****CAR Planning**:

Team met with Angela Smith to assist in the 5 upcoming CAR submissions for CAM. Beyond demand planning, Angela is interested in brainstorming the “art of the possible” for leveraging AI:

5 CAM CARs:

(1) Discovery: CAM Transformation & Design.

--> Define the Technical Architectural and Business Process Design

--> How should onboarding happen, relative to existing capabilities or new capabilities (like a scheduling tool)

(2) Demand Planning (John Makan)

--> Supply Chain Demand Planning to ensure our hiring engine.

--> Will initially go quick.

(3) Recruiting

--> Have an internal tool called SeaTrack

--> ATS: Not intended for maximum optimization and a warehouse of functionality (not smartest). SAS cloud-concept

(4-5) Air & Travel (Jessica Ginart / Julie)

--> Very large of what we're booking for Air is an intelligent/smart Booking Engine.

--> 90-95% of bookings. Pick the best priced tickets out of there.

--> Let crew be able to pick their own flights to improve flexibility.

--> Not a free-for-all and have business rules (i.e. fences within budget or upcharges to pay over an overage)

--> Need to get money from crew member to supplement our charages.

--> Need to know if a crew member is at a booked hotel.

--> Need to know optimized connections

Laura Mao / Craig Bauer (IT People)

Schedule a workshop and share the CARs (except Design ones)

--> Wants to focus on Travel & Air. What could we build here?

--> Workshop: Next week is Travel & Air workshop.

--> What is the Art of the Possible?

--> Standard APIs and go into the brainstorming zone

--> Want to fly 2 legs and not 4 legs (not an airport at 1am in the morning, and figure out how to get to the hotel). Employees want to feel they are treated like a valued employee (i.e. what we would want to fly)

Multiple Tranches for CAM Transportation

--> Next parts of CAM capabilities will be focus (like planning)

--> Need to roll out substantial products for Tranche 1

--> Address a cut-cut for the brand and HR

Next year's focus: onboarding, scheduling

This year cant be 50-50 delivery, but 80-20% improvement.

--> Need some something substantial this year.

--> Operationally connect with new systems

Dave, Ben, and Erick met with HR & Air IT teams (Laura Mao, James Defendis, Miguel Gonzalez) to discuss:

**Core CAM crew travel context:**
CAM crew travel optimization is fundamentally different from guest travel and pricing. Air inventory is not owned by RCG and sits in a separate ecosystem where airlines control schedules, fare buckets, cabins, and pricing dynamics. Today’s crew air process is highly complex and largely driven by layered business rules, pulling large sets of itineraries from Sabre (GTS) and narrowing them down to a single recommendation based primarily on cost, non-stop preferences, operational constraints, and policy guardrails. Crew travel decisions focus on minimizing cost while maintaining acceptable crew experience and reliability, factoring in constraints such as citizenship, airport delay risk, and layovers that may require hotels. Air is only one component of a broader crew movement problem that also includes hotel and ground transportation, budgeting, and operational cost forecasting, all of which are challenged by disruptions and drift in historical data.

**Potential AI use****-cases discussed:**** **The discussion highlighted opportunities for AI to augment, not replace, the current rule-based approach. This includes improving rule optimization and decisioning across large itinerary sets, better handling of dynamic pricing and fare changes (such as price reshopping), and supporting more reliable forecasting for budgeting and operational cost management. AI could also help incorporate broader crew-experience considerations beyond base fare, improve responsiveness when prices drop, and assist with managing disruption-driven variability. Over time, there is interest in extending optimization beyond air into hotel and transportation decisions, and eventually into crew assignment and scheduling, recognizing that scheduling is a later-phase opportunity while air, hotel, and transportation optimization begin first.

**ECR Automation: **We also kicked off conversations with Tracey Tavarez and Carol Hernandez (key contact).

Dana requested a complete rehaul of the ECR system:

--> Abandoning Lotus Notes

--> Leverage the RMA CAR to rebuild the automation (not just accelerate like was previously agreed with IT)

--> Carol will setup a meeting to work with IT (Rita and Mark Ambler) to discuss the new vision with them and gain working requirements

Also they want to use HR's new AI resource on GenAI CoE (under supervision of Brandon Schassberger) to help build out an interface like CorAssist that helps the ECR Coordinators more effectively answer employee questions and inquiries.

**Mert**

**New Build**

Completed development of the Newbuild AI Observatory Web App with full integration to Azure AI Search, Azure Knowledge Agent, Databricks Unity Catalog tools, Databricks Genie, and Databricks Vector Search.

Continuing to improve the UI and preparing for user testing.

Met with the Newbuild team to review AI Observatory progress.

Mert:
MIAP
Worked with the IAM team to resolve the expiring SharePoint access mechanism.
Met with the Decarbonization team and aligned on a $500K budget for 2027 to develop hull and propeller performance models. A proof-of-concept model is planned before the summer to support CAR memo development. This project has a net new $10M/year savings potential, including a $350K/year reduction by canceling Eniram’s legacy model. One remaining risk is access to Eniram accelerometer sensors. If access is not granted, we will model using draft sensors (which are prone to drift) and explore longer-term alternatives.

Reza:
MIAP
Updated the filtering logic for the service power area.
Fixed models for ships AL and OA and updated their baselines.
Identified a mismatch between the itinerary and legs tables that caused fuel forecast accuracy issues.
Coordinated with the deployment system manager to identify the root cause and updated the code to mitigate the accuracy issue.
Updated the base and dynamic models for ship NV in the service power area.
Identified a bug in the LNG ships optimizer and coordinated with a team data scientist to address it.
Continued root-cause analysis of the recent incinerator consumption issue.
Analyzed the “no optimization” lazy algorithm that leads to long runtimes and worked on diagnosing the root cause to improve performance (ongoing).
Diagnosed and fixed an incorrect unit conversion (kW to MW) in the air lubrication system power consumption.
Attended the hull performance platform meeting to understand project scope and initial plans.

Arya:
MIAP
Identified multiple model versioning issues.
Created documentation for handling this job-related issue.
Fully integrated no-optimization logic into the digital twin, including adding a regression model for STG predictions and fixing LNG fuel-type bugs.
Tested finance team models against current models.
Followed up with the securities team on real-time map updates; currently optimizing ship location queries and adding new features.
Investigated pipeline failures on the 24th.
Added fuel tags to the analytics mean-10 table.
Continued development of the fuel monitoring dashboard, currently in QA within the MIAP app, now tracking all main onboard fluids for Edge-class ships with customizable charts and refresh frequency.

Mahshad:
MIAP
Identified approximately 500 kW in AHU savings for HM and sent a summary email to the ship; awaiting response.
Followed up with WN and SY regarding sensor issues on the TCV valves.
Added chiller models to the pipeline, including debugging and compilation fixes.
Addressed several data pipeline issues.
Scheduled a meeting with the HVAC engineer to discuss potential issues with the SC TCV valves.

Will:
MIAP
Fixed errors loading pilot fuel models.
Corrected incorrect fuel total calculations in FACTS mode.
Removed power columns from the FACTS mode results dataframe.
Added API endpoints to validate leg and optimization option availability. The leg check validates leg existence and viable speed; the optimization mode check validates compatibility with the ship’s sensor and reporting configuration.
Productionized FACTS mode as an option in the Optimizer.
Productionized the demand rounding step in both the API and web app.

Ram:
MIAP
Worked on loading historical Eniram tags for IC, ST, NO, and RA.
Fixed a bug in rerun notebooks that caused production data issues and reloaded all affected data.
Added a file count KPI to the MIAP Sample Count dashboard.
Started building a dashboard for the MIAP REST API and collected service cost data; currently identifying services to remove that are not part of the MIAP REST API before sharing the report.
Made progress on fixing the Silver deployment profile task in MIAP ETL with Brendan.

David Whitney

Loyalty: Merge Recommendation Engine

Over the past week, the primary engagement with Jason Fortier centered on **guest profile deduplication in support of the upcoming co****-brand credit card launch**. Jason flagged approximately **225K duplicate guest profiles** tied to credit card memberships and requested support from the Data Science team to run those records through the **Merge Recommendation Engine (MRE)** using the match/merge logic established last year, with particular emphasis on **frequent traveler logic**. The business need is time-sensitive due to the **April 28 co****-brand launch**, and both IT and business stakeholders emphasized the importance of validating merge confidence, identifying edge cases, and producing a summary view that could be operationalized in MDM ahead of conversion activity. You confirmed willingness to engage, began reviewing the provided dataset, and verified access to the source table for immediate analysis. , ,

In follow-up Teams conversations, you and Jason aligned on **practical guardrails for merge confidence**, including the need for **higher confidence thresholds (e.g., ~0.8–0.9)** given the sensitivity of credit card member data. Jason shared that his spot checks revealed some records that should clearly not be merged, reinforcing the value of MRE as a filter ahead of Informatica’s proposed daily batch merges. The discussion also surfaced broader **Golden Record quality concerns**, particularly around **phone numbers and mailing addresses being associated with multiple guest profiles**, which complicates caller authentication and downstream AI use cases. You noted that MRE is currently a prototype and could be productionized if the business intends to rely on it regularly, while leadership acknowledged that if this represents a systemic gap, it should be addressed visibly and with appropriate funding rather than handled ad-hoc.
