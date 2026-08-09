Erick & Cristian

MyCruise Recommender
AI-powered recommendation engine for post-booking, pre-cruise products serving the ForYou personalization experience.
Recommendations Engine (Cristian V.)
Apriori Model — Business Policy Re-Ranking: Deployed updated model with margin-sensitive re-ranking. Business can now prioritize recommendations by revenue, margin contribution, product age, or popularity/trending via a weighted scoring system (70% original rank + 30% business policy weight).
Business Rules Configuration Panel: Discussing implementation approach with stakeholders (Rosie/Taylor). Options include a maintained lookup table or a Next.js configuration UI so the business can self-serve hardcoded product placement (e.g., Royal Beach Club). Decision pending.
ForYou Model Coverage Fix: Identified ~42% empty response rate when a same-port filter is applied. Root cause: insufficient recommendations loaded into the API due to memory constraints. Working on expanding coverage; exploring Postgres as the backing store.

Erick

Project Axiom — Voice 360
Dataset-agnostic framework to extract and deliver insights from any unstructured customer feedback using AI and LLMs.

Axiom Power BI (Danusio G.)

- Dashboard Stakeholder Feedback: Alessio reviewed the updated dashboard and responded positively — finds the sailing-level table with topic filtering very useful. Implementing requested UI refinements: expandable/collapsible comment summaries (moving from tooltip to toggle), fixing table-to-chart bidirectional filtering, matching table style to existing visuals, and adding NPS accuracy and AI hallucination disclaimers.

- Trend Plot (Backlog): Identified request to add an over-time scatter plot showing topic NPS and mentions; to be scoped with stakeholder.

Email Reports (Danusio G., Rodrigo B., Erick A.)

- GSO Safety Email (Danusio G.): Awaiting Melissa's feedback before deploying venue context improvements to production. Venue files sourced and validated against existing Medallia NLP repo.

- Port Email — Roatan Coverage (Rodrigo B.): Implemented Shore Excursion comment query to expand Roatan coverage. New query yielded ~600 comments (~120 net new). Also used a Copilot-generated place list to surface ~3,000 relevant comments. Sending current draft to Matt B. for initial stakeholder feedback while coverage improvements continue.

- Guest Strategy & Analytics Email (Rodrigo B.): Primary approver (Jose) on paternity leave. Awaiting feedback from Alvaro. Email currently running on Mondays at 5 AM.

- Silversea Email Reports (Erick A.): Working through Silversea-requested change list before handing off to Rodrigo for implementation support.

Meta Data Extraction (David M.)

- Open-Ended Topic Extraction Pipeline: New prompt producing consistent, concise (≤3 words) topics aligned to primary topic categories. Results reviewed and quality validated. Waiting for final approved topic list from Erick (expected within days) before running full pipeline against bullet points table.

- Guest Logs Categorization: Corrected 5 out of 20 validation errors (misclassifications tied to schema gaps, not model failures). Full pipeline cost estimated at ~$800 from 2023 onward. Will not run until Alessio approves the final topic list (meeting Wednesday); pipeline is one-shot given cost.

- Grok / Azure AI Foundry: Grok model approved by Infosec — Microsoft confirmed data isolation (no sharing with OpenAI or third-party providers). Awaiting Marcio to configure the Foundry endpoint before the team can begin using it.

- Forecasting Data: Weather forecast table created and daily job scheduled (16 days ahead + 2 historical days for consistency). Weather data will also feed Osvaldo's Target Setting model integration.

Axiom Webapp — Keyword Correlation Tool (Osvaldo V.)

- Query Performance Optimization: Investigated pre-joined table approach; modest gains for small queries but large queries (100K+ rows) still slow due to data transfer volume. Reverted to original approach. Erick to integrate branch as a dedicated Lambda service (same architecture as Drivers Model) to decouple retrieval from the web app.

Axiom Driver/Target setting models (Osvaldo V.)

- Weather Integration for Target Setting Model: Kicked off new multi-model pipeline initiative. Model 1 (rolling NPS baseline) validated with ~11 features (ship age, seasonality, cold-start flag, rolling averages). Osvaldo now focused on Model 2 — integrating Danusio's weather forecast table to model residuals between predicted and actual NPS at the sailing level.

Erick

HR — Crew Demand Forecasting (Erick A.)

- Initial scoping: Initial scoping call with John Makan (CAM planning) held last week. Team is currently forecasting headcount demand across all Royal Caribbean brands/ships via a manual Excel model.

- The team replicated the excel model by reading the raw data directly from the excel and forecasting via python.

- Follow up emails have been sent to John documenting our current understanding of the use case and providing an initial list of questions to the stakeholder.

Doug

CEL Rev Management:

* Completed test design and sailing list production for Celebrity T4 AB test. Once started, near window test will run for 12 weeks and far window test will run for 24 weeks. Attempting to measure a 2% change in T4 booking percentage.

* Restarted work on dual-branded replenishment automation KPI measurement and modeling. Will remain as top focus through the end of March.

CEL | Quad Test Design

Status: This ticket is complete as of 03/17/2026

Deliverables:

Feasible, but due to tight T4 penetration variance, requires longer tests.

Near window 12 weeks. Far window 24 weeks.

Near window limited to 7N Caribbean, Short Caribbean, Australia, Europe due to many metas already above booking thresholds for 2026.

Sailing lists provided to business to allow them to implement test conditions.

Test planned to launch in the coming week.

Delays: None.

Potential future issue: None.

Evan

RCI Revenue Management

SPI Factor Models

Query & Data Layer Improvements

Standardized new queries around passenger and cabin capacity, PPCD, and PCD metrics

Rewrote methods for most CTE instances to improve query performance for large-scale data use cases

Histogram & Bands Optimization Framework

Created initial framework for identifying optimal feature bands relative to SPI within the histogram view

Built a custom confidence function that evaluates how well a given range describes the target outcome (positive SPI).  Actively working to finalize the approach for clearly communicating how changes in a factor's value will impact SPI

Combined Feature Relevance & Interaction Analysis

Built initial framework for combined feature relevance, illustrating how a defined range (such as quantile) across two features jointly describes SPI behavior

Added an interactive component to the portal enabling quick preliminary analysis of feature interactions, providing a foundation for additional model development

Databricks Deployment & Azure Progress

Deployed SPI Factor Model to a Databricks web app with permissions scoped to specific groups and individuals

Collaborated with ML Ops to advance efforts toward full Azure deployment

Cabin Type & Pax Build Normalization

Identified relationships between different cabin types and passenger build with SPI; working on additional normalization methods in the dataset in preparation for model introduction

Misc.

Backup SPI Scoring Table

Added a fallback SPI scoring table to ensure continuity in the event of a model failure (no failures to date)

Useful during my absence over the next two weeks and communicated with stakeholders using the table on diverting to this in the case of a unforeseen failure

Portal Visual Improvements & Debugger

Added a development-branch debugger to the portal to support ongoing development and troubleshooting

Implemented a series of visual and design improvements across the portal interface

Interactive HTML Presentation Template

Developed a reusable, interactive HTML template for SPI, but looking to see how this artifact could be introduced and integrated into long term goal

Jesse

SSC Revenue Management

SSC Upper-level suites

1**.Upper-level suite EDA **– I conducted an additional exploratory data analysis on SSC upper-level suite metrics, examining revenue losses (e.g., lower net ticket revenue) associated with buying a veranda and “bidding upward” to a more luxurious suite. SSC customers who bidding upward paid 28% less on average for their upper-level suites than customers who booked them directly.

**2.Upper-level suite input data **– In anticipation for an ab test, I compiled a data set containing relevant voyages to compare for similarities. I received input from SSC Revenue Teams on potential voyages, as well as hard and soft parameters to compare and optimize the pairing process. This dataset is an essential component of the uab framework, which utilizes it for pairing and power analysis.

3.**Presenting to stakeholders **– I presented the results of my EDA to SSC stakeholders with positive feedback. Stakeholders provided guidance as to what an AB test should look like, as well as additional hard and soft parameters to consider. Next steps:

Define “success” and KPI for upper-level suite ab test

Pair voyages for ab test

**SSC Handoff **– in anticipation for my upcoming military training, I am introducing my code base and my work to other team members

4.Introductory meeting – today I met with Data Science Manager and explained my code base to him. Data Science manager will review code base and follow up tomorrow with questions.

Michelle

**CEL**** Revenue Management: ****Category-Gapping 2.0**

Updates tested in qa.

Run was failing on data validation portion of TAP process owned by strategy team.

Issue resolved and pushed to prod.

**RCI**** Revenue Management: ****Category-Gapping 2.0**

Added in upper bounds for gaps based on historicals.

Reworked DART to match CEL framework with individual sailing, group and 6-month average residuals.

Updated optimization to lower gaps if revenue lift is not significant.

Each sailing’s revenue curved is assessed for curvature and gaps are lowered to within $1 of the optimal APD is it passes threshold for “flatness”.

Currently testing entire pipeline and valuating results before sharing with business.

**RCI**** Revenue Management: ****Category-Gapping ****3****.0**

Met with RCI team to discuss tier groupings, decided on recategorizing based on achieved prices instead of using current tiers that were hardcoded based on room characteristics by the business.

I reworked the tiers and sent to business to be approved by the team.

**CEL Revenue Management: Category Gapping 3.0 ****Modeling / Scenarios**

Created grids of every possible combination of features and gaps incrementing by 3%.

Grids are split by availability to simulate scenarios when any of the tiers are closed.

Modularized functions to first predict gty tradeup with 2.0 models and thereafter split out the tradeup by the probabilities predicted from the 3.0 models.

Each scenario pulls the appropriate 2.0 and 3.0 model depending on ship-class, meta, cat-class, wts bin, market, lead type, and availability.

Sent predictions to business for review.

These tables are being searched within the optimization.

**Interpolation / Smoothing**

If testing a gap that falls between grid points, interpolate smoothly to estimate realistic tier shares.

Piecewise linear (PWL) smoothing to make our predicted demand curves stable and continuous across price gaps.

Instead of relying only on discrete model outputs, PWL lets us interpolate predictions between grid points, reducing noise and ensuring the optimizer evaluates realistic, smooth revenue curves.

This includes bi linear and tri linear interpolation, which allow us to smoothly estimate predictions across two and three dimensional gap combinations.

**Business / Feedback**

Business team is creating a formula for how they wish for revenue to be calculated for this project, awaiting their response.

CEL team gave feedback on model outputs, currently working on:

GTY share only shifting based on gty-lead gap. Including feature in 2.0 models that includes effects of the upper prices.

Predicted shares do not decrease as sharply as necessary so optimal revenue is found at highest gaps, however this is not business optimal

Need more realistic share declining at higher premium/upper

Carlos & Bao

**E-Commerce: Customer Targeting**

Updated prediction pipeline to use latest models recently migrated from databricks model registry to databricks catalog

continue manual integral testing of prediction pipeline in qa (pending reporting code)

Developed code to recreate consumer booking propensity history from models saved in MLflow

Deliver booking propensity history for Celebrity consumers in 2025 to stakeholder.

**Clickstream Data Optimization**

Developed logic to reduce consumer clickstream columns from 1,000+ to ~300, focusing on features useful for building consumer history.

Reduced row count from 13 billion to 4 billion by filtering to only **known consumers** with matching IDs.

Created column renaming logic to improve column visibility and clarity in clickstream data.

**App Data Feature Engineering**

Conducted a thorough analysis of app data for ingestion.

Identified two key features with high influence on consumer propensity:

Number of voyages where the consumer used the app **after** their cruise.

Recency of the latest app usage.

Analysis on consumers sampled 12 months ago showed:

Post-voyage app usage is more predictive of booking activity than cumulative or phase-based usage.

Recent app users had higher booking rates.

Consumers who used the app after their cruise showed increased booking likelihood.

**Blockers**

**Brand Column Naming Conflict:** 
Celebrity and Royal clickstream data have the same column counts and overlapping column names (e.g., evar34) that represent different variables according to each brand’s dictionary. This complicates combining data across brands to build a unified consumer history.

**Cluster Performance Issues:** 
Carlos helped create a new cluster optimized for large data volumes, but lazy execution causes the join between consumer ID and clickstream data to run on every operation on the dataframe df. To mitigate this, I am creating and loading a **checkpoint table** containing raw clickstream data for consumers with IDs to speed up future aggregations and column pruning.

**Access to Booking Propensity Models:** 
Despite reaching out to multiple contacts, I have not yet received access to the web-based booking propensity model tables needed for comparative analysis. I will continue following up.

**Ben and Camila**

**Supply Chain**** IBP****:**

Adjusted code in 15 notebooks making approximately 260 changes of code lines to change the model training process to support a Model Training Date that is as of the current date. The impact is that when mid-month model training takes place, all of the consumption data through the current date will be used as the training data set for the business forecasts. Previously we were excluding current month consumption data from model training data for business forecasts. Pipeline with new code successfully ran on 3/16 and 3/17 and validated all data. Sent email to stakeholder showing the impact on one product that had some significant consumption in March, to show how the demand forecasts were higher for the rest of March than they were with the old process which had excluded the high consumption from the first half of March on this product on the given ship.

Delivered temporary Master Load Schedule with Catalyst Voyage Numbers. However, the voyage numbers from the shipfin table provided by the Catalyst team is missing some voyages that we have on our current production Master Load Schedule table. As a temporary fix, we used a left join from the production Master Load Schedule table to the shipfin table so no rows from the Production Master Load Schedule table are dropped, but there are voyages in 2026 missing a Catalyst voyage number. Since this is a data quality issue, we have alerted Data Engineering and they are working on a permanent solution.

Code refactoring work is in process on the Guardrails notebook to make compute time more efficient and code easier to maintain.

Medical Forecasting Improvements

Added controls to prevent unrealistic low predictions for active products (additional guardrails).

Added additional STLY features to improve seasonal signal capture.

Tested robust loss behavior and increased model capacity.

Validated a log target (CONSUMPTION 4 WKMA) approach, which is currently the strongest production candidate of all the current 7 versions completed.

Tested inverse sample weighting to improve model behavior across uneven demand patterns.

Daily Requisition

Shifted time logic from sailing end date based grouping to sailing start date based grouping so outputs align better with planning cadence.

Added explicit sailing date handling in schema and downstream transforms to reduce ambiguity in joins and aggregations.

Split output into separate past and future overwrite tables, then deep cloned those into IBP SSO tables for validation for stakeholders.

Spend Allocation

Future spend per day using finance tool (total voyage demand per sailing) was improved in two phases: first for day-type allocation, then for multiplier quality and fallback behavior.

Delivered first-phase sea/port day proration for future spend allocation. Phase 1 gave baseline sea/port proration.

Improved logic for selecting eligible future voyages so active/in-progress voyages are handled correctly.

Updated reconcile-based quantity usage so calculations align with actual reconciliation behavior.

Added stronger table-output structure and snapshot handling for downstream consumers.

Multiplier logic in phase two is still being refined for edge cases.

Using historical consumption patterns, Phase 2 applies a multiplier to each voyage's daily spend estimate to reflect whether a day at sea or in port is typically higher or lower cost than average. These multipliers are derived from actual past voyages and applied at increasing levels of specificity (by ship, itinerary type, and voyage length) with automatic fallbacks to broader averages when data is sparse. The result is a per day spend profile that is proportionally allocated across the full sailing window.

Snapshot (Finance Tool)

Centralized baseline-overwrite logic into a dedicated flow.

Reworked merge behavior so actual cost center and actual GL account fields are retained correctly.

Improved join strategy for reconcile date granularity, where row splitting previously caused inconsistencies.

Orchestration, Metrics, and Operational Reporting

Added key notebooks into weekly orchestration sequence.

Simplified execution tier configuration by removing inactive/commented paths.

Completed override-tracking metric enhancements.

Updated MOT comparison content and integrated the MOT comparison table into execution/reporting as a standalone task.

Tested end of month notebooks with job compute and fixed all errors.

Monitoring new orchestration master notebook workflow

SSC finance tool step one is completed, just need to review. Next is step 2.

**Ben and Camila**

**Supply Chain**** IBP****:**

Project: IBP | Purchase Order (MOT) Metrics 
[DOE-1185] IBP | Purchase Order (MOT) Metrics - Jira

**Completed:**

**MOT Metrics Table Build (****by_new_metrics_cruise_mot****)**: Finalized the cruise-level MOT metrics table in Databricks, including robust grain and duplication validations across cruise mapping, procurement items, and final output to ensure each cruise–product pair is unique.

**Metrics Refinement & Validation (****new_metrics_purchase_order_mot_cruise_mot****)**: Incorporated stakeholder feedback to update the MOT comparison table, executed ~30 validation queries, and confirmed all but one non-critical validation passed (limited to a small subset of 2024–2025 cruises not relevant to BEYOND).

**Stakeholder Alignment & Handover (Dashboard Design)**: Met with finance stakeholders to align on how to represent MOT variance for Beyond sailings, documented a proposed dashboard partitioning, and shared the underlying calculation logic for independent validation.

**Production Integration & Code Delivery (DA2I-RCG_SUPPLY_CHAIN repo)**: Merged the notebook and SQL logic implementing the MOT value comparison into the shared repository and supported integration of the new metrics into the existing production pipeline run.

**Ongoing:**

**Variance Interpretation & Expansion Planning**: Continuing to support validation and interpretation of an identified ~-$2.0M March MOT variance for Beyond, and documenting implications for extending the methodology to additional ships in future phases.

**ETL Scheduling & Monitoring Strategy**: Awaiting confirmation on desired refresh cadence for the MOT pipeline and exploring options (e.g., dependency ordering, row-count checks, MLflow freshness metrics) to enforce data quality before each scheduled run.

**Ben and Camila**

**Supply Chain**** IBP****:**

Project: IBP | SSC Crew Count Forecast Model | Phase 2 
[DOE-1241] IBP | SSC Crew Count Forecast Model | Phase 2 - Jira

**Completed:**

**Data Source Investigation (Uniforms & Fidelio)**: Deepened analysis of the uniforms demand table and Fidelio crew data, including fuzzy and exact-matching of job descriptions (typ_comment) to uniform job codes, achieving ~75% mapping coverage and highlighting remaining gaps.

**Cross-Brand Data Quality Checks (****supply_chain_onboard_uniform_demand****)**: Re-ran data quality checks on the uniforms demand table and confirmed all cruise brands except Silversea are currently updated, escalating the Silversea data lag to owners via email.

**Stakeholder Engagement & Working Sessions**: Coordinated and held exploratory sessions with reporting and data engineering stakeholders (including Eleonora’s team) to surface inconsistencies in crew count logic, job codes, future demand, and gaps in recent reporting, and to initiate an upstream investigation.

**Ongoing:**

**Forecasting Approach Design (Voyage-Level Crew Count)**: Continuing to shape a pragmatic forecasting approach at the voyage–cost-center level, balancing a simpler moving-average baseline against more feature-rich time-series methods while ensuring input data is sufficiently stable and interpretable.

**Upstream Logic Clarification (Paolo/Dom/DE Teams)**: Partnering with upstream owners who are investigating source logic and tables, and preparing findings/questions from current analysis to bring into follow-up sessions so that the Phase 2 modeling relies on well-understood, auditable inputs.

**Silversea Data Refresh & Coverage**: Tracking resolution of Silversea’s missing or stale data in supply_chain_onboard_uniform_demand and assessing its impact on the timeline and scope of the crew count model deliverables.

**Ben and Camila**

**Supply Chain**** IBP****:**

Project: IBP | Spend Report Regional Mapping 
[DOE-1275] IBP | Create an additional column to map Central America to North America - Jira 
DOE-1275: IBP | Create an additional column to map Central America to North AmericaTESTING | QA | 9…

**Completed:**

**Region Normalization Logic (****spend_report_adj****)**: Implemented a consolidated region-mapping function in Databricks that standardizes regions (including mapping Central America to North America) and enforces consistent handling of APAC, EMEA, South America, Alaska, and excluded categories.

**Data Integrity Validations (****spend_report_adj****)**: Added safeguards to raise exceptions if the new mapping ever produces null regions or drops existing rows when overwriting spend_report_adj, ensuring region logic changes cannot silently degrade data coverage.

**Initial Stakeholder Check-In (Regional Mapping Usage)**: Verified with business stakeholders that no issues have been observed so far from the updated delivery-region mapping in downstream reporting.

**Ongoing:**

**ETL Scheduling & Operationalization**: Awaiting confirmation on an appropriate schedule for running the updated regional-mapping ETL, and planning how best to plug associated validations into any consuming pipelines so that failures are surfaced early instead of downstream.

**Pipeline-Wide Validation Integration**: Reviewing existing notebooks and validation patterns (e.g., row-count checks, freshness audits) to design a reusable pattern for integrating the spend_report_adj checks into the broader IBP pipeline.

**Ben and Camila**

**Supply Chain**** IBP****:**

Project: IBP | Data Lineage & Table Reference Automation 
[DOE-1317] Table References Script - Jira

**Completed:**

**Automated Table Reference Extraction (Table_Search.csv)**: Ingested a curated list of unique tables from the DA2I-RCG_SUPPLY_CHAIN repository and built a script/experiment that scans code artifacts for table references, logging structured JSON to MLflow for easier lineage and dependency analysis.

**MLflow****-Backed Experiment Setup (Table Reference Logging)**: Configured an MLflow experiment to capture table-search runs with a consistent JSON schema, enabling reproducible analysis of where and how key tables are used across the analytics codebase.

**Ongoing:**

**False-Positive Reduction & Logic Refinement**: Actively refining the detection logic to remove read/write-focused heuristics that rely too heavily on surrounding context (current source of false positives), with the goal of making the table-reference script reliable enough for broader automation and follow-on tooling.

**Next-Step Automation Opportunities**: Considering follow-up enhancements—such as automatically surfacing impacted notebooks when a table changes or feeding lineage into validation frameworks—building on the current experiment now that the core extraction is in QA-ready shape.

**Caleb**

**CLV**: Demand Forecast

**In Progress:**

Validating full 2025 Actuals to be able to rerun our ETL pipeline (PCDs, Pax, NTR, OBR)

Continuing to clean/transform competitive pricing data into ingestible format for demand model

Assisting with auditing fleet model and competitive deployment excels in effort to provide clean, validated figures for Situational Assessment report

**Completed:**

Reconfigured validations to check important measures aligning to EPM + VCAP wherever data is available -- increasing our data's robustness and trustworthiness

Added measures checked:

Distinct sailings

Deployment by meta product

Average sail length

Book-to-sail-window methodology/density

Booking type split

Meta + RDSS channel proportions

Mirielle

Contact Center: **Workforce Planning – North America (Royal)**

**Baseline Model Calibration**

Continuing to calibrate the model using **Loyalty** and **STAR**, the LOBs that do *not* share agents. Darren provided the current FTE values for these groups to support calibration.

Building both:

an **ErlangA**** model** targeting **abandon rate**, and

a **Service Level–based model** targeting **SL%**.

Successfully completed **backtesting**** of the FTE model** for Loyalty using **January and February 2026** data. Finally, a Happy result:

Loyalty January FTE 2026: actual (68), Model by SL (67), Model by ABN (83)

Loyalty February FTE 2026: actual (52), Model by SL (53), Model by ABN (68)

The backtesting uses **true call volume** and **true operational assumption ****inputs**(office shrinkage, servile level, abandon rate, average answer speed, avg patience).

Key insight: **Any small modification to assumption inputs (AHT, shrinkage, occupancy, intervals, etc.) will ****impact**** the resulting headcount**, making assumption management essential for stability.

The Erlang A model with service level as the target is definitely the strongest one.

**Why Service Level Over Abandon Rate?**

We can't control when customers hang up — but we can control how fast we answer.

Abandon rate depends on customer patience, which is unpredictable and outside our control. A customer may hang up after 10 seconds or 10 minutes — we have no influence over that.

Service level (e.g., "80% of calls answered within 60 seconds") is a target we can directly act on by adjusting staffing. It gives us a clear, actionable goal that drives the right staffing decisions. In short: We should staff based on what we can control (how quickly we answer), not on what the customer controls (when they give up).

There is a request to experiment with a **30minute interval model**, while the current modeling approach only supports **1hour intervals**. Moving to 30minute intervals may delay the delivery of this phase because it requires additional work, including building new matrices for office hours, updating callvolume proportions, and reviewing parts of the model design.

For now, the plan is to **first complete the initial ****ErlangA**** model using 1hour intervals** before extending the framework to support 30minute intervals.

By the end of the project, the portfolio of models will include:

**A. ****ErlangA**** Model — 1Hour Interval**

Erlang model with **Abandon Rate** as the target

Erlang model with **Service Level** as the target

**B. Adjusted ****ErlangA**** Model — 30Minute Interval**

Erlang model with **Abandon Rate** as the target

Erlang model with **Service Level** as the target

Mirielle

Contact Center: **Workforce Planning – North America (Royal), App Enhancement /Call volume adjustment**

**1. Enhancements Requested**

Enable the app to support **multiselection** of LOBs and return **combined results**.

Add the ability to apply an **alpha adjustment by month** for modifying call volume forecasts.

Expand KPI cards to include **Avg Service Level** and **Avg Answer Speed**

**1. Better Visualization — Historical vs Forecast vs Adjusted**

We added a new chart that displays **three bars side by side** for each month:

**Historical** (actual call volume)

**Forecast**

**Adjusted** (usermodified forecast)

**Why this matters:** Users can now see how adjustments compare to real performance, making it easier to spot over or undercorrections and improve the accuracy of monthly planning decisions.

**2. Data Integrity — Saving Complete Daily Detail**

The system now **always saves data at the daily level**, even if the user is working from a monthly view.

**Why this matters:** Daily granularity is essential for downstream FTE modeling. Saving full detail prevents rounding errors and ensures staffing calculations remain accurate.

**3. Accountability — Tracking Who Changed What**

Each saved forecast now captures:, **User name** (required field), **Save month**, **Tier label** (Draft, Preview, Final)

**Why this matters:** This creates a clean audit trail, especially important when multiple users collaborate or adjust forecasts within the same planning cycle.

**4. Controlled Access — ****ThreeTier**** Save System**

We introduced a structured saving workflow with access control: Each level requires a **unique passcode**.

**Why this matters:** It prevents accidental overwrites and ensures that only authorized users can publish final planning numbers.

**5. Historical Tracking — No Data Overwritten**

All saves, at every tier, now write to a **single ****nonoverwriting**** backup table**. 
Tierspecific tables (Draft, Preview, Final) update only within the current month.

**Why this matters:** Teams get:

A **clean working space** for the current planning cycle

A **complete historical record** for auditing and comparison

Nothing gets lost.

**6. Database Resilience — Automatic Schema Updates**

When new fields are added, the system automatically updates existing tables by adding missing columns. **Why this matters:** This prevents errors caused by outdated database schemas and reduces the need for manual intervention.

Next Step:

Run the FTE model with the real call volume forecasted data

Run the FTE model for each LOB with the baseline assumption data

**Mert**

**MIAP**

MIAP fuel savings reached **$1M for 2026**, bringing the **cumulative total to $7.6M**.

Completed ETL, processing, and vector database creation for Newbuild SharePoint archives using Databricks and Azure AI Search.

Prepared detailed reporting for Newbuild on the AI Observatory project for **Hani Aid** to present to **Harri**.

Met with GMO teams for the monthly AI strategy discussion.

Met with the deployment team on deployment optimization initiatives.

**Mahshad**

**MIAP**

Increased anomaly detection savings to approximately **$1M** by adding savings from **WN AHUs, OV AHUs, and SC AHUs**.

Added the overall **chiller COP pipeline**; some additional debugging is needed before adding the Agent for chiller anomaly detection.

Identified anomalies on **ML TCV valves, WN TCV valves, and SC TCV valves**, and followed up on data issues for SC chillers.

**Will**

**MIAP**

Added shore power data to the **GMO Silver ETL**.

Added FACTs ship metadata to the **GMO catalog**.

Added FACTs port metadata to the **GMO catalog**.

Reported RF deviations and met with the **RF Chief Engineer** to discuss findings.

Added load data to power plant figures to better diagnose identified deviations.

Integrated shore power into the **MIAP REST API** and **MIAP Web App**.

Added dtm to FACTs Mode results columns in the digital twin package to enable Web App integration.

**Reza**

**MIAP**

Prepared three workflows to support the **Fuel Forecast Platform** for **2025, 2026, and the Union workflow**. Each workflow calculates Digital Twin outputs, Finance team prediction outputs, FACT actuals, and sensor-based actuals for every ship at both leg and voyage levels. The output is a consolidated table with all calculated values and performance metrics.

Deployed the workflows to **QA**, optimized configurations for efficient parallel processing, and completed full testing and validation. The workflows are now ready for promotion to **Production**.

Conducted regular monitoring of the **Service Power area** to identify anomalies, model issues, and data quality concerns.

Continued improving model accuracy by analyzing Finance predictions and adjustments, refining calculation logic, and enabling more accurate apple-to-apple comparisons between model results and Finance forecasts.

**Ram**

**MIAP**

Finalized **Bronze layer** ingestion logic and initiated requirement gathering for **Silver**** layer** table structures.

Resolved critical issues for the Silver layer deployment and continued refining notebook logic to implement a permanent fix.

Developed code to track file counts by crosser in **ADLS**, establishing validation checks to identify missing data.

Updated Eniram rerun notebooks to support historical data loads, with ongoing enhancements to ensure process stability.

**Arya**

**MIAP**

Developed ship configuration folders for the **digital twin powerplant**, documenting fuel lines, MCR values, and scrubbers.

Experimented with testing **no****-optimization mode** in the digital twin Web App.

Added EQ to machinery and began calculating baseline values for fuel analytics; updated deployment documentation with machinery details.

Conducted **three ****deep****-dive**** analyses** on potential anomalies in ship machinery and hotel components; will follow up with shipboard engineers regarding set-point changes.

Developing a framework for a **machinery diagnostic agent**.

Fixed **SFOC diagnostics reports** and updated training data to improve curve fitting.

Lamis

CEL Revenue Management: Track Optimization:
WIP - extracted predicted future SPI-based top performers to compare their tracks against the optimal. This is in progress - results are to be validated/analyzed/visualized and reported.

Lamis

RCI Revenue Management: Track Optimization:
- Revised the bkg waves flag based on the feedback received from Nick in Dec
- completed code adjustments to run the DP on the entire fleet. 
- made necessary code adaptations to generate demand curves for RCI sailings, generated all curves for RCI and saved them in UC
- Ran the DP-based track optimization on RD calculated metrics and compared them against the business tracks on sailing and aggregated levels.
- Ran the track optimization on the entire fleet. Results need to be validated and compared against SPI tracks and business tracks.

Javier & Glen-erik

PROPEL

Measurements: (Javier)

Presented the new measurements results and collected feedback. Made improvements to the metric calculations.

Ability to compare test vs control purchases that occurred after an offer was made and calculate APD and uplift based on those future days after the offer.

Identified edge cases like 100% awareness sailings that were causing issues with the APD uplift calculations, will filter out awareness only sailings.

Created a mapping table for offer to purchase category and aligned with Meital.

Identified additional mapping gaps/requirements for purchases to ensure end to end mapping is correct (offer to purchase category accuracy). Some products show up in the wrong category in the purchase history data, like HHG. *Next step: **Creating a report for the purchase categories that don't match up like Onboard Activities, HHG, Packages (**shipex** vs package), and Other.*

Support: (Santiago)

Missed runs due to bug in code. Bugfix should be finalized by Monday, running manually for EQ when needed in the meantime.

Resolved the timezone transition issue that occurs when a ship changes time zones during sailing, and 11's days missing information. The fix addressed the logic so time-based calculations remain aligned when the vessel crosses into a different UTC offset.

24/7 support: (Glen-Erik)

Pager duty setup

Presented Service now form to business to collect feedback, still need feedback from Garrett.

Eswar:

RCI Revenue Management

Data Validation Framework:

Reviewed PRE output data validation process

Updated the framework to accommodate additional checks needed

Updating sharepoint authentication method as the existing one getting expired

Evaluating strategy in Hosting stating Web app vs docker based solution for a  RM application

Deploying flask app via containers for factor model

PR review and CI/CD monitoring

Glen-Erik

PCP Pricing Automation

Email:

Aligned data requirements with marketing and ecommerce.

App:

Prod data table created so DE can work on the pipeline to kafka in preparation for the copy being ready and testing with a 2030 prod dummy sailing.

New schema, kafka topic, and testing almost finished by digital so we can use if for the next offer.

Kevin

PCP Pricing Automation

Currently Data Science and ML engineering team are awaiting feedback from Digital for next steps on 1:1 testing. The team has successfully stress-tested creating offers in Databricks by Data Science, stream these offers through Apache Kafka by Data Engineering, and offers are created automatically in Hybris by Digital Teams. Digital is testing the Service that Takes Offer in Hybris and dispatches to Notification Gate. They want to take an event and scale it up to pressure-test the system. Goal is to send >10,000 messages to see if any micro-services crash or display unacceptable performance. Go-Live has been moved from 3/23 release tentatively to 4/9 release.

Ignacio

PCP Pricing Automation

**Adjustments for final promo automation testing**

The final round of testing was ready to be done for promo automation. First, the catalog schema for the UC table used for promo automation uploads was updated to the new DS catalog schema (instead of the DE one) in order to allow easier write/delete access for the promo automation workflow. In addition, the code was slightly adjusted in order to allow for the ability to leave START TIME of a promo empty, which the system will be able to fill in with the current date time (this is often used in preview mode). These changes were made and final steps of testing were then completed for final validation of promo automation.

**Adhoc**** meetings & help regarding OBR**

A meeting was had with Anaand regarding A/B testing gameplan for waterpark.

**Recurring meetings with business team**

The EDA findings were shared with the CEL team (Correa & Garrett). They provided feedback for additional adjustments to the EDA to share with them & next step plans were discussed moving forward.

Additional meeting was also had with Gaby to discuss Bev and its A/B testing plan

**E2E Final Promo Automation Testing in Production**

A final set of testing for the promo upload automation was done across several sessions:

**first session**: tested purely on preview mode promo uploads, tessting all promo conditions

§ all tested promos succeeded as expected

§ a few extra promos were purposefully created with errors (nonexistent product codes and sailing IDs) in order to make sure that they were not reaching the state of approval/rejection decision -- this also worked

§ approval step also worked as expected

§ only promos with defined start dates were tested

**second session:**

§ meant to test actual production promo uploads (no longer preview); adjustments had to be made to the created promos in order for them to work for testing

§ all promos were made for the MA 2030 test sailing

§ promos were also now tested with empty start dates -- the changes were made & tested in lower env in order for this to now work in prod

§ this process highlighted a few important notes for the automated promo process guardrails in order to make sure it works:

• code will automate the uploads for the RCI_Sharepoint_Automated_Promo_Uploads.xlsm file in the prd SharePoint folder; if the spreadsheet is not in this folder (or not with the correct name), the upload workflow will fail since it will fail to find the file

• if several tabs are created in the excel file, the code will only read in the first one (left-most tab) for promo automation, so it's important to make sure the one for upload is placed correctly (name of tab does not matter)

§ testing was not completed -- there was issues with the cluster on the data engineering side that caused the testing to fail. Testing is to be repeated and finalized the next day

**third session:**

§ testing was run again to complete what failed yesterday due to the issue with the cluster from the DE side for kafka processing

**RCI Beverage PRE A/B Test**

Power Analysis + Analysis on distribution of data

A power analysis was run to determine the number of samples needed to prove significance for the beverage A/B test for RCI. the KPI being used is revenue normalized by both pax & sailing nights, which results in a fairly normal distribution.

Given high sample size resulting from this, the power analysis is being repeated segmented by meta (focusing on 7N & SHORT CARIBBEAN) & seasonality. This results in much more reasonable required sample sizes for the test.

Aagam

**PCP**** Pricing Automation:**

**RCI | OBR | RBC Dashboard v2**

Analyzed RBC Passes and RBC Bundles based on the dashboard and presented my preliminary findings to the business.

Insights Passes and Bundles.docx

RCI | OBR | RBC Dashboard v1

This week I focused on updating the RBC Dashboard based on the following:

Adding Cat Class level insights (revenue split, customer count split, and booking lead time)

Indexing the different groupings to compare the conversion rate of customers buying any RBC pass/bundle/cabana/daybed (understanding out of all the customers in a given group, how many of them end up purchasing an offering)

Analyzed the RBC Bundles for the past 90 days and provided my analysis to the business team

Published the changes recommended by the team and added a few cat class level insights to better help decision making

Kevin Diaz

PCP Pricing Automation

**Beverage PRE:** We are planning two tests for different versions of the recommendations:

Weekly Price Recs / Demand Targets with the goal to hit ending volume forecast.

Weekly Price Recs / Demand Targets with the goal to hit last year’s achieved volume +5%.

This week we focused on designing the test and have been taking steps to limit the number of sailings needed to achieve statistical significance. We plan to propose test sailings next week. The test should be run through the mass promotion writeback that should be enabled soon.

**Waterpark testing:** Similar to Beverage we expect to have a testing plan next week. This week Anand completed some EDA and initial power analysis as he became more familiar with the dataset.

**RBC: **Aagam has been working with Maria to enhance the monitoring dashboard and recommended sailings for the new A La Carte Trial. Aagam is also preparing the results of our first few tests since the sailings are beginning to wrap up and will be sharing the results and findings next week.

**ShoreX**** Classification: **ShoreX Classification is a foundational project that will enable us to work on ShoreX Recommendations beyond private destination. Anand has been working through analyses on Alaska and other Meta products at the request of the Celebrity Brand. He will be replicating the analyses for RCI as well.

** **

In addition to these, I would like to propose the following tests for boost as we discussed yesterday:

Notification to guests $X away from the next free tier i.e. Oceanview to Balcony

Notification for guests to bet $X in X min/hours for $X in free casino play.
