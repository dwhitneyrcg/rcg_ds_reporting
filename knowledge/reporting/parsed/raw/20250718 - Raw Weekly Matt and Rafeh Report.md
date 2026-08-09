**Erick Alfaro**

**GenAI SEAT Reporting**

******** ****Guest Logs GenAI Reporting****

Piloting Cursor during development work on this project.

Completed 30 days worth of GenAI chunking/preprocessing of data.

Presented findings to Steering group.

Next step includes comprehesive review of abbreviations and acronyms found in guest logs to improve LLM context awareness.

Completed feasibility analysis and finalized acronym mappings

Cleaned guest log data and transitioned to single-line outputs per log (per business request)

Next: Build GenAI summarization + metadata tagging for each log entry

Goal: One-line-per-log format with problem/resolution columns

**Erick + PCP**

**PCP**** Product Recommendations**

****MyCruise Recommender****

- Top priority: Recent code change was identified as the root cause of Recommendations showing incorrectly during testing. A patch has been deployed and the team is working on an automated QA pipeline that would only allow automatic deployments if unit tests on the test Endpoint pass.

- Active: Segmentation/clustering for recommendation engine, recommender ETL optimization, research on Databricks Serving, and AI categories framework.

- Multiple completed tasks: research, ETL/feature enhancements, environment setup, and retraining.

- Next: Expand clustering, retrain models, finalize API category logic, and enhance unit testing.

Designed improved segmentation model with new features: seasonality, ticket price, conversion rates, shopping patterns, sail-date proximity

Integrated customer interactions into ETL; reduced processing time from 50 min to <5 min

Deployed modular hourly/daily ETL jobs

Note: Recommender will receive 100% of traffic at launch — no ability to downsample audience

**Erick Alfaro**

**GenAI SEAT Reporting**

**### Medallia GenAI Reporting**

Modified the logic for how we exclude topics in the email

Added multiple new users to email distribution

Integrated Oasis ship data; presented work to Steering and Product teams (positive feedback)

In progress:

- Developing and validating modular email sorting logic for Royal and Celebrity brands

- Building out Celebrity fleet-level summary reporting;

- Enhanced comparative analytics, deeper data insights at shipboard/division/state/nationality levels, early alerting system, and report formatting improvements.

Erick Alfaro

GenAI SEAT Reporting

**Medallia Driver Analysis**

Working on a thresholds model to identify meaningful threshold changes in "other" Medallia fields such as the Food metric. Presented initial findings to stakeholder regarding Thresholds project which attempts to identify specific *thresholds* by Driver. The idea being that after a certain Threshold we can expect notable impact on NPS.** **

- Tested EBM and Pyearth models for interpretability

Finalized modeling logic using residuals and weighted average NPS scores

Erick Alfaro + Parimala

Contact Center - Lead Prioritization

**CTI**

- Lead scoring optimizations for the contact center continue due to conversions still not matching prior year conversions.

Implemented business rules to classify Galapagos leads appropriately

River Cruise leads need special care and will need further collaboration with Siebel teams

Fixed scoring duplication issue; documented logic

In progress: Table permissions, threshold tuning, alerting logic, and inference updates

Erick Alfaro + Gaurav

**Digital App Analysis**

- Held brainstorming session with stakeholder on next steps. Stakeholder is primarily interested in better explainability around which app interactions/behaviors can be pinpointed as the drivers of incremental spend.

Completed modeling of precruise revenue as a function of booking behavior and app engagement. Delivered feature definitions to stakeholders

Erick

Other SEAT **Exploratory Work**

Brainstormed GenAI use cases for Homeport Modernization

Introduced SSC Contact Center to Emerging topics logic delivered for Alper

Pending sentiment analysis implementation for SSC

Met with International (Josh Barrocas, Anthony Calderon) to brainstorm GenAI opportunities

**Erick Alfaro**

**GenAI SEAT Reporting**

**Qualtrics**

- Backend tool for open-ended response summarization operational; self-service web app in preliminary scoping.

Conducted stakeholder scoping and architecture review.

Next: Implement POC using Cursor local development and CI/CD to Databricks Apps

**Erick Alfaro**

**Medallia App**

**- Several filter additions, API/data enhancements, and infrastructure tasks have been backlogged following ****wide ranging**** feedback from various app users.**

Provided permissions to Product teams

Kevin + Kartik

Loyalty:

Presented preliminary findings on Spend to Save Pilot to EC. Results are still being shown using total sailing APD, which is muddying findings considerably. Several analyses are pending and accurate measurement will continue to be skeptical until guest level data is available. EC was made aware of current limitations, but based on current findings showing little to no effect, provided some insights. Jason in particular is focused on testing rewarding spend by providing exclusivity and access rather than a cash back reward.

Kevin

RCI Revenue Management - Elasticities

Had a successful alignment meeting with both brands highlighting the current elasticity models and recent improvements being made. Next steps will be focused heavily on validation and backtesting to determine model performance in both short term and far out forecasting horizons.

Aagam has run into a few challenges on the pre-logic testing that require further investigation, causing us to re-sequence the meetings with the business. We will discuss gty-lead and how it impacts inventory decisions next week, and pre-logic the following week. Team is investigating the concerns Aagam raised as I think they may be related to the feedback we received from Anastasia with uncapped changes to prices increasing with the latest elasticity model implementation. Projections causing negative values in look back period:

(1) Negative Elasticity predictions, or very high elasticity predictions

(2) Track considering occpcy i.e. PAX level, where volume forecasts are at the booking level. Aagam has assumed double occpcy, but this scenario coupled with high elasticities can lead to abnormal pricing

(3) I will be reviewing these and doing further investigation into the PRE code for both brands to confirm if it is the way Aagam is building the test scenario notebook or if they persist in the PRE code.

Kevin

Had a successful alignment meeting with both brands highlighting the current elasticity models and recent improvements being made. Next steps will be focused heavily on validation and backtesting to determine model performance in both short term and far out forecasting horizons.

Aagam has run into a few challenges on the pre-logic testing that require further investigation, causing us to re-sequence the meetings with the business. We will discuss gty-lead and how it impacts inventory decisions next week, and pre-logic the following week. Team is investigating the concerns Aagam raised as I think they may be related to the feedback we received from Anastasia with uncapped changes to prices increasing with the latest elasticity model implementation. Projections causing negative values in look back period:

(1) Negative Elasticity predictions, or very high elasticity predictions

(2) Track considering occpcy i.e. PAX level, where volume forecasts are at the booking level. Aagam has assumed double occpcy, but this scenario coupled with high elasticities can lead to abnormal pricing

(3) I will be reviewing these and doing further investigation into the PRE code for both brands to confirm if it is the way Aagam is building the test scenario notebook or if they persist in the PRE code.

Michelle

CEL Revenue Management

Michelle will also be focusing on backtesting and validation for GTY-Lead 3.0 at the request of Anastasia. This approach is particularly important given the optimization is attaching the same value to far out forecasts.

Ignacio + Cihan

PCP Pricing Automation

Significant progress on CAR submission, but further alignment necessary with Digital/E-Commerce teams on the PCP Promotions Builder App + Notifications Automation pieces of the CAR.

Ignacio has made considerable progress this week on Beverage packages moving refreshment to prod and completing development on 18+ International beverage. International is awaiting Jorge's review tomorrow. Cihan has also had a big week adding many new shoreX products to the feature stores and conducting EDA in coordination with the business. We are still awaiting confirmation that changes to the hybris promotion ingestion flow are complete. Test and Stage were scheduled for testing on Wednesday, but Digital has not responded to my email for a confirmation on this.

Ben + Camila

GSCBP / IBP (Global Supply Chain Business Planning)

a. Completed

• Fixed aggregation error in the CocoCay consumption model

– Previously summed consumption; updated logic to select first value.

– Validated weekly consumption matches back-tested tables.

– Noted remaining discrepancy in monthly consumption; to investigate in guardrails notebook.

• Updated Inventory Depletion dataset

– Included POs cut with future orders assigned to warehouse rather than ship.

• Enhanced HF&B model with new ship logic

– Added STAR OF THE SEAS and XCEL.

– Observed no predictions for new ships post-update; issue under investigation.

• Began expedition-items work for SilverSea (Yan’s request)

– Completed Parka example.

– Next: integrate proper consumption table and match Excel results; implement broad-table checkpointing for speed.

• Delivered Uniforms modified-product-names v2

– Pipeline ran successfully; will compare performance across four naming strategies.

• Volatility reports enhancements (delivered 7/14)

– Switched to PERCENT_CHANGE for threshold alerts.

– Adopted hybrid reporting via email+SharePoint links.

– Updated code to implement changes.

Ben + Camila

GSCBP / IBP (Global Supply Chain Business Planning)

b. In Progress / Pending

• Develop hybrid threshold-alert solution combining PERCENT_CHANGE and absolute difference.

• Uniforms Model V3

– Prepare overview presentation.

– Build new ETL for higher-level product-name stripping to evaluate model performance.

• Other pending deliverables

– SilverSea expedition-item forecast for bottles.

– CocoCay dashboard.

Carlos

E-COMMERCE Customer Targeting

a. Completed

• Replaced SHAP dependency plots with custom plots in production dashboard (fixed for non-continuous numeric data).

• Deployed interactive-plot backend code to production.

• Released and tested new feature-selection algorithm in production.

• Resolved dashboard bug caused by Oracle table data-type change.

• Conducted EDA on scoring data to support Bao’s Databricks dashboard:

– Optimized top-destinations query (now returns full top-5 ranking).

– Simplified population filters and condensed marketability filters.

– Halved query count; leveraged built-in filters to split views by brand in a single query.

• Provided ongoing “genie” chatbot feedback to improve responses.

Carlos

E-COMMERCE Customer Targeting

b. Next Steps

• Replicate dashboard filters on the Consumer Demographics tab for UI consistency.

• Evaluate adding additional models and optimize epsilon-data queries and layouts.

• Meet with Carlos to refine queries and integrate them into his pipeline for improved speed.

Mirielle

CONTACT CENTER

A. Lead Prioritization (BK2CX):

Data Validation: Validate data quality in the new prd_silver.dpc_pss2.sbofrd feed versus existing sbcxed table with ~85% with sbcxed; 4 new columns; 3 sbcxed columns missing.

Added Booking ID: Initial BKTOCX release omitted Booking_ID in Cruise Reference, but as of July 7, 2025, new BKTOCX outputs include Booking_ID. Legacy files loaded into Siebel prior to update lack Booking_ID; require back-fill or reprocessing.

Duplicate Leads: Duplicate leads due to SBCXED push without disabling legacy sources. Siebel must ingest all SBCXED lead types:

– Royal (6): BKTOCX, OFTOCX_CC, OFTOCX_WEB, CX, PGR_DIRECT_GROUPS, PGR_DIRECT_WEB

– Celebrity (8): BKTOCX, CX_ONBOARD, CX, BKTOCX_ONBOARD, OFTOCX_WEB, OFTOCX_CC, PGR_DIRECT_WEB, PGR_DIRECT_GROUPS

Mirielle

CONTACT CENTER

A. Lead Prioritization (BK2CX):

Ongoing Tasks (Iterative)

• Monitor lead counts via max(sequence_id).

• Test pipeline in staging environment.

• Track nightly file drops in SFTP.

• Cross-check min/max sequence_id per lead type and brand for Siebel vs. Data Science consistency.

• Timeline: Process initiated Monday; ongoing through Friday.

Mirielle

CONTACT CENTER

B. Workforce Planning POC

Work Completed – WPS Staffing Model Development

• EDA on daily call volume (RES line of business).

• EDA on daily average handle time forecasts (RES).

• Imported international staffing-model functions.

• Began adapting functions to North America context (ongoing).

• Executed end-to-end model run for RES to validate function orchestration (ongoing).

Mirielle

CONTACT CENTER

B. Workforce Planning POC

Next Steps

• Prepare and deliver project walkthrough for stakeholder review.

• Continue iterative model runs in staging to validate staffing computations.

Cihan

DIGITAL APP Review

GS Chatbot Project

• Resolved dashboard data-refresh issue; restored seamless, up-to-date reporting.

Cihan

Digital APP

Digital Mobile App Review Project

• Developed ai_classify_rcg() LLM function to improve topic classification:

– Enforces correct list output format.

– Restricts responses to predefined labels to minimize hallucination.

– Supports customizable topic descriptions.

– Enables single- and multi-label classification.

Cihan

PCP Pricing & Optimization

Accomplishments

• Held kickoff with stakeholders; gathered initial feedback.

• Performed EDA on waterpark shore-excursions data.

• Prepared findings for next stakeholder meeting.

Cihan

PCP Pricing & Optimization

b. Planned Tasks (Next Week)

• Digital Mobile App Review:

– Finalize stakeholder topics list.

– Classify app reviews into predefined topics.

• PCP Pricing & Optimization:

– Continue EDA based on feedback.

– Refine analysis in preparation for follow-up discussion.

Ben

CUSTOMER LIFETIME VALUE (CLTV)

a. Completed

• Rebuilt indirect-cost allocation in analytics pipeline (per-booking basis).

– Adjusted solo’s value index to 0.92.

– Switched from per-pax to per-booking threshold logic based on cruise experience.

• Validated indirect-cost spread to pax level and re-aggregated to match corporate planning totals.

• Produced Excel summary of value indices by brand/cohort; compared old vs. new methodologies; conducted per-pax checks.

• Diagnosed lost passengers in CLV pipeline due to inner/left join logic change.

• Identified and removed true duplicate pax in CLV base_with_index tables.

• Detected anomalous total-value calculations for incomplete 2025 data; underscored need for accurate unique-booking aggregation.

Ben

CUSTOMER LIFETIME VALUE (CLTV)

b. In Progress

• Assist Corporate Strategy in shifting to per-booking rates from 2019, 2023, 2024 for cost-spreading.

• Explore integration of cruise experience into cost calculations.

• Support Gaby in querying agency counts and sharing value indices to aid Trade.

**Mert**

**MIAP**

Collected fleetwide ship stability booklets from SharePoint and manually organized everything into a Volume storage to be used for the Newbuild Stability Project. Parsed all PDF files and created a vector search database for AI agents to access documents.

Created a vector search database for the enriched weight estimates table.

Developed a collection of Databricks function tools for AI agent interaction.

Created a Databricks AI agent using LangChain/LangGraph and MLflow.

Implemented a UI and agent management class on the MIAP WebApp for the Newbuild Stability Chatbot.

Tested AI agent performance.

Created detailed project tracking and milestone updates for the decarb team as requested.

Investigated the usage of Lakebase for the Safety Culture database.

**Will**

**MIAP**

Implemented individual power plant model performance plots and model error plots.

Working on completing the monthly performance plot.

Collaborated with Mert and Brendan to fix issues loading recently created models in the REST API.

Assisted IT in deploying the new GMO Page for Data Quality Tracking.

**Arya**

**MIAP**

Joined Royal Caribbean.

Started exploratory data analysis (EDA) on the sea events dataset, specifically focusing on fire events.

Met with Michael from Maritime Safety and learned about relevant processes.

Attended three team lunches.

Leveraging NLP to annotate the dataset as either customer-origin fires or crew-member-origin fires.

Received one indirect message from Erick regarding serverless usage.

**Brendan**

**MIAP**

Wrote 500+ lines of code building out the Total Propulsion Power Prediction library in support of the Fuel Forecast project; completed the first draft of the library.

Performed a code review of the Total Propulsion Power Prediction library with Mert; identified opportunities for improved future-proofing, caching of models, and vectorized operations.

Troubleshot an environmental bug related to getting predictions from pickled models.

Supported MIAP data scientists with pipeline failures, troubleshooting API issues, and bug fixes.

Held a session with a Naval Architect to review the ALS Utilization/Savings model; identified key areas for improvement in MIAP ALS visualizations in the GMO app.

Attended a session with the ML Ops team to discuss code version control strategy and best practices.

**Ram**

**MIAP**

**July 11th**

Worked on Sea Events and developed a script to migrate the Bronze ETL from Silver Seas to the DE workspace.

Focused on the Eniram final table loading process and archiving, which took approximately 1 hour and 10 minutes to complete.

**July 14th**

Connected with the team to understand the MIAP ETL process and identified potential areas causing delays.

Tested Eniram and observed changes in ship tag lengths; worked on code development to accommodate the new Eniram updates.

**July 15th**

Based on inputs such as schema and table names, completed code development for Sea Events.

Tested and made code adjustments for the Eniram API, successfully reducing processing time from 1 hour 10 minutes to 55 minutes.

**July 16th**

Analyzed vessels that were failing to provide data, reached out to the Eniram team, and conducted end-to-end testing.

Sent an email to Eniram support with details and revised the approach for the final table loader.

Analyzed MIAP ETL code.

**July 17th**

Due to updates on the Eniram side regarding tag additions, modified variables and tested with different values, noting the results.

Developed a new approach for the final table loader using a ForEach loop, reducing processing time from 55 minutes to approximately 30 minutes for all 33 vessels.

Analyzed MIAP ETL and Silver Analytics code for further improvements.

**Next Week**

Will continue testing Eniram and aim to move the code to production.

Will finish code for Historical Eniram.

Will continue analyzing MIAP ETL.

**Mahshad**

**MIAP**

- Detected anomalies in the SM WHR system and its control valve temperature regulation. The ship’s crew is aware and plans to replace the faulty component soon. The WHR system has been out of service since 2020. Not using this heat recovery network results in higher steam consumption, leading to increased fuel consumption from the boilers both at berth and at sea during low-speed operations. Savings opportunities associated with this system will be assessed during the upcoming six-month monitoring period and are expected to be significant, particularly since the OFBs operate using MGO fuel.

Addressed errors encountered during QA deployment.

Collaborated with a new team member to set up API access, enabling connection to the API and full editing capabilities for all GMO app plots.

Continued developing the ML class by creating all relevant plots for WHR data analysis.

Worked on the ML class involving VFD, Waste Heat Recovery (WHR), and ventilation fan signals; gained domain knowledge and identified potential anomalies.

Identified anomalies in the ventilation fans of ML and SM located in the chiller room and gas turbine rooms: VSDs were either bypassed or forced to run at 100% speed in manual mode. After consulting the engineering team, it was confirmed that ML fans should operate at 100% in hot weather to manage engine room temperatures. Therefore, potential energy savings may be found for SM fans, as SM operates in colder Alaska conditions.

Continuing analysis of ML, CS, and IN systems to identify additional energy-saving opportunities.

Studied marine analytics to better understand ship operations and worked with Valmet to become comfortable with its settings and configurations.

**Reza**

**MIAP**

Updated fleet-wide baselines for the HVAC area.

Investigated the root cause of the anomaly observed in AHU Public 204 on the vessel *Constellation*.

Conducted meetings to review and understand fleet voyage reports, FACTS, and BunkerWebb tables, aiming to develop a new fuel consumption model for ships lacking sensor data.

Completed water-side cooling power calculations for AHUs and integrated the relevant plots into the GMO application for enhanced visualization.

Alejandro

PROPEL

Uplift model recommendations to select the best-performing offers from the past 120 days deployed in dev for propel including auto-retraining, Qini curve analytics and History saving for future analysis.

Spa offers were adjusted to not be sent when having a special occasion so that OBR Team

ShorEX rule based offer was created to target those without a booking the first two days of a cruise.

Targeted offer for high spenders (USD +1k)

My Cruise Recommender workflow to automate data refresh for PCP endpoints

[In progress] Dynamic test and control for propel to ensure 100% coverage of offers (everyone gets an offer)

Aagam

RCI | CEL | PRE Logic Testing

This week, I focused on evaluating different look-back and look-forward windows to determine the track for the PRE. Specifically, I computed the track for the following scenarios:

Average of future track for 3, 4, 5, 6 weeks

Average of look-back window of pax build for 3, 4, 5, 6 weeks

Weighted average for future track for 3, 4, 5 weeks

Weighted average for look-back window for pax build for 3, 4, 5 weeks.

Using each of these track calculations, I applied the new elasticity model to estimate prices and identify the most effective methodology for selecting the track.

Challenges:

The elasticity model is based on booking data, whereas the track is at a PAX level, making direct comparisons challenging.

To address this, I have temporarily considered all bookings as double occupancy

In some cases, the new pricing results in extremely high APDs.

Conversely, there are instances where APDs turn negative.

Additionally, the prices are aggregated at a 5 WTS bin level because the elasticity is observed at this 5-week interval. Consequently, all my calculations are currently based on the 5 WTS bin level. To achieve a more precise understanding, I need to break down these results to a weekly level.

Next Steps:

Additionally add another blended scenario, where we consider look back and look forward period together to calculate the track

Atefeh

RCI Elasticities

- Working on the `price_change_4_0` notebook to apply the new demand prediction model and calculate recommended price changes.

- Calculated the average of requested TRACK values based on current WTS and a dynamic window set by the business.

- Pulled `y_pred_4.0` (demand prediction from the new model) and elasticity values.

- Used the formula for Ridge models:

`p_new = p_current + (1 / elasticity) * (TRACK - y_pred_4.0)` to determine new prices.

- Encountered a blocker: TRACK is at occupancy level, while the model is trained on double occupancy; temporarily adjusted the table accordingly with approval.

- Plan to review the approach used for the CEL brand to ensure consistency across brands.

- Next steps include integrating the recommendations into the `New_Price_Hierarchical` notebook and working toward full production deployment.

Bernard

RCI - SPI-guided FIT track optimization

- Fine-tunned track recommendations through model fine-tunning separately on peak and off-peak booking seasons with hyperparameter tunning on three parameters (learning rate, tree depth, and estimators) simultaneously.

- Generated deltas in track ask between high and low SPI sailings, highlighting need to push more volume to periods enjoying high organic demand and greater pricing responsivity.

- Nick recommends separate models for SPI scoring of winter and summer seasons, which more naturally follows demand patterns rather than segmenting by calendar year.

Bernard

CEL - SPI scoring model finalizations

- Anastasia provided final sign off on CEL SPI scores after a productive 2 months of scrutiny and fine-tunning.

- Enhancements asked for by CEL team will also be used to update RCI scoring methodology

- CEL SPI model to be pushed to production in coming week.

Doug

RCI Revenue management - PRE

Booking data discrepancies in RZBKVD. Detected in berthing results on Sunday and continued coordination on ongoing anomalies thru the week.

RCI PRE upgrades:

1. Volume forecast elasticity output fixes. Rolling window fix (Aagam)

2. PRE output cleanup

3. Pause parameter table output redirected into Unity Catalog

4. Inversion fixes reworked, missing data file resolved, output redirected to Unity Catalog

Michelle

RCI | GTY-LEAD 2.0 | Quads Exploration

Exploration complete. Business reviewing results. Next steps: unifying codebase with 2.0.

Michelle

CEL | GTY-LEAD 3.0 | CATGAP Inter-category Gaps Stage 3 | Feedback Loop

CODE EFFICIENCY Testing PuLP vs scipy minimize for code efficiency.

Sailing Validations - Comparing predictions against past sailing that did not perform well (use model trained up until that point).

Michelle

RCI | GTY-Lead 3.0 | CATGAP - Stage 3

Training and Sailing Data Validations - Verifying that previously created tier mapping and price gaps maintain true. Utilize to retrain model and adjust optimization code accordingly.

Lekha

CEL | PRE | Reporting on the Pricing/Elasticities

After last week’s meeting with Tristan from celebrity team we agreed that adding revenue period columns in the retraining output tables would help join the output table with the revenue table for better revenue metrics analysis.

So, I implemented a proration function to break down cruise nights revenue across months, and added revenue_month, revenue_year, and revenue_quarter columns based on this proration logic.

These revenue columns have now been added to both the final output table and the weekly lag analysis table, enabling more granular joins and improving analysis of model performance with actual revenue data.

CEL | Elasticity Backtesting Framework

Used read_date as the time column to create time-based expanding splits with growing train windows and fixed 30-day test windows separated by 7-day gaps to avoid data leakage.

MLflow models were originally trained on approximately from 2023-01-01  to 2024-02-28, while backtesting is performed on 2023-01-01 to latest read_date  to evaluate model predictions on unseen future periods.

Automatically generated train-test splits where training data expands with each split, and test data covers subsequent unseen periods for realistic forecasting validation.

Loaded the latest MLflow models per meta product code cat_class and made predictions at row level for both train and test sets.

Calculated comprehensive custom error metrics (MAE, RMSE, MAPE, SMAPE, MSLE, Poisson deviance) per sailing level to assess model accuracy and robustness.

EDA with panel plots revealed inconsistencies in predictions vs actuals, indicating potential issues in prediction alignment or feature mismatches requiring refactoring.

Planned next steps include refactoring prediction logic, validating input features, adding detailed logging, and confirming time split correctness to ensure reliable backtesting results.

Lamis

RCI | Elasticity-based Track Optimization – JULY

Tested re-running the track optimization using the upgraded elasticity model - shared initial finding s with Chris - and received a feedback to incorporate the wave flags explicitly and expand the testing on multiple sailings.

I am also working on running a version of track optimization using the elasticity values generated from the model (and not the inverse of the demand model) - Elasticities are directly incorporated in the PRE and worth testing in the track optimization. Should discuss results with Chris tomorrow

Lamis

RCI | PRE Elasticity Upgrades | Production Code – JULY

MLFlow Distributed Logging for each meta cat class model

As of today - I have completed refactoring the model training notebook to train different model experiments - selects the best model based on error specific metrics - log the best model in MLFlow at each meta - cat class in distributed fashion using applyInPandas.

I still need to do the followings:

→ work on saving the logged model objects under a schema in the UC for easier future handling.

→ Finalize the code to be able to call a specific model object (based on meta - cat class) and perform .predict() for scoring.

Ignacio

PCP Pricing Automation

Developed elasticity models for 0812 (including EUROPE, ASIA, AUST metas) using a Poisson Regressor with target encodings, interaction effects, and scaling, similar to the Deluxe package.

Built an optimization routine for 0812, mirroring the Deluxe approach, with price deviation constraints, demand/capacity limits based on historical trends, and revenue-focused objectives; reviewed and approved by the OBR team.

Added CocoCay ShoreX data (waterpark, hideaway beach, royal beach club) to the OBR feature store, performed initial EDA, updated queries, and integrated additional tables (e.g., tour dates, passenger ages) to support elasticity modeling, with handoff to Cihan for further analysis.

Created elasticity model for product code 3224 (focused on EUROPE, ASIA, AUST metas), completing the full PRE pipeline, integrating it into the OBR optimization workflow, debugging, and validating results with the OBR team to ensure alignment with business goals.
