**Bao**

**E-Commerce:**
**Booking Propensity Model: Weekly Accomplishments**

**CEL May 2025 Historical Scoring**: Configured and executed the full historical scoring pipeline for CEL May 2025. Resolved 6 pipeline bugs across training and scoring. Pipeline ran end to end successfully.

**Clickstream Feature Research (v6)**: Completed exploratory data analysis across 23 candidate features spanning 8 novel behavioral dimensions. Narrowed the shortlist to 5 consumer-level features with an estimated 3 to 4% AUC improvement: Implementation plan is documented and ready to execute with no new data ingestion required.

**Epsilon Feature Sunset Validation**: Epsilon is sunsetting a portion of their demographic attribute catalog. Completed a cross-reference of all Epsilon features currently used in the propensity model against Epsilon's planned sunset list to identify any at-risk inputs and assess potential model impact.

**CEL March 2026 PCP Model Training**: Trained and registered 10 Pre-Cruise Purchase models across five product categories (beverages, dining, internet, shore excursions, spa) for the March 2026 historical scoring run. Resolved 5 pipeline bugs. Scoring pipeline is configured and ready to execute in Databricks.

**CEL Campaign Validation Support**: Guided marketing stakeholders on which historical scoring tables contain the PHML propensity segments needed to evaluate the Targeted Offers campaign performance. Documented the segment logic and relevant model variants.

**Carlos A.**

**E-Commerce:**

Analysis of Silversea data availability and Estimates Roadmap migration-develop of they CLTV, Booking Propensity, Lead Scoring, and Lead recapture models.

Data source tables are available except by GCP, which Kate confirmed they are working on it. Also not sure about refresh rate, some of them seems to be updated only once.

Didn't find any Jacala code, maybe its in an environment I don't have access to . They should provide inference code (feature engineering for prediction step and models weights).

The roadmap/duration depends in what we start with, and where we  want to go. 
It seems there are two layers:
**Layer 1-** Jacala handoff, where we get the models running in databricks but still depending on Jacalas weight and GCP data. (I estimates 7 weeks)
**Layer 2-** We build our own models. (I estimates 12 weeks assuming we have a good understanding of the data from jacala docs and inference code)

**Loyalty – Carlos:**

Build new loyalty simulator not longer based on spend as before, -this is different than the guest-sailing simulator we have been working on and which is the base for the loyalty simulator

Fix and analysis of 6 test guest-sailings scenarios generated

Improve documentation

**Carlos A.**

**Win on Waste:**

We’re meeting next week with Michael and Tim Waren on behalf of Linkin to explore potential approaches for applying computer vision to onboard food waste tracking. The discussion stems from Linkin’s interest in leveraging FPMS iPads to automate portion measurement—either by counting leftover food items or replacing manual weighing entirely. A vendor solution (SnapAI) has also entered the conversation, offering the ability to identify food items and estimate weight directly from a photo, prompting questions about whether similar capabilities could be developed internally using existing hardware.

From our side, we see a viable path to replicate and potentially enhance these capabilities by combining modern computer vision techniques (object detection, segmentation, and depth estimation) with regression-based models to infer weight. Carlos Andarcio is actively evaluating how this could be implemented within RCG—including feasibility, cost, and timeline—and we’ll bring a structured proposal into the discussion. The goal of the session will be to align on operational practicality (e.g., snapshots vs. weighing), compare vendor vs. in-house approaches, and define a clear path forward.

Research on algorithms for food weight estimation and Develop POC app implementing results found

Carlos A.

**Loyalty – Carlos:**

Build new loyalty simulator not longer based on spend as before, -this is different than the guest-sailing simulator we have been working on and which is the base for the loyalty simulator

Fix and analysis of 6 test guest-sailings scenarios generated

Improve documentation

Mirielle T
**Contact Center:** Security Vulnerability Fixes & Dependency Updates

**Summary**

Security findings were reviewed in collaboration with Brendan to clarify update requirements. It was confirmed that dependency updates are mandated by company security policy, regardless of the Azure Container Apps hosting environment. All identified Critical and High vulnerabilities have been addressed through dependency updates, and application stability is currently being validated to ensure no breaking changes.

**Description**

This work addresses Critical and High security vulnerabilities flagged by Snyk across application dependencies. While Azure Container Apps was initially expected to abstract package management concerns, updates are required to comply with internal security standards.

**Changes Implemented**

Updated requirements.txt with patched versions for all dependencies affected by Critical/High CVEs (e.g., pillow, cryptography, pyasn1, pyjwt, fonttools, urllib3, requests, azure-core, azure-identity, numpy)

Added explicit version pinning for transitive dependencies to prevent installation of vulnerable versions

Removed duplicate dependency entries and cleaned up comments

Removed obsolete script (run_local.ps1)

Updated README.md documentation

**Testing & Validation**

Verified all dependencies install successfully without conflicts

Confirmed application runs correctly and all pages load without errors

No breaking changes observed; updated packages remain backward compatible with the existing codebase

**Craft the TOR — Workforce Planning Workstreams**

The Terms of Reference (TOR) defining two key Workforce Planning initiatives:

**Workstream 1: Office Shrinkage Data Model**
Build a Databricks pipeline to produce automated, reliable shrinkage metrics (in-office and out-of-office), enabling data-driven inputs into the Workforce Planning Simulator.

**Workstream 2: FTE Tracking System (Discovery Phase)**
Define a long-term solution to track **Planned vs. Actual FTE**, moving away from fragmented Excel-based processes toward a centralized, consistent, and sustainable data framework.

**Workforce Planning — North America (Royal) / Advanced App Functionality: “Run Your Own FTE”**
**What was tested:** Every screen of the workforce planning simulator, end to end
**Goal:** Walking through the tool as a real user and reviewing the code underneath

**Part 1 — The Seven Screens: What We Checked and What We Fixed**

**Screen 1 — Home (the starting point)**

**What we**** checked:**
We confirmed that the home screen gives a first-time user a clear picture of where to start and how far along they are. A checklist at the top tracks which of the four inputs (schedule, assumptions, call distribution, joined view) have been saved in the current session, so the planner always knows their next step.

**What we fixed:**
The home screen previously displayed a message stating that the 30-minute version of the tool "was not loaded yet." Since the 30-minute version has now been developed, this message was removed to avoid confusion.

**Screen 2 — Office Hours (the weekly schedule)**

**What we checked:**
We confirmed that the planner can set which hours each line of business (LOB) is open, day by day, hour by hour. We checked that:

The screen shows the standard schedule on the left and the planner's edits on the right, side by side

A counter tells the planner how many slots they changed vs the standard

Before clicking Save, the screen shows exactly which table in the data warehouse will be written to — no surprises

Previously saved versions are listed in plain language (DRAFT · saved May 2026) rather than long technical table names

**What we fixed:**
The very first time a planner tried to save a schedule for a brand-new line of business, the save failed because the history log table did not yet exist. We fixed this so the tool creates the log automatically on first use — the planner now sees a clean success message.

**Screen 3 — Input Assumptions (the operating parameters)**

**What we checked:**
We confirmed that the sliders for average handle time, abandon rate, service level target, patience time, answer speed, and shrinkage:

Start at the **real 3-month average** from the brand’s own data

Show a reference column next to each slider so the planner can see actual historical values while adjusting

Allow a wide enough range to test extreme scenarios

**What we fixed:**

**Screen 4 — Hourly Proportion (splitting daily calls)**

**What we checked:**
We confirmed that the tool correctly distributes daily call volumes across time intervals using historical patterns. We checked:

Heatmaps for both proportions and resulting call volumes render correctly

Save messages clearly indicate what was written

**What we fixed:**

**Screen 5 — FTE Inputs / Joined View (merging everything together)**

**What we checked:**
This is the assembly step — merging schedule, assumptions, and call distribution into one dataset. We checked:

Source pickers use readable labels

A health-check confirms row count and date range

Diagnostics identify any missing or inconsistent inputs

Each save creates both an active table and an audit log

**What we fixed:**

**Screen 6 — Erlang ****A**** Engine (running the staffing model)**

**What we**** checked:**
We verified the full execution flow:

Step-by-step guidance: select inputs → define save settings → run → view results

Pre-run summary confirms scope (row count, dates)

Results available by day, week, and month

Each view supports CSV download

**Key improvement — Auto-save:**
Previously, results had to be manually saved after running the model (which could take up to an hour, especially for finer time intervals such as the upcoming 30-minute version). If a session expired, results were lost.

Now, planners **define save settings before running**, and results are **automatically saved** upon completion. A confirmation banner is shown, and a re-save option is available if needed.

**Gap identified (not yet fixed):**
The audit log table naming does not include the line of business. While LOB is visible inside the table, it is not reflected in the table name.

**Screen 7 — Compare (side-by-side experiment comparison)**

**What we checked:**
This screen is read-only to prevent accidental changes. We confirmed:

Filtering by brand, LOB, staffing target, grain, and time resolution

Multiple scenarios can be compared side by side

Summary metrics (total, average, peak FTE) are displayed

Charts update dynamically

% change vs baseline is available

Export includes all scenarios in one file with identifiers

**What we fixed:**

**Executive Summary — End-to-End Testing (FTE Simulator)**

The workforce planning simulator was tested end to end across all seven screens. The objective was to confirm that a planner can independently produce a complete FTE forecast, from inputs to final results.

Overall, the simulator is **functionally complete and stable for the 1-hour version**, with strong improvements in usability, reliability, and traceability.

**Key Outcomes**

All seven screens were validated from input setup through final comparison

Usability improved (clear workflow, better messaging, progress tracking)

Data reliability strengthened (fallback logic, correct table loading, consistent naming)

Full traceability ensured via versioning and audit logs

Auto-save implemented to prevent loss of results

**Next Step: 30-Minute (30mn) Version**

The 30-minute version is **not yet available in the tool**

Supporting data structures and functions will be **developed, tested, and integrated in the next step**

**Caleb S.**

**Consumer Lifetime Value (CLV)****:**

Completed

Conducted a comprehensive audit of all Customer360 tables to identify relevant attributes for the CLV final table. Created logic for consumer-level aggregate features including total interaction counts and cumulative external spend.

Validated the newly refreshed VCAP staging tables curated for CLV, with detailed checks across channel mix, passenger cruise days, pax counts, and net ticket revenue. Evaluating whether this staging logic can be integrated directly into our pipeline to eliminate the manual refresh dependency on revenue planning.

In Progress

Collaborating with the data solutions team to verify C360 attributes are correctly incorporated into the POC.

Meeting with Kiana and Vanessa (5/22) to review progress on open items: specifically tracing cost allocation logic and validating table sourcing for the current POC.

Caleb

**CLTV: ****Sailing Environment**** Model****:**

Completed

Met with Neila to align on overall project structure and initial milestones.

Set up a new Azure DevOps repo to centralize previously completed work.

Compiled the full artifact set from CS's demand model — data sources, queries, ETL pipeline, EDA, modeling, testing, and validations — and produced a comprehensive summary and inventory document.

In Progress

Working with Neila and Gaby to define the project plan, including scoping decisions around level of granularity (e.g., cabin class vs. category class) and identifying which exploratory threads warrant investment versus those with diminishing returns.

Camila

**IBP ****Supply Chain: **

Finance Tool Pilot:

Multi Ship Parameterisation: all downstream notebooks will use pilot ships parameter to reduce code changes in the future. Now currently hosting Beyond and Summit for pilot ships

Ongoing sailings freeze predictions as well as recently completed sailings so that prediction doesn't change/update during the sailing

Seasonality Guardrail following STLY format

Using historical predictions to adjust current and future predictions based on STLY but am thinking of adding an additional layer of actuals.

Uniform & Medical & CocoCay:

Reported on data bug where ship codes where duplicated due to an additional space which caused misaligned joins and under counted crew counts

Edited ETL for Uniform and Medical to automatically trim ship codes until the issue gets fixed

Reported on blank brands where it's only affecting SSC brand. Waiting on this to be fixed

Automated backtested data pickup for all three models to grab all available years that the model has trained on. Was originally filtering out 2026 data since a full year has not completed yet.

Royal Beach Club:

Borrow from CocoCay: CocoCay's shore excursion program is more mature than RBC. Its guest take-rates (ship's PAX vs shore excursion guests) and seasonal patterns are used as a reference baseline for RBC behavior. CocoCay launch ramp is borrowed to model how demand grows week after week.

PCP and onboard revenue guest signals to estimate how many guests are expected to visit RBC. Don't think the guest revenue is mature enough to build a guest forecast model so I am applying a baseline from actual NAS guest revenue + CocoCay beach club + hideaway to apply for future data to get an estimated forecast of guests.

Still in development:

New Destinations Transfers: Santorini destination has no real consumption history but I want to begin thinking of a way to have a forecast based on historical voyages in that region:

Mediterranean ships: voyages whose itineraries include Greek island ports (ATH, JTR, JMK, etc.) tell us how many passengers are sailing there each week

Live PCP bookings: actual Santorini PCP, even if sparse, give a real take-rate signal

SSC Finance Tool:

Validated that all of Steps 1-3 follow RCI/CCI format with latest logic applied of frozen predictions and certain filters.

I do want to begin thinking of a way to get historical predictions from the latest enhanced model from Ben to begin developing all the additional reporting done for RCI/CCI. Would like to get ahead if I can.

Ben F.

**Supply Chain:**

**Headline**

Four workstreams shipped in parallel:

- New Silversea demand-model productionized and stakeholder documentation delivered.

- The new model reduces MdAPE error on the back-tested month from 33% in the old model to 25% in the new model.

- The new model after engineering 284 candidate features with Agentic AI, used a cost weighted approach using Recursive Feature Elimination with Cross Validation on 7 time periods. The final model selected the features that were in 5 or more of the 7 time periods. In total there were 117 features selected and forecasted load factor is the dominant feature in the model for many of the Main Store categories. More detail is contained in the documentation below.

- Order-creation data foundation migration after validating the new master load schedule table with catalyst voyage numbers

- Delivered a production Daily/Weekly Digest Databricks agent built end-to-end and implemented providing team-members updates each day at 8am and a weekly update sent Thursday at 3pm to provide clarity on the Pull Requests each team-member makes, what code changed, how the code changes work and why it was done with notifications sent in Microsoft Teams.

- Delivered ad-hoc analysis on historical consumption of Beyond when the ship was at CocoCay and how future forecasts are trending on CocoCay port days to handle concerns from on-board crew about how the model will respond when the ship is at CocoCay.

**1. SSC Demand Model ****Documentation**

**2. Order-Creatio****n Pipeline**

- Validated the new Master Load Schedule table with Catalyst Voyage numbers contains all voyages in the business used Master Load Schedule excel file on Homeport.

- Refactored Order-Creation code resulting in multiple hour reduction in compute time, and significantly reducing size of notebook for easier readability.

**3. Daily / Weekly Digest Agent — Zero to Production in One Week**

**Stood up automated GitHub-activity digest delivered to Teams via Power Automate****: **Fetches commits + PRs, summarizes per-item with databricks-claude-sonnet-4-6, delivers Adaptive Cards in Microsoft Teams chat notification.

**Production hardening shipped sequentially:** cluster switch to cost-controlled compute, run-as-user fix, full-summary mode (no clipping), 22 KB byte-budget chunking for oversized payloads, @-mentions attached only to chunk-1 cards (one notification per run), 08:00 ET dev schedule.

**Weekly roll-up added****:** For assistance in weekly status reporting.

**4. ****Perfect Day at Coco Cay Analysis for Beyond Pilot**

**Stakeholder PowerPoint: **Showed actual consumption for Food at CocoCay port days on Beyond voyages visiting CocoCay and compared to future CocoCay port day forecasts to support that our Forecasts are not under forecasting when the ship is at CocoCay on upcoming voyages as shipboard staff voiced that concern. Plot was shown to our working group and it wasn’t a concern. Sidney has other operational concerns but these concerns Evan is handling and is outside the scope of our work.

**Outlook**

- **Marine Consumables Demand Modeling: **Model improvements in process to reduce model error.

- **Code Refactoring and Validation: **In process of reviewing refactored Finance Tool code to confirm parity with production monolith code. Supply Model code refactoring also in process with validation pending.

**Nico T.**

**Supply Chain:**

**RCI/CCI HF&B Order Creation Dashboard MLS Discrepancies**

· In Progress · Highest

Completed:

Replaced dev_datascience.ibp_sso.master_load_schedule_source with qa_gold.ibp.rcg_master_load_schedule: Ben completed validation across voyage numbers and row-level values to ensure that voyages were retained across the table outputs.

Realigned validation approach with Ben (Thu 5/15): After speaking with Ben, refocused the validation to ensure all Voyage Numbers are preserved in the new table version. Outlined a new plan: create a copy of the Order Creation Notebook with the table swap and suffixed writes, add a ship_load_date > 2026-02-01 filter, run both versions in parallel, and compare distinct Voyage Numbers across each written table.

Voyage Number comparison results — low match rates (Mon 5/19): Ran the parallel comparison on ORDER_CREATION_DATA_UNAGGREGATED. Results were concerning:

VOYAGE_NO only: 72% match

VOYAGE_NO + SHIP_CODE (no filter): 43%

VOYAGE_NO + SHIP_CODE (≥ 2026-01-01): 12%

VOYAGE_NO + SHIP_CODE (≥ 2026-02-01): 0%

Root cause investigation — batch_id logic in Paolo's table (Tue 5/20): Determined that Paolo's qa_gold.ibp.rcg_master_load_schedule is simply pulling records from the latest batch_id of the prior table (prd_silver.shipfin.rcg_mls_out_t), which only captures the most recent load per voyage — not all loads. Traced a specific example (Ship: AT, Voyage: 117): present in the PRIOR notebook version, not present in the NEW version, but found in the Excel file under LEGACY VOY #. Sent detailed findings to Paolo with the question of whether the batch_id filtering logic needs to be extended.

Excel cross-reference check (Tue 5/20): Outlined the next diagnostic: verify whether the missing ship_code/voyage_no pairs exist in Paolo's Excel file. If yes → query logic issue; if no → Paolo's table validation was incomplete.

Ongoing:

Awaiting Paolo's clarification: Need Paolo's response on the batch_id filtering logic before continuing. The current approach may require extending the logic to consider the latest batch_id per partition key/grain rather than a global latest batch_id.

**SSC Uniforms Model — Combinatorial Gender/Generation Ratios**

· In Progress

Completed:

Completed Guardrails code run-through (Tue 5/20): Ran through the full Guardrails code and is now ready to proceed with the crew adjustments in the next step of the pipeline.

Ongoing:

Crew adjustments: Moving to the crew adjustment step now that the Guardrails notebook has been executed.

AI Prediction $ / PCDs & Guest Counts Table

· Done ✅

Completed:

PySpark conversion completed: Converted the notebook code from pandas/SQL to PySpark and validated the new outputs against the original outputs. Results matched.

Ayon G.

Win-on-Waste

Hi Dave GM, I have no updates for WOW this week. I set up a meeting with you for sync and also WOW presentation (that I shared with u in this chat) on 5/27 from 9-30 to 10 (that was the only timeslot I found in your calendar available.

Working on deliveries from last week. Preparing for a large WoW presentation summarizing the last year of work. This presentation tells the story of how a cruise fleet transitioned from manual, intuition-based food production — which led to **$1.28M in annual food and beverage losses** — to an AI- and data-backed system called FPMS. The platform uses a distributed, per-entity modeling framework spanning **29 ships**, combining clustering, classification, regression, and optimization across thousands of menu-item variations to generate accurate production forecasts for chefs.

The results have been significant: over **$110M in cumulative food waste savings**, **$5.9M saved in April 2026 alone**, and **35M+ pounds of food saved** since the program launched during return-to-service in 2021. Forecast accuracy is strong, with **306 out of 401 items within 15% MAPE**. The system analyzes over **1 billion rows of data daily** across **50K AI models**, and the team is now expanding into a beverage POC to bring FPMS capabilities to bars.

**Erick A., Cristian V., ****Danusio**** G. **

**MyCruise**** Recommender**

*Personalized post-booking recommendations (excursions, dining, spa) powering the **ForYou** surface in the app.*

**Infrastructure / Postgres & API *****(Cristian V.)***

**Redirect Recommendations Traffic to New Postgres Prod Instance** *(Cristian V.)*: Calendar recommendations endpoint deployed to prod this week; a schema-mismatch bug (dropped features from an aggressive rebase) was caught and fixed. Engineering is working to integrate the prod endpoint into web and app.

**Guest Segmentation / Clustering Selection *****(******Danusio****** G.)***

**Determine Minimum Cluster Count** *(**Danusio** G.)*: Last week’s homogeneity-driven scoring jumped the optimal count to 89 clusters. This week’s weight-tuning results confirm **fewer clusters (<20) outperform the higher counts (~100)** — aligning with Erick’s 10–15 target range. Next step: validate the final cluster selection with Cristian using the full recommender back testing as the target.

**ETL Infrastructure *****(Osvaldo V.)***

**Investigate Failing ****GraphQL**** ****ShoreX**** Product Detail Job** *(Osvaldo V.)*: **HTTP 423 — Akamai WAF authentication error** blocking all product categories (ShoreX, dining, spa). Erick is creating a Platform team ticket to resolve the firewall issue. Once access is restored, Phase 2 expands to other product categories with parallel/async calls.

Erick A., Rodrigo B., David M., Danusio G.

**Project Axiom — Voice 360**

*Insight extraction from unstructured customer feedback (Medallia, Guest Logs, Qualtrics) via LLM pipelines — feeds emails, dashboards, **drivers** analysis, and chat.*

**Email Reports**

**Guest Strategy & Analytics weekly report** *(Rodrigo B.)*

**Target-value mismatch** *(Rodrigo B.)*: Maria flagged missing target values for certain sailings. Root cause: the targets table’s return date mismatches actual return dates for interporting itineraries (passengers embark/disembark mid-cruise). Fix: join on sailing + embark_date instead of return date alone. Rodrigo confirming with Maria whether the affected sailings are indeed interporting.

**Metrics section added to guest email** *(Rodrigo B.)*: Last week the layout was finalized; this week Maria requested an additional metrics section for Royal Santorini Beach Club in the guest strategy email. Rodrigo implemented it by copying the existing Santorini metrics table into the guest email format.

**Port Email** Rodrigo addressed all prior review comments: added a glossary (promoters, detractors, response counts), changed the ambiguous “number of responses” metric to “total number of comments,” included KPI tables for all shorex, and attached a QA file with raw comments. Shared cleanliness tracking with reviewers.

**IVR Survey Report** *(Rodrigo B.)*

**IVR Survey Report Draft** *(Rodrigo B.)*: Alper confirmed he’s happy with the week-over-week IVR analysis. IVR analysis refers to the post call surveys given to guests (i.e. Do you have 5 minutes to answer a few questions regarding your call? )

**Meta Data Framework**

**Asset Bundles — Databricks Tokens Blocker** *(David M.)*: Last week’s setup was complete end-to-end in develop, awaiting Eshwar’s Databricks tokens. This week: Eshwar committed to delivering the tokens but has not yet responded. David following up; Erick will escalate directly if no response by EOD Thursday. This remains the gating step before GitHub Actions / secrets-per-environment can proceed.

**Backfill Bullet Points using new ****medallia**** meta data generation pipeline** *(David M.)*: Last week’s batch processing started 2026-05-12 for Jan 2025 forward. Batch is running successfully with good quality. Plan: validate current Jan 2026 output, then extend backward to full Jan 2025 historical coverage.

**Guest Logs — Email Pipeline *****(David M.)***

**Replicate Reporting Topics Notebook for Guest Logs Email** *(David M., In Progress)*: New this week — David’s pipeline can now extract bullet points, people’s names, sentiment scores, places, and topic keywords from guest logs (same column structure as the Medallia bullet-points project). Input table has a known data issue, but Erick directed David to use the existing older table from January 1st onward as a de facto production source.

**Webapp — 3D Ship Model *****(Rodrigo B.)***

**Staircase Deck Layout** *(Rodrigo B., In Progress)*: Implemented a new staircase view mode — user can spread decks into a staircase arrangement, focus on a single deck, and return to stacked view. Also added: date filter redesign (dropdown with “since day” / “between dates” / “specific dates”), separation between data filters and visual controls, and navigation instructions overlay.

**Webapp — 3D Globe Visualization *****(Osvaldo V.)***

**Three.js Globe with Product Histograms** *(Osvaldo V., In Progress)*: Globe with AI product category histograms pinned to port locations is functional inside Databricks (displayHTML).

**Celebrity Operations Analysis *****(Osvaldo V.)***

**Xcel & Silhouette Operations Analysis** *(Osvaldo V., In Progress)*: Reusing the existing dry-dock LLM topic-extraction pipeline for Celebrity’s Xcel (Nov 2025 – Apr 2026) and Silhouette (Dec 2025 – Apr 2026) sailings.

**Erick A., ****Danusio**** G.**

**Project Axiom: Web**** Scraping**

*Cross-brand initiative to build a unified scraping platform serving Consumer Insights, Hotel Operations, Product, and **Social Media**. Phase 1 targets review/forum sources → Unity Catalog.*

**Phase 1 — Review & Forum Sources *****(******Danusio****** G.)***

**Scrape **** Reviews** *(**Danusio** G., In Progress)*: TamperMonkey script now working (required handling a click-to-render reviews panel). Python translation created but not yet fully tested.

**Scrape Cruise Critic Forums** *(**Danusio** G., In Progress)*: Stage 2 (content scrape) confirmed producing identical results in Python and JS. Stage 1 (link discovery/crawling) still pending in Python — that’s the remaining gap before end-to-end automation.

**Scrape Reddit Cruise Subreddits** *(**Danusio** G., In Progress)*: Python scraper working (unauthenticated) for search-by-query mode (scraper #2). Captures URL, title, score, comments, date/time. Scraper #1 (subreddit feed for historical backfill) not yet built. Architecture: scraper #2 runs daily for new posts; #1 is one-time; Reddit scraping is on-demand (not scheduled) due to rate-limit risk.

**Test Python/Selenium Translations** *(**Danusio** G.)*: Fixed a Mac-specific PATH issue (browser driver not in ENV). Both Python and JS now produce matching output. Cruise Critic results confirmed identical between TamperMonkey and Python.

**Create Unity Catalog Schema for Scraped Data** *(**Danusio** G., new)*: New task — create a persistent landing zone (data_science.scraping or similar) in Unity Catalog for review data. Reviews only (monthly cadence); forums remain ad-hoc.

**Project Concept Testing Lab**

*Agent-persona framework using LLM-driven synthetic respondents to A/B test ideas and concepts before committing to live tests. Built on **TinyTroupe** (Microsoft OSS).*

**Explore ****TinyTroupe** *(Osvaldo V.)*: Last week was blocked waiting on Hannah’s team to share code. This week: received repo access, cloned, and starting analysis. Plan: complement the existing app with TinyTroupe’s bulk-persona creation framework — not starting from scratch.

Erick A., Osvaldo V.

**Contact Center**

**Siren — Time-to-Topic Analysis *****(Osvaldo V.)***

**2024 Baseline Comparison Complete** *(Osvaldo V.)*: Last week’s replication CSV is now validated — columns match, values are similar to Erick’s reference. However, the dependency table is **empty for 2026**, blocking the 2026 rerun.

**Shorex GSO Safety Email *****(******Danusio****** G.)***

**Trust & Safety Report Differences** *(**Danusio** G., Completed)*: Last week Danusio pushed a quick fix and Eduardo asked for a written explanation of query divergences. This week: direct conversation with Eduardo confirmed results are **99% adherent** — the 1% difference comes from filtering out the 200-character long-text comment field. Task closed.

Neila B.

RCI Rev Mgmt:

**Plan: Regional Pricing-Power Signal (Bullish / Bearish)**

**What it answers:** A weekly read, per brand × region, on one question — *can we charge premium prices right now, or not?* Bullish means the market is absorbing premium rates; bearish means we can only fill by discounting.

**How it works:** We build it on metrics RM already uses. The Rate Build vs Volume Build decomposition is the core signal — Rate Build (rate rising) is pricing power; filling only through Volume Build at a falling rate is discounting. We aggregate that sailing-level signal into a fleet-level environment read, baselined against STLY, with currency impact separated out so FX swings don't get mistaken for real demand.

**The one methodology refinement:** For the pricing-power read specifically, we decompose Yield into cabin-level axes — cabin occupancy and NTR per cabin — rather than the standard LF × APD. The reason: occupancy mix (free T4, KSF) swings LF and APD dramatically while actual pricing power is unchanged, which produces false signals. The cabin split avoids that. Importantly, **it reconciles to the exact same Yield** — we're choosing a cleaner factorization of the metric, not changing the metric, so nothing in reporting moves.

**Serves both forecast windows:** Caleb and I have the same problem with different windows — he needs to project further out, I need closer in. We share one method (treating each sailing's booking trajectory as a sequence of states with an expected final yield) and tune the features and horizon per window. Close-in we have rich booking data and high confidence; far out we lean on external and structural signals with honestly lower confidence.

**Scope:** This is decision support — it tells RM where pricing power is strong or weak; it doesn't set prices. It's forward-looking by construction (booking pace), uses our own data plus the external context we want visible (e.g., search trends), and avoids lagged features and peer-company data.

**Next steps:** Compute golden three products (Europe, Short Caribbean, 7N Caribbean)→ build both decompositions and run the cabin-vs-passenger proof → validate against known events (e.g., Eastern Med geopolitical softness) → wire in the near-in forecast and scope the far-out scenario view with Caleb.

**My Progress This Week:**

**DUAL | GOLD | Sailing Environment - EDA + Historical Market Characterization (Europe Pilot)**

*Completed:* foundation extended to all three markets, both brands; peer baseline built and published; re-architected to run off foundational data (removing a basket-model dependency that dropped sailings); Caribbean validated (reconciliation, region mapping, season isolation); Royal casino reconciliation fix applied and validated.

*Remaining:* adopt the curated season taxonomy; align the pace source onto the per-sailing grain (completes Layer 2); re-validate on a hurricane-season group and complete the Europe region check; build the signal layer (Layer 4) — the per-brand × region bullish/bearish read with both horizons.

Michelle M.

**CEL ****Revenue Management: ****Category-Gapping 3.0**** Update**

Focus on a major breakthrough in the category gapping modeling approach, specifically simplifying the model architecture while maintaining accuracy. Michelle Manfrini demonstrated that instead of maintaining multiple models for different availability combinations, a single model with availability as a feature could replicate the same behavior through normalization. This insight reduced complexity significantly (from ~12 models down to ~3 by ship class), improved maintainability, and aligned with business expectations after validating that normalized outputs closely matched observed behavior. David Whitney strongly reinforced this as a high-quality outcome, emphasizing the importance of using data to influence stakeholder decisions and avoid unnecessary model proliferation.

A second key theme was improving model robustness through temporal awareness (i.e., incorporating “DART-like” behavior). David Whitney walked through how autoregressive features (e.g., prior gaps, shares, or recent errors) can approximate residual adjustment techniques without formally implementing DART. The discussion highlighted a practical approach: layering a lightweight post-model adjustment (e.g., moving average of recent errors) on top of base predictions to correct drift, rather than embedding full complexity into the core model or lookup table. This preserves the simplicity of the optimization framework while still capturing time-based dynamics. However, caution was emphasized—over-reliance on recent data could cause the model to “cheat” and degrade generalization if not carefully balanced.

The conversation also explored forward-looking architecture for multi-period optimization and forecasting. David Whitney introduced a more advanced “stacked” or hybrid modeling concept: combining (1) a base model trained on historical/structural features, (2) a temporal adjustment layer capturing recent trends/errors, and (3) a meta-model that determines how much to weight each component depending on the forecast horizon. This framework would allow the team to intelligently balance stable historical signals with short-term dynamics—particularly important as the business moves toward optimizing category gaps across multiple future time windows. This direction aligns with parallel efforts (e.g., demand forecasting work with Evan) and reflects a more scalable, enterprise-grade ML architecture.

**Key Takeaways:** The team successfully simplified the modeling approach (single-model strategy), validated that normalization preserves expected behavior, and established a clear path to incorporate temporal adjustments without overcomplicating the system. The group also aligned on a longer-term vision for multi-horizon optimization using hybrid modeling techniques. **Action Items:** Michelle Manfrini to finalize and productionize the single-model approach and begin prototyping temporal adjustments (moving-average error correction); Michelle Manfrini to start designing how future week-of-sale optimization will be structured using “bucketed” time windows; David Whitney to share supporting materials on time-series and forecasting approaches and socialize this win with leadership (e.g., Matt); Eddie Baffa to coordinate simplifying recurring meetings and align stakeholder touchpoints (including replacing the GenAI sync with a more relevant cadence).

Brand Breakout:
**RCI****: **Dependency on strategy team. Awaiting response.

**CEL****:**
- After building out validation framework last week, I compared outputs from all 12 models to ensure consistency across predictions in varying availability conditions.
- After this was completed and reviewed with business, team requested I combine all availability dependent models into a single framework to facilitate future validations and project updates. This required built out a single EBM including new features for availability, which I have completed.
- Team requested this approach since the original list of MVPs requested all model outputs match. This idea of a single model was originally pitched but business feedback revealed different behaviors were expected so there was a preference for separate models. After I built the validation framework, this revealed how complex it was to truly validate all scenarios where there are millions of combinations. I conducted an EDA with historical data revealing that tier shares where only 2 tiers are open match renormalized shares from when all tiers are open. This proved to the team that behavior is consistent across availabilities and a single model is feasible.
- I spoke with business and demonstrated how a single model performs in comparison to actual historical shares and initial feedback is positive, the outputs are aligning with expectations. Next step is to run optimization with new model and assess recommendations.
- Certain sailings have extreme desired shares (90%) for a single tier because of unbalanced capacity. This is resulting in the optimization selling the space mainly through GTYs because it cannot find a matching row in the lookup table where feasible gaps result in 90% of bookings coming in for a single tier.
- In this case, I am relaxing the share matching to allow for what is the max possible share in the table. For example, if the sailing desires a lower share of 90% but the lookup table only contains up to a 70% lower share, then this match should not be penalized because it is the closest feasible option. This has reduced the count of cases where gty share is > 50% by over half, significantly improving the outputs and not losing revenue through excessive GTY sales.

Lamis A.

RCI Revenue Management

Lamis centered on the behavior and validity of the track optimization model, particularly how it allocates demand across the booking window. The team observed that the optimization systematically shifts demand toward the Wave period (early booking window), asking for higher volume during that time and less later in the year. While this behavior aligns with pricing power dynamics, it raised concerns about whether the model is implicitly assuming sufficient demand capacity during Wave. Importantly, analysis showed the model is generally not constrained by upper or lower bounds, meaning the results are driven by pricing optimization rather than hard demand limits.

A core theme was the sensitivity of the model to assumptions—especially around “carrying capacity” and future demand environment. Bounds are currently derived from historical data (2024–2026), but there are gaps due to structural changes like increased ship capacity and atypical demand conditions in earlier years. The team discussed dropping 2024 data due to its non-representative nature and highlighted the need for more adaptive, tunable parameters that reflect current market conditions. Ultimately, there was strong alignment that optimization outputs are only as reliable as the assumptions behind them, particularly given uncertainty about future demand (e.g., whether next year’s Wave will be strong or weak).

The session also covered enhancements in pricing and model design. The team is moving away from static pricing constraints (±30%) toward dynamic caps that vary by ship class, booking window, and inventory position. Additional improvements include better handling of new deployments with limited historical data, smoothing logic corrections, and incorporating environment-aware adjustments. On delivery timelines, there is a slight delay in the demand model (pushed ~1 week), with broader uncertainty depending on how the new model performs in practice. The group aligned that track optimization will not be a “set-and-forget” solution but will require ongoing calibration, stakeholder input, and clear communication around assumptions driving decisions.

Jesse B.

SSC Revenue Mgmt

**Upper Suite EDA **– Completed some additional EDA before solidifying my algorithm for top-tier suite pricing.

**Top-tier pricing algorithm **- I further developed the top-tier suite algorithm. I met with Eddie for a strategy session, where we discussed the feasibility of said algorithm. Eddie had some constructive ideas for how to price the bottom top-tier suite, namely making the price a ratio of veranda or lower-tiered suite pricing.

I initiated a “stress test” of the top-tier suite algorithm. This stress test will involve using bootstrapping to test the feasibility of the algorithm compared to the current pricing system used by SSC Revenue teams. The stress test will also give us an idea of the necessary inputs to the algorithm, specifically, the top-tier LAF, the category gaps between top-tier suites, and the slope of price over booked position.

**SSC | PRE | AB Test | Expand Upper-level suite EDA**

**Status:** This ticket is complete as of 05/20/2026

**Deliverables:**

Examined differences in price paid between bought upper-level suites and up-bid upper-level suites

Examined floor and ceiling prices for bought upper-level suites

Examined relationships between price paid versus sailing area, cruise ship, cabin category level, etc.

See attached text file for comprehensive organization of EDA figures and stats.

**Delays:** None

**Potential future issue:** We will re-visit EDA if the need emerges.table_of_context.txt

**Formulate Upper-level suite Model**

**Status:** Ticket completed as of 05/20/2026

**Deliverables:**

·       Established a workable, repeatable pricing strategy for top-tier upper-level suites

·       Alignment achieved between Data Science and management on the pricing approach

**Delays:** None

**Potential future ****issue****:**

·       The algorithm will require ongoing review and scrutiny over time

**Update (May 20, 2026):**
Data Science met with management to review the top-tier suite pricing algorithm. Management supported using booking position to guide pricing but recommended incorporating voyage characteristics (e.g., veranda pricing ratios) to further refine decisions. This enhancement will be considered.

**Update (May 19, 2026):**
To meet prior conditions, Data Science developed a linear upward pricing algorithm tied to booking position. Upper-level suites are split into two tiers:

·       **Lower-tier suites:** Grouped across XTR categories behaving similarly to verandas; pricing adjusted relative to track

·       **Top-tier suites:** Limited (8–12 per ship) premium units priced above highest cabin categories; managed collectively based on booking position, with category price gaps preserved and no price reductions applied

**EDA Insight (May 19, 2026):**
The pricing model aims to increase SSC revenue by:

·       Encouraging early purchase of upper-level suites instead of bid upgrades

·       Preventing traditional high-end buyers from obtaining suites at lower prices

**Bootstrap-test upper-level suite model**

·       Met with Data Science management and discussed my plan for a bootstrapping test. Manger agreed.

Anneke

**SSC**** Rev ****Mgmt**

**PRE | Review & Action ****On**** Post-Promotional Price PRE with Stakeholders**

Work completed May 21, 2026

Met with Camille from Silversea team to review post-promotional price PRE and implications moving forward. Camille was pleased with the results and we started discussions on other enhancements.

Work completed May 21, 2026

I merged the changes reviewed during the stakeholder meeting such as changing the runtime of the Tuesday run to 1PM to allow users to have more time to review the pause file and removed unused fare codes.

**SSC PRE | Forecast EDA**

**SSC PRE | Incorporate SSC Promotions into PRE**

Work Completed May 15, 2026:

Moved version of PRE that is based on post-promotional price to production. Will be reviewing with stakeholders on May 20, 2026

Srileka

**CEL**** Rev ****Mgmt**** | Europe Actual Price Paid Analysis**

**Status**: This ticket is complete as of **5/19/2026**

**Deliverables**:

After delivering the initial analysis it became clear that the pricing and booking logic needed to be aligned with how Exciting Deals actually operate in production. Exciting Deals prices go live every Tuesday and run through Monday a 7-day window. The original logic was anchored to WTS meaning the prices and booking volumes captured could span across two different promo cycles. This week's work corrected that.

Pricing reference date changed to Tuesday (week_start_date). Since Exciting Deals prices activate on Tuesday, Tuesday's price is what the Product team uses to evaluate the trade-up gap. Tuesday’s GTY price and the lowest available Lead price, both pulled on Tuesday.

Booking window aligned to Tuesday–Monday. Bookings are now aggregated only for the 7-day period when promo prices are active. This ensures GTY vs Lead booking volumes and trade-up rates reflect actual customer behavior during the live promotion

Updated dataset and plots sent to Monica with the revised methodology. The analysis now fully aligns with the live promotion calendar. Monica confirmed the analysis was helpful for the Europe Product team it is being used to identify where trade-up is being suppressed by the GTY-only Exciting deal structure, which price points are driving demand, and where Lead promotions should be introduced to rebalance the GTY–Lead gap waiting for the feedback

**Potential future issue**: None

Kevin D.

PCP Pricing Automation

Dilution Analysis — RCI & CEL (EDA + Modeling Progress)
Completed a comprehensive analysis of cancel–rebook behavior across both brands using 12M+ transactions from Hybris, establishing a clear view of dilution drivers and actionable levers.
Key Insights
Dilution Levels
• RCI: ~19% of bookings involve cancel–rebook activity
• CEL: ~8%, significantly lower, driven by broader product tier structure
Primary Drivers
• Discounting is the strongest driver: deeper initial discounts materially increase likelihood of dilution
• Booking timing: earlier bookings (longer lead time) are more prone to cancel–rebook behavior
• Customer profile: higher loyalty guests show materially higher dilution rates
• Channel mix: Travel Agent bookings have the highest dilution; direct channels perform better
• Product mix: premium products (e.g., suites) dilute more than entry-level products
• Behavioral signal: repeat “serial diluters” are clearly identifiable
Price Sensitivity
• Strong monotonic relationship observed
• ~8% dilution at low discount levels vs ~33% at high discount levels
→ Confirms discount strategy is a primary lever
Cross-Product Switching
• RCI: clear upgrade/downgrade behavior across beverage tiers
• CEL: more complex switching across 14 product groups
→ Switching behavior is now measurable and can be incorporated into optimization
Trends
• Slight year-over-year increase in dilution
• Clear alignment with promotional calendar timing
Data Quality Improvements
• Resolved major data coverage gap (increased from ~44% to ~100%)
• Removed operational noise (same-day / same-price rebooks)
________________________________________
CEL Multiclass Model — Customer Behavior Prediction
Developed a new model to predict not just dilution, but next action (retain, cancel/rebook same product, or switch products).
• Strong predictive performance across all outcomes
• Provides forward-looking visibility into product switching behavior, a key unlock for pricing strategy
Also identified and corrected a model weighting issue that was significantly biasing predictions—now resolved.
________________________________________
Model Validation & Calibration
Conducted a full audit of all dilution models to ensure reliability of outputs:
• Identified and corrected calibration issues in CEL models
• Confirmed RCI models and backtesting approach are sound
• Post-fix results confirm models are well-calibrated and decision-ready
________________________________________
CEL Standalone Model — Validation
Re-ran full pipeline with fixes:
• Model accuracy and calibration within expected ranges
• Cross-product price differences are a primary driver (~35% importance)
→ Reinforces importance of managing relative pricing across tiers
________________________________________
RCI Model
• Pipeline and methodology reviewed and confirmed clean
• No issues identified
________________________________________
Next Steps
• Integrate clickstream data to enhance behavioral signals
• Expand analysis of multiclass switching to inform price/volume trade-offs (CEL)
• Apply learnings to improve price curve construction
• Continue development of “new demand” modeling and integration into optimization
• Ongoing stakeholder alignment (RCI readout completed; CEL sessions next)

Ignacio

PCP Pricing Automation

**Created ****product_groups**** table of OBR products for digital-DS collab**
• The table {env}_datascience.digital.product_groups_xref was created to store all the OBR products along with their associated category (e.g. Beverage vs ShoreX) and product group (e.g. Premium Beverage), if appllicable. This is meant to be used in a collaboration with digital & data science team for severla of the projects being worked on. The table was pushed to dev & QA already. Movement to production is in process.
**Develop granular Feature Store tables for CEL Beverage modeling**
The source datasets were organized and joined together appropriately at a very granular level for the purposes of the MNL modeling planned for CEL Beverage PRE/DM. This dataset is very granular at a pax/consumer level for every product and sailing historically. This mainly involved:
Breaking down the transactional data at a granular level, no longer aggregating at a daily, weekly, or WTS bin level. Instead, there is now a rwo for every pax on every sailing and for every beverage product purchased and/or cancelled. This level of granularity is useful for when joining with the clickstream data for more behavioral trends and momentum and how that may be related to price points and what actions were taken.
Some propensity data at a CONSUMER_ID level was properly processed in order to create features representing historical propensity of a certain CONSUMER_ID purchasing beverage (along with other associated bundled items like wifi). These features helped essentially calculate the % penetration of beverage package bookings (the % of sailings at which repeat pax ended purchasing a beverage package) along with the % frequency of dilutions and tradeups at a CONSUMER_ID (very granular level). This was used along with priors calculated for different segments of the addressable population (i.e. different combinations of cabin class & market) in order to calculate a Bayesian Smoothing of these calculated booking behaviors of pax. These can all be used as additional helpful features when building the MNL purchase model as well as the dilution/tradeup/cancellation model.
These datasets were then joined together for a very robust dataset that is planned to be joined with the clickstream behavioral dataset as well.
The next steps for this include adding in a robust seasonality feature (cosine of WOY) and joining with the clickstream data table from digital as it continues being worked on.
**Add cosine seasonality feature + join with clickstream data + better adjust the calculation of priors for Bayesian Smoothed propensities of consumers**

The data engineering and feature engineering from several different data sources were done at a very granular consumer level, encountering a lot of edge cases and inconsistent results that needed to be corrected for. For example, CONSUMER_ID’s were repeated on the same sailing, uncovering some issues that led to having to change data sources and querying methods. Propensity features for beverage purchases were calculated at a customer-by-customer level using CONSUMER_ID; Bayesian smoothing was calculated per customer based on how many of their historical sailings they had purchased beverage. The same was also done for AI and Internet, along with their overall frequency/count of sailings. The intention of this is to build a set of booking features at a customer level to also be joined with the behavioral clickstream data for a more comprehensive enriched feature set at a granular customer level that can be used for the Beverage PRE/DM.

A planned future enhancement is to adjust this cos/sin WOY feature to be instead based more off of a KPI metric (e.g. volume of bookings, revenue, etc) in order to have the signal more closely align with the KPI of interest.

Note: On Bayesian Smoothing: yes hes defining his prior as the expected conversion from that segment (intl, balcony, 7N) for example. then his feature is (prior + historic bookings)/(1+opportunities to book. It's a way of getting the conversion rate but adjusting how much we trust the guest level info based on how many times theyve had the opportunity to purchase

i.e. if we have sailing history for a guest that has been on one sailing and didn't buy beverage vs a guest thats been on 100 sailings and never bought beverage they're likelihood of purchase could be different

Aagam

PCP Pricing Automation

**RCI | PCP2 | Conversion based recs v2**

This week, I focused on adapting the beverage conversion-based recommendations from a product code level to a grouped product level, in alignment with how the business team plans to provide track inputs. For example, product codes 3222 and 3224 are now treated as a single “Deluxe” group, resulting in one unified track instead of separate tracks.

To support this change, I rebuilt the conversion-related metrics from scratch at the grouped level using web data, as the existing digital tables were only available at the product code level. I also ensured that the conversion-based recommendation framework is fully ready to be applied once the track inputs are finalized by the business team.

Additionally, I started working on the ABN Test framework to test out the waterpark prices based on 3 different logics.

**Blocker**: I am currently waiting on the track-based recommendations for RBC Passes and Beverage Packages to obtain the corresponding recommended discount outputs.

Anand

PCP Pricing Automation

**CEL | New Tour Categorization Automation Pipeline**

**Status Update — 05/21/2026**

Classification pipeline is complete for both Royal and Celebrity brands. All new tour codes are automatically detected, categorized via 3-pass LLM consensus (gpt-4o-mini), and persisted to the segmentation tables (dev_datascience.product_segmentation.tour_classification_confident_new / _unresolved_new).

**Completed this sprint:**

QA/QC of classification clusters validated for both CEL and Royal

End-to-end pipeline tested and producing correct label + group assignments

Post-categorization next steps scoped (Wed 5/20 planning session)

**Current state:** TESTING | QA | 90% — pipeline logic is complete and validated. Remaining 10% is automation of the detection-to-append flow as a scheduled job.

**Next steps:**

Build a business-facing portal so business teams can explore, modify, and update segments without DS intervention

Schedule the pipeline as an automated Databricks Job for ongoing new tour code detection

Begin scoping a downstream ShoreX pricing model that consumes the categorization output

**Blockers:** None

Evan M.

RCI Rev Mgmt: Demand Model

Aiming to deliver initial Demand Forecasting model for PRE integration by next week. Go-leve in production for early June.

Instantiated changes that improve and validate model accuracy

**Value ****add:**** foundation for sustained accuracy gains, with material lift visible today**

Improved accuracy and established a multi-model approach

Models can target pax build over the week or focus on cabin-level demand

Data is aligned with expectations and elasticity curves look substantially cleaner

Predictions remain at the cat class level, with feature improvements enhancing rather than redefining the target

Running for both target as pax build and cabin build

Created a pipeline for future changes and updates

New features and model variants can be integrated without rebuilding the entire workflow

Validation and backtest steps are repeatable across everything with defined checks for overfitting / leakage

Set up framework for delivery to PRE and Track Optimization

**Value ****add****: a standard demand model output reduces ETL friction on every connected project**

Aligned table format and delivery to match downstream data requirements

Collaborated with other team members to confirm schema, granularity, and refresh cadence

Defined pipeline and CI/CD

Output is reusable across PRE, Track Optimization, and future without per-product transformation

Versioned tables in the demand_forecast schema

Downstream products can point to a stable output while iteration improvement continues

Mert E, Ben F., David W.

Reviewed the Project TIDE business case with Corporate Strategy, Risk Management, and IBP teams. Aligned that a significant amount of work already exists and that we should continue from where we left off.

**What we plan to deliver ****in**** the next capital project**

The Integrated Business Planning (IBP) team is advancing a multi-year program to transform how Royal Caribbean Group plans, forecasts, and optimizes Food & Beverage spend and revenue across the fleet. The program concentrates on **four strategic thrusts**:

**Pillar 1: ****Expanding into Risk Management & Safety**

Establishing a claims intelligence capability to reduce litigation exposure and prevent incidents over time that (a) leverages predictive modeling to identify and prioritize high-value guest claims, enable faster and more cost-effective settlements, and (b) systematically feed risk drivers back into operations and safety teams that are augmented by AI agents for auditability and decision support.

**Pillar 2: ****Proliferating AI Tooling for Finance Teams (Generative AI Agents)**

Deploying AI-powered agents grounded in Oracle financial data, Agiloft contract data, and Capital Planning data so Finance teams can identify IBP opportunities, interrogate forecasts in plain English, and run auditable what-if scenarios without manual cycles.

**Pillar 3: ****Scaling the HF&B Financial Budgeting Pilot**

Extending the proven BEYOND Finance Tracking Tool across the full Celebrity (~17 ships) and RCI (~28 ships) fleets, converting it into the governed source of truth for production-order, purchase-order, and future-spend reporting that Finance can operate against an SLA.

**Pillar 4 (Tentative): ****Food and Beverage Cover Modeling**

Standing up a net-new demand forecast at the ship × voyage × day × meal-window × venue grain to unlock specialty-dining yield management and provisioning alignment, a multi-million-dollar incremental revenue

Key Notes:

**Primary focus should be Pillar 1: Expanding into Risk Management & Safety**, since the document positions it as the strongest near-term value driver and you’ve clarified it is the **main cost savings driver with up to $5–10M expected savings**.

The expected delivery for that pillar includes:

**Guest claims management models**

**Claims management automation**

**Risk management web app, AI chatbot, alerts, and workflow automation**

**Safety KPI framework, root-cause analysis, and enhanced understanding of shipboard safety events**

Potentially **crew claims models**, but the document suggests those could be moved to a later phase

**Tentative resourcing needed**

The most supportable tentative ask for this next capital project is:

**1 Sr. Lead Data Scientist**

**1 Data Scientist Analyst**

**Partial Data Engineering support rather than a large net-new DE ****ask**

The document has mixed discussion on DE need, but the most grounded interpretation is:

**Some DE capacity is needed**, especially for safety work

This may be covered through **shared/internal DE support** rather than a full standalone new DE hire

There is explicit discussion of **~25% DE allocation for safety**, with mention that **50% could be better**

**Important framing **

**Pillar 1 should be framed as the lead investment case** because it is the **clearest cost-savings lever**

**Pillar 4 should be treated as speculative/tentative**, since the document and your note both indicate uncertainty on prioritization

So the clean executive takeaway is:

**Fund Pillar 1 now as the core business case**

**Keep Pillar 4 out of the primary ask or position it as optional/future-state**

**Mert**** E.**

**MIAP**

Worked on fixing vulnerabilities and making adaptations to two new MIAP AI agents and a new analytics app built by Francisco from Jan Solum’s team; fully productionized.

Worked on fixing vulnerabilities and making design improvements to the new fleet tracking app built by Arya.

Collected detailed design and user documentation for the AMOS Asset Management Database by coordinating with the parent company. Built a hybrid AI search engine using a Knowledge Graph database and a Vector Database, and enabled local coding agents to effectively use the documentation. Also provided Databricks access to the agents and began creating high-value Silver/Gold tables for AMOS with agent automation and review. Once all Silver/Gold tables are completed, the plan is to develop agent tools, create an AMOS Agent, and begin work on Brian Soresen’s requested fleet performance app.

Joined a workshop between Wärtsilä and RCG on the development of an Engine Reliability Index. Agreed to start joint collaboration. Some disagreements arose during the meeting, as Wärtsilä raised concerns about our API limitations for data sharing and advocated for deploying their own data collection servers.

Met with Captain Henrik to discuss Project ORCA, which aims to use AI agents to facilitate operational assessments of officers. Due to PII concerns, reached out to Suzan Low regarding how this data should be stored.

Met with Jan Solum (Marine Operations Safety VP) to discuss the creation of Safety KPIs. Discussed availability of funding for a Data Scientist in the upcoming Risk Management CAR dedicated to Safety. Agreed to continue developing a roadmap for safety initiatives.

**Will:**

**MIAP**

Worked with multiple business partners to resolve issues with SSC FACTs digital twin data (still a work in progress).

Researched a new Charge Air Cooler efficiency modeling opportunity with Javier Gutierrez (Decarbonization team) and Mert Ersoz.

Documented available data and completed charge air cooling system tag mapping for one ship.

Began EDA on the charge air cooling system.

**Ram:**

**MIAP**

Verified all database relationships and created the POLARIS database in PostgreSQL (including indexes and relationships). Planned creation of two additional tables (pending validation).

Implemented required changes for the Marine package and REST API for real-time streaming; deployed to QA. Performed initial local testing confirming expected performance.

Loaded new TCP protocol data and Modbus Eniram data into development tables; submitted for verification.

Designed and implemented a new configuration file format for ship- and tag-level vendor access; deployed to QA.

**Reza:**

**MIAP**

Developed a proof of concept for the Targeted Moving Average (TMA) residual boosting method to enhance the in-house weighted moving average approach. This method unifies handling of both continuous signals (e.g., HVAC, service power) and step-function signals (e.g., scrubber, OFB) into a single regressor.

Tested, verified, and further developed the TMA method. Results below:

**TMA vs. WMA Benchmarking (preliminary):**

HVAC (continuous): improved 24/25 ships (96%); mean SMAPE 7.42 → 6.26 (~16% improvement).

Hotel (continuous): improved 25/27 ships (93%); mean SMAPE 5.00 → 4.74 (~5% improvement).

Service Power (continuous): improved all ships evaluated (100%); mean SMAPE 4.49 → 4.07 (~9% improvement).

Scrubber Power Total (step-function): improved 17/17 ships (100%); mean SMAPE 43.93 → 24.52 (~44% improvement).

OFB Total (step-function): mean SMAPE 75.56 → 71.81 (~5% improvement).

The TMA method has been deployed to production for scrubber models. Other areas will be rolled out incrementally after hyperparameter tuning and further testing.

**Mahshad:**

**MIAP**

Added deployment to QA on the GitHub platform and resolved security issues.

Worked on AX following the addition of Chiller #4 (multistack); updated the model to include the new chiller and contacted Valmet to obtain the required information (e.g., NodeID for data integration).

Completed individual chiller models; modeling for all chillers across each ship is now complete.

Investigated and resolved several job run failures.

**Arya:**

**MIAP**

Finished productionizing the fleet tracking app; now live on the MIAP app.

Worked on testing the Target Moving Average model and comparing it with current solutions.

Designed a new Monte Carlo algorithm to compete with TMA; currently evaluating results.

Integrated TMA as the default algorithm for hotel, HVAC, and scrubber systems.

Finalized SORA deliverables for the GMO team.

David W.

Human Resources (HR): **Demand Planning ****CAM ****CAR**

Responded to Martha’s concerns regarding the framing of the agentic capabilities in the CAR, particularly around whether the proposed solution is truly agentic versus conversational, and around the associated incremental OpEx. We clarified that the solution is fundamentally an enterprise demand planning capability built on forecasting, automation, and governed operational data, with GenAI functioning as a secondary interface layer to improve usability and decision support. Based on that feedback, we are tightening the CAR narrative to better articulate the distinction, clarify the role of the digital worker versus human planners, and strengthen the explanation of recurring support costs. **Submission remains planned for next week.**

Santiago & Javier

PROPEL (CEL, Santiago & Javier)

Measurements:

Conversion uplift analysis, APD uplift measurement, incremental revenue calculations, p-values, confidence intervals, two-proportion z-tests, Welch tests, and propensity model validation using decile lift and ranking analysis.

Spikes:

Developed architectural and business governance recommendations focused on strengthening experimentation governance, improving test/control balance and contamination prevention, standardizing analytical grain using booking_key and booking_category_key, and introducing statistical validation as a governance layer for experimentation and monetization initiatives.

Proposed continuous PSI and drift monitoring, propensity model retraining triggers, and clearer separation between offer effectiveness, model weakness, experiment quality, and operational issues.

Developed the landing page front end for assigning quota values usually managed through SharePoint.

Linear Programming Optimization:

Developed the LP optimization logic in PySpark and prepared it for real-time performance validation during the next execution.

Bugs & Issue Investigation:

Investigated issues related to Model Serving cost spikes, workflow deployment stability, Databricks Asset Bundles.

Diagnosed the incorrect passenger name issue as an upstream Fidelio/Silver timing problem involving a cancelled placeholder guest that temporarily flowed into propel.guest and was later displayed in the PDF.

Identified the missing Player IDs issue as a timing gap where the Casino CSV was generated before the Player IDs became available in the Silver Oasis table.

Diagnosed the Missing Offers issue as an offer_config enrichment problem caused by historical offer_config_id references missing from the current table, and added a controlled fallback from offer_config_history.

Glen-Erik

PCP Pricing Automation (Glen-Erik)

App/ Web: New Schema in production

Email / SFMC: testing completed in dev, in progress in prod and should be finished Friday May 22nd.

Targeted offers Hub UI -

tested in dev and identified minor bugs in data. Bugs fixed and re-testing is in progress.

Container app and postgreSQL backend DB created. In process of setting up.

Access control group created as well.

Glen-Erik C

HR: JD Tool (Glen-Erik)

Launched teams-based agent with HR Business Partners to get feedback. However, during the demo, the solution was having response issues where the same question sometimes has to be asked 2-3 times before getting a response. Raised the issue with microsoft.

Eswar

Other DS Projects (Eswar)

Demand Forecasting project discussions and setting up a new repo by developing all the CI/CD needed. Currently productionizing couple of workflows forecasting expected demand given knowledge of constraints and market behavior to input PRE and Track optimization.

Sailing environment project discussions, created a new repo in Data science, enabled developers in starting development and bypass all security issues.

Web Scraping script optimization by reducing run time, improving by adding failure handlings, updated chrome driver to scrape and validated results with stakeholder.

Setting up Asset Bundles deployment in GitHub for project axiom_meta_data_gen

Following up on OBR support request to add business team to OBR-DS group, so that they can control workflow runs.

Deployed OBR product xref workflow

Eswar

Revenue Management Automation (Eswar)

Conducted enablement session on CI/CD, productionizing workflows to the RMA new members.

Feature Store tables validation, by creating views provided by DE team and providing feedback to improve match rate

Monitoring CI/CD deployments, helping with PRs
