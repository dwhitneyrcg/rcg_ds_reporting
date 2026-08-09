Erick Alfaro, David M, Osvaldo V, Danusio G, Cristian V

## MyCruise Recommender

*Personalized post-booking recommendations (excursions, dining, spa) powering the ForYou surface in the app.*

### Recommender Pipeline / ALS _(David M., queued for Cristian's review)_

- **Build Metrics Notebook** _(David M., Completed)_: Last week's MLflow metrics notebook is finished — binary and weighted metrics with logging, on branch `feature/dm-improve-foryou-recommendations`. In Cristian's review queue alongside the rest of the recommender workstreams.

- **Explore ALS Model Improvements** _(David M., Completed)_: Broader-exploration task formally closed. David, Cristian, and Erick aligned that recommender optimization beyond the metrics notebook sits with Cristian; David focuses on clustering integration + propensity once Cristian completes the review.

- **Integrate Propensity Models** _(David M., new)_: Two propensity models are in flight (Carlos, Glen Erik). Open design question — combine at the re-ranking layer — staged for Cristian's review and held until clustering improvements land first.

### Product Clustering _(Osvaldo V., queued for Cristian's review)_

- **Last week's "converged at 9.9% disagreement" has now translated into a measurable lift in the offline backtest.** Composite score on the backtest moved from a ~0.05 baseline to ~0.5 with the new product clusters — roughly **10x** — using the novelty + serendipity + weighted-recall metric. 38 GPT-5-Nano categories. Online/production validation is still pending integration; the offline result is what's ready for Cristian's review.

- **Anand getting up to speed as an additional contributor.** Osvaldo walked Anand through the clustering approach and ALS training on 5/12; Anand is exploring parameter improvements as a contributor to the broader recommender effort.

### Guest Segmentation / Clustering Selection _(Danusio G., queued for Cristian's review)_

- **Cluster-count breakthrough** _(Danusio G.)_: The metric used to pick optimal cluster count was switched to prioritize **homogeneity** instead of overall quality — for 7N Caribbean, the optimal count auto-jumped from **3 → 89** with no business input. The target range for clusters is 10–15 segments; Danusio is tuning the 5-metric weights to land in that range before the larger backtests run.

- **LLM Explainability Layer for Clusters** _(Danusio G.)_: New persona-storytelling layer feeds cluster centroids to an LLM (GPT-5 Nano) to produce business-readable cluster descriptions. First version delivered. Next move: generate LLM descriptions for the 89-cluster output to see how narratives shift from 3 → 89.

- **Hybrid Feature Approach for Clustering** _(Danusio G., Completed)_: Loyalty and passenger count are now pinned as mandatory cluster features; RF importance can pruned the remaining features. Last week's memory issues were resolved via a 500K-booking sample stratified by meta-product × brand.

- **Does guest segmentation actually help the recommender?** _(Danusio G.)_: Last week's offline backtest (1,000 bookings) showed recommender quality is better when the new guest clusters are used than when they aren't — the first head-to-head evidence that segmentation adds value. The larger offline backtest at 100,000 bookings is queued behind the cluster-count tuning above; online/production validation still pending integration.

### Apriori / Royal Beach Club _(Rodrigo B., queued for Cristian's review)_

- **Investigate Royal Beach Club Product Recommendations**: Pre-compute extending Cristian's recommendations table is built (schema: card + predictions, minimal compute time). Root cause is lack of historical interaction data; resolution will combine a network-graph model with hard-coded slot reservation. Cards-without-coverage handling is on Cristian's review agenda; Rodrigo will also walk him through the work directly.

### ETL Infrastructure _(Osvaldo V.)_

- **Investigate Failing GraphQL ShoreX Product Detail Job** _(Osvaldo V.)_: MCR ETL has been failing for 5–6 weeks with a "No objects… that can cat name" error. Endpoint appears live and not expired. Erick pointed Osvaldo to the correct entrypoint — the `001 MCR ETL GraphQL` job notebook (not the core GraphQL notebook) with `product_category` as a parameter. Plan is a precise single-sailing analysis to isolate which categories work/fail, not the full multi-hour loop.

Erick Alfaro, David M, Osvaldo V, Danusio G, Cristian V

## Project Axiom — Voice 360

*Insight extraction from unstructured customer feedback (Medallia, Guest Logs, Qualtrics) via LLM pipelines — feeds emails, dashboards, drivers analysis, and chat.*

### Email Reports

**Port Email** _(Rodrigo B.)_

- **Latest version is "our best report yet."** Roatan baseline-entry corrected, OSAT rescaled to 1–100, improvement labels reworded, star-indicator drivers, max-8-word solutions, prompt tightened to drop intro framing, and port-scope re-scoped so per-port commentary only counts comments that mention the port.

- **New track — model upgrade** _(Rodrigo B.)_: Anne Marie's review flagged hallucinated weather, wrong-port attribution, and food-quality phrasing. Plan is to upgrade the model (gpt-5.2 or 5-mini) to improve reasoning; cost is a non-issue since this runs quarterly.

**Royal Santorini Beach Club Email** _(Rodrigo B.)_

- **Layout finalized.** Per-route metrics table with brand-specific chips, route-by-route columns, and a composite-across-routes column is in. Two-week lag is partially implemented (one week for now — data window is still insufficient for the full two). Awaiting scheduled send to stakeholders.

**Shorex GSO Safety Email** _(Danusio G.)_

- **Last week's Phase 2 cost optimization is now live.** Pipeline is running end-to-end for both Shorex and GSO after redeploy of the `gpt-5-mini-safety` model. Duplication bug that was driving Eduardo's ~10x runtime/cost spike was found and fixed — current state is ~5x with expanded filters, validated over the next two weeks. **GSO PR is in Erick's review queue.**

**Silversea Email Reports** _(Erick A.)_

- 39-topic final-email infrastructure in place; comment trend-line graphs added; KPI composite tuned (Restaurant Service 95 → 93.5); Ray-report mention-counts bug fixed. Open: LTR removal, STLY column, Promoter/Neutral/Detractor breakdown, and a reconciliation call on composite-score discrepancies that suggest not all component questions are being included.

### Meta Data Framework

- **Asset Bundles Setup** _(David M.)_: Setup complete end-to-end in develop. Email failure notifications wired (David, Erick, shared mailbox); 2-worker cluster with 5-minute auto-termination; README at repo root. PR is coming to Erick for divisions-aspect-only enablement (bullet-points and open-ended remain off until the batch lands). Next step is GitHub Actions / Databricks secrets per environment, which sits with Escobar.

- **Bullet Points — Replicate Medallia Prompt** _(David M.)_: Bridging last week's "topic update kicked off" — topic list is now finalized, duplicate-request bug found and fixed, and **batch processing started 2026-05-12 for Jan 2025 forward.** Open-ended pipeline is downstream of this completing.

### Target Setting _(Erick A.)_

- **Last week's v1 model has now been deployed as a pipeline (2026-05-11)** extending the Target Setting framework beyond NPS / rebook to include onboard revenue targets for Track (Hotel Operations planning). Data shape unchanged: one row per ship + sail date + market, with revenue split by category (Internet, Shorex, Dining, etc.). v1 forecasts total revenue per category. MAPEs: **Internet sub-20, Dining sub-20, Shorex 30–40.** Market-level forecasts remain deferred. Next: business review.

### Webapp — Cluster Visibility on 3D Ship Model _(Rodrigo B., new)_

- The 3D ship explorer's deck plans, room alignment, and ship shape are correct; the clustering layer overlaid on the model is currently uninterpretable. Rodrigo is picking up Erick's clustering code to make the visualization business-functional.

### Stakeholder ask — Celebrity Operations Analysis _(Osvaldo V., new)_

- Celebrity has requested dry-dock-style operations / service analysis for **Xcel** (Nov 25, 2025 – Apr 26, 2026 sailings) and **Silhouette** (Dec 27, 2025 – Apr 26, 2026). Pipeline reuse: existing dry-dock LLM topic-extraction → operational themes → summary report. Erick handing off code and report template.

Erick A.

Contact Center

### Infrastructure — CCAS Missing Table

- **Reverse-engineer missing `CCAS.EDA Booking-Parsed 2024` table** _(Erick A. + Osvaldo V., new)_: Two-track investigation to recover the missing 2024 table from the existing 2026 notebook so Osvaldo's time-to-topic baseline can run.

Erick A.

PROJECT AXIOM:

## NEW: Project Scraping

*Cross-brand initiative to build a unified scraping platform serving Consumer Insights, Hotel Operations, Product, and Social Media across Royal Caribbean and Celebrity. Replaces team-by-team one-off crawlers with a single ingestion pipeline. **Phase 1** targets review/forum sources (Booking.com, Cruise Critic, Reddit, RC blogs) → SharePoint. **Phase 2** tackles social platforms (TikTok, YouTube, Twitter/X). **Phase 3** builds a stakeholder dashboard and LLM agent over the scraped corpus.*

### Scoping

- **Scope Market Trends Sources for Enterprise Distribution** _(Danusio G.)_: Identify the website set that would power an "ultimate" internal Market Trends report for Enterprise Distribution. Output is the input list for per-source scraping. Danusio using Perplexity for discovery; Erick has pre-identified Booking.com, Cruise Critic, Reddit, RC blogs, TikTok (Rapid API), and YouTube as Phase 1–2 candidates.

### Phase 1 — Review & Forum Sources _(Danusio G., all Not Started)_

- **Scrape Booking.com Reviews**: Two-stage pipeline (enumerate ship/product URLs → scrape reviews).

- **Scrape Cruise Critic Forums**: Two-stage pipeline (enumerate forum thread URLs by cruise line/ship/itinerary → scrape full threads with posts, replies, dates, authors). Erick has prior code to share.

- **Scrape Reddit Cruise Subreddits**: Coverage across r/royalcaribbean, r/cruise, r/cruises. Decision pending on API (PRAW / Pushshift) vs. unauthenticated.

- **Scrape Royal Caribbean Blogs and Forums**: Long-form guest commentary on RC fan blogs (e.g., RoyalCaribbeanBlog.com).

### Phase 2 — Social Platforms

- **Evaluate TikTok Scraper API Quality** _(Danusio G.)_: Testing a Rapid API TikTok endpoint (free tier: 300 requests/month). Go/no-go on coverage, fidelity, rate limits, and pricing before requesting a paid subscription. Danusio has prior YouTube scraping experience that should transfer.

Erick Alfaro

PROJECT AXIOM:

## NEW: Project Concept Testing Lab

*Agent-persona framework using LLM-driven synthetic respondents to A/B test ideas, concepts, and content variants (subject lines, marketing copy, product positioning) **before** committing to live tests. Built on TinyTroupe (Microsoft OSS persona-simulation library) plus an existing internal persona codebase. Stakeholders: Marketing, Consumer Insights, Social Media.*

- **Explore TinyTroupe** _(Osvaldo V.)_: Prototype a minimal end-to-end persona evaluation (define persona → run single concept eval → inspect output), locate the existing internal persona codebase, and sketch how the two compose.

Erick A., Osvaldo V., Rodrigo B.

## Contact Center

### Siren — Time-to-Topic Analysis _(Osvaldo V.)_

- EDA on **how many days prior to sail date** guests call about each topic — the goal is to measure the cadence of specific topics (e.g. how many days before sailing guests typically call about Dining, Shorex, etc.) so the company has a high-level estimate of when calls for each topic are expected and can send pre-emptive emails to head off the call. **Active focus: reproduce the 2024 baseline first** (filters: brand, channel, call type, intent → percentiles of days-prior-to-sail-date) before iterating on the 2026 version. Reconfirmed 2026-05-14.

### IVR Survey Topic Extraction _(Rodrigo B.)_

- **Last week's "project restarted after October pause" is now into active execution.** Data-extraction issues resolved; dataset available in Databricks. Pivot from full common-labeling to **bullet-point extraction of complaints/issues only** for higher-signal output, reusing the Tips & Gratuities email template. One-time analysis from mid-March 2026 forward, aligned with Augusto's friction / abandoned-cart workstream.

Ben F., Nicolas T, Camila A.

IBP Supply Chain

**IBP Supply Chain delivered a strong week anchored by tangible Beyond Pilot momentum and structural platform modernization.** The Celebrity Beyond pilot continues to validate value creation, with ~$5K in weekly savings and leadership approval to expand to Summit and Alaska ships. The broader theme across all workstreams is a deliberate shift from fragile monolithic notebooks to modular, orchestrated pipelines—improving resilience (restartable stages), auditability (traceable data flows), and velocity (parallel development with AI-assisted workflows). This is foundational, enabling not just better engineering, but faster and more reliable business impact across Finance, Supply, and Marine.

**On the forecasting side, key capabilities moved from concept to measurable validation.** SSC V6, the next-generation supply forecast, is now production-ready in “shadow mode,” allowing direct head-to-head comparison against V5 using real data—closing the gap between research confidence and decision-grade proof. In parallel, Marine Consumables Gen1 was stood up as a new forecasting line of business, using the same architecture as RCI/CCI, bringing visibility and measurable performance to an area that historically lacked it. These advances are critical to expanding forecast accuracy measurement and economic impact beyond current domains.

**Refactor programs for Finance and Supply models continue progressing but remain gated by full parity validation.** Both pipelines have been successfully decomposed into modular stages (including 13-stage orchestration for Finance and multiple Step 1/Step 2 segments for Supply), with tooling now in place to detect row-level discrepancies vs. legacy monoliths. Several reconciliation issues have already been resolved, but neither system has yet achieved end-to-end validation against the legacy baseline, meaning monoliths remain the system of record. While the architecture is largely built, proving numerical equivalence is the key milestone required to unlock business adoption.

**Finally, enablement, visibility, and forward motion are aligning for scale.** The Beyond Pilot dashboard now has a functional local build and is moving toward Azure production deployment for executive consumption, while foundational improvements in tooling (AI onboarding workflows, job monitoring reliability) are sustaining development velocity. Additional contributions across IBP (pilot enhancements, Summit onboarding, Royal Beach Club modeling), Order Creation simplification, eCommerce data integrity fixes, workforce planning application progress, and CLV modeling reinforce strong cross-functional momentum. Near-term priorities center on V6 validation, Marine backtesting, dashboard productionization, and—most critically—closing parity gaps to fully transition from legacy monoliths to scalable, governed systems.

Ben F.

Supply Chain IBP

**## The Bigger Picture**

Had an outstanding SteerCo meeting with Keith, Evan, Hotel and Food operations for Celebirty Beyond pilot. Keith was very pleased with the good story we had to tell and are on track to save $5k on this week’s Beyond Sailing. Green light was given for pilot expansion to Summit and then shortly thereafter to other CEL Alaska ships.

Across all five workstreams this week, the through-line is the same: ****we are converting long-standing "monolith" code — single massive scripts that only one or two people in the company can safely change — into modular, orchestrated pipelines that the whole team can own, audit, and improve.****

That shift matters for three reasons:

1. ****Resilience.**** A modular pipeline that fails in step 7 of 13 can resume from step 7. The old monolith would have to re-run from the beginning, often costing hours of compute and delaying business reporting.

2. ****Auditability.**** Each module has a defined input, output, and contract. Finance, Supply, and Marine numbers can now be traced to a specific stage rather than a black-box script.

3. ****Velocity.**** Multiple people (and AI-augmented teammates) can safely work on different modules in parallel without stepping on each other.

The deliveries below should be read in that frame: most of what shipped this week is incremental progress on ****converting the supply chain's mission-critical models from monoliths into governed, modular systems**** — while also making the underlying forecasts more accurate.

**---**

**## Executive Summary**

A heavy delivery week, with progress on five fronts:

- ****SSC Forecasting (V6) — Next-generation supply forecast model**** moved from a research prototype into something we can safely run in production alongside today's model (V5) and judge head-to-head. The harness for that comparison is now in place.

- ****Marine Consumables Gen1 — New forecasting capability**** for marine consumables was stood up end-to-end on the same architectural pattern as our other forecasts. This opens marine as a measurable line of business, parallel to our Royal Caribbean and Celebrity supply forecasts.

- ****Finance Tool Refactor — In flight.**** Continued migration of the Finance Tracking Tool out of legacy monolith code into a 13-stage orchestrated pipeline. This week built the parity tooling and fixed several reconciliation issues on the SharePoint reporting stage. End-to-end data validation against the monolith baseline is ****not yet complete**** — the monolith remains the system of record until full parity is proven.

- ****Supply Model Refactor — In flight.**** Six new analytic segments built out across Step 1 and Step 2 of the modular Supply Model rewrite. The new code runs and produces outputs, but end-to-end data validation comparing the modular results to the legacy monolith is ****not yet complete**** — the monolith remains the system of record until parity is proven.

- ****Beyond Pilot Executive Dashboard — In flight.**** First working version of the executive-facing supply performance dashboard was built and is running locally; productionization on Azure Container Apps is the next milestone.

All code-side work landed on `master` and is running on production data.

Ben F., Camila A.,  Nicolas T.

IBP Supply Chain

**## SSC V6 — Hardening the Next-Generation Supply Forecast**

****What this is:**** SSC V6 is the next-generation version of our core supply chain forecast model — the model that predicts how much of each product each ship will consume on each voyage. V5 is in production today. V6 was a research artifact going into this week.

****What shipped:****

- The V6 model's curated feature set (118 features chosen by a rigorous selection process) was promoted into production storage. V6 now reads the same stable feature list every run, instead of recomputing it each time.

- Fixed a quiet data bug where two important demand signals — actual load factor and forecasted load factor — were being collapsed into a single value. Both signals now flow through cleanly.

- Fixed several deploy-time failures that were preventing V6 from running on the production cluster at all.

- Aligned training cutoff dates and feature-importance calculations to the actual pipeline-run date, so the dates on the output match what business stakeholders expect.

- Built "shadow mode" tooling — V6 and V5 can now be scored side-by-side on identical real data, with a standardized error metric (MdAPE), without contaminating today's production outputs.

****Why it matters:**** Until this week, we couldn't honestly tell leadership whether V6 was actually better than V5 — only that researchers thought it was. The shadow harness is the gate that turns "we believe V6 is better" into "we can prove it on a week of real data." That's the decision-quality threshold we need before recommending a model swap.

Ben F.

IBP Supply Chain

**## Marine Consumables Gen1 — Standing Up a New Forecast Line of Business**

****What this is:**** Royal Caribbean and Celebrity supply forecasts already exist. Marine — the consumables side of marine operations — did not have an equivalent production-grade forecast. This week we built one.

****What shipped:****

- A complete, end-to-end pipeline scaffold modeled after the proven Royal Caribbean / Celebrity architecture, but adapted to the per-ship, per-product cadence of marine operations.

- A modeling approach where each (ship, product) pair gets its own gradient-boosted regression — the same partitioning pattern that has worked well on the other brands.

- A cost-weighted, log-transformed loss function so the model optimizes for the way the business actually measures error (MdAPE), not a generic statistical metric.

- A multi-period feature selection pass that picks the right variables across multiple forecast horizons, with cost-aware weighting so high-value products drive the selection.

- A series of performance fixes so the full Marine training cycle finishes in a tractable window on the shared cluster (previously it would not complete).

- Tuned per-(ship, product) hyperparameters and a high-volume correction to fix systematic under-forecasting on the highest-volume pairs.

- Orchestrator integration, smoke tests, and Azure Data Factory environment wiring so Marine runs end-to-end like the rest of the portfolio.

****Why it matters:**** Marine is now a measurable forecast line of business on the same foundation as the rest of supply. That's the prerequisite for extending Beyond Pilot's economic measurement (forecast accuracy, realized savings, inventory impact) to Marine — historically the area with the least visibility.

Ben F., Camila A.,  Nicolas T.

IBP Supply Chain

**## Finance Tool Refactor — Monolith to Modular Pipeline (In Flight)**

****What this is:**** The Finance Tracking Tool is the system that translates supply forecasts into financial reporting (inventory valuation, spend impact, year-over-year reporting that surfaces in SharePoint for finance stakeholders). Historically it was a single monolithic notebook — change one line and the whole thing had to be retested. The team is migrating it into a 13-stage orchestrated pipeline ([Finance_Tool_Orchestrator.py](Visualization/Finance_Tool_Orchestrator.py)) where each stage has a defined contract, supports automatic resume on failure, and can be independently audited.

****What shipped this week (incremental progress, not completion):****

- Built a ****parity gate**** that compares the new pipeline's outputs to the legacy monolith baseline on every run and surfaces a row-level diff — so divergences become visible instead of silent.

- Fixed several causes of divergence on the SharePoint / Finance Tracking stage: misaligned archive unions, archive rows leaking into the wrong checkpoint, and a date-inheritance bug where child stages weren't picking up the right run date from the orchestrator.

- Added a monolith-snapshot helper and extended notebook timeouts to support cleaner side-by-side comparisons.

- Recorded the rerun evidence so the fix can be audited by finance.

****Status / what is NOT done:**** End-to-end data validation of the new pipeline against the legacy monolith is ****not yet complete****. We have the tooling to detect divergence and have fixed several specific divergences, but we have not yet certified that all 13 stages produce numbers that match the monolith across a full reporting cycle. ****The legacy monolith remains the system of record**** and continues to feed finance reporting. The refactored pipeline cannot replace it until parity is proven end-to-end.

****Why it matters:**** A modular finance pipeline is only valuable when its numbers provably match the legacy baseline. This week's work moves us toward that goal — the gate is in place, several known mismatches are resolved — but the trust threshold for retiring the monolith has not been met. Finishing that validation is the gating item for the refactor's business value.

Ben F., Camila A.,  Nicolas T.

IBP Supply Chain

**## Supply Model Refactor — Step 1 & Step 2 Segments (In Flight)**

****What this is:**** Parallel to the Finance refactor, the Supply Model is being broken out of its legacy monolith into well-defined stages. ****Step 1**** is the demand-side foundation — recognizing demand, valuing it, joining inventory state. ****Step 2**** decomposes that demand into analytically useful slices (by region, by lead time, by inventory state) so downstream consumers — dashboards, finance, realized-savings reports — can pull the view they need without rebuilding logic.

****What shipped this week — six segments built out in the modular pipeline:****

- ****Step 1 — "Before-supply value":**** the value of inventory at the moment demand is recognized, before any supply action is taken. This is the baseline number every supply intervention is measured against.

- ****Step 2 — Shipboard carryover:**** unconsumed inventory carrying forward from prior voyages. Critical for not double-counting demand.

- ****Step 2 — No-shipboard demand:**** demand on routes and products where shipboard inventory is not maintained — a fundamentally different supply pattern that previously got bundled into the same view.

- ****Step 2 — Voyage load lead-time:**** decomposes lead time at the voyage-load event level and emits a parseable monthly chain that downstream consumers can subscribe to directly.

- ****Step 2 — Sailing-date region segment:**** regional demand keyed to **sailing date** rather than order date — closer to how operations actually plans.

- ****Step 2 — Region demand pivot (two slices):**** pivoted regional demand views that feed the dashboard layer.

Each segment went through review, cleanup, and integration into the modular pipeline.

****Status / what is NOT done:**** End-to-end data validation comparing the new modular pipeline's outputs to the legacy Supply Model monolith is ****not yet complete****. The new segments run, produce outputs, and have been reviewed at the code level — but they have not been certified to reproduce the monolith's numbers across a full forecast cycle. ****The legacy Supply Model monolith remains the system of record**** and continues to feed downstream consumers (Finance, dashboards, planning). The modular pipeline cannot replace it until parity is demonstrated.

****Why it matters:**** Step 2 segmentation is code-complete — the analytic shapes (regional, lead-time-aware, inventory-state-aware demand views) now exist in the modular pipeline. But the work to **trust** those views as a drop-in replacement for the monolith is still ahead of us. Without that validation, downstream teams cannot safely cut over, and the refactor's value remains potential rather than realized. Finishing parity validation is the next milestone.

Ben F., Camila A.,  Nicolas T.

IBP Supply Chain

**## Beyond Pilot Executive Dashboard — In Flight**

****What this is:**** Beyond Pilot is the executive-facing program for measuring the supply chain's forecast accuracy and economic impact. The dashboard is its primary surface — the screen where leadership will see forecast vs. actual, realized savings, and inventory impact.

****Status:**** A first working version was built this week in Next.js with executive-friendly charting. It runs end-to-end locally against the production data layer.

****Not yet shipped:**** Productionization. The dashboard is ****not**** deployed for executive consumption yet. The next milestone is deploying it as an Azure Container App with the appropriate authentication (Entra ID), secret management, and custom domain wiring so leadership can access it from a stable URL.

****Why it matters:**** This is the surface that makes the rest of the work visible. The pipelines underneath are what produce the numbers; the dashboard is how leadership sees them. Productionizing it on Azure Container Apps is the gating item for stakeholder rollout.

Ben F., Camila A.,  Nicolas T.

IBP Supply Chain

**## Tooling & Team Enablement**

- ****Onboarding documentation for AI-augmented teammates**** — codified the workflows the team is using for AI-assisted development so the rest of the group can adopt the same pattern without a multi-week ramp.

- ****Hardened the Databricks job-monitoring polling loop**** — previously, transient network hiccups were occasionally being misread as run failures and triggering false retries. Now real failures are distinguished from transient ones.

****Why it matters:**** These are unglamorous but compounding. Better tooling and onboarding is how we keep the velocity of the past two weeks sustainable, not exceptional.

Ben F., Camila A.,  Nicolas T.

IBP Supply Chain

**## Looking Ahead — Next Week**

- ****V6 vs. V5 shadow scoring**** — first real read on whether the next-generation forecast delivers measurable accuracy lift on a week of production data.

- ****Marine Gen1**** — first full backtest cycle now that the pipeline is end-to-end runnable; this is where we find out whether the model architecture transfers cleanly from RCI/CCI to Marine.

- ****Beyond Pilot dashboard**** — Azure Container App productionization (Bicep template, ACR, Key Vault, custom domain, Entra ID auth) so the dashboard can move from "running locally" to "available to leadership."

- ****Finance Tool refactor**** — drive end-to-end parity validation against the legacy monolith using the gate built this week; resolve each divergence stage-by-stage until the new pipeline is certified as a drop-in equivalent.

- ****Supply Model refactor**** — begin systematic parity validation of the new Step 1 & Step 2 segments against the legacy Supply Model monolith; the segments exist, but until they reconcile, downstream consumers cannot cut over.

**# Risks / Watch Items**

- ****V6 vs. V5 decision**** depends on shadow-mode results landing cleanly next week. The harness is in place; we now need a clean week of data through it.

- ****Marine Gen1**** is brand-new code on the shared cluster — the first full week of production runs is the real test. Smoke tests and per-period caps reduce but do not eliminate compute-budget risk.

- ****Beyond Pilot productionization**** has dependencies on Azure infra access (Container Apps environment, ACR, Key Vault, Entra ID app registration). Pulling these in early reduces risk of slipping the stakeholder rollout.

- ****Finance & Supply refactors remain unvalidated.**** Both refactors are code-progressing but ****not yet certified against the legacy monoliths.**** Until end-to-end parity is proven, the monoliths must remain the systems of record. The risk is not that the code is wrong — it is that "looks right" is not the same as "matches the baseline," and only the parity validation will tell us which divergences are bugs in the new code, defensible improvements, or hidden issues in the legacy monolith itself.

Camila A

IBP Supply Chain

**IBP – Camila:** 
Beyond Pilot:

Daily & Supply Breakdown:

Added ESG Alternative Items

Adjusted Holiday Predictions: when prediction is too high for passenger count, adjust the prediction based on the historical matched sailing with that similar passenger count (threshold is +-50 passengers to match to)

Added fallback to sister ship when product on current ship (Beyond) does not have enough history to create supply ratio

Using live finance file to adjust predictions higher than budget to be at least $17k less. This is a safety net but we do expect the model to correct itself when getting closer to the sailing with the high prediction

Freeze PCD when the sailing begins so that any update by revenue team does not change the prediction given on the first day of the sailing.

Consolidated table:

Freeze ongoing sailing prediction so that when the pipeline updates, we do not adjust the prediction already given to the ship.

Royal Beach Club (NAS):

Developing demand forecast model

Developing guest forecast model

To enhance on the models itself due to lack of history, I will use CocoCay shore excursions data to help as features for each model (consumption and guest based)

I need to prioritize guest model so that I can fix the issue where we don't have enough PCP and Onboard Revenue data for future sailings within 2026. This will also allow me to get the GUESTS and FCST_GUESTS to normalize consumption and create the features for demand forecast model.

I would also like to explore "New Destinations" transfer model. The idea is to use NAS and also ships itineraries where they visit the new destination. Santorini is already getting picked up in PCP data so this gives possibly some ground to cover and can allow a head start for Puerto Costa Maya once launched

Summit Pilot:

Adjusting all code to ensure we are including Summit. Working on a more automative way where instead of modifying all the files each time a new ship is introduced to the pilot, we only need to edit one line instead and manually add the ship code there.

**Nico T**

**IBP – Nico:** 
**RCI/CCI HF&B Order Creation Dashboard MLS Discrepancies**

· In Progress · Highest

**Completed:**

**Aligned on simplified validation approach with Ben & Paolo (Thu 5/8)**: After a meeting with Ben and Paolo, agreed that Paolo had already validated voyages across qa and legacy for Feb–Dec 2026 sailings (with two exceptions). Realized the prior comparison was being run against the wrong legacy table (prd_silver.ibp.master_load_schedule instead of prd_silver.shipfin.rcg_mls_out_t) and began correcting the notebook code.

**Branch reset & AI-assisted table swap (Sun 5/11)**: Erased all prior branch work that had become overcomplicated, reset the file to master, and used a prompted Copilot approach to systematically swap prd_silver.shipfin.rcg_mls_out_t → qa_gold.ibp.rcg_master_load_schedule while suffixing all checkpoint tables with QA_MLS_SWITCH. Built a separate comparison notebook using row-level hashes. Executed 250/272 cells, then discovered the notebook wasn't accounting for internal read→write dependencies (Table1V2 written, but Table1V1 still read downstream).

**Row-level hash comparison results (Mon 5/12)**: Initial results showed low match percentages across intermediary tables. Identified nuances: time/batch-related fields may cause legitimate differences, tables written before the swap point (Cell 35) should match but don't, and a 0.01% match on one table is likely an implementation error. Flagged open questions (why some tables are 100% match, why the final table matches despite lower upstream matches).

**Deep-dive into **mls_with_catalyst validation (Tue 5/13): Documented the full construction pipeline for the mls_with_catalyst table, tracing through mls_max_batch_date → out_voyages → mls_voyage_starts → voyage_no_lookup → profile → mls_with_catalyst_voyage. Filtered comparisons at two date thresholds:

**≥ 2026-02-01**: 183 Voyage_Nos missing from QA switch, 4 missing from base

**≥ 2026-03-01**: 22 missing from QA switch, 4 missing from base

**Decision to remove MLS Lookup logic entirely (Wed 5/14)**: After a morning meeting, the team agreed that since the Order_Creation_Notebook has no historical data dependencies and all current/future data is post-Catalyst, the MLS Voyage Lookup logic (CRUISE_NUMBER → VOYAGE_NO lookups across pre/post-Catalyst MLS) can be **removed entirely**. Plan:

Merge master into MLS Discrepancies branch

Copy the notebook and replace MLS Lookup logic with the pre-Catalyst version (sent by Camila, also in Visualization/RCI_CCI_ORDER_CREATION_BEFORE_CATALYST_REF.py)

Replace all qa_gold.ibp.rcg_mls_out_t references with Paolo's qa_gold.ibp.rcg_master_load_schedule

Rename suffix to NO_MLS_VN_LOOKUP

**Ran NO_MLS_VN_LOOKUP comparison (Wed 5/14)**: Integrated the changes and ran the comparison. Key findings:

mls_with_catalyst has **no downstream table dependents**, making its comparison unnecessary

The MLS Voyage Lookup removal erased the mls_with_catalyst table write (as expected)

Proceeding to validate the next four direct consumers of qa_gold.ibp.rcg_master_load_schedule: cruise_profile_data_before_join_to_mls, market_master_with_master_load_schedule (×2 schemas), and Order_Creation_After_Total_Days

**Ongoing:**

**Validating downstream table comparisons**: Running through the four remaining table comparisons to confirm the simplified (no-MLS-lookup) approach produces equivalent or improved results.

**Carlos A.**

**E-Commerce: Carlos:**

- Added historical saving of quarterly scores to models inference pipeline, and bug fix related to saving location.

- Evaluated performance of journey assignment model, .

- Added journey stage computing to journey scoring inference. (In dev and for RCI only, planning to move to production during next weeks)

- Fixed data leakage bug related to latest ingested journey class data.

Carlos A

**Loyalty: Carlos:**

Loyalty Simulator Enhancements:

- fix bugs related to newest loyalty category introduced (dtype unmatching)

- Ran 4 simulations for period 2026-2029, 2 pendings. This will help to evaluate better logic and parameters for final simulator.

Bao

**E-Commerce; Bao:** 
**Completed This Week**

**App Feature Temporal Ordering Improvement**

Identified a potential data leakage risk in the app usage feature pipeline (etl/feat_eng_features.py)

Risk: return_date was used as the activity window anchor, but max_hit_date can occur days or months after voyage return, which could allow post-voyage app activity to bleed into the pre-label training window

Improvement: replaced the anchor with greatest(return_date, max_hit_date) as a guardrail to ensure the window is always anchored to the latest possible date, preventing any future leakage risk

Code committed to bl/develop; a retrain of BP PG models is pending to confirm there is no meaningful metric impact

**Journey Cluster Feature Leakage Research**

Audited etl/build_journey_clusters.py for data leakage risks and identified two distinct issues

Issue 1 (population leakage): the clustering population is filtered to consumers who confirmed a brand booking on or after 2024-01-01, meaning every consumer with a cluster assignment is by definition a booker. Non-bookers carry a null cluster label. This directly encodes the target variable into the feature

Issue 2 (sequence leakage): journey sequences used to fit the KMeans model are truncated at the BOOKING event itself, so cluster geometry is defined by paths that end in a conversion

Both issues must be resolved before cluster features can be used safely in production models

**CS Feature Integration Decision (Closed)**

Expanded the clickstream EDA from 6 to 16 feature candidates across 5 behavioral dimensions

Results in a CS-only context: +3.2% AUC for PR, +4.0% AUC for PG

Decision: gains are not expected to be additive in the full 200-feature model and do not justify the pipeline infrastructure cost of a new data source

**Feature Visibility Dashboard (Initial Build)**

Built a dedicated Databricks dashboard to centralize visibility into the model feature landscape

Surfaces feature importance scores, active features per model, and cross-run stability

Addresses a key pain point: because dynamic feature selection varies the active feature set by model and run, there was no single place to audit feature usage across all 48 models

**Ongoing**

**App feature retrain**: retrain BP PG models with the temporal ordering fix applied and confirm there is no meaningful metric shift from the baseline

**Feature importance dashboard**: continued development and refinement of dashboard views and model coverage

**New feature ingestion validation**: validating ingestion results for newly added features and confirming that their importance rankings are directionally sensible

**Disparate impact audit**: finalizing the audit notebook, identifying features of concern that may implicate the New York City Automated Employment Decision Tools law, and developing alternative feature transformations that preserve signal without violating fairness constraints

**CS feature library review**: coordinating with Carlos to evaluate whether the 16 proposed clickstream features are worth adding to the standard feature library for future use

Mirielle

Contact Center

**Workforce Planning: Mireille:**

**Data Quality Issues (Genesis Migration)**

Call-volume data may still be impacted by **incomplete or corrupted historical records** due to the ongoing Genesis migration. As a result, current forecasts could be unreliable.

**Next Steps**

Wait for full completion of the data migration before rerunning forecasts.

Update the **historical baseline datasets** for all markets once data stabilizes.

Plan a **full re**-**validation and refresh** of International, Royal, and Celebrity forecasts after migration is complete.

**B. Workforce Planning — North America (Royal)**

**Advanced App Functionality: “Run Your Own FTE”**

**Status:** *Building — data ingestion nearing completion; model integration in progress*

This week focused on **advancing the application toward an end**-**to**-**end functional prototype**.

**1. Progress on Data Ingestion Pipeline**

Advanced development of the **Hourly Proportion** tab.

Progressed the **FTE Inputs** (data join layer) to consolidate all required datasets.

Continued structuring data flows to ensure clean integration across tabs.

**Why it matters:** 
Moves the app closer to a fully connected data pipeline where all inputs required for headcount modeling are available in one place.

**2. Erlang A Model Integration (In Progress)**

Tested the **1**-**hour Service**-**Level–based Erlang A model** within the app.

Validated input/output transformations between the UI and model layer.

Ensured compatibility with aggregated **weekly and monthly outputs**.

**Why it matters:** 
This is the core step enabling users to **trigger headcount calculations directly from the app**.

**3. Dataset & Function Validation**

Validated core datasets:

Office hours

Input assumptions

Adjusted forecast

Continued testing helper functions (load, save, join, engine wrapper).

**Why it matters:** 
Ensures data reliability and prevents downstream errors during model execution.

**Where We Are**

**Next Steps**

Finalize end-to-end app testing.

Complete validation of the **1**-**hour Service**-**Level Erlang model**.

Execute the first **full end**-**to**-**end app run**.

Prepare for a **POC demonstration with stakeholders**.

Build datasets and functions for **30**-**minute interval models**.

Integrate 30-minute Erlang variants.

Test and validate 30-minute model outputs.

**Summary**

This week focused on **strengthening application robustness** and advancing the Royal **“Run Your Own FTE”** feature toward a functional prototype. Progress was made on data ingestion, dataset validation, and Erlang model integration, bringing the app closer to enabling **self**-**service headcount simulation**. In parallel, call-volume forecasting remains on hold pending completion of the Genesis data migration to ensure future outputs are accurate and reliable.

**Caleb**

**CLV:**

**In Progress**

Validating newly refreshed VCAP stage tables specifically curated for CLV

Including detailed checks on channel mix, PCDs, pax, and NTR

Going through every Customer360 table in order to identify relevant and sufficient cols to include in our CLV final table

**Completed**

Engaged with Corporate Planning to develop a deeper understanding of RCG's cost of acquisition methodology, with the goal of being able to reproduce the process with SG&A dollar magnitudes for each step.

Created a detailed questionnaire for allocation process creators addressing all ambiguities needed (with screenshot references to sourced material)

Created Sankey diagrams to visualize the full allocation process

Mert E. and David W.

NewBuild

Met with the Newbuild teams this week and discussed progress of AI Observatory and reviewed Newbuild progress, as well as planned a CAR.

**Overview Session**

The Newbuild overview session grounded the AI strategy in a clear understanding of a highly complex, multi-year (~5-year) ship development process that is both structured and deeply iterative. While the lifecycle follows defined phases—Pre-Concept, Concept, Global and Local Design, Detail Design, and Production—the execution is highly parallelized and heavily driven by design cycles, with each venue requiring dozens of meetings (12–15 core plus ~20 prep) and multiple coarse-to-fine iterations. The process is Miami-centric for early design, with shipyards and vendors taking over in later stages, and relies on Workfront for project tracking and SharePoint for documentation. However, data and documentation practices remain inconsistent, especially in Newbuild vs. the more mature Fleet Modernization process, creating fragmentation and limiting visibility.

The session converged on a pragmatic, bottom-up AI approach focused on solving real pain points rather than attempting a top-down transformation. The highest-value opportunities identified were compressing design iteration cycles (biggest ROI), automating repeatable deliverables (e.g., contracts, briefs, business cases), and capturing meeting-driven knowledge—recognized as the primary source of project intelligence yet largely unstructured today. This supports a longer-term vision of an Enterprise Observatory, integrating Workfront, SharePoint, and meeting transcripts into a unified knowledge layer enabling AI-driven reporting, decision support, and process acceleration. The agreed path forward is to prioritize and cluster 30–40 existing use cases, engage directly with business owners, and deliver incremental, high-impact solutions—starting with simple, repeatable problems and scaling toward more advanced AI capabilities over time.

**CAR Planning Session**

- **AI Enterprise Observatory Initiative:** David, Joseph, and other team members discussed the development of the AI Enterprise Observatory, focusing on consolidating unstructured data, building a central knowledge repository, and leveraging generative AI to enhance decision-making and operational efficiency.

- **Team Structure and Resource Planning:** The participants, including David and Joseph, reviewed the proposed team structure for the observatory project, discussing the roles of core and scaling teams, the need for dedicated senior talent, and strategies for balancing internal and contractor resources.

- **Financial Planning and Capitalization Strategy:** David and Joseph explored the financial aspects of the project, including budgeting, cost uncertainties related to AI usage, and the complexities of capitalizing project expenses within the organization's accounting framework.

- **AI Implementation and Use Case Development:** The team discussed the practical aspects of implementing AI solutions, including the process for developing use cases, lessons learned from pilots, and strategies for balancing automation with critical thinking.

- **Technical Approaches and Tooling:** David and others discussed the technical methods and tools used for AI development, including prompt engineering, leveraging different AI platforms, and the importance of structuring unstructured data for effective AI application.

- **Follow-up tasks****:**

- **Finance and Accounting Alignment: **Connect Joseph with the finance team to review and clarify capitalizable versus non-capitalizable elements for the CAR and ensure proper financial modeling and accounting treatment. (David, Joseph)

- **Capital Planning Coordination: **Draft a skeleton CAR including the manager role and coordinate with capital planning to explore funding options and prepare for capital allocation discussions. (David)

- **Vision Data Integration: **Talk to Mert to scope the integration of Vision data into the AI Enterprise Observatory and assess the feasibility of including historical and current data. (David)

- **Resource Planning for Core Team: **Evaluate the need for a dedicated FTE or manager-level resource to support the project and adjust the resource plan accordingly. (David, the team)

- **Cost Monitoring and Optimization: **Monitor and optimize software and cloud infrastructure costs during the pilot phase, especially regarding token usage and evolving vendor pricing models. (David, the team)

Mert E and David W.

Met with the Brand Deployment and Revenue Planning Deployment teams and discussed the deployment optimization roadmap.

The session with Liz Oates and Josh Carroll’s team aligned both the business and AI organizations around a unified vision for transforming deployment planning into a scalable, optimization-driven capability. At the core is the shift from manual, slow scenario evaluation toward automated generation and optimization of itineraries that maximize NIY while respecting operational constraints (ports, regulations, contractual commitments). To enable this, the group agreed on a single, centralized deployment platform (e.g., deployment.rccl.com) with shared data, reusable code, and governed architecture—avoiding fragmented solutions and ensuring enterprise scale. Roles are clearly defined: the AI/Data team will own backend infrastructure, data integration, and governance, while business teams will own the front-end workflows and decision experience.

A critical unlock identified is the data foundation—historically fragmented across revenue forecasting, expense modeling, and operational constraints—which has limited the ability to make fast, centralized decisions. Current efforts (e.g., Alex leading expense-side data integration, consolidation of forecast references, and tools like the port vetting tracker) are focused on bringing these datasets together into a unified, automated pipeline. This enables micro-level decisions (e.g., port feasibility, timing, cost inputs) to inform macro deployment outcomes. The delivery approach will be incremental and modular, starting with micro-capabilities such as digital twin modeling, time optimization logic, and constraint integration, then scaling toward full fleet optimization over time. Net, the effort represents a foundational step-change—from siloed, manual planning to an integrated, AI-enabled system capable of rapidly evaluating and optimizing deployment decisions at scale.

**Key Risks & Dependencies (Deployment Optimization)**

**Data fragmentation (primary dependency):** Revenue forecasts, expense models (EPM/Catalyst), and port/berth constraints remain siloed and inconsistently structured. This is the single largest gating factor to scaling scenario generation and optimization.

**Manual input dependency on Rev Mgmt / Ops:** Current workflows still require manual data pulls for each scenario, limiting speed, repeatability, and auditability.

**Platform alignment risk:** Without strict adherence to a **single centralized deployment app**, there is risk of duplicate / fragmented builds across teams (Dan/Alex, Ben/Mahshad), reducing enterprise leverage.

**Model complexity vs. delivery risk:** Jumping too quickly to full optimization (vs. incremental “micro capabilities”) could delay value delivery and increase execution risk.

**Data automation maturity (expense-side especially):** Expense forecasting automation is still in progress (Alex leading), creating imbalance between revenue and cost inputs required for full NIY optimization.

**Port feasibility & constraint quality:** Tools like the port vetting tracker (Jake) are critical—micro-level accuracy directly impacts macro optimization outcomes; incomplete/low-quality constraints will degrade model quality.

**Cross-functional dependency risk:** Strong reliance on multiple stakeholders (Rev Mgmt, Ops, Decarb, Finance) creates coordination overhead and potential delays without a clear operating model.

**Governance & security dependencies:** Centralized platform requires alignment with AI, data, and cyber governance; delays here can slow deployment of shared infrastructure.

**Immediate Next Steps & Owners**

**Stand up centralized deployment platform (repo + environment baseline)**
*Owner: AI/Data team (Mert, David) with Dan/Alex, Ben/Mahshad alignment*

**Unify core datasets (revenue + expense + constraints)**
*Owner: Alex (expense-side), Ben/Mahshad (integration), Data Engineering support*

**Define “single source of truth” for forecast + plan inputs**
*Owner: Ben/Mahshad + Rev Mgmt partners*

**Package current prototypes into reusable modules (digital twin, time logic, constraints)**
*Owner: Dan/Alex (core modeling), AI/Data team support*

**Establish cross-functional working team cadence and structure**
*Owner: Liz Oates / Josh Carroll leadership, with David + Mert coordination*

**Prioritize initial modeling scope (e.g., single ship class + single season)**
*Owner: Deployment business leads (Josh’s team) + AI/Data team*

**Formalize port constraint inputs (port vetting tracker integration)**
*Owner: Jake + Ops stakeholders*

**Define automation pathway for scenario-level forecasting (remove manual Rev Mgmt dependency)**
*Owner: AI/Data + Rev Mgmt partnership (Ben/Mahshad lead integration)*

**Executive Bottom Line****: **The success of the deployment optimization initiative is less about the optimization model itself and more about **data integration + platform standardization**. Immediate progress depends on unifying datasets, enforcing a single platform, and delivering modular capabilities quickly—before scaling toward full fleet optimization.

**Mert:**

**MIAP**

Fully completed migration of all 15 repos of MIAP from Azure DevOps to the new Alpha GitHub Organization. Established reusable pipeline templates for Container Apps, Python Packages, and Databricks that will establish the basis for the rest of the AI team. Resolved newly found cybersecurity vulnerabilities after integration with Orca Container Scan.

Met with Marine Technical SVP Brian Sorensen and reviewed his demand for live Asset Management KPI dashboards. We agreed to start developing these live dashboards on the MIAP App upon hiring of the new Sr. Data Scientist, which we are actively seeking.

Developed new dynamic models for Power Plant Steam Turbines with improved accuracy.

**Will:**

**MIAP**

Identified an issue in the legs table causing cascading issues in the FACTS SSC Digital Twin pipeline.

Built analysis tools for exploring results data for the FACTS SSC Digital Twin pipeline.

Built an analysis tool to visualize itinerary vs. FACTS actual deployment data.

Built an analysis tool to visualize FACTS model features.

Created a FACTS finance comparison notebook to finish the FACTS pipeline; now working on improving models and fixing data issues causing errors.

**Ram:**

**MIAP**

Connected with Captain Henrick and did an initial analysis on the POLARIS database.

Identified that ship-level tags are required from vendors and need to be added to the configuration to proceed further.

Investigated null body issues and made progress toward resolving them.

Created a new Postgres database for real-time testing, implemented all required functionalities, and converted the table into a hypertable.

With Wesley's support, updated the Crosser flow to enable data flow into the new table.

Coordinated with the platform team to set up a scheduled cron job to automatically delete records older than 26 hours.

**Mahshad:**

**Deployment**

Worked on deployment and added the required deployment configurations.

Fixed template issues and aligned them with the other MIAP applications.

Resolved access issues for tables, notebooks, and clusters related to deployment.

After migrating to GitHub, started adding files and addressing security vulnerabilities.

**Mahshad:**

**MIAP**

Attempted to schedule a meeting with the SC engineering team. Over the past couple of months, there were issues with most of the TCV valve sensors, which are now resolved. We are trying to understand the root cause and what led to the resolution.

Sent an email to OV regarding a recent anomaly in the DD. They indicated that AHU filters need to be replaced and a PO is required.

Also contacted an AN engineer regarding a 500 kW anomaly on the chiller and AHUs. They suggested it might be related to relocation. The investigation is ongoing, and we will follow up with the ship once more information is available.

**Arya:**

**MIAP**

Worked on improving the quality of the MIAP Fleet Tracker:

Using ArcGIS maps and other feature layers.

Added more customizability (draggable menus, auto-scaling to webpage size, etc.).

Improved the coordinate-pulling algorithm.

Currently researching other weather feature layers to add.

Pushing for a production release this week for the securities team.

Fixed minor bugs on the MIAP app and energy savings features.

**Reza:**

**MIAP**

Completed the Fuel Forecast (F1.0) for 2025 and 2026. Prepared results and comparison charts, and delivered them — along with separate source CSV files at the datetime, leg, and sailing levels — to the Fuel Finance team for further analysis.

Continued work on improving scrubber models.

Developing a proof of concept for the residual boosting distributor function (currently using a sigmoid function) to optimize performance, particularly in areas with step-function-like behavior (e.g., STG engines, scrubbers).

Maintaining service power area models and baselines.

Collaborating with a data scientist on the team to address fuel forecast issues for Silversea ships using FACTS data.

Attended a meeting with the SVP of Marine Technology.

Ayon G.

WOW Update 5/14:

**MDR Interport – Development Progress:**
Completed **ETL and POS orchestrator** for MDR Interport. The **guardrail orchestrator is currently in unit testing**, with next steps focused on completing the **rules engine** and integrating it into the **MDR regular pipeline**.

**Windjammer Pipeline Modernization:**
Development is in progress to **refactor and align the Windjammer pipeline** with the MDR architecture. This includes introducing a **JSON****-based parameter dictionary** to manage **ship****-specific cutoff dates**, enabling seamless joining of **historical (Q****-Control)** and **future (CrunchTime)** data without code changes.

**Operational Support:**
Resolved multiple **ServiceNow tickets related to forecast variance** across several ships, ensuring stability and continuity in forecasting outputs across the fleet.

**Team Enablement & Knowledge Sharing:**
Created and presented a **WOW project deck** to the Data Science team, improving visibility, alignment, and knowledge sharing on key innovations and progress.

Evan McFall

RCI Rev Mgmt: Demand Model

Created elasticity framework and evaluated at different levels of LAF / D price changes

Explored model weights and determined approach to ensure price features were not overweighted but reflective

Finalized structure of output for PRE model integration and wrote test instances to UC

Worked with Lamis to meet isotonic expectations of elasticity and consistency

Constrained model to ensure it meets these requirements

Worked on model accuracy and added quad forecasting capabilities

Compared against existing model runs and aggregated metrics for doubles and quads

Explored marketing data and built initial queries around promotions and email campaigns aligning them with sailing dates

Lamis A.

CEL Revenue Management

**Lamis – This Week’s Update (Key Points)**

**Scaling model validation:** She is running the model across the **entire fleet (vs. sample cases)** to assess overall performance and support 2027 deployment workstreams.

**Model refinement:** Actively **adding new constraints** into the model based on stakeholder feedback (notably from Anastasia and team).

**Output improvements:** Working on **integrating error metrics directly into the baseline model outputs**, improving usability and interpretability.

**Validation quality focus:** Continuing to **pressure-test price-demand relationships**, raising concerns about feature design (e.g., multiple price signals, lagged bookings bias) and ensuring the model reflects realistic elasticity behavior—not just optimizing prediction metrics.

**Trajectory of improvement:** Noted that **model performance is improving (curves now responsive vs. previously flat in 3.0)**, but still not at target quality—focus remains on building trust in outputs.

**Next milestone:** Planning to **review results mid-next week once full-fleet runs and updates are complete**, rather than sharing partial outputs.

**Executive Read**

Lamis is driving **core model validation and credibility** work right now—moving from sample-based testing to full-fleet evaluation, tightening constraints, and ensuring the elasticity logic reflects how the business actually expects demand to behave. The emphasis is less on incremental accuracy gains and more on **trustworthiness and interpretability of price-demand relationships**, which remains the key gating factor before broader deployment.

David W.

RCI and CEL Revenue management:

Met with RCI and CEL stakeholders this week on planning out demand forecasting deliverables in May.

- CEL Stakeholder Meeting: We will be updated PRE elasticity model by end of May that accounts for recent trends and historical information, and then will deliver a slimmed down model without recent trends for use in Track Optimization. The team also aligned on next steps for Category Gapping 3.0 and Track Optimization.

- PRE Meeting: The path to 100% PRE approval is focused on improving model accuracy, simplifying pricing logic, and increasing responsiveness to true customer demand. Key efforts include enhancing demand forecasting (including WTD considerations and expansion across all products), track optimization, and completing the quad rework by end of June (shifting management to cat-class level and fixing occupancy split and off-peak quad issues). On the rules side, there is active refinement of PRE business logic (dynamic caps, inversion rules, and use of actual price paid), with a proposal to eliminate fixed inversion gaps between cabin categories and instead allow demand signals to drive pricing more fluidly across categories. The core debate centers on how aggressively to manage pricing across categories—balancing the need to stimulate weaker segments without disrupting premium demand. The emerging direction is to allow downward adjustments where needed, but avoid suppressing higher-category demand. Leaders emphasized simplifying rule structures (e.g., managing to adjacent categories rather than large gaps), focusing on real paid price signals, and creating practical, scalable rules that align pricing with observed booking gaps while maintaining flexibility for different demand scenarios.

Jesse B.

SSC Rev Mgmt

**Upper Suite EDA **– I performed several new EDAs this week concerning how to properly price upper-level suites. In these EDA, I distinguished top and bottom-tier upper-level suites, as well as passengers who bought upper-level suites and those that upgraded their suites after purchase. These EDAs will inform the foundation of the pricing upper-level suite pricing strategy.

**Top-tier pricing algorithm **- I have devised an algorithm for pricing top-tier upper-level suites. This algorithm requires grouping the top cabin categories into one category for pricing purposes, while preserving category gaps between them. The algorithm will raise prices based on booked position benchmarks; but will involve a lower LAF for top-tier upper-level suites to entice price-elastic passengers to buy these suites at the beginning of a sailing season, rather than up-trading later. Next week, I will utilize the upper-level suite EDA (item 1) to inform the input values for this algorithm.

**ANNEKE**

**SSC PRE | PRE Tracking Dashboard**

Closeout Statement:

This ticket was completed on May 11, 2026

Silversea PRE tracking dashboard has been shared with the stakeholders with great reception. Stakehodler will use this dashboard to understand how PRE is being used, when it is violating business rules, how often we are approving PRE recommendations, and why.

Link to dashboard:

The dashboard features pages for Total Recs, Actioned Recs and why, and t-test results for the A-B tests done for the first 4 areas.

**SSC PRE | Incorporate SSC Promotions into PRE**

Update May 13, 2026:

Currently testing post-promotional price enhancement in QA.

Work done includes:

Added querying task to existing ssc pre job to process promo-pricing table into format that could be joined into the pre input table

Added discount and post-promotional price to input table

Changed target for pre algorithm to include post-promotional price instead of price_dbl from pricing featurestore table

Made edits to pause file to include new post-promotional price column as well as free-text pause reason description.

Srilekha

CEL Rev Mgmt:

**CEL Europe Actual Price Paid Analysis**

Received request from Celebrity / Europe Product team to evaluate effectiveness of exciting deals, focusing on weekly % gty -lead gap, % trade-up, and price point impact on demand (GTY vs PHYS)

Pulled and validated pricing data from promotion_daily_snapshot (promo) and pricing_daily_snapshot (baseline), and cross-verified with AS400 to ensure price calculation accuracy

Built a week-over-week dataset (since Feb) capturing GTY and Lead pricing, booking splits, and promotion impact at a weekly level

Calculated pre-promo and post-promo GTY vs Lead price gaps, establishing that gty-lead gap before excited deals is stable ( aprox10%) across all weeks

Observed that post-promo gap increases significantly (up to ~30–60%) due to exciting deals applied on gty , showing strong pricing gap impact

Incorporated weekly minimum price points for GTY and Lead cabins to identify which price levels are actively driving demand

Found that as the post-promo gty-lead gap increases for GTY cabins, GTY bookings rise significantly, while trade-up % declines and PHYS bookings weaken, indicating that demand shifts toward lower-priced GTY due to higher gty-lead gap after exciting deals

Delivered week over week plots and a detailed dataset to Monica, clearly highlighting the price points and gap % after exciting deals that are driving volume. Monica will review these insights with the Europe Product team and follow up with feedback..csv&action=default&mobileredirect=true)

**Build Separate Promo Action Recommendation Process for Analyst Review**

The Celebrity Pricing team shared analyst decision driven exciting deals promo recommendations for the current week in a manually curated Excel file. These recommendations are based on analyst judgment, and the goal is to validate how many cases our decision framework—based on best-performing SPI booked position, and non-exciting vs exciting price bands—aligns with or differs from these analyst recommendations which are driven by business intuition.

Ingested and processed analyst-provided Excel file, which is manually maintained and not in a standardized format

Transformed semi-structured data (pricing, cabins, taxes, currencies) into a clean and structured dataset suitable for analysis

Standardized data into Spark for consistent downstream processing

Ensured correct mapping of promo prices, and cabin-level details

Prepared the dataset to support actual price paid analysis decision framework

Next steps :Will perform analysis to compare decision framework exciting deals promo directionality recommendations vs analyst-selected promos, and evaluate whether the promos are necessary

Will generate insights on pricing and demand behavior for these sailings to identify alignment or gaps between data-driven recommendations and analyst decisions.csv&action=default&mobileredirect=true)

Ignacio V.

PCP Pricing Automation

**Fix edge case failure for uploading copy of Sharepoint sheet of uploaded promos to historical table**
• A batch of promos uploaded through automation raised an edge case failure of the process of saving a copy of the Sharepoint sheet of uploaded promos to the historical table for purposes of copy/paste reference for future promo creations in a more efficient manner. The promos uploaded, but the saving of the promos to the table failed. The changes were made for the edge case to work successfully. In addition, some of the cabin class codes provided to me from the CEL team were not compatible in the Hybris system, so these codes were removed from the encoded mappings of codes for each cabin class.
**Finalize Feature Store tables using Transactional & NEW clickstream data from Digital**
• Worked on organizing the transactional side of the data to be used in the MNL model driven CEL Beverage PRE/DM
**Fix the list of mapped cabin class codes used in Sharepoint sheet for CEL promo uploads**
• The cabin class conditions needed to be adjusted for the CEL SharePoint sheet for promo automation. The codes associated with each cabin class were adjusted and corrected for. In addition, the cabin classes F, B & C were separated into their own selections and mappings rather than having the 3 different balcony cabin classes grouped together. These changes were made available to the CEL team already on the sheet.**
Recurring Business Meetings & OBR DS Meetings**
• A couple meetings were had with Keivn for brainstorming the CEL Beverage PRE/DM gameplan & strategy involving very granular & guest level clickstream data.
• A meeting was had with the SH of CEL (Rafa, Alex, and Gaby) for presenting the rollout plan for the CEL Beverage PRE/DM moving forward, in a step-by-step process.
• A meeting was had with some of those from the RCI side discussing CRF automation tied to the promo automation feature that has already been developed.
• Meeting had with digital BI team for further discussion behinf the targeted 1:1 offers as well as the clickstream data desired for behavioral data/features for PRE/DM modeling

Aagam

PCP Pricing Automation

**RCI | PCP2 | Conversion based PRE v2**

This week, I shared my results with the business and received approval on both the logic and the outcomes. In parallel, I worked on expanding the conversion-based recommendation framework for both RBC Passes and Beverage Package products for RCI.

I am currently waiting on the track-based recommendations for RBC Passes and Beverage Packages to obtain the corresponding recommended discount outputs.

Additionally, as a follow-up, I created a summary table highlighting the differences between the track-based recommendations and the conversion-based recommendations.

Anand

PCP Pricing Automation

**Web Price Scraping Pipeline — Production Finalization & Validation**

Completed the consolidated replacement pipeline and ran a full production-scale test: scraped 450,068 products across 14 categories, 30 ships, and 1,885 sailings (USD). Built automated data quality assertions (minimum product count, category coverage, null rate checks, worker error monitoring). Performed head-to-head validation against Andrew's production table — 30/30 ships match, 385,095 matched product records with 59.6% exact price match and 69.2% within $5. Differences traced to scrape-timing gaps and a single high-value suite product (Y933). Pipeline is end-to-end validated and ready for scheduled deployment.

**2. ShoreX Product Categorization — QA & EDA**

The LLM-based tour categorization pipeline has been completed. Now working on two fronts: (1) thorough QA/QC of the classification results to build confidence in downstream analysis, and (2) running EDA on the current categorization to understand the landscape — distribution across categories, revenue concentration by category, and identifying potential misclassifications or gaps.

Upcoming Next Week:

Deploy the web scraping pipeline as a single scheduled Databricks job (replacing Andrew's 29 notebooks)

Continue sailing clustering feature engineering with Aagam and Ignacio

Continue Celebrity ShoreX QA and categorization landscape analysis with Alex

Neila

RCI Rev Mgmt

Made a request to Dhanita and team for access to Marketing Data to understand the impact of external factors on demand + pricing.

MICHELLE M.

**Category-Gapping 3.0**

Implemented a production-safe, exact-match validation framework that ensures reduced-dimension choice models (LP, LU, UP, and GTY variants) remain mathematically consistent with their full-reference models (LUP/GLUP) by reconstructing implied shares from the full models (via renormalization to the relevant alternatives) and directly comparing those implied shares to the standalone model outputs on the specific business-required gap dimensions (e.g., lower_premium_gap_perc, lower_upper_gap_perc, upper_premium_gap_perc, plus GTY “laf” gaps where applicable). The suite surfaces both detailed and rollup diagnostics—max absolute deviation, configurable tolerance-based violation counts/rates, worst-case partitions, and explicit coverage gaps—so discrepancies become immediately visible and traceable without manual inspection of millions of rows. As the framework has been applied, model adjustments have materially reduced violations (e.g., UP reduced from ~45K to ~7K), and it formally satisfies the MVP requirement that UP/LUP/LP shares remain proportional at comparable gaps while supporting ongoing Category Gapping 3.0 iteration for CEL/RCI.
- Implemented a robust, exact match validation suite to verify consistency between our reduced dimension models (LP, LU, UP and GTY variants) and their full choice reference models (LUP, GLUP).
o Reconstructs implied shares from LUP / GLUP (e.g., LP shares implied from LUP lower+premium, LU from lower+upper, etc.).
o Compares these implied shares directly to the standalone LP / LU / UP / GTY model outputs.
o Computes detailed and summarized diagnostics:
§ max absolute deviation
§ violation counts and rates (configurable tolerance)
§ worst case partitions
§ explicit coverage gaps (unmatched points)
Validation rules required by business:
o LP df should be checked against LUP df where LUP shares are renormalized to only contain lower and premium. match only lower_premium_gap_perc.
o GLP df should be checked against GLUP df where GLUP shares are renormalized to only contain gty, lower and premium. match only laf_lower_gap_perc and lower_premium_gap_perc.
o LU df should be checked against LUP df where LUP shares are renormalized to only contain lower and upper. match only lower_upper_gap_perc.
o GLU df should be checked against GLUP df where GLUP shares are renormalized to only contain gty, lower and upper. match only laf_lower_gap_perc and lower_upper_gap_perc.
o UP df should be checked against LUP df where LUP shares are renormalized to only contain upper and premium. match only upper_premium_gap_perc.
o GUP df should be checked against GLUP df where GLUP shares are renormalized to only contain gty, upper and premium. match only laf_upper_gap_perc and upper_premium_gap_perc.
- This is important for the business because:
o it ensures consistency across all model variants
o makes discrepancies immediately visible and traceable to a specific gap dimension (avoids hours of manual digging through datasets with millions of rows)
o Provides a production safe regression check as we iterate on Category Gapping 3.0 logic for CEL / RCI.
- As I have been applying this framework, I’ve been making the necessary adjustments in the models to reduce the amount of row violations. For example, the UP model had about 45,000 violations and has now been reduced to about 7,000.
- This checks off the “UP, LUP, LP... shares are proportional to each other at similar gaps” requirement from the MVP list.

Kevin D., Ignacio V., Glen-Erik C.,

PCP Pricing Automation

- Ignacio is also advancing the CEL beverage PRE at a guest level through clickstream data integration.

- Glen-Erik is close to finalizing the targeted offers UI and added capability to automatically split test and control populations for measurement. GE provided control groups for the pilot but there seems to be no lift (tiny sample size). high level: conducting retrospective right now with all teams on targeted offers to identify path forward for all teams to scale and productionize.

- Kevin met with Jorge to walk through codebase for track based recommendations, adapting Jorge's alteryx workflow for limited products to a scalable solution that works for all products, including enhancements for historic sailing matching and integrating a dynamic track. There are a few updates needed to match the logic Jorge is using to identify the "optimal price". Kevin also advanced POC dilution models and demand forecast for beverage for both brands. This is an alternative approach to track based recommendations that will scale to all unconstrained inventory products. dilution model to be presented to brands next week.

David W.

HR

The demand forecasting CAR is being submitted in two weeks, along with 4 other CAM-related CARs and will be funded through allocations by IT. A sync meeting with Martha is occurring today.

David worked with Chiara to ensure 30k OPEX would go to AI Team and updated CAR for submission this week. Angela requested that John Makan be the CAR Manager and David will assist John with finances.

Glen-Erik

PCP (Glen-Erik)

PCP Pricing Automation

Targeted Offers Hub UI

Web / iOS / Android:

Added more validations (poke yokes)

Added automatic control group creation and tracking

Cleaned up UI making it more user friendly (less clutter)

Collected additional requirements for a separate Audience Creation Hub UI that creates audiences that can then be leveraged in the Targeted Offers Hub.

Presented the TO Hub UI to various stakeholders receiving positive feedback and excitement.

Web / iOS / Android:

New schema testing

Email:

Sent data to SFMC successfully in dev end to end. Minor format changes needed.

Eswar

RCI Revenue management (Eswar)

bronze_pricing_initial_load query drafted by a data scientist is taking 40hrs to run on a medium warehouse. Identified the odds in the queries and focusing on optimizing it currently.

Asset Bundles workflow deployment working session to new joinees in the team

Identified new active list of feature store tables which are active and provided to DE team

Validated feature store tables provided by DE team and providing my feedback to them.

Glen-Erik, Doug B., Santiago, and Javier

PROPEL:

Measurements: (Javier)

Enhanced measurement_granular, pre_granular, revenues, and offers_purchases pipelines to improve experimentation and uplift analytics.

Improved sailing departure datetime handling, UTC/local time alignment, and day_sail calculations using exact datetime differences.

Created production grade workflows and update logic for measurements process to move to production.

Investigated deployment blockers related to Terraform reconciliation and Databricks job ownership configuration. Spike

Spike: Offer Reduction over time: (Santiago)

Identification of the root cause of offer loss and initiation of variable standardization for the SKU table due to inconsistencies.

Developed PySpark code for assigned offer validation.

Scheduling table upgrade: (Santiago)

Correction of the scheduling table logic, protection of historical records through a proper merge strategy, and addition of documentation and comments.

Production & other issues: (Santiago & Javier)

Review and recovery of the development environment, which was down.

Investigated issues related to missing offer_config_id generation impacting downstream Assign Offer joins.

Debugged PySpark business-rule execution failures related to age restrictions, sailing filters, beverage-package exclusions, and empty sailing inputs.

Other projects:

Web scraping migration: (Eswar)

Optimized web scraping notebooks provided by hotel operations and made it to 1 single notebooks and bought down run time to 3hrs all together.

OBR migration: (Eswar)

Troubleshoot OBR oracle connection issues from prd workspace as DNS is blocking it. Fixed it with help of platform by enabling it.
