**Carlos A.****
****E-****C****ommerce**** Customer Targeting**

Updated alerts pipeline, now it uses teams workflows, instead of webhook connector.

**Carlos A**

**Loyalty****: Loyalty Simulator**

Find and fix bug that caused loyalty tiers flattening after oct 2025, replaced  simulation_base pipeline (from erick) since we are not longer computing loyalty based on spending and  was breaking.

Generate status report for stakeholders.

**Carlos A.**

**Win on Waste:**** Food Tracking with Computer Vision**

Showed POC app to IT stakeholders, and agreed on next steps.

The IT/Hotel Ops teams will provide trial data, where 10 items from a Specialty Venue, where we get image screenshots on an IPAD and records the waste weight.

Carlos will build an approach leveraging world foundational models + tuning (either using model fine-model tuning or infer weight using a ML regressor) that labels the images and estimate the weight from the image alone.

**Bao L.:****
****Weekly Update: May 24 to May 28, 2026**

**Completed**

Successfully delivered all historical May 2025 and March 2026 model scores to ecommerce stakeholders for campaign and email analysis

Fixed a ZeroDivisionError bug in the PCP historical scoring pipeline and completed CEL March 2026 PCP historical scoring

Completed EDA for 5 new clickstream features, including performance benchmarking and brand split analysis. Features show a stable +1.4% AUC lift for PG consumers and marginal +0.6% for PR (May 27). The 5 features are:

avg_session_duration_sec: average time a consumer spends per web session

n_distinct_departure_ports: number of distinct departure ports a consumer has browsed

n_distinct_shipcodes: number of distinct ships a consumer has viewed (requires brand-level logic due to performance differences between PG and PR segments)

funnel_velocity: rate at which a consumer moves through booking funnel steps per session

funnel_revisit_intensity: average number of booking funnel page views per funnel-entered session

Discovered and diagnosed a clickstream data staleness issue. The ingestion pipeline has never been wired into the production ETL, meaning all 39 existing clickstream features in weekly scoring have been operating on stale data. Root cause confirmed and fix designed

Built an MLflow history ETL notebook (model_drift_etl.py) that pulls model evaluation metrics and feature importance scores across all 6 model groups dating back to 2023. Results are written to two new Delta tables for dashboard consumption

In Progress

Implementing 5 new clickstream features into production and wiring the clickstream ingestion job into the MKT Models ETL pipeline

Building a Databricks dashboard on top of the new history tables to visualize model performance drift and feature importance shifts over time (relevant for assessing impact of app usage feature additions)

**Ben F. **

**IBP: Forecasting Improvements **

This week my work focused on two major Supply Chain analytics priorities: improving the Marine Consumables forecasting pipeline and building a more scalable data foundation for Silversea Supply Chain.

For Marine Consumables, I advanced the forecasting work through a full research-to-production cycle. The work included diagnosing upstream data quality and engineering issues, correcting foundational pipeline logic, and iterating through several model and feature-engineering versions. The main outcome this week was moving the Marine pipeline into a stronger validation position, with better traceability into what is driving forecast behavior and which data issues need to be resolved before we make any formal performance claims.

For Silversea Supply Chain, I built and refined a ship-aware data unification layer that brings together MMS and Crunchtime consumption/spend sources. This is important because Silversea ships are transitioning systems over time, and downstream reporting/modeling needs one consistent view regardless of which source system a ship is currently using. The new layer supports cleaner source selection by ship, reduces duplicated downstream logic, and creates a more reliable foundation for SSC reporting, finance analysis, and future demand modeling.

The broader impact of this week’s work was to reduce risk in two high-priority areas: improving confidence in Marine forecasting before production decisions are made, and preparing SSC for a cleaner data-source transition as ships move between operational systems.

Current Status / Next Steps

Marine Consumables remains in validation. I am not yet treating the model results as final until the remaining data checks and comparison work are complete.

SSC data-source unification is substantially advanced, with the next focus on validating downstream consumers, confirming edge cases by ship/source, and ensuring the new unified view can support production reporting and modeling workflows.

**Camila A.****
IBP: CEL Beyond Pilot****
**Working on seasonality guardrail for Beyond and Summit pilot

with an additional layer of comparing to the budget so that if the prediction needs to be increased due to the comparison then the increase is applied but still below the budget

Working on venue + daily breakdown for Beyond and Summit pilot

Pending: add vendor conversion for order creation actual quantity needed (focused on Beyond)

Enhanced guest counts for RBC using order entry table instead of the originla source that only contains RCI data to find onboard and pcp guest activity for Hideaway, coco beach club, Nassau rbc, and Santorini RBC

Gained some insight from Mario about Santorini. For example, no consumption data will be available for Santorini anytime soon due to a third party handling that.

Medical enhancement improvement: 55.485013746595996 -> 42.93953776359558

**Nicolas T.:****
IBP: **MOT Data Calculation Change

· To Do · Very High

Completed:

Built Notebooks that requested to the MOT calculation in: MOT_Value_Comparison_Monthly, MOT_Value_Comparison_Monthly_QTY_PCD

Built MOT Cruise-vs-Monthly consistency validation notebook (Wed 5/28): Created the MOT_Cruise_vs_Monthly_Consistency_Check notebook comparing ship-level grain (SUM(Value) for each sailing in a given month) against month-level grain (Value for the given month). Ran 18 validation checks — 5 failed:

C3: CURRENT_PCD (SUM) — 116 mismatches

C10a: CURRENT_SAILING_NIGHTS (SUM deduped) — 4 mismatches

C10b: CURRENT_PAX (SUM deduped) — 4 mismatches

C10c: CURRENT_PCD (SUM deduped at cruise level) — 4 mismatches

C10d: CURRENT_PCD_SAILINGS == COUNT(DISTINCT cruise) — 4 mismatches

Ongoing:

Investigating Beyond/Summit discrepancies: Determining whether the Beyond/Summit 07/2026 and 08/2026 mismatches are a data quality issue or a logic gap in the aggregation from voyage-level to monthly-level MOT.

RCI/CCI HF&B Order Creation Dashboard MLS Discrepancies

· In Progress · Highest

Completed:

Met with Fanny — no concerns with findings (Tue 5/27): Shared validation findings with Fanny, who expressed no concerns given her main priority is replicating the Excel file (which Paolo had accomplished). Recommended putting Paolo's proposed table changes on hold until a definitive answer is obtained on the MAX(batch_id) logic enabling those changes.

Documented Paolo's batch_id clarification (Wed 5/21): Logged Paolo's response — Narendra originally provided the MAX(batch_id) guidance to remove old/invalid/duplicated rows. Also noted Ben's parallel validation work using a separate notebook (MLS_Excel_vs_qa_gold_validation.ipynb) for another MLS source (dev_datascience.ibp_sso.master_load_schedule_source → qa_gold.ibp.rcg_master_load_schedule).

Investigate Consumables Consumption across SSC at Cost Center Level

· In Progress · Medium

Completed:

Scoping call with Camila on cost-center allocation flaw (Mon 5/26): Discussed a potential flaw in the current logic: uniform demand is distributed across cost centers based on crew staffing counts, not actual consumption. This means cost centers that never consume a given product still get allocated demand. Agreed on investigation path:

Check if Silversea consumption table has a cost center field

If not, explore a Silversea Item Code → Final Cost Center mapping from the Royal/Celebrity PRD Gold consumption report

Compare cost centers in crew table vs. consumption reports

Ask Yan about Silversea cost center data availability

Confirmed no cost-center field in Silversea Consumption (Tue 5/27): Investigated the Silversea Consumption report and found no cost-center related field. Now exploring alternative approaches using historical consumption patterns to establish likelihood-based allocation across cost centers.

Ongoing:

Alternative allocation approach: Investigating whether historical consumption patterns can be used to derive cost-center allocation weights as a substitute for the missing field.

SSC Consumption and Prediction Ratio Adjustments

· In Progress

Completed:

Executed run_adjusted_tables_step_1.py (Thu 5/22): Ran the adjusted tables pipeline covering:

uniform_no_job.py — creates crew count data with contract_length filled as 3 months, sourced from ssc_uniform_checkpoint (written by CREW_COUNT_ETL.py). Documented the full lineage.

crew_consumption.py — reads from prd_gold.ibp.ssc_consumption_report, creates crew consumption of uniforms across all variants, and outputs to SSC_UNIFORM_CONSUMPTION_{VARIANT} tables.

Flagged crew-staffing vs. consumption-based distribution concern (Mon 5/26): Identified that in both unpivoted_table_adjusted.py and crew_consumption.ipynb, predicted uniform demand is distributed using crew-staffing ratios (proportion of crew in a group) rather than consumption-based ratios (proportion of products actually consumed by a group). This means crew groups that don't consume a product still receive allocated demand.

Ongoing:

Addressing allocation logic: Working with Camila to determine whether the crew-staffing-based distribution should be replaced with consumption-based allocation, which ties directly into the cost-center investigation in DOE-2104.

**
****Caleb**** S.**

**Consumer Lifetime Value (CLV)**

Completed

Met with Kiana and Vanessa (5/22) to review productionization progress — traced cost allocation logic, prepped EPM output tables for direct cost-of-acquisition ingestion into our pipeline, and validated table sourcing for the current POC.

Identified errors in the CLV stage table caused by an NVL statement pulling from the wrong channel field (creation instead of credited) — an issue we originally flagged during 2025 validation. Working with Lissette to rebuild the stage tables with corrected logic that ties to actual channel mix.

In Progress

Building EPM queries to trace P&L cost-of-acquisition values for 2026 actuals (March onward). This involves mapping account tagging, org-level mappings, and studying BCG's prior work on the allocation process. Currently troubleshooting an incomplete form that claims to calculate cost of acquisition by channel but doesn't account for the full runway of brand-allocation dollars from shared services.

Supporting Corp Strategy with an analysis of booking behaviors among potential Upper and Luxury guests who sailed on RCI and CEL in 2024–2025.

**Caleb**** S.**

**Consumer Lifetime Value (CLV)**: **Sailing Environment**

Completed

Met with Neila, Eddie, Ben, and Gaby to align on project structure and initial milestones — covered ownership, goals, next steps, and data acquisition considerations (capacity, pricing, competitor fleet, deployment, etc.).

Shared Corp Strategy's full demand model repo — data sources, queries, ETL pipeline, EDA, modeling, testing, and validations — along with a comprehensive summary and inventory document

Erick A.

**PCP ****MyCruise**** Recommender**

*Personalized post-booking recommendations (excursions, dining, spa) powering the **ForYou** surface in the app.*

**Productionization (Cristian V.)**

**Team model upgrades moving to production:**
The team’s recommender improvements—David’s faster training and metrics, Osvaldo’s product clustering, Danusio’s guest segmentation, and Rodrigo’s cold-start—have been queued for several weeks awaiting review.

Backlog is now in active integration.

Cristian owns rollout of all four components.

David’s contribution is nearly implemented.

**Infrastructure / Postgres & API (Cristian V.)**

**Postgres dev/prod separation:**

Full code refactor completed to split database traffic between dev and dedicated prod Postgres instances.

Successfully deployed and working in **dev**.

**Prod remains blocked** due to network/firewall issue.

Databricks secrets (replacing hard-coded credentials) are now live in the email job and replicated into the recommender.

**A/B Testing (Cristian V.)**

**Recommender-owned A/B testing enabled:**

Digital (Lance’s team) added a parameter indicating which page a user is on.

This allows the recommender to track who received which recommendation and where.

Enables Data Science to own A/B testing instead of relying on engineering instrumentation.

**Initial test ideas:**

Margin vs. revenue re-ranking.

Recommendations with vs. without hard-coded business picks.

**Open question:**

Apigee caching behavior must be understood, as caching may distort exposure tracking.

**Tooling (Cristian V.)**

**DevOps → GitHub migration:**

Planned migration of recommender project from Azure DevOps to GitHub.

Aligns with broader team version control standard.

**Business-input form app:**

Lightweight app for business users to input promoted-product selections.

Writes to a Databricks table (no Postgres dependency).

Prioritized after productionization.

**Blockers**

Postgres prod deployment blocked by network/firewall issue.

Erick escalating via ServiceNow with Marcio and Jose.

Apigee caching behavior must be resolved before A/B testing can be trusted.

Erick A.

**Project Axiom — Voice 360**

*Insight extraction from unstructured customer feedback (Medallia, Guest Logs, Qualtrics) via LLM pipelines—feeding emails, dashboards, driver analysis, and chat.*

**Email Reports**

**Port Email (Rodrigo B.)**

**Presented to ****stakeholder****:**

Reviewed with Josh Carroll.

Next steps:

Rank topics by importance using driver model coefficients.

Show topic shifts vs. prior quarter.

Refine LLM prompt and report structure.

Implementation in progress.

**Royal Santorini Beach Club Email (Rodrigo B.)**

**Ready for automation:**

Weekly scheduled send capability (Mondays) now complete.

Awaiting stakeholder approval before activation.

Erick confirming go-live timing.

**Shorex GSO Safety Email (****Danusio**** G.)**

**Fleet rollout:**

Presentation scheduled for **June 3–4** to RCI and Celebrity fleets.

Danusio preparing briefing materials.

**Meta Data Framework**

**GitHub Action live in production (David M.):**

Databricks token blocker resolved (via Eswar).

Automated CI/CD pipeline now running for divisions workflow.

**Guest Logs integration nearly complete:**

Final guest logs table created with standardized structure:

Sentiment

Topics

People

Places

LLM cost/runtime metadata

Enables cross-source topic tracking.

Initial guest-logs report in development.

May migrate report logic into metadata-generation repo for reuse.

**Blocker**

CI/CD pipeline blocked pending service principal access to required tables.

**Drivers Model (Osvaldo V. → David M.)**

**Handoff complete****; next phase underway:**

Osvaldo transferred model and notebooks to David.

Next steps:

David builds booking-level feature dataset from guest logs.

Features based on topic frequency per booking.

Osvaldo retrains model after dataset completion.

**Webapp — 3D Ship Model (Rodrigo B.)**

**Clustering reworked for usability:**

Replaced DBSCAN with Gaussian Mixture Model (dynamic clustering by date range).

Adds:

Adjustable severity slider.

Improved interpretability.

**Fixes completed:**

Corrected LLM API key issue.

Fixed insight pop-up.

Resolved unintended LLM calls on hover.

**Next step:**

Validate clusters against known noise hotspots (Symphony OTS decks 3, 9–11).

**Webapp — 3D Globe Visualization (Osvaldo V.)**

**Map view in development:**

Visualizes excursion-category distribution by port.

Current issue: pie-chart scaling when zooming (JS rendering limitation).

Potential shift to alternative GIS library.

**Celebrity Operations Analysis (Osvaldo V.)**

**Ship reports recreated:**

Xcel and Silhouette reports regenerated using new LLM-compiler approach.

**Follow-ups:**

Migration from Google Colab to GitHub Copilot (aligned with Azure environment).

Erick sharing report with stakeholder (Gabby) for operational feedback.

**Erick A.**

**Project AXIOM: Web**** Scraping**

*Unified scraping platform across Consumer Insights, Hotel Operations, Product, and **Social Media**.*

**Phase 1 — Review & Forum Sources (****Danusio**** G.)**

**Scrapers fully functional:**

Sources:

Cruise Critic

Booking.com

Reddit

Royal Caribbean blog

Browser (TamperMonkey) and Python outputs aligned.

Icon of the Seas full sample pull underway.

**Blocker**

**Reddit account banned:**

Browser and Python scraping no longer viable.

API-based pipeline (Reddit API) now the **only path forward**.

Reddit ingestion paused until implemented.

**Phase 2 — Social Platforms (****Danusio**** G.)**

**TikTok progress:**

Working scraper for comments and metadata (browser version).

Python version pending.

**Next steps:**

Benchmark TikTok APIs for link-search and transcription.

Build pipeline:

Rapid API → yt-dlp → transcription

Objective: analyze influencer and user sentiment on ships.

**Erick A.**

**Project AXIOM: ****Project Concept Testing Lab**

*LLM-driven synthetic personas for pre-testing concepts using **TinyTroupe** (Microsoft OSS).*

**TinyTroupe**** operational; first outputs generated (Osvaldo V.):**

Framework running locally.

Initial outputs produced for:

Single grounded persona

TinyTroupe-generated personas

**Program positioning:**

Framed as “Concept Testing” app with GenAI CoE and Hannah (Ecommerce).

Interest from Consumer Insights and Product.

**Defined deliverables:**

Persona for sample segment (e.g., younger couples).

Personas derived from Medallia feedback (e.g., food/wine enthusiasts).

One-page stakeholder report in development.

David W.

Loyalty: Merge Recommendation Engine

The team is aligning on the timeline to validate ~43K co-brand match pairs against MRE engine recommendations using the dataset dev_bronze.consumer_ld_mdm.cobrand_consumer_merge_pairs_0529_all, with David Whitney and Jason Fortier responsible for confirming execution timing and overall merge completion. This effort supports the broader Co-Brand initiative, including reconciling ~40K Bank of America records not currently in RCG systems and assessing duplication via MRE-driven matching rather than prior batch merge approaches.

Execution has been paused for broader merge dependencies, with a revised target of June 2nd pending data submission from Sujeet; ~80% of records meet high-confidence thresholds, while ~10K lower-confidence matches will be exported for Data Steward review. Key dependencies include inbound bank file timing (expected Tuesday), defining MRE-based merge conditions, and resolving edge cases if merges cannot be completed, aligning with Project EASE goals to proactively resolve data issues before customer impact.

David W.

New Build

Aligned with Joseph and our finance team that we will right a NewBuild CAR and socialize this CAR with Matt. Currently NewBuild has no allocated funds and the project will likely have to get prioritized on the capital allocations watchlist. David W is committing to writing a first draft CAR up over the weekend.

Ignacio V.

PCP Pricing Automation

**PCP2 | MAY - Recurring Business Meetings & OBR DS Meetings**

sync with Kevin on dilution model & work being done on the demand model

MDM matching rules meeting regarding data quality

update meeting with Rafa & Alex (CEL) regarding the dilution model

Aagam S.

PCP Pricing Automation

**OBR | Ad-Hoc | Kids Free**** at Royal Beach Club**** AB Test Prelim Insights**

For the analysis I compared the sales of the test and control sailings for the previous week vs the flash sale week, and I also compared the sales between the test and control sailings during both the flash sale weeks. The test and control groups were different tour dates They wanted to see if there was any value in letting kids go to RBC for free

**Initial Insights:**

The analysis shows a clear trade-off between the Test (kids free + adult surcharge) and Control strategies. The Test consistently increases average revenue per booking (e.g., +16% in Flash Sale 1 and +23% in Flash Sale 2), indicating stronger monetization. However, it underperforms on bookings, with a notable decline in Flash Sale 1 (-19%) and weaker growth in Flash Sale 2 compared to Control.

In contrast, the Control strategy drives significantly higher booking volume—especially in Flash Sale 2 (+115% vs +52%)—which ultimately leads to much stronger total revenue performance (+106% vs +87%).

Overall, the Test works well for increasing per-customer value, particularly in longer booking windows where families plan ahead, but it limits demand. During high-intensity flash sales and closer sailing dates, success is driven by volume and pricing simplicity, where the Control strategy clearly outperforms.
Following is the summary that I provided to the business team based on my analysis.

**RCI | PCP2 | CRF Automation RBC Passes**

This week, I focused on building the foundational data tables to capture sailings, RBC passes, bundles, and cabanas across all upcoming sailings. I structured the codebase to be dynamic and scalable, enabling easy expansion to support RBC products in regions like Europe and Australia in the future. I also ensured that key configurations, such as product codes used for identification, can be managed directly by the OBR team, improving both automation and flexibility.

I have also set up an automated process to pull all relevant sailing data for RBC runs, ensuring that we capture all the necessary data points required by the OBR team to calculate discounts based on their existing rule set.

The initial phase centered on automating the extraction of base tables, including:

Base pricing for passes

Base pricing for deluxe packages

Base pricing for cabanas

In addition, I developed ship-level metrics, including:

Identifying sailings relevant to the RBC process

Calculating ship counts at the time of the RBC call

Counting bundles, passes, cabanas, and daybeds for each sailing

The next steps would be to layer in the business rules, validate the results, and push it into prod so that it can run weekly for the business teams

Anand S.

PCP Pricing Automation

**1. Alaska ****ShoreX**** Consumer Behavior EDA for Celebrity - Deep Analysis — **Completed a comprehensive **8-chapter behavioral analysis** of Celebrity Alaska shore excursion consumer behavior spanning 2023-2025, directly answering Alexander's cross-price elasticity questions from last week's pricing strategy meeting. Built consumer-level journey profiles from dream_cruise_object and dream_new_commerce_ods: **460K ticket records**, **3M commerce events**, **2.8M timeline events** across **397K consumers**. Key findings: same-tour gaming is minimal (~90% rebook at same price, only ~6% capture a price drop, so the pricing model is NOT being broadly exploited), **Alaska ports are heterogeneous** (Juneau, Sitka, Icy Strait Point, Skagway each have distinct cancel rates and price levels and should NOT be pooled like Caribbean), and the cancel rate crisis is promo/channel-driven rather than a pricing model failure. Applied three audit-driven corrections (post-sail system refund exclusion, join explosion dedup, same-day swap separation). Developed recommendations for Alexander: **port-specific demand ****curves** (HIGH priority), targeted late-window cancel controls, promo-triggered rebook locks, and ShoreX-first pricing rollout.

**1a. Consumer Booking Journey Profiling —** Developed data models to analyze booking and cancellation behavior at the individual consumer level. Tables persisted in dev_datascience.anandshahtemp (cel_alaska_ticket_base, cel_alaska_commerce_events, cel_alaska_consumer_journey, cel_alaska_event_timeline, cel_alaska_ml_features). Generated 100-consumer journey visualization PDF. These form the foundation for propensity modeling and upcoming ShoreX's pricing demand model.

**2. Web Scraping Pipeline -**** Pending Compute Fix** **— **Pipeline run failed over the last week. Waiting on **Eswar **to assign appropriate compute so that it can come back up and running. Once we have successfully run Royal pipelines, I will focus on building the same thing for Celebrity.

**3. Sailing Clusters - Handover Sync Pending** **— **Waiting to sync up with Kevin to chat about next steps on this topic and accept handover from his and Jorge's work. Cluster assignments table (dev_datascience.sailing_clusters.sailing_cluster_assignments) is production-ready and ready to be leverage or updated per new business requirements.

**4. Significance Testing Pipeline ZH01** **— **Working with Aagam to run ZH01 product code through the significance testing notebook pipeline and working on building a stakeholder update. ZH01 = Thrill Waterpark Full Day Pass

**Upcoming Next Week:**

Sync with Kevin on track smoothing integration (spline code from Eddie), help with integration work

Continue ShoreX pricing model scoping, Alaska EDA findings feed directly into V1 business rules architecture

Resolve web scraping compute with Eswar; begin Celebrity pipeline build once Royal is stable

Deliver ZH01 significance testing stakeholder update with Aagam

Anneke A.

**SSC ****Revenue Management: ****PRE | Business Upgrades**

**Closeout Statement**

Achieved the following enhancements to the Silversea PRE model requested by the stakeholders:

Once within 20 weeks to sail, the farecode target changes to UL (last minute)

SSC PRE now uses post-promotional pricing but was expecting an absolute discount amount, now logic has been amended to allow for both absolute and percent discount strategies

Also finalized EDA on track and forecast metrics for Silversea, aiming to understand why some PRE recommendations are paused when “forecast is achieved.”

This month we enacted several enhancements to the Silversea PRE model such as enabling post-promotional pricing, developing and sharing a dashboard, and establishing weekly stakeholder calls to continue to refine and improve engagement with this model.

Srilekha M.

**CEL | Build Separate Promo Action Recommendation Process for Analyst Review**

**Status**: This ticket is complete as of **5/26/2026**

**Deliverables**:

Built an end-to-end Promo Recommendation Validation process, structured into two notebooks — one for transforming raw analyst Excel inputs into a clean dataset, and one for generating data-driven promo actions

Developed a Promo decision framework that evaluates each sailing using key drivers: Current Promo state, booked position vs best-performing SPI benchmarks, and weeks-to-sail timing

Outputs are simplified into clear actions: Stop Promo , Give Promo (aggressive/standard), No Action, or Monitor and added Promo reason that clarifies why that action need to be taken

Uses Tuesday pricing as the baseline and incorporates booking performance through Friday for that price point , aligning with the analyst’s weekly promo decision cycle.

Enables side-by-side validation of analyst intuition vs data-driven promo signals, helping identify alignment, gaps, and opportunities to optimize promo strategy

**Potential future issue**: None

Jesse B.

Silversea Revenue Mgmt:

**SSC | AB Test | Expand Upper-level suite EDA**

**Status:** This ticket is complete as of 05/20/2026

**Deliverables:**

Examined differences in price paid between bought upper-level suites and up-bid upper-level suites

Examined floor and ceiling prices for bought upper-level suites

Examined relationships between price paid versus sailing area, cruise ship, cabin category level, etc.

See attached text file for comprehensive organization of EDA figures and stats.

**Delays:** None

**Potential future issue:** We will re-visit EDA if the need emerges.table_of_context.txt

**SSC | PRE | AB Test | Upper-level Suites**

This work item involved preparing KPI analyses related to booking and pricing behaviors for management, with ongoing testing and approval processes.

Jesse Bausell compiled and organized EDA data, adding extra analyses as needed to support the KPIs.

A meeting was scheduled to seek management approval for the finalized upper-level suites pricing algorithm and to initiate bootstrapping.

The work remains in testing/QA at 90%, with further steps pending management approval and finalization of the pricing algorithm.

**SSC | PRE | Bootstrap-test upper-level suite model MAY**

No updates since last week

Kevin D.

PCP Pricing Automation

Continued development of dilution model for both brands. Presented the dilution model to cel leadership and got some constructive feedback. Iterating on that and working through the demand model next week

Michelle M.

CEL Revenue Management: Category Gapping

The team validated that a single optimization model is performing well against historical booking patterns, with initial business feedback confirming outputs are directionally accurate. Targeted post-hoc adjustments—especially to Lower-Premium tier shares—improved alignment with historical distributions and significantly reduced cases where GTY probabilities exceeded 50%, alongside fixing edge cases where extreme share targets (e.g., 90%) previously forced unrealistic GTY-heavy outcomes.

To further stabilize the model, a shift was made from static to dynamic, data-driven constraints: tier pricing gaps are now bounded using historical distributions (p95-based limits with controlled expansion), applied at a ship-class and category level. This replaces overly broad global constraints with row-level bounds, reducing unrealistic exploration while preserving optimization flexibility, improving output realism, and maintaining consistent revenue performance without changing core optimization logic.

**Category-Gapping 3.0**
- Last week, I spoke with business and demonstrated how a single model performs in comparison to actual historical shares and initial feedback is positive, the outputs are aligning with expectations. Some post-hoc adjustments of the single model outputs were needed. Tier shares for Lower-Premium adjusted to match actuals seen in historical bookings. This improved share matching and decreased the count of rows with GTY probabilities over 50%.
- Certain sailings had extreme desired shares (90%) for a single tier because of unbalanced capacity. This resulted in the optimization selling the space mainly through GTYs because it cannot find a matching row in the lookup table where feasible gaps result in 90% of bookings coming in for a single tier. In this case, I relaxed the share matching to allow for what is the max possible share in the table. For example, if the sailing desires a lower share of 90% but the lookup table only contains up to a 70% lower share, then this match should not be penalized because it is the closest feasible option. This has reduced the count of cases where gty share is > 50% by over half, significantly improving the outputs and not losing revenue through excessive GTY sales.
- Post-hoc adjusting single model outputs where needed. Tier shares for Lower-Premium adjusted to match actuals seen in historical bookings. This improved share matching and decreased the count of rows with GTY probabilities over 50%.
- Reviewing sailings with significant APD drops. Confirmed revenue calculations are correct for current vs optimal APDs. Identified needs for dynamic bounds in tier shares because static caps were allowing the model to explore outside of a realistic range.
- I implemented a data-driven approach to dynamically set gap upper bounds for each pricing tier and incorporated these directly into the optimization process. This improves both the realism and stability of the model outputs by aligning optimization decisions more closely with observed customer behavior.
- Instead of using fixed global limits for pricing gaps, I calculated tier-specific upper bounds at a granular level using historical data.
o For each gap type (e.g., lower–upper, upper–premium, lower–premium), I computed the 95th percentile (p95) of the gap distribution.
o This represents the point below which ~95% of observed values fall, providing a robust estimate of the realistic upper range.
o I then expanded this slightly to allow exploration beyond observed data, while still staying controlled:
§ Took the minimum of:
• 1.5 × p95 (relative expansion)
• p95 + 0.1 (absolute expansion)
• 1.0 (hard cap)
o To prevent overly tight bounds in sparse cases, I also enforced a minimum bound threshold.
- Result → Each ship-class/cat-class now has a custom upper bound per gap, grounded in real data but allowing limited extrapolation.
- Previously:
o The optimizer searched over static, global gap grids (e.g., all scenarios evaluated gaps up to fixed values like 0.20 or 0.15).
o This meant:
§ Over-exploration in unrealistic regions
§ Inconsistent behavior across ship classes and categories
- Now à The optimizer builds row-level search grids dynamically:
o lower_upper_gap is bounded by the row’s lu_upper_bound
o upper_premium_gap is bounded by up_upper_bound
o Similar logic applied for other models (LP, GLP, etc.)
- The rest of the optimization logic (spillover, capacity constraints, penalties, etc.) remains unchanged.

Lamis A.

RCI & CEL Revenue Mgmt

**CEL| RCI Track Optimization**

**DUAL: Model Error ****Analysis**** + Error ****Adjusted**** P-d curves**

Fixed some errors that were causing the error-adjusted demand curves not to look as expected. Completed a run on RCI EUROPE to test the results after factoring-in the prediction model error. The full EDA on results will fall under June scope. Implemented the same changes to CEL and EDA is yet to be done.

** It is important to note that the current advances in track optimization are all based on the old demand model version. A lot of validations and EDAs will need to be re-done after the new long-term demand model is pushed to prd.

**CEL: Align and validate input data with business stakeholders**

During this week’s meeting we aligned with CEL team on starting track optimization from FIT booked position and only develop FIT tracks to be in harmony with the data used to train the demand model. I will share the final data processing nb / query for the team to check and validate.

**DUAL: Analyze and document root causes of track optimization issues**

This week - I treated some causes of failure - specially for very close-in sailings where the model is reading oversold cabin status (-ve remaining capacity) instead of recording a failure in this case for track opt, set all future track builds to zero.

Noticed some issued with the 2nd stage smoothing MILP algorithm - over smooths after wave dips, treated the model not to smooth the optimal track ask during or after wave,

This process will continue until the model is pushed to prd and after - as part of the monitoring.

**DUAL | Track ****Opt**** | Dynamic-based Price Caps code development + results EDA**

Applied the same logic to CEL data this week - done some EDAs but set to present the results to the CEL team when Anastasia is back.

Evan M.

RCI & CEL Revenue Mgmt: Demand Model

Investigated and improved model signal quality. Plan to go live within 1-2 weeks.

**Value ****add****: Model signal is more grounded in structural demand features, reducing feedback loop risk**

Improved accuracy and signal quality

Analyzed feature contributions to identify areas where the model leaned on booking history rather than price and demand context

Path forward defined to adjust feature store logic so prior observations inform without dominating

Elasticity curves look cleaner with current feature configuration

Worked with Lamis for curve evaluation

Improved visualization and diagnostics for ongoing model review

**Value ****add****: Better front end for user acceptance and evaluation**

Built segment-level breakdowns by ship, category, WTS bucket, and sail month

Added calibration curves, error CDF, and bias-by-WTS charts to detect systematic over or under-forecasting

Styled metric comparison tables established a repeatable format for Updated vs Prior review

Worked with Lance on KPIs and effective metrics

Will be scheduling a working session with additional members on best practices for front end design and deployment

Formalized model output as a deployable class

**Value ****add****: Deployment workflows aligned and prepared**

Refactored notebook logic into a Python class with train and predict instances

Removes dependency on notebook execution order and enables clean integration into scheduled jobs

Finalized CI / CD with Eswar and built workflows for ensured continuity

Mirielle T

Contact Center

**Part 2 — **Advanced App Functionality: “Run Your Own FTE”: I**ntegration of the 30-minute mode.****
Why we are building the 30-minute version****
**The 30-minute model was initially requested by the North America team to address specific planning needs. However, it is important to note that the existing 1-hour model remains a strong and valuable baseline for most use cases.
The current simulator operates at a one-hour resolution, calculating the number of agents needed for each full clock hour (9:00–10:00, 10:00–11:00, etc.). This level of aggregation is efficient and well-suited for many lines of business, especially in stable or predictable operating environments.
That said, call volumes do not always distribute evenly within an hour. For example, a spike at 9:30 (after a promotional email) may be averaged with a quieter period at 9:00. In these cases, the hourly view can:

Underestimate short peak periods

Overestimate quieter intervals

These effects can lead to less precise staffing decisions, particularly in more dynamic environments.
The 30-minute version complements — rather than replaces — the 1-hour model. By working with half-hour intervals (9:00–9:30, 9:30–10:00, etc.), it provides finer visibility into intra-hour patterns. This can be especially valuable:

For LOBs with highly variable demand

During peak or high-season periods

When short-term spikes significantly impact service levels

In summary, the **1-hour model remains appropriate for most planning needs**, while the **30-minute model offers additional precision where demand variability requires it**.

**How we are introducing it****
**Rather than building a separate tool, the design introduces a **single granularity toggle** in the simulator header:
**Granularity: 1h | 30mn****
**The planner selects the granularity once, and all screens adapt accordingly.
At this stage:

The **Erlang A calculation logic has been prepared for 30-minute inputs**

The **data pipeline and supporting functions are being structured to support this mode**

Full integration into the user workflow is **planned for the next phase**

**Work prepared to support the 30-minute version****
**The preparation work has been structured across key components of the app:

**Summary — May 28, 2026****
**This week focused on preparing the **30-minute (30mn) version of the FTE simulator**, a key enhancement to improve staffing accuracy. The current 1-hour model averages demand within each hour, which can miss intra-hour peaks (e.g., spikes at 9:30). The 30-minute version will capture these variations, leading to more precise staffing decisions.
Work completed this week defined how the 30-minute mode will integrate into the existing tool:

Designed a **granularity toggle (1h | 30mn)**

Prepared updates across all components (schedule, call distribution, validation rules, model, and comparison)

Aligned data structures and logic to support 48 time slots per day instead of 24

**Current status**

The **1-hour version remains the only active production mode**

The **30-minute version is in design and preparation phase**

Core logic, structure, and user experience have been defined

**Development, testing, and integration are the next steps**

Mert

Deployment

Met with deployment teams and fully aligned on developing within a common GitHub org (RCG Alpha). Agreed on a standardized architecture and a joint deployment web app for both Brand and Revenue Planning deployment teams.

Mert

New Build

Added vision model parsing for the Newbuild AI Observatory and deployed the employee onboarding data source as a vector database.

Mert:
MIAP
Met with the new VP of Marine Strategy, Clayton van Welter, together with AI Ambassadors Captain Henrik and Patrick, and introduced MIAP solutions.
Received an urgent request from Clayton van Welter to help optimize the GMO Strategic Plan, which includes over 1,200 capital projects over three years. Developed an optimization model that automatically selects capital projects based on drydock dependencies, budget constraints, and risk score (Impact × Likelihood).
Completed productionization of the Polaris App for the port and berth database creation tool developed by Captain Henrik (vibe-coded by him on the MIAP App), resolving all bugs and vulnerabilities.
Met with the Maritime Safety team regarding their request for Sea Events (Marine Technical Incidents) KPI automation, where a KPI score will be assigned to events based on descriptions and KPI definitions using GenAI.
Was introduced to a Second Engineer hired for data tag mapping over the next four months. He will go onboard several ships to support the mapping process. Agreed to sail onboard Allure together on his first day and return from Nassau.
Continued discussions on Project TIDE for claims management with IBP and Risk Management teams. The IBP team is insisting on using sensitive fields (e.g., age, gender, race). This needs urgent review by the ethics team so IBP can be clearly advised not to use discriminatory features. Concerning.

Ram
MIAP
Successfully loaded navigation data from Eniram Modbus and Eniram Inclinometer sources into production.
Separated protocol-based workflows, reducing overall load time by approximately 40 minutes.
Collected ship-specific tags from Wärtsilä, created the required configuration file, and deployed it to the QA REST API environment.

Will
MIAP
On the feature/charge_air_cooler branch, completed EDA and a modeling proof of concept for detecting charge air cooler fouling on the Wärtsilä 46F fleet.
Established a first-principles thermodynamic model calibrated with factory test data, validated against IoT sensor data, and benchmarked multiple ML approaches (including a physics + ML hybrid) to predict fouling degradation.
Identified that engines 1 and 3 are a different variant (W16V46F), requiring engine-specific reference conditions—now handled automatically.
Organized the codebase into three notebooks (data exploration, thermodynamic model, ML POC) with a shared Python module, ready for production pipeline development.

Reza:
MIAP

Tested and validated a new approach for dynamic modeling in the oil fuel burner area by incorporating targeted moving average (TMA), gate correction, and feature adjustments in the classification step of a two-phase approach.
Deployed the final pipeline integrating TMA into power plant models for Steam Gas Turbines (STG) and Specific Fuel Oil Consumption (SFOC), with the following improvements:
STG Power: Improved performance for 13/13 ships (100%). Mean WAPE reduced from 34.09 to 28.99 (Δ −5.10, ~15% improvement).
SFOC: Improved 177/180 pairs (98%). Mean SMAPE reduced from 1.98 to 1.68 (Δ −0.30, ~15% improvement).
Resolved a workflow error for ship AX in the HVAC area.
Fixed workflow issues in the hotel HVAC area caused by a residual boosting library version mismatch.
Continued maintaining energy models and anomaly detection systems in the service power area.
Participated in two rounds of interviews for a Senior Data Scientist contractor role.

Arya:
MIAP
Improved the overall look and feel of the MIAP AI agent terminal with Pixel Agents.
Worked on adding safety data as an index and data source to dev-alpha-ai-search (production coming next), currently addressing permission issues with the platform team.
Worked on SORA bugs.
Fixed Fleet Tracking bugs.

Eddie B.

CEL Rev mgmt.

We have recommendations up until time of sailing. BUT they are automatically paused within 12 weeks (VERY arbitrary and I hate it). I've been fighting to change that for a long time. So now we are making close-in pricing recommendations for analysts, but done thru promotions (its a manual activity due to BRMS).

- Goldner requested more on it yesterday so I am going to give an estimate for the next PRE meeting. Coordinating with the Short Caribbean teams in particular to see how aggressive and close they are comfortable with getting. the big issue on the RCI side was the presence of these promotions. VPS reads the price but we would be changing a different Price_01_amt. I've been sending them pause files that close the gap from 12 WTS to 8 WTS for over 6 months. the feedback I got was that the recs look fine but the promotions are a stopper. Anastasia and team aren't comfortable moving closer in yet because of the reliance of track that uses retentions and etc. Figured when we get them on price optimization / new demand forecast and let the dust settle they'll gain some comfort with close in accuracy. plus its admittedly not as big a concern to move close in on CEL because of the difference in booking curve RCI the opportunity is significantly larger.

For both brands we are building out an addition to the PRE that takes into account Promotions. While we currently look at LAF prices after promotions are applied, we don't have a good way of distinguishing which promotions and how much is discounted. The biggest promotion that shows up are Replacement Value Promotions, typically done closer to sailing.

For both brands, we are building out a process that uses the PRE to run on all eligible sailings for Replacement Value (Exciting Deals for CEL, Last Minute Cruises for RCI) to generate a LAF price recommendation through PRE. The layer built on top of it uses Cabin Availability, WTS benchmarks of strong SPI sailings, current Promotion Status and recent performance to give a recommendation on whether or not it should stay on Replacement Value Promotion.

Because we cannot execute the promotion (it lives in BRMS which we do NOT have a way of writing to in the same way we update prevailing prices) there is a requirement to provide the analysts a recommendation they can send to the channels to have the promotion live.

CEL's recommendations are currently delivered to the team. Pending feedback from the business team but strategy team signed off!

RCI we are building similar framework, but also adding in an additional layer that will allow for PRE to run on closer in sailings per the team's request.

RCI Short Caribbean in particular has been requested to prioritize moving the PRE closer in to capture the booking window.

Ayon G.

Win-on-Waste

No major updates from mem except working through a lot of tickets (for finishing Win-on-Waste in June) and cleaning up poor code from Luis Vargas (contractor that went AWOL and has been terminated). I am training Abhishk for maintenance, optimistic he will pick up Now for WoW we won’t need additional new resource but celebrity we will need to be careful In selection

David W and Kevin D.

PCP Pricing Automation

Huge interest in the strategic direction of the CAR by Gang W. and Rafa T. Team shared the financial view of which only 4% has been actually spent, but the team can account for most of the future spend. Currently, David W. is projecting CAR based on forecasted burn rates can fund work well into next year (Feb. – May)

Onboard Revenue Team Leadership is really worked on notifications orchestration on the App side, since the Pre-Cruise Targeted Offers pilot required manual intervention by Rachel’s team under Yassine using ONESIGNAL. There are discussions with E-Commerce (Samantha) if we can migrate notifications into Salesforce Cloud, like the E-Commerce team uses for Ticket Targeted Offers.

We will be hiring an additional data scientist contractor and hire an additional resource for Andrew Smith’s team to accelerate Clickstream data integration into pricing automation. HotelOps will also start charging to the CAR.

David W.

SSC PROPEL

The SSC PROPEL sCAR has been accepted by Capital Planning with some revisions. Will go out for review today.

Javier, Santiago

CEL PROPEL (Javier & Santiago)

Measurements: (Javier)

Deployed the new measurements granular job to production to run daily.

Added new notebooks and orchestration logic for sailing-level measurement processing.

Added revenue validations

Enhancements:

XC Casino Offers: Deployed fix to dev and monitored for missing casino offers. (Santiago)

Production Issues:

Duplicate offers: (Santiago)

Scheduling table: Successfully deployed updates to the scheduling table logic to avoid duplicate runs, followed by thorough performance monitoring.

Job Scheduler Fixes: Identified and patched a bug that allows duplicate offers during the scheduling job execution.

Offer loss:

The IDs are changed on every ingestion, instead the IDs will have more permanence by using a hash rather than always being a new number. (Javier)

Offers to wrong guests: traced issue back to data freshness issue, raised with Data Engineering since the DE table is still showing the wrong guests compared to fidelio. (Santiago)

Missing PDF for specific decks: due to intermittent sharepoint upload failure. Upload retries are in dev now to avoid this. Also documented what to do for the offshore team. (Javier)

Glen-Erik C.

PCP Pricing Automation

Targeted Offers Hub UI:

Migrated from SQLite (dev database) to PostgreSQL (production level cloud data base)

Deployed targeted offers hub app to Azure in QA at . However, IT still needs to complete the ticket to add the URL to the DNS so it isn't easily accessible by anyone yet (must add a DNS entry to the laptop manually to see it).

Measurements:

Provided feedback and guidance on measurements.

New Schema:

Tested new schema in prod but notifications didn't make it to iOS or android. Retesting and troubleshooting with Digital.

Eswar

RCI & CEL: Revenue management

RMA: (Eswar & Javier)

Feature store: (Eswar)

Validated 5 tables provided by DE team and compared to the existing prd tables and provided the results.

Demand Forecast: Bundle Deployments setup  Eswar)

Web scrapping project: currently looking at spark compute optimizations to reduce run time as well as DBUs, necessary before moving to production. (Eswar)

TAP Refactoring: (Javier)

Centralized duplicated logic & functions into reusable framework modules including schema enforcements, training and IO logic, and transformation code.

~3,700 lines of duplicated code removed.

~50 files refactored.

Other Projects:

Axiom: Asset Bundle Deployment setup for axiom meta data gen project in git (Eswar)

Job Description Agent: Fixed agent response delay due to model. (Glen-Erik)
