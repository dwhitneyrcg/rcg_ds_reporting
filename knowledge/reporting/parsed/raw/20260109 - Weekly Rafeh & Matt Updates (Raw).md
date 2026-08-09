**Mert**
MIAP
Identified a total of 54K/month active energy deviation across several ships, with cost to date of $1.1M.
Resolved identified issues onboard Quantum-class ships, resulting in 150K cost savings. Continuing work on remaining ships and collaborating with the HVAC technical team and shipboard engineers. Total MIAP savings increased to 6.9M.
Developed and productionized a data-trending tool on the MIAP app that leverages the MIAP API to quickly build visualizations from selected variables, including ship-to-ship comparison and real-time data streaming.
Presented the data-trending tool to the Newbuild Maritime Technology team together with Energy Management.
Met with C3.ai to understand their capabilities and agreed to a follow-up session for drydock project optimization.
Started implementing custom agentic AI solutions hosted on the MIAP API, with a library of tools, dedicated agents, and a supervisor-agent architecture using LangChain/LangGraph/FastAPI. This will establish the foundation for custom AI agents for marine/new-build projects, with expert agents for HVAC, machinery, hotel, fresh water systems, and other areas.
Met with Risk Management and Corporate Strategy teams to align the agenda for a larger meeting to discuss the future of Project TIDE for claims management.

Ram

MIAP
Deployed a fix for the Bronze Valmet job by adjusting Spark partitions.
Updated dependencies in the MIAP ETL for the Bronze Valmet job.
Implemented code to load Modbus data; mapping information is still needed, but the code implementation is complete.
Implemented code to load data from a Kafka topic directly into the silver table, avoiding intermediate data movement, reducing latency, and lowering storage costs.
Fixed a data-type issue in the MIAP API that occurred when a low value was transmitted as an int and implemented the necessary changes.
Next week
Deploy the streaming shipboard job changes to production.
Identify and implement mappings for Modbus and deploy them to production.

Brendan
MIAP
Fixed a bug in the Fuel Forecast API that prevented simulations from working with default parameters.
Investigated MIAP REST API chargeback to vendors (with Ram): created a query to get SQL Warehouse costs, derived a formula to calculate pro-rated cost per user based on REST API logs, and identified gaps in the existing Azure costs table that prevent project-level cost accounting. Ram and I will work with the platform team to find a solution.

Mahshad
MIAP
Worked on an issue in the Digital Twin function.
Conducted self-directed learning on AI agents to automate anomaly detection.
Began developing a report-generation pipeline for the MIAP app.

Arya
Identified data issues with IC in the ETL.
Identified tag-mapping issues related to lube oil.
Researched implementation of online dynamic model decomposition.
Updated SFOC models.

Will

MIAP
Completed planning (created a Markdown file of the math) for the LNG optimizer and conducted a detailed review with Mert.
Standardized notation, units, and variable names across code and documentation to remove convention mismatches.
Corrected mathematical errors and updated derivations; validated objective functions and constraints.
Began implementing the documented LNG optimization in code.

Reza

MIAP

Worked on the Digital Twin / Fuel Forecast performance pipeline, including:
Debugged an overestimation issue in the SFOC models and explained the cause to the assigned team member so they can correct the dynamic-model weights.
Debugged a problem in the time and/or distance columns of the silver_deployment.legs table that caused elevated speed values during the maneuvering phase and led to optimization failures; met with Alex Moss from the Deployment Systems & Analytics team to discuss the issue and potential solutions.
Deployed the workflow to the development environment for testing.
Held initial discussions on the output dashboard format for the MIAP web app. Next steps: continue debugging and develop dashboard concepts before pushing them to the MIAP web app.

Erick

**Axiom****/Medallia **

**Meta Data Extraction**

David M. (working for Erick) is working on migrating the topic labeling process to the new meta data generation framework. This will be a faster, cheaper, smarter approach to labeling medallia comments.

David M. is working on a pipeline to create quantized embeddings on all medallia comments which will serve several downstream use cases. One use case will is a new tool in the Axiom web app which will allow users to explore comments using network graphs.

Erick

**Axiom****/Medallia **

**Reporting**

Erick delivered the first Silversea AI email in December. Several points of feedback were given and will be working to make improvements/modifications.

Erick is working on automation of Division level email templates (Distribution list for Fleet detractor report: Raimund Gschaider, Jocelyn Lloret, Joao Mendonca, Richard Nentwich, christos Karavos, Nayoung Kim, IVELIN HRISTOV, FERNANDO CRAVO JORGE, Andreas Zachariou).

Erick scraped 3 websites to extract Celebrity and Royal ship level information. This will be used as context for the new meta data generation framework that David M. implemented.

Osvaldo, under Erick, documented all of his work for Genie and has merged his work with prod. Genie is pending business review.

Erick

**Axiom****/Medallia **

Danusio, under Erick, is working on delivering a Shorex Safety report for legal identifying safety related comments found in medallia comments.

Danusio is working on delivering a report for Legal summarizing guest feedback related to misrepresented pricing, offers, and deals.

Danusio & Rodrigo are both working on a pipeline/tool for ad hoc topic exploration to be used by CEL Consumer Insights. Approach 1 will use LLMs for clustering and Approach 2 will use BertTopic for clustering. This tool can be thought of as a way to automatically cluster, classify, and aggregate the topics in a given document.

Erick

**Axiom****/Medallia **

Rodrigo, under Erick, has finalized his work on the Port-of-call report. The biggest blocker is the data mismatch between Unity Catalog and Medallia which is being explored by data engineering.

Rodrigo is working on a new version of Shorex Marketing "Verbatims" that exemplify what consumers are telling us about their experiences on shore excursions. This could be used as novel marketing material placed on the web/app for guests such as "Guests love the views from the tour bus."

Rodrigo is working on a report for Nassau Beach Club aggregating all feedback we receive related to the new shorex.

Rodrigo implemented the ability to save ALL of our email reports to sharepoint.

Erick

**Axiom****/Medallia **

**Modeling**

Osvaldo is working on the Medallia Drivers model. Model has been trained and Osvaldo is performing extensive EDA on SHAP scores.

David M. is working on a Guest Log level classification model for cleaning up old topics to conform with new topic standards (over 1400 topics/subtopics make this task very difficult)

**Erick & Christian**

**MyCruise**** Recommender**

**Project Updates**

Cristian is actively reviewing how prior recommendations testing was performed including reviewing code, rewriting code, and building an intuition around the data and aggregations. Lots of effort has gone into translating R code into Python and questioning assumptions. Cristian will be holding a review session with the broader team on Friday the 9th to review his current approach and gain feedback.

We still need to align with Digital engineering on where and how Stage data will be used during QA for calendar recommendations.

**Cihan**

**PCP Pricing Automation: ****OBR Waterpark**
OBR Waterpark PRE (Owner: Gang Wang)
Completed/In Progress:
First PRE version was consistently hitting highest constraints; focused on improving the model and features.
Added Celebrity sailings to the dataset.
Simplified ship-class feature to a single column (count of Icon/Oasis ships at CocoCay for the tour date).
Grouped meta products into long (≥7 nights) vs short; reduced from three columns to two.
Applied target encoding to WTS bins and sailing_season (peak/holiday/summer/etc.).
Included forecasted total pax per sailing to estimate expected demand at CocoCay on the tour date.
Tested multiple constraint sets and initializations to reduce boundary hits.
Next:
Re-run optimization with revised features/constraints and report boundary-hit reduction and forecast stability metrics.

Cihan

RoyalOne Community: Digital – Guest Services Chatbot (Owner: Eunha Kim)
Pending:
Stakeholder to deliver escalation pattern definitions based on the provided sample dataset.
Next:
Convert stakeholder patterns into labeling/feature rules and proceed to initial training once received.

Mirielle
Contact Center: Lead Prioritization
LP Meeting: CVP Duplicate Leads, Web Chat Lead Delay, IDS Power BI Report
Outcome:
Duplicate lead behavior stems from guest actions creating multiple distinct booking IDs across time; production workflow functioning as designed.
Next:
Augusto and product teams to drive follow-ups; data team available for additional diagnostics as needed.

Mirielle
Contact Center: Workforce Planning – North America (12 LOBs)
Scope:

Key Scope is that Mirielle is working on building a competitive demand forecasting model for North America, which would replace the rules model in production.
LOBs: CO_GROUPS_SALES, CO_GROUPS_SERVICE, GEM, CE_SALES, LOYALTY, STAR, GROUPS, CASINO_SERVICES, CO_SALES, CASINO_SALES, RES, CO_CE_SERVICES.
Data: Train/test time split with 20% test (2023-01-01 to 2025-10-31); backtesting window through 2025-12-31.
Modeling/Evaluation:
Models: LightGBM, XGBoost, CatBoost, HistGradientBoosting (selectable via models_to_run).
Features: Calendar/holiday proximity, weekend/holiday interactions, lag/rolling stats, trend/volatility; optional AHT features when present.
Metrics: R², MAE, RMSE, MAPE consolidated and compared per LOB; best model flagged per LOB.
Visualization: Four-panel dashboard (metrics, residuals, actual vs fitted, actual vs forecast) plus history/forecast overlays; published from VS Code to Azure Container Instances.
Tuning: Focused hyperparameter sweeps with early stopping for underperforming LOBs; tracked versus baseline.
Next:
Complete backtests for all 12 LOBs; integrate AHT where available; circulate dashboard links and per-LOB readouts.

Caleb
Customer Lifetime Value (CLV)
In Progress:
Co-developed a 2026 CLV Plan (POC improvements, full build timeline, future scoping, brand engagement, sizing potential analyses).
Created slides detailing celebration analysis procedures: MECE lenses, cross-cuts, KPIs, and initial findings.
Running deeper analysis with stratification to control for premium inventory confounders using decision trees, ANOVA, and regressions; objective is actionable insights to increase celebrators via selective offerings, marketing, or bundling.
Built an ETL cost methodology workbook; proposal to move from ship class/month costs to voyage-level ship costs.
Next:
Finalize POC enhancements with Liz’s team; prepare insights/recommendations for Figgis and outline brand-specific pilots.

Carlos
Ecommerce Customer Targeting
Completed/In Progress:
Implemented gating in feature engineering to skip full processing for low booking propensity consumers; expected ≥30% compute reduction (pending production enablement).
Resolved production pipeline memory overflow errors; improved stability.
Presented enhanced booking propensity drivers report to ecommerce stakeholders.
Next:
Enable gating in production; monitor compute savings and performance; refresh drivers report with next data update.

Ben & Camila
Supply Chain
Medical/CocoCay/Uniforms Models
Goals: Improve medical MdAPE before guardrails by ≥10%; treat sparse product predictions separately.
Completed:
RCI/CCI Min–Max Par Volatility Report delivered.
Base SSC Uniforms model using crew data (for more accurate actuals and predictions).
get-model-error and challenger model notebooks updated for medical and CocoCay.
In Progress:
Uniforms challenger model path: array-type product fields complicate joins; building a modified unpivoted backtested table (v1) and extending to v5/v6 with crew attributes (cost center, contract length) and similar products mapping.
“Last Updated Dev Datascience Tables” for Yan and team to improve efficiency.
Awaiting feedback from Yan on consolidated Royal/Celebrity/Silversea tables (regions + predictions; same products across brands mapping).
Next:
Complete unpivot strategy for uniforms; integrate crew attributes; publish accuracy deltas; incorporate Yan’s feedback on consolidated tables.

Ben 
Supply Chain

Silversea Cruises 2026 Demand Forecasting — White Paper v1.0 (Ready to Execute)
Objective:
Adapt RCI/CCI 2026 feature engineering and RFECV validation to SSC’s luxury/expedition context; target MdAPE ≤2.5%.
Scope/Features:
296 candidate features (62 baseline, 108 enhancements, 84 SSC luxury/expedition, 30 RFECV-derived, 12 SSC-exclusive nationality features).
MAIN_STORE-based category schema across 11 SSC ships; voyage-level scaling and expedition features.
Methodology:
RFECV via Probatus (SHAP-based ranking), multi-period validation (5 sequential periods), cost-weighted MAPE to prioritize high-value products, leakage prevention via 1-week exclusive windows.
Implementation Phases & Timeline:
Phase 1 Feature Engineering (3–4 days), Phase 2 RFECV (2–3 days), Phase 3 Backtesting (1–2 days), Phase 4 Production Integration (2–3 days), Phase 5 ADF Integration (1 day). Total 9–13 business days; RFECV compute ~10–15 hours on LS_IBP_JC_BIG.
Success Criteria:
MdAPE ≤2.5%; 70–100 stable features (≥4/5 periods); feature stability ≥80%; no regressions vs 2025 baseline.
Decisions (Resolved in plan):
Use 1-week exclusive leakage-safe windows; prioritize via cost-weighted RFECV; train Silver Ray on its own 18+ months of data; initial target MdAPE 2.5%.
Next:
Kick off Phase 1: implement SSC_V6 feature modules, MAIN_STORE mappings, SSC nationality features; prepare RFECV sampling and backtest periods.

Ben & Camila
Supply Chain

ESG Proration & Finance Tool MAPE Implementation (Celebrity Beyond Pilot Preparation)
Delivered:
ESG demand proration with checkpoint-derived weights normalized to conserve demand (sum to 1.0).
Finance Tool MAPE alignment to Write_Parquet_Files (ABS error over ACTUALS × 100; robust zero handling).
Stub records for forecasted products without consumption to close coverage gaps.
Results:
Forecast coverage gap reduced from ~$100M to <$10M (target ≤$5M).
Voyage-level MdAPE (Nov 2025, core categories): ~14.5% (1M), ~15.2% (2M), ~15.9% (3M), ~16.7% (6M), ~21.2% (12M).
Product×Ship×Month MdAPE: ~9–15% across horizons; category example (1M): Beverage ~14.9%, Food ~20.8%, Consumables ~38.8%, Replaceables ~56.5%.
Technical Notes:
ESG effective date split: ETL applies proration for WRITE_DATE ≥ 2025-12-20; historical notebook applies retroactively for prior dates to avoid double-processing.
Weights derived from most recent checkpoint, aggregated weekly-to-monthly to match finance granularity; robust aliasing/casting to prevent union/join errors.
Next:
Execute Celebrity Beyond finance pilot; monitor proration weight freshness and accuracy alignment; prepare routine reporting on MdAPE and coverage.

Ignacio

PCP Pricing Automation

**Ignacio Villasmil**

**OBR | Back****-end checks on source data for OBR – JAN**
Scope: 2.0 story points
Comments: *Status*: This ticket is complete as of 11/??/2025. Deliverables: ??? Delays: Waiting for DE to change the source table from a view only table & optimize it in order to use it better for proper back-end checks on the source data. Potential future issue: None.
“AB testing automation is basically the same project Ignacio and Jesse are working on, but I'm waiting on Jesse to finish his part so that I can work on like unit testing and everything. So that's that ticket I'm basically… Because I need there needs, there needs to be a in a bridge between what Jesse's doing and what Ignacio's doing.”

**OBR | BUG | Alaska ****ShoreX**** inconsistent source data**
Scope: 3.0 story points
Comments: Duplicate product codes fixed; corrected average price calculations to exclude zero-price bookings; adjustments made to Daily FS & Binned FS; DE team to verify remaining inconsistencies.

**OBR | Create Continuous A/B Testing Framework – JAN**
Scope: 2.0 story points
Comments: No Jira comments.
“Dependency noted on Jesse’s work and Kartik’s unit testing bridge.”

**Aagam Shah**

**RCI Revenue Management**

**DUAL | GTY****-Lead 2.0 – handoff & maintenance**
Scope: 5.0 story points
Comments: Acceptance Criteria: GTY-Lead 2.0 handoff completed successfully; Maintenance plan documented and implemented; No critical issues remain.
“Sitting with Michelle almost seven hours out of eight, understanding what exactly is happening in the code, how it affects the business, and maybe what changes we have to make.”

**PRE – Logic Analysis (RCI | Basket Logic Enhancements)**
Scope: 2.0 story points
Comments: Acceptance Criteria: PRE logic analysis completed; Findings documented and shared; Recommendations provided.
“Still not sure what exactly we have to do over there, but I'll talk to Kevin maybe starting next week once I'm more or less done with the category gapping part.”

**MTRB 2.0 – Curve fitting / Cat****-class SPI integration**
Scope: 3.0 story points
Comments: Curve fitting functions aggregating at meta product level need to change to ensure cat-class granularity is added.
“Most of my time I'm focusing on understanding the category delete gap and oh sorry, category gapping from Michelle. Just understanding the code, seeing the areas where I might have to jump in to help Monica out.”

**Douglas Bedell**

**CEL Revenue Management**

**RCG | PRE Common Core Price Upload Facility – JAN**
Scope: 8.0 story points
Comments: Combine RCI and Celebrity PRE price uploads into one single process. Remove all remaining Oracle dependencies. Ensure all uploads are using the RMA price upload via DE table and trigger files.
“Massive ticket; some work will roll into February. Identified issue with Elasticity 4.0 code not running correctly in dev environment; permissions fixed; retested successfully.”

**CEL | Perks Gap Test – Monitoring & Final Findings (JAN)**
Scope: 5.0 story points
Comments: Continue monitoring of the Perks Gap Test. Present final findings from test results.
“Monitoring sample size differences; investigating mismatches in ALASKA/NEAR, ASIA/FAR, EUROPE/NEAR, LONG CARIBBEAN/FAR.”

**RCG | PRE Codebase**
Scope: 5.0 story points
Comments: No Jira comments.
“Broader tri-brand codebase consolidation (elasticity, business rules); expected to roll month-to-month.”

**Lamis Amer**

**RCI Revenue management**

**RCI – Pricing Optimization (JAN)**
Scope: 5.0 story points
Comments: This task extends the November work on price optimization validation and reporting, with a focus on model deployment into production and troubleshooting required during this process.
“We had a meeting with Nick early this week and received good feedback. Doing validations and adjustments this week; planning to push to production next week.”

**RCI – Track Optimization: validation & scaling to entire fleet (JAN)**
Scope: 5.0 story points
Comments: Validation and scaling optimization to run on the entire fleet.
“Already working on this task; scaling optimization code base for Royal and Celebrity.”

**Lamis Amer**

**CEL Revenue management**

**CEL – Track Optimization**
Scope: 3.0 story points
Comments: No Jira comments.
“Celebrity track optimization is in progress; code base is 90% same as Royal.”

**Kartik Ullal**

**PCP Pricing Automation**

**AB testing automation (sub****-task)**
Scope: 2.0 story points
Comments: No Jira comments.
“AB testing automation is basically the same project Ignacio and Jesse are working on, but I'm waiting on Jesse to finish his part so that I can work on like unit testing and everything.”

**Fix and work through web scraping for OBR team (sub****-task)**
Scope: 2.0 story points
Comments: No Jira comments.
“There was some web scraping projects they wanted to work on in the OBR team and I was helping Andrew on the OBR team with that. This is almost done and I'll probably I'll put it finish it up tonight or tomorrow.”

**RCI | OBR | Royal Beach Club – Jan**
Scope: 4.0 story points
Comments: No Jira comments.
“I've been moving over to Royal Beach Club stuff now, so a lot of my tickets are gonna be based on Royal Beach Club. Awaiting Kevin to hand over his code to me because once he does that, I'll be working on that and on top of that as well.”

**James McFall**

**RCI Revenue Management**

**RCI – Inventory KPI Mods (new SPI scoring approach)**
Scope: 2.0 story points
Comments: Current focus: refine the scoring model to provide the most effective SPI possible. Factor models will require more specific requirements from users later.

Nick was pleased with the improvements on the SPI model and is ready to move on to the factor model(s).  Huge step and excited he feels comfortable about it.

**DUAL – SPI Factor Model (breaking tracking)**
Scope: 5.0 story points
Comments: Same as above; exploratory analysis of factors and relationships to SPI.
“Team member had a conflict and could not attend.”

**DUAL – RCI/CEL V2 SPI Scoring Model (JAN)**
Scope: 5.0 story points
Comments: Refactor and pipeline improvements for SPI scoring. 
“Team member had a conflict and could not attend.”

**Jesse Bausell**

**SSC AB testing for PRE**

**RCG – Create robust Power Analysis Framework**
Scope: 7.0 story points
Comments: No Jira comments.

Universal A/B Framework

Today I presented the latest version of the Universal A/B Framework to Data Science management. In this updated version, I added a power analysis module that takes paired samples and user-supplied inputs to compute the statistical power of said A/B test. It also computes distributions from past samples (included in the input table), which it uses to draw samples for the power analysis. The updated Universal A/B Framework also has modifications that enable “Gecko” code to be added to it. Moving forward, I will annotate my code and simplify the user input yaml file to make it accessible to a non-data professional.
“I finished the robust power analysis framework; spent about seven days on it.”

**SSC PRE – Feature Store Upgrade**
Scope: —
Comments: Upgrade feature store tables so no data are being dropped. Shift data pipelines from table generators to scripts that update existing tables.
“Not started yet; will scope when work begins.”

**SSC PRE – PRE Vista Elasticity**
Scope: 2.0 story points
Comments: Pinpoint a single example of price elasticity in SSC by examining the lowest cabin category, Vistas (VI).
“Not working on this right now; may revisit later.”

Kevin

PCP Pricing Automation

Kevin has delivered a Databricks Dashboard with extensive reporting on Royal Beach Club. This includes financial metrics of money made vs forecast (from track) as well as building out prototype automation for pricing recommendations of the Royal Beach Club.

Glen-Erik

PROPEL

Resolved Offer delivery delay caused by ship concentration in the same time zone creating a queue for offer creations. Offers were taking up to 7 hours to complete, now back down to 2-3 hours.

Provided support over the Holidays as ships were having daily offer delivery delay issues due to the above queue.

Enabled offer templates in dev for all shorex, spa, and raw on 5. Created and tested template for awareness offers for shorex, still work in progress.

Eswar & Javier

RCI Revenue Management

RMA: Assisted RMA team with code conflict and deployment issues and job run failures.

Automated Code Review: Created dashboard to track code violations across the entire codebase over time to get a wholistic picture of compliance, rather than focus only on the violations present in the PR. The prior compliance dashboard presented an inaccurate/incomplete picture since it didn't include any of the things that were actually fixed, only the things that weren't and if those were fixed after they were flagged.

Contact Center

**Accomplishments Last 7 days? (Accomplishment + Impact)**

Please include project and business impact

**SpeechIQ**** to Cresta Transition**

Scraped Cresta front-end for blocks and behaviors to identify gaps and align systems.

Initiated data validation process to ensure all use cases are included for transition.

Impact: Supports seamless migration from SpeechIQ to Cresta, improving agent guidance and operational consistency.

**Cresta New Hire Pilot**

Implemented a logarithmic model to estimate learning-rate improvements for new hires, showing positive alignment with expectations.

Reviewed dashboards and pilot results with stakeholders.

Impact: Accelerates onboarding efficiency and reduces Hold + ACW times, improving overall agent productivity.

**Cresta Full Rollout & Optimization**

Defined KPIs for Phase 2 and advanced call skill mapping for Phase 3.

Collaborated with Cresta to identify tailored hints/behaviors for Sales departments.

Impact: Enhances agent performance and optimizes customer interactions across multiple phases.

**Conversational IVR**

Monitored existing IVR solution, noting a significant increase in automation rates due to seasonality.

Supported Guest Profile API deployment and troubleshooting.

Impact: Improves call routing efficiency and enhances customer experience.

**Copilot Migration & Reporting**

Supported testing team with creation of test cases for migration.

Developed best practice guide for bot building and tagging to enable accurate reporting.

Impact: Lays foundation for robust voice agent performance reporting and operational insights.

**Generative AI FAQs**

Continued prototyping for six approved topics (App, Wi-Fi, Dining, Luggage, Ground Transportation, Beverages).

Extended use cases with common questions extracted from Cresta and refined filters in vector database.

Impact: Reduces call volume by enabling voice-based self-service for common inquiries.

**Guest Profile API Integration**

Secured initial approvals from IT and business; awaiting production readiness.

Impact: Enables personalized guest experiences and improves data availability for agents.

**Leadership & Operational Support**

Built senior leadership presentation on Contact Center and project status.

Partnered with IT on disaster recovery planning and coordinated Phase 1 training approach.

Impact: Strengthens operational resilience and ensures leadership visibility on progress.

**What is currently being worked? (Task + Expected Impact)**

Please list projects and expected outcomes

**SpeechIQ**** to Cresta Transition**

Presenting data gaps to QA team and driving ingestion of data for parity between systems.

**Cresta Rollout & Optimization**

Monitoring New Hire Pilot and reviewing KPIs for Phase 1 and Phase 2.

Pulling Phase 1 data for initial analysis to validate rollout methodology.

Advancing optimization by leveraging SpeechIQ insights for new Cresta behaviors.

**Copilot Reporting & Migration**

Pulling data for Copilot agent reporting and Cresta agent reporting.

Continuing support for migration testing and refining reporting structure.

Impact: Enables accurate performance tracking and actionable insights for voice agents.

**Guest Profile API Integration**

Preparing for production testing and Data Warehouse build once API is live.

**Generative AI FAQs**

Continuing prototyping and expanding use cases for voice-based self-service.

**Research & Insights**

Identifying call deflection opportunities through insights for other business units.

Investigating SMS use cases and efficiencies across FAQs, app, and policies.

**Operational Support**

Developing combined project plan for Cresta production rollout.

Managing leadership-level presentations and supporting 360Learning implementation for training accuracy.
