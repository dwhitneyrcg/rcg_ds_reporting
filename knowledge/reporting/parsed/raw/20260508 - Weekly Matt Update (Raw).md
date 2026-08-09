**Ayon Ghosh**

**Win-on-Waste**

**Weekly Update – ****WOW(****Follow****-up to 5/1)**

**Interport**** MDR – Active Development Progress:**
Continued development of the **Interport**** MDR pipeline**. The **ETL layer and POS orchestrator pipeline ****are**** now complete**, establishing a stable data foundation. Work has begun on the **guardrail orchestrator**, integrating **XDining**** reservation data** to enhance demand controls and improve forecast robustness for MDR interport sailings.

**Q****-Control to ****CrunchTime**** Recipe Mapping (In Progress):**
Initiated a critical **Q****-Control to ****CrunchTime**** mapping exercise** in response to upcoming **recipe ID changes for buffet venues**. Historical data resides in Q-Control under legacy IDs, while future data will exist in CrunchTime under new IDs for the same recipes.

**Dynamic Cutover Handling Across Ships:**
Addressing the complexity that **cutover dates differ by ship** (only Oasis currently has a defined cutoff, others do not). To future-proof this transition, we are building a **dynamic, parameterized job****-configuration dictionary** that controls ship-specific cutoff dates.
By updating job parameters only, the pipeline will automatically:

Union historical (Q-Control) and future (CrunchTime) data correctly per ship

Eliminate the need for any code changes as cutoff dates evolve

**Operational Support & Issue Resolution:**
Resolved multiple **support tickets related to forecast discrepancies** across several ships, restoring expected forecast outputs and ensuring continuity for onboard operational planning.

Erick Alfaro

**MyCruise**** Recommender**

**ALS Improvements**

**Last week's ****MLflow**** metrics notebook is now complete and awaiting review.** Final-stage metrics work is finished — saving binary and weighted metrics with logging added; branch + pipeline doc + notebook links shared (feature/dm-improve-foryou-recommendations).

**Propensity model integration is the next track.** Once review feedback lands, Carlos's propensity model data tables will be reviewed and wired (along with Glen Erik's potentially) into the final pipeline stage. Three propensity models are now in flight, so the open design question is whether to combine them at the re-ranking layer.

**Product Clustering**

**All recommender work pushed into a shared branch** (experiment/als-clustering-notebook_cats). The latest categorization notebook running on the ALSRecommender was also shared.

**Open follow-ups**: increase LLM-generated category count from 38 → 100–150 to improve personalization (last week's Jaccard ~1.0 finding suggests under-segmentation), and Jaccard-calculation-level verification (de-prioritized — composite score is now the team's primary recommender metric).

**Guest Segmentation**

**Last week's "comparable to ****booking-level****" ****finding has**** now flipped into a clear win over the legacy baseline.** Composite score on a 1,000-booking validation came back **>0.2 with new clusters vs <0.2 without**; full 100,000-booking integration test (using product clusters instead of products) was running at week's end, with the loss function expected to land near **~-0.30 vs the prior ~-0.14 baseline** — a meaningful lift if it holds.

**Two new tracks opened from this week's standup**: (1) **Hybrid feature approach** — pin loyalty and party size as required cluster features and only let RF importance prune the rest; (2) **LLM explainability layer** — feed cluster centroids to an LLM to produce business-readable persona stories per cluster (complements the statistical explainability already done).

**Backtest**** ETL PR ****still**** pending.** Both ETL artifacts (quarterly model save + backtest table) and the demo notebook are ready; PR has not yet been opened for review. This is the gating step before clusters get integrated into ALS.

**Apriori**** Model**

**Last week's pre-computed recommendation tables continue to progress.** The Apriori + CF + CF-by-product combination is being staged in the standard table format so the strategy can be served from a precomputed lookup rather than computed at request time.

Erick Alfaro

**Project Axiom — Voice 360**

**Email Reports**

**Royal Santorini Beach Club Email**

**Email evolved substantially this week.** SHAP heatmap of OSAT importance now embedded; appendix metrics columns replaced with chips for cleaner layout; sections split per route with positive / negative bullet topics extracted per route. Open layout question: 3 main sections by polarity (positive / negative / improvements) with 3 routes each, vs current per-route subsections.

**New track: per-route metrics table** containing all metrics available for Royal/Santorini Beach Club, split by route with a composite-across-routes column. Once finalized, latest version will be sent to all current stakeholders (Gang Wang, Jay Schneider, Carly Montanti, Justin Birzon).

**Drivers / SHAP Analysis**

**Last week's sailing-level OLS regression is now superseded by a tree-based + SHAP approach**. SHAP rankings (cleanliness #1, safety #2) align with what other models surface; trees handle the multicollinearity that made OLS coefficients unreliable. Underlying 49-sailing dataset is still small but the consistency across models is encouraging.

**Sample-size column added to ****drivers**** analysis** *(**Completed)* — addresses last week's small-N visibility concern.

**New track: SHAP heatmap across all ports** — extending the tree/SHAP pipeline port-by-port and aggregating into a port × feature heatmap (also feeds the Santorini email).

**Shorex GSO LLM Pipeline**

**Last week's GSO cost optimization is now in Phase 2.** Phase 1 shipped — new methodology consumes less time and fewer tokens with quality close to the prior output.

**New PR opened** moving the GSO data-table generation logic out of the email job and into 000_main_ETL so the email job only sends emails.

**Dry Dock Analytics**

**Icon of the Seas Dry Dock Pain Points Report** *(Completed)*: replicating last week's Symphony delivery for Icon. Two HTML reports — 01_medallia_dry_dock_report.html (Medallia-driven) and 04_public_sources_report.html (Reddit + Cruise Critic reviews + forums + TripAdvisor). Methodology: anchor in Medallia, then external scraping to corroborate, expand, and surface issues guests don't always raise on the survey.

**Meta Data Framework**

**Bullet-points topic update kicked off this week.** Topics for bullet points are being updated in the metadata extraction repo using the new definitions structure.

**Guest Logs Classifier**

**Stakeholder demo of the Guest Logs Classifier delivered this week** to kick off the topic-cleanup effort. **Main takeaway: AI/ML/LLM will be used to clean up the existing Guest Logs topics and make them more consistent.** This is the **initial step in preparing the data for all downstream analytics work** — automated emails, driver analysis, and chat capabilities all depend on a consistent, cleaned topic taxonomy. Follow-up meetings with the relevant teams have been scheduled as the project develops.

**LLM Reasoning Capture moved to In Progress** *(carryover from last week)*: reasoning summary implemented on the Guest Logs side; plan is to delete the legacy reasoning prompt and rely solely on the model-provided summary going forward.

**New track: Migrate Guest Logs / action instruction repo from OpenAI Chat Completion API to the Response API** — motivation is lower cost and better reasoning support. Migration is in progress.

Erick Alfaro

**Contact Center**

**AI Pivot — Contact Center IVR Surveys**

**Project restarted after October pause.** Alper has finished fixing the survey questions and signaled it's good to resume. Prior IVR documentation is being re-read; kickoff chat with Augusto being set up. Priority bumped to 2.

**Siren — Contact Center Transcript Analytics**

**Rerun the prior handle-time-by-topic ("time to topic") analysis** on the latest transcript data — multiplies talk time by topic probability to attribute call duration to each topic.

**Mert:**
MIAP

Set up MIAP GitHub in the new Alpha Org, including CI/CD pipelines and branch protection rules, and migrated 12 repositories. Three repositories are still pending full migration. This work will lay the foundation for the rest of the DS team, as pipelines are set up as reusable templates.

Troubleshot ongoing inaccuracy issues with Digital Twin models and identified the root cause as a simple division vs. multiplication error in fuel calorie conversion. Achieved a 4% ($40M) improvement in fuel forecast accuracy across the fleet.

Met with the Maritime Safety team on automating SeaEvent KPI creation. The solution would use GenAI to interpret user inputs, generate a recommended KPI severity score, and send it to GMO and Maritime Safety leaders for approval.

Arya:
MIAP
Worked on repairing CI/CD pipelines.
(1) Fleet Tracking: Continued development of the ArcGIS map for the Securities team.
The map now tracks 44 ships.
Added ports and port weather.
Added news reports refreshed every 24 hours and labeled by severity.
Added an ocean reference layer.
Clicking on a ship now displays past, current, and future itineraries.
Added a “Diagnose Area” button to scan a selected area and display weather conditions, ships, and ports in a more concise view.
Enabled all tables to be draggable.
Added a 3D globe function.
Aligned color schema.
(2) SORA for Safety: Set up a pipeline to receive expected JSON inputs for analysis.

Ram:

MIAP
This week:
Worked on VPS fuel reports. The existing flow only loaded the latest file without validating whether a file had been received the previous day. Updated the process to validate file availability and added email notifications when files are missing in ADLS, along with guidance to reach out to the VPS team in such cases.
Pushed the PEPLINK batch to production; it is functioning as expected.
Generated per-vendor cost reports and shared them with Mert and the Finance team for review.
Separated ADLS landing folders for Crosser based on protocol. This needs to be tested across all sources in the development environment before promotion to production.
Developed and raised a PR for configuration file changes. Ship-level tags are required from vendors and need to be added to the configuration to proceed. All required changes for the REST API and marine package are already completed.
Next week:
Work on real-time streaming via Postgres using TimescaleDB.
Make required changes to the REST API and marine package to support joins for value conversions.

Reza:
MIAP
Identified and led the resolution of a bug affecting port duration calculations in the itinerary and fact tables, which was contributing to performance degradation in the Digital Twin package.
Resolved a workflow issue caused by overlapping datetime values between voyage legs.
Fixed a critical issue in the Digital Twin package where the latest models (including propulsion, service power, OFB, and power plant) were unable to predict N-day averages of target variables, which could previously cause failures.
Continued debugging failures within fuel forecast workflows.
Prepared an initial draft of Digital Twin forecasts at both datetime and voyage levels as a reference for the Finance Fuel team.
Conducted ongoing analysis of service power models, focusing on ships with low-performing models or anomalies. Updated the model and baseline for ship UT to improve performance.

Mahshad:

MIAP

Identified potential energy savings and sent an email to the Engineering team:

AHU SM: 100 kW

OV AHU: 100 kW — this value comes from DD and requires further investigation.

Investigated issues with the LHV tables and corrected the values for IC and ST, which are using LNG only.

Fixed pipeline issues related to OFB, Machinery, and Chillers.

Updated plots for Chillers and model data; they now appear correct.

Worked with the Deployment team to add a deployment page to the MIAP app; this work is still in progress.

Ben F.

Supply Chain: 
This week’s work focused on validating code finance tracking tool pipeline supporting the Beyond Pilot.

We compare old and new outputs and historical parquet files previously created to track how ESG products were allocated. There was some concern that possibly the ESG products were not being properly allocated by our stakeholder but my analysis proved that the products were properly allocated, however the allocation of these products changed on the March 7th parquet file write, as the business supplied mapping of ESG products changed at this time.

There is also active work underway on the next Supply Step 1 section, focused on demand shipboard master load schedule logic. Early validation shows that the new separated version matches the original output across roughly 15 million rows. This continues the same pattern: split out one section, validate it carefully, then move to the next.

I also am still working on the feature selection for Silversea for a new model build.

Work in Progress:

Silversea Demand Model Rebuild continued: Previously we were getting some code errors where recursive feature elimination with cross validation was not working properly but we recently completed a test on a single product and ship after making code changes and the test worked, so the full feature selection process is resuming today.

Finance Tool Code Refactor in Process; Had to suspend this work for this week due to the need to support the data validation work on the Beyond pilot,but am resuming this work time permitting with Beyond work.

Other IBP Code Refactoring: In progress of refactoring Supply Model notebooks, but also put this work on pause, but am resuming it, time permitting with Beyond work.

Camila
Supply Chain:  
Beyond Pilot Finance Tool:

High estimate food cost predictions:

Removed products that were predicted but not consumed (if the sailing is completed since that is when actuals populate). This was not allowing us to have a correct estimate on food cost savings when looking at historical sailings.

Once actuals populated for most recently completed sailing on Beyond (4/26), the prediction value increased. After analysis, it was found that the average inventory average cost increased for several products which drove the original prediction value to a higher value once the actuals were populated. In progress is an enhancement to be sure that the unit cost is brought in to the tables that are updated daily so that we get a better estimated prediction value while a sailing is ongoing. Specifically for 4/26, it seems that there were a lot of random spikes that is the most likely reason we have a variance from before the sailing was completed to now.

Added orphan detection for products with zero historical consumption on a given ship (Beyond). It was originally found that about 50 products that were predicted were never found on Beyond which was then excluded.

It was then noted that ESG products were missing. I noted that it could be the orphan predictions enhancement and I was correct. The orphan products were then fixed to include an ESG product flag. If the flag is 1 then we should not consider the product with a prediction as an orphan product, meaning it should not be removed from estimated prediction value.

Added PCD scaling factor for future sailings based on the ratio of forecasted PCD to the average of the last 12 completed voyages. This helped a lot of high predictions for future sailings. Also a lot more automated since we will be getting the latest PCD information every time the revenue table is refreshed. Downside is that for the current sailing (5/3), the 4/26 sailing had an update during the week and not when the sailing completed. This caused the value to change and alerted questions but this can be argued that its a lot more accurate now. I would still like to find a way to improve this because a sailing should still not get an updated prediction about 3 days in.

Creating a new enhancement to tackle holiday sailings specifically. It was noted by Chef and shipboard team that it doesn't make sense to have a future sailing with a similar guest count to a historical sailing to have a higher prediction value than the historical one. We still believe the model is still working effectively due to the sailings they pointed out being a Memorial Day sailing. However, we want to add an additional guardrails specifically based on a lookup of future sailing passenger count to a historical sailing with a similar passenger count (I currently have a threshold of +-50 passengers). For example, for the memorial day sailing starting on May 24th that has about 3406.7 guest counts in their FCST_PAX column from revenue data, this has a direct comparison to that of March 22nd with 3407 guest counts. Understandably so, why is the prediction showing a higher value compared to that of March? This new guardrails will reduce the prediction if this flags true that a historical sailing has a very close guest count to that of the future. Still in development. I would like to make this even more enhanced by looking at product categories possibly.

Royal Beach Club (RBC) Demand Forecast: in progress

Took CocoCay demand forecast model code and just replaced all mentions with RBC instead.

SSC Finance Tool: in progress. Next steps are to build consolidated table. I need to make sure that all changes applied to RCI/CCI version are applied for SSC. The frozen predictions and parquet files need to start being developed so that we have history to refer to.

Nico

Supply Chain: 
**SSC Uniforms Model — Combinatorial Gender/Generation Ratios**

· In Progress

**Completed:**

**SHAP notebook executed & ****MdAPE**** computed across 3 experiments**: Ran the SHAP notebook end-to-end and computed MdAPE across three cumulative feature sets — (1) baseline, (2) + SCD crew count features, (3) + combinatorial female × generation ratios. Shared results with Camila.

**Clarified experiment scope with Camila**: Confirmed the experiments test additional features, noted the initial MdAPE of 16% vs. Camila's reference of 41%, and flagged the need to re-run on a comparable consumption_date for an apples-to-apples comparison.

**Flagged two open items**: (1) potential target leakage from the ±45 day employee_count distribution window, and (2) missing MALE equivalents to the FEMALE × GENERATION combinatorial columns.

**Guardrails code review & bug identified**: Reviewed SSC_Demand_Model_Adjustments_and_Guardrails.py, found a hard-coded model_training_date='2024-07-01' that causes the SharePoint Health Report to always show the latest model. Updated the code to dynamically derive the date. Also raised a concern about whether the cumulative overforecast logic in guardrail_adjustment_step_1() is the intended behavior.

**Ongoing:**

**Comparable ****MdAPE**** re-run**: Aligning consumption_date across experiments to produce a directly comparable MdAPE number.

**Spend Report Data Quality**

· In Progress

**Completed:**

**Ruled out code-level changes as cause of inflation**: Compared prd_gold.ibp.ssc_spend_report (a view) across table versions 116–122, confirmed avg_price_2025 doubled (3.63 → 6.01) at version 121 only for MAIN_STORE=Food. Verified no notebook code changes in the past 30 days and confirmed all job runs used identical code.

**Detailed version-by-version comparison**: Produced aggregate comparisons for each subsequent version from 116 onward, pinpointing version 121 as the change point, and shared the version history and SQL query with the team.

**Proposed converting the view to a table**: Recommended converting the ssc_spend_report view to a versioned table so future discrepancies can be tracked at the row level, and asked Camila Furtado if this is feasible.

**Ongoing:**

**Awaiting DE escalation**: Proposed escalating to Data Engineering since no code-level cause was found and the view has no historical snapshots.

**AI Prediction $ / PCDs & Guest Counts Table**

· QA / Testing

**Completed:**

**Table delivered**: Created dev_datascience.ibp_sso.beyond_ai_predictions_daily_breakdown with validations passing, noting two minor data discrepancies (outlier Total_AI_PREDICTION on four sailings, and missing Latest_PCD for two future sailings).

**Ongoing:**

**Pipeline integration**: Camila requested the table be integrated into the orchestration pipeline so it updates daily; currently in QA.

**Beverage Product Name Label Extraction (AI POC)**

· Done

**Completed:**

**Delivered final categorization to Matt**: Sent the finalized beverage product categorization using the basis of products from the 2023–2025 Beverage PO files, combining pre-existing drink_category_label values with AI-extracted labels. Moved story to QA.

**Automated Spend Report & Consumption Fix**

· QA / Testing

**Ongoing:**

**Yearly folder structure**: Identified the need to create yearly folders for each report type and modify the upload code to target the respective directories.

**RCI/CCI HF&B Order Creation Dashboard MLS Discrepancies**

· In Progress

**Ongoing:**

**Paused — awaiting Yan's reply**: Put the validation on hold pending Yan's response to the email about the single-voyage finding. Planning to escalate to Paolo and the DE team once feedback is received.

Carlos A.

**E-****commerce :**** **

deployed latest big code refactor to production (some hotfixes needed), now all pipelines are running dbr 17.3 LTS

**Bao**

**E-Commerce ****Customer Targeting****:** 
**1. Unity Catalog ****MLflow**** Pipeline Fix (shipped)** 
Identified and resolved the root cause of cascading pipeline failures across all three production pipelines (MKT_Models_Train, MKT_Models_Predict, MKT_Models_ETL). The failure traced to a single malformed MLflow API call in report_train_bp_rci.py that was incompatible with the Unity Catalog model registry format. Also removed a stranded classifier reference in report_train_phml.py that would have caused a secondary failure. All three pipelines reran successfully after the fix and a PR is ready for merge.

**2. Clickstream Feature Integration Research (decision reached)** 
Ran a full EDA across four experiment variants to evaluate whether web clickstream features should be integrated into the BP booking propensity model. Results showed the RCI LGB model regressed by 0.054 AUC with CS features added. Celebrity showed a 0.041 lift, but this was from a CS-only experiment rather than the full model context. Decision: do not integrate. The added complexity and maintenance cost are not justified by the uncertain and inconsistent lift signals. This conclusion prevents a costly model change that would have degraded RCI performance.

**3. App Usage Feature Post-Integration Analysis (complete)** 
Completed a post-integration analysis of the app usage features that were merged into the model pipeline. Produced a complete inventory of which models are actively using the features and identified the subset of models where at least one app usage feature ranked in the top 20 by feature importance. This gives the team a clear picture of where app behavior is meaningfully driving model predictions.

**4. Disparate Impact Audit Stage 1 (complete, Stage 2 in progress)** 
Stage 1 of the disparate impact audit for the BP model ran successfully. Core protected classes came back clean. Geographic proxies were flagged for monitoring and will be addressed in Stage 2 via proxy detection using logistic regression and SHAP analysis.

Carlos A.
**Loyalty ****Simulator****:**

develop and integrated new model for better match consumers to cruising based on sailing nights probability. Now we have 4 models working together in the simulator (sailing date , cabin category, sailing nights, spend prediction).

ingested latest deployment plan, handed by revenue managing team (now we have planned sailings until ~2024)

engineered new cabin category feature, to replicate loyalty points gain.

improve simulator speed (a most after adding two ne models) based on multistep sampling

**Caleb:**

**CLV:**

**In Progress**

As we prepare the CLV proof-of-concept for industrialization with Kiana's team, we are revisiting our approach to passenger-level cost allocation. Historically, costs have been distributed at a ship/month grain, but with Catalyst now available, there is an opportunity to refine this allocation to the sailing level, which would significantly improve attribution accuracy.

Engaged with Corporate Planning to develop a deeper understanding of RCG's cost of acquisition methodology, requiring detailed examination of SG&A line items and review of a granular allocation report produced by Peloton Consulting Group

Consulted with Revenue Planning on optimal strategies for integrating Catalyst cost data with VCAP passenger-level records. This is part of an ongoing cross-functional dialogue between Revenue Planning and Data Solutions

Revisiting the previously deprioritized concept of lagging marketing costs to more accurately reflect booking timing when attributing expenditures at the passenger level (current methodology allocates annual marketing spend uniformly at the sailing-year level)

Requires development of a booking timing relationship with corresponding marketing allocation weights

Quantifying the impact of booking cancellations on cost attribution

Establishing meaningful segmentation of marketing cost categories for differential allocation

Supporting Corporate Strategy on the Cost of Sale initiative, evaluating the feasibility and potential revenue uplift of vertically integrating alcohol distribution at select ports.

**Completed**

Conducted an assessment of existing Customer 360 attributes and delivered a PowerPoint summarizing current state, integration feasibility, and strategic value of incorporating these attributes into CLV's productionized final table. This deliverable feeds into an ongoing process with Data Solutions to finalize a granular workplan defining required table features and implementation priorities.

Srilekha

CEL Rev Mgt

Promotions Decision Rules

Actual Price Paid / Trader Performance Analysis (Celebrity & RCL)

**Detailed Update**

Lekha completed trader performance and trade-up analysis and shared results with Monica.

Based on new feedback from Celebrity:

Stakeholders do not want immediate productionization.

Instead, they want analyst-facing visibility to review promotions effectiveness.

Proposed solution:

Use SharePoint-based visibility

Highlight where promotions are underperforming

Allow analysts to review and decide on next steps.

Going forward, Lekha will:

Close out completed analysis work (credited to May),

Maintain a main ticket with subtasks for ongoing visibility and application work.

**Comment**

“I finished the trader performance and trade-up analysis and shared it with Monica. Today, Celebrity gave feedback that they want a separate visibility process using SharePoint so analysts can review promotions and see where we’re not doing well. This won’t go straight to production—analysts will review the work and decide next steps. I’ll focus mainly on that visibility work now.”

Anneke

**SSC** **PRE | PRE Tracking Dashboard**

**SSC | PRE | AB Test | Upper-level Suites**

This work item involved preparing and analyzing data for an upper-level suite AB test, with ongoing efforts to finalize setup and approval.

I completed exploratory data analysis (EDA), including correlation checks and power analysis, and refined the AB test framework, expanding the testing horizon through 2027.

Stakeholders requested refinements to the existing predictive model before proceeding with the test, and the pairing process for experimental groups was completed, with considerations to incorporate price effects.

The next steps include determining the experimental treatment approach, refining the PRE model, setting up the AB test, and obtaining approval to run it, with ongoing stakeholder engagement**.**

**Detailed Update**

Anneke is leading the experimental design (A/B testing) for upper level suites PRE.

In parallel, she is refining a PRE performance dashboard:

There was no prior Silver Sea PRE reporting.

Dashboard now includes:

Number of recommendations

Actionable vs paused recommendations

Automation-driven price changes

Ongoing stakeholder feedback suggests:

Additional EDA is required to finalize experimental design.

PRE refinements may expand scope beyond initial estimates.

Some ongoing collaboration with Jesse is not yet fully represented in tickets and will be added as subtasks.

**Comment**

“I’m working on the A/B test design for upper level suites and refining the PRE dashboard based on stakeholder feedback. There was no Silver Sea PRE reporting before, so the dashboard now shows recommendation volumes, approvals, pause reasons, and automation-driven price changes. There’s additional EDA needed and more stakeholder refinement before we start the test.”

Neila

RCI Rev Mgmt

Sailing Universe

Requirements Gathering, Methodology, and Deployment

**Detailed Update**

Neila has started work on both major tickets.

Primary effort this week has been finalization and deployment coordination.

New stakeholder requests added to scope:

Static baskets for the Suites revenue planning project:

Do not change quarterly

Editable via SharePoint

Target completion by Friday

Excel extracts of tables published in Databricks.

Some methodology work rolled over from April and is being refined.

Total scope remains within estimated capacity.

**Comment**

“I’ve started both tickets. Most of the work has been around finalization and deployment. There’s a new request for static baskets for the Suites revenue planning project that won’t change quarterly and will live in SharePoint. I’m also delivering Excel extracts of Databricks tables. This should be completed by Friday.”

Michelle

**RCI ****Rev ****Mgmt**** ****| Category-Gapping 3.0**
- Met with business. Plan is to wait for maintenance work to go into effect mid-June before any ML approach is used. RCI plan is to improve data before it is utilized to create recommendations.
- Model is being iterated and improved so it is ready for when the team wishes to use it. Strategy team is reviewing outputs to ensure it matches business intuition.
- All 2.0 updates were approved. Tested in QA and pushed changes to PRD.

Michelle**
CEL**** Rev ****Mgmt**** | Category-Gapping 3.0**
- Met with team and received list of MVP requirements. Current progress is:
o Current predicted, Goal shares, and Optimal shares add up to 100% - DONE
o All future sailing/cat-classes combos are in there (usd for everything, gbp for Europe, aud for Australia) - DONE
o Available inventory matches - DONE
o Confidence Check Column - DONE
o UP, LUP, LP... shares are proportional to each other at similar gaps – IN PROGRESS
o GTY share not higher than 50% - Team wishes to hold off for now
o Check highest price - no compounding gaps – Team will review this
o Flag / dig into where optimal revenue < current – Flag added to output. This is due to the “optimization” recommending gaps to achieve desired pricing. It is not solely a revenue optimization so there will be cases where gaps are not increasing APD because we are prioritizing shifting booking shares.
- Working on ensuring all shares are proportional across models.
- Continuing progress on DART layer.

Ignacio

PCP Pricing Automation

**Automate Waterpark Promo Uploads**
• Process of pushing this to production (i.e. having it work across all 3 envs: dev, qa, & prd) has some complications. The function for copying over Oracle tables into Databricks works fine in lower env, but is running into issues in the QA & PRD environments, which is problematic i order to load the necessary data for automation of the waterpark promos.**
Recurring Business Meetings & OBR DS Meetings**
• Meeting was had with Garrett regarding some of the nuances in the approach he took for integrating clickstream data for beverage and the overall PRE logic.
• Several meetings have been had with Doreen regarding the table schema to be used for clickstream data in the CEL Beverage PRE. Some more of these will continue to be had at a recurring basis while the schema and data in the table is further validated for the use case of the CEL Beverage PRE/DM.
• A meeting was had to sync with the Digital BI & Data Engineering team behind a lot of the new data developments for OBR/PCP, including mass promo data, clickstream data, etc.**
Explore Garrett's modeling approach & identify areas of improvement**
• The notebooks for the PRE logic from Garrett was further investigated. The 00_coinfig notebook made lots of sense and was well understood. The 01_data_build notebook is up in the air since the data to be used for it is currently incomplete and changing as we align more with the digital team in obtaining the necessary data for the modeling. The different model training notebooks make sense more or less, but a lot of it was vibe-coded by Garrett using Genie and not well understood by him on his end, so the modeling wants to be further studied and well understood; there are already some identified areas for improvement such as:
• adding in cross-elasticity & trade-off effects by expanding out of flat MNL
• upgrading out of Poisson GLM to a more advanced model for pageviews (e.g. LightGBM)
• optimization for the entire booking window instead of just the current point in time of the booking window.
• better scaling of features & better temporal CV validation
• interaction effects, correction of multicollinearity, and other additional new features

Doug

PROPEL

Aagam

PCP pricing Automation

**Conversion-Based PRE V2 – Waterpark, RBC Pass, Beverage Package**

This week, I focused on layering price recommendations generated from **track-based signals** with those derived from **conversion metrics**, and formalized business rules to resolve conflicts between the two.

**Approach and business rules applied:**

**Same direction, track recommendation stronger**

When both track-based and conversion-based recommendations point in the same direction (increase or decrease),

And the magnitude of the track-based recommendation is higher,

We adopt the track-based price recommendation.

**Same direction, conversion recommendation stronger**

When both recommendations move in the same direction,

And the conversion-based recommendation is stronger than the track-based one,

We apply the conversion-based recommendation, but cap the adjustment at 5 percentage points above the track-based recommendation.

**Opposite directions**

When track-based and conversion-based recommendations conflict,

We rely on the track-based recommendation as the primary signal,

And dampen its magnitude based on the conversion-based signal to reduce risk.

**Pricing guardrails**

Independent of the recommendation logic,

Guardrails were implemented to ensure prices do not exceed predefined upper or lower bounds.

I will be sharing my results with the business team (on 05/07/2026) and push the waterpark prices to test starting next week.

**Comment:**

“This is a follow-up from last month. I added track-based recommendations and made the process reusable across product codes. This week I’m focused on waterpark recommendations. I’m meeting with Jorge to walk through them, then we’ll push them into an A/B test next week and compare performance. After that, I’ll replicate the same approach for RBC Pass and beverage packages.”

Anand

PCP Pricing Automation

**1. Sailing Classification & Clustering — EDA Phase** Working with **Aagam** and **Ignacio** on the sailing clustering project. Performed initial **EDA on two key feature store tables**: prd_revenue_mgmt_bu.feature_stores.ship_sdt_features (sailing-level attributes — 7,769 sailings across 465 departure dates, 226 itineraries, 20 brands) and prd_revenue_mgmt_bu.feature_stores.ship_sdt_productcode_wtsbin_aggs (product-level sales aggregated by WTS bins). Profiled feature completeness (zero nulls on core identifiers), validated grain (ship_code × sailing_date is unique), and explored the booking transaction table (prd_silver.cmrc_ods_core.booking_transaction_order_entry) for deriving performance signals. Established the approach: use ship_sdt_features as the sailing-level base, then aggregate WTS-bin product data to one row per sailing before clustering.

**2. Web Price Scraping Pipeline — **Handover & Rebuild Took handover of Andrew's web scraping infrastructure (29 individual Selenium notebooks scraping Royal Caribbean cruise planner pricing across 14 product categories, 30 ships, USD & GBP). Performed a full audit of the dev_hotel_operations_bu.web_scraping schema — 647K rows in the main snapshot, 19.2M in history across 112 scrape days. Identified critical gaps: GBP scraping is fully dead (6–10 months stale), 3 categories have broken/limited coverage, and scrape frequency is irregular. Built a consolidated replacement pipeline in a single modular notebook with dev-mode toggle, temp-table-only output, and production schema validation. Tested end-to-end successfully — scraped 2 ships, all 12 product codes matched production (100% cross-reference), schema is 14/14 columns validated.

**3. Celebrity ****ShoreX**** Product Performance Analysis** Ran EDA on top-performing shore excursion tours/products for each brand. Analyzed historical transactional data and exported to Excel for further analytics on key metrics: **COMPONENT_CODE**, **COMPONENT_NAME**, **total_amt_guest_paid_usd**, **total_volume_sold**, **Revenue Percent**, **calculated_price**, **Avg Rev Per Day**, and **Avg Vol Per Day**.

**Upcoming Next Week:**

Write complete pipeline and scripts for **significance testing on Waterpark (ZH01) A/B test**

Finalize and **deploy the redesigned price scraping pipeline** to production (replace Andrew's 29 notebooks with single automated job)

Continue sailing clustering feature engineering with Aagam and Ignacio

Continue Celebrity ShoreX analytics with Alex

Glen-Erik C., Javier, Doug

PROPEL

Measurements:

Doug is helping improve the measurements and make it across the finish line. Investigated edge cases where cabins get reassigned a booking, sometimes a booking isn't cancelled until after the sailing even the guests didn't sail.

Created category level APD views and propensity binning to see uplift and conversion by propensity.

Javier reviewed and validated NULL values in measurement_granular and pre_granular, identifying root causes and reducing inconsistencies (<1% impact).

Refactored logic to track data at booking and pax_id level, avoiding issues caused by cabin-based backfilling.

Improved handling of multi-cabin scenarios, reconstructing customer journey where possible.

Decoupled metadata (guest, sailing) from transactional data to ensure more stable and complete fields (cabin, pax, ship attributes).

Standardized category and offer mappings to ensure consistency between offers, purchases, and propensity outputs.

Integrated propensity probabilities, preserving correct association between pax_id, cabin_number, and y_pred_proba.

Investigated mismatches with all_inclusive_rate_information, identifying join issues (date formats and grain alignment).

Identified and started resolving date inconsistencies in casino revenue logic.

Began improving pipeline robustness, highlighting need for partial redesign to reduce volatility and improve monitoring.

Updating daily job to incorporate fixes and ensure more stable outputs.

Enhancements:

XC casino offers enablement in progress (Santiago)

Prod issues: (Glen-Erik & Santiago)

There was an issue with the new schedule table Santiago had created to fix scheduling gaps that caused the history of executions to be wiped triggering duplicate runs when deployed. We weren't sure what was causing the duplicates since the schedule doesn't have them listed so ended up working most of last weekend on it.

The addition of the Art category somehow introduced a null value in the list of categories, and when the monthly automatic retraining of the model happened it created a model that was expecting a non existent null category so the inference of the model started failing. Traced this back to the category data which in turn was due to how the ingestion of the input data was setup sometimes causing out of sync issues as the null value didn't actually exist in the front end data anymore. Instead of merging the input data now that data is overwritten and the historical data for offers is stored in a separate table.

Glen-Erik

PCP Pricing Automation

Targeted offers Royal: TOs went out to 103 guests and 2 test bookings for Web/App on Wednesday and for Email on Thursday.

Targeted offers Celebrity: Tos went out to 236 guests and 1 test booking for Web/App on Thursday and we are scheduled to send the email on Saturday.

Scaling up to 1,000 guests in the next 1-2 weeks.

Eswar

RCI Rev Mgmt

OBR oracle connection and directly pulling up tables which can eliminate usage of ADF copy data activities.

Productionizing actual_doubles_performance_alloc and actual_quads_tradeup_performance workflows for TAP.

Fixed the Mis-alignment between develop and one developer branch caused due to few reverting and cherry picking in TAP project.

Created and Validated the views ship_sdt_features and ssc_weekly_ship_sdt_sailing_voyagefeatures provided by DE team after my initial feedback.

Providing ML support debugging issues

Monitoring CI/CD deployments, PRs

Eswar

PCP Pricing Automation

Price webscraping Knowledge transfer sessions. Requested and got access to hotel-operations databricks workspace inorder to access the scripts.

Jesse B., Anneke, Eddie B.

SSC PRE: Leadership Sync

**Key Takeaways**

**PRE expansion moving forward for 2027 voyages**

The team is aligned on expanding PRE usage across **Mediterranean, Northern Europe, Caribbean, and Alaska voyages**.

Prior A/B testing indicates **similar revenue performance vs. current pricing tools**, supporting broader rollout.
*(From meeting transcript + shared screen summary)*

**Shift away from paired voyage testing (for lower suites)**

Historical paired A/B testing is no longer required for certain segments.

Decision: **Proceed with full rollout**, with ongoing monitoring of performance and acceptance rates.
*(From Jill, Claire discussion)*

**Upper-level suite pricing is a major opportunity**

Identified **~$10M revenue upside** from shifting demand from bid-up upgrades to direct purchases.

Challenge: **Limited price elasticity data** due to sparse historical variation.

Approach: Use **A/B testing and exploratory analysis** to define pricing strategies.
*(From Claire, Anneke, Jesse)*

**Inventory & data limitations are a key risk to PRE accuracy**

PRE relies on “track” (booked position), but:

**Group allocations, options, and unnamed space are not fully reflected**.

Silversea systems differ from Royal/Celebrity, especially:

Options not reflected until deposit

Unnamed group space behaves differently

Risk: **Incorrect demand view → suboptimal pricing decisions**.
*(From Camille, Claire, David discussion)*

**PRE is useful but not sufficient alone**

Consensus: PRE is a **speed/efficiency tool**, not a full replacement for human judgment.

Acceptance rates are **not expected to be 100%** and currently remain **relatively low**. *(From Claire, David)*

**Need to move from symptom tracking to root cause fix**

Rather than just tracking acceptance rates, leadership emphasized:

Capturing **specific rejection reasons**

Using that data to **systematically fix gaps (track logic, inputs, rules)****
***(From David, Eddie, Kevin)*

**Transition to post-promo pricing**

PRE will be updated to operate on **post-promotional prices**, expected to significantly improve consistency and interpretability.
*(From Jesse, Camille)*

**Action Items (with Owners)**

**1. PRE Rollout & Monitoring**

**Move forward with full PRE rollout across key 2027 voyage regions **

**Owner:** Jill / Claire

**Closely monitor acceptance rates to validate confidence **

**Owner:** Claire + Revenue Teams

**2. Reason Codes for Price Changes / Rejections**

**Design and implement structured “reason codes” (and allow free text initially)**

Capture causes such as:

Promotions

Group allocations / inventory nuances

Pricing freezes

**Owner:** Jesse (system capability), Camille + Silversea team (input), Eddie/Kevin (framework alignment)

**Refine taxonomy (potentially move from free text → standardized codes)**

**Owner:** Eddie + Kevin (working session next week)

**3. Inventory & Data Alignment Improvements**

**Validate how group allocations and options are reflected in track / reporting**

**Owner:** Claire + Data & Reporting Team

**Assess changes with new reservation system**

Ensure alignment with Royal/Celebrity data models

**Owner:** Claire + Data Team

**Evaluate whether to incorporate options + retention rates into modeling**

**Owner:** Revenue Planning (Liz’s team) + Analytics

**4. PRE Model Enhancements**

**Transition PRE to use post-promotional pricing inputs**

**Owner:** Jesse

**Develop dashboards for:**

Acceptance rate

Rejection rate

Rejection reasons

**Owner:** Jesse / Anneke

**5. A/B Testing Expansion**

**a. Expedition / Galápagos Voyages**

Begin A/B testing (account for group booking complexities)

**Owner:** Jesse + Camille

**b. Upper-Level Suites**

**Define test design and pricing actions (in progress)**

Based on exploratory analysis (data sparsity challenge)

**Owner:** Anneke + Jesse

**Select voyages using AB testing framework**

**Owner:** Jesse (with Silversea input)

**6. Business Process Improvements**

**Capture “freeze periods” (e.g., during promo launches) as explicit reasons for no price changes**

**Owner:** Camille + Jesse

**Use GenAI / analysis to cluster and summarize rejection reasons**

Goal: accelerate root-cause resolution

**Owner:** David (concept), Analytics / AI team

**Bottom Line (Executive Readout)**

**Decision:** Proceed with PRE expansion for 2027 across major voyage regions.

**Constraint:** Model accuracy is limited by incomplete inputs (groups, options, promotions).

**Focus Shift:** From tracking acceptance → **fixing root causes in inputs and logic**.

**Value Driver:** Upper-suite pricing optimization represents a **clear ~$10M ****opportunity**, but requires new testing and analytics methods.

David Whitney and Mert Ersoz

Newbuild Planning

**Key Takeaways**

**Shift to narrative-driven updates (from the meeting transcript)**

The team’s recent update to Harry and Alfredo was well received, particularly the **structured storytelling approach** (situation → progress → needs).

Expectation is to **maintain this cadence and format** for bi-weekly updates.

**Process understanding is foundational to AI value (from the meeting transcript)**

Newbuild and Fleet Modernization processes (phased workflows, deliverables, quality gates) will be walked through in upcoming sessions.

Core principle: **AI solutions will not succeed without deep understanding of how teams ****actually operate**** day-to-day**.

**AI Observatory direction = augmentation, not replacement (from the meeting transcript)**

The vision is to **enhance existing tools (e.g., Power BI dashboards)** with AI (e.g., chat/agent layers), not replace them.

Focus is on **removing transactional/manual work and enabling deeper interaction with data**.

**Emerging roadmap mindset: bold + outcome-driven (from the meeting transcript)**

Strong push to define a **transformational roadmap (multi-quarter / multi-year)** including:

Build vs. buy decisions

Tool consolidation opportunities

Guidance: **prioritize high-value ideas first; funding approach (****OpEx**** vs. ****CapEx****) can be solved later**.

**AI fluency gap is material (from the meeting transcript)**

Skills assessment shows:

**Low capability in using AI agents** (lowest scoring area)

**Broad opportunity across adoption, frequency, and skill depth**

Notably, **self-ratings were lower than manager ratings for AI**, which is unusual and validates the gap.

**Leadership adoption is the critical constraint (from the meeting transcript)**

Leaders are mandating AI usage but **often lack hands-on understanding**.

Key risk: **shallow adoption (e.g., generic use cases) vs. real business impact**.

Required shift: leaders must **actively use and model AI**, not just direct teams.

**Resource model must evolve (from the meeting transcript)**

Success requires **dedicated, embedded technical resources** within Newbuild:

On-site, integrated into day-to-day workflows

Floating/shared resources are insufficient for transformation.

**Parallel tracks emerging (from the meeting transcript)**

**Enterprise Observatory + AI solutions development**

**AI capability building (training + adoption)**

**Process mapping + integration opportunities**

**Funding + CAR development**

**Action Items (with Ownership)**

**Process & Discovery**

**Conduct Newbuild “process by phase” walkthrough sessions**

**Owner:** Hani / Mala

**Timing:** Starting next Wednesday session

**Objective:** Document phases, deliverables, and identify AI integration points

**Evaluate where AI/Observatory can improve workflows**

**Owner:** David / Mert + Newbuild team

**Objective:** Identify automation, augmentation, and data gaps tied to actual workflows

**AI Skills & Training**

**Share AI skills assessment data**

**Owner:** Noah

**Objective:** Enable deeper analysis (by function, role, geography)

**Align with enterprise training efforts (Ajeet’s team)**

**Owner:** David

**Objective:** Tailor training to Newbuild needs using assessment insights

**Define leadership-focused training approach**

**Owner:** David / Hani / Noah

**Objective:** Ensure directors+ are **hands-on and capable of driving adoption**

**Product / Platform Strategy**

**Define integration approach (AI + existing tools like Power BI)**

**Owner:** David / Mert

**Objective:** Validate how agents/chat experiences integrate into current workflows

**Develop transformational roadmap (multi-year vision)**

**Owner:** David / Hani

**Objective:** Outline build vs. buy, tech stack evolution, and efficiency targets

**Funding & CAR**

**Draft initial CAR proposal**

**Owner:** David (first pass)

**Support:** Hani / Alfredo

**Objective:** Define scope, investment needs, and rationale

**Align on funding approach (****OpEx**** vs. ****CapEx****)**

**Owner:** David / Hani + Finance

**Note:** Secondary to defining the right solution

**Resourcing**

**Define and secure dedicated Newbuild technical resources **

**Owner:** David

**Objective:** Identify embedded (likely contractor) roles reporting into DS/AI but sitting with Newbuild

**Stakeholder Alignment**

**Schedule follow-up with Harry & Alfredo (end of month)**

**Owner:** Hani / David

**Objective:** Provide updated progress and roadmap direction

**Schedule session with Kelly (SVP Design)**

**Owner:** Hani

**Objective:** Bring in missing stakeholder group and align on needs

**Net Assessment (Executive Framing)**

You are **transitioning from pilot → scaled transformation**, but success hinges on:

**Deep process grounding (not tooling-first)**

**Leadership-driven adoption**

**Dedicated embedded resources**

**Clear roadmap + bold investment posture**

The conversation is **appropriately shifting from “what can AI do” → “how do we operationalize AI into Newbuild workflows at scale.”**

Kevin Diaz

PCP Pricing Automation

Built out a new optimization approach for unconstrained products (like beverage) that optimizes revenue using a demand forecasting model and accounts for dilution. beverage PRE using Jorge’s Tracks seems to be doing well actually. driven mostly by population shift from same time last year.

Evan McFall

RCI Revenue Management

Working on a new GBM-based Demand Forecasting Model enhancements and aligning closely with Lamis A. on Track Optimization. New model seemingly appears lower impact of price, but other features that are related to price have higher weight. Instead of worrying about a high-level feature or SHAP importance, focus is on testing on the Demand vs Price marginal relationship from the context of making a price change. The key is understanding how pricing recommendations change using the new volume forecast vs the GLM approach.

Presenting an evaluation of a stacked ensemble approach to demand forecasting. The core idea is to combine multiple models — each optimized for different forecast horizons — into a unified framework. By layering additional meta-models and learners, the ensemble better captures low-volume demand scenarios that single models tend to miss. Custom base estimators and transformer-based architectures provide flexibility, allowing the same structure to serve both short-term and long-term predictions while supporting existing optimization workflows.

On the engineering side, significant improvements have been made to the data pipeline. A centralized, class-based architecture now manages table creation, data access, and feature engineering in one place, making changes fast and maintainable. New dynamic transformers and lagged features are automatically produced and reduced within the pipeline, and external data sources from **FRED** and **Google** have been integrated with automated update mechanisms. These infrastructure upgrades lay the groundwork for more scalable and reproducible model iterations.

Performance comparisons show meaningful accuracy gains. The ensemble outperforms both the original model and the prior version across most demand bin sizes, with new features and methods driving the improvement. Sensitivity analysis reveals the updated models are less reactive to price fluctuations — curves align with expected elasticity patterns but assign smaller relevance to price, suggesting the models rely on a broader, more balanced set of demand signals. However, pricing may be a more important component after accounting for feature interactions.

David Whitney and Glen-Erik C

PROPEL (SSC)

Aligned on SSC PROPEL CAR with Senior Leaders on final draft and ready to submit next week to Capital Planning. Erin Green has asked for time to discuss capital allocations for next year to scale the PROPEL pilot up and address other use-cases.
