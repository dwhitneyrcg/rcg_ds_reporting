**Kevin**

RCI Revenue management:

Created SPI Factor Model planned design based on many point in time models and digital twin concepts. Socialized with Nick and Anastasia for feedback and alignment.

High-Level Approach:

(1) Forecast Ending SPI, based on sailing’s current position​

(2) At a point in time, evaluate best action:​ Using SHAP and Feature Importance Identify Key Drivers of Sailing Performance​ and Identify all levers available​

(3) Optimize sailing management by targeting highest leverage points, giving a “best configuration” ​

(4) Create an interface that allows users to manipulate forecasted sailing SPI score by tweaking levers

​Immediate Goals on Optimizing Sailing Management Factors:

Manipulate highest leverage points to create revenue optimal “Best” Configuration​

Limit for uncertainty using backtesting and confidence intervals​

This is likely too computationally difficult to scale with traditional solvers. Solve through heuristic approaches like greedy search.

Forecasting SPI:

(1) Distinct Point In Time Models​

Many models trained to understand specific drivers and interactions given the sailing and season and time to sail. ​

Feature Importance and relationships will vary per sailing​

Avoid Normalization or Calibration​

The goal is to identify the best course of action for each sailing, not grade sailings for high or low performance​

(2) Backtest/Validate Model Output​

Build an intuition for model metrics/usability. ​

Model should only be used for sailing management where it can be trusted​

Identify appropriate boundary conditions and confidence level. If a lever can increase SPI by 0.1 with an expected error of +- 0.01, we should choose that over an increase of 0.2 with a +- of 0.3.​​​

**Ben & Camila**

IBP - Supply Chain
Completed/Delivered

SSC Order Creation: Revised code to ensure no missing Delivery Date records through Q2 2026; validated by AI and Supply Chain; delivered to SSC.

RCI/CEL Aggregate Bid Data: Stabilized and optimized the pipeline that reads 230+ Excel files to build the unified Power BI table. Addressed error caused by increased file count by coordinating SharePoint clean-up with Supply Chain and enhancing code. Runtime reduced from 2h45m to 45m (~70% faster); pipeline now running without errors.

RCI/CEL Order Creation: Added columns required for Yan’s “Actual Quantity” calculation.

Uniforms: Completed v1 with crew columns; validating compatibility with backtested table creation code.

Ben & Camila

IBP - Supply Chain

In Progress

Uniforms: Building a prds-modified version with the new uniforms table (cleaner, lower-code). Investigating prolonged checkpoint since Wednesday; creating a simplified table (prds-modified without crew columns) to isolate the bottleneck.

Private Destinations: Planning to begin Labadee demand work to establish a repeatable automation approach for new private islands (ahead of Mexico Perfect Day).

Risks/Issues and Mitigation

Uniforms pipeline checkpoint duration is unusually long; mitigation in progress via simplified table build and isolation of crew-column impact.

Requests/Decisions

Request approval to initiate the Private Destinations (Labadee) demand automation workstream following the new-ship automation playbook.

Ben

CLTV
Completed/Delivered

Integrated Erick’s GenAI topic classification and sentiment on Medallia comments into the CLV dataset; ~25% of CLV records are now enriched.

EDA on Medallia-derived features vs. VALUE_INDEX_CABIN.

Uplift analysis by normalized cabin category z-scores.

Key Findings

Effect sizes are very small overall. Where positive, promoters’ normalized cabin value is only marginally higher than detractors’; where negative (notably in CASINO and some NTC rows), detractors’ value is somewhat higher, still small in absolute terms.

The “top” positive differences are not statistically reliable (p-values do not rule out chance).

Sentiment and normalized cabin value are nearly independent within topics and experience segments (r ≈ 0).

Line-plot EDA also shows no meaningful relationship between sentiment and value-for-cabin.

Ben

Customer Lifetime Value

In Progress / Next

Continue combining Medallia-enriched comments with prior Likelihood-to-Recommend work.

Build a model to predict value index (normalized for cabin class) to test for any predictive signal. Corey is eager to review results.

Carlos

E-Commerce Customer Targeting
Completed/Delivered

Restored access to rcimkt.ciu_email_sent and rcimkt.ciu_email_response. Aligned with Kiran and DBA team on usage; best practices confirmed.

Carlos

E-Commerce Customer Targeting

In Progress / Next

Identify and stand up a new Siebel data source after the previous feed stopped updating.

Add exception handling to the ETL.

Add dependency plots for hybrid/ensemble models (PHML, uplift) to the dashboard.

Risks/Issues

Siebel source outage; work underway to locate and integrate an alternative data source.

Cihan

PCP Pricing Automation (Onboard Revenue)
Completed/Delivered: Finalized EDA and presented findings for Perfect Day Waterpark to Gang.

Key Findings and Recommended Actions:

Cabin class: For I and O cabins, waterpark prices are lower than last year; recommend decreasing prices for these cabins.

Meta-product: High demand for 7-night cruises departing from outside Florida; recommend price increases for these sailings.

Day type: Higher demand on weekends; adjust pricing to differentiate weekday vs. weekend demand.

Cihan

PCP Pricing Automation (Onboard Revenue)

In Progress

Elasticity model for Perfect Day Waterpark: Feature engineering and data preparation underway.

Next Steps

Build and validate the elasticity model.

Cihan

Digital App 
In Progress

Deploying the classifier model to production.

Next Steps

Meet with Jaime and build a classifier for Qualtrics surveys.

Cihan

Digital App — Guest Services Chatbot
Completed/Delivered

Resolved the STAR chatbot data issue (root cause: Digital team table change); coordinated with Eswar and team to fix.

Corrected related code in the notebook.

Added STAR to the two dashboards currently used by the team.

**Ayon**

**Win-on-Waste**

Provided comprehensive support to all 26 vessels and their culinary teams by clarifying forecast data and adjusting projections for identified edge cases.

Executed multiple hotfixes in the modeling pipeline to address forecast discrepancies, specifically correcting slightly inflated forecast numbers on several ships.

Collaborated closely with the product team and chefs to explain the PAR PULL methodology and incorporate PAR and NEED numbers into the forecasting process, ensuring improved accuracy and alignment with operational requirements.

**Doug**

**CEL**** Revenue Management**** | Inventory: Upgrade Re-berthing Log**

Celebrity Re-Berthing Logging Update

Status: Complete as of September 2, 2025

Deliverables:

Updated logging process to reduce FIT GTY limits after successful cabin allocations

Adjusted Sunday schedule to:

Remove FIT berthing

Re-enable re-berthing trigger

Change run time from 2:00 PM to 9:30 PM

Added code to subtract successful berthings from virtual category limits

Testing: Successfully tested in both development and QA environments

CEL | Effects of Automation Analysis

FIT berthing analysis. Growth of automation effects over time. Shared with the brand.

**Michelle**

**CEL Revenue Management | ****GTY-Lead 3.0 | CATGAP**

Explore new features (WTS 50+, LAF, granular bins)

Feature Exploration and Model Enhancements

Status: Complete as of September 4, 2025

Deliverables:

Completed feature exploration

Next steps identified: explore model adjustments and DART approach

LAF feature found to be insignificant; category type yields better results

WTS bins refined to 5-week groupings for improved business alignment

Models now trained on all weeks of data (no longer filtered to 12–50 weeks)

Enhanced data coverage enables recommendations for far-out bookings

Potential Issues: None

**LAMIS**

RCI Revenue Management | Elasticity Model 4.0 Upgrade and Code Refactoring (Sept)

Validate the wts_agg_v4 data used in the model - Investigate the big spikes in the price column

Visual

Investigation into Price Spikes in Elasticity Model Data

Status: Task closed pending further upstream data sources

Findings:

Initial investigation traced price spikes to the price_01_amt field in the pricing_daily_snapshot table

Sample cases show unexplained spikes in actual price data (avg_vps_laf_plus_nccf_apd)

These spikes are not recommended by the Elasticity Model or Track Optimization

Business team confirmed the spikes are not valid or expected

Analysis included reviewing wts_agg_v4 and raw vps_pricing_flat data

Next Steps: Further analysis required once additional upstream data is available

**LAMIS**

RCI Revenue Management | Elasticity-based Track Optimization

Optimization Testing – Infeasible Solutions Due to Capacity Limits

Issue Identified:

Some sailings yielded infeasible optimization results due to very low FIT capacity limits

In certain cases, over 70% of cabins were marked as ‘busied’, which were excluded from capacity estimation, leading to unrealistic constraints

Resolution:

After discussion with Chris, agreed to exclude sailings where the ‘busy’ status exceeds 50%

This adjustment resolved infeasibility and improved optimization accuracy

Next Steps:

Continue exploring additional edge cases as optimization is tested on a broader set of sailings

**Lekha**

CEL Revenue Management | Backtesting Elasticity Model | Finalized Testing

Backtesting Report: Prediction Quality Assessment and Visualization Features

Created prediction quality columns to evaluate if the Elasticity model is overpredicting, underpredicting, or performing within acceptable ranges.

Developed visualizations for both train and test datasets to identify systematic over- or underprediction in specific meta subcategories across booking window bins (near, mid, far).

Added filter widgets to enable filtering by calendar week (WOY) and sailing level. Utilized heatmaps and tables for detailed analysis and easy interpretation.

Jesse

SSC Revenue Management

**SSC | Variable PRE algorithms**

I am re-factoring the PRE to utilize SQL-generated input tables. This new, re-factored PRE will incorporate greater flexibility to interchange the types of track-based algorithms that PRE relies on.

SSC | PRE | Rec Optimization SEPT

I am now resuming flexible variances (number of weeks) as part of re-factoring PRE code to utilize SQL-generated input tables (feature stores).

8/26/2025 - SSC Unbundeling Meeting

Data Science and Data Engineering met to discuss the unbundling farecodes. Takeaways were as follows:

Mapping unbundelled farecodes to legacy farecodes

updated price point history from ssc_price table

improving PRE validation performance

**Data Science continues to advance on unbundling. Rollout date is still uncertain, but expected for 9/9/2025**

**Aagam**

**CEL Revenue Management ****| MTRB Updates**

This week I created the process to automatically update the weekly and quarterly tables for MTRB. Which ensures that the process are logged every week and not overwritten.

Blocker:

Need the business to send across the correct logic to identify the newest deployments, will send the process into prod after this

**Aagam**

**RCI Revenue Management: ****PRE Logic Testing – SEP**

This week I focused on updating the track tables so that I only consider the FIT track and also consider all occupancies for both RCI and CEL.

**Atefeh**

RCI Revenue Management | PRE Model Production Pipeline (SEP

The new VPS dataset, including Neighborhood CatClass, was added to the current workflow where the previous VPS dataset was created. As of today, 9/4/2025, the run in QA was successful, and it is ready for production.

QA Pipeline Testing and Fixes

Issues Identified & Resolved:

File Path Errors:

The cluster’s working directory differed from expected paths

Resolved by switching all file references to absolute paths

Unity Catalog Write Error:

Columns "alphas" and "betas" contained NULL values

These were converted to NullType in Spark, which Unity Catalog cannot handle

Issue was addressed to ensure compatibility

Outcome:

Pipeline errors were fixed, enabling successful testing in the QA environment

**Atefeh**

RCI Revenue Management | Elasticity-Based Price Adjustment Formula

This task focused on revising the price adjustment equation to align directly with the definition of price elasticity of demand, which is based on the ratio of the percentage change in demand to the percentage change in price.  We want to compare the recs between this new logic and the current logic applied in the code.

I have revised the price equation so that it is now based on the principle of percentage change in demand over percentage change in price. This leads to the following derivation of p_need:

p_need = df[NUMERIC_FEATURES[0]] - (df[NUMERIC_FEATURES[0]] * (df['TRACK'] - (df['TRACK_WEIGHTED_Y_PRED'] * df['OCCUPANCY_PAX']))) / (df['ELASTICITY_SHRUNK'] * df['TRACK'])

The formula has been validated through Excel testing and compared with existing model outputs.

**Ignacio**

**PCP Pricing Automation**

**CEL | OBR | Cabana A/B Tests 2.0 (Bi-branded) – SEPT**

Add in all other remaining metas into the beverage package PRE elasticity model training (except CHINA)

Deliverables:

OBR team meeting revealed a need to expand PRE coverage to additional meta products

Original metas included:

7N CARIBBEAN, SHORT CARIBBEAN, ALASKA, EUROPE, ASIA, AUST/NZL/SOPAC

Newly requested metas:

MEXICO, CANADA, BERMUDA, CARIBNE, LONG CARIBBEAN, WESTCOASTSHORT

EDA conducted to assess data sparsity and demand trends across booking windows, sailing nights, and price-demand relationships

Resulted in groupings for elasticity model training:

[7N CARIBBEAN, MEXICO]

SHORT CARIBBEAN

[ALASKA, CANADA]

[BERMUDA, CARIBNE, LONG CARIBBEAN]

WESTCOASTSHORT

EUROPE

ASIA

AUST/NZL/SOPAC

Delays: Awaiting pull request approval

Potential Issues: None

**Kartik**

Loyalty

Verify Booking numbers with various data sources and investigate the issue

There was a discrepancy on data bookings we were getting on our side compared to business team side

Figured out the discrepancy and found duplicates in their data

**Mert:**

**MIAP**

Troubleshot a bug with DataBricks AI agents caused by a recent DataBricks update that affected the Newbuild Agent.

Started developing a new AI Agent as a tag mapping assistant.

Collaborated with the Icon Chief Engineer and identified an 875 kW power deviation in the HVAC system.

Prepared tag metadata for navigational data OPC UA servers.

**Brendan:**

**MIAP**

Simplified email notification configuration in the DataBricks asset bundle so that QA and PRD asset bundles remain identical; removed alerts for jobs in QA.

Worked with Mehdi to integrate the model Pickle file into a new feature branch alongside the stability agent code to support his model integration into the agent.

Attended Databricks Advanced MLOps training.

Re-enabled the Service Power job in production after confirming that changes to the dependent job (Power Plant) resolved the bug.

Investigated the root cause of compute spikes in MIAP QA and Dev environments and remediated the issue with help from Utkarsh, Jose, and Shazia on the Platform team.

Collaborated with the MIAP Data Science Analyst to investigate failures when loading base models using MLflow for HVAC.

Worked with the MIAP Data Scientist to review the Revite regression model; demonstrated how code could be added to a tool and tested it in the Databricks Playground.

Deleted historical checkpoint files from the dev environment, saving approximately 34 TB of storage, based on recommendations from Shazia and Jose on the Platform team.

Created an anomaly detection job in Databricks to alert the MIAP team of spikes in Databricks costs; also improved the MIAP Cost Monitoring Dashboard to include daily spend by workspace over time.

**Will:**

**MIAP**

Worked on data issues affecting power plant modeling on LNG ships. Completed development on GTG models and started developing STG models.

**Mahshad:**

**MIAP**

Claimed savings of 350 kW on WN AHU power for three months, an issue detected from the beginning and followed up with the ship to resolve. Also found sensor anomalies on WN TCV valves; awaiting HVAC engineering team approval to contact the ship.

Currently working on detecting anomalies in ventilation and incorporating engine room temperature data into the analysis.

Worked on anomaly detection data issues.

Monitoring EG for possible anomalies on AHU.

Completed thruster models for nearly all ships.

Added plots for OFB to test in the GMP App.

**Mehdi:**

**MIAP**

Completed the regression model by splitting sparse data into two separate models with a classifier to select between them.

Integrated and tested the model as a tool within the Databricks AI agent, successfully enabling weight predictions.

Extracted necessary features from user prompts and is working on transforming them for model compatibility.

Registered the model in UC and managed model storage and loading with MLflow.

Currently finalizing the tool and improving code and results.

**Arya:**

**MIAP**

Developed a new classifier to determine if an incident aboard a ship occurred between the posting of a work order and its resolution (correlating AMOS and LSA/LOPPS data).

Discovered an issue with MLflow search which limits results to a maximum of 10,000 models; implemented pagination to resolve this and is working on integrating it into analytics.

Added EX to HVAC and chiller systems.

Reworking the addition of ST to HVAC, service, and hotel systems.

**Erick & Parimala**

Contact Center: Lead Scoring CTI:

Two bugs were identified and fixed on August 28th and in the following 7 days RCI CTI conversion appears to finally be matching conversion rates observed in prior years. Team will continue to monitor the CTI model and is experimenting with using Call Transcripts as part of the lead scoring process.

**Erick**

Axiom - Medallia Reporting Automation (SEAT)

The preliminary report went live on September 2nd. Prior to this the team worked on delivery of a number of nuanced breakouts that were included in both the final and preliminary reports. The granular breakouts now contains aggregations of Nationalities, Generations, Load Factor, and number of families that mention each topic.

**Erick**** & Gaurav**

Axiom - Medallia NPS Drivers Model (SEAT)

Gaurav is leading the effort in adapting the feature importances coming out of the Medallia Drivers model to create thresholds that can be used for alerting purposes. The idea is to inform the business about the key thresholds for each metric afterwhich there is an impact on NPS.

**Erick**

Axiom - Medallia Reporting Automation (SEAT):

Pending Work

Met with Evan to collect feedback on custom CEL report.

Met with Gangs team (Alessio & Melissa) to discuss next steps after having delivered prelim report.

- Department specific reports where specific departments get a custom email based on predefined topic/subtopic combinations.

- Automation of Guest Logs data and creating initial email.

Met with Althea Palmer on new potential use case for Email automation concerning incoming product questions from guests.

**Erick & Christian**

PCP Product Recommendations

Recieved and approved a request from Digital engineering to increase the rate at which the MyCruise Recommender API will get hit (caching layer will hit API directly every 6 hours).

Eswar

Revenue Management (RCI)

Feature Store hand-off to Data Engineering:

Identified feature store tables that are being actively used by RMA production jobs.

SPI & MTRB: Undergoing knowledge transfer sessions with Bernard

Operations:

PR reviews and monitoring CI/CD deployment pipelines

Updating mlflow version to 2.19.0 in pre elasticity model training.

Upgrading PRE_main_notebook to DBR 15.4 from 13 by refactoring the code accordingly

Updating DBR, compute configurations in ADF workflow "ple_pre_5pm_E2E"

Modified fs_inv_avail_features_generate, fs_inv_avail_features_update and OBR_drinkpackage_elasticity_train workflows and productionized it.

Productionized ssc_featurestore_generator workflow which refreshes tables which will be used in silverSeas processes.

Resolving copy data issues with pl_sailing_companion pipeline in ADF.

**Glen-Erik and Alejandro**

PROPEL:

Capability to only send awareness offers, this will allow to continue running the program even in cases were there is no wallet to invest in promotions

Dynamic test-control moved to production, this enhances the measurements capabilities and ability to have 100% coverage of offers during a sailing.

Support to Ops, keeping offers flowing for CEL Fleet

Adjustments to offer decks configurations

Improvement to data shuffling and memory usage in clusters

**Javier**

RCI Revenue Management: Automated Code Review tool

RMA Implementation update: compliance fixing code violations now 30%, up from ~10% in June. Good progress but certain developers still fully ignoring even critical violations, needs follow up.

Added GenAI support for creating checks:

Modularized prompt architecture by splitting the core prompt (prompts/prompt.md) from customizable user rules (prchecks/rules.md).

Expanded coverage to Databricks YAML, ADF JSON, Python (.py and flattened .ipynb), and repo-hygiene checks.

Activated Azure, OpenAI fallback while clarifying **403** errors.

Merged GenAI functionality with legacy regex-based deterministic rules.

Compliance tracking:

Stabilized PR comments with hidden HTML markers, avoided auto-resolving when model output was empty, standardized rule IDs/messages.
