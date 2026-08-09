**Henry Drescher**

**Contact Center ****ConversationalAI**

**Key Updates**

**Optimizing Cresta and piloting **

**Agent assist**

**Analytics**

**AI analyst (ChatGPT style interface to ask questions on transcripts)**

**Migrating Conversational IVR to CoPilot**

**Developing conversational IVR backlog**

**Working with Ben and team for scaling forecasting**

**RFP for CCAS vendors**

**Kevin, Lamis, and Atefeh**

**RCI Revenue Management - Pricing Elasticities**

**RCI: Elasticity Model Integration development is complete and in QA, expected to be used in coming week’s PRE run. Considerable progress was made on Track Optimization to integrate the new elasticity model and to adjust logic to better match business expectations.**

**Kevin, Lamis, and Lekha**

**CEL Revenue Management - Pricing Elasticities**

**Backtesting**** framework ****completed**** and was used to assess over fitting concerns on CEL elasticity model. Several versions of clickstream informed baskets were prepared and shared with the business. Further integration with existing baskets ****in**** progress.**

**Michelle**

**RCI Revenue Management - Category Gapping**

**Logic adjustments made to GTY-Lead 3.0 cutting ****compute**** time from over 40 minutes to less than a minute per sailing. Different binning strategies are being explored to more closely align with business expectations.**

**Michelle**

**CEL Revenue Management - Category Gapping**

**Logic adjustments made to GTY-Lead 3.0 cutting ****compute**** time from over 40 minutes to less than a minute per sailing. Different binning strategies are being explored to more closely align with business expectations.**

**Aagam**

**RCI Revenue Management - Pricing Elasticities**

**Developed and prepared analyses on PRE price change logic decisions to better assess track targets**

**Aagam**

**CEL Revenue Management - Pricing Elasticities**

**Developed and prepared analyses on PRE price change logic decisions to better assess track targets**

**Kevin & Kartik**

**Refreshed ****spend**** to save results. Refactored power analysis on choice benefits for more specific findings to better account for business landscape ****stly****. Delivered initial power analysis for co-brand card pilot. Kartik Currently working through matched pair design for choice benefit audience**

**Ben & Camila**

**Supply Chain Analytics**

**Accomplishments & In-Progress Initiatives**

- **IBP Award:** As we wrap up the second quarter of the year, IBP was honored to receive incredible recognition during the Silversea Operation Townhall today for the accomplishments we’ve achieved together so far this year. We want to take a moment to sincerely THANK YOU for your dedication and support throughout this journey. Without each of you, IBP would not be where it is today.

**Enhanced Demand Forecasts in Cursor****: ** The Supply Chain team is experiment with Coding Agents to accelerate productivity for ML deliverables with highly positive results:

Launched advanced time series feature engineering (trends, seasonality, outlier labeling, consumption momentum, statistical features) and ship class-specific consumption factors.

Developed cross-product relationship analytics (complementary, substitute, correlation features) and newly engineered mathematical features for improved predictive stability.

Implemented scalable hyperparameter optimization and robust cross-validation ensemble modeling (including model uncertainty metrics, performance logs).

Operationalized concept drift detection using distributed Spark UDFs across 200k+ models, delivering comprehensive performance reporting and alert classification.

Currently testing code scalability in Spark and determining production integration strategies.

**New Ship Demand Automation**

Fully automated newbuild ship identification using voyage/consumption data; removed hardcoding for ships like XCEL/STAR.

Dynamic handling of maiden voyages, ship class/sister ship assignments, and reference data updates—now factoring in gross tonnage and other operational heuristics.

Enhanced logic for onboarding new classes and phased-out “new” status after sufficient data accrual, maintaining up-to-date sister ship mapping.

Actively iterating on automation logic for edge cases (Celeb. river ships, future classes).

**CocoCay Forecast Guardrails**

Deployed guardrails to correct high-variance prediction outliers by calibrating forecasts to recent actuals (delivering >50% improvement on 839 SKUs/products out of 1,614 evaluated).

Introduced special reporting for SKUs with marginal/zero improvement, targeting ongoing refinement for sub-10% improvement group.

Established a dedicated dashboard page for CocoCay model metrics; evaluated dashboard scalability and prepared for widget/query growth.

**Expedition Inventory Forecasting**

Delivered completed forecasts for parkas, bottles, backpacks (including child/adult size ratio refinements for parkas, and voyage-level demand adjustments for specialized SKUs).

Integrated total cabin capacity for ship-level demand estimation; calculated out-of-stock projections for all inventory categories.

Addressed missing data and “zero” forecasts; further investigation ongoing for items with limited history (notably, bottles on non-expedition ships).

**Other**

Finalizing intern presentations for review with leadership.

**Ben & Camila**

**Supply Chain Analytics**

**Upcoming**

Integration and productionizing of new Cursor features and models.

Ongoing refinement of CocoCay guardrails and dashboard modularization.

Finalize item-count anomaly investigations in expeditions forecasts.

Ben & Caleb

**Customer Lifetime Value (CLV)**

**Accomplishments**

Conducted C-suite session for Celebrity, presenting actionable cohort statistics and value/NPS index exploration.

Delivered comprehensive cohort feature analysis to Corporate Strategy; introduced clustering framework to pinpoint underlying customer patterns and discussed methodology adoption with leadership.

Validated analytics pipeline NPS against Medallia, confirming data integrity.

Ben & Caleb

**Customer Lifetime Value (CLV)**

**In-Progress/Next Steps**

Expanding CLV pipeline clustering via PCA/MCA to enhance behavior segmentation.

Cataloguing all pipeline scaling issues ahead of future architecting.

Ongoing collaboration with Hotel Ops to improve casino revenue attribution and GTR/NTR differentiation.

Preparing intern presentation for upcoming executive review.

Carlos

**E-Commerce**** Customer Targeting**

**Accomplishments**

Improved booking propensity model accuracy by refining validation dataset selection and training protocols.

Upgraded dashboard visualizations (removed empty bins, optimized sorting; implemented recommended confidence thresholds for PCP models).

Integrated uplift metrics into Databricks dashboard—enabling visibility into Persuadable Consumer segments who book only when exposed to targeted offers.

Completed optimization and integration of dashboard queries; transitioned business logic from SQL to PySpark for greater scalability and efficiency.

Initiated exploration of Databricks Genie API for future conversational analytics integration.

Carlos

**E-Commerce**** Customer Targeting**

**In-Progress/Next Steps**

Validating dashboard KPIs and collaborating on further query optimizations with the data engineering team.

Exploring data source expansion and Genie AI integration opportunities for the e-commerce analytics platform.

Preparing final internship presentation for executive leadership.

**Mirielle**

**Contact Center**

**Lead Prioritization & Data Pipeline Modernization**

Coordinated ingestion setup for all lead types across Royal (6) and Celebrity (8) portfolios with Siebel/DS teams.

Aligned and updated file output structures (including CRUISE_PREF_TEXT column enhancements, new variables, and ordering) per product stakeholder requirements.

Initiated iterative end-to-end testing with Siebel: SFTP file transfer, monitoring sequence IDs, pipeline staging, and input/output reconciliation for data integrity.

Actively working on comprehensive ingestion validation, supporting both Royal and Celebrity models.

**Mirielle**

**Contact Center**

**Workforce Planning POC**

Adapted international staffing model functions for North American context; ran initial RES line-of-business scenarios.

Drafted project walkthrough, reviewed with stakeholders, and collected feedback and design input.

Outlined and aligned on three-phase roadmap (from basic forecasting and UI build, to full forecast model integration and FTE computation).

Immediate next steps: finalize Casino LOB mapping, aggregate office shrinkage factors, and begin phase one app/testing cycles.

Cihan

**Pre-Cruise Pricing**** Automation**

**Accomplishments**

Migrated Oracle data platform to Databricks (via Azure Data Factory) for improved pipeline agility and accessibility.

Initiated detailed data validation and EDA—benchmarked new table calculations against established dashboard numbers to ensure alignment.

Cihan

**Pre-Cruise Pricing**** Automation**

**Upcoming**

Deepen EDA to extract customer and market insights.

Schedule stakeholder sessions to present findings, gather feedback, and chart the roadmap for advanced analytics implementation.

Cihan

**Digital ****App Analysis**

**Accomplishments**

Completed comprehensive topic classification for app review data.

Held results meeting with stakeholders, reviewed classification output and impact areas.

Erick

Medallia
### In-Progress

- Developing a brand new App using Flask (versus Streamlit)
- Enabling deeper data insights (by family status, age group, nationality, loyalty, casino engagement).
- Division / employee level / guest segment specific email templates.
- NPS comparative analysis for state and nationality level.
- Improvements to email formatting, modular sorting, and linking to supplementary detail.
- Exploratory work on using NPS Driver Model for advanced sorting and reporting.
- Developing preliminary/final report timing and Celeb-specific email logic.
- Celebrity fleet summary updated with top topics.

Erick

Medallia
### Completed
- Interactive heatmap completed.
- Ad hoc ETL updates, email list updates, and duplicate email suppression hotfixes.
- Enhanced email sorting (NPS, ratio-based).

Erick & Parimala
## Axiom – Guest Service Logs (Medallia)
### In-Progress
- Ongoing work on time-zone-based automation for shipboard daily email recaps.
- Forecasting mid-cruise NPS using guest logs sentiment and topic analysis.
- Acronym mapping for improved entity extraction.

Erick & Parimala
## Axiom – Guest Service Logs (Medallia)
### Completed
- Brought Medallia topics into guest logs for topic parity.
- Added sentiment (end mood) to GenAI chunking context.
- Automated ETL for Guest Logs dataset refresh.

Erick
## Axiom – Medallia App
### In-Progress
- Infrastructure migration to Azure container apps for long term scalability.
- Ongoing app stability improvements (error tracing, try/except blocks).
- Addressing UC permissions expiration requiring app redeploys.
- Scope out work for "OE Tool" proposed by Consumer Insights as feature for app. 
- Implementation of new and extended filters (Sailing, Consumer, Product/Venue specific, Booking Promo, Internet/Beverage, NPS comment, Voyage ID).
- Preparation for more advanced model options (gpt4o-mini, gpt4.1-nano).
- Data source migration and discrepancy reduction (Medallia API updates, improved ingestion pipeline).

Erick
## Axiom – Medallia App
### Completed
- Deployed new Flask-based web app with robust CI/CD pipeline and Cursor integration.
- Scraped ship coordinates data.
- New web page with 3D mapping of newly scraped ship coordinates data.

Erick
## Axiom - NPS Driver & Thresholds Analysis (Medallia)
### In-Progress
- Experimenting modeling normalized medallia scores for thresholds model.

Gaurav 
## Digital RoyalOne Community
### In-Progress
- Deep-dive on app engagement journey and its impact on pre-cruise purchases.
- Refining queries/feature engineering for mapping app events to revenue.

Erick & Christian
## MyCruise Recommender
### In-Progress
- Rollout of enhanced customer segmentation (granular clustering, mini-batch KMeans, MLflow tracking).
- New model retraining and documentation for improved ALS segmentations.
- ETL pipeline alignment for API/model refresh and live purchase integration.
- GenAI-driven product category and user preference sorting for personalized recommendations.
- Development of functional/automated unit tests for all models and ETL components.
- Ongoing research into recommender metrics, algorithms, product classification, and API improvements.

### Completed

- Release delayed due to frontend toggle issues for MyCruise recommendations by Digital. There were a few issues that popped up during go live and will need some development time to fix. Namely having to do with the on/off button for the recommendations not working properly.  While delayed until next release (1 month delay), this will be a HUGE accomplishment and a long-time coming to integrate recommendations into front-end guest experience
- API stress-testing and validation, including EDA, diagnostics, and troubleshooting.
- Deployed optimized ETL and associated DataBricks job for production.
- Implemented batch LLM tools and agentic mass processing for AI categories.

Parimala & Erick
## Lead Scoring – CTI (Contact Center)
### In-Progress
- Improving deployment & CI/CD efficiency, reducing manual MLOps dependencies.
- Exploring automated threshold mapping updates in the CTI workflow.
- Continuing to improve and evaluate model performance.
- Ongoing research and validation on river cruise expansion logic and new lead/quote views.

- Parimala & Erick
## Lead Scoring – CTI (Contact Center)
### Completed
- Deep-dive/troubleshooting completed on Galapagos product and probability assignment.
- River cruise logic and field-level exploratory analysis (29 call reasons) completed.
- CTI model retraining and production deployment, ensuring parity between Dev and Prod.
- Retrained model live; data validated, edge-case MVAL logic reviewed.
- Asset bundle deployment issues partially resolved in collaboration with MLOps.
- Detailed analysis conducted on lead conversion and probability range assignments.
- Methodology for lead conversion and logic enhancements reviewed and applied.

**Ayon **

WOW Updates:

**Resolved** major library incompatibility issue that occurred due to Databricks pushing silent background updates. The issue stopped the new pipelines, and we notified the Glen Erik and Eswar. However, we resolved the changes over the weekend through Monday EOD. This didn’t result in production outage because the old pipelines ran to generate forecast data as backup.

**Pleased to announce:** The Specialty Dining forecasting (version one) pipeline and models have been rolled out to production successfully. The new pipeline is a huge enhancement over old pipeline. The new model is more curated, and enhanced such that it reflects in the accuracy and performance report – a summary of comparison between the old and the new pipeline is as follows:

**Overall Accuracy:**
The new pipeline outperforms the old pipeline **72%** of the time in terms of prediction accuracy.

**Ayon **

WOW Updates:

**Popular Items Performance:**
For the most frequently sold items, the new pipeline performs **84% better** than the old pipeline.

**Ships with Frequent/Popular Items Performing Better on New Pipeline:**
['SY', 'WN', 'SC', 'VY', 'LB', 'QN', 'AL', 'GR', 'VI', 'HM', 'OA', 'OV', 'IC', 'AD', 'BR', 'SR']

**Ayon **

WOW Updates:

**Least Frequent/least popular Items Performance:**
For less frequently sold items, the old pipeline performs **16% better** than the new pipeline.

**Ships with Least Frequent Items Performing Better on Old Pipeline:**
['EN', 'AN', 'OY', 'EX', 'UT', 'MA', 'FR']

**MAPE Accuracy:**

New pipeline predicted with **MAPE ≤ 20% in 80% **of times.
Old pipeline achieved the **same accuracy in only 20% **of times.

**Additionally,** the new pipeline predicts on 9,687** **model groups**(****recipe+ship+meal_peiod****)**, compared to **5,614 **groups **(****recipe+ship+meal_peiod****) **in the old pipeline, indicating a broader and more comprehensive coverage.

**Ayon **

WOW Updates:

Rolling out forecasting solution for Windjammer today.

**Pleased to announce:** The Windjammer pipeline (complementary venues pipeline), designed to project guest buffet consumption based on historical trends, has been rolled out as well. The Windjammer pipeline and models factors in **menu rotation** for all meal period and **cold start** use cases of ship deployments in geo locations (without history of that specific ship + recipe combination). Additionally, the pipeline and models has been carefully curated to match the specialty Version 1 pipeline for easier debug and future enhancements keeping all pipelines as much consistent as possible. Glimpse of accuracy achieved:

Although Absolute percentage error (APE) is less informative for small consumption items (which we have many) since a 1- or 2-unit deviation can result in a 30-50 % APE, it can still provide a useful    overall view of the model performance. Encouragingly, we can observe that **50%** of last week's predictions were within the **0-20%** APE bin, and cumulatively **75%** of the predictions were within the 0-**40%** APE. This suggests that the model is performing reliably for most items, even when accounting for the inherent variability in APE in smaller-volume predictions.

Over all stats:

**Median abs percentage error:** 21.507

**Median abs error:** 6.85

Windjammer pipeline predicts on **6000 **model groups**(****recipe+ship+meal_peiod****)**,

**Ayon & Glen-Erik**

**Win-on-Waste pipelines**

Solved prod failures in WOW project. One notebook failed due to improper calling of import notebook and another failed due to having python kernel restart command in between the commands which caused loss of all variables stored throwing error.

Identified lot of improvements in WOW project like switching the workflows to Job compute, currently running with all-purpose compute. Implement env separation, right now project is running in prd. Advisory on best coding practices.

Help WOW developers in fixing compute issues they are having.

**Mert:**

**MIAP:**

Completed the Scrubber Power dynamic model for all ships in the fleet.

Held a workshop with GMO and Newbuild on shipboard Alarm Management and discussed how MIAP and GenAI can be used to analyze alarm fatigue onboard ships.

Discussed with Mike Tepel how we can combine this effort for decarbonization optimization, not just revenue optimization. This presents a potential CAR opportunity. The Deployment team is concerned about unclear IRR, but we have the potential to add this additional scope to the Digital Twin Model Phase II Project.

**Arya:**

**MIAP**

Identified the engine causing data issues on the power plant.

Built a power plant outlier detector for individual diesel engines to identify anomalous SFOC and power data values.

Edited the power plant configuration so that every ship’s diesel engine can now be used.

Successfully found and resolved a tag mapping issue with *Star of the Seas* and *Icon of the Seas* due to incorrect longitude tag mapping.

**Mahshad:**

**MIAP**

Worked on the Thrusters model and integrated it into the QA pipeline for testing.

Added visualization for the fan ratio to identify additional energy-saving opportunities in machinery.

Investigated a saving opportunity on the dimming board at HM, estimated at around 100 kW. The issue was traced to faulty sensors on a couple of dimming boards. Contacted the ship, and they have resolved the problem.

Identified a saving opportunity of approximately 120 kW on the HVAC AHU at IN. Prepared documentation and awaiting team approval before contacting the ship.

Resolved a humidity data issue on VY.

Analyzed the SC scrubber’s high energy consumption, which peaked around 300 kW.

**Brendan**

**MIAP**

Continued development of the Fuel Forecast Total Propulsion Power Prediction API. Simplified code to reduce repetition and unnecessary complexity.

Began laying the foundation for a reusable framework to enable other MIAP developers to rapidly implement future Fuel Forecast components. Next week will focus on enhancing reusability and cross-training the team on best practices.

Created a plan to reduce MIAP Workflow Failures by 75%, including:

Using federated authentication instead of PATs (already completed).

Enforcing successful QA workflow executions before approvals for PRD PRs.

Tuning failure-prone tasks in the MIAP ETL job.

Discussed MIAP ETL job performance tuning strategy with Ram, covering simplification of SQL queries, partitioning and workload distribution, and minimizing processing at each step to avoid cluster overload.

Mentored the MIAP Data Science team on Git best practices, including advancing from feature branch to QA, combining files from multiple branches into a single PR, resolving merge conflicts, etc.

Remediated the new AHU Cooling Power Workflow by updating the MIAP Databricks Asset Bundle.

Established development standards within the MIAP dev team for promoting code from Dev → QA → Production, minimizing the chance of errors reaching production. This will improve MIAP stability and increase end-user trust.

Supported MIAP Data Scientists with troubleshooting bugs, workflows, Git, and other related tasks.

**Reza:**

**MIAP**

Used AHU model results on the GMO app to identify AHUs with anomalous electrical consumption on the ship *Summit*. Pinpointed the root cause using the Valmet platform, created a report, and sent it to the team. After contacting the ship, they confirmed the anomalies and corrected the control platform settings. This resulted in a saving of 42 kW, worth approximately $14k.

Used AHU model results on the GMO app to find AHUs with anomalous electrical consumption on the ship *Millennium*. Identified the root cause using the Valmet platform, created a report, and sent it to the team. The ship’s AC engineer has been contacted with supporting documents. This has a potential saving of 72 kW, worth approximately $24k.

Fixed a bug in the AHU cooling power workflow.

Working on gathering and joining required tables for fuel consumption from various sources, including "fleet voyage reports" and "facts" — ongoing task.

Fixed a bug in the Fuel Analytics workflow.

Kevin, Glen-Erik, Esward

Revenue Management Automation RCI

Operations:

Feature store workflows cleanup, revising the workflows and removing uneccessary ones.

Paused OBR Optimization Routines workflow and renamed them for clarity.

Deployed 2 new projects Event Driven Suites Target and Event Driven Suites projects to prod.

Solved git related issues to RCI data scientists and help them in productionizing their changes.

Monitored CI/CD deployment pipelines and review PR's

Automated Code Review:

Refined code to be able to exclude specific flake8 checks that would overwhelm end users if implemented.

Centralized the config files to keep the current configuration structure with one file instead of requiring 3 files, which would cause confusion and mistakes.

(in progress) Ability to run against entire repo for centralized refactoring:

Enabled running all validations on a local folder without requiring Azure DevOps integration.

Alejandro

PROPEL

Credit holders: Developed a dedicated offer for guests holding onboard credit.

All-Included vs RO: Since preferences differ across spend percentiles, specific rules were created at the percentile and AI/RO group level.

Awareness offers for all CEL: All guests now receive either a monetary or awareness offer.

New split: 90% of guests receive a monetary offer, increasing chances of conversion and APD uplift.

[In progress] Experimental design update / Dynamic Control groups: Developing new logic to support 100% offer coverage during a sailing without losing statistical power in measurement.
