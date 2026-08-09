***Erick A., Cristian V., ******Danusio****** G., Osvaldo V., David M., Rodrigo B.)***

**PCP***** *****MyCruise**** Recommender**

**Team Onboarding & Alignment**

**Full Team Mobilized on Recommendations** *(Erick A.)*: Onboarded the broader team onto MyCruise recommendations as the top short-term priority. Danusio assigned to guest segmentation (y-axis), Osvaldo to product clustering (x-axis), David to ALS model improvements, and Rodrigo to Apriori robustness. Erick sent the recommendations slide deck to team and is creating requirements documents for each workstream.

**Collaborative Filtering Improvements**

**Guest Segmentation** *(**Danusio** G.)*: Built and iterated on a clustering model for the user-item matrix. ML feature selection reduced 24 features to 5 with a 0.78 silhouette improvement. DBSCAN outperformed other methods (3 of 4 quality metrics). Agreed to use meta_product + brand as primary segments, dropping rate_class_cat in favor of APD/RFM. Will save model objects (not just parameters) with quarterly rolling models for backtesting. Meeting with David Silva (product team) to align on business-facing segments.

**Product Clustering** *(Osvaldo V.)*: Current product names are only 4-5 words and produce overlapping clusters (~350 currently). Enriching product descriptions using the MCR product details table (highlights, what_to_wear, activity_level, restrictions, duration) to create more distinctive embeddings. Focusing on Shore X first, then expanding. Coordinating with Anand (pricing) on shorex segmentation alignment.

**ALS Model Exploration** *(David M.)*: David now understands the repo structure, model serving, and ALS algorithm with evaluation metrics. Next: sync with Cristian on improvement ideas — Cristian specifically suggested exploring re-ranking mechanisms on top of existing ALS predictions, which may be as effective as changing the model itself.

**Apriori**** Model**

**Ranking Policy API Bug** *(Cristian V.)*: The new ranking_policy parameter is live for Apriori all categories, but testing revealed an attribute error — API doesn't recognize the parameter. Cristian investigating.

**Apriori**** Robustness Issue** *(Cristian V., Rodrigo B.)*: When same-port filters are applied, ~40% of recommendations return empty because mined association patterns don't cover all filter combinations. Rodrigo being onboarded to improve this. Erick creating a requirements document from standup context.

**A/B Testing & Front-End Signal**

**WIN — Apigee Use-Case Parameter** *(Cristian V.)*: Lance confirmed the use-case source will be added as a parameter in the Apigee request body. This enables tracking which front-end use case is calling the API, unlocking A/B testing control and per-use-case performance evaluation. The Service Side Calendar Changes task is now resolved — engineering agreed to this alternative approach, avoiding disruptive changes to DS pipelines.

**Infrastructure / Postgres**

**Postgres Instability** *(Cristian V., Erick A.)*: Marcio's upgrade caused pipelines to break (user set to read-only mode). Cristian refactored code to work around it and is testing post-upgrade performance. Erick spoke with Utkarsh in person and is drafting a formal email to Platform requesting an exclusive Postgres DB instance for recommendations — the current shared dev DB has caused repeated incidents when other projects make changes. Also recommended Cristian test asyncpg as an alternative to Spark JDBC for bulk operations.

**Databricks ****GraphQL**** Whitelisting** *(Cristian V., Erick A.)*: Cristian raised a Jira ticket with Platform to enable Databricks outbound HTTP for GraphQL staging. Carlos (Platform) confirmed the ticket. Going forward, all platform requests must go through Jira.

***Cristian V., Erick A., ******Danusio****** G., Osvaldo V., David M., Rodrigo B.***

**Project Axiom — Voice 360**

**NPS Drivers / Weather Analysis *****(Osvaldo V.)***

**Weather Analysis Concluded**: Weather correlation with NPS is very low (0.091). Even in best/worst weather scenarios, the gap between predicted and actual NPS remains large. Weather affects NPS slightly but is not a significant driver. PR submitted for Erick's review. Osvaldo has transitioned to recommendations work.

**Email Reports *****(Rodrigo B., ******Danusio****** G.)***

**Port Report — Regional Comparison** *(Rodrigo B.)*: Built a new port comparison section showing OSAT for the target port vs. other ports in the same region (using Medallia region field), with a table and bar chart with deltas. Erick approved the concept but asked to condense the layout. Next: send screenshot to Matt via group chat for approval.

**Port Data Pipeline for ****PowerBI** *(Rodrigo B.)*: Sent the initial table to Efrain. Awaiting feedback on time range, granularity, and update frequency. Erick suggested proposing monthly updates (weekly may lack sufficient new survey data).

**Abandoned Cart Dashboard** *(Rodrigo B.)*: All new dashboard field modifications added to the pipeline and table updated. Pipeline notifications now in place.

**GSO Safety Email** *(**Danusio** G.)*: Sent the report to Alessio via automated email. Still needs to distribute to the broader stakeholder list (Hunter, Ross, Jocelyn). Danusio also opening a new PR for GSO/ShoreX changes after the revert of PR #318.

**Meta Data Extraction *****(David M.)***

**Guest Logs Gold Table Investigation** *(David M.)*: New gold layer table only retains one record per guest_log_id (most recent by change_date), whereas the old table had multiple. Working with Alex Kim (table owner) via group chat to resolve discrepancies in record counts and text content.

**Classification Model Accuracy** *(David M.)*: Reviewed the misclassification Alessio flagged — the correct candidate IS in the model's candidate list, but LLM randomness causes inconsistent picks. Options: modify prompt, set temperature to 0 (limited support on GPT-5 nano medium), or upgrade to Grok for more deterministic output. Erick following up with Platform on Grok Foundry endpoint provisioning.

**Gratuity Topic Analysis *****(Rodrigo B.)***

**New Request from Alessio** *(Rodrigo B.)*: Analyzing gratuity-related guest comments from Medallia. Identified the correct data source (DS web app parsed_comment extract, not raw Medallia tables). Awaiting Alessio's direction on whether to use fixed topics for historical tracking or AI-generated topics that adapt weekly.

Carlos A and Bao

**E-Commerce**** Customer Targeting****:**

**Progress in feature ****engineering  for**** journey scored model (****challenging**** since initial database have ~20 ****billions**** (10^9) rows, Kudos to Bao here for reducing ****the number of useful columns. ****
(pending incremental logic and to add more features)**

**defined difference in the code between session and visit for web data.**

**Code review**

This week’s work advanced both **business adoption of our analytics** and the **operational maturity of our data science pipeline**.

**Business Enablement & Adoption**
Finalized and presented data science updates across ecommerce and marketing, highlighting how teams are actively leveraging our models to **identify high****-value consumer segments** and deploy **more targeted, personalized offers**. This signals growing business adoption and improved alignment between analytics outputs and marketing decision-making.

**Operational Efficiency: Clickstream Data Foundation**
Refactored the clickstream ingestion process to systematically reduce columns based on null rates, cardinality, and redundancy. This results in a cleaner, more efficient dataset (~50–60 core features) to support the **journey scoring model**, improving data quality, model performance, and long-term scalability compared to the previous domain-only selection approach.

**Customer Journey Intelligence (R&D)**
Began research and experimentation on a baseline **Hidden Markov Model (HMM)** to infer a consumer’s purchase stage from their sequence of clickstream interactions with time gaps. Early results indicate **six potential purchase****-journey stages**, establishing a foundation for future capabilities such as stage-based targeting and better timing of marketing interventions.

**Booking Propensity Model Enhancements**
Started integrating app-related behavioral features (e.g., prior app usage, post-voyage app engagement) into the booking propensity models. Current focus is on testing and validation to ensure **clean ingestion, correct date sampling, and avoidance of data leakage**, supporting a reliable and production-ready pull request.

**Improved Decision Framework Clarity**
Re-visualized the stakeholder decision framework to make **POC target consumer segments more immediately identifiable**, improving interpretability and accelerating business decision-making.

Next Steps

**Deploy ****Streamlit**** Validation Tool**
With PRs for the data source validation Streamlit tool approved, the next step is to **rebuild the Docker ****image** so the application reflects and exposes the new validation functionality.

**Fix Historical Prediction Pipeline**
Investigate and resolve failures in the historical prediction pipeline caused by **MLflow**** issues and recent code changes**. Once fixed, proceed with generating historical predictions for the **POC consumer segment** and complete back-testing.

**Camila A. & Ben F.**

**Supply Chain:**

**ML Prediction Reference Builder (New Feature)****
- Created a new notebook to capture a frozen snapshot of ML predictions at the exact point-of-forecast****
- Produces a sailing-date-level summary table that cross-validates against existing predicted voyage demand values**

** Weighted Average Cost Tracker — Step 3 Fixes and Enhancements****
- Enhancement: Added PREDICTED_VOYAGE_DEMAND and ACTUALS_VOYAGE_DEMAND columns to preserve ML predictions and actual consumption separately (3 cells edited):****
  - Forecast rows: Copies VOYAGE_DEMAND into PREDICTED_VOYAGE_DEMAND before overwrite; sets ACTUALS_VOYAGE_DEMAND = null****
  - Consumption rows: Sets PREDICTED_VOYAGE_DEMAND = null (no ML prediction); sets ACTUALS_VOYAGE_DEMAND = QUANTITY_RECONCILE**

** Historical Model Training Dates Voyage Demand (****NB1) —**** Bug Fixes****
- Bugs found: END_DATE column missing and forward-straddle voyage logic incorrect (LMVD issue) (made it miss voyages that had end date in the following month)****
- Corrected formula: LMVD = _MONTHLY x VD / SUM_MONTHLY_VOYAGE_DEMAND (bypasses the lost VD_PRORATION)**

** March/April sailings (BEYOND FOOD):**

**  Sailing   Cross-Month?   VD        LMVD Before   LMVD After   Ratio Before   Ratio After****
  Mar 15    no             245,737   203,042        222,354      0.826          0.905****
  Mar 22    no             223,010   206,804        202,668      0.927          0.909****
  Mar 29    yes            227,938   137,727        212,061      0.604          0.930****
  Apr 05    no             230,901   227,658        226,071      0.986          0.979****
  Apr 12    no             211,659   208,687        207,232      0.986          0.979**

** February cross-month (Feb 22 to Mar 1):**

**   Sailing   Cross-Month?   VD        LMVD Before   LMVD After   Ratio Before   Ratio After****
  Feb 22    yes            219,730   182,833        201,414      0.832          0.917****
  Mar 01    no             217,081   196,432        198,469      0.905          0.914****
  Mar 08    no             218,425   196,430        200,002      0.899          0.916**

** Key findings:****
- Mar 29 (original anomaly): Fixed from 0.604 to 0.930 — now consistent with neighbors****
- Feb 22 (second cross-month): Fixed from 0.832 to 0.917 — also consistent with its neighbors now****
- Same-month sailings with multi-row products (Mar 15) also benefited — the same formula corrects a related deduplication artifact****
- Controls (Apr 05, Apr 12) barely changed (0.986 to 0.979) — the fix does not distort correct data****
- All LMVD/VD ratios now fall in the 0.90 to 0.98 range — consistent across all sailings****
- The previous naive fix (replacing with _MONTHLY_VOYAGE) would have set Feb 22 to 362,874 (1.65x VD) — that is what exposed the error. The correct formula produces 201,414 (0.917x VD).**

** Override Tracking Scorecard (Major Refactor)****
- Migrated data source from raw consumption tables to the consolidated finance tracking table: reduces query complexity and aligns with finance team's single-source-of-truth****
- Fixed critical duplicate-row bug caused by missing deduplication logic; added binary Excel support and sheet-name fallback for more robust file ingestion from SharePoint****
- Moved override impact calculations to run before aggregation, improving both correctness and performance**

** ETL and Bid Data Fixes****
- Silversea: Recovered lost Weight and Comments columns in bid data aggregation using a two-phase column recovery approach. Columns had been silently dropped during a prior schema change****
****- RCI: Updated bid data aggregation to handle new upstream column schema without breaking the downstream finance pipeline**

**we**** had a ****sharepoint**** issue come up last week and we had to update all code that uses ****sharepoint****, the code was not properly handling all the files in the folder which is why there were only 2 source files. **

**Then the code was only picking up xlsx and ****xlsm**** files with the ****fix ****i**** made for this^ which got me to 200 files**

**however****, it wasn't 100% correct still because there were also ****xlsb**** file types which required another step where we import a package to the code. ****this**** got me to 387 files**

**But,**** Paige then mentioned that ****it is**** 389 files you guys need so I knew I was missing two. The error there was that for the missing two ****files were**** missing a "Data" sheet. ****instead**** it was "Sheet1": **

**Bid Analysis - Alaska 2026 - Produce Analysis.xlsb**

**Bid Analysis - Hawaii - Apr 26 to May 26 (produce).xlsb**

**i**** then**** added a section in the code to include files if they have a Sheet1 file as well and to not exclude those.**

**Bug Fixes to HF&B pipeline****
- Fixed SharePoint Graph API pagination logic that was truncating large file lists; corrected EDA export file paths that were ****writing**** to wrong directories****
- Fixed Silversea PRD Silver tracking query to pick up ****prd**** gold reference instead since ****prd**** silver table does not contain any data anymore. That was generating false data-freshness alarms (something to revisit to make sure no other notebooks are using the ****prd**** silver table)**

**Automated Spend Report & Consumption Fixes**

Completed:

**UOM added to automated reports**: Updated the automated report outputs so **all files now include the UOM column**.

**Naming convention redesign**: Implemented the naming convention (potentially ({Quarter}_{Year}) versions per report), including whether/how to backfill prior quarters/years.

**SharePoint code integration testing**: Validated the implemented SharePoint changes by testing against copies of the SharePoint folder.

Ongoing:

**Backfill approach (report_automation_write_in_date.py)**: Exploring use of report_automation_write_in_date.py to support re-running/backfilling historical report versions.

**Project: IBP | Consumption and Spend Report Data Quality**

Completed:

**Findings escalated to delivery team**: Shared your findings with **Camila Furtado and team** for follow-up since they’re more engaged on that side.

**Stakeholder update**: Updated **Christian Carlan** with the findings and set expectations that you’ll share more as you learn additional details.

Ongoing:

**Stakeholder follow-ups**: Continuing to keep Christian posted as investigation progresses and more root-cause detail becomes available.

**Project: IBP | SSC Crew Count Model — Downstream Notebook Testing**

[DOE-1230] IBP | Testing latest crew count changes on downstream notebooks - Jira

Completed:

**ETL rerun** **(****ETL.ipynb****)**: Re-ran ETL.ipynb to validate the latest changes and move toward getting CCR crew count into the final training dataset.

**ETL debugging/unblocking**: Worked through multiple execution errors in the ETL notebook (including using Autopilot-driven modifications to bypass errors) to get runs completing.

Ongoing:

**Feature impact evaluation** **(SCD_CREW_COUNT)**: Continuing to assess the effect of the new SCD_CREW_COUNT feature (SHAP analysis, MdAPE comparison, and correlation/covariance ch

Mirielle T.

Contact Center:
**Weekly Report – April 09, 2026**

**Workforce Planning – North America (Royal)**

Prepared a presentation for the Data Science community to provide a high-level overview of the Workforce Planning project. The goal was to introduce the project vision, objectives, core components, and application phases, and to outline what each component delivers.

This session focused on building shared understanding of the overall solution. I am planning to return with a follow-up presentation dedicated to the FTE and headcount modeling in more detail.

**North America (****Royal) —**** Erlang A Model at 30****-Minute Intervals**

**Objective: **Extend the existing Erlang A headcount model from hourly to **30****-minute intervals** to better capture short-term demand peaks and improve staffing accuracy.

**Work Completed**

**1. Data Preparation**

Built a **30****-minute call****-volume proportion matrix** to allocate daily forecasted volumes into half-hour slots.

Built a **30****-minute weekly office****-hours matrix** to reflect service availability by LOB and time slot.

**2. Erlang A Model Adaptation (30****-Minute Intervals)**

**Pure Erlang A Functions (30****-Minute Adapted)**

abandon_prob_erlang_a: Computes probability of abandonment from steady-state distribution.

service_level_erlang_a: Calculates service level using the Garnett (2002) approximation.

calculate_metrics_erlang_a: Wrapper function returning all key Erlang A KPIs.

estimate_capacity_by_service_level_erlang_a: Estimates the minimum number of agents required to achieve a target service level *(accepts call volume per 30**-minute slot)*.

estimate_capacity_by_abandon_erlang_a: Estimates the minimum number of agents required to meet an abandonment target *(accepts call volume per 30**-minute slot)*.

**3. FTE Aggregation (30****-Minute Adapted)**

Determines maximum capacity per LOB based on historical FTE.

Aggregates staffing requirements to daily, weekly, and monthly FTE
using slots_per_shift = 16 (30-minute intervals).

**Next Steps**

**Calibrate the daily call****-volume forecast** to align with 30-minute intervals.

**Test and validate the Erlang A model** at the 30-minute granularity to ensure accuracy and stability.

**North America (Royal): App Phase III: Advanced app functionality and full model integration.**

**Ongoing Work: **Designing the end-to-end data workflow and defining how the application interacts with the models and data.

**What We’re Building: **A self-service FTE simulator “**Run Your Own ****FTE”**  embedded within the Workforce Planning app.The Workforce Planning team loads a call-volume forecast, sets staffing assumptions, and produces **monthly headcount (FTE) by Line of Business** in minutes **without needing data****-science support**.

**Step****-by****-Step Workflow**

**1. Select LOB**

Users select a single Line of Business or multiple LOBs combined.
This automatically loads:

The relevant call-volume forecast

The call-distribution (proportion) matrix

Baseline staffing assumptions

**2. Choose Time Granularity**

Users choose:

**Hourly (1****-hour)**, or

**30****-minute (30****-min)** intervals

Finer granularity captures short-term demand spikes that hourly averages can hide.

**3****.  Set**** Staffing Assumptions**

Users configure:

Average Handle Time (AHT)

Service Level target

Shrinkage

Customer patience

ASA

Baseline values are pre-filled. Any deviation from baseline is clearly flagged, and recent actuals are displayed as reference points.

**4. Override Office Hours (Optional)**

If a Line of Business adjusts operating hours (for example, peak season extensions or budget reductions), users can:

Set custom open and close times

Automatically trigger a recalculation of the call-distribution matrix

**5. Confirm Data & Run**

Before execution, a preview panel summarizes:

Date range

Selected LOBs

Total forecasted calls

Sample input rows

The user confirms before the model runs.

**6. View Results**

Outputs include:

Monthly FTE bar chart by LOB

Full assumptions recap

Optional sensitivity analysis (±10% / ±20%) on key parameters.

**7. Compare Scenarios (Optional)**

Users can:

Save each run as a named scenario

Modify assumptions and rerun

Compare **up to 8 scenarios side****-by****-side**

Comparisons include:

Grouped FTE charts

Assumption differences

Absolute and relative FTE deltas

**8. Save or Export Results**

Results can be:

Saved to Databricks using a **Draft → Preview → Final** tiered workflow

Exported as an Excel workbook containing results, assumptions, and metadata

**Why This Matters**

**Speed**: FTE answers in minutes instead of days of back-and-forth between teams.

**Agility**: Users can instantly test “what-if” scenarios — volume spikes, AHT changes, stricter service levels — during discussions.

**Ownership**: Business owners control the inputs and clearly see how each assumption impacts staffing.

**Accuracy**: The model validates inputs, flags deviations from baseline, warns against risky parameter combinations, and allows realistic overrides (such as office-hour changes), ensuring outputs reflect operational reality rather than outdated defaults.

**Success Criteria: **When complete, the Workforce Planning team will be able to:

**Generate an FTE result **

**Test any assumption change independently**

**Compare up to 8 scenarios in a single session**

**Explain every result**, with assumptions attached

**Share outcomes instantly** via Excel export or Databricks records

**Trust the output**, supported by validated inputs and guardrails

**Next Step: Meeting with the North America team** to review and validate the overall strategy.

**International and Casino International— App Phase II: Call Volume Forecast**

**Goal:** Build and integrate the call-volume forecasting models into the Workforce Planning application for International and Casino International.

**Ongoing Work:**

Reviewing and updating the feature-engineering framework originally developed for the North America call-volume forecasting models.

Tailoring feature engineering to reflect the specific needs of the International and Casino use cases, including the integration of international holiday calendars into the forecasting logic**. Covers markets: **Singapore, Germany, Ireland, France, Nordics (Sweden, Norway, Denmark, Finland), Italy, APAC, Spain, Other EMEA, Mexico, UK, Brazil, Australia.

**Next Steps:**
Continue refining feature engineering, review and validate the call-forecasting modeling functions, and conduct testing to deliver an initial run across all markets (without optimization or parameter tuning).

Caleb S.

**CLV Update**

**In Progress**

**CLV ETL Pipeline Revision** – Revising the CLV ETL pipeline in preparation for a PR to share requirements with Kiana's team. Key efforts include:

Developing a comprehensive deduplication strategy to isolate patterns and determine the correct rows to retain

Consolidating the ETL folder by merging redundant notebooks and deprecating unused ones

Documenting the complete pipeline and branching strategy to ensure reproducibility

**MSC Competitive Intelligence** – Assisting Corporate Strategy with ongoing analysis in support of MSC competitive intelligence initiatives.

**Completed**

**Caribbean Hurricane Risk Analysis** – Built an end-to-end hurricane risk analysis quantifying the likelihood and impact of hurricanes across 12 distinct Caribbean regions. The analysis encompasses:

Sourcing and scraping historical storm data from the National Oceanic and Atmospheric Administration (NOAA) hurricane database

Classifying storms by severity and damages, weighted by relative region-GDP impact

Computing a suite of risk metrics including storm probability by severity and time interval, return periods, return period trend comparisons across time horizons, expected cost of damages, expected annual cost, and relative risk indexes benchmarked against peer regions

Developing a PowerPoint deliverable that formats quantitative findings into regional table slides with key takeaways, along with overall summary tables and strategic insights

**Glen-Erik, Javier, Santiago**

**PROPEL**** (CEL)**

**Measurements**

Identified peculiarities or issues with the data affecting the measurements and working through those.

**Input data (revenue) **- There is negative revenue due to refunds and might not happen the same day of the purchase.

We are measuring purchases after an offer, if someone buys something before an offer and returns/cancels it after an offer, it shows up as negative revenue rather than cancelling itself out. *Javier almost finished solving this issue pending validation*

Some "refunds" have no matching purchase even looking at other dates. A few of these are huge, like -102 massages for -$15,000 for one cabin with no matching purchases. *Proposal: *ignore any negative numbers that exist that don't have a matching purchase.

Onboard purchases happening before a sailing or after a sailing is concluded (including timestamps that haven't yet happened as of now, like May & June 2026, we are in April), see above.

**PROPEL tool itself:**

test/control has always been assigned at the cabin level. People change cabins. There is no booking_id in the final offer assignment for traceability.

*Impact*: Someone in control group for one cabin can become test when they move to another cabin.

*Magnitude*: 1-4% bookings showing up in two cabins.

**Scheduling**

Analyzed schedule to find gaps in runs (missed runs) and currently working on a solution to address those gaps

Improved the handling of time gaps in the scheduling_table.

Removed duplicate records and refined the UTC timezone logic.

Reviewed and updated the logic for excluded ports.

Further smoothed the time difference calculations, enforcing a strict maximum margin of ±3 hours.

**Bugs:**

Missed an offer delivery due to bug in email notification code saying the wrong day (not matching the run itself) that occurs under rare circumstances. Identified the root cause and will hve a fix by 4/10 (today).

**Glen-Erik**

**PCP**** Pricing Automation: 1:1 Targeting**

**App / web:**

Created the script to feed offers using the new format that supports different notification and takeover texts rather than both being the same. The new format also cleans up a lot of unused fields and wrongly named ones. However, this will not be used for the first delivered offer to avoid delays since kafka to hybris logic and full end to end testing still needs to be done.

**Email:**

Aligned structure for SFMC, created synthetic data and an automated script to feed the data to a dev Kafka, DE created the kafka topic, and now Digital is working on feeding that to the SFMC api in dev.

**Eswar**

**RMA:**

Cel T4 Outlier PR to develop, didn't reflect changes in QA due to some reverts and cherry picks didn't push certain commits. So, fixed the issue by cherry picking specific commits which are not in sync and made T4 Outlier workflow run without any issues.

Productionized CEL TAP T4, OBR optimization_v2 workflows and paused TAP CEL GTY LEAD Optimization workflow.

Deployed SPI Factor analysis application and designed a proper Architecture to deploy apps across RMA/Data Science.

Prd CI/CD bundle deployments failure due to secret expiry. Followed up with Platform team and fixed the issue.

Inventory QA deployments fix due to RCI developers pushing same notebook with different formats and wrong yml structure.

Providing ML support debugging issues

Monitoring CI/CD deployments, PRs

Mert

NewBuild

Converted the Newbuild AI Agent framework into a reusable Python package for multiple projects.

Mert:
MIAP
Refactored the MIAP API to start using the new Agent Framework.
Started refactoring the MIAP web app to convert it from a Flask app to FastAPI/Next.js to align with the corporate tech stack.

Mert & Mashad

Deployment

Met with the Brand Deployment team to review their deployment optimization solution, which was jointly developed by our team. The RCI Brand Deployment team created a web application for deployment optimization; we agreed to host it within the MIAP app and support authentication and security.

Will:
MIAP
Finished adding SSC ships to the FACTS pipeline by replacing sensor-based weather measurements with expected weather at the nearest port, enabling FACTS models for ships without sensor data.
Added 9 new ships to the digital twin package.
Worked on adding shore power to Reza’s testing pipeline.
Working on improving SSC FACTS models using open weather data.

Ram:
MIAP
Fixed Stream Shipboard code to handle CMS and MDE.
Made code updates for PEPLINK, including adding a sample method.
Updated the PEPLINK data flow to land data into the same table used by MAS and other categories.
Resolved a weather station error in production by adding secrets to Key Vault and executing the fix.
Nearly completed analysis comparing Postgres and Kafka.

Arya:
MIAP
Repaired AHU and chiller pipelines.
Automated Capgemini processes.
Fixed a naming convention bug in the digital twin.
Built a script that scrapes Confluence documents as Markdown and uploads them to Databricks volumes.
Met with Francisco (Maritime Safety) to develop SORA using improved agentic frameworks.

Mahshad:
MIAP
Anomalies in the CS and ML systems are still ongoing, with an estimated impact of ~150 kW and ~400 kW on the HVAC side.
ML Energy Recovery Wheel (ERW) performance has decreased significantly; coordinating with the HVAC engineer to replace the entire ERW.
Met with the deployment team to discuss the itinerary optimization problem and assess opportunities to extend collaboration.
Fixed issues in the chillers pipeline.
Worked on resolving multiple pipeline bugs and failures.
Began integrating the chiller COP model into the MIAP application.

Reza:
MIAP
Implemented a proof of concept for a new residual boosting approach based on leg-level FACTS data and DTM-level digital twin outputs using historical data. Results are being tested and verified across different ships, years, and optimization approaches. The final product is being productionized as an online residual boosting package.
Worked on resolving service power area total target power mismatches.
Evaluated new FACTS-based models and diagnosed issues with itinerary table ship codes for Silversea ships.

Kevin

We worked on demand forecast if I recall (Kevin), finishing up KPI tracking that will be shared next week with Revenue Planning, Ignacio worked on Beverage Forecasting and we are pivoting to a new PRE model to ensure stable pricing recommendations, Michelle continuing to work on Category Gapping, and Doug "Detected, reported, troubleshot, validated effects of 24-hour live streaming outage. Systems returned to normal (almost) by Friday. Root cause, Kafka streaming outage. Why that happened? Still unanswered."

beat me to it. Those are good for RMA. for OBR 1:1 is being tested next week. mass promos development work completed to fix bug enabling shipboard promos as well as PCP. Advanced waterpark and RBC insights with digital conversion data. waterpark A/B test design completed to be shared with stakeholders at 3 pm today. beverage optimization for stly +5% developed but results are not in line with business expectation due to variability in WoW recommendations and magnitude. Revisiting beverage with more business rules.
