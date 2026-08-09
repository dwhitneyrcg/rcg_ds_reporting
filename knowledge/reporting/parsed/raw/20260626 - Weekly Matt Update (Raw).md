Ayon G.

**Win-on-Wastes**

**New Venues Added:**
Successfully onboarded three new venues: Wonderland (159), Railway (333), and Sichuan Red (213). Each venue had unique configurations in CrunchTime and QControl, which presented technical challenges during setup.

**Technical Implementation:**
Addressed and resolved differences in system configurations by carefully mapping recipes from legacy setups to the new structure. Ensured accurate data transition while preserving historical records.

**Data Migration:**
Completed end-to-end mapping of recipe data from old systems to new formats, maintaining integrity and continuity of historical data.

**New Ship Integration:**
Added a completely new ship build, **Legend of the Seas**, into the test environment. This required updates to filters and pipeline configurations to ensure the build is correctly isolated and tested specifically for the FPMS application.

**Mert**

**Newbuild**

Met with the RCI Private Destination Product team to understand their needs for the APEX Engine—an AI agent platform to provide executives with high-level insights and actions related to highly confidential private destinations. Agreed to partner with the ship product development team and seek support from Jay for a dedicated FTE Data Scientist to support both teams while preserving confidentiality.

**Mert**

**IBP: Risk Management**

Met with IT regarding Risk Management data integration. Agreed that Data & AI teams will take over data ingestion to the Alpha Platform, while IT will support any RPA needs for the Risk Management team.

Mert

MIAP
Finished deploying the IBP App and IBP Agent API with Active Directory sign-in, Orca/Snyk code scans, and now running on Azure Container Apps (dev-ibp.rccl.com).
Worked on improving the in-house RAG Python package and integrated Decarbonization SharePoint and HVAC documentation for agent usage.
Web-scraped the Chantiers de l’Atlantique website for all Oasis/Edge class ship document libraries, gathering metadata and URLs for all shipboard documents. This enables agents to easily download shipboard documentation and accelerates MIAP development work.
Improved thermodynamics formulas for Engine Charge Air Cooler fouling detection.
Completed the Python package for the MIAP Real-Time Calculation Engine using a Kafka + PostgreSQL + Container Apps hybrid approach to enable real-time enrichment of MIAP data. Ported all existing Databricks calculations for one ship to this framework. The package supports usage via either Databricks (Spark mode) or Container Apps. Achieved ~0.5 second lag for raw data and +1–2 seconds for enriched data.
Interviewing for a Data Scientist contractor.

Reza:
MIAP

Continued working on per-class fuel forecast final tuning and report deliverables, including:
Prepared scripts to compare OFB, incinerator, and thruster fuel consumption across ship classes to identify potential reference ships.
Added an intercept tuning option to the propulsion model to enable forecast adjustments.
Prepared per-class workflows to run historical data for residual boosting and generate the current F1.0 2026 forecast.
Attended a meeting with the team’s data analyst to collaborate on fuel forecasting.
Completed tuning for Quantum, Spectrum, Anthem, and Ovation; Odyssey will be completed next to finalize the Quantum class.
Participated in two interviews for Senior Data Scientist candidates.

Mahshad:
MIAP
Worked on understanding the energy recovery wheel from both mechanical and marine engineering perspectives.
Identified a formula suitable for ship data to calculate wheel efficiency.
Set up the workspace for Claude.
Analyzed potential savings in SM and identified an opportunity of approximately 100 W savings for the SM AHU.
Followed up with BY on an additional AHU energy-saving opportunity.
Currently working on MA chillers due to recent overconsumption.

Will:

MIAP
CAC (Charge-Air Cooler) — Pivot from v6 to New Approach
Decision (with Mert Ersoz):
The original CAC project on feature/charge_air_cooler became overly complex—incorporating multiple model levels, multi-signal fusion heuristics, consensus/sensitivity combinations, and common-mode environmental guards—making it fragile and unlikely to succeed in production. That approach has been scrapped.
Key changes in the new approach:
Per-engine and per-variant (engine-type) model combination—each engine has its own sensitivity model, complemented by a fleet-wide model across similar engine types for robustness.
Pivot from Random Forest to linear/ridge regression to improve interpretability (e.g., understanding how load, ambient temperature, and coolant inlet impact heat transfer), making the system explainable and auditable.
Simpler, feature-engineering-first design—CAC health variables are integrated into the existing power_plant_features pipeline rather than built as a standalone system.
Use of ΔT_LT (water-side temperature rise) as the primary fouling signal, normalized to standard operating conditions.
Work completed this week (feature/cac_feature_engineering):
Restructured power_plant_analytics/ into dedicated sfoc/ and cac/ sub-packages; moved legacy EDA assets to cac/eda/.
Added CAC health monitoring tags in configs.py (pressure, LT/HT temps, CAC outlet temp, inlet air temp, seawater temp, etc.).
Built CAC feature engineering logic in calc_power_plant_features.ipynb.
Added CAC smoke tests for temperature ranges, pressure, and delta validation.
Established miap-eda/CAC as the design reference (v8 plan + modular code structure).
Scrapped work (not carried forward):
Databricks workflow registration
Per-ship visualization and integrations
SMAPE accuracy tables and visualization fixes
Scheduling changes and documentation
Fresh Water Analytics — EVAP/RO & FW Figures
Populated missing RO_PLANT_INFO rows (9 entries) and EVAP_PLANT_INFO rows (47 entries across 24 ships).
Updated totals to 77 RO rows (previously 68) and 67 EVAP rows (previously 20).
miap-databricks:
Fixed NULL evaporator totals in FW generation calculations using COALESCE (~818k rows recovered).
Removed hardcoded ship lists in favor of generic column checks.
miap-app:
Corrected RO specific energy units (m³/kWh → kWh/m³).
Standardized evaporator units (kWh/m³ and °C).
Other fixes:
Fixed missing return in calc_ratio_pilot_fuel.
Improved handling of NULL evaporator totals in FW analytics.

Arya:
MIAP
Focused on digital twin QN class tuning.
Built a diagnostics notebook analyzing three data sources to determine optimal data usage.
Enabled detection of when a reference ship is required.
Developed a report generator for tuned digital twin ships for submission to the fuel finance team.
Improved propulsion linear regression model performance during maneuvering phases.

Ram:
MIAP
Worked on the real-time streaming job by renaming schemas, applying table properties, and scheduling cron jobs.
Started documentation for the MIAP DE process and building a knowledge base.
Identified cost optimization opportunities in VPS SFTP connections and engaged the VPS team for alternatives.
Improved monitoring to better distinguish issues between Crosser and Databricks pipelines.
Implemented version control improvements for configuration files and successfully deployed/tested them in QA.

Eswar

Revenue Management RCI & CEL

RMA (Eswar)

Fixed Oracle connection in pl_cel_track_fitgrp adf pipeline

Fixed TAP RCI GTY Lead pipeline fix which failed with latest code changes

Category Gapping pipeline fix, which failed due to data differences in dev/QA compared to prd

Fixed RCI Category gapping model training pipeline failure due to time constraints

GTY Lead, Category gapping Knowledge transfer sessions, code and workflow reviews as Michelle is leaving this week.

Monitoring CI/CD deployments, helping with PRs

ML Support in debugging issues and enabling fast development

Eswar

PCP Pricing Automation

Mass Offers: (Eswar)

Optimized feature engineering reducing runtime from 3 days to 3 hours for the query off of vcap daily snapshot that creates the final features for a model with clickstream data.

Glen-Erik C.

PCP Pricing Automation

Targeted Offers: (Glen-Erik)

Added ability to filter bookings by email reachability and app reachability. In other words, we only include bookings in which someone in the booking can be reachable in app and someone (else) via email. The entire booking gets the offer (with guest level exceptions like minors for bev, or Zennith Celebrity guests).

Launched POC3 with 4 products. Summary to be shared later today.

Celebrity

Beverage non-US (3045)

Beverage US (3005)

Royal

Beverage (3222)

Unlimited Dining (Y6OE)

Javier & Santiago

PROPEL CEL

Offer Template:

Pre-work:(Javier)

Synced code from prod to dev to allow for

Resolved a SharePoint PRD-to-DEV config sync issue, especially for the offer_config list.

Measurements: (Javier)

Created historical tables to support a POC model for more accurate purchase-versus-offer classification and prediction.

Designed an initial model architecture based on category-text features.

Defined new metrics to evaluate whether the proposed model improves functionality compared with the current approach.

Worked on assigning probabilities for all days when an offer was active, including cases where multiple days had associated offer probabilities.

Uplift Model Revenue Categorization: (Santiago)

Identification of 3,000 SKU inconsistency cases, correction of those inconsistencies, and grouping of records that were the same but differed in capitalization or characters.

Analysis of three different tables with various SKUs, unification of SKUs, offering_text, and obr_area, creation of a unique hash identifier for data uniqueness, creation of an outlier table for business review, connection to Databricks AI for quality control and semantic record assignment, and consolidation in dev_celobrbi_bu.propel_measurements.ai_product_classification_20260625

Mapping of non-matching obr_area values in uplift and offering_text, achieving matches across most categories, adapting the model for all ships, preparing the model for production, and correcting final details.

Bugs:

Continued working on the contamination issue related to test/control assignment at the cabin level. (Javier)

Ship Requests:

XC not showing Casino: Fix is almost in prod. Reconciliation with prod code necessary due to offer template code sync. (Santiago)

Art not showing on Edge: Art needs to be added in the quota file with a quota target by the OBR team. (Santiago / Garrett)

Salmon Gravlax needs to be removed. (Garrett)

PROPEL Configuration UI: (Santiago)

Inclusion of SQLite, and PostgreSQL for storing data coming from SharePoint tables.

Erick A & Cristian V.

**MyCruise**** Recommender**

*Personalized post-booking recommendations (excursions, dining, spa) powering the **ForYou** surface in the app.*

**Spotlight & Ranking Policies**

**Spotlight Control Panel Shipped** *(Erick A., Completed)*: Spotlight lets the business hand-pick products into the top recommendation slots for a specific sailing. Last week it was live on DEV and queued with Erick; this week he shipped it in the MyCruise control-panel web app — a simple CRUD panel (one row = one rule) that writes directly to a Unity Catalog table feeding the recommender, overriding the top two slots.

**Spotlight Governance Pushback** *(Cristian V. & Erick A.)*: In the stakeholder review, Taylor was uncomfortable with Spotlight being broadly accessible via the public web app. The team's position is that requiring sailing-by-sailing setup deliberately discourages indiscriminate overrides and keeps the model as the default, with the control panel as the official governance layer — to be revisited with Taylor. The team also aligned that the recommender should ultimately be judged on **net revenue**, and that static hard-coding must not contaminate the A/B tests that measure it.

**Ranking Policies Generalized** *(Cristian V.)*: A ranking policy is how the business tunes what the recommender optimizes for (e.g., margin vs. revenue). Cristian extended ranking-policy support from the Apriori model to the other models and, per Rosie's direction, the policy will now be set through a control panel rather than passed as an API parameter. The ranking-policy control panel is the next build, gated on Erick switching the MyCruise control panel to the production endpoint.

**Ensemble Pipeline & ALS Tuning**

**4U Model Integration & Expanded Training Window** *(Cristian V.)*: Building on last week's unified auto-retraining pipeline, Cristian nearly finished safely swapping the old models to the new "4U" versions and added a flexible training window — instead of a fixed 2-year history it can draw 3+ years, which materially helps under-represented segments (Celebrity and some Royal sailings with thin history). He also moved best-hyperparameter selection from David's holdout set to the test score for stability, and began logging all metrics/artifacts to MLflow.

**Recommender Visualization Playground** *(Cristian V.)*: To make the recommender legible to stakeholders (and double as a QA tool), Cristian built a mockup with persona/segment and product-cluster views, top component codes per persona, business-value metrics (avg margin/revenue/relevance per segment), recommendation-diversity views, and online precision/recall tracking over time. The goal is to integrate this visualization playground into an app that is shareable with stakeholders.

**A/B Testing & Cache Validation**

**Apigee↔Databricks**** Parity Check Scoped & Handed Off** *(Erick A. → **Danusio** G.)*: The recommender is served two ways — directly from Databricks and through the Apigee API gateway, which adds a caching layer that may silently drift. Erick wrote the full parity PRD plus a starter script (sample 500–1,000 payloads, fire both endpoints, diff and bucket mismatches across the prod ForYou/Naive/Apriori models) and handed it to Danusio.

**Infrastructure & Deployment**

**PCP Container-App Deploy Validated** *(Erick A.)*: Erick deployed a mock app end-to-end to both the QA and prod PCP container apps, confirming RBAC works, and filed the remaining access requests (registry contributor, prod resource-group reader, AD-group ownership, and a firewall opening to the GPU server). Waiting on Alejandro to grant them. (Jira DPS-5369.)

Erick A.

**Project Axiom — Voice 360**

*Insight extraction from unstructured customer feedback (Medallia, Guest Logs, Qualtrics) via LLM pipelines — feeds emails, dashboards, **drivers** analysis, and chat.*

**Guest Logs Classifier**

**Realtime Classification Service — API Live & In the App** *(David M.)*: Bridging last week's Hotel Ops demo, David turned the realtime guest-issue classifier into a deployable service — created the model-serving API, added a tab in the Axiom app (similarity categories, response time, top-20 results), and improved accuracy by switching from a plain centroid to a weighted average favoring authored examples. The PR is up; Erick to approve and deploy, which unblocks the SmartService integration.

**Speech-to-Text QA Passed** *(David M., Completed)*: Bruno sent real speech-to-text guest-log examples to validate the classifier against likely future inputs. David ran them through and saw very good results, closing the QA ticket; a separate ticket now tracks formal validation against the live data.

**Gold-Layer Table EDA** *(David M.)*: The new gold-layer guest-logs table keeps only the latest log per ID, which breaks booking-level aggregation. David is doing an EDA on the upstream raw table to recover all logs, reusing Erick's legacy dedup/concatenation notebooks. Choice of which gold-layer table to standardize on is still pending the data-model meeting.

**Drivers Model**

**Meta-Product Models Answered: Global Wins** *(Osvaldo V.)*: Last week Osvaldo set out to test whether per-meta-product drivers models beat the single global model. The answer is consistent across every meta product tried (7-night Caribbean, Caribbean/Europe/Asia, short): the **global model performs better**, and when restricted to Medallia features the important drivers (resolve-problems, ship cleanliness, ship appearance) and their partial-dependence curves line up — including useful satisfaction thresholds (resolve-problems spikes ~93.5, cleanliness ~96). The earlier concern is resolved. Next: targeted EDA on the two features where the models genuinely disagree (dining/bar service on 7-night Caribbean; guest service on short Caribbean), both likely under-representation in the training set.

**AI Product Categorization**

**Spa, Beverage & Dining Categories Complete** *(Osvaldo V., Completed)*: Reusing the Shorex categorization pipeline, Osvaldo finished AI-driven product categories for spa, beverage, and dining — each in its own table matching the Shorex structure. This exploratory exercise is now done; optional housekeeping is consolidating the per-category notebooks into one and PR'ing it.

**Power BI & Dashboards**

**Axiom ****PowerBI**** Refactor & Bug Fix** *(Rodrigo B.)*: Rodrigo refactored the Axiom Power BI dashboard and tracked down a row-duplication bug — an Average-NPS aggregation column was mistakenly used as a join key. After the fix and rebuild the daily job runs correctly; he'll keep monitoring.

**Abandoned Cart Dashboard — v1 Nearly Ready** *(Rodrigo B.)*: The first version is close to publishing but held by two clarifications: Eliana needs to confirm three charts whose values Rodrigo can't reproduce, and older Qualtrics survey responses can't be decoded because only the current value-mapping is downloadable. Rodrigo is asking Vanessa (Qualtrics data engineering) for the previous mappings.

**Destination Strategy**

**New Destination Strategy Requests** *(Erick A., new)*: Consumer Insights asked for two high-priority builds — a dashboard comparing Qualtrics vs. Medallia port/destination ratings (then layering in onboard-revenue signals), and a creative "destination strategy" agent spanning Qualtrics/Medallia/OBR sources. Both are queued for scoping with Consumer Insights.

**Email Reports**

**Port / Board Email — Awaiting Template Sign-Off** *(Rodrigo B.)*: The redesigned board email (recurrence chips + approximate prior-quarter mention counts) is finished. Per Erick (aligned with Matt and Anne Marie), no further board-email changes until Josh approves the template; Rodrigo is moving to other use cases meanwhile, with Matt's three ship-insights-report number updates targeted for early next week (one point still blocked on stakeholders sending the location matrix).

**GSO Shorex Safety Pipeline Fixed** *(**Danusio** G., Completed)*: The cascading June 14 empty-dataframe failure that lingered last week is resolved — fixes merged via Erick-approved PR. Weekend runs will be monitored for recurrence.

**Guest-Logs Web App — Dual-Source Analysis** *(Rodrigo B.)*: Rodrigo's web app now combines Medallia surveys and guest logs per sailing with a source selector (showing split counts, LLM summaries, and cross factors) plus a per-cabin 3D-style visualization (e.g., noise complaints by stateroom). CSV export already falls out of the clustering step; deeper cross-source work waits on David's full multi-ship dataset.

**Webapp Platform**

**Axiom App Migrating Flask → Next.js** *(Erick A.)*: To modernize the Axiom web app, Erick decided to rewrite it from Flask into Next.js for the next version, moving to a new domain (axiom.rccl.com) on Azure Container Apps from its current Databricks hosting.

**VDI Path for Team Axiom Access** *(Erick A.)*: Team members on Capgemini machines can't reach the Axiom URL — Zscaler blocks it and the machines can't run two corporate accounts at once. Erick confirmed the fix is a per-person VDI (as already set up for the new CEO) and will file the requests, starting with David.

**Project Scraping**

*Cross-brand initiative to build a unified scraping platform serving Consumer Insights, Hotel Ops, Product, and **Social Media**. Phase 1 review/forum sources; Phase 2 social platforms.*

**TikTok Link Discovery Pivots to Google Search** *(**Danusio** G.)*: Last week's decision gate was whether fresh weekly TikTok signal exists. It largely doesn't — TikTok's own search returns only ~3–5% relevant results for ship complaints, and quality decays with pagination. So link discovery moved off TikTok's relevance model to **Google Boolean search** (site:tiktok.com + ship + recency filters), proven via SERP API and now reimplemented as a dependency-free TamperMonkey browser script (scope deliberately kept TikTok-only — no YouTube/news). The viability test now pivots to **Wonder of the Seas** (dry-docking soon, likelier to surface negative feedback than flagship Icon), and a good/bad flag column is being added to the export. *Caveat: SERP API is not licensed for commercial **use — **legal review needed before any scaled use.*

Erick A.

**Contact Center**

*Predictive lead scoring and analytics built on contact-center (CTI) data.*

**Celebrity CTI ****Lead**** Scoring — New Sources** *(Erick A.)*: Stakeholders requested adding three lead sources to Celebrity CTI scoring — River (RVAL), Galapagos (GVAL), and a future UVAL bucket — each mapped to its own ID range. The adjustments are done on the data-science inference side, but are now blocked on IT, who must make the corresponding Siebel change before the new sources flow end-to-end.

Erick A.

**Contact Center**

*Trade-partner** segmentation and reporting pipelines (CCAS).*

**Trade Segmentation Pipelines Repointed to Unity Catalog** *(Erick A.)*: The CCAS trade-segmentation pipelines were broken — notebooks were still reading dead Hive tables fed by a broken Oracle→ADLS sync. Erick root-caused it, repointed ~59 references to Unity Catalog, opened four PRs (#4574–#4577), and built a replacement Databricks job for the dead Azure Data Factory triggers. The first stage validates end-to-end; the rest is in final validation. (Part of the broader UC migration, Jira DPS-5694.)

Doug B.

**Revenue Management (RCI & CEL)**** | Operations Support | JUNE**

**Review and escalate booking ****misberth**** incident findings**

**Deliverables:**

Reporting to all parties of interest expanded:

Continued twice-daily automated reporting of ADA bookings not actioned due to lack of inventory.

Continued twice-daily automated reporting of ADA berthing failures due to unreleased cabins.

New weekly report showing all active ACS bookings currently berthed in non-ACS cabin. For visibility to Accessible team.

**Investigate and monitor stale price rate spikes**

**Deliverables:**

Confirmation stale issue is resolved. PRE and TAP price uploads returned to normal and have been in line with expectations for over two weeks.

Data quality team is now actively monitoring for elevated stale rates daily. If daily rate exceeds 1%, notification is sent to team members for further investigation and resolution.

**Close-out Celebrity Short Carib T4**

**Deliverables**:

Short Caribbean T4 closed out. Analyses at overall, ship class and RDSS provided to the business. Recommend discontinuance of TARIFF 40 as driver of T4 booking rate. FREE T4 shows mixed results, dependent upon segmentation. Candidate for future confirmation testing.

Lamis A

**CEL**** Rev ****Mgmt****:**** ****PRE ****Price Optimization**

Completed Integrating the new Demand Forecast model outputs into the price optimization logic. This task includes:

Created a Data Processing Pipeline to generate p-grid and q-grid columns based on the percent_change, y_pred_up, y_pred_down, lafd_up and lafd_down columns from the demand_forecast.pax (and booking) tables. These grids are used to generate the demand curves required to run the optimization. The current version of the DF model output only generates the current week's predictions and demand curves - which is needed to run price optimization.

Revised the process to read the unweighted track ask (after coordinating with the SHs to read the raw track ask for the current week - this is different from the track ask in the price_change nb tables cause this is currently looking backward - optimization should look what track is asking this week (forward look).

Created a .html dashboard to visualize the demand curves for all active sailings. The current version of the dashboard only visualizes one demand curve for each sailing_date, ship_code, cat_class (for the current WTS). Once the long-term version of the DF model is completed, should update this dashboard to include all possible future Demand curves.

Validating the new model Demand Forecast Outputs - This includes inspecting the demand curves, things I observed and shared with Evan to investigate / resolve:

Curves are not monotonically decreasing - This has been fixed, but after enforcing monotonicity, I noticed that the demand curve y-axis (pax) scale has completely changed (originally for a particular product/WTS $100 apd predicted 7 pax in the latest version it predicts 2 pax - same sailing, cat class and WTS), shared my observations with Evan to look into this.

Discrepancy in the most recent WTS between the weekly table (this week's preds) and the full table (historical + current weeks') - Evan is looking into fixing this.

Eddie B.

Revenue Management RCI/CEL

Eddie baffa walked TUI Rev Mgmt team thru RMA. Focus was Suites, and they are following up on next steps. Got them comfortable with functionality. I had Suites and Cat Gapping content, only ended up talking through Suites this time.  What I walked through includes "**Revenue Management Automation (****RMA) —**** Royal Caribbean Group**

**A self-running pricing system** that replaces manual analyst pricing by reading live inventory and bookings, applying tested logic, and writing price changes back to the booking system automatically across both brands (**RCI** and **CEL**), running on a **Databricks/Spark** pipeline.

**Two flagship engines drive the value:** **TAP Suites** (vertical pricing — raising and lowering premium cabin prices over the booking window, ~**$18M** incremental in 2025) and **Category Gapping** (horizontal pricing — tuning the **GTY-to-physical-lead** premium, an estimated **$115M** upsell uplift in 2025).

**A repeatable, growth-oriented playbook:** every optimization starts with a controlled A/B test on a price premium, feeds a predictive trade-up model, and is governed by guardrails (price floors, freeze windows, exclusions) — anchoring a **2026 RMA target of ~$303.5M** and extending to new levers like bundled fare tiers (VIP PRO / PRO / PLUS / PUR)."

**Ben**

**IBP Supply Chain**

IBP has been rebranded to FreshFlow per Evan and Jessica. Our new logo is below:

Four things up front.

The self-improving forecaster is live in production for the cruise-line (RCI/CCI) book, and it is working. On the May backtest it cut model error from 13.7% to 9.4%, and it beat the prior model on all 11 earlier months tested. This is a major win. The forecast that drives cruise-line food and beverage planning is now more accurate, and it keeps improving under human approval rather than needing a rebuild.

We delivered a new ESG planning capability to production in under three days. Mario brought us new requirements, and we turned them into working production code in less than three days, across a large part of the FreshFlow codebase.

IBP is now FreshFlow. This is a product name change directed by Jessica and Evan. I am using FreshFlow from here on.

The FreshFlow app is live in Azure. You can open it at . This is its first hosted deployment, and the link is yours to share.

The new ESG capability. The new rule is simpler and closer to how buying actually works. Instead of splitting every sailing a little between the environmentally preferred (ESG) product and the conventional one, each sailing is now planned as all ESG or all conventional, and we reach the yearly ESG target across the full calendar year. It blends what ships have actually consumed so far with the forecast for the rest of the year, and it only assigns ESG to the ports that can truly source those products, using our Market Master and cruise itinerary data. Demand planning and finance now read from one shared decision, so both always show the same number. In the first full year, 2027, the plan reaches 94% of the ESG goal. 2026 lands lower because the rule starts mid-year, which is expected.

The self-improving forecaster, beyond the cruise-line book. We extended the same approach to the supply-chain (SSC) book. It is not live yet. It stays in watch-only review until it clears the same safety checks, and its self-improvement loops run only in our test environment under human approval. This week we got it producing accuracy scores and built its corrector, so we’re getting close to deploying a new model for Silversea.

Sharper forecasts for tricky ships. We improved the forecast guardrails so several hard cases now come out right. A new ship, LEGEND OF THE SEAS, now forecasts in line with its sister ship. Products newly assigned to a region now stay in the supplier forecasts, which brings back about 25,500 rows across 41 ships, including one supplier forecast that had been missing. Together these refine the fleet forecast down by a modest 1.6% by removing demand that was not real. One ship, GRANDEUR, comes down about 49% on its own as part of this, which is expected.

More accurate inventory cost, and it helps every ship. We improved how we calculate the average cost of inventory in the cost tracker. It no longer leans only on the cost of what ships have already consumed. It now blends in the cost of upcoming purchase orders, so the projected cost reflects what we are actually about to buy. This builds on the voyage-number change from Project Catalyst, and this week we made sure the blend flows correctly across all 45 ships after that change. For the BEYOND pilot alone it brings about $503K of purchase-order cost back into the figure, and the whole fleet benefits.

More reliable data pipelines. We strengthened procurement's demand-forecast files in SharePoint so they publish on schedule again, with alerts added so any future gap is caught right away as there was a bug which we addressed of files not being updated in Sharepoint. We rectified this issue within 24 hours of notification of the issue.

Documentation for review. We packaged the seven review documents into one decision-ready set for senior review, with consistent numbers and a clear, reversible approval step, plus a technical guide so a senior director can verify the system directly.

Camila

IBP - FreshFlow:

CocoCay:

Guests Ashore (GA) -normalization — re-based consumption from PAX → guests-ashore across all files.

TEST_MODE pipeline infrastructure — added a parameterized routing layer to all 6 model notebooks

The big finding: the guests-ashore win didn't hold up

Initial A/B looked good (mean APE −19%, CONSUMABLES −42%). Rigorous re-validation overturned it: it didn't replicate on the 2nd training date (mean APE 80→100), the "win" was a single week + a small-quantity %-error artifact, and on volume-weighted (units) error it was worse everywhere (+125k units).

Root cause, established across four tests: turnout is near-constant (~0.92, CV ~5%), so guests-ashore ≈ collinear with PAX. Timing features are static per-ship constants. Weather (rain) genuinely drives behavior per-day (food-exposure r = −0.335) but washes out at the weekly grain. And food/beverage-hour exposure, tested directly against consumption_report, adds +0.001 R² over PAX.

Conclusion: PAX is a sufficient driver; no guest-behavior signal beats it.

Working on matching guest id and/or cabin number to loyal account. My hypothesis is that for a newcomer arriving to CocoCay, they would like to take advantage of the full day, however, for a guest who has had multiple visits to CocoCay, we can possibly see their time offshore shortening as time goes on. Ultimately I am trying to find the guests that actually consume food under the food slot (10:30 am-3:30 pm) and who consumes the other categories

Pilot Pipeline:

The finance group pipeline was re-platformed onto a region/time-gated, multi-task Databricks Job architecture and hardened for reliable unattended operation. Previously, a single scheduled run processed the entire fleet and took roughly 6–9 hours, causing runs to overrun and queue behind one another, with occasional failures left to manual recovery.

This effort delivered five outcomes:

Runs are now scoped to the ships whose local time is in their morning window — typically 2–15 ships per slot instead of all 45 — so each run finishes well inside its time slot.

A latent defect that silently pulled the entire fleet into every run (the root cause of the multi-hour runs) was diagnosed and fixed.

Per-brand fault isolation was added so a slot with ships from only one brand (or none) can no longer fail the run.

A cost gate skips all heavy work — and avoids starting compute clusters — when a slot has nothing to do.

An automated daily coverage audit now produces a per-ship report card and emails an alert if any sailing ship is missed.

Net result: bounded, non-overlapping runs; graceful handling of single-brand and empty slots; lower compute cost; and daily, auditable proof that every sailing ship is refreshed within a 26-hour range. The pipeline currently writes to the test (test_mt_) namespace as a safeguard ahead of production cutover.

Status as of this report: the most recent daily coverage audit reports 45 of 45 sailing ships refreshed within SLA (full coverage), with zero alerts.

My next steps is to include the order creation group into the run to trylu see the full length of how long everything will take.

Validating CEL brand fleetwide on their guardrails predictions for daily breakdown. Implemented and enhanced the new ships automation to fit Xcel (no year comparison) and Legend (no actuals yet), and fixed the way PCDs were being picked up to have the guardrail apply for variance of budget to predictions

**Nico**

**IBP ****FreshFlow**

**Fix Relative Month Column Calculation to Use MODEL_TRAINING_DATE Instead of Current Date**

· Done ✅

**Completed:**

**Validated pipeline output via Genie verification report (Thu 6/18 → Sun 6/22)**: Reviewed the output of the successful June 12–13 pipeline run against the Jira story requirements. Genie's assessment confirmed all five Jira concerns resolved:

✅ **Temporal misalignment** — both notebooks now derive columns from MODEL_TRAINING_DATE = 2026-06-01, not execution date

✅ **Missing column errors** — new ensure_month_columns() safeguard guarantees all PREVIOUS_N_MO / FUTURE_N_MO columns exist (filled with 0 if data absent)

✅ **PREVIOUS_1_MO** populated for all 9,884 rows in the main PIVOTED table (May 2026 data)

✅ **FUTURE_1_MO** non-null for 100% of rows across all downstream tables

✅ **Full pipeline re-run** completed end-to-end (CREW_ETL → ETL → Demand_Probatus → Guardrails → archival)
DOE-2312: IBP | Fix relative month column calculation to use MODEL_TRAINING_DATE instead of current…

**Identified two separate issues during validation (Sun 6/22)**: The verification also surfaced two issues **not caused by DOE-2312**:

**Minor type bug**: lit(0) instead of lit(0.0) in ensure_month_columns() creates int vs double inconsistency for PREVIOUS_5_MO and PREVIOUS_4_MO in the crew table

**Pre-existing join failure**: All FUTURE_*_MO columns are NULL in the crew-adjusted table (_prds_modified_similar_crew) — traced to an overly strict composite join key including VARIANCE in pivoted_table_adjusted

**SSC Consumption and Prediction Ratio Adjustments**

· Done ✅

**Completed:**

**Closed out**: Given the need to run the pipeline from the beginning in DOE-2312, and the pipeline completing successfully, the story was closed. The WRITE_DATE fix (DOE-2252) was documented as completed in a prior sub-task. **Story moved to Done.**

**SSC Uniforms Model — Combinatorial Gender/Generation Ratios**

· Done ✅

**Completed:**

**Closed out**: The combinatorial gender/generation ratio features were integrated and tested through the full pipeline run. **Story moved to Done.**

**Challenger Models**

· In Progress

**Completed:**

**Created feature branch (Sun 6/22)**: Created the DOE-1469-Challenger-Models branch for this work.

**Created sub-task for HF&B reconciliation (Sun 6/22)**: Given the potential structural similarity to the SSC HF&B Model, created  to reconcile applicable commonalities between the two pipelines.

**Confirmed latest pipeline run has 2026-05-01 and ****2026-06-01**** ****model_training_dates**** (Mon 6/23)**: Verified the CLONE Weekly Uniforms pipeline output contains both dates. Running through the output to verify backtested results and report a new MAPE.

**Identified missing ****model_training_dates**** gap (Tue 6/24)**: Successfully replicated dates from 2024-03-01 to 2025-10-01 along with 2026-05-01 and 2026-06-01, but **missing **2026-02-01 and 2026-03-01. Documented two alternative plans to generate the missing dates.

**Ongoing:**

**Generating missing ****model_training_dates**: Evaluating the two proposed plans to fill the 2025-11-01 through 2026-03-01 gap in the backtested archival tables.

**Integrate Changes from SSC HF&B Model Pipeline (Challenger Models)**

· To Do · New this week

**Completed:**

**Documented 13 key logic differences between HF&B and Uniforms Challenger notebooks (Sun 6/22)**: Used Genie to perform a code-level comparison of SSC_Challenger_Models.py between the HF&B (reference) and Uniforms (current) versions. Key differences identified:

**Model type widget & **group_by_columns_model — reference threads model-type variants through every groupBy/join; Uniforms has no equivalent

**Selected categories** — reference is Uniform-only; current handles all 8 categories

**Consumption path logic** — reference maps each model_type to a different consumption table

**Column alignment** in wrapper function — reference has alignment step missing from Uniforms

**Environment handling** — Uniforms uses dynamic env; reference is hardcoded

**MMS/****Crunchtime**** Migration for SSC Uniforms Demand Model**

· To Do · New this week

**Completed:**

**Created story with full acceptance criteria (Mon 6/23)**: Documented the migration plan to update the Silversea Uniforms forecast pipeline to use PRODUCT_NAME_NUMBER as the stable product identifier across both MMS and Crunchtime. Acceptance criteria include: reading from the DA2I unified consumption view, preserving SOURCE_SYSTEM, updating product-level joins to not depend on non-null ITEM_ID, and validating Crunchtime rows for migrated ships (especially Silver Shadow).

**Documented 10 additional migration considerations (Mon 6/23)**: Beyond the core product grain change, identified: preserving SOURCE_SYSTEM through the pipeline, validating MAIN_STORE = 'Uniform' filter for Crunchtime rows, reviewing all ITEM_ID-based joins, handling Crunchtime missing fields, ship/voyage/date validation, cost/product enrichment compatibility, migration-specific QA checks, and documenting the new data contract.

Ale

IBP FreshFlow:

**CocoCay Shore Excursion Feature — Pipeline Integration**

- Moved Shorex work from initial signal validation into the CocoCay demand pipeline.
- Added weekly Shorex guest metrics from `COCOCAY_SHOREX_GUESTS` into the Demand notebook using the same weekly `TIME` grain as the model.
- Added matched venue totals, per-venue guest counts, private venue context features, and 30-day as-of booking signals.
- Carried the new Shorex features through to Probatus so they can be evaluated in SHAP-based feature selection.
- Used `_ALE` sandbox checkpoint tables to test changes without overwriting production outputs.
- Completed full notebook runs through the sandboxed CocoCay flow.

**CocoCay Shorex Validation & EDA**

- Built additional checks to validate whether Shorex data has useful predictive signal for CocoCay consumption.
- Reviewed matched venue signals across Coco Beach Club, Hideaway Beach, Waterpark, Oasis Lagoon, and South Beach.
- Focused the next iteration on more forecast-realistic signals, including 30-day as-of booking activity, cancellation rate, and product count.
- Checked for potential issues such as duplicate guest weighting, overly concentrated product signals, and same-week leakage risk.

**CocoCay Supporting Work**

- Updated CocoCay notebook paths/imports so the pipeline is easier to run from personal repo.
- Continued organizing the Shorex feature work around CocoCay-specific source tables rather than shared RBC forecast tables.

**Next Steps**

- Get introduced to the HF&B new ships automation project.
- Continue testing Shorex features through Probatus to determine which signals should move out of the `_ALE` sandbox path.

Ryan

IBP FreshFlow:

This week I completed Phase 0 and Phase 1 of my CocoCay Demand Model YOY Feature Enhancement Project— Phase 0 involved implementing 5 target-aligned year-over-year features and confirming deployment to the AGG table, while Phase 1 validated feature correctness by confirming all new lags point correctly and pass null/zero audits. Phase 2 (a Backtest A/B comparing the CocoCay demand model with and without the new YOY features) is nearly complete, and I expect to advance to Phase 3 next week,, which seeks to help us understand whether the new features are driving real demand signals or if the model is still leaning on operational constraints applied by the guardrails.

I also progressed the CocoCay demand model explanation slides, building out model results and feature importance visualizations for Yan. The GMO Inventory Depletion Table was completed last week but received minor updates this week to finalize documentation. Additionally, I scoped out upcoming work including the pre-merge cleanup, HF&B Replaceables Guardrails Enhancement, and EDA/ETL tasks. Overall, the CocoCay Demand Model YOY Feature Enhancement Project is on track through its phased validation plan.

Carlos A

E-Commerce Customer Targeting

RCI/CEL:

added new source of data "crm events" to the marketing models (~350 million rows of  very useful signals, ie: consumer acquisition type - paid vs organic.

maintenance (fix password deprecated issue, review PRs, replace local_checkpoint for checkpoint ..)

Silver Sea Propensity Modeling:

Meet with DE to agree on models output

Study Jakala provided code (feature engineering) and plan new model implementation architecture

Carlos A.

Loyalty:

generate new sailing scenario for 8 years into the future (3 years only previously)

Bao:

E-Commerce:

**Status Update**

**Clickstream Ingestion**

Completed a full review and remediation of the clickstream ingestion pipeline. Identified several historical data quality issues, including Celebrity sessions leaking into the RCI clickstream table (~2.24% of rows), an incremental ingestion grain mismatch that undercounted multi-device visits, boundary-day duplicate records, and unresolved consumer ID sentinel records contaminating feature windows.

Implemented and deployed fixes to production (commit 6944fd0, merged to bl/develop):

Added brand tagging (RCI vs. CEL) based on domain rather than dropping Celebrity traffic.

Updated feature engineering to exclude non-RCI sessions and unresolved consumer IDs from RCI model features.

Fixed incremental processing grain to align with bulk ingestion logic.

Eliminated boundary-day duplication during incremental loads.

Rebuilt and validated the production clickstream table. Validation confirmed correct brand attribution, zero null brands, zero duplicate boundary records, and proper incremental processing. A backup table was retained for rollback purposes.

Currently investigating a separate data quality issue impacting Celebrity clickstream data. A large majority of Celebrity visitors cannot be mapped back to a consumer ID, even when a valid RWDID is present. Since RWDID is typically used to resolve identities through the cross-reference (xref) table, I am working to determine why Celebrity identity resolution rates are significantly lower than expected and whether the issue is occurring upstream in the identity graph or within the resolution process itself.

Next steps:

Add cross-brand engagement features for RCI consumers who also browse Celebrity.

Finalize business logic for "last 3 visits" features (cross-brand vs. brand-specific).

Continue working with the Data Team on the Celebrity identity resolution issue, which is currently blocking broader Celebrity consumer modeling efforts.

**Training Report Dashboard**

Investigated and resolved an issue where Booking Propensity (BP) destination models were missing from the training dashboard. Root cause was an overly broad filter that unintentionally excluded all destination models.

During investigation, identified and fixed several additional reporting issues:

Single-model retrains were causing other models to disappear from the dashboard.

A single corrupt or missing model artifact could cause the entire report to fail.

Invalid brand/model-type combinations in the NBO UI could generate user-facing errors.

Implemented fixes to:

Restore visibility of all BP destination models.

Load the latest run per model rather than relying on a single latest report.

Make report loading fault-tolerant when individual model artifacts are missing.

Restrict NBO dropdown selections to valid brand/model combinations.

All dashboard fixes have been committed to the ble/develop branch and are ready for review/deployment.

Caleb

Customer Lifetime Value:
**Caleb's Weekly Update — 6/22**

**Consumer Lifetime Value**

*Completed*

Fixed a pipeline bug that was nulling out ~50% of our final value indexes. Root cause was a stale channel mapping. A few months ago we corrected our meta-channel logic with RP — the CREDITED and CREATION channels had been swapped — and last week validated that the fix ties cleanly to VCAP MICE. But the pipeline and our marketing-cost mappers from Corporate Planning (CP) were never updated to match. We re-mapped both CP's channels and our raw creation channels down to their lowest common grain to preserve the splits, so cost now merges cleanly into our per-booking allocation for US adults. (Fix is designed and coded; final validation is underway before it goes to production)

Built automated null-detection checks into the pipeline so this class of bug is caught going forward.

Confirmed CLV is ready to extend through 2025 on the revenue side. Verified that 2025 booking/revenue data is fully loaded and behaves consistently with prior years, so extending coverage is safe. A temporary cost proxy is in place for 2025 until the actuals land.

Prepared the agenda/workshop guide for our 6/29 Data Solutions session. Covers Customer360-to-pax joins at the correct grain, how often ingested features refresh, which features will be production-ready, and open questions organized by feature type (profile, interactions, offerings, transactions).

*In Progress*

Testing the corrected cost architecture, then re-validating end-to-end before productionizing. Building the layered cost tables (consolidated acquisition-cost reports → indirect-cost base → creation-channel mapper) and re-running the upstream pipeline stages, then validating on the new testing job ahead of production.

**Caleb: ****Sailing Environment**

*In Progress*

Validating our internal sailing-level anchor (capacity, NTR, yield) and rolling it up to tie to BIMA and the 2025 Strat Plan forecasts (both ship-level), with a more granular cross-check against Corporate Strategy's sailing-level working file.

Mireille T.

Contact Center: Workforce Planning Simulator
**Weekly Report June 25**

**WFP Simulator**

Orchestrate Celebrity North America data sources to flow into the "Run Your Own FTE" advanced section, covering call volume, assumptions, and all supporting inputs (in progress about 70% completed)

**Office shrinkage data Model**

brainstorming session with Fatou to support her understanding of the task on the office shrinkage data model, reviewing the WFP project to understand the overall context and how her work integrates, while also clarifying key terminology and sharing LOB mappings for North America

Using the eight tables, Fatou has explored and identified the relationships between them, determined the relevant columns for computing shrinkage by market, brand, and line of business, and calculated the key metrics.

Identified a missing table (**DEV_CCAS_****DATA.MKRPOPS.V****_CMS_CS_DAGENT_30_ALL_PS_HST**), which appears to have been dropped or deprecated due to missing dependencies in Unity Catalog. Actively coordinating with the data engineering team and multiple stakeholders to restore access or identify an alternative data source. (pending). Attempted to retrieve the data via Oracle using shared code, but this approach has not been successful yet.

**LP ****Prioritization :**** Lead Source Scoring Update (Celebrity CVP – Request from Rene Gonzalez):**

Received request to incorporate new lead sources **RVAL (River)** and **GVAL (Galapagos)**, which should be treated as dedicated categories and no longer classified under SVAL. Implementation is pending and will require updates to current model logic.

Requested review and alignment of existing handling for River and Galapagos leads across models, as historical classifications under SVAL differ from current production behavior. Both **BKTOCX and Offer model pipelines need to be reviewed** to ensure consistency with the new structure. Waiting for Augusto confirmation before implementation.

Implementation will require coordination with the **Siebel team** to ensure proper ingestion and availability of the new lead sources (RVAL, GVAL) in upstream data feeds.

Michelle M.

CEL Rev Mgmt: Category Gapping and GTY-Lead

**DUAL | Handoff Document**

Finalizing handoff document for 2.0 and 3.0 work. Pushed all code changes to prod as well as new pipelines created for 3.0 project. All code is in the brand respective TAP repo.

Reviewed pipelines in detail to identify differences versus what was duplicated, and consolidated most of the logic into shared components to reduce maintenance and prevent divergence. Replaced separate notebooks with a single parameterized pipeline, where brand controls only the areas that truly differ, such as bookability filters, GTY handling, category exclusions, and pricing behavior

Standardized the data construction layer across availability, booking (VCAP), pricing joins, and feature engineering so both occupancies use the same underlying data definitions, improving consistency and validation reliability Preserved real pricing differences (per-person for doubles vs. cabin-level for quads) but isolated them in one section so the rest of the pipeline remains shared and easier to maintain

Improved overall code quality by removing redundant operations, fixing edge cases in logic, and making calculations more robust and deterministic, helping ensure stability in production. Restructured the pipeline into a cleaner design.

Reduced duplication across the entire workflow, making the code easier to read, test, and extend, and lowering the risk of inconsistencies over time

Created clear documentation explaining the pipeline structure, key data flows, and where important business logic lives, including pricing and GTY behavior

Ran walkthrough sessions with the team to go through the pipeline end to end, including how to run it, debug issues, and validate outputs, with an emphasis on building intuition around key logic.

Evan M.

RCI/CEL Rev Mgmt

**DUAL | Demand Forecast - CI/CD**

Work completed: end-to-end production deployment of the Updated demand forecasting and elasticity model.

The Updated demand forecasting and elasticity model is deployed end to end to production. PRE consumes the new Unity Catalog table contracts across all brands, with stable schemas, walk-forward validated backtests, and per-sailing elasticity grids.

**Scope closed by this ticket**

Deployment across environments

Extension across remaining brands

Handoff to operations

**DUAL | Demand Forecast - Data Architecture JUN**

Demand Model

Aligned predictions with historical buckets and enforced data congruency
**Value ****add****: Representative predictive capability without focusing on MAE; model is accurate and aligned with each bucket of demand**

Asymmetric monotonic enforcement, from full-curve isotonic regression to right-side-only enforcement. Left side preserves raw LGBM output to retain elasticity sensitivity.

Identified parameter ranges and checked hypermeters if needed (not required)

Ensured dataset is congruent between all tables in UC for different types of forecast publishes

Magnitude divergence:

Diagnosed as model capacity from the original model

Sources agree near base price and at the high-price tail.

Added additional validations and visualizations for ensuring model alignment

Fixed FSData inbound ETL, incremental appends seemed to have a problem with approach

Found a best approach to demand curves with monatomic / isotonic regression from modeling side rather than enforcing a curve to 0.

Anneke

SSC Rev Mgmt - PRE – Dashboard & Pricing Enhancements

Update June 24, 2026:

Pushed changes for featurestore tables to production to resolve discrepancy between what the stakeholders were seeing for Load Factor and Booked Position to what we were presenting. Stakeholders brought up a spreadsheet where the comparison between their metrics and ours were always elevated. The issue was resolved by fixing the maximum capacity calculation and including some fare codes that had been left out.

Srilekha

CEL Rev Mgmt

**Promo Price Change Recs Decision Layer ****2  -**** Promo Price Change Recs Based on Recent Trends**

Status: This ticket is complete as of 6/25/2026

**Deliverables:**

The GTY pricing recommendation framework has been fully developed and shared, covering both promo eligibility (Layer 1) and price adjustment logic (Layer 2). The model leverages SPI benchmark comparisons, recent 5-week weighted booking trends, and sell-out pacing to generate targeted and explainable promo and pricing recommendations.

The work is complete from a development standpoint. Validation has been transitioned from Monica to Eduardo due to her other priorities. I’ve walked Eduardo through the full methodology, currently awaiting Eduardo’s feedback

**Potential future issue: **validation feedback from Eduardo; any feedback/request during validation may require minor adjustments to the framework

**RCI | Actual Price Paid JUNE**

**Document data sources, Get best performing SPI benchmarks**

**Adapted the Celebrity framework to RCI’s ****cadence** : RCI promos run Friday–Thursday (vs. Celebrity’s Tuesday–Monday), so I realigned all week logic, booked position reads, and pricing dates to match the brand’s actual promo week.

**Built the best-performing SPI benchmark for ****RCI** : established the booked-position benchmark from RCI’s best performing from SPI sailings at each WTS across different segments(meta, cat class, peak season flag) i giving the framework its basis for judging whether a sailing is on track.

**Pulled together promo prices, bookings, and current booked position**: all aligned to the Friday–Thursday week, so each sailing’s performance is measured consistently against its benchmark.

**Added visual diagnostics**: created plots showing each future sailing’s current booked position vs. the SPI benchmark zone across the booking window, making it easy to spot where promos are being applied unnecessarily (e.g., sailings already overperforming far out but still on promo).
Attaching plots above to review

Lance

RCI Rev Mgmt:

**RCI Data Addition to Dashboard**

RCI data (old and new model) added to dashboard and fully functioning properly. Filters including brand, ship, meta, etc. functioning with RCI data.

**RCI | model Performance Metrics Dashboard**

RCI data successfully added to dashboard. Next steps are feedback loop with RCI teams on new metrics and dashboard.

Aagam

PCP Pricing Automation

**CRF Offering**

The CRF Offering automation is now complete. This process prepares the Marketing file for flash sales approximately three weeks in advance by reading CRF details directly from SharePoint and automatically populating the required worksheets, including discount ranges, PCC sailings, RBC sailings, and other sailing-related data.

**CRF Automation | ****ShoreX**** CRFs [Generic, Alaska, Europe, RBC Santorini, RBC]**

Completed the automation for RBC Santorini, ShoreX Alaska, ShoreX Europe, generic, and RBC Alc pass.

**Next steps:**

Validation and pushing into prd

Anand S.

PCP Pricing Automation

**PCP Promotion Recommendation Pipeline — Daily Conversion, Validation & Analytics Completed**
Successfully converted the full promotion pipeline from weekly (52 WTS) to daily granularity (365 DTS) across all 7 Databricks notebooks. Implemented enhanced constraint logic (±5% daily, ±10% rolling 7-day, ±40% lifetime), recalibrated spline smoothing for higher-resolution tracking, and resolved 5 critical bugs spanning parameter consistency, revenue alignment, constraint enforcement, and smoothing behavior.

Executed first end-to-end daily pipeline run:

Runtime: **32.5 minutes** (14% faster vs weekly despite ~2.5x data volume)

Output: **230K+ recommendations across ~498K forecast rows**

All steps validated with full data integrity and no failures

Built full analytics and documentation layer:

**Analytics Explorer notebook (19 cells)** with interactive dashboards (fleet KPIs, product trends, constraint behavior, gap analysis)

**Tables Exploration notebook (31 cells)** with complete pipeline lineage and 20+ validated SQL checks

Architecture documentation updated with actual runtime metrics and daily design

Key findings:

**94%** of product-sailings have zero bookings (forecast-driven recommendations)

**54%** of recommendations clipped by constraints

Forecast correlation remains weak (**r=0.105**) → calibration opportunity

Majority of matches (**86%**) at ship-class level; dynamic adjustments still limited

Status: Fully validated, documented, and ready for production scheduling and stakeholder review.

**2. Celebrity Web Scraping Pipeline — Productionized & Running Daily**
Pipeline has been fully built, optimized, and deployed to run on a daily schedule across the Celebrity fleet.

This week’s work included final stabilization:

Fixed critical SQL ambiguity issue in snapshot rebuild; validated main table rebuild (**187K+ rows**)

Verified multi-category pipeline execution with **100K+ products scraped**, 0 failures, all quality checks passing

Restored full **13-category coverage across 13 ships**

Performance optimizations:

Runtime reduced from **18.8 ****hrs**** → ~5 ****hrs** via compute right-sizing and browser optimization

Implemented Chrome recycling to eliminate memory degradation

Added page-level failure tracking with threshold-based alerting

**Production outputs available in:**

dev_datascience.scraped_prices.web_scrape_celebrity_products_hist

dev_datascience.scraped_prices.web_scrape_celebrity_products_main

Status: Pipeline is running daily and stable. Final validation criteria is **7 consecutive successful daily runs**; upon completion, pipeline will be considered fully production-ready for ongoing use.

**In Upcoming Weeks:**

• Schedule PCP pipeline as a formal production Databricks job
• Improve forecast calibration and filter zero-revenue signals
• Validate rolling 7-day constraints after sustained daily execution
• Address fill ratio scaling edge cases
• Conduct stakeholder review with Revenue Management
• Complete 7-day validation window for web scraping pipeline

Ignacio V.

PCP Pricing Automation

Hot fix promo automations

The recent password and 2-way authentication led to some breaks on the DE workflow for promo autmoastion that platform is working on. This led to all promos that were tried to be uploaded to fail. In order for the fix to work without duplciates, a hot fix was done to revert the prd_revenue_mgmt_bu.obr_automation.promo_price_upload table to a previous version before today’s upload attempts.

Add QA guardrails to promo automation:

Notebook was adjusted to check for if BOTH product code and category were never specified for a promo rule included in the batch for promo automation. In these instances, in order to avoid rules applying across all products, these are excluded from the upload. In addition, when this happens, automated notifications to the business team were created using PowerAutomate in order for them to be aware of this ASAP and fix as needed for reuploads. Similar notifications and saferty checks were done for when the business team may accidentally edit the column names, which breaks the data structure and could cause the uploads to fail. As time goes on, when new edge cases are identified, these QA checks can be further enhanced.

Identify & debug error with AND groups for promo automation (with digital & De team)

Reconnected with the digital and DE team. The bug was identified by the DE team as double applying serialization that can lead to unexpected alterations to the data and string inputs of backslashes that breaks the schema/data type expectations. Lucas from DE is currently working on this fix. Once complete, lower env testing can be repeated before pushing the changes to production.

Refine & debug demand model training after Feature Store cleaning/fixes

The demand model run was finally able to complete for a first run and evaluation on the test set. Two different methods of this were done. Overall, the demand model is done at a weekly WTS level of data aggregation. One method segments by meta/meta group, resulting in 12 total models (6 meta groups, one clickstream model & one static model per meta group). The second method does NOT segment by meta and instead takes care of the high data quantity into Pandas by batching the data; this trains just one global clickstream model and one global static model, where now meta group is used as a primary categorical feature. Next steps are to evaluate this further (performance metrics, feature importances, etc) and look for areas of improvement

David W., Ben F.

HR

CAM Demand Automation Forecast was presented to the Capital Committee, where questions centered on the lack of a clearly quantified return. In response, the team clarified that the primary value lies in downstream operational improvements—reductions in over-hiring, rescheduling churn, onboarding rework, and travel inefficiency—which are materially larger than direct labor savings but difficult to size precisely at this stage. As with other early AI investments, the focus is on enabling faster, more consistent, data-driven decision-making, with a deliberate choice to be conservative in current value claims and quantify benefits as they are proven out.

The team also reinforced that this initiative is not a standalone ROI case but a foundational capability for broader CAM transformation efforts. It underpins multiple dependent initiatives (e.g., scheduling, onboarding, travel), meaning deprioritization would stall downstream value rather than free resources cleanly. Framing was adjusted to position success at the portfolio level, with an offer to provide directional, order-of-magnitude estimates to support prioritization decisions without overstating precision.

David W.

Loyalty

David worked on modifications to the Merge Recommendation Engine to be able to analyze bad MDM Merges (75k records). The modifications included building a brand new data pipeline (that included sourcing loyalty) and auto-building a fixed Excel file for human teams to evaluate the MRE outputs. IT wants the MRE to play a more central role in the MDM batch merge process:

Aryton (Leader in IT): I want to share this deck with you to give you visibility on how we are coordinating all the work to get to the other side of the Consumer Data Quality issues we are having. This was used on a large workshop with the commercial organization this week. MRE as a filter to Batch Merge is one of the initiatives we provided an update

The **MRE** is a new validation filter being inserted into the **batch merge flow** for MDM as **Step 2**, sitting between candidate identification and the final merge. The process runs in three stages: **Step 1** — the batch identifies pairs of consumer records that look like the same person based on identity-field similarity; **Step 2 (new)** — the MRE validates each candidate pair against **transactional signals** to confirm they're genuinely the same consumer; and **Step 3** — only validated pairs are committed and merged into a single **golden record**. The key shift is that today's batch merges on **identity-field similarity alone**, whereas the engine layers in transactional evidence to catch and cut wrong merges at the source before anything is committed.

To make that call, the engine checks a set of **transactional attributes** — **passengers on recent bookings**, **booking & sailing history**, **loyalty activity**, **contact & address signals**, and broader **transaction patterns** — so a merge only proceeds when the behavioral data backs up the identity match. This is part of the **Technology Process** workstream, currently **in progress** with engine logic and flow integration underway, targeting a go-live of **early July 2026**.

A couple of follow-ups I could tackle: condense this into a few talking-point bullets for the meeting, or pull a similar summary for the related Passport ID tokenization slide.
