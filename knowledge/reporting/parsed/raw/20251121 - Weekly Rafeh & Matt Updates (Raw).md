**Erick**

**Project Axiom**** (Medallia)**

**Progress**

Following the well-received GenAI Medallia ShoreX specific summaries Onboard Revenue (Megan Shaw) wants to expand scope by creating weekly, monthly, quarterly, annual tour specific summaries to track product sentiment.

Digital BI (Doreen) expressed strong interest in collaborating on identifying Medallia ShoreX Tour "verbatims" from guests that could be highlighted across App/Web.

Kristina Murray proposed expanding scope of our Medallia Drivers model to include better understanding how guest feedback influences future return rate & spend.

Delivered an ad-hoc Qualtrics survey GenAI deep dive which breakouts 3000 survey responses into quantified topics and summaries. Received feedback from stakeholder and will work to implement changes.

**Erick**

**Project Axiom**** (Medallia)**

**Working On**

Divisions Templates will be completed by end of this month and presented to business by mid December.

Additionally team is working a weekly fleet detractor report to be delivered by end of month.

Released a new version of the Axiom Medallia App with multiple bug fixes and minor features such as the ability to export data in bulk, improved API response times with code changes, and ability to load random subsets of comments when the user is attempting to analyze a context window that is too large for the API call.

The team is continuing to work on integrating the Drivers dashboard into the Axiom webapp. New Model will be trained at booking level data instead of consumer level.

**Erick & Cristian**

**PCP**** ****MyCruise**** Recommender**

Successfully implemented postgresql database into calendar recommender service. This allows us to scale pre-computed recommendations.

Met with Digital Engineering for a 30 min recorded session introducing the teams to the API in preparation for App integration.

Ayon

Win on Waste:

In response to intermittent issues where the FPMS app displayed a blank forecast screen despite receiving 200 responses from the third-party API to Couchbase, we initiated saving the entire JSON payload into Databricks volumes. This allows querying the JSON data directly to verify if the issue originates from our side.

Addressed and resolved multiple tickets raised by IT managers on ships via Snow, providing detailed explanations and supporting screenshots.

Initiated development of a digital itinerary twin model for each ship, recipe, and venue—treating each day as a sea day. This solution aims to mitigate the long-standing problem of last-minute itinerary changes caused by rough sea conditions, such as missed ports or altered routes.

Mert, Brendan, and Reza

Claims Management

Met with Corporate Strategy and Risk Management teams for pre-alignment on project TIDE CAR prior to the meeting with Naf.

Brendan Reloaded legal data from Riskonnect into Databricks and troubleshot data quality issues for Reza's analysis.

Reza Prepared data and performed modeling and tuning for the legal project (TIDE). Comparing models with and without sensitive features.

Mert

MIAP

Completed the Digital Twin GUI on the MIAP app and released it to stakeholders for feedback. The GUI lets users experiment with models by changing all possible voyage configurations and viewing the simulation output visualized.

Met with the GMO PMO team and discussed support for developing a CAR memo-writing AI assistant.

Had a kickoff meeting with Nacos to discuss the Silver Muse OPC UA installation project.

Met with the GMO Strategy team and aligned on next steps for non-energy-related AI initiatives for marine. Agreed to create a document showing all project ideas for asset management and safety to present to GMO leadership.

Brendan

MIAP

Updated the Fuel Forecast API to utilize the new ALS Compressor Power model.

Added a tool in the Fuel Forecast API to determine the typical ALS turn-on speed for a ship.

Fixed a bug in the Fuel Forecast API that resulted in a power prediction of 0 when the ship had no ALS-enabled propulsion model and the user requested an ALS utilization rate of 100%.

Conducted Git training for the MIAP team covering best practices such as feature branching, resolving merge conflicts, and undoing bad commits.

Mahshad

MIAP

Fine-tuned the service power model to improve results.

Worked on deployment optimization model.

Identified ML-driven energy-saving opportunities for TCV valve sensors.

Ram

MIAP

- Fixed issues for the Crosser shipboard table.

Developed a script to notify and load records landed in the bad records folder by the autoloader.

Implemented capturing of data frame size in the REST API.

Next week

Check the checkpointing location, identify any missing data for this month, and develop a script to address it.

Resolve a certificate issue in the REST API and progress on the logging mechanism.

Mehdi

MIAP

Updated the stability booklet vector data by integrating the SY and HY 2025 reports.

Worked with the Databricks team to fix an integration issue between the regression tool and the Agent.

Reza

MIAP

Tuned service power models for the Fuel Forecast platform.

Arya

MIAP

Fixed an ETL pipeline failure for XC.

Added XC to AHU and chiller.

Participated in a hackathon (did not win).

Finished deploying UT to all MIAP analytics.

Working on service power parameter tuning for moving weighted average (step size).

Learned a great deal about how azipods function.

Will

MIAP

Delivered LNG Speed Fuel Curves for F1.0

Added Maneuvering voyage phase to FACTs features

added local time voyage phase start and end to FACTs features

Found and resolved bug in MGOeq convrsion formula in power plant feature notebooks

Added Maneuvering arrival and departure speed to FACTs

Recreated AX speed fuel curves for Decrab Team with updated configs

Created UT speed fuel curves at the request of Decarb Team

Ben & Camila

Supply Chain: IBP – HF&B
New demand forecasting model (backtest vs current model)
Scope: Beverage, Consumables, Food, Replaceables; Royal Caribbean & Celebrity, excluding Medical; backtest April–October 2025.
Metric: MdAPE (median absolute percentage error).
Results: New model median MdAPE 16.2 vs 18.3 for current model (6.7% reduction in typical error).
New model outperforms in 5 of 7 months (April, July, August, September, October).
Biggest gains in Replaceables and Beverage; modest gains in Food; mixed/flat results in Consumables.

Ben & Camila

Supply Chain: IBP – HF&B
Uniforms & SharePoint data
Preparing crew uniforms version 6 for SharePoint, adding logic to handle array-type product numbers that SharePoint does not support natively.
Adding UOM (unit-of-measure) fields to all SharePoint files.
Enhancing SSC Uniforms challenger model notebook to support array-type product numbers and group crew model types by contract length and cost center (for accuracy for Yan and Paige).

Ben & Camila

Supply Chain: IBP – HF&B
Medical free-of-charge consumption
Integrated medical “free of charge” consumption using inbound orders and shipboard inventory instead of the legacy consumption table.
Retraining backtested dates so consumption values are correct under the new methodology.

Ben & Camila

Supply Chain: IBP – HF&B
SSC port mapping / finance data quality
SSC Warehouse Transfer Order → Region mapping is waiting on a fixed port itinerary table from Data Engineering (to be delivered to QA).
Identified duplicate records in data for the finance automation tool; awaiting review from Yan.

Ben & Camila

Supply Chain: IBP – HF&B
CocoCay & Royal Beach Clubs demand work
Researched shore excursions as an input to CocoCay demand forecasting, with potential application to Royal Beach Clubs where no historical consumption exists (e.g., Nassau in three months).
Constraint: instructed not to use CocoCay forecasts directly for Royal Beach Clubs (unlike new ship automation).
Considering Revenue Management’s suggestion to use Coco Beach Club as a comparison point.
Implementing CocoCay port logic from Fanny on which items should come from which source; this logic is being hardcoded now.

Ben & Camila

Supply Chain: IBP – HF&B
SSC Par Level (safety stock, inventory, orders, pricing)
Safety stock logic completed and pending review from Yan:
Convert monthly forecast to daily consumption; apply configured days of coverage for items marked as needing safety stock; compute SAFETY_STOCK_VALUE from product cost.
Integrated safety stock with shipboard inventory (completed, pending review).
Order-creation logic completed and pending review: safety stock used as proposed MIN_PAR_PROPOSED; MAX_PAR_PROPOSED set to 2× minimum.
Last purchase price from consumption, spend, and shipboard inventory integrated into SSC Par Level logic, pending review.

Mirielle

Contact Center – Lear Prioritization OFTOCX (SBOFRD E2K Replacement)
Testing and validation
Completed iterative testing with the Siebel team: shared min/max sequence IDs and record counts for each sub-lead; verified counts and sequences match between systems.
Ran ETL production-style processes for each lead type and loaded outputs to SFTP.
Fixed code to ensure the brand column is consistently uppercase.
Go-live planning and next steps
Target production window: Dec 9 (preferred) or Dec 11; migrations likely evening of Dec 8–9; avoiding Black Friday/Cyber Monday.
Test plan due Nov 18; limited time the following week, so testing must be ready ahead of the Dec 9 window.
New code to use agency ID from SBOFRD/SBCXED for suppression/delay rules goes live Nov 18.
Business rule decision needed: confirm delaying certain agency leads by two days vs suppressing them.
Expanding testing to validate business rules (phone formats, travel-agent leads, CVP rules, BAU rules), not just volumes.
Keeping key stakeholders (Amy Seplin, Rene, Adam, Chandra, CVP Siebel team) looped into communications and approvals.

Mirielle

Contact Center: Workforce Planning – North America
Databricks app migration to Azure Container Apps
Working with Mukund (platform team) to migrate the Workforce Planning app to Azure Container Apps.
Validating the app and fixing issues in the new environment.
Next: define promotion process for DEV/QA/PRD; grant access via an Azure AD group (no direct production access for individuals); transition to Service Principal + OAuth for Databricks access.
Proposed URL: RCGWFPlan.rccl.com.

Carlos
E-Commerce Customer Targeting
Model reporting and interpretability
Added dashboard reports for latest models: sailing_window, booking_window, and sailing_propensity.
Tweaked sailing-window models to add clearer labels and remove overlapping time periods, making outputs easier for business users to interpret.

Caleb

Customer Lifetime Value (CLV)
Documentation & methodology
Finalizing SOP documentation for CLV methods and database use, including clearer field descriptions, example SQL, join patterns, and aggregation rules.
Splitting into a public-facing guide and a detailed CLV-personnel version to avoid confusion.
Indirect cost logic and ETL
Validating updated RCI indirect cost logic (80/20 infrequent/frequent booking split) against the early April version.
Analyzing impacts by year, channel, cruise experience, and brand, and assessing the effect on rate adjustment factors.
Finalizing a refined ETL pipeline for a clean/shareable CLV table (adding CRUISE_HISTORY, more granular CRUISE_EXPERIENCE segmentation, and new indirect cost logic by booking and by RCI cruise experience).
ETL rerun planned once approved by Cory (target: week of 11/21).

Cihan

PCP Pricing Automation

OBR Waterpark PRE
Data issue identified; temporary copy table created in Unity Catalog as a workaround.
Data Engineering expects to fix the underlying issue by EOW.
Completed data preparation with Ignacio; actively working on the optimization component.
Met stakeholders to review current PRE status and discuss ideas for future versions.

Cihan

RoyalOne Community:

Digital – Qualtrics Survey
Implemented asynchronous, batched Azure OpenAI calls to run topic classification in parallel, significantly reducing processing time.
Digital – Guest Services Chatbot
Created and shared a sample dataset of escalation types and chat data.
Stakeholder is using it to detect patterns and define guidelines for classifying escalation types, which will inform future chatbot improvements.

Michelle

**CEL**** Revenue Management**** | Category-Gapping 3.0**

**Data Preparation**: Created updated tier-level dataset with normalized price features.

**Model Development**:

Built initial **Explainable Boosting Machine (EBM)** using normalized prices (LAF-based) and assessed feature importance.

Goal: Output a small optimization to confirm approach validity.

**Next Steps**:

Fitting a simpler **GAM** on top of EBM predictions for model simplification.

**Business Engagement**:

Sent initial sample predictions to business for review.

Michelle

**RCI Revenue Management**** | Category-Gapping 3.0**

**Business Meeting (11/19/25)**:

Reviewed category gapping plan and presented initial strategy.

RCI wants to build on **2.0 recommendations** and **only optimize physical categories**.

Tier-level optimization not desired (most bookings fall into same tier).

Avoid changing price differences between Bronze categories.

**Data Work**:

Building category-level dataset.

Created **dynamic WTS bins** based on track demand.

Lamis

**RCI**** Revenue Management |**** Track Optimization**

Ran a small test to generate optimal track for a new Alaska deployment in 2027 (as requested by the business).

Shared results with the team and compared against:

Historical meta-ship class-sail month performance.

Top SPI-based performers.

Feedback was positive. but were probably going to exclude Suites cause they are always behaving erratically vs specific rules

- Lamis

- **RCI Revenue Management | RCI Price Optimization**

Continued validation and refinement of the optimization model.

**Prediction Error Adjustment**

Issue: Counter-intuitive price changes caused by model prediction errors (e.g., predicted bookings ≠ actual bookings).

Fix: Adjusted demand curve to include actual price point and shifted curve to align actual bookings with predicted curve for correct directional price changes.

**Track Performance Constraint**

Added a **3-week hit/miss rate** metric:

If hit_rate ≥ 0.5 → raise price.

If hit_rate < 0.5 → lower price.

**KPIs for Validation**

**Optimal Acceptance Rate**: % of cases where optimization recommendation ≈ analyst decision (≤ 2% difference).

**PRE Acceptance Rate**: For comparison with optimal.

**Opt**** vs PRE Acceptance Rate**: Cases where PRE accepted but optimal rejected.

**Results**:

Best scenario: ~80% acceptance rate vs 19.1% for Alaska.

Only 1% (8 cases) where PRE accepted but optimal rejected.

Currently investigating those cases.

**Analyst Behavior vs Model Logic**

Analysts raised prices despite high miss rate (opposite of optimization logic).

Eddie investigating rationale behind these decisions.

Reinforces need for business rules notebook after optimization.

Lekha

**CEL | Elasticity Minor ****meta Products**

**Asia Model Evaluation**

**Objective**: Assess Asia as an individual model and its key metrics.

**Meta Mapping Tests**:

Mapped various metas for Asia to check if different mappings improve metrics.

**Result**: No significant improvement observed.

**Key Observations**:

Asia has only **one ****rdss_product_code**, which may interact poorly with features expecting multiple codes.

Due to this constraint, mapped Asia meta to **BRAND MODEL** (consolidated model of all metas except Australia).

Australia can remain an individual model (metrics are strong).

**Experiment: Cabin B Exclusion**

Investigated excluding **Cabin B** for ship_class edge (ship_code = RF) from training dataset while keeping all cabins in test dataset (mirroring current production behavior).

Implemented and ran **backtesting** for upgraded model on separate train/test datasets.

Required tweaks to backtesting code to support experiment.

**Result**: Excluding Cabin B in training did **not** significantly impact evaluated metrics.

Aagam

**RCI ****Revenue Management**** | ****PRE Logic**

**Year Fix in Sailing Baskets**

During a code review I discovered that using the normalized sailing date (month-only) causes incorrect Days_Apart calculations and allows sailings from different years to be grouped together. I’m meeting with the business to determine whether this is expected behavior; if not, I’ll update the logic to use full sailing_date and re-run tests before deployment

Atefeh

**RCI ****Revenue Management**** | ****PRE Logic**

**Pricing Paid Analysis**

**Data Preparation**: Finalized aggregation and confirmed hierarchical patterns for all groups/subgroups with Eddie.

**Exploratory Analysis**:

Compared **TRF vs TRF_T4** distributions.

Analyzed subgroup behavior.

Conducted **Timing and WTS-based analysis** for REPLACEMENT_VALUE category (last-minute promotions), segmented by WTS buckets.

**Deliverables**:

Generated category/subcategory percentage tables showing distribution and contribution patterns.

Shared finalized insights with Eddie.

**VPS Workflow Debug**

Issue: Final table had many nulls due to update file missing last 20 days before merge.

Fix: Corrected merge logic and updated production job to ensure proper data inclusion.

Atefeh

**CEL**** ****Revenue Management**** | ****PRE Logic**

Price Paid

**CEL Team Request**

Clarified handling of **negative ****track_pax_build**:

Implemented **variance-preserving adjustment** (shifts track and builds proportionally to maintain variance).

Integrated variable normalization, modified code, and generated PRE output.

**Outcome**: CEL team reviewed and approved; changes moved to **production**.

Jesse

SSC Revenue Management

**A/B Testing Reporting**
I finished an exploratory data analysis (EDA) of SSC's ongoing A/B test to determine how successfully PRE is managing to dynamic track. I compiled the results in a powerpoint deck and presented to SSC business and executive teams. While PRE is not managing to track, due in large part to small-magnitude price changes, my findings created important conversations on how to successfully utilize PRE to manage to track in the future.

Outcome of meeting with Claire Mason is to continue PRE testing, but to design AB testing in January to understand the pricing-power of SSC. Concern is that current pricing changes by PRE and analysts are not effectively steering demand.

Jesse

SSC Revenue Management

**PRE Monitoring**
I finished up a collaboration with Data Engineering to create two tables to track price changes and SSC promotional discounts. These tables are now accurate and reliable. We can use them to monitor not just listed prices, but the actual cabin prices that are available to consumers. They also alert Data Science and Revenue teams as to the origin of price changes in addition to their implementation date.

Doug

Celebrity Revenue Management: Celebrity Perks Test:

Business landed on a 12/3/25 start date. I provided the finalized sailings to them this week and we're currently iterating through options to ensure they get the test coverage they want with optimized matched sailings. Ready to go with plenty of time for any final adjustments. Test to run 8 weeks across 6 metas in both peak and off-peak seasons. Next up will be test monitoring after the launch.

Doug

RCI Revenue Management: Inventory Automation:

Over the past several weeks, moved 13 high-priority automation processes out of ADF and into Databricks. Processes have been fully-validated in the new environment and are running without error. This is a major upgrade in that it frees up entire blocks of time which prevented people from doing pull requests into ADF. Additionally, the business teams are now able to run and cancel production jobs without having to ask DA2I or MLOps for assistance, giving them more autonomy over the control of their processes. The jobs also run on the lowest possible powered job cluster (2-4 DBU/hr), reducing Databricks costs.

Doug

RCI Revenue Management: Optimized Replenishment:

Investigation of meaningful KPI to measure replenishment success and revenue impact. We discussed this in our 1:1 and both Celebrity and RCI are encouraged by the approach... modified demand forecast for guarantees combined with measuring "Stockout Rate".

Doug

Celebrity Revenue Management: Dual-branded PRE:

Moving discussion forward discussions for plan to combine code bases with rewrite of PRE where necessary. Eddie and I have had some high-level discussions but will wait for Kevin's return to get into details on scheduling the work. First look is to get a common data pull foundation since currently each brand is doing it's own data pulls from identical sources. Goal is a single dual-branded data pull and prep on Monday afternoon and then branching into the main code and identifying core common elements vs. where brand requirements necessitate divergence in the code.

Glen-Erik & Alejandro

PROPEL

New styling template deployed to dev/QA

New ShorEx templates created for each meta_product

Holiday sailings now receiving awareness-only offers rather than turning completely off.

Dynamic control-test groups: created workflow jobs

Glen-Erik & Eswar

RMA

Data validation framework:

Added file based trigger to validation workflow, which gets job_id, run_id from main project pipeline based on which validation checks will be applied.

Feature store migration:

Guidance and support to DE team providing tables information, usage details, refresh timings etc

Operational Support:

Support and guidance in migrating Inventory ADF pipelines to Databricks for both RCI and CEL brands.

Advisory on creating OBR workflows in ADF, where we need to copy few customer solutions tables from Oracle to ADLS.

Providing ML support debugging issues

Monitoring CI/CD deployments, PRs

Glen-Erik

IBP Supply Chain: Separation of Dev & Prod:

Created usage report for data tables in IBP to tease out which one need to be migrated. In IBP alone there are 2,657 tables out of which 973 have been updated in the last 60 days. The number of tables and further analysis suggests high level of technical debt with many tables with identical structure being created with dates in their names to split the data.

Created script to migrate the data for IBP when data tables are finalized.

Glen-Erik

Win-on-Waste: Separation of Dev & Prod:

Provided full list of data tables that are active for Ayon and team to confirm before migrating them. Some restructuring or refactoring required since the data in "dev" is managed as a different wow_test schema which need to change to be dev and prod catalogs instead.

Eddie

RCI Revenue Management: Meetings

Pricing Project for Panama Inclusive Rates

TAP Project pushed this week with objective of Improving European Acceptance Rates on PRE (extra rates previously not pushed vs Base Sailing)

Eddie

RCI Revenue Management: Meetings

PRE

Based on previous discussion, future conversation with Brand stakeholders to plan out future PRE before we continue changing separate models.

Audit of FIT track inputs – identifying sailings falling off (some of which are solved) and where methodology has changed (Currency Level tracks no longer required- action being taken)

Progress made in gauging Promotion impact on Track Performance in booking windows – key for expanding PRE acceptance within Close In Window

Progress made in Price Optimization method of price change vs 4.0 elasticity model output. Deployment expected after the holiday

Eddie

- RCI Revenue Management: Meetings

Inventory Automation

Enhanced ADA Berthing to account for Cat Class Upgrade

T4 Limits moved Entirely into Databricks

All of Inventory Automation migrated out of ADF

Opens up ADF Prd push Schedule

SPI

Discussion with RCI highlighted next steps:

Compare scores with yields for 5 ships to gain confidence / alignment in scoring model

Current iteration of model captures trends but SOME areas of opportunity

Experimenting with potential features (with mindset of being able to tie into Yields without introducing TOO many factors)

Seasonal capacity (deployment schedule based)

School calendar (differences in spring break, easter, etc) (Most likely to stay)

Holiday input (captures days outside rev reports -  Chinese New Year, etc)

Macroeconomic Trends (CPI, search trends, etc)
