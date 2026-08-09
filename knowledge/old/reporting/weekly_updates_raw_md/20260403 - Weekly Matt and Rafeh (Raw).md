---
tags:
  - aagam_shah
  - ayon_ghosh
  - bao_le
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/customer_targeting_(e-commerce)
  - business_area/hr
  - business_area/newbuild
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/propel_targeted_offers_(cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/supply_chain_optimization
  - business_area/win-on-waste_(hotel_operations)
  - caleb_sharkey
  - camila_aichele
  - carlos_gonzalez_andarcio
  - cristian_villamarin-villamil
  - david_martinez
  - erick_alfaro
  - glen-erik_cortez
  - ignacio_villasmil
  - kevin_diaz
  - lamis_amer
  - mert_ersoz
  - michelle_manfrini
  - project/automation_upgrades
  - project/booking_propensity_models
  - project/casino_spend_analysis
  - project/category_gapping_optimization_3.0
  - project/cococay_integration_and_guardrails
  - project/expansion_of_medallia_reporting
  - project/forecasting_pipeline_expansion
  - project/gty-lead_fare_optimization_model
  - project/lead_prioritization_-_bk2cx_(rci_&_cel)
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/nps_drivers_analysis_for_alert_system
  - project/perfect_day_product_pricing
  - project/pre_4.0_elasticity_enhancements
  - project/promotional_workflow_automation
  - project/propel_targeted_offers_deployment
  - project/workforce_planning_tool
  - raw
  - srilekha_reddy_madupu
  - weekly_update
date: "2026-04-03"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2026-04-03

## Update 1

**Date:** 2026-04-03
**Business Area:** Project Axiom
**Business Project:** Expansion of Medallia Reporting
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[cristian_villamarin-villamil/overview_cristian_villamarin-villamil|Cristian Villamarin-Villamil]]

### Summarized Update

MyCruise Recommender (Cristian V., Erick A.)
Postgres Scaling Bottleneck (Cristian V.): Postgres load times for ForYou Calendar recommendations are taking 20–25 minutes per table, causing failures when dev and prod jobs overlap on the shared database. Cristian exhausted all optimization options (bulk inserts, partitioning, index timing). Escalated to Marcio/Platform.

### Raw Update

MyCruise Recommender (Cristian V., Erick A.)
Postgres Scaling Bottleneck (Cristian V.): Postgres load times for ForYou Calendar recommendations are taking 20–25 minutes per table, causing failures when dev and prod jobs overlap on the shared database. Cristian exhausted all optimization options (bulk inserts, partitioning, index timing). Escalated to Marcio/Platform.
Service Side Calendar Changes (Cristian V.): Service-side team requesting additional fields for the ForYou Calendar, which increases Postgres load times further. Cristian opposes but cannot continue blocking — will need to open backlog space to accommodate.
Apriori Expansion to New Product Categories (Cristian V.): The Apriori "frequently bought together" recommendation model — which mines purchase patterns to suggest products guests commonly book together — has been extended beyond its original product categories and deployed to dev. Waiting on Taylor's side for production integration.
Front-End Signal for AB Testing (Cristian V.): The DS team currently has no way to control or observe which recommendation model is deployed in production or which front-end use cases are calling it — making proper AB testing impossible. Cristian met with Rosie to explain this limitation; she agrees it's a problem. Lance (engineering) has sent encouraging signals about exposing this information via the front end. Cristian investigating whether the data is accessible via API.
Recommendations Simulator Web App (Erick A.): Built and completed a POC web app using Databricks Apps + Next.js that calls the recommendations API and visually displays results. Pricing recommendations (Kevin/Ignacio) and promotions (Glen Erik) teams have asked to partner, making this a shared web app across multiple DS use cases. Rafael Torres has also requested revenue data alongside recommendations.

---

## Update 2

**Date:** 2026-04-03
**Business Area:** Project Axiom
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

NPS Drivers / Weather Analysis (Osvaldo V.): Strategic perspective is that weather may not actually correlate with NPS typically despite guest comments. Weather Feature Engineering & EDA: Created per-port time series plots showing rainfall and temperature vs. NPS (Cozumel, PCC, CMM).

### Raw Update

NPS Drivers / Weather Analysis (Osvaldo V.): Strategic perspective is that weather may not actually correlate with NPS typically despite guest comments.
Weather Feature Engineering & EDA: Created per-port time series plots showing rainfall and temperature vs. NPS (Cozumel, PCC, CMM). Some visual patterns suggest temperature may correlate with NPS more than rainfall, but nothing conclusive — similar temperature drops at the same port sometimes affect NPS and sometimes don't. Still exploring whether weather pattern combinations (e.g., temp drop + rain, or high wind causing missed ports) explain the inconsistency.
Two-Stage Modeling Approach: Implemented a first model predicting negative weather topic mentions from weather features, then feeding that prediction into the NPS drivers model. Results are marginal — gap reduced slightly (65 to 59) but the first model performs poorly, injecting noise into the second model. Weather data alone is not yet producing meaningful model improvement.
Next Steps: Replace raw negative comment count target with weighted sentiment score feature (topic_mentions_neg_all) — accounts for both count and severity of negative comments. Retrain Model 1 and re-evaluate. Also adding composite weather features (rain × wind for storm detection). This remains exploratory work.
Email Reports (Rodrigo B.)
Port Email (Rodrigo B.): Sent Miami port email to Port Operations teams and presented Port emails to VP Port Services Jaime Casillo. Stakeholders expressed interest in expanding scope to include all turn ports. Port email PDFs now saving to SharePoint.
Port Email Data Pipeline for PowerBI (Rodrigo B.): New task — building a process to save port report data to a Databricks table on a weekly/monthly basis, enabling Port Operations analysts to consume DS-controlled data rather than replicating pipeline logic independently.
Abandoned Cart Dashboard (Rodrigo B.): Finishing stakeholder-requested improvements — added new topics (political unrest, war), translated non-English comments via LLM (using language detection package to only translate non-English), standardized travel agency names in word clouds, added weekly/monthly trend toggles for booking factors and completion rates, integrated new QAD39 question. Relabeled comments from January 2026 onward with new topics (avoided full history relabel since topics reflect recent events).
Meta Data Extraction (David M.)
Guest Logs Categorization (David M.): Corrected reclassification estimate — 4% of records (not 7%) require alternate model processing, at ~$800 cost. Will run full funnel analysis using the new PRD gold table, tracking worker counts per pipeline step since 2023.
Embeddings / Vector Storage Architecture: Team discussed options — Databricks Vector Search (cost concern at scale), PG Vector (David has experience), ChromaDB (free, local SQLite-like — Osvaldo's suggestion), Qdrant (Docker-based), or flat quantized embedding files on Lambda with GPU similarity search. David exploring FAISS for clustered/indexed retrieval. Embeddings will serve multiple use cases: RAG, D3JS clustering visualization, and classification model inputs.

---

## Update 3

**Date:** 2026-04-03
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - BK2CX (RCI & CEL)
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

Legacy Pipeline Restored (Erick A.): Platform team (Marcio) fixed the ADLS permissions issue that had broken the existing WebFunnel lead scoring pipeline. The legacy process is now back online. Pipeline Rewrite (Erick A.): Erick is rewriting the WebFunnel lead scoring pipeline from scratch, restructuring the codebase to be optimized for AI-assisted coding.

### Raw Update

Legacy Pipeline Restored (Erick A.): Platform team (Marcio) fixed the ADLS permissions issue that had broken the existing WebFunnel lead scoring pipeline. The legacy process is now back online.
Pipeline Rewrite (Erick A.): Erick is rewriting the WebFunnel lead scoring pipeline from scratch, restructuring the codebase to be optimized for AI-assisted coding. ~90% complete, still in progress.

---

## Update 4

**Date:** 2026-04-03
**Business Area:** Win-on-Waste
**Business Project:** Forecasting Pipeline Expansion
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

Specialty Pipeline Architecture:
Developed all modules for a new specialty pipeline architecture to enhance feature engineering and overall forecast quality. Added outlier detection to improve bulk accuracy, with specific focus on identifying most-consumed and least-consumed items across ship venues. Forecast Accuracy Reporting:
Created a new comprehensive accuracy report using NAE (Normalized Absolute Error) with decile-based consumption volume analysis.

### Raw Update

Specialty Pipeline Architecture:
Developed all modules for a new specialty pipeline architecture to enhance feature engineering and overall forecast quality. Added outlier detection to improve bulk accuracy, with specific focus on identifying most-consumed and least-consumed items across ship venues.
Forecast Accuracy Reporting:
Created a new comprehensive accuracy report using NAE (Normalized Absolute Error) with decile-based consumption volume analysis. The report compares model forecasts against a simple moving average (naïve baseline) across the last three itineraries, clearly highlighting relative model performance.
This report feeds into Power BI, enabling an integrated, stakeholder-facing dashboard. Individualized ship- and venue-level reports will be distributed to IT Excellence, Chefs, and F&B Operations Excellence teams.
Interport Pipeline Validation:
Conducted focused unit testing on the Interport PL, particularly the ETL components, to ensure accuracy and correctness of complex joins throughout the extended data pipeline.
Bar Pipeline Hotfix:
Delivered a production hotfix to the Bar forecasting pipeline in response to a ServiceNow ticket raised by a ship, resolving the reported issue promptly.

---

## Update 5

**Date:** 2026-04-03
**Business Area:** NewBuild
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

Mert:
NewBuild: Newbuild Enterprise Observatory
Deployed a fully working AI app for the Newbuild Enterprise Observatory; fixed all bugs and implemented performance enhancements to bring it to a demo-ready state for stakeholders.

### Raw Update

Mert:
NewBuild: Newbuild Enterprise Observatory
Deployed a fully working AI app for the Newbuild Enterprise Observatory; fixed all bugs and implemented performance enhancements to bring it to a demo-ready state for stakeholders.

---

## Update 6

**Date:** 2026-04-03
**Business Area:** NewBuild
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

Continued progress on MIAP REST API cost management, incorporating platform team updates; implementation is in progress and targeting closure next week. Extracted historical HPP tag data from Eniram and loaded it into downstream Silver tables. Working on optimizing Silver analytics; the current approach requires redesign due to missing source-category partitioning.

### Raw Update

Continued progress on MIAP REST API cost management, incorporating platform team updates; implementation is in progress and targeting closure next week.
Extracted historical HPP tag data from Eniram and loaded it into downstream Silver tables.
Working on optimizing Silver analytics; the current approach requires redesign due to missing source-category partitioning.
MIAP
Reza:
Developed a function to merge voyage legs with cruising.
Added an optimization method to forecast tables.
Added Silver Ray to the HPP trends table and defined its HPP baseline.
Evaluated the no-optimization fuel forecast platform and identified improvement areas.
Collaborated with the team to improve forecast accuracy and performance.
Prepared train/test datasets and conducted EDA.
Tested different residual modeling approaches to improve fuel forecast accuracy.

Mahshad:
MIAP
HM electrical usage in AHUs dropped by 500 kW; however, since the system is entering dry dock, this reduction will not be considered a confirmed saving.
Started developing individual chiller COP models.
Debugged the overall chiller COP model pipeline to improve stability and accuracy.
Debugged the MIAP application for plotting errors; identified issues related to incorrect tag mapping and coordinated with the tag-mapping team to resolve them.
Met with the deployment team and established clear goals for ongoing bi-weekly collaboration meetings focused on optimization.
Scheduled a meeting with the GMO leadership team to understand their perspectives and expectations for our team.
Worked on the API and data connection between the GMO platform and the MIAP application to improve data rendering speed and reduce system failures.
As this was my onboarding week, attended onboarding sessions and meetings and completed initial learning activities.

Will:
MIAP
Created the first formulation of emissions-based call-time optimization for the Deployment Optimization project (new project).
Consulted with the deployment team on port sequence optimization formulation (new project).
Added SSC ships to the FACTS pipeline (foundational work completed; a bug remains in the feature data).
Added SFOC figures to the MIAP REST API; pending integration into the web app.
Completed minor bug fixes in the web app.
Working on adding shore power support to Reza’s digital twin testing pipeline.
Added leg and optimization validation support to the digital twin front end.

Arya:
MIAP
Restructured code for no-optimization mode in the digital twin (now production-ready).
Completed initial testing with no optimization.
Added AHU information to the SQL database for Radiance-class ships.
Built a framework for a Databricks job monitoring agent.
Added BR, JW, and SR to AHU analytics.
Improved SFOC curves.
Added predictive analytics for forecasting consumption rates in the live fuel tracker.

Brendan:
MIAP
Worked with Ram to troubleshoot the MIAP deployment profile ETL job that had been failing for over two months; pushed a fix to production.
Deleted stale model versions to prevent exceeding Databricks model version quotas.
Supported MIAP developers as needed.

---

## Update 7

**Date:** 2026-04-03
**Business Area:** Supply Chain
**Business Project:** CocoCay Integration and Guardrails
**People:** [[david_martinez/overview_david_martinez|David Martinez]], [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

On Thursday, Databricks computing clusters are not running in both the dev-da2i-dbricks and dev-da2i-alpha-dbricks environment, and it caused some job clusters to fail early this morning for IBP/E-Commerce Customer targeting. I do not know if other Databricks environments are suffering the same problem, but I can successfully start clusters in dev-RCI-Revenue-Mgmt-dbricks and Doug reported RM pipelines ran this morning without an issue. So the problem does NOT appear to be global.

### Raw Update

On Thursday, Databricks computing clusters are not running in both the dev-da2i-dbricks and dev-da2i-alpha-dbricks environment, and it caused some job clusters to fail early this morning for IBP/E-Commerce Customer targeting. I do not know if other Databricks environments are suffering the same problem, but I can successfully start clusters in dev-RCI-Revenue-Mgmt-dbricks and Doug reported RM pipelines ran this morning without an issue. So the problem does NOT appear to be global. I am also not seeing any outages reported on Azure Databricks.
Cause: Platforming Engineering worked on both workspaces last night. I created a managed identity for both workspaces to talk with the new foundry using managed identity to improve security and bypass secret expirations. It looks like it affected the access to the storage.The dev-da2i-alpha-dbricks  looks like is back to normal.
My Response: I like avoiding API keys and SP secrets. in the future though, if we are testing something in the new environment, please let us know in advance. Im just glad we have the fix identified and can get everyone running again.
Bottom-Line Conclusion: This was preventable with better communication, but exposes the DS team cannot have "prod" jobs in the development environment. This is bad hygiene and I will be pushing to have all prod jobs moved to an isolated "prod" environment. This mitigates risk to prod jobs if you need to test something in our dev environments. No way you could have known and this one is on me, and I will push to fix and tighten expectations. ive asked my team before, but will now set expectations to prioritize (like the Sharepoint fix)

---

## Update 8

**Date:** 2026-04-03
**Business Area:** Supply Chain
**Business Project:** CocoCay Integration and Guardrails
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Completed refactoring of a large 8,000 plus line monolith notebook into 9 notebooks. Refactoring reduced the weekly compute runtime by 5 hours per week and also provides much greater readability and easier maintenance. The nine notebooks are orchestrated by a master notebook which writes a file at the start of the run and logs each successfully completed notebook.

### Raw Update

Completed refactoring of a large 8,000 plus line monolith notebook into 9 notebooks. Refactoring reduced the weekly compute runtime by 5 hours per week and also provides much greater readability and easier maintenance. The nine notebooks are orchestrated by a master notebook which writes a file at the start of the run and logs each successfully completed notebook. Should any notebook fail in production in the future, this architecture allows for us to update the code only in the failing notebook, retrigger the master notebook, and skip the notebook steps that ran successfully going directly to the failing notebook step, allowing for faster recovery in the event of a production failure. Future work involves directing Photon compute only on the notebooks providing more than a 2x speed up to further reduce compute costs and runtime. Prior analysis showed 3 of the 9 notebooks would benefit from Photon.
Completed code migration of reading and writing to Sharepoint using new Graph API functions from legacy process to ensure production code continues to run without error. Updated over 20 notebooks and performed E2E testing to ensure new functions worked properly. This was a HUGE success and worth highlighting that we prevented failures from ACS retirement.
Work in progress on refactoring Finance tool, consisting of 5 notebooks with about 10,000 lines of code to 13 notebooks. Expected benefits of reducing compute time and reduce compute cost, easier to maintain and read code are the outcomes that will be delivered from this work. The 13 notebooks for the new refactored finance tool code are completed and validation of data is in progress.
Enhanced the COCOCAY demand model by adding five year-over-year lag features: CONSUMPTION_4WKMA_LAG_1YR, CONSUMPTION_4WKMA_LAG_2YR, NORMALIZED_CONSUMPTION_LAG_1YR, NORMALIZED_CONSUMPTION_LAG_2YR, and YOY_GROWTH_RATE. These were integrated into feature engineering, backtesting, aggregation, and monotonic model constraints, replacing a simpler prior-year approximation and improving the model’s ability to handle recurring seasonal demand. The same features were also added into the Probatus feature selection workflow so they can be properly evaluated during feature selection.
Added high-variance product tracking output to COCOCAY so products exceeding the 90% variance threshold can now be logged for before-and-after comparison as the new lag-based logic is evaluated.
Completed the pickup of live sharepoint file to be integrated in the order creation actual quantity needed equation. There were doubts from shipboard team due to actual quantity needed not being the amount they expected so adding in the MIN PAR based on certain criterias allows more confidence from the team.
Enhanced the order creation workflow by moving the RCI CEL Order Creation Equation notebook from tier 1 to tier 3, allowing it to run in parallel with Finance Tool notebooks instead of blocking them sequentially. This improves orchestration efficiency and reduces unnecessary delays in downstream processing.
SSC FINANCE TOOL: Cleaned up large sections of commented-out legacy logic across multiple notebooks, including old ESG proration logic, deprecated voyage mapping rules, unused inventory queries, outdated brand processing, debug display cells, and an obsolete read_table_version function. This cleanup improves readability, reduces confusion, and makes the workflows easier to support over time.
ETL SSC Aggregate Bid Data: Paige identified issues where source file, weight, comments columns weren't appearing as they should. I identified the issue was the way that Fanny and team had their excel files. They included headers AND subheaders which didn't allow us to pickup the right information. This work is still in progress as there are over 50 files with similar patterns.
Graph API: Added read_sharepoint_excel() helper function that downloads an Excel file to a temp directory, reads all sheets into a dict of pandas DataFrames using openpyxl, and automatically cleans up the temp file. This allowed the sharepoint to azure pipeline that runs weekly on Thursdays to run smoothly.
Shipboard team does not want the spend per day table to have SUSHI/RAW ON FIVE data as when it was discussed, they agreed to not get penalized for over spending in this area. Instead we add a average total voyage $ value over the last 12 months to show what they have spent in this venue. This is to be added to the override tracking and spend per day KPI tables
PRD SILVER -> PRD GOLD for cococay, uniforms, and medical for better accuracy

---

## Update 9

**Date:** 2026-04-03
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

IBP | Crew Count Decision (Uniform vs. Oracle)
Ticket: [DOE-1342] IBP | Crew Count Decision: uniform table vs. fidelio table (which is more stable to create a forecast)
URL: DOE-1342: IBP | Crew Count Decision: uniform table vs.

### Raw Update

IBP | Crew Count Decision (Uniform vs. Fidelio vs. Oracle)
Ticket: [DOE-1342] IBP | Crew Count Decision: uniform table vs. fidelio table (which is more stable to create a forecast)
URL: DOE-1342: IBP | Crew Count Decision: uniform table vs. fidelio table (which is more stable to create a forecast)TESTING | QA | 90%
Completed
Created a People Analytics Work Order request and are awaiting response.
Comment: DOE-1342: IBP | Crew Count Decision: uniform table vs. fidelio table (which is more stable to create a forecast)TESTING | QA | 90%
Shared crew-count data-quality findings via Databricks dashboard for a specific ship filter.
Dashboard link (from your comment):
https://adb-6976407220220490.10.azuredatabricks.net/dashboardsv3/01f126ef31a11b9ab5f2496d72458139/published?o=6976407220220490&f_26ec119a~ship_filter=Silver%2520Cloud
Comment: DOE-1342: IBP | Crew Count Decision: uniform table vs. fidelio table (which is more stable to create a forecast)TESTING | QA | 90%
Ongoing
Aligning with Yan / Crew Planning: you noted you were waiting to meet with Yan and planned to leave the item open for April sprint.
Comment: DOE-1342: IBP | Crew Count Decision: uniform table vs. fidelio table (which is more stable to create a forecast)TESTING | QA | 90%
Escalating inconsistencies back to reporting: you want to speak with Yan to get clarity on inconsistencies observed.
Comment: DOE-1342: IBP | Crew Count Decision: uniform table vs. fidelio table (which is more stable to create a forecast)TESTING | QA | 90%
Potential source-of-truth shift to Oracle: based on Yan’s conversation with Crew Planning, you captured that Oracle is their source of truth, and once DE receives Dom’s query, it can be implemented directly from Oracle in Databricks.
Comment: DOE-1342: IBP | Crew Count Decision: uniform table vs. fidelio table (which is more stable to create a forecast)TESTING | QA | 90%

---

## Update 10

**Date:** 2026-04-03
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

IBP | Testing latest crew count changes on downstream notebooks
Ticket: [DOE-1230] IBP | Testing latest crew count changes on downstream notebooks
URL: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Completed
Reviewed the uniforms model codebase and documented that there’s an initial learning curve due to size/complexity. Comment: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Identified required changes + downstream consequences for integrating the crew count forecast, and laid out three integration options:
Separate column added to final training data (cleaner/explainable but slower to implement)
Replace uniforms-derived crew count (risk losing aggregate uniform demand signal)
Supplement current uniforms-derived crew count (current approach mixes two value types)
Comment: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Captured your understanding of final training data table and linked the dataset being used:
Table link (from your comment):
https://adb-6976407220220490.10.azuredatabricks.net/explore/data/dev_datascience/ibp_da2i/ssc_uniform_weekly_consumption_voyage_data?o=6976407220220490&activeTab=sample
Comment: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Ongoing
Clarifying schema/feature meaning: you started a thread specifically on the “TIME” column, indicating more investigation/definition needed. Comment: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Final decision pending on how to integrate crew count forecast into the training dataset (separate vs replace vs supplement), given tradeoffs you described.

### Raw Update

IBP | Testing latest crew count changes on downstream notebooks
Ticket: [DOE-1230] IBP | Testing latest crew count changes on downstream notebooks
URL: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Completed
Reviewed the uniforms model codebase and documented that there’s an initial learning curve due to size/complexity.
Comment: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Identified required changes + downstream consequences for integrating the crew count forecast, and laid out three integration options:
Separate column added to final training data (cleaner/explainable but slower to implement)
Replace uniforms-derived crew count (risk losing aggregate uniform demand signal)
Supplement current uniforms-derived crew count (current approach mixes two value types)
Comment: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Captured your understanding of final training data table and linked the dataset being used:
Table link (from your comment):
https://adb-6976407220220490.10.azuredatabricks.net/explore/data/dev_datascience/ibp_da2i/ssc_uniform_weekly_consumption_voyage_data?o=6976407220220490&activeTab=sample
Comment: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Ongoing
Clarifying schema/feature meaning: you started a thread specifically on the “TIME” column, indicating more investigation/definition needed.
Comment: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress
Final decision pending on how to integrate crew count forecast into the training dataset (separate vs replace vs supplement), given tradeoffs you described.
Comment: DOE-1230: IBP | Testing latest crew count changes on downstream notebooksIn Progress

---

## Update 11

**Date:** 2026-04-03
**Business Area:** CLV
**Business Project:** Casino Spend Analysis
**People:** [[caleb_sharkey/overview_caleb_sharkey|Caleb Sharkey]]

### Summarized Update

In Progress
2025 Actuals Validation – Completing validation of full 2025 Actuals data to enable the final rerun of our CLV pipeline. Competitive Situational Assessment Support (CS):
MSC Compendium & Fleet Analysis – Validating and developing visuals for the MSC compendium. Leveraging our previously validated fleet model to substantiate claims around MSC's future APCDs by region.

### Raw Update

In Progress
2025 Actuals Validation – Completing validation of full 2025 Actuals data to enable the final rerun of our CLV pipeline.
Competitive Situational Assessment Support (CS):
MSC Compendium & Fleet Analysis – Validating and developing visuals for the MSC compendium. Leveraging our previously validated fleet model to substantiate claims around MSC's future APCDs by region. Additionally, constructed an organizational chart of top MSC leadership, informed by public interviews and articles mapping inner-circle relationships.
2040 Vision Analysis – Conducting forward-looking analysis using the most current 2025 CLV data to support our 2040 strategic vision. This includes segmented cuts on family age distributions (older vs. younger parents) and an assessment of how differing value metrics influence our long-term outlook. Also analyzed U.S. state-level sourcing distributions and fly/drive segmentation to identify high-potential regions.
Completed
End-to-End Validation Overhaul – Reconfigured validations across the full table journey to align against EPM, Revenue Reports, and VCAP wherever source data is available, strengthening overall data robustness and trustworthiness. Delivered a comprehensive Excel workbook covering:
Core Measures (validated across the entire table journey): PCDs, Pax, NTR, OBR, APD
Supplemental Measures:
Distinct sailings
Age distribution
Group sizes
Deployment by meta product
Average sail length
Book-to-sail window methodology & density
Booking type split
Meta + RDSS channel proportions

---

## Update 12

**Date:** 2026-04-03
**Business Area:** Customer Targeting
**Business Project:** Booking Propensity Models
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]], [[bao_le/overview_bao_le|Bao Le]]

### Summarized Update

research tsetlin machines algorithm for building explainable models
finetune optimal sampling for models training
Clickstream Data & Feature Engineering
Resolved initial challenges with loading clickstream data. Even after filtering by consumer ID and removing ~80% of columns, the ingestion/checkpoint table creation failed due to data size constraints. Further pruned the dataset down to 30 essential columns, enabling successful construction of clickstream session-level features tied to consumer IDs.

### Raw Update

research tsetlin machines algorithm for building explainable models
finetune optimal sampling for models training
Clickstream Data & Feature Engineering
Resolved initial challenges with loading clickstream data. Even after filtering by consumer ID and removing ~80% of columns, the ingestion/checkpoint table creation failed due to data size constraints.
Further pruned the dataset down to 30 essential columns, enabling successful construction of clickstream session-level features tied to consumer IDs.
Successfully created the first checkpoint table.
Next Steps: Review with Carlos to validate which clickstream fields are required for enriched session-level feature development and refine feature set accordingly. This feature set would technically be used in the booking propensity model along with the upcoming journey scoring model.
Booking vs. Web Propensity Model Comparative Analysis
Completed the first full run-through of exploratory data analysis comparing booking propensity and web propensity models.
Developed a scoring-based segmentation approach to identify consumers most likely to respond to targeted offers.
Identified a high-opportunity segment:
Consumers categorized as low propensity in the booking model, but medium/high propensity in the web model.
This segment demonstrated strong potential responsiveness to targeted offers, even after incorporating uplift gain scores.
Found that ~21% of consumers within these combined segments are “persuadable”:
They fall below the booking propensity threshold under the base model.
When uplift is incorporated, they exceed the threshold and become likely bookers if targeted.
Identified additional consumer groups that are effectively “blind spots” to one model but captured by the other, reinforcing that a combined modeling approach provides stronger coverage than either model independently. Some of these consumers include loyal offline consumers who have strong history/profiles but prefer to book through other avenues.
Stakeholder Engagement & Next Steps
Developed and presented a PowerPoint deck to the e-commerce and marketing teams outlining findings and segmentation strategy.
Next Steps:
Backtest a January consumer sample using a 3-month booking horizon to validate booking lift.
Evaluate integration into upcoming targeted offer POC (in-session offer valid for 3 days).
Continue development of next week’s presentation materials for Matt.
Integrate app features into booking propensity models

---

## Update 13

**Date:** 2026-04-03
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** Automation Upgrades
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]], [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

##########################################################
Summary: Azure ACS Retirement Mitigation – Graph API–Based Access Model
##########################################################
Your team has proactively mitigated the Azure ACS retirement risk for SharePoint integrations by transitioning to a Microsoft Graph API–based access model, backed by Azure Entra ID service principals and IAM-managed, site-scoped permissions. This approach replaces legacy SharePoint “backdoor” ACS mechanisms with a secure, durable, Microsoft-supported pattern that avoids production outages across Data, AI, and Revenue Management pipelines. What Is Being Retired (and Why It Matters):
Azure ACS enabled two legacy SharePoint access patterns:
(1) Hidden SharePoint AppInv / client-ID backdoor
(2) SharePoint-created client credentials
Both are being fully retired, creating a material risk of read/write failures for pipelines that ingest from or publish to SharePoint (pricing automation, IBP, PRE, Power BI refreshes, etc.).

### Raw Update

##########################################################
Summary: Azure ACS Retirement Mitigation – Graph API–Based Access Model
##########################################################
Your team has proactively mitigated the Azure ACS retirement risk for SharePoint integrations by transitioning to a Microsoft Graph API–based access model, backed by Azure Entra ID service principals and IAM-managed, site-scoped permissions. This approach replaces legacy SharePoint “backdoor” ACS mechanisms with a secure, durable, Microsoft-supported pattern that avoids production outages across Data, AI, and Revenue Management pipelines.
What Is Being Retired (and Why It Matters):
Azure ACS enabled two legacy SharePoint access patterns:
(1) Hidden SharePoint AppInv / client-ID backdoor
(2) SharePoint-created client credentials
Both are being fully retired, creating a material risk of read/write failures for pipelines that ingest from or publish to SharePoint (pricing automation, IBP, PRE, Power BI refreshes, etc.).
Power App & Shared Service Principals:
Existing Power App–backed service principals remain valid.
What changes is how those principals are authorized to SharePoint:
They must now be explicitly granted access to each SharePoint site via IAM using Graph.
This is why your solution does require IAM support to add each SharePoint to the service principal backing the Power App.

---

## Update 14

**Date:** 2026-04-03
**Business Area:** Customer Targeting
**Business Project:** Booking Propensity Models
**People:** [[david_martinez/overview_david_martinez|David Martinez]]

### Summarized Update

Context & Constraints
Cecilia is pushing to accelerate the use of AI to improve SSC marketing effectiveness. There is $60K available to fund a Data Science contractor, but there is limited delivery bandwidth from Kristin V’s E-Commerce team through year-end, driven by the ongoing SSC migration to Adobe Clickstream and CDP (Email in early Q4, Web in late Q4). As a result, near-term AI work must be lightweight, low-dependency, and future-proofed to avoid rework once the CDP/Adobe foundation is in place.

### Raw Update

Context & Constraints
Cecilia is pushing to accelerate the use of AI to improve SSC marketing effectiveness. There is $60K available to fund a Data Science contractor, but there is limited delivery bandwidth from Kristin V’s E-Commerce team through year-end, driven by the ongoing SSC migration to Adobe Clickstream and CDP (Email in early Q4, Web in late Q4). As a result, near-term AI work must be lightweight, low-dependency, and future-proofed to avoid rework once the CDP/Adobe foundation is in place.
Strategic Recommendation
Rather than waiting for the CDP migration to complete, the recommendation is to build a small set of focused, high-value AI models now, with full awareness and oversight from Kristin’s team, and design them so they are adjustable and extensible once SSC migrates to Adobe Clickstream and CDP. This allows SSC to begin capturing value immediately while ensuring alignment with the long-term Martech and data architecture.
Proposed Focus: Two AI Verticals
1) Customer Marketing (Primary Near-Term Focus)
Scope
CRM, Direct Mail, Email, Call Campaigns
Sell Classic vs. Expedition cruise products
Begin groundwork for Land Programs
Support loyalty-driven upsell and premium differentiation
Key Design Principles
Focus on two SSC segments, not all guests:
Classic
Expedition
Treat Classic and Expedition as distinct populations with limited overlap.
Use internal data only (e.g., RFM, booking history, product affinity), avoiding external data dependencies until CDP is live.
Models should be channel-agnostic now, but CDP-ready later.
Candidate Models
12-Month Booking Propensity Models
Separate models for Classic vs. Expedition
Score likelihood to book within the next 12 months
Upsell & Premium Potential
Identify guests likely to:
Upgrade to Upper Suite
Purchase longer cruises
Next Best Cruise / Destination
Dataset may be small for pure destination propensity
Use 1:1 modeling combined with market basket analysis
Example: Guests who book Arctic/Antarctic itineraries → adjacent expedition offerings
Activation Today
Scores land in Jakala Data Lake
Used for:
Direct mail & email across ~13 destinations
Call campaigns (agents receive prioritized guest lists)
Why This Works Now
Jakala already holds SSC transactional data and runs a large outbound operation (~30% of team focused on lead prioritization).
Historical precedent exists (e.g., Bob Becker’s “Next Best Destination” work when lead volume was constrained).
Minimal dependency on real-time web/email behavior until CDP migration completes.
2) International & Performance Testing (Secondary / Opportunistic)
SSC has access to global international models already in use.
Recommendation is to reuse and adapt existing global models for:
Test-and-learn in select international markets
Performance benchmarking for Classic vs. Expedition segments
Keeps scope limited while still enabling learning ahead of broader rollout.
Martech & Data Alignment (Critical Guardrails)
Jakala models today
Need clarity on:
What features are currently being used
Whether any web/email signals are ingested today
Open Questions to Answer (by April 15)
What features are Jakala’s current SSC models using?
Are we ingesting any web or email activity for SSC today?
How should web/email behavior be incorporated into AI models post-CDP?
Is Kristin’s team planning only base booking propensity and spend models, or a broader model ecosystem?
CDP Migration Alignment
Near-term models should:
Avoid tight coupling to legacy clickstream structures
Be modular so web/email features can be added, not rewritten, post-migration
Target state:
Early Q4: Email signals integrated
Late Q4: Web behavior integrated via Adobe Clickstream
Supporting Workstreams
Valtech (with David Martinez)
Assessing current Martech stack and how to use it for future growth
Goal: build a robust marketing hub for E-Commerce and consumer communications
Kristin’s Team
Will define the process for Proof-of-Value
Build a model repository to ensure governance, reuse, and transparency as AI usage scales
Bottom Line
We should not wait for the CDP migration to finish before applying AI.
Use the $60K DS contractor to build a small, targeted set of SSC marketing models now.
Keep scope tight (Classic vs. Expedition), data internal, and architecture adjustable.
Ensure Kristin’s oversight so near-term work cleanly feeds the Adobe Clickstream/CDP future state.
This balances immediate value, organizational bandwidth constraints, and long-term platform alignment.

---

## Update 15

**Date:** 2026-04-03
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

Weekly Report – April 02, 2026
Workforce Planning – North America (Royal). 1.FTE Modeling — Calibration, Validation, and Full Run
We calibrated the Erlang A model  with Loyalty and Star LOBs. To validate the end-to-end workflow and confirm that the model produced reasonable results, we executed the model using the forecasted call volume, then we extended the model run to **all LOBs**.

### Raw Update

Weekly Report – April 02, 2026
Workforce Planning – North America (Royal).
1.FTE Modeling — Calibration, Validation, and Full Run
We calibrated the Erlang A model  with Loyalty and Star LOBs.
To validate the end-to-end workflow and confirm that the model produced reasonable results, we executed the model using the forecasted call volume, then we extended the model run to **all LOBs**.
The Model **Erlang A by Service Level** variant turned out to be the best-performing model. Erlang A is a queueing-based forecasting model used in contact centers to determine staffing needs, wait times, and abandonment by explicitly modeling how long customers are willing to wait before hanging up.
The Modeling architecture was modified to account for more input as  the Average Patience Time and the Average Answer Speed. which is why those parameters were added to the Assumptions App page in this session. As of FTE Modeling, we set the **Service Level target to 70%** across all LOBs as the baseline for staffing calculation.
The resulting FTE numbers from the model run were then used to update the app, replacing the previous FTE data with the new model-derived headcount.
2.Added Three New Planning Inputs to the Assumptions Page
Previously, the Assumptions page only captured four parameters: Average Handle Time, In-Office Shrinkage, Out-of-Office Shrinkage, and Abandon Target. We added three more:
- Service Level Target — the percentage of calls that should be answered within a set time
- Average Patience Time — how long a caller typically waits before hanging up
- Average Answer Speed— how quickly calls are picked up on average
Why it matters: These three parameters are essential inputs for the Erlang A staffing model that we're building next. Without capturing them here, planners wouldn't be able to run headcount simulations. Now the full set of assumptions is collected, saved, and audited in one place.
3. Fixed the "Save" Feature for Assumptions
After adding the new fields, saving broke because the database table still had the old structure (6 columns instead of 9). We fixed this so that:
-When **overwriting** a table, the app now rebuilds it from scratch with the correct columns — no more mismatches.
- When **appending** to the backup/audit table, the app automatically detects any missing columns and adds them before writing — so historical records are preserved and new records include all fields.
**Why it matters:** The app won't break when we add new parameters in the future. The save logic adapts to whatever columns the data has, which saves development time going forward.
4. Upgraded the FTE Forecast Data to More Accurate Tables
The app was reading staffing forecasts from an older set of data tables. We switched both the **monthly** and **weekly** FTE data to new tables that contain headcount numbers computed from an improved, more accurate call volume forecast:
- Monthly FTE → new table with refined monthly staffing numbers
- Weekly FTE → new table with refined weekly staffing numbers.
5.Next Step — Build the Erlang A Model at 30-Minute Intervals
The current model runs at a **1-hour interval** granularity. The next step is to build a **30-minute interval** variant of the Erlang A model.
What the 30-minute model requires:
1. Calibrate the daily call volume forecast to 30-minute intervals.
2. Build a 30-minute call volume proportion matrix
3. Build a 30-minute weekly hourly office matrix
4. Adjust the Erlang A mathematical functions.
5. Run the FTE calculation at 30-minute granularity
6.Next Step — Move to App Phase 3 ("Run Your Own FTE") Instead of Manual Scenario Testing.
Rather than spending time running different scenarios manually — changing assumption values (AHT, shrinkage, SL target, patience, etc.) one by one in the notebook, re-running the model, and pushing updated FTE numbers to the app each time — My suggestion is to move directly to **App Phase 3: Run Your Own FTE**.
The Phase 3 gives planners self-service.  Once the Erlang A model is embedded in the app, any planner can adjust assumptions , run the model and see the impact on FTE — without filing a request or waiting for someone else to run the model.

---

## Update 16

**Date:** 2026-04-03
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** Unidentified

### Summarized Update

Recall of the Team Feedback & Action Items
The team provided several valuable suggestions:
Add tables to visualize the call volume proportion split at each level (Market, Brand, and LOB)
Remove or consolidate certain LOBs (such as River and Outbound)
Display the sum of LOB-level adjustments in red when they exceed the total market volume
Re-introduce historical call volume from the same period last year in the call-volume adjustment section of the app
1. Split Proportion Tables — Visibility into Forecast Distribution
Added new "Split Proportion" tables to the Call Volume Forecast page, in both the **Forecast by Brand & Market** and **Forecast by Market & Line of Business** tabs. These tables sit between the Historical and Forecast views.

### Raw Update

Recall of the Team Feedback & Action Items
The team provided several valuable suggestions:
Add tables to visualize the call volume proportion split at each level (Market, Brand, and LOB)
Remove or consolidate certain LOBs (such as River and Outbound)
Display the sum of LOB-level adjustments in red when they exceed the total market volume
Re-introduce historical call volume from the same period last year in the call-volume adjustment section of the app
1. Split Proportion Tables — Visibility into Forecast Distribution
Added new "Split Proportion" tables to the Call Volume Forecast page, in both the **Forecast by Brand & Market** and **Forecast by Market & Line of Business** tabs. These tables sit between the Historical and Forecast views.
**Why it matters:**
Previously, users could see the total market-level forecast and the brand/department-level forecast, but there was no easy way to understand *how* the market forecast was being distributed. The new Split Proportion tables show the percentage breakdown — for example, how much of the UK market forecast goes to Royal vs Celebrity, or how much goes to Reservations vs Customer Service. This transparency helps planners validate that the distribution logic is reasonable and catch any unexpected shifts early.
2. Brand Sort Order — Royal Displayed First
Changed the brand display order from alphabetical (Celebrity → Royal) to reverse alphabetical (Royal → Celebrity).
3. Department Filtering — Removing Irrelevant Lines of Business
Added filters at the data query level to exclude any department containing "River" or "Outbound" from all forecast and historical views.
4. Same Period Last Year — Historical Context on the Adjustment Chart
Added a purple dotted line overlay to the Forecast Adjustment bar chart, showing the call volume from the same calendar months one year ago.
**Why it matters:**
When adjusting forecasts, planners need context. Seeing last year's actual volume on the same chart as the current forecast and proposed adjustment gives an immediate visual benchmark. It helps answer: "Is this forecast reasonable compared to what actually happened last year?" — without flipping between pages or running separate reports.
5. LOB Adjustment Validation — Color-Coded Totals
Updated the Line of Business adjustment page to color-code the total percentage row:
- Green when the split totals exactly 100%
- Orange when the split is under 100% (volume is being under-allocated)
- Red when the split exceeds 100% (volume is being over-allocated, saving is blocked)
**Why it matters:**
When planners redistribute forecast volume across departments, the percentages should add up to 100%. Previously, the validation only showed green or red. The new orange state provides an early visual warning that volume is being under-distributed — which could mean some departments are missing from the plan. This reduces errors and gives planners more confidence that their adjustments are complete and correct before saving.
Next Step:
Features engineering for the call volume forecast International Markets and Casino International.

---

## Update 17

**Date:** 2026-04-03
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

Next Step:
Get the Office Hourly Matrix by 1h and by 30mn
Get the Hourly/30mn call volume proportion Matrix
Features engineering for the call volume forecast International Markets and Casino International.

### Raw Update

Next Step:
Get the Office Hourly Matrix by 1h and by 30mn
Get the Hourly/30mn call volume proportion Matrix
Features engineering for the call volume forecast International Markets and Casino International.

---

## Update 18

**Date:** 2026-04-03
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** GTY-Lead Fare Optimization Model
**People:** Unidentified

### Summarized Update

Update – Bronze and Silver layer work is complete. The following Bronze and Silver layer components have been implemented and completed as part of this effort:
Configuration Framework — Defined fleet scope, basket parameters, corridor thresholds, DTD bucket boundaries, and refresh settings in centralized configuration tables. All pipeline behavior is config-driven, allowing changes to business rules, fleet coverage, or analytical parameters through configuration updates only, with no code changes required.

### Raw Update

Update – Bronze and Silver layer work is complete.
The following Bronze and Silver layer components have been implemented and completed as part of this effort:
Configuration Framework — Defined fleet scope, basket parameters, corridor thresholds, DTD bucket boundaries, and refresh settings in centralized configuration tables. All pipeline behavior is config-driven, allowing changes to business rules, fleet coverage, or analytical parameters through configuration updates only, with no code changes required.
Bronze Layer — Booking Change Log — Implemented an append-only event log capturing all meaningful booking state transitions (new bookings, cancellations, fare changes, cabin moves). This preserves the full booking lifecycle and supports accurate reconstruction of historical booking pace.
Bronze Layer — Pricing Change Log — Implemented complete price revision history across all guest slots and markets using watermark-based incremental refresh logic. This enables both current price lookups and historical fare distribution analysis without full source rescans.
Bronze Layer — Sailing and Reference Tables — Built and maintained sailing master, itinerary details, ship metadata, and calendar reference tables that anchor all downstream joins. These tables operate at universal scope (all brands, all ships) with no fleet filtering at the Bronze layer.
Silver Layer — Sailing Universe — Created a single clean row per sailing with product identity, ship class, capacity denominators, and deployment context pre-joined, eliminating repeated multi-table joins in downstream analytics.
Silver Layer — Booking Pace Spine — Enriched the booking change log with frozen days-to-departure at each snapshot and active booking flags. This table serves as the analytical backbone for pace curve construction and all downstream occupancy calculations.
Silver Layer — Pricing Tables — Produced both a current-state pricing view (one row per sailing × category for fast Gold-layer queries) and a full historical pricing event timeline to support fare analysis and feedback loop development.
Brand and metaproduct coverage notes: Royal Caribbean metaproducts follow the defined meta structure.
Celebrity (Brand C) — Ocean includes metaproducts 13–24, using the same metaproduct codes where Celebrity deploys ships. This is a subset of Royal Caribbean coverage, as Celebrity does not operate all products, but each brand × metaproduct combination with sufficient volume is modeled independently.
Celebrity (Brand C) — River includes metaproduct 25, RIVER — Celebrity River Cruises, which is completed.
All Bronze and Silver layer deliverables are complete and validated.
Update – RCI | 7N CARIBBEAN basket model work is complete.
The following scope has been fully implemented and delivered for the 7N CARIBBEAN metaproduct:
Booking Pace Feature Engineering has been completed, with a standardized pace matrix measuring occupancy at fixed days-to-departure windows from 360 through 30 days.
Sailing Trait Matrix Construction has been completed and includes key sailing characteristics such as ship class, homeport, itinerary composition, time of year, and related contextual attributes used for model explainability and grouping logic.
Statistical Basket Assignment has been implemented using decision tree models to create distinct peer groups of sailings. Baskets were validated based on significant booking pace separation at three key action windows.
Product Basket Derivation has been completed by subdividing statistical baskets into operational product baskets that contain only contiguous sailing weeks, ensuring practical usability for pricing execution.
Velocity Corridor Computation has been completed, with percentile bands (P25, P50, P75) computed for booking pace at every days-to-departure bucket within each product basket.
Pricing Signal Generation has been implemented, classifying each sailing into one of five action categories (Discount, Monitor, On Track, Hold, Raise Price) with a clear recommended action based on corridor position and recent velocity.
The Quarterly Recalibration Process has been implemented, enabling models to be refit on a rolling historical window to ensure continued alignment with current booking behavior.

---

## Update 19

**Date:** 2026-04-03
**Business Area:** CEL Revenue Management
**Business Project:** Category Gapping Optimization 3.0
**People:** [[srilekha_reddy_madupu/overview_srilekha_reddy_madupu|Srilekha Reddy Madupu]]

### Summarized Update

Srilekha
CEL Revenue Management: Actual Price Paid Analysis:
I have done analysis to check whether raw (uncapped) PRE price change recommendations are aligned with the actions we usually expect to take for sailings Influenced by replacement value. I grouped sailings into G1, G2, and G3 based on how they performed against Track Ask - beating Track without replacement, beating because of replacement, or missing even with replacement. For each group, I looked at whether the direction of the price change (increase, hold, decrease) matched the commercial action we would typically take for that type of demand situation.

### Raw Update

Srilekha
CEL Revenue Management: Actual Price Paid Analysis:
I have done analysis to check whether raw (uncapped) PRE price change recommendations are aligned with the actions we usually expect to take for sailings Influenced by replacement value.
I grouped sailings into G1, G2, and G3 based on how they performed against Track Ask - beating Track without replacement, beating because of replacement, or missing even with replacement.
For each group, I looked at whether the direction of the price change (increase, hold, decrease) matched the commercial action we would typically take for that type of demand situation.
I ran this analysis across multiple product levels (meta product, category class, ship class) to check if the pattern holds consistently and is not driven by one segment.
In most cases, PRE’s price change direction matches the expected action for the group - increases or holds for strong demand, cautious moves for replacement-driven wins, and decreases when demand underperforms.

---

## Update 20

**Date:** 2026-04-03
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model
**People:** Unidentified

### Summarized Update

Ticket: DUAL \ Inventory Automation KPI - Definition + Alignment (RMA-5398)
Mar 31 2026 1:08 PM
Status: This ticket is complete as of 03/31/2026
Deliverables:
Proposed KPI is modification of stockout rate previously evaluated. Combine detected stockout periods, 7-day demand for stocked out category, lead category and category class availability at time of stockout. Tie to revenue by comparing difference in price between GTY and Lead.

### Raw Update

Ticket: DUAL \ Inventory Automation KPI - Definition + Alignment (RMA-5398)
Mar 31 2026 1:08 PM
Status: This ticket is complete as of 03/31/2026
Deliverables:
Proposed KPI is modification of stockout rate previously evaluated.
Combine detected stockout periods, 7-day demand for stocked out category, lead category and category class availability at time of stockout.
Tie to revenue by comparing difference in price between GTY and Lead. Observed effect to guest is a price increase.
Evaluate potential loss of volume due to perceived increase in price.
Discussed with David Whitney and Kevin Diaz and they see this as an initial viable measure of benefit of automated replenishment.
Delays: None.
Potential future issue: None.

---

## Update 21

**Date:** 2026-04-03
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

RCI \ Track Optimization – DP Scaling, Fleet Execution, and Track Comparisons (RMA-5474)
Mar 30 2026 11:24 AM
Computed the following metrics to analyze the gaps / pace of both the optimal and the business tracks:
MAE
0.11
On avg, across all WTS, sailings/classes, the business curve is about 11.4% builds away from the optimal curve
RMSE
0.13
When we penalize larger deviations more heavily, the avg gap becomes 13% builds away. Some weeks/ sailings/classes have larger-than-avg gaps
Bias
0.049
On avg, the business curve is about 5% builds ahead of the optimal curve. At a given WTS, has a higher cumulative build % - Business plan more aggressive/faster building than the optimal.

### Raw Update

RCI \ Track Optimization – DP Scaling, Fleet Execution, and Track Comparisons (RMA-5474)
Mar 30 2026 11:24 AM
Computed the following metrics to analyze the gaps / pace of both the optimal and the business tracks:
MAE
0.11
On avg, across all WTS, sailings/classes, the business curve is about 11.4% builds away from the optimal curve
RMSE
0.13
When we penalize larger deviations more heavily, the avg gap becomes 13% builds away. Some weeks/ sailings/classes have larger-than-avg gaps
Bias
0.049
On avg, the business curve is about 5% builds ahead of the optimal curve. At a given WTS, has a higher cumulative build % - Business plan more aggressive/faster building than the optimal.
Generated visuals to present the results and findings to the SHs.
RCI \ Track Optimization \ Execute DP optimization for entire fleet through April 2028 and persist results (RMA-5476)
Apr 02 2026 12:05 PM
Status: Closing this ticket on 02-APR-2026
Deliverables:
Executed DP optimization for entire fleet through April 2028.
Persisted and versioned results for downstream use.
Validated runtime and fleet-wide coverage.
Prepared outputs for auditing and comparison.

---

## Update 22

**Date:** 2026-04-03
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** GTY-Lead Fare Optimization Model
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

AD HOC | DUAL
Microsoft is decommissioning the old way of connecting to SharePoint. Updated all notebooks writing/reading SharePoint to avoid failures in pipeline runs. Category-Gapping 2.0
RCI
Business is reviewing output.

### Raw Update

AD HOC | DUAL
Microsoft is decommissioning the old way of connecting to SharePoint.
Updated all notebooks writing/reading SharePoint to avoid failures in pipeline runs.
Category-Gapping 2.0
RCI
Business is reviewing output.
Awaiting team’s final approval before pushing to PRD.
Category-Gapping 3.0
RCI
·       Team approved data-driven tiers.
·       Currently using the same framework built for CEL to begin training RCI’s models.

---

## Update 23

**Date:** 2026-04-03
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** GTY-Lead Fare Optimization Model
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

CEL
·       Team sent the desired revenue formula for optimization. ·       Instead of maximizing revenue, the goal is to price tiers to reach desired booking shares. ·       It will still:
Optimize the gty-lead gap using the 2.0 models
Split out physical shares according to availability
·       This will sell cabins at the necessary rate to avoid overselling while still selling out as much as possible.

### Raw Update

CEL
·       Team sent the desired revenue formula for optimization.
·       Instead of maximizing revenue, the goal is to price tiers to reach desired booking shares.
·       It will still:
Optimize the gty-lead gap using the 2.0 models
Split out physical shares according to availability
·       This will sell cabins at the necessary rate to avoid overselling while still selling out as much as possible.
Applying PWL Within Optimization
·       To apply PWL, the model must predict a lookup table with gaps incrementing by specific steps.
·       Confidence intervals (CIs) ensure that every step change reflects real, meaningful differences in customer behavior—not noise.
Why CI Filtering Is Needed
·       Models create many small bins because they search for any pattern that improves predictive accuracy:
Some bins reflect true behavior differences
Others are random, unstable, or driven by noise (especially in low-density regions)
·       Using raw model outputs would result in:
Overly complex pricing behavior
Volatile recommendations
High sensitivity to small input changes
Poor interpretability for business partners
·       CIs allow us to retain only meaningful changes.
EBM Bin Evaluation Using Confidence Intervals
·       For every bin in the EBM:
We estimate the effect (how the bin influences prediction)
We estimate uncertainty around that effect
·       EBM outputs:
Bin scores (impact of gap on probability of choosing a tier)
Stability of each score
·       Confidence intervals define a “trusted” range for every bin score.
Comparing Adjacent Bins
If the next bin’s lower CI is above the previous bin’s upper CI:
The model is statistically confident the bins differ
If CIs overlap:
Difference is not statistically reliable
Likely noise
Boundary is discarded
Benefits of CI-Filtered Bins
•       Fewer, cleaner, stronger step changes
•       More stable pricing effects
•       Each step reflects real customer behavior
•       Prevents “zig-zag” or noisy curves
Full Pipeline
1.      EBM Finds Raw Bins
Based on cross-validation
Optimized for predictive accuracy
May include noisy or marginal splits
2.      Confidence Interval Filtering
Removes bins with overlapping CIs
Keeps only statistically different segments
3.      Define PWL Step Sequence
Clean
Stable
Behavior-driven
Business interpretable
Ensures PWL inherits trusted patterns only (not noise)
Latest Results
·       Created new predicted grids with:
Normalized APD bins
Data-driven gap increments
Tier-to-tier gaps
·       Observations:
More consistent shares across all tables
Premium shares now drop appropriately (previous sharp-drop issue fixed)
“Jump” behaviors in shares are no longer present and align with realistic customer behavior
Currently In Progress
Applying backtesting framework to ensure stable model performance
Integrating the team’s desired revenue formula into the optimization

---

## Update 24

**Date:** 2026-04-03
**Business Area:** PCP Pricing Automation
**Business Project:** Promotional Workflow Automation
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

Create set of test-control paired sailings for Bev PRE testing
• A set of test-control paired sailings were created for setting up the A/B test for RCI Beverage PRE. This resulted in 24 pairs of test-control sailings (48 sailings total), targeting specifically 7N CARIBBEAN & SHOIRT CARIBBEAN sailings in SUMMER of 2026. These are also mainly tested on only 3 ship classes: IC, OA, and FR.

### Raw Update

Create set of test-control paired sailings for Bev PRE testing
• A set of test-control paired sailings were created for setting up the A/B test for RCI Beverage PRE. This resulted in 24 pairs of test-control sailings (48 sailings total), targeting specifically 7N CARIBBEAN & SHOIRT CARIBBEAN sailings in SUMMER of 2026. These are also mainly tested on only 3 ship classes: IC, OA, and FR.
Recurring meetings with Business Team (PREs, CRF Automation, etc) & DE Team (Mass Promo Table & Targeted Offers)
• meetings were had with both the RCI & CEL OBR teams regarding promo automation
• with CEL in particular, a walk through was done as to how the sheet and automated promo pipeline can be used for promo automation
• meetings were had with both brands begin the first rollout of promo automation use for new flash sales
Add shipboard promos into the promo automation sheet & code
• Shipboard promos (specific website for each ship for each brand) were added as an additional functionality in the SharePoint sheet for promo automation. This was tested in lower environment and threw no errors for the ship data that existed in lower environment for testing. This is no available for the RCI & CEL teams to start using in production as well.
Update to NEW SharePoint code
• The SharePoint code for automated promo uploads was updated to the newer version to be used across the board. In addition, one other change was done to the workflow for extracting hybris promos into a table. The extraction of the SAILING TAG condition was corrected to no longer be removing the underscores from the sailing tags; this was resulting in incorrect values for some of the extracted hybris promos.
Modify table of extracted promos from Hybris
• In addition, an additional modification was done; it was found that some of the sailing tags extracted from promos in the Hybris system were having their strings modified with the underscores being removed. This was fixed so that the strings were no longer being incorrectly modified without underscores. This helped the business team have better access to example formats of past promos they can use moving forward for the promo automation pipeline.

---

## Update 25

**Date:** 2026-04-03
**Business Area:** PCP Pricing Automation
**Business Project:** Perfect Day Product Pricing
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]], [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

We have finally achieved automated writeback capability to Hybris end-to-end with the Digital Team. Digital finally was able to get into production the necessary auditing features and the Data Science team is now actively working with Onboard Revenue Teams. THIS IS A HUGE MILESTONE.

### Raw Update

We have finally achieved automated writeback capability to Hybris end-to-end with the Digital Team. Digital finally was able to get into production the necessary auditing features and the Data Science team is now actively working with Onboard Revenue Teams.
THIS IS A HUGE MILESTONE. Mass promotion writeback is the critical execution layer that turns pricing and AI recommendations into live, governed promotions—without it, automation remains theoretical and cannot scale.
Strategic Importance of the Mass Promotion Writeback Capability
What the Capability Enables
The mass promotion writeback capability provides a direct, automated path to deploy promotions into Hybris using the same schemas, approval workflows, and governance rules that business teams use today—without manual setup. Promotions can be submitted either by humans or by automated systems, but they flow through one consistent execution mechanism.
This means pricing recommendations, promotion logic, and future AI outputs are no longer trapped in analytics tools—they can be executed at scale.
Why This Capability Is Strategically Critical
1. It Is the Execution Layer for Pricing and AI
Mass promotion writeback is the bridge between decision intelligence and revenue realization. Pricing models, elasticity optimization, and AI-driven recommendations are only valuable if they can be pushed live reliably and repeatedly. Writeback is the mechanism that makes automation real, not theoretical.
Without it, pricing and AI initiatives remain advisory; with it, they become operational.
2. It Dramatically Reduces Time from Insight to Action
Historically, promotions required manual configuration, spreadsheet uploads, and one-off validations. Mass promotion writeback:
Eliminates manual setup of nested discounts and sailing-specific logic
Preserves existing approval and governance controls
Enables faster iteration and execution of promotional strategies
This collapses cycle time from days or weeks to near-real-time, allowing teams to react to demand, inventory, and market conditions much more quickly.
3. It Is the Foundation for Scaling AI-Driven Promotions
Mass promotion writeback is the foundational capability that allows the organization to scale from:
Manual promotions
→ segmented mass promotions
→ AI-generated promotions
→ future 1:1 targeted offers
All future pricing automation, price-gapping, and targeted offer strategies depend on this writeback path to function as a closed-loop system.
4. It Creates a System of Record for Governance and Measurement
Because all promotions—manual or automated—flow through the same writeback mechanism, the organization gains:
Visibility into what promotions were submitted, approved, rejected, or modified
The ability to distinguish automated promotions from manual ones
A foundation for measuring adoption, throughput, and effectiveness
This turns promotions from an opaque operational process into a measurable, auditable, and optimizable system.

---

## Update 26

**Date:** 2026-04-03
**Business Area:** PCP Pricing Automation
**Business Project:** Perfect Day Product Pricing
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

RCI | OBR | CRF Automation
Status: This ticket is closed as of 03/31/2026, this month I worked on the set up of the CRF automation process, will push the process in production in the next month. RCI | OBR | RBC Dashboard v2
This week I focused on the following:
Analysis of Bundles and Passes: Provided my recommendations on how to target customers for RBC Passes and RBC Bundles along with the context(document). Minor Tweaks from v1: Completed the minor tweaks based on stakeholder feedback (re-ordering loyalty tier columns, renaming a few charts)
Data Fixes: During the update process, I traced the failure back to inaccurate data in a few tables feeding customer age and loyalty tier.

### Raw Update

RCI | OBR | CRF Automation
Status: This ticket is closed as of 03/31/2026, this month I worked on the set up of the CRF automation process, will push the process in production in the next month.
RCI | OBR | RBC Dashboard v2
This week I focused on the following:
Analysis of Bundles and Passes: Provided my recommendations on how to target customers for RBC Passes and RBC Bundles along with the context(document).
Minor Tweaks from v1: Completed the minor tweaks based on stakeholder feedback (re-ordering loyalty tier columns, renaming a few charts)
Data Fixes: During the update process, I traced the failure back to inaccurate data in a few tables feeding customer age and loyalty tier. I identified the problematic records, addressed the data quality issues, and implemented a fix to ensure the dashboard calculates the customer age successfully and considers all customers
RCI | OBR | AB Test Analysis (Low Price Sailings)
Data Extraction and prep: Gathered the data for alcoholic and non-alcoholic passes for all 12 test sailings, including associated revenue metric (penetration rate and revenue uplift). I also developed a customer-level view incorporating datapoints such as category class, Group/FIT designation, loyalty tier, and age, providing a granular view of the impact of price change on each of these segments.
Statistical Significance and Impact Analysis: Ran a statistical significance test (one sided stratafied permutation test) that gave the following results:
Penetration Rates:
Control mean: 10.5131%
Test mean:    13.1525%
Abs lift:     2.64%
Rel lift:     25.11%
I further did ana analysis to see the lift of penetration rate across cat-clases, loyalty tiers, age groups, cruise frequency, Group vs FIT
Presentation: Developed a presentation to showcase the results of the test to the leadership team.
Have a stakeholder meeting tomorrow (03/27/2026) to showcase the results of the analysis
RCI | OBR | AB Test Analysis (Low Price Sailings) Follow Up
Completed the follow up analysis, where I analyzed the revenue before and during the test, and also calculated the penetration rates for alc and non-alc passes for ages <=12, 13-20 and 21+. Have provided my analysis to the stakeholders in the excel below
https://royal-it.atlassian.net/browse/RMA-5570 (Link to results in comments)

---

## Update 27

**Date:** 2026-04-03
**Business Area:** PROPEL
**Business Project:** PROPEL Targeted Offers Deployment
**People:** [[glen-erik_cortez/overview_glen-erik_cortez|Glen-Erik Cortez]]

### Summarized Update

ROPEL Targeted Offers – Q1 Performance Report
Audience: PROPEL Steering / CEL Onboard Revenue
Contributors: Analytics Team (Alex, Andrew, Meital)
Context: Q1 review of PROPEL Targeted Offers performance with updated analytics delivered to the CEL Onboard Revenue teams. Feedback from stakeholders has been incorporated to improve interpretability and decision confidence. Executive Summary
In Q1, the Analytics team delivered enhanced PROPEL performance reporting to the CEL Onboard Revenue teams, enabling deeper visibility into offer-driven revenue uplift and surfacing several critical measurement and data quality issues.

### Raw Update

ROPEL Targeted Offers – Q1 Performance Report
Audience: PROPEL Steering / CEL Onboard Revenue
Contributors: Analytics Team (Alex, Andrew, Meital)
Context: Q1 review of PROPEL Targeted Offers performance with updated analytics delivered to the CEL Onboard Revenue teams. Feedback from stakeholders has been incorporated to improve interpretability and decision confidence.
Executive Summary
In Q1, the Analytics team delivered enhanced PROPEL performance reporting to the CEL Onboard Revenue teams, enabling deeper visibility into offer-driven revenue uplift and surfacing several critical measurement and data quality issues. Directionally, PROPEL continues to demonstrate positive performance signals in Q1—particularly in beverage and gaming—when excluding known distortions such as charter sailings and missing Internet revenue. However, current results should be interpreted with caution due to structural changes in measurement methodology, incomplete revenue capture, and aggregation choices that obscure sailing-level dynamics. Stakeholder feedback has been constructive and has directly informed a prioritized set of remediation actions to stabilize and strengthen PROPEL reporting going forward.
Key Takeaways
1. Charter sailings materially distort reported performance and must be excluded by default
A Reflection charter sailing on February 16 introduced an artificial spike in reported uplift, particularly in dining and restaurant revenue, creating a misleading view of PROPEL performance. Charter sailings behave fundamentally differently from standard sailings—often operating as awareness-only or control-only populations—making them unsuitable for standard test/control analysis. Stakeholders aligned that charters should be excluded by default in dashboards, with an optional toggle for transparency and exploratory analysis.
Impact: Current Q1 results are partially contaminated by charter effects and should not be interpreted without exclusions.
2. Internet, Photo, and select Package revenue are missing due to data tagging issues
Internet revenue drops off beginning in January despite continued sales activity, and Photo revenue has been absent since January 2025. The issue appears to stem from mis-tagging within OBR / VOBR total revenue tables rather than a true decline in transactions. This materially understates PROPEL’s absolute impact, particularly given Internet’s strong contribution in late Q4.
Impact: Q1 results are directionally useful for non-Internet categories, but total revenue uplift is understated.
3. Measurement methodology shifted with awareness offers becoming the control
Prior to late July, PROPEL measured uplift against a true “no exposure” control. Starting July 28, awareness offers were rolled out fleet-wide and became the control condition. As a result, apparent post-July declines reflect relative performance versus awareness—not true value erosion. PROPEL remains directionally positive, but expectations must be reset under the new baseline.
Impact: Post-awareness results are not directly comparable to earlier periods.
4. Q1 directional signal is positive, but reconciliation gaps remain
Excluding Internet and charter sailings, January showed a strong APD uplift (approximately $0.91), driven primarily by beverage and gaming. However, APD uplift does not currently reconcile cleanly to total dollar uplift, and category-level APDs are not additive due to differing PCDs. This has created understandable skepticism among stakeholders.
Impact: Signals are encouraging, but confidence is limited until APD-to-dollar math is fully reconciled.
5. Aggregation must move to the sailing level to avoid distortion
Current reporting aggregates first at the category or ship level, masking variability across itineraries and sailings. Stakeholders strongly prefer calculating uplift at the sailing level and rolling up to ship, class, meta, and enterprise views to ensure like-for-like comparisons.
Impact: Sailing-level aggregation is required before deeper interpretation or decision-making.
Action Items & Ownership
Exclude charter sailings from all core dashboards (with optional toggle)
Owner: Glen-Erik Cortes / Analytics
Why: Prevent artificial inflation and misleading comparisons.
Engage Data Engineering to fix Internet revenue tagging
Owner: Glen-Erik Cortes, with support from David Whitney
Why: Internet is a major revenue driver; its absence materially understates performance.
Document Photo revenue as a known blind spot
Owner: Analytics Team
Why: Avoid repeated confusion and misinterpretation in Q1+ readouts.
Rebuild uplift calculations starting at the sailing level
Owner: Glen-Erik Cortes
Why: Ensure like-for-like comparisons and reduce aggregation distortion.
Reconcile APD uplift to total dollar uplift
Owner: Glen-Erik Cortes
Why: Restore stakeholder confidence that APD and $ views are mathematically coherent.
Produce a clean Q1 view excluding charters and Internet
Owner: Analytics Team
Why: Clearly answer the core question: has PROPEL continued to perform directionally?
Bottom Line
When adjusted for known distortions and data gaps, PROPEL continues to show a positive directional signal in Q1. The primary blockers to confident interpretation are structural (aggregation level, control definition) and technical (revenue tagging, reconciliation), not a lack of underlying performance. Addressing these items will materially improve trust, clarity, and decision usefulness of PROPEL reporting in Q2 and beyond.

---

## Update 28

**Date:** 2026-04-03
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]], [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Key Meeting 1: Tri-Branded RMA – Track Adjustment & Optimization Meeting Summary
This session focused on how Revenue Management evaluates, adjusts, and optimizes booking tracks using SPI-informed ideal pacing, demand forecasts, and pricing coordination. The discussion centered on ensuring sailings remain aligned to high-performing booking behavior while preserving healthy booking shapes, managing capacity constraints, and avoiding value-destructive pricing actions. At the core of the approach is the concept of an “ideal track”, derived from booking curves of historically high-SPI sailings.

### Raw Update

Key Meeting 1: Tri-Branded RMA – Track Adjustment & Optimization Meeting Summary
This session focused on how Revenue Management evaluates, adjusts, and optimizes booking tracks using SPI-informed ideal pacing, demand forecasts, and pricing coordination. The discussion centered on ensuring sailings remain aligned to high-performing booking behavior while preserving healthy booking shapes, managing capacity constraints, and avoiding value-destructive pricing actions.
At the core of the approach is the concept of an “ideal track”, derived from booking curves of historically high-SPI sailings. These curves define an optimal booking range by weeks-to-sail, with the midpoint used as the reference deployment track. Sailings are continuously monitored against this benchmark using pacing, booked position, and curve shape to identify deviations from expected SPI-aligned behavior.
How track issues are identified
Tracks are flagged as problematic when they materially diverge from SPI-aligned behavior, including:
Pacing mismatches, where sailings are meaningfully ahead of or behind expected bookings despite similar curve shapes
Curve shape issues, such as irregular momentum shifts that differ from the smooth booking patterns seen in top-performing SPI sailings
Specific flags include future booked position or track asks that fall more than one standard deviation from top SPI performers, as well as week-over-week and three-week FIT pacing deviations above defined thresholds.
Short-term track adjustment mechanics
For near-term corrections, business rules are applied to:
Flag “bad” tracks
Quantify the gap between actual bookings and expected SPI-aligned booked position
Redraw the future track to move back toward the ideal SPI shape
Small deviations are corrected quickly, while larger deviations are spread gradually over remaining weeks to preserve curve integrity and avoid abrupt behavioral shifts.
Price and track coordination
Pricing actions are tightly coordinated with track adjustments through PRE logic. Price changes account for both track deviation and cumulative booked position relative to SPI, with different actions depending on whether those signals reinforce or conflict with each other. This ensures pricing supports track correction rather than undermining it—for example, avoiding unnecessary rate reductions when demand momentum is already strong.
Long-term track optimization
Beyond short-term fixes, the framework evaluates multiple feasible candidate tracks that comply with “bad track” constraints. Demand forecasts are used to estimate expected net ticket revenue (NTR) lift for each candidate. A key principle emphasized is that individual sailings have unique elasticities, meaning even high-performing SPI curves are not universally optimal. Tailored track optimization is required rather than applying a one-size-fits-all pacing strategy.
Scenario planning further adjusts track aggressiveness based on:
Demand signals
Capacity conditions
Competitive context
Tracks are simulated under different business environments, with the revenue-optimal track selected for prevailing conditions.
Key discussion themes and concerns
Several important concerns and debates surfaced during the discussion:
Track vs. Demand Forecast alignment:
Goldner raised concerns about forward-looking track shapes diverging from the demand forecast, questioning whether misalignment should be attributed to the forecast or the track itself. Eddie and Nick expressed the view that the track may be off in some cases, emphasizing that demand forecasts and tracks cannot fundamentally disagree—there must be an optimal point of convergence.
Capacity and ship upsizing:
The group discussed how load factors build over time when ships are upsized, recognizing that there is finite capacity available for early baseloading. This reinforces the need for dynamic aggressiveness rather than static pacing targets.
Dynamic aggressiveness and momentum:
There was strong alignment that aggressiveness should flex based on recent performance and SPI signals. If a sailing is trending ahead and SPI indicates strong underlying demand, dynamic caps can be applied. A recurring theme was the importance of preserving momentum and not “trashing rates” when demand is coming in. The further a sailing is from the optimal curve, the more aggressive corrective actions can be justified.
Value of early bookings vs. latent demand limits:
While booking further out is generally valuable, the group acknowledged limitations in latent demand and the need to balance early pace with realistic downstream absorption.
Confidence in track reliability:
Questions were raised about how reliable current tracks are, what pricing curves underpin the optimal tracks, and what assumptions are embedded in those curves. There was interest in explicitly incorporating strategic pricing shapes (e.g., high-low, high-low-high, low-high) into the track framework.
Where the group landed
SPI-informed ideal tracks provide a strong reference point for evaluating pacing and curve health
Tracks and demand forecasts must ultimately converge; persistent divergence indicates a modeling or assumption issue
Track corrections should be dynamic, proportional, and momentum-preserving
Pricing must reinforce track adjustments, not work against them
Long-term optimization must account for sailing-specific elasticity, capacity evolution, and business environment
Open questions and next considerations
How explicitly demand forecast assumptions should be embedded into track targets
How to formalize pricing curve assumptions within optimal track generation
How to better quantify confidence in tracks under different capacity and demand regimes
Key Meeting 2: CEL Track Optimization – SPI Review Meeting Summary
This session served as a checkpoint on CEL Track Optimization, focused on validating and comparing three approaches to booking tracks: business-generated tracks, optimally generated tracks, and SPI-based tracks derived from historical top-performing sailings. The objective was not to operationalize SPI at this stage, but to understand where SPI aligns with current RM strategy and optimization outputs, where it diverges, and whether it can eventually inform or guide track decisions.
Lamis walked through the SPI-based track methodology, emphasizing that no new SPI scoring logic was introduced; all SPI scores were previously developed by Evan. SPI-based tracks are constructed by grouping historical sailings at a high level (meta product, season, holiday flag, and capacity clause) and identifying “top performers” as sailings with SPI > 1. For these sailings, booking position by weeks-to-sail is summarized using 25th–75th percentile confidence intervals and a weighted median track, with higher SPI scores receiving more weight. This prompted discussion around statistical caution, particularly that very high SPI scores may reflect noise or outliers rather than true best-in-class behavior.
Review of example sailings showed that SPI-based tracks tend to align more closely with optimal tracks further out in the booking window, where early-stage demand signals are cleaner and less impacted by prior pricing or capacity decisions. Closer to sail date, divergence increases materially—especially in the mid-cycle (roughly 50–20 weeks-to-sail)—where existing bookings, earlier pricing actions, group allocations, and incomplete retention information make SPI confidence regions harder to interpret. In some cases, SPI-based targets were infeasible or misleading if applied mechanically.
A major theme of the discussion was granularity mismatch. Current SPI groupings operate above category-class or RDSS level, while optimization works at a more detailed structure. This explains why SPI and optimal tracks do not always align, even when both are directionally correct. The group discussed potentially starting SPI grouping at a finer grain (category-class or RDSS) with fallback logic to meta-product when sample sizes are insufficient, acknowledging the tradeoff between stability and overfitting.
Conceptually, there was strong alignment that SPI should not be used as a hard constraint in track optimization today. If SPI is used at all, it must be dynamic and conditional on the current booking position, rather than applied as a static historical curve across the full booking window. SPI appears best suited, for now, as a directional signal or sanity check, particularly far from sail date, rather than a prescriptive target.
Two important unresolved topics were also highlighted. First, FIT vs. Group interactions: SPI reflects total performance, while optimization primarily manages FIT demand, and group allocations materially alter remaining capacity and the shape of the FIT curve. Long-term, this likely requires explicit modeling of group behavior layered into FIT optimization. Second, retentions and cancellations: current comparisons rely on actual bookings and do not fully account for retention dynamics, which can make future sailings appear artificially ahead or misaligned with SPI expectations. Incorporating projected bookings and improved retention modeling was identified as critical for making SPI more trustworthy closer-in.
Where the team landed
SPI should remain informational, not prescriptive, at this stage
SPI is more reliable further out in the booking window
Any SPI integration must be dynamic, booking-state aware, and aligned with optimization granularity
Broader internal alignment is needed on SPI definitions, aggregation levels, and FIT vs. Group treatment
This work should be explicitly tied back to Evan’s broader SPI framework
Next steps
Review SPI usage, weighting, and assumptions with Evan
Explore finer-grain SPI groupings with clear fallback rules
Continue validation before any operational use
Hold a broader internal session to align DS and RM on SPI integration, checkpoint windows, and track optimization usage

---

## Update 29

**Date:** 2026-04-03
**Business Area:** HR
**People:** [[david_martinez/overview_david_martinez|David Martinez]], [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

This activity centered on advancing an HR Demand Forecast initiative through a draft sCAR, with Angela Smith providing critical strategic and execution-focused feedback that materially shapes the path forward. While there was strong alignment on the value of automating CAM Planning’s labor-intensive, Excel-based workforce forecasting—to improve speed, auditability, forecast accuracy, and early risk identification—Angela was clear that the effort should be positioned as a full CAR rather than an sCAR, reflecting its strategic importance and cross-functional impact. She emphasized an aggressive mid-April submission timeline, while flagging the need to first clarify dependencies and expectations with People Analytics and Data Engineering, noting that only one Data Scientist is likely required but that scope must be realistic.

### Raw Update

This activity centered on advancing an HR Demand Forecast initiative through a draft sCAR, with Angela Smith providing critical strategic and execution-focused feedback that materially shapes the path forward. While there was strong alignment on the value of automating CAM Planning’s labor-intensive, Excel-based workforce forecasting—to improve speed, auditability, forecast accuracy, and early risk identification—Angela was clear that the effort should be positioned as a full CAR rather than an sCAR, reflecting its strategic importance and cross-functional impact. She emphasized an aggressive mid-April submission timeline, while flagging the need to first clarify dependencies and expectations with People Analytics and Data Engineering, noting that only one Data Scientist is likely required but that scope must be realistic. Her feedback highlighted key tensions to resolve: the ambitious deliverable set versus a single-contractor capacity, the mismatch between “exploratory” framing and production-like outputs, and unresolved questions around data readiness, historical depth, and forecast-vs-actual validation. Angela also raised important governance and capital considerations, including useful life requirements, clarity on what constitutes the capitalizable asset, alignment with parallel Crew Air optimization work, and explicit success criteria that would justify a future full-scale investment. Overall, her input reinforced that while the concept is compelling and timely, success hinges on tightening scope, de-risking data dependencies, and clearly articulating how this pilot translates into a durable, enterprise-grade planning capability.
Discussed focus on an HR Demand Forecast and wrote a SCAR:
Project Description:
This CAR will fund an exploratory, limited-scope build of a shoreside Demand Planning Automation Tool to help CAM Planning forecast staffing supply and demand across ~750 positions and ~100,000 crew members spanning Royal Caribbean, Celebrity, Silversea, and TUI Marine. The work is needed now because the current Excel-based process requires manual assembly of multiple large headcount files and repeated data manipulation to produce each forecast—slowing decision-making and limiting CAM’s ability to proactively identify staffing risk and connect long-term planning with near-term operational scheduling. To address these constraints, the CAM team proposes building a pilot AI-enabled automation that includes:
a position-level demand planning model tailored by role (including promotion in/out rules)
an 18-month hiring and promotion forecast by month with promotion pipeline visibility
integrated dashboards for PAR outlook and short-term (0–12 weeks) and long-term (3–18 months) staffing views by ship, cost center, and position
week-over-week and month-over-month variance reporting using historical snapshots
automated KPI reporting across CAM Ops (Planning, Talent Acquisition, Scheduling, Onboarding, Travel)
forecast input validation to compare assumptions against actual results

---

## Update 30

**Date:** 2026-04-03
**Business Area:** Project Axiom
**Business Project:** NPS Drivers Analysis for Alert System
**People:** Unidentified

### Summarized Update

Current solution in place: CAM Planning relies on numerous Excel models and existing dashboards to assess staffing. The workflow begins with a headcount snapshot file containing ~100,000 rows and ~50 columns, which is manually transformed to estimate “available” and “future available” supply by position across the fleet. That output is then joined with separate demand inputs (PAR, vacation, contingency, surplus targets, attrition) to create a forward-looking supply/demand view, and then combined with a promotion pipeline file to iteratively estimate promotions and hiring timing.

### Raw Update

Current solution in place: CAM Planning relies on numerous Excel models and existing dashboards to assess staffing. The workflow begins with a headcount snapshot file containing ~100,000 rows and ~50 columns, which is manually transformed to estimate “available” and “future available” supply by position across the fleet. That output is then joined with separate demand inputs (PAR, vacation, contingency, surplus targets, attrition) to create a forward-looking supply/demand view, and then combined with a promotion pipeline file to iteratively estimate promotions and hiring timing. Building and replicating this model set takes ~4–6 hours per cycle, and the broader planning team then spends an additional ~3–6 hours making manual adjustments to correct for the “one size fits all” nature of the current approach and known pipeline limitations—totaling ~7–12 hours every two weeks. The process is labor-intensive, difficult to audit, dependent on repeated manual steps, and produces outputs that quickly become stale.
Why it needs replacement/upgrade: The Excel-based approach does not scale to the operational complexity and decision speed required for multi-brand crew planning. Replacing it with a daily-updated, integrated, auditable planning tool will (1) reduce manual effort and key-person dependency, (2) enable consistent position-specific rules as standard, governed inputs instead of ad-hoc adjustments, (3) provide variance reporting and snapshots to clearly explain what changed between plans and support faster decision-making, and (4) bridge long-term hiring/promotion planning with short-term scheduling to identify and mitigate staffing risk earlier. The upgraded solution also enables systematic validation of assumptions (e.g., contingency and attrition), improving forecast quality over time and reducing inefficiencies across Talent Acquisition, Scheduling, Onboarding, and Travel, supporting better operational readiness and cost control.
Discussion Points:
Angela Smith wants to have a full CAR, but not just a sCAR. We will likely have to discover next week what we need from People Analytics Group and DE. However, we likely only need one Data Scientist. She wants to ideally submit mid-April, which is aggressive.
Other key points
Financial
Bill rate. The sCAR uses $69/hr. Insight contractors are at $73/hr and Cap Gemini I believe are $78/hr.

---

## Update 31

**Date:** 2026-04-03
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** Unidentified

### Summarized Update

"Exploratory" framing vs. production-like outputs. The sCAR calls itself exploratory but lists concrete deliverables like integrated dashboards and automated KPI reporting.

### Raw Update

"Exploratory" framing vs. production-like outputs. The sCAR calls itself exploratory but lists concrete deliverables like integrated dashboards and automated KPI reporting. Recommend clarifying which deliverables are prototypes and which are expected to be production-ready — this distinction matters for how Finance evaluates the request.
Retention modeling discussed but not listed. We discussed a "retention score" (likelihood a candidate reports for duty) as high-value, but it does not appear in the sCAR deliverables. Should it be added, or is it intentionally out of scope for this phase?

---

## Update 32

**Date:** 2026-04-03
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Limited historical depth. The existing dashboard only covers ~1.5 years. No historical forecast-vs-actual data.

### Raw Update

Limited historical depth. The existing dashboard only covers ~1.5 years.
No historical forecast-vs-actual data. Current data shows outcomes ("where we ended up") but not what was projected at each point in time. Without that comparison, back-testing and validating forecast accuracy will be difficult from day one.
Manual data dependencies. Riding Crew Headcount is manually provided by one person. Attrition and Promotions data come from dashboards rather than queryable tables.
People Analytics as a bottleneck. Nearly all data sources flow through People Analytics, who — per John — don't have deep CAM business context. There is no defined SLA or working agreement for PA to support this project, creating a risk of being deprioritized against their other commitments.

---

## Update 33

**Date:** 2026-04-03
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Lead + Install Time mismatch. The sCAR template shows "Lead + Install Time: 12 Months" but funding covers only 36 weeks (~9 months). Is the remaining 3 months an unfunded ramp-down, or a template artifact that should be corrected?

### Raw Update

Lead + Install Time mismatch. The sCAR template shows "Lead + Install Time: 12 Months" but funding covers only 36 weeks (~9 months). Is the remaining 3 months an unfunded ramp-down, or a template artifact that should be corrected?

---

## Update 34

**Date:** 2026-04-03
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** Unidentified

### Summarized Update

The sCAR states a full CAR "may be submitted next year" if the pilot succeeds. What triggers that decision? (e.g., forecast accuracy improvement target, cycle-time reduction threshold)
Useful Life Expectancy of 3 years.

### Raw Update

Path to full CAR. The sCAR states a full CAR "may be submitted next year" if the pilot succeeds. What triggers that decision? (e.g., forecast accuracy improvement target, cycle-time reduction threshold)
Useful Life Expectancy of 3 years. Capital policy requires a 3-year minimum useful life. For an exploratory pilot, what specifically is the capitalizable asset — the model code, the dashboards, the data pipelines?
"Expected In-Service: Q4 2026." Does this mean the tool is production-ready by Q4, or simply that the contractor engagement concludes?

---

## Update 35

**Date:** 2026-04-03
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[david_martinez/overview_david_martinez|David Martinez]]

### Summarized Update

David deliver a PoC where we created a SPI Factor Model that looked at how the demand built in WTS bins. He built a quick Yield model over the weekend, accounting for the SPI enhancements form Evan, (i.e. brushing off my dusty DS skills) that predicts the value of a given track shape to revenue.

### Raw Update

David deliver a PoC where we created a SPI Factor Model that looked at how the demand built in WTS bins. He built a quick Yield model over the weekend, accounting for the SPI enhancements form Evan, (i.e. brushing off my dusty DS skills) that predicts the value of a given track shape to revenue. without understanding the pricing implications, organically being able to realize the SPI booking curves (that prefer base-loading) would be worth ~$20 APD. but that wont organically happen and we need to change price. either way it gives us a ballpark estimate that track is important (which is what Goldner+Brian are saying)
The biggest issue is reconciling capacity and price we need to set against this optimal shape. There is no way we can base-load every sailing.
But whats nice is we can see the expected behavior in our AI models. Here you are looking at the marginal contribution of normalized FIT builds (i.e. what percentage of demand we built in a given 5-WTS bucket relative to total capacity). You can see the SHAP values (representing the marginal contribution to yield) go up when we are building less demand close-in and more demand father out. This validates baseloading as a revenue-optimizing strategy, but balanced against how much latent demand is present in the far-out booking window (and what cost to APDs to realize the demand).
Shared with Anastasia C. with positive feedback. She would like to see this analysis replicated for CEL, as it was done for RCI data only.

---

_Source: 20260403 - Weekly Matt and Rafeh (Raw).docx_