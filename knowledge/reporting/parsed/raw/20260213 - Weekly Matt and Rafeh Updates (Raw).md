Mert
MIAP
Implemented data analytics visuals for alarms and events.
Started tag mapping for Radiance-class ships for Phase IV.
Completed tag mapping of Oasis- and Edge-class diesel engine tags in preparation for future asset-management work.
Met with Newbuild and IT teams and identified a Newbuild Innovation Fund idea for Hero of the Seas: replacing the real-time vendor analytics solution from Meyer Turku (MEMS) with MIAP. If approved, these funds will support development of a shipboard real-time compute engine and ML model serving at the edge, serving as MIAP Phase V.
Interviewed candidates for the Senior ML Engineer role.
Met with the deployment team to discuss deployment optimization opportunities.
Met with the Nacos team to discuss the Silver Muse OPC UA project.
Met with the GMO Electrical team and agreed to move forward with a cabin automation data pilot on Quantum-class ships.

Mahshad
MIAP
Advanced ML-based anomaly and deviation detection for chiller systems, including plotting Coefficient of Performance (COP) under consistent supply-water temperatures and varying loads.
Investigated recent drops in enthalpy and began comparing cooling power across AHUs to identify potential anomalies.
Developed a new tool for deviation analysis and made progress on an additional tool focused on AHU deviation detection.
Resolved a bug in the ORBM library to diagnose data issues occurring in WN.
Addressed several tag-mapping issues and continued monitoring both CS and WN environments.
Participated in a fuel-saving discussion and followed up with an email regarding ML chiller work.
Met with the deployment team to align on upcoming tasks related to PAX guarantee constraints for itinerary selection.
Spent time learning how to build and structure Agents to support future automation and ML workflows.

Reza

MIAP
Continued work on FACTS-based and sensor-based workflows related to the fuel-forecast pipeline (all tests currently in the QA environment).
Added digital-twin sensor comparison workflows and analytics scripts.
Implemented row-wise error-tolerance modifications to the digital-twin platform.
Fixed naming issues across several modules to improve consistency.
Identified bugs in the LNG optimizer and shore-power workflows; scheduled meetings with data scientists to address them.
Optimized workflow performance to improve execution speed and avoid runtime errors.
Resolved a bug related to consolidate/remove sampling on voyage legs.
Met with a data analyst to discuss solutions for overall SFOC models.
Met with a data scientist to review requirements for the HVAC AI Agent.

Arya
MIAP
Added a fix for the incident summary table in the GMO app.
Fixed data issues related to RA common features.
Restructured the chiller notebook for ad-hoc, single-ship runs.
Added delayed sigmoid functions for lower power values in individual MGO equivalent power-plant models.
Fixed AHU and chiller pipelines.
Started building an initial deep-learning framework to predict individual DG power from total power.

Brendan
MIAP
Leveraged new tables from the GMO team to create a single view of hull-coating events, including dry docks and maiden voyages; updated the Fuel Forecast API to use this view.
Explored multiple approaches to resolve “out of disk space” errors in MIAP pipelines using external storage provided by the platform team; issues persist. Followed up with the platform team to request increased disk space on the deployment agent.
Assisted with resetting the MIAP REST API QA branch and created a new Azure DevOps group for MIAP developers with appropriate permissions to perform this operation going forward.

Ram

MIAP
This Week
Added Modbus source-load logic to the existing shipboard code and successfully deployed the changes to Production.
Worked on migrating the Sea Events and VPS ETL jobs, including updating dependencies from Bronze to Silver tables in the Mariner workspace.
Completed the initial proof of concept (PoC) for Honeywell data and loaded the data into the respective tables.
Next Week
Investigate and resolve the Production failure in the MIAP ETL pipeline.
Gather business requirements for Honeywell and update the logic accordingly.

Will

MIAP
Fixed bug with shore power disconnect delay

Fixed bug where shore power is greater than 0 when not available

Fixed bug affecting feasibility of optimization when shore power cap is higher than total MCR

Working on adding new metrics to shore power and adding to Web App

Erick

Project Axiom

*AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.*

### Meta Data Extraction

- **Divisions Meta Data Framework** *(David M.)*: Added auto incremental ID column to production tables. Batch processing code nearly complete and entering testing. New division aspect mapping tables created with model version and execution date columns for traceability.

- **Bullet Points Migration** *(David M.)*: Remains blocked pending Erick's confirmation of new topics. Batch process code is ready to execute once input is received.

### Reporting

- **GSO Safety Email** *(**Danusio** G.)*: New safety email requirements received from Melissa (Global Security). Email will split into Onboard (priority) and Shorex sections using LLM-based two-step classification.

- **Voice of Detractor Fleet Report** *(David M.)*: Weekly Fleet detractor report emails delivered successfully for all 3 brands (sent every Monday). Pending stakeholder follow up on the final distribution list.

- **RBC Recap Email Enhancement** *(Rodrigo B.)*: Improved existing RBC email report to include quantification of negative topic mentions.

- **Guest Strategy Email** *(Rodrigo B.)*: Weekly Guest Strategy Email delivered successfully for Gang Wang & Hotel Operations teams (sent every Sunday). Positive feedback from stakeholder with minor suggestions for improvement provided. Pending stakeholder sign off

Erick

Project Axiom

*AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.*

### Modeling

- **NPS Drivers Model** *(Osvaldo V.)*: Proposed feature clustering using correlation distances to reduce redundancy of Medallia survey features and improve interpretability. Proposed a new model trained on negative-data-only.

- **Drivers ****Streamlit**** SHAP POC** *(Osvaldo V.)*: Merged Royal and Celebrity APIs into a single consolidated endpoint. Front-end integration with Axiom platform planned for Friday workshop.

- **Medallia Keyword Correlation Tool** *(Osvaldo V.)*: New task assigned to develop a generalized tool for filtering Medallia comments by keywords and correlating with KPIs. Using previous weather-sentiment analysis as foundation.

- **Weather API Data** *(**Danusio** G.)*: Automated daily job running at 6:00 AM. Preparing sailing-level data query to enable integration with the Drivers Model pipeline.

- **Guest Logs Classifier** *(David M.)*: Erick requested access to David's code and data to address concerns raised by stakeholder Alessio. David sharing code and results for review.

Erick

Project Axiom

*AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.*

### Project AI Pivot *(Qualtrics Topic Extraction)*

*Self-labeling framework for automatic topic discovery from survey data.*

- **Qualtrics Abandon Cart Emerging Topic Detection** *(**Danusio** G.)*: Presented trending topic framework with semantic similarity and moving averages for emerging topic detection. Running backtest analysis for Seven Night Caribbean product to evaluate framework.

- **Qualtrics Abandon Cart LLM Topic Extraction** *(Rodrigo B.)*: Created a topic dashboards by week and product. Identified recurring Friday peak patterns. Preparing visuals for stakeholder presentation.

- **Power BI Dashboard** *(**Danusio** G.)*: VDI access granted to be able to develop and deploy for Power BI dashboards. Deployed Axiom dashboard to Data Science Premium workspace.

Erick & Cristian

## MyCruise Recommender

*Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app.*

### Recommendations Engine *(Cristian V.)*

- **Graph-Based Recommendations**: Shifting to graph based recommendations and precomputing and storing recommendations in Postgres. Achieved high precision on holdout sets for some meta products. Exploring .

- **Axiom Recommendations Frontend Tab**: New task to implement a frontend tab in the Axiom web app connecting to the existing recommendations API. Planned for the Friday GitHub Copilot workshop.

- **Missing Royal Beach Club Product Recommendations in Dev**: Bug found in dev API endpoint - resolved. Prod unaffected.

Ayon

Win-on-Waste

**Weekly Update – February 13, 2026**

**1. Demand Segmentation Framework – Development Completed**

The clustering-based demand segmentation pipeline for Interport models has been fully developed and is pending validation/testing. The segmentation logic classifies each trading day into **High Demand, Regular Demand, or Low Demand** categories based on a multi-factor feature set, including:

Historical consumption patterns

Day of week effects

Month/seasonality trends

Demographic attributes

Geolocation variables

Holiday indicators

Proximity to holidays and special events

Based on this classification, the pipeline automatically filters and routes historical observations into the appropriate demand-specific training datasets. This enables separate model training for high, regular, and low demand regimes, improving forecast sensitivity and reducing regime-mixing bias.

Testing and performance validation are the next steps.

Ayon

Win-on-Waste

**Weekly Update – February 13, 2026**

**2. POS Operational Data Quality Issue – Mitigation Module Developed**

We identified a recurring operational process gap across the fleet affecting POS consumption data integrity:

Items consumed on Day *T* are frequently closed in the POS system on Day *T+1*.

The POS dataset does not contain a marker distinguishing true same-day consumption from next-day administrative closures.

This creates artificial volatility in daily consumption signals (e.g., 600 units on Day T followed by 2 units on Day T+1).

This pattern introduces extreme fluctuations in the time series, leading models to regress toward the mean and produce biased forecasts (e.g., stabilizing toward mid-range values instead of capturing true demand spikes).

**Actions Taken:**

F&B Operations have been formally notified.

A fleet-wide memo has been issued to reinforce correct POS closing procedures.

From a data science standpoint, we have developed an outlier-detection and filtering module that:

Identifies likely administrative carryover anomalies.

Flags and removes these distortions from model training datasets.

Preserves genuine high-demand signals while eliminating artificial volatility.

Development of the mitigation module is complete. Testing and validation against historical scenarios are pending.

**Next Steps:**

Complete segmentation model testing and backtesting.

Validate anomaly-filtering logic impact on forecast accuracy.

Quantify uplift in model stability and error reduction.

Ben and Camila

SUPPLY CHAIN (IBP)

Highlight: Order Creation Dataset Recovery - Beyond Critical Path

Project Catalyst introduced a breaking change to our Order Creation table over the weekend. Ben identified on Saturday that the Ship Code and Voyage Number columns from Crunchtime datasets contained a new voyage number format that could not be mapped to the original voyage numbers used by Revenue Planning. This meant we could not join the Master Load Schedule to the Cruise Profile dataset, as our production prd_silver.ibp.master_load_schedule table still referenced the old voyage numbers — directly threatening the active Beyond pilot.

Ben and Camila led the rapid response:

Ben created a temporary mapping table as an immediate stopgap while coordinating with the Catalyst team.

Connor, Yan, Ben, and Camila held an urgent call with the Catalyst team to communicate the severity given the live Beyond pilot. The Catalyst team disclosed a previously unknown table containing Master Load Schedule data with the new voyage numbers.

Ben validated the new Catalyst table and discovered significant differences in column values and voyage inconsistencies compared to our production master_load_schedule table.

To protect data integrity, the team retained the existing prd_silver.ibp.master_load_schedule table and implemented a targeted join to the new Catalyst table solely to retrieve the new voyage number, then joined it back to the master load schedule.

The approach has been fully validated by comparing the new Order Creation dataset against the pre-Catalyst dataset. A backup table was created pre-Catalyst as a permanent validation reference to prevent loss from data engineering vacuum operations.

The Data Engineering team has been briefed and is now working to create a blended table merging the Catalyst shipfin table with the existing prd_silver.ibp.master_load_schedule, with their own data validation in progress.

Ben and Camila

SUPPLY CHAIN (IBP)

Beyond Pilot — Ongoing Data Pipeline Development (Camila)

Supply Name Consumption Ratios:

Resolved an issue where live consumption values were missing because supply name values were not populated for consumption prior to the current date. New supply name values only appeared after the current date, which prevented accurate live consumption calculation. The fix was implemented and validated in time for Paige's demo.

Snapshot Table:

Purchase/production order snapshot table now captures a static view of future one-month data only, scoped appropriately rather than overall data.

Baseline Table:

Consolidated table built from end-of-month run data for consistent reference.

Backup Baseline Table:

All weekly run values for the baseline table are now uploaded to Azure Blob Storage. This enables comparison across runs so that if predictions ever look off, we can replace specific values with data from prior runs.

Scorecard Table:

Purchase order: Added live spend report information, now running daily for the most accurate results for Laura.

Production order: Added live consumption report information, now running daily for the most accurate results for Laura.

Actual Quantity Needed vs. Spend Report:

Investigating alignment between spend report create dates and actual quantity needed refresh data. Planning to create a consolidated table with actual quantity needed (including backups) where the refresh date is not a single overwritten value on every run. The original baseline table will be adjusted to address this.

Master Notebook:

Creating a single master notebook to orchestrate all necessary tables sequentially to ensure smooth, reliable execution for the Beyond pilot.

Mirielle

CONTACT CENTER

Workforce Planning -- North America (Royal)

LOB & Skill Mapping

Current LOB mapping relied solely on skill field, breaking whenever skills/splits were updated

Redesigned with Darren and Gustavo to use department + sub-department + skill name combination

New structure automatically reflects future system changes for long-term maintainability

Call Forecasting & Backtesting

Computed monthly backtesting call volume dataset and refresh process for MAPE display (forecast vs. actual)

Gives stakeholders visibility into forecasting performance to guide upcoming adjustments

Next step: Integrate backtesting results into the application UI

Headcount Modeling

Refreshed hourly call volume proportions (2025-04-01 to 2025-09-30)

Source table prd_silver.mkrpops.cms_interval_stats_all not yet refreshed upstream; using average proportions by LOB as interim

Reviewing hourly call volume proportion dataset required to run headcount model

Working with Darren to confirm office hours (opening/closing times) as essential model input

Mirielle

CONTACT CENTER

Workforce Planning -- North America (Celebrity)

Darren's team provided target LOB list

Augusto shared Power BI report with Celebrity call volume and skill numbers

Ongoing iterative LOB mapping alignment between Augusto, Darren, Gustavo, and broader team

Additional features being computed to finalize mapping

Next: Cross-validation working session with Darren/NA team (tomorrow), collect office hours/shrinkage/baseline data, update app with Celebrity historical call volume

Workforce Planning -- International & Casino

Brendan set up repository, Nico provided URL: intlfcst.rccl.com

Next step: Migrate existing code and begin testing

Carlos

E-COMMERCE CUSTOMER TARGETING

Consumer Dashboard

Began development of low-level consumer dashboard showing individual consumer features, historical behaviors, and propensity scores across all models

Epsilon Feature Evaluation

Completed full run-through of new Epsilon features; consolidated into Excel showing benefit and rationale

Compared new features against existing to minimize redundancy

Epsilon Data Transformation

Started transformation of Epsilon data and historical snapshots using Min-Max scaling

Blocker: New Epsilon features only ~1 month old; 6-month window required. Preparing data for ingestion so it is ready when the window is met

Bug Fixes

Fixed CEL uplift models incorrectly referencing RCI target columns

Fixed model name validation/generation function error

Fixed Epsilon data ingestion error causing missing data

Fixed zero-division error in SMAPE computation

Code Quality

Removed credentials from repo

Added SQL injection prevention

Extracted duplicated code into reusable functions

Fixed typos, replaced deprecated function calls

Added type hints to all functions

New Capabilities

Added cross-validation option to model training and feature selection

Added unit tests

Added staging environment support (dev, qa, prd)

Caleb

CUSTOMER LIFETIME VALUE / CORPORATE STRATEGY

Received final model input data: media spend, lead sourcing, web funnel entries

Aligned on approach to gauge outputs at two aggregation levels (cabin mix and ship) to assess cabin mix assumptions

Finalizing data cleaning for model inputs with clean mappings across external Excels and internal Delta tables

Merging cruise industry cabin class mix by ship using fuzzy matching (messy ship names)

Documenting full process with GitHub Copilot: executive overview, workplan, technical workflow, data sourcing, assumptions table

Cihan

PCP Pricing Automation

Alaska Shore Excursions Dashboard (Gang & Rafa)

Built comprehensive Databricks dashboard with 20+ visualizations using complex SQL

Includes: revenue/bookings by category (2024 vs 2025), guest product distribution, category/product pair analysis, cumulative bookings vs days to sail, yield curves, bundled products, price trends, daily yield by category, deviation histograms

Presented to Rafa, Alex, Ivaylo, Anastasiia -- approved with requests for cost analysis, inventory analysis, and expansion beyond Alaska

Waterpark PRE (Gang Wang)

Presented price-demand EDA to Jorge and Anastasia

Proposed A/B test at different price points

Stakeholders recommended simple naive method: adjust price based on whether monthly revenue meets target

Second meeting held to finalize target revenue for pricing

Current avg price ~$60 should support elasticity modeling; prior ~$100 price point was too high (appeared inelastic)

Aagam

**RCI**** Revenue Management**** | PRE Logic Price Analysis**

Calculated the track based on the hypothesised methodology.

Methodology: It is a blended method, where we look at track 3 weeks in the future and projected pax build 3 weeks historically and the closer weeks are weighted higher and the average of that is considered as the track for the week to smooth out the track ask.

Using the new track method, I simulated this week’s PRE runs for B, I, and O cat-classes, comparing the current and hypothesized approaches to observe differences in price changes.

To gain a primary understanding of how the price changes are affected I first looked at the histogram of price change % spread for both the different methods and based on the chart, came to a conclusion that the newer method (blended 3 week weighted avg) is more centered towards 0, indicating that the price changes are more spread across the center and we will not see any major fluctuations in pricing.

To analyze the shift more precisely, I created a cross tab to track how price changes move between the two methods. This revealed that the spread of price changes has narrowed—for example, price changes that previously ranged between -0.75% and -0.5% have now tightened to around -0.25%, and so forth.

**RCI | PRE Dynamic Caps 2.0**

This week I focused on getting the correct T3 pricing to solve the QUAD Floor Variance subtask. Earlier quad floor variance was not dynamic, now we have updated it to consider the T3 pricing for that sailing, additionally ensured that the quad floor variance only applies to quad occupancies and not doubles.

Additionally, I focused on creating the automated sharepoint such that we have individual rows for each ship-sailingdate-catclass-occupancy, instead of having one list of fixed limits for all the sailings. This would enable us to manually change caps for any individual sailing that are doing good/bad based on the business.

Third, I focused on removing the wts dependency in the process.

Lekha

**CEL**** Revenue management**** | Save New Feature Columns and Prediction Outputs in Delta Table**

Status: This ticket is complete as of 2/12/2026

**Deliverables:**

The changes have been validated in QA and approved by Monica from Celebrity. Once we deploy to production, the tables will begin saving y_preds correctly in the history tables, along with all the columns needed for future price optimization run.

**CEL**** Revenue Management**** | Elasticity Model Health Check Dashboard**

**Data gathering for Dashboard**

Met with Monica to understand dashboard requirements for tracking price changes, elasticity impact, forecasted demand (y_pred), and model accuracy, with the goal of improving historical model-performance visibility.

Reviewed all relevant tables and identified that price_changes_elasticity_hist was missing y_pred values from June onward, even though weekly price changes and elasticities were present; fixed the issue and pushed the correction to production.

Investigated an overwritten table that previously contained y_pred history; attempted to recover past versions with Eswar, but encountered data-type mismatches (bin_length) across versions, making historical recovery infeasible.

Revised the approach by joining the elasticity model output table with the price changes history table to consolidate raw price changes, elasticities, and y_pred using keys: ship_code, sailing_date, read_date, cabin_category_class_code.

Identified a read_date calculation issue in the model output table (derived as sailing_date − bin_end × 7 days), causing misalignment with the Friday-based read_dates used in price changes notebook table working on correcting this logic to align read_dates and enable consistent joins

Ignacio

PCP Pricing Automation

**RCI | OBR | Drink Package PRE for Bundles**

**Add additional improvements to the optimization routine accounting for the effect from RBC-beverage bundles**

The main changes to be enhanced in the optimization routine are:

Make price and demand ratio of solo beverage bookings vs. bundle beverage bookings more demand driven for the particular sailing be optimized

For both price and demand, adjust the backup business knowledge driven assumptions to be more dynamic and data driven rather than with hard coded business rules (this well help automatically fix drifts in these trends in the future).

**OBR | Hybris | E2E Final Promo Automation Testing in Production**

Delayed while additional things need to be debugged from Digital/Product team & the final approval process procedure is finished for the workflow.

Doug

**RCG **** Revenue**** Management****| PRE Common Core Price Upload Facility | FEB**

**Separate RCI pause uploads from price uploads | FEB**

Status: This ticket is complete as of 02/06/2026

**Deliverables:**

Pause table loading from Oracle separated from price upload pipeline. All requirements satisfied.

**RCI: Transfer price upload process from ADF to Databricks**

Status: This ticket is complete as of 02/06/2026

**Deliverables:**

PRE price upload moved into Databricks job pipeline. Australia processes at noon and non-Australia processes at 7:30pm on Tuesdays

In Progress

Dual: Schedule RCI and Celebrity to run sequentially | FEB

Dual: Combine RCI and Celebrity price upload into single table | FEB

Michelle

CEL Revenue Management:

**Category-Gapping 2.0**

Final approach used: Allowed APD to deviate by 1% from true max revenue. Team requested minimum 3% gap on all sailings.

Output is being reviewed by business.

**Category-Gapping 3.0**

Presented updates to CEL business on 2/10/26. Approved pricing calculations (bundled cost per person). Team is pleased with current progress but has requests for next meeting:

Back tested sailing examples.

Combined approach where GTY decision is a trade-up choice using the 2.0 model and the EBM Classifier only includes the physical tiers.

Features:

No preference between laf-tier vs tier-tier gaps.

Strong emphasis on availability features.

Further exploration of SPI features.

Trained models for ship/meta/cat-class, ship/meta, ship/cat-class, ship, meta, cat-class. Saw strongest signals at brand and ship-class aggregations. As models become more granular, there is sparser data.

Current focus is feature selection. Following Evan’s framework, I have added:

GTY booked %

Deployment length

Days at sea

Holidays during length of sailing

Spending score for sailing

Next steps:

Continue testing features and feature selection methods.

Output sailing examples for business team.

Align RCI with CEL progress as my focus has been on CEL models.

Lamis

**CEL**** Revenue Management**** | Pricing Optimization | Data Adjustments Approval + Track Optimization Readiness (Post PRE4.0 Review)**

**Run Price Optimization Model + Compare Recommendations**

Did an initial run on the week of Jan 26th,  presented results to the business and received their feedback. Implemented their feedback and completed another run based on this week (the week of Feb. 9th). Generated comparative report and has a meeting with the business tomorrow to discuss the results and receive their feedback.

**Generalize_the_Model_PWL_function**

I completed the codebase for this task in standardized, bi-branded, and class object format. It takes 5-8 mins in average to process for each ship_code. Currently optimizing for speed of processing by experimenting different parallelization/repartitioning settings. Also, experimenting with writing long-format tables (to avoid 2 array type columns). This may take 1-2 more story points.

Jesse

SSC Revenue Management

SSC Revenue teams request to revert prices back to their status two weeks ago. To expedite this process (so Revenue doesn't have to resubmit manually), SSC Revenue team has provided a list of price recommendations to revert. I am creating a modified version of PRE code that is designed to take these changes and insert them into the reservation system.

Glen-Erik

CEL PROPEL:

Offer templates: Presented new offer template to OBR team and aligned changes needed in configurations on their side. *(Glen-Erik)*

Measurements Dashboard *(Javier & Glen-Erik)*

Optimization: met with JC to troubleshoot measurements dashboard and received guidance on areas for improvement that the OBR team should address. Using aggregate tables and incremental refreshes. The additional dynamic test/control measurement charts also need to be redone without python code. *(Glen-Erik)*

Missing categories: investigated why there are missing categories in the dashboard. Redoing the python chart and data will likely fix this issue. *(Javier)*

Uplift measurements logic: investigated current logic to understand and document metrics in place for dynamic test/control *(Javier)*

Solstice Deck Plan update: learned process to update deck plans. The plans provided by OBR must be complemented by a housekeeping file that is not yet ready to map the stateroom attendant section to a stack of offers.  *(Glen-Erik)*

Investigated how to add Park West logic replicating Effy targeting. Most of it can be done with minimal changes, like targeting high spenders (top 5 percentile) and/or people that spend more than 1K onboard. Targeting AI / RO, honeymoon is easy as well. Targeting past purchasers would require more custom logic that should really be generalized to be "past purchaser of current product" and "past purchaser of current product category" rather than "past effy collector" and adding "past park west collector".* (Javier & Glen-Erik)*

Support: Trained offshore team on how to regenerate offers when necessary. *(Glen-Erik)*

*Hiring: new contractor to support PROPEL should be joining soon, extended an offer, pending start date.*

Eswar

RCI: Revenue management

SPI: (Eswar)

Separated project from feature store.

Setup all CI/CD for the new SPI repo & productionized workflows via bundles.

Migrated Databricks Asset Bundle standardizations to QA, unfortunately there was naming bug that deployed the workflows to the wrong place creating duplicates and we had to roll back those changes. Should be ready to redeploy next week. *(Javier, Eswar, Glen-Erik)*

Data Governance: Aligned architectural process to marry the Data Validation Framework with the Data Governance checks, starting with stopping pipelines from running if critical tables are outdated. Raising silent failures must be transparently communicated to the development and business teams in advance because the more rules (beyond outdated critical tables) we add, the higher the likelihood that a process will fail when it shouldn't (false positive). The business must approve and validate these automated decisions to stop pipelines. *(Glen-Erik)*

Support: *(Eswar)*

Restored PRE Lite using historical data versions for Data Scientists to build visualizations upon.

Deploying new code and assisting with code conflicts and issues.

Glen-Erik

MIAP

There are ongoing failures in MIAP pipelines. Some are known issues, others are bugs that could have been avoided running in QA which is currently off.

*Hiring: contract to hire passed interviews with Glen-Erik & Eswar, and Mert & Brendan. Needs approval from David on budget. Pending take home as well.*
