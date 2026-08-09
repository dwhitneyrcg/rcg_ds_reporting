**Mert & ****Mehdi**

**New Build**

Completed the Newbuild Revite Agentic AI chatbot app and presented it to stakeholders.

Worked to improve EDA on stability data. Performed feature engineering and calculated feature importance metrics using RF and XGB models. Evaluated performance of different regression models.

Discussed datasets and results with the stability team.

**Mert:**

**MIAP**

Started development of the Scrubber Power model and completed it for several ships.

Resolved cybersecurity vulnerabilities across multiple MIAP repos and updated Python packages.

Deployed Explorer of the Seas MIAP IoT Flow.

Prepared a demo anomaly detection model for casino table games data, saved the model to the Unity Catalog, and it is ready to be deployed on MIAP Edge servers (Crosser) as RCG's first Edge streaming ML model in partnership with IT. Received EA approval for the POC. Pending confirmation that Gang's team will allow the POC work before proceeding. The model will run onboard independently of the internet, predict with streaming data, and send anomaly flag signals.

**Reza:**

**MIAP**

Created and added AHU cooling power workflow.

Brainstormed and implemented ideas on the stability project.

Working on development of the fuel consumption model based on voyage info, including creation of required feature tables and performing EDA and queries.

Prepared slides for MIAP presentation titled "MIAP Status Update."

Fixed a bug in GMO app plots.

**Mahshad:**

Worked on the issue related to pipeline tag mapping for ETL.

Analyzed VY chillers power consumption (~500 kW).

Followed up on AD chillers with higher power consumption (~700 kW).

Collaborated with the engineering team to evaluate WHR, VFDs, and pumps for the ML class; identified false positives regarding higher consumption concerns for CS and ML.

Analyzed HVAC figures on GMO APP.

Identified potential energy savings that need further investigation and follow-up:

AHU CS: ~60 kW to 100 kW

SY AHU: ~100 kW

ML AHU: ~50 to 60 kW

Prepared a couple of slides for the MIAP presentation titled "MIAP Status Update."

**Brendan:**

**MIAP**

MIAP API:

Performed total cost analysis of MIAP API

Fixed bug leading to inability to load environment variables in MIAP REST API development environment

Fuel Forecast API:

Defined requirements document for MIAP Propulsion Fuel Forecast API and refined w/ Mert

Continued implementation of Fuel Forecast API for Total Propulsion Power Predictions

API Standards meeting with EA pushed back to next week

Operational Support:

Helped MIAP Data Scientist identify root cause of missing column error (improper tag mapping)

Researched repeated MIAP workflow failures reported by CAP team - devised plan for remediating issues

**Ram:**

**MIAP**
*This week:*

Finalized the approach for the Eniram Historical Notebook and completed two related notebooks.

Made necessary modifications and am in the process of cleaning up the final code for the Eniram Incremental notebooks.

Received additional inputs requiring updates to the Eniram logic, which I am currently implementing.

Analyzing the MIAP ETL workflow and brainstorming potential improvements.

Pushed the Sea Events code to QA for testing.

Reviewed the Eniram code score and am incorporating the suggested changes.

**Ram:**

**MIAP**

*Next week:*

Deploy the Eniram Incremental code to QA for testing over the next two days, followed by deployment to production.

Perform end-to-end testing of the Eniram Historical notebooks, then move them to QA.

Work on MIAP ETL improvements.

**Arya:**

**MIAP**

Created explanatory visualizations detailing areas to focus on to reduce the number of safety incidents and created a pitch deck for it.

Figured out how to use ARCGIS with Python to create a dynamic map to track ship routes.

Read 3 chapters of sequential decision analytics and modelling.

**Will:**

**MIAP**

Reworked overall and individual power plant model metric plots so that each type appears on one plot and there is only one selector for individual power plant models.

Fixed issue with column naming in Fuel Analytics.

Implemented back-testing in the dynamic model.

Implemented cross-validation in the base model.

Started fine-tuning dynamic models.

Ayon Ghosh

Win on Waste: WOW Update 7/25:

1) Launched specialty V1 pipeline

2) Hotfixes on windjammer pipeline

3) Hotfixes on MDR V1 pipeline

4) Developing rules engine for windjammer and MDR V1

Ben and Camila

Integrated Business Planning (Supply Chain)

Accomplishments:

• Completed enhanced demand forecasts for new build ships; fixed mapping bug for Star and Xcel.

• Automated daily, monthly, and quarterly consumption and spend reports. Migrated notification workflow ahead of Teams webhook retirement.

• Improved CocoCay forecast accuracy by ~30% (MdAPE). Developed and testing new guardrails for outlier variance.

• Consolidated expedition item tables; updated Uniforms V3 model, presented to business.

Ben and Camila

Integrated Business Planning (Supply Chain)

In Progress / Next:

• Finalize CocoCay and Uniforms model improvements (V4 underway).

• Roll out new dashboard features; integrate additional uniform features (materials, possible sizing).

• Expedite review/test of expedition item forecasts.

Risks/Needs:

Uniforms V4 model experiencing over-simplification—will adjust segmentation to retain accuracy.

Carlos

E-Commerce Customer Targeting

Accomplishments:

• Prototyped advanced visualizations (network graph, sankey, sunburst) in Pyvis for dashboard enhancement.

• Developed new methods for uplift modeling and refined scoring metrics for marketability.

• Standardized demographic filter experience across dashboards.

• Generated new query (via PySpark) to identify incremental bookers due to targeted offers.

• Began Databricks dashboard table creation PR.

Carlos

E-Commerce Customer Targeting

In Progress / Next:

• Correct inaccuracies in “consumer scored” metric; finalize, clean, and deploy updated dashboards.

• Complete uplift model integration into dashboards.

• Research Databricks Conversational API for possible Genie AI chatbot feature.

Risks/Needs:

Validation and deployment of uplift/scoring metrics required before launch.

Cihan

Digital Analytics (Digital App Reviews)

Accomplishments:

• Finalized LLM-based topic classification function, incorporating stakeholder feedback.

• Locked taxonomy of review topics for labeling.

• Initiated topic classification runs on app reviews.

Cihan

Digital Analytics (Digital App Reviews)

In Progress / Next:

• Complete automated topic classification for all app reviews.

• Share results in upcoming stakeholder review session.

Risks/Needs:

No blockers at this time.

Ben

Customer Lifetime Value (CLV)

Accomplishments:

• Validated new indirect cost methodology, updated to rate-of-cost/booking.

• Verified consistency between CLV analytics and Rev Planning reports.

• Delivered merged “clv_agency” analytics table to Trade, enabling targeted high-value guest strategies.

• Detected critical drop in casino guest spend index—deep-dive initiated with Hotel Ops and data teams.

• Supported Corporate Strategy with new cohort analyses.

Ben

Customer Lifetime Value (CLV)

In Progress / Next:

• Continue validation of casino spend methodology and disaggregation by sailing/variable.

• Rerun analytics pipeline with streamlined logic.

• Enhanced error tracking in workflow.

Risks/Needs:

Casino data quality/methodology a top investigation priority.

Cihan

Pre-Cruise Pricing Automation

Accomplishments:

• Presented Exploratory Data Analysis (EDA) findings to stakeholders.

• Flagged issues with outdated tables; coordinated remediation with data engineering.

Cihan

Pre-Cruise Pricing Automation

In Progress / Next:

• Initiate Oracle-to-Databricks migration via Azure Data Factory.

• Continue EDA and feature engineering on refreshed dataset.

Risks/Needs:

Legacy data constraints—closely monitoring effectiveness of ADF migration.

Mirielle

Contact Center Analytics

Lead Prioritization:

• Completed ingestion and monitoring of key Royal & Celebrity lead types.

• Verified data flow and pipeline consistency with Siebel and SFTP teams.

Mirielle

Contact Center Analytics

Workforce Planning POC:

• Adapted international staffing model; processed for North America RES LOB.

• Drafting project walkthrough for stakeholder alignment.

Erick

Guest Logs GenAI Reporting

- In Progress:

- Including “End Mood” in GenAI text chunks.

- Continued to work with business on an in-depth acronym dictionary for guest logs to augment LLM context.

- Added topic classification to guest logs to enable parity between guest logs and medallia.

Guarav

Digital App Analysis

- In Progress:

- Excluded low interactions guests from analysis and re-running feature importances.

- Developing a query to aggregate web/app data to map out Digital journey prior to PCP purchases.

Erick

Medallia Driver Analysis

- In Progress:

- Designed an initial version of a tool that simulates thresholds afterwhich NPS is affected - given changes in underlying Medallia metrics.

- Aggregating topic-level to rating-category level for analysis.

Erick & Parimala

CTI (Contact Center Intelligence)

- In Progress:

- Trained new R/C scoring models to improve performance.

- Updated probability thresholds in Siebel.

- Will continue to monitor performance.

- EDA to identify how to accommodate river cruises. River cruises must always be classified as SVAL.

Erick & Christian

MyCruise Recommender (ForYou API)

- In Progress:

- Team has been in QA mode the last 2 weeks

- API Validation & Testing includes load testing and validation of endpoints to ensure recommendations and data refreshes are accurate.

- Cristian and Erick conducted independent tests across various components of the endpoint to ensure comprehensive QA coverage.

Erick & Christian

MyCruise Recommender (ForYou API)

Concerns:

- The implementation of Databricks Endpoint API is not stable

- It looks like databricks once again capped our workspace RPS Which means this is a direct blocker for us going live with recommendations next week

- We have two options - (A) we raise all hell with databricks (B) we ask Digital to switch the endpoint configuration to oauth - which last I asked they didn't want to do since it was a headache

Erick

Medallia GenAI Reporting

- In Progress:

- Scraped all deck plans from Royal Caribbeans website.

- Used cv2 to identify all cabin coordinates on deck plans.

- Building a 3D render of every cabin on a ship to allow visualization of key Medallia features (heatmap request from Laly).

Lamis and Atefeh

RCI RMA Pricing Automation

Elasticity Model is close to implementation with planned release next week. The team is successfully making price changes, but the magnitude of the changes is unexpected due to a mismatching levels of granularity (volume forecast model is in bookings per catclass, where track is pax per catclass occupancy. Have a solution from the business and should be in prod next week.

Aagam

RCI RMA Pricing Automation

RCI PRE Logic testing, has been more challenging than original estimates. After brainstorming session on Thursday we believe we have a path forward.

Michelle

RCI RMA Pricing Automation

GTY Lead was presented to the business during the cross-branded alignment meetings including current state and proposed path forwards. Nick is aligned on the added benefit of berthing and replenishment but notes there are potential risks that need business rules considerations, like safety zones.

Michelle

CEL RMA Pricing Automation

GTY Lead was presented to the business during the cross-branded alignment meetings including current state and proposed path forwards.

Lekha

CEL RMA Pricing Automation

Lekha is working through backtesting framework still. She has an approach that is close to working but needs to debug error metrics, and make the code generalizable. This should be ready to go next week. Once debugging is completed the backtesting framework will be used to test inclusions of RCI features.

Bernard

CEL RMA Pricing Automation

Anastasia and Jonathan are revisiting the SPI scoring model. They find it difficult to use and interpret because all SPI scores are essentially the same (a score of 1.0). This is caused by a number of reasons.

*We are normalizing for many features.

*Bernard purposely introduced considerable target leakage for normalization purposes.

* This combination has caused the model to "memorize" all of the data and create perfect predictions rather than generalized normalization. Bernard is going to work on a better solution here.

Ignacio & Cihan

PCP Pricing Automation:

Continuing to work with the digital teams to replicate data to hybris. They have stated test and stage are corrected and prod is ready to deploy as well once testing is completed in test and stage. Work continues to be done on shoreX eda where there have been difficulties caused by asynchronous data in Oracle and UC. We are having to use ADF copy/data protocols to get accurate data. Beverage package automation is also in flight. Ignacio met with Ivaylo and Alex Correa to discuss initial work for CEL.

Kevin & Kartik

Loyalty:

Kartik is actively working on matched pair design for choice benefits, while continuing to monitor the spend to save pilot. I am reviewing the power analysis for choice benefit to ensure the sample sizes provided are accurate, and preparing a power analysis for the co-brand card pilot. I am also meeting with Ricky to discuss the missing OBR data today, as I believe there is a risk they will not hit there deadlines if the data is not already in UAT with the business.

(Alejandro)

PROPEL: Uplift Model 2.0:

Calculated confidence intervals and uplift by offer category.

Dynamic Test/Control:

Performed power analysis on a new measurement methodology in scenarios involving changes in control group definition.

Developed an offer prioritization method tailored to business needs.
