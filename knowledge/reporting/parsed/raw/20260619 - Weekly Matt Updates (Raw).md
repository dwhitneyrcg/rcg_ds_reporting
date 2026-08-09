Erick E.

## PCP - MyCruise Recommender

*Personalized post-booking recommendations (excursions, dining, spa) powering the ForYou surface in the app.*

### Webapp / Playground

- **Playground Web App Deployed with ForYou Calendar Controls** _(Erick A.)_: The Playground is the stakeholder-facing app for exploring what the recommender returns; the ForYou Calendar surfaces day-by-day recommendations across a sailing. Erick deployed the latest Playground with new API parameters so users can interact directly with the ForYou Calendar recommender and tune what it returns.

- **RCI Email Marketing Demo — Booking-Level Recs Wanted** _(Erick A.)_: Erick demo'd the latest model set to the RCI email marketing teams. There's clear appetite to feed **booking-level recommendations** from the recommender into customized, booking-level marketing emails — a concrete new channel for the engine beyond the app/web surface.

### Ensemble Pipeline & ALS Tuning

- **ForYou Pipeline Unified, Auto-Retraining, and Hardened** _(Cristian V., Milestone)_: The ForYou recommender is an ensemble of three models — client clustering, product clustering, and ALS (the collaborative-filtering model behind personalized recs). Building on last week's clustering integration, Cristian consolidated the whole training + auto-retraining flow into a single standardized pipeline (less manual overhead, less technical debt) and added a grid-search framework that auto-tunes hyperparameters from simple to complex configurations.

- **Better Recommendations for Niche Segments** _(Cristian V.)_: Certain low-volume brand/meta-product combinations were underrepresented in the holdout set and getting weaker recommendations. Cristian refactored the evaluation logic to dynamically pick the parameters with the best bias-variance tradeoff per segment, lifting quality for those niche segments without hurting the rest.

- **Deterministic Real-Time Cluster Labels (SHA-256)** _(Cristian V.)_: Client-cluster labels are generated dynamically per brand/meta-product combo and must map the same way every time during low-latency API inference. Cristian implemented a SHA-256 labeling strategy that guarantees consistent customer-to-cluster mapping for live requests with zero database-lookup overhead.

### A/B Testing & Ranking Policies

- **A/B Splitter & Ranking-Policy Control Panel** _(Cristian V. & Erick A.)_: Continuing last week's A/B splitter (assigns each booking to a stable test group so recommendation configs can be compared head-to-head), Cristian is generalizing the models to support ranking policies and asked Erick to build a control panel so Product can set the ranking policy (e.g., margin vs. revenue) per brand and use case. Splitter still in progress; control panel queued with Erick.

- **Hard-Coded Business Picks** _(Cristian V.)_: The capability to drop business-selected products into specific recommendation slots is fully built and live on DEV; Erick is integrating the override into the Playground control panel before the prod push.

### Recommender Engine

- **Apriori Extended to All Categories** _(Rodrigo B.)_: Bridging last week's Apriori build-out (market-basket rules — "people who bought X also bought Y"), Rodrigo's multi-category rules (Dining, Beverage, Spa) are computed and ready on a branch; remaining work is integration into the recommender.

- **AI Product Categories — Beverage & Dining Done** _(Osvaldo V.)_: Osvaldo reused the Shorex product-categorization pipeline to generate fresh AI-driven product categories — **beverage and dining are complete**, spa and one more remain. This is an exploratory exercise for now (not yet wired into the recommender); next he'll consolidate the per-category notebooks into one and PR it.

### Tooling / Documentation

- **Confluence Docs Now Auto-Updated by Agents** _(Erick A.)_: Building on Cristian's `sync_to_confluence.py` utility from last week, Erick stood up automation that updates Confluence documentation directly via agents — keeping the recommender's docs in lockstep with the code without manual edits.

Erick A.

## Project Axiom — Voice 360

*Insight extraction from unstructured customer feedback (Medallia, Guest Logs, Qualtrics) via LLM pipelines — feeds emails, dashboards, drivers analysis, and chat.*

### Email Reports

- **Five New Dry-Dock Reports Delivered** _(Erick A., Milestone)_: The dry-dock-style ship report (first proven on Symphony/Icon, then scaled by Osvaldo) analyzes Medallia and public-source feedback to feed dry-dock business cases. Erick delivered five new dry-dock reports plus a new-build report to **Michael Figgis**, covering Enchantment, Navigator, Ovation, Rhapsody, Vision, and Wonder (EN, NV, OV, RH, VI, WN).

- **Port Email — Recurrence Chips** _(Rodrigo B.)_: Following Josh Carroll's ask to track how complaints shift over time, Rodrigo replaced the long recurrence-analysis section (lots of length, little value) with per-complaint chips — flagging each as new, few-mentions, or recurrent versus the prior quarter, plus an approximate prior-quarter mention count. Sending the version with mention counts to Anne Marie and Matt, who'll decide whether to keep that detail.

- **Shorex Per-Location OSAT Column** _(Rodrigo B., new)_: To resolve an ambiguous stakeholder "matrix" request without bloating the report, Rodrigo is adding a per-location OSAT (overall satisfaction) column at the Shorex level and will confirm the approach with stakeholders before building further.

- **Royal Santorini Beach Club Email** _(Rodrigo B.)_: Gabriela confirmed the email can go out; Rodrigo is scheduling the send job.

- **Shorex GSO Safety — Guardrails & Job Consolidation** _(Danusio G.)_: Bridging the prior token-spike investigation, two weekend failures surfaced (both empty-dataframe edge cases) — the **June 13 error is fixed**, June 14 is proving stubborn (failures cascade as each is patched). Separately, GSO preprocessing is being consolidated into the prod main job, with the standalone GSO job kept only for debugging and slated for deletion once stable.

### Guest Logs

- **Realtime Text-Search Tool Demo'd to Hotel Ops** _(Erick A. & David M.)_: Bridging last week's new SmartService initiative (AI-assist guest-issue categorization at the desk), Erick demo'd the realtime text-search tool to the Hotel Ops teams. Next step is discussions around formally deploying an **API to integrate into SmartService** — the agent-facing app. Under the hood, David's v2 service scaled the category taxonomy from ~100 to ~1,000 and improved both speed and accuracy.

### Drivers Model

- **Container-App Deployment Unblocked** _(Erick A.)_: The drivers model (predicts NPS / guest satisfaction and explains what drives it) needed a hosting target beyond Databricks. The team obtained Azure Container App access this week, clearing the blocker — the drivers model is back in active scope for final touches and improvements.

- **Local Databricks Experimentation Working** _(Osvaldo V.)_: Osvaldo got a local-to-Databricks connection working via GitHub Copilot, so he can now inspect the repo, propose improvements, and run experiments and hyperparameter tuning locally against the Databricks cluster.

- **Meta-Product-Specific Models** _(Osvaldo V., new)_: Today there's one global drivers model trained across all sailings. Osvaldo will train a 7-night-Caribbean-only model and compare its feature importances to the global model — testing whether meta-product-specific drivers models reveal materially different satisfaction drivers.

### Webapp

- **Port Map Integrated into the Axiom App** _(Osvaldo V.)_: Bridging last week's D3.js port map (excursion-category distribution across all ports), Osvaldo wired the map into the Axiom app tool and tested it locally; pending Erick's review before deployment.

### Scraping

- **TikTok Real-Time Relevance — Decision Gate** _(Danusio G.)_: Bridging the working TikTok harness, Danusio reran the pipeline over full history and found only ~15% of comments relevant (below the 30% bar), with the signal dominated by old viral news (the Icon glass-slide incident). The final test before continuing: filter to the **last 7 days for Icon of the Seas** and check whether fresh weekly issues surface — if not, the effort may be abandoned. Multi-source blog and Booking.com scrapes are backlogged behind the GSO pipeline fixes.

## Silversea

*Brand-specific guest-feedback email reporting for Silversea, adapted from the Axiom email-report framework.*

- **Email Report Enhancements** _(Erick A., Milestone)_: Erick added several features to the Silversea email report — **STLY (same-time-last-year) metrics**, removed outdated KPIs, and a new **GenAI section on how to convert neutrals into promoters** — sharpening the report toward actionable satisfaction levers.

- **Axiom Ship Scorecard (SSC) Changes** _(Erick A.)_: Bridging last week's queued SSC changes, five of six are done — removed LTR and Hotel Services, added STLY based on ship matching, added a neutrals breakdown, and surfaced total promoter/detractor/neutral counts. Remaining: align with the team on shipboard email deployment.

## Project Concept Testing Lab

*Agent-persona framework using LLM-driven synthetic respondents to A/B test ideas before committing to live tests. Built on TinyTroupe (Microsoft OSS).*

- **TinyTroupe Comparison Ready to Present** _(Osvaldo V.)_: Closing the prior in-build comparison, Osvaldo's report weighing TinyTroupe against the team's current concept-testing implementation — validated against Royal Caribbean's real 2021 Hideaway Beach study — is ready to present to Hannah and the broader group to set direction.

Erick A.

PCP Pricing Automation

## Operational / Cross-Project

- **Target-Setting Readout for Gang** _(Erick A.)_: The daily target-setting model (forecasts revenue targets for internet, shorex, dining, etc.) has run in production since mid-May. Erick is assembling the forecasting-accuracy summary Gang expects — current MAPEs are sub-20 for Internet and Dining, 30–40 for Shorex — broken down by product category and market-level vs. aggregate.

- **Contact Center — Siren / CCAS** _(Erick A. & Osvaldo V.)_: The time-to-topic pipeline analyzes how quickly contact-center calls reach a given topic. Osvaldo replicated the 2024 baseline and has a CSV ready, but the 2026 rerun is **blocked on data engineering** — the source table has no data past 2025.

- **Task Tracking via Confluence/Jira Agents** _(Erick A.)_: Rather than build a custom leadership project-tracking web app, Erick chose to push task/note tracking onto Confluence and Jira programmatically via agents — reusing existing platforms and Cristian's sync utility instead of new infrastructure.

Erick A.

## Blockers & Dependencies

- **Product-ETL expansion (beverage/dining)** — blocked on the platform team fixing GraphQL ShoreX access.

- **GSO Shorex Safety pipeline** — June 14 empty-dataframe failure cascading; Danusio still chasing root cause.

- **Drivers model + Guest Logs integration** — the new gold-layer guest-logs table is missing booking ID, blocking booking-level aggregation; awaiting data-engineering follow-up.

- **Siren time-to-topic rerun** — blocked on data engineering; source table has no data past 2025.

Carlos

Ecommerce Customer Targeting

RCI/CEL Targeting: Code maintenance (replace localcache for actual cache function,  optimization of prediction pipeline stage 2 for single node cluster). Added Journey score training report to ecommerce dashboard

Silver Sea Models (JAKALA): Study existing Jakala feature engineering code

Carlos

Loyalty Simulator:

Code clean up

Ingest consumer loyalty points from dim_loyalty (research stage)

Bao

E-Commerce:

Discovered a critical discrepancy in the Royal Caribbean production clickstream table, where Royal Caribbean and Celebrity Cruises data became merged starting July 2025, leading to incorrect brand-level booking propensity features.

Conducted a detailed exploratory data analysis (EDA) to pinpoint the issue, document the root cause, and quantify the impact on model inputs.

Designed a comprehensive plan to fix the ingestion process so that clickstream data is separated by brand, ensuring more accurate intent signals in future models.

Created a detailed EDA notebook to capture the discovery process, ensuring transparency and reproducibility of findings.

Identified that the Celebrity Cruises clickstream table was outdated and lacked meaningful consumer and source IDs after July 2025.

Developed a strategy to backfill historical Celebrity clickstream data, integrating it into the training dataset to ensure both brands are represented historically.

Outlined a plan for Royal Caribbean ingestion fixes and delegated tasks across brand teams for smooth execution.

Began assessing how new Epsilon features will replace existing demographic data features; noted that we need a few months for the new data to develop a longer historical record before integration.

**Caleb:**

**CLV: ****Consumer Lifetime Value**** data**

*Completed*

Completed end-to-end validation of the CLV stage table against VCAP MICE across all years (2017–2025), segmented by brand, year, and channel. This confirms that channel logic is now applied consistently across all passengers for all historical years. The only discrepancy identified was approximately 90K passengers present in VCAP but absent from stg2; the distribution of these records suggests a missing filter upstream.

Awaiting team confirmation to rerun validation and subsequently re-execute the pipeline.

*In Progress*

Coordinating with the CLV Build team to evaluate feature attribution from Customer360. Discussion will cover data readiness, feasibility, and grain resolution required to map from booking/event/consumer level down to passenger level.

Awaiting access to the appropriate Epsilon and Medallia tables to assess which columns offer the most analytical value.

**Caleb: **

**CLV: ****Sailing Environment (Demand Model)**

*Completed*

Refreshed the model's input data sources, including the Cruise Industry Fleet Model, Deployment Blocking File, and prior Strategic Plan forecasts.

Refactored the data pipeline to persist cleaning and transformation logic as Delta tables, improving shareability and version control.

Built an automated competitive earnings scrape that extracts all available financial and capacity metrics from each corporation's SEC filings.

Validated against the existing manually maintained file through 2019 — results match exactly, with the added benefit of automation and corporation-specific reported figures.

*In Progress*

Debugging the pipeline by validating specific queries against RP's source tables to ensure output accuracy.

Mireille

Contact Center: Workforce Planning

**Executive Summary**

**SFTP:** Connection validation, retry logic (3 attempts / 60-second waits), and controlled file-write delays are live — tested and redeployed.

**Erlang A engine:** Optimized search complete — same output, fewer unnecessary steps, reusable for international.

**Data loading:** Parallel query runner live across the full app — faster screens, same results.

**Combined LOB:** All composite teams can now be planned as a single unit — tested and validated end-to-end.

**Per-LOB staffing ceilings:** Active for RCI — resolves Casino's ~2-hour run time.

**30-minute model:** Integration complete; testing pending upstream data quality stabilization from the Genesys migration.

**Multi-Scenario Comparison:** ≈80% complete — planners will soon compare unlimited what-if scenarios side by side with full CSV export.

**Demo:** Postponed — Jason's team is resolving Genesys production issues for Royal and Celebrity.

**Next focus:** International advanced app development.

**Next Steps**

**CCI North America data integration** — integrate, map, and orchestrate Celebrity North America data sources to flow into the "Run Your Own FTE" advanced section, covering call volume, assumptions, and all supporting inputs.

**Monitor upstream data quality** — track prd_silver.mkrpops.cms_interval_stats_all and prd_silver.mkrpops.cms_skillset_vtest for stabilization; complete 30-minute testing once clean data flows through.

**Finish Multi-Scenario Comparison** — complete the remaining 20% and validate end-to-end.

**Reschedule demo & feedback session** — once Jason's team is unblocked from Genesys production work.

**Begin International advanced app development** — carry forward the NA architecture and optimizations to adapt to the international data specificity.

Detailed Report from Mireille here:

Ben F.

Integrated Business Planning:

**Executive Summary**

Laura approved Option 1. We finish the Celebrity-fleet rollout of the IBP procurement capability, aligning what we buy to the AI demand forecasts, before we move to Royal. Royal completes by end of 2027. That gives us a committed, sequenced program across both brands: Celebrity first, Royal second.

The big item this week is that the RCI/CCI food-and-beverage corrector went live in production on June 18. It is the first model from the self-improving forecasting system to clear the full governance gate. A machine-learning corrector now sits on top of the existing demand model. It is approved and armed, but it has not changed a published number yet. The first new run of the new RCI/CCI demand model from the automated system publishes automatically on the next weekly run, Saturday June 20, and only if that run's accuracy-precision and volume checks pass. If they do not, it falls back to watch-only on its own, no manual step. When it does publish, dashboards, supply, and orders inherit the improvement, and original values stay preserved for instant rollback.

On accuracy, the gain is real but the track record is still young. We measured about 23% better on the settled month (median error 12.1% to 9.3%), about 27% on the live serving surface, and about 29% on the dashboard backtest. That approval rests on one fully-settled month under a time-limited window. The approval is good through July 1, and the evidence-bar override expires July 15, with the standard three-month record still building. The supply-chain (SSC) book stays in watch-only and is queued next.

**This week's progress**

**New RCI/CCI Demand Model Activated in Production**

The new model has been approved and ready for deployment this weekend. Documentation on it is here;

Verified accuracy: about 23% better on the settled month (independently reproduced at about 0.90 precision), about 27% on the live serving surface (this re-measurement is what cleared the go-ahead after an earlier review held it back), and about 29% on the broader dashboard backtest.

The weekend RCI/CCI demand modem run applies the new model only if its live checks pass: approval valid, accuracy precision above floor, total volume within guardrails. An out-of-band result reverts to watch-only automatically. No manual deployment needed.

The SSC automated demand model improvement system stays in watch-only. Its first live measurement was just unblocked, and it must clear the same gate before activation.

**Durable AI infrastructure**

Moved the self-improvement machinery onto company-owned, scheduled cloud infrastructure, running on a Microsoft Azure-hosted model. It runs reliably, restarts cleanly, and we can audit it.

**Executive visibility**

Finished the executive dashboard on the IBP App and deployment work to Azure Container App is in progress following meeting with Yan and team.

A new Model Registry shows which forecasting models are deployed versus awaiting approval and links to the formal whitepaper and a plain-language summary.

The Executive Overview now reflects only the ships actually in the pilot, with a real deployment map across all 44 Royal Caribbean and Celebrity ships. Most placeholder data is gone, so what leaders see is genuine with remaining placeholder data on track for migration to live data soon.

**MOT Reporting fidelity**

Did a deep review of how MOT was calculated and code validation before the meeting with Laura to confirm how the data was being calculated and that results were accurate. Presented results to Yan and Connor and we aligned on the output reports.

**Next steps:**

Confirm the first live RCI/CCI new demand model lands on the June 20 pipeline run cleanly: check the guards pass, the four forecast checkpoints update, and accuracy holds. Watch the auto-revert and auto-demote safeguards through their first cycle.

Activate the SSC automated demand model improvement system.

Working with Mert and platform team on IBP UI deployment to Azure. Pending this deployment, testing of the app and proper user authentication and onboarding is needed.

Migrate PowerBI reporting to the IBP UI App using Dax code Yan has provided.

Sunset remaining placeholder data in IBP UI Executive Overview page when Shipboard Inventory (Brenda), Data Engineering (Paolo) provide updated data sources.

**Appendix: PR references (for the record)**

Self-improving forecaster (corrector hardening, governance, served re-measurement, activation): #565, #568, #573, #577, #585, #587, #600, #608, #609, #612, #616, #619, #620, #621

Durable AI infrastructure / Azure migration: #576, #583, #586, #589, #590, #607, #618

Executive dashboard (Model Registry + Overview): #617, #623

Procurement-cost (MOT) reporting correctness: #572, #574, #575, #578, #579, #580, #598

Camila A.

IBP:

RBC Demand Forecast

Monthly product consumption at the Royal Beach Club destinations: NAS (Nassau / Paradise Island, established) and JTR (Santorini new).

Guest forecast

Consumption only happens when ships arrive and guests come ashore, so guests are built in two layers:

Passengers arriving — from the sailing/itinerary schedule: which ships call each week and how many passengers each carries, summed across the several ships that call (typically ~7, up to 13 per week).

Visit rate (take-rate) — the share of those passengers who actually go to the beach club, from pre-cruise purchases + on-board purchases + the destination's own realized visit history.

Guests = expected passengers × expected visit rate, then consumption scales with guests and recent consumption-per-guest.

Cold-start handling: a brand-new destination (JTR) borrows the visit-rate pattern from the established sister beach club (CocoCay) until it accrues its own history.

Graduation rule: a destination switches from "transfer-prior only" to its own full consumption model once it has ~26 weeks of consumption. NAS has graduated (28 weeks); JTR has not (0 consumption weeks, still transfer-based).

Guest model accuracy + how it was derived

Metric: predicted guests vs actual booked guests over realized historical weeks → median % error (typical) and volume-weighted % error (WAPE).

Established destination (NAS): ~8% typical error (~13–15% weighted) — accurate, slight ~8% over-estimate.

New destination (JTR): ~80% — purely cold-start; its total volume is on target (ratio ≈ 1.0) but week-to-week is noisy.

Overall, volume-weighted: ~16%, driven by the established destination (the large majority of guests).

Consumption forecast accuracy

Finish (latest run, 2026-06-15): final monthly guardrailed MdAPE ≈ 43.6% (model stage 43.9%; nearest-month ~40%).

The one validated step-change was the near-term recency blend: ~5 points (a controlled like-for-like test, 48.2 → 43.1 on the same product-weeks).

Guardrails + new enhancements that helped

Near-term recency blend — blends recent actuals into the short-horizon forecast (the ~5-point win; deployed).

Per-ship → product-week consolidation (CocoCay-parity fix) — the recent-trend signals (the model's #1 driver) were being computed across individual ship arrivals instead of weeks; now consolidated to one row per product-week before trends. Plus new cross-ship signals (how many ships called, how full they were).

Guardrail layer: caps unreliable predictions (e.g., very sparse, low-history products) and produces the final monthly numbers.

Added RBC (Royal Beach Club Paradise Island) as a parallel union into all 8 Supply Step 2 segments for HF&B code, mirroring the existing Cococay pattern and leaving Cococay untouched

Pilot - RCI/CCI integration:

Test-mode table isolation for all groups (MOT, Order Creation, Finance Tool)

To possibly reduce runtime from running both brands and all their ships in one run, we create two separate pipelines, one dedicated for each brand, with a final consolidated union of rci and cel at the very end

Run time is estimated with both brands and only finance tool group to be 6-9 hours.

I proposed to Yan to have dedicated time slots for certain tasks to reduce compute time if this pipeline needs to run at least 4x a day to get all consumption from all regions due to time differences.

Guardrails enhancements now fleetwide:

The seasonality guardrail in the Celebrity pilot finance tool was under-predicting food spend for two ship types: EDGE (an established ship whose summer actuals run 60–100% above P8 model predictions) and XCEL (a new ship with no historical data of its own).

Three code changes were made to fix this: the sister-ship pool that XCEL uses as a benchmark was restricted to only use verified actual spend data (not model predictions), a per-ship calibration scalar was added so chronically under-predicted ships like EDGE can automatically correct toward their historical actuals, and the corridor parameters for new ships were tightened so predictions target within $0.10 of budget instead of the $0.60 floor that was designed for established ships.

CocoCay:

Wired 7 gangway/guests-ashore features as ShapRFECV candidates (GUESTS_ASHORE, LOAD_FACTOR_IOT, MEAN_DWELL_HRS, MORNING_DISEMBARK_PCT, DISEMBARK_DURATION_HRS, CENTRAL_DISEMBARK_HR, ASHORE_RATE_WK)

PAX is the better normalizer since it has the current and future pax count (stable, complete, predictable).

GUESTS_ASHORE is the better actual headcount — so it lives as a candidate feature and reference table for data-accuracy, where its physical truth is the point, rather than as the denominator, where stability is the point.

Ale:

IBP:  
**Ale's Weekly Update: June 18, 2026**

**GMO Unhealthy Inventory Dashboard — Consumption Logic Refinement**

Updated the consumption exclusion logic to filter on GL account only, removing the prior dependency on cost center. The notebook now resolves each EXTRANO value to its legacy GL-account format via prd_gold.ibp.gl_ccid_mapping — handling both old and new formats — and excludes rows matching accounts 6203, 7201, 7205, 7250, 7307, 7320. Validation across 1.7M stock transaction rows confirmed 435K excluded and 1.3M retained. The fix was synced across the workspace notebook and Repos branch copy.

Also resolved a separate issue where inventory records with a PARTTYPENO starting with WST were being incorrectly included in GMO inventory totals, artificially inflating overall inventory values. After confirming the root cause with the team, these records are now properly excluded from the calculation.

**CocoCay Shore Excursion Feature — Signal Validation & EDA**

Completed initial signal validation to determine whether pre-cruise shore excursion booking counts carry genuine predictive power for weekly venue consumption at CocoCay, beyond what PAX already provides. Correlation analysis across five venues confirmed a statistically significant signal in three: Coco Beach Club, Waterpark, and Oasis Lagoon all showed meaningful same-week Pearson and Spearman correlations (p≈0), while Hideaway Beach and South Beach did not show a meaningful signal at this stage.

**Next Steps**

With signal validation complete, the focus for the coming week is implementing the shorex feature join into the CocoCay demand pipeline — aggregating weekly excursion metrics from COCOCAY_SHOREX_GUESTS into the demand panel and carrying those columns through to the Probatus feature selection checkpoint.

Ryan

IBP: 
**Ryan Weekly Update:**

Finalized the GMO Inventory depletion pipeline and merged to master. Created a job to orchestrate it.

Focused on getting up to speed on the CocoCay Demand Model. I traced the CocoCay pipeline end-to-end: ETL builds weekly product × ship grid → Demand_Notebook collapses to product × week, engineers features, creates backtested folds, writes AGG table → Probatus runs RFE feature selection and trains gradient boosting → Guardrails applies post-hoc seasonal corrections → Safety Stock aggregates to monthly for ordering.

Reviewed the backtesting structure: cross-join with MODEL_TRAINING_DATEs creates train/test folds. The LATEST_ swap freezes trailing features on forecast rows to prevent leakage. Model target is CONSUMPTION_4WKMA, predicted for each of 30 forecast weeks per product.

Currently, min_backtest_dates = 1 means only 2 monthly folds (same season) reach Probatus.

Will explore increasing this for a dedicated validation run to prove the new features reduce MAPE across diverse seasonal windows.

Confirmed root cause: 4 YoY lag features are unnecessarily frozen via LATEST_ swap. At ≤30-week forecast horizon, they always reference data ≥22 weeks before training date (no leakage). The freeze flattens the seasonal signal, producing unseasonal predictions that Guardrails must compensate for.

Reviewed the A/B implementation approach provided by Camila: 5 new *_TARGET_LAG_* columns bypass the freeze with a leakage-safe guard while originals remain as the control.

**Next Steps:**

Define the 5 feature expressions, register in both branches of create_backtested_data  (before the LATEST_ swap), add to all downstream feature/aggregation lists, add to probatus_rfe.py. Deploy and confirm all 5 arrive in the AGG table as DoubleType

Eswar

Revenue management Automation:
1. Productionized Category-Gapping Model Training, Category-Gapping Optimization workflows for both brands RCI and CEL which helps in finding missing opportunities and turn those predictions to decisions
2. Validating the results of Data Engineering Feature store queries and providing the feedback to enhance match rates
3. Fixed pl_cel_track_fitgrp ADF pipeline which failed due to hardcoding dev catalog and in prd, it cant query dev catalog due to permission issues. CEL team didn't perform QA check, so detected it in prd run. 
4. Monitoring CI/CD deployments, helping with PRs 
5. ML Support in debugging issues and enabling fast development

Eswar

PCP Pricing Automation
PCP Mass Promos: 
1. Developed and deployed hotfix_promoTable_to_version_yesterday workflow for OBR to revert prices to yesterday's as promo automation process failed on the DE side of the workflow due to the password and 2-way authentication changes
2. Optimizing the query where working off of vcap daily snapshot to feature engineer the final feature set for a model with clickstream data and its stuck running for more than 3 days. Currently working on it to optimize it and reduce run times -OBR

Glen-Erik
PCP Pricing Automation: Targeted Offers: (Glen-Erik)
1. Email Offers: finished automating and testing the SFMC prod pipeline with digital and marketing sending two 4k offer batches that successfully made it to SFMC.
2. POC #3: Put together an email eligibility table/query to identify guests we are able to reach via email.
3. Targeted Offers Hub Interface: 
a. Launched production site at https://to-pricinghub.rccl.com/
b. Stratified sampling for test/control: 
i. Finished testing and launched capability in the app.
ii. Logged automatically in Databricks for analytics and transparency.
c. Added duplicate row checks to the CSV since there were a few duplicates last time.
d. Began adding guest email for joining data in analytics and language for analysis as well. (in progress)

Glen-Erik

HR: Job Description Agent: (Glen-Erik)
1. Positive feedback about the agent from HR BPs.
2. Agent went down due to cloud-wide microsoft teams issues with agents. Restored and communicated issues and resolution with HR for awareness.

David Whitney

HR: CAM Demand Planning

Updated the CAR Document to answer questions from Capital Planning team on the CAR Submission. Nothing major, but more context about the asset, how it fits into the other CAR submissions, and corrections on the Opex part of the finances.

Santiago and Javier
CEL PROPEL: (Santiago & Javier)
1. Uplift ML Logic Adaptation: Adjusted the Uplift Machine Learning model logic to be compatible with the newly created measurement_granular_offering_text table.
2. Granular Table Engineering: Built the measurement_granular_offering_text table, preserving the original measurement logic while deepening the granularity down to the offering_text level.
3. Offer Remapping & Reconciliation: 
a. Corrected and remapped the offers within the offers_purchases table to prevent any revenue discrepancies and ensure an exact match in the final output.
b. Reviewed the category and SKU mapping logic, including the use of offering_bng, offer_config_table_csv_ingest, v_offering_to_category_mapping, and SKU_MAPPING_ACROSS_TIERS_BNG, and identified some mappings that may need further validation.
4. Revenue Data Quality: Investigated changes in the obr_total_revenue table across Delta versions and confirmed that historical revenue values appear to be changing for completed sailings, raising traceability concerns. In several cases, the data seems to be duplicated. Also found discrepancies between the new associated table for revenue and the older one.
5. Application UI Expansion: Developed two additional tabs in the new data ingestion application to complete the migration of the legacy SharePoint templates.
6. Edge Case Investigation & Escalation: Investigated specific anomalies (Art/Park West offers for the 6/2/2026 sailing, missing art categories, and the SM 'Salmon Gravlax & Avocado Toast Class') and escalated the findings to the business stakeholders so they can adjust their source tables.
7. Attribution Base Layer: Constructed the pre_granular table to accurately map sales attribution across test, control, and organic segments, serving as the foundational foundation for the final granular measurement table. 
8. Pipeline Delay Diagnosis (generate_pdfs): Investigated the execution delay in the generate_pdfs run and traced the root cause to SharePoint image ingestion errors, confirming that the underlying offer data and proportions are structurally correct.

**Mert:**

**MIAP**

Completed a pilot for MIAP real-time data streaming (Ram’s Dream Engine) to Azure PostgreSQL as an in-house alternative to Databricks Lakebase. Achieved 0.8 to 1.2 seconds ship-to-cloud data stream latency (including Starlink delays).

Developed the MIAP Calculation Engine Python package for real-time data enrichment (machine learning predictions, physics calculations, and other custom logic). This shared library is used by both the real-time calculation engine (Azure Container App, pure Python) and Databricks (Spark). The approach enables continuous real-time processing from raw PostgreSQL MIAP data streams, writing results back to PostgreSQL to support real-time visualizations in the MIAP app. On the Databricks side, it supports continuous batch ingestion with backup coverage for satellite outages.

Developed a hashing algorithm to enable automated Databricks backfilling for the real-time calculation engine, allowing reprocessing of all gold table records when input formulas or data change, significantly improving recalculation efficiency.

Created Azure resources and repositories for the IBP API and app, and completed preparation of the IBP GitHub ecosystem. Currently preparing the IBP API and app for Azure deployment.

Enhanced Project TIDE mockups based on IBP team requests.

Finalized hiring of a local Asset Management Data Scientist contractor to support AMOS and Asset Management initiatives, accelerating M&T IBP efforts.

Met with the GMO PMO team to support development of an AI agent for CAR memo review and drafting.

Met with GMO Riding Team leaders to develop a riding team assignment optimization framework.

**Ram:**

**MIAP**

Implemented code for inclinometer data conversion.

Implemented real-time streaming in the marine package and deployed it to the master branch.

Refactored streaming code in the marine package to support batch backfill processing.

Working on integrating streaming changes into the Dev MIAP app.

**Reza:**

**MIAP**

Prepared scripts for per-class tuning of the fuel forecast project and delivered them to the team’s data analyst.

**Mahshad:**

**MIAP**

Completed the COP model for individual chillers.

Integrated COP into the HVAC agent.

Added location data to MIAP app plots for improved analysis.

Implemented location-based analysis within the HVAC agent.

Included chiller inlet and outlet temperatures in both the MIAP app and HVAC agent.

Added TCV valve analysis to the HVAC agent.

HVAC agent is approximately 90% complete, with accurate analysis results.

~100 kW savings identified for MA AHUs.

~200 kW savings identified for SM AHUs.

Additional ~100 kW savings opportunity identified for SM AHUs in the cabin area.

**Arya:**

**MIAP**

SORA is in good shape and expected to enter QA (with form entry) next week.

Uploaded a new vector AI index for safety narratives.

Creating a validation dataset for KPI definitions.

Made minor improvements to fleet tracking.

**Will:**

MIAP

Started work refactoring power plant figures in the webapp

Created version 5 of the CAC model that integrated 9 more ships

Fixed bug that was preventing lt whr tags from loading

Refactored power plant features so that it conforms to PEP 8 and improve the efficiency by reducing the number of .withColumn calls

created smoke tests for power plant features to ensure stability

Fixed major bugs in fresh water analytics

Doug B.

Revenue Management: CEL

**CEL | T4 Testing Updates | JUNE**

**Status**: This ticket was completed on Jun 12, 2026

**Deliverables**:

Celebrity T4 test: updated monitoring metrics and notebooks. Test continues as planned.
Six sailing clusters removed due to changes in sailing status or low booking volume.

**Delays**: None.

**Potential future issue**: None.

**DUAL | Category Gapping Handoff & Support | JUNE**

Configuration review:
1. Requested confirmation on use of widgets to configure job runs.
2. Recommended update for setting run environment. Code was using outdate methodology tied to workspace ID.
3. Requested confirmation on whether RCI GTY category XI on Icon-class ships needs to be considered in gap modeling.

**RCG | Operations Support | JUNE**

In progress

Lamis

Revenue Management: CEL

**1. Realistic Weekly Demand Bounds Refinement (CEL)**

Besides capturing how demand comes with respect to the WTS, I enhanced the existing methodology to reflect the booking patterns for wave and non-wave periods by performing stratified sampling prior to calculating the percentile-based upper and lower bounds. At the sailing-cco level this has improved the bookings pattern and ensures that it resembles the real case scenario. Originally, we could have cases where the bounds would allow more bookings in non-wave periods. This is handled in the newly proposed approach. It has been discussed and presented to CEL SHs and they align with this approach.

**2****.  Dynamic**** Price Caps Adjustment** (Based on CEL SH feedback)

Revised the logic to go down to the RDSS product code level and fall-back to the meta level to capture different pricing strategies specifically for Europe

**3****.  CEL**** Price Optimization**

Started Integrating the new Demand Forecast data into the price optimization logic. This includes validation of the new model results, transforming the format of the data in accordance to the optimization, generate dashboard to visualize and validate the demand curves and troubleshooting those curves, adapting the optimization code to align with the new df raw data - This is a WIP

Michelle

CEL Rev Management

**DUAL | Prepare codebase for production**

I unified the residual modeling workflow and Category Gapping pipeline by removing duplication between doubles (D) and quads (Q) and consolidating them into a single, parameter-driven pipeline. Previously separate datasets and notebooks were audited line by line to distinguish true business/modeling differences from unintentional duplication, enabling shared logic while maintaining correct occupancy-specific inputs.

The structure of the logic—combining weighted moving average residuals with fallback layers (grouped residuals and 6-month averages)—remains consistent, with only table inputs and key behavioral differences parameterized (e.g., bookability filters, GTY occupancy constraints, category exclusions, and pricing calculations). This ensures consistent fallback hierarchy, reduces divergence risk, and makes the pipeline easier to reason about, test, and extend.

I standardized the shared data construction layer (availability features, booking/VCAP logic, joins to pricing and metadata tables) to be occupancy-agnostic, ensuring both models operate on identical underlying data definitions. Occupancy-specific logic is now handled in a lightweight second layer, including filtering, pricing differences, and residual selection.

Pricing differences were preserved but isolated: doubles rely on per-person pricing (price_01), while quads construct cabin-level pricing using price_01 and price_04. This separation confines complexity while keeping the rest of the transformations shared.

In addition, I improved code quality and production readiness by removing redundant operations (e.g., duplicate joins), fixing subtle boolean logic issues, enforcing null-safe and deterministic calculations, and aligning window definitions and feature engineering for reproducibility.

Overall, this transforms a duplicated, multi-notebook workflow into a cleaner two-layer, parameterized architecture that is production-ready—reducing maintenance burden, improving consistency and robustness, and providing a clearer foundation for future enhancements and handoff.

**CEL | GTY-Lead 3.0 JUNE**

Met with CEL team, they requested additional sailing level examples to explain project to product teams. I had provided example illustrating the steps and formulas of the optimization, however they would also like to illustrate the differences in inventory and how this affects recommendations.

Anneke

SSC Rev Mgmt
Update Jun 17, 2026:

**Featurestore**** Fixes**

Over the last few days I investigated a data quality issue in the feature store where booked position and load factor were underreported versus stakeholder views.
Root cause was in the daily bookings pipeline: capacity scaffold generation used a hard-coded fare code list, and downstream left joins excluded valid bookings for fare codes not in that list, causing data loss in final aggregates.

Implemented fixes:

Replaced hard-coded fare codes with dynamically sourced fare codes so all valid booking records are represented.

Applied performance optimizations to offset the additional compute from dynamic fare expansion, including query plan simplification and tighter temporal filtering.

Updated downstream booked position handling to ensure capacity logic remains correct for null/blank category scenarios.

Current status:

Results now align with expected stakeholder reporting.

Final validation is in progress today.

Production deployment will follow completion of testing.

**Performance Visibility and Revenue Tracking Framework**

I have been conducting EDA to develop a track variance metric for Silversea that will work with the low-volume tracks and actuals. WMAPE and WRMSE on a week-by-week basis severely penalize low booking periods so I am looking at doing a 5-week rolling window. I continue to develop this track variance tracking framework.

Neila

RCI/CEL Rev Mgmt:

**Data: Reconcile EXISTING Corporate Strategy data - Own Data - Part 1**

continuing to align internal data - meeting with stakeholders on Jun 16, 2027 confirmed that TUI should be considered competitor and yield should be ntr/apd based on cruise days not BIMA deployment days.
Team would like to see yield yoy with premiumization and without.

Srilekha

CEL Rev Mgmt

**CEL | Validating PRE OUTPUT FILE**

Integrated the new model’s elasticities and generated a final output file for Monica (Celebrity) to validate. While reviewing the output, noticed that short Caribbean far-out sailings were showing the same elasticity value of -0.5 across the board — a cap applied in the existing business rules.

Identified the root cause as expected model behavior, not a data quality issue. In the far-out booking window, most customers aren’t shopping yet, so the model correctly predicts zero demand response for those sailings — but this zero prediction causes a divide-by-zero when calculating elasticity, resulting in a null value.

Discussed with Evan how these null values should be handled going forward. His initial thought was that since the model shows no demand response, the elasticity should be set close to zero (e.g., -0.1) to reflect that lack of sensitivity. However, since elasticity sits in the denominator of the price formula, capping at a value close to zero actually produces a larger, more aggressive price move — not a smaller one as the reasoning might suggest. This would misrepresent sailings with no real demand signal as needing a steep price change, so we agreed to avoid this approach.

Added the y_pred column to the final pricing output file so the Celebrity team can see why a large share of sailings show a clipped, least-negative elasticity value. This happens when no demand signal exists to predict from (y_pred = 0), meaning that elasticity number isn’t a true reflection of price-demand sensitivity for that sailing — it’s just the fallback. Agreed for now to cap elasticity between -0.25 (max, least negative) and -5 (min, most negative). Re-ran the file with this change and sent the updated output to Monica for validation

Lance

**CEL Rev ****Mgmt****: ****Dual | Model Performance Metrics**

**Validate and test the model grading framework**

Metrics match business needs on historical data and can accurately separate good and bad sailings correctly through the metrics. Celebrity team gave positive feedback and accepted the new framework.

**CEL | Demand Model Health Check Dashboard**

CEL team had positive feedback and accepted new proposed tolerance-based metrics like weighted tolerance ratio, tolerance ratio, and hit rate. Demoed the dashboard to them and got positive feedback on that too.
**Next steps:**
- add historic pricing to dashboard
- automate data updating (not just local file)

Dashboard created for Celebrity. Shows bookings over time for both the previous and new model, as well as average bookings over WTS. Includes fully functioning filters for brand, ship class, ship code, meta, cat class, and others. Shows down to individual sailing-cat level for deeper analysis. Includes scorecards for key metrics like weighted tolerance ratio, hit rate, median tolerance ratio, MAE (< 10 bkgs), and MAPE (> 10 bkgs). Also includes top contributors to weighted error for quick identification of worst performances by the model. Metrics have been tested and confirmed to accurately score the model performance based on the business needs. The multiple views over time and over WTS help identify drift and mistakes by the model.
Very positive feedback from Celebrity team about the mew metrics and dashboard with no pushback.
**Next steps:**

Add RCI data (1 pt)

Add elasticity tab (reliant on model changes)

Add selection for bkgs versus pax, selection for occupancy level, and pricing view (1 pt)

Feedback loop with RCI team

Aagam S.

**PCP Pricing Automation**

**CRF Automation | Other Products [Refreshment, Soda, Water, Cul Exp, Lunch, Dinner, AAT, UDP, Internet]**

This week I completed the CRF automation for the following products:

Internet (1 device, 2 devices, 3 devices and 4 devices)

refereshment

soda

water

refreshment & 10 drinks deluxe

your choice

night package

UDP

AAT

The Key

Ignacio V.

PCP Pricing Automation

**Optimize & fine-tune final Feature Store for CEL Beverage**

Worked on finetuning and optimizing the code for creation of the granular and huge dataset for CEL Beverage PRE (includes clickstream data). This involved adding in strategic optimization of how the data is created and stored (incremental load code set up, checkpointing, intermediate table delta saves, and liquid clustering). In addition, a new version of doing it an aggregated weekly level instead is also being tried, as this will certainly run faster and may possibly work better than the daily level data (this is something that can be tested to choose a winner, but the weekly aggregation surely has the advantage of faster runtime). Lastly, it is part of the plan to attempt changing this process into pure SQL (no more spark) in order to use a medium SQL warehouse to see how that can improve the runtime drastically. Once a v1 of the Featrue Store can be saved and validated, the plan would be to expand the amount of data to include even more historical data and move it on to the model training.**
Enhance opportunity cost penalty model by shifting to Causal Inference model**

Worked on setting up the code for a future enhancement (once the v1 of the is completely tested) of the opportunity cost model for far-out discounts. This primarily involved using Causal inference models, including EconML DML, EconML CausalForest, and a CausalML UpliftTreeClassifier. The code was set up to try creating this model and combining their usefulness for adding in a far out discount penalty (which can cause cannibalization) into the optimization routine.

Set up Claude Code on VS code, including also integrating with databricks

Anand S.

PCP Pricing Automation

**Web Scraping Pipeline (Celebrity) — Near Production Ready**
Completed a full-scale run scraping **184K products across 579 sailings and 13 ships**, with all data quality checks passing and results successfully stored. The pipeline is now stable after addressing fleet scope gaps, performance slowdowns, and improving failure visibility. Runtime has been reduced from ~19 hours to an expected ~2.5 hours with optimized compute. One minor fix remains before finalizing.
**Status:** One clean end-to-end run away from scheduling as a recurring production job.

**2. PCP Promotion Recommendation Pipeline — First End-to-End Run Delivered**
Successfully migrated and executed the promotion recommendation pipeline in Databricks, producing **233K recommendations across 29 ships and 534 future sailings**. Output is now scoped to active ShoreX products, improving relevance. Results have been validated with no quality issues identified.
**Next steps:** finalize minor edge cases and begin stakeholder review with Revenue Management.

**Upcoming Next Week:**

Resolve remaining Celebrity scraping gaps (including spa category) and promote pipeline to full production scheduling

Explore PRE implementation for major OBR/PCP products

Present cancel/rebook EDA to Celebrity business stakeholders

Continue ZH01 significance testing toward consolidated stakeholder update

Evan M.

RCI/CEL Rev Mgmt

Demand Model

Diagnosed issues with elasticity and demand curves
**Value add: We know why the curves looked off and have a clear path to fix them**

Elasticity was reading weaker than it should, the curves were too flat to trust for pricing

Traced it to price moving with demand in the historical data, which masks the true response

Confirmed the cause with a set of diagnostic tests rather than guessing

Fix is in progress, **Lamis** is reviewing the corrected curves as they come through

Kept the production pipeline stable and improved accuracy
**Value ****add****: Forecast refreshes run clean and on schedule**

Cleared the deployment issues from the earlier runs

Made the feature refresh incremental so it updates faster without a full reload

Added new features and capabilities, tested out better monotonic solutions

Improved accuracy with new features and tested different methods of loss regressors

Standard Format / Presentation

Worked and added a method to automatically create portals (used in demand) and presentation slides in HTML

**Value ****add****: Reduction of time needed on ****powerpoints**** and presentation development**

Standardized a format and method that allows for quick automatic creation of a html presentation format matching RC slides

Modified a script that allows for quick dashboard creation given static datasets
