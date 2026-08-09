Erick

# Team update

- New capgemini contractor joined the team this week.

- Will have interviewed 10 candidates in the last week.

Erick, Gaurav

# Axiom: Medallia

- Gaurav is working to implement drivers model by end of month with POC dashboard.

- David (new contractor) is leading the development efforts to build a generalized framework for metadata extraction over unstructured data. This will allow us to quickly scale to other data sets and various granularities.

- Erick met with several stakeholders this week and is aligned to deliver meta data for Division level reports using the framework that David is building by early November.

- Erick and team will deliver division specific reports be early December.

- Erick is working with CEL/RCI to refine target setting model as the current model is currently under performing. Fleet wide NPS has been trending upwards and estimations from the current model for 2026 are below expected.

Erick & Christian

# PCP Product Recommendations: MyCruise Recommender

- Met with Digital Engineering to agree on expected API response for Calendar recommender.

- Working to implement MVP and enable digital engineering with a functioning API and allow for development of the feature in the app.

- Model improvements will be made AFTER the API is functional.

Mert
MIAP
Started developing the Edge and Quantum class power plant optimizer and completed the Radiance and Millennium class optimizers.
Prepared for the Digital All-Hands presentation of MIAP.
Working on cybersecurity improvements to the MIAP app and API.
Presented Sea Events analytics to the Safety team.

Ram
MIAP
Updated the existing Bronze Eniram code to align with the new Eniram system, making necessary compatibility updates.
Modified the Eniram API package, updating methods to reflect the new endpoints and response structures.
Moved Safety Culture data to production for both Bronze and Silver tables, ensuring availability and consistency.
Implemented essential changes to the Eniram code within the DE workspace to support the updates.

Will
MIAP
Delivered an ad hoc request for Speed Fuel Models for the SSC fleet, including a Power BI dashboard for easy access and analysis by business partners.
Investigated XSS vulnerabilities reported by the Cybersecurity team.
Worked on consolidating the STG feature into one calculated column based on ship configuration.
Investigated and documented issues in power plant models.

Mehdi

MIAP
Created a clean branch from master and moved the stability agent to it to avoid conflicts.
Worked on deploying the agent and fixing the issue with updating to the new endpoint version.

Brendan
MIAP
Completed incinerator implementation in the Fuel Forecast API.
Began performance tuning for data processing in the Fuel Forecast API by batching predictions by day (in progress).
Completed an overhaul of the reference drydock calculation in the Fuel Forecast API.
Aligned with the GMO team on drydock and hull coating activity dates and updated propulsion models accordingly.
Performed test cases on the propulsion component of the Fuel Forecast API.

Reza
MIAP
Presented at the Digital All-Hands.
Started working on the fuel forecast comparison platform.
Updated the Marine Analytics version.

Mahshad
MIAP
Implemented fixes on the GMO app.
Investigated anomalies on the IC resulting in an approximate 300 kW impact. Root cause: the IC absorption chiller was down, increasing AHU power.
Reported anomalies on the IN. Operations responded that changes were made due to a customer complaint and will revert the settings to normal.
Sent an email about anomalies on SM ventilation fans and TCV valves.
Sent an email regarding the WN ventilation fan setpoint; compared to similar outdoor conditions (e.g., HM), several setpoints should be adjusted.

Ayon

Win-on-Waste: WOW Update 10-09:

Weekly Report Summary:

1. Investigated and resolved a critical issue causing zero or null forecast counts in the MDR pipeline that emerged on 10/6. The root cause was traced to a data anomaly in a sailing itinerary feature outside FPMS scope. The original use of wildcards and regex for filtering failed due to extraneous characters in this feature, leading to null results. The fix was implemented and successfully replicated in the specialty pipeline.

2. Collaborating with the Manila team to develop a first-point solution for effective triage of forecast and data quality issues.

3. Conducted four candidate interviews: three from Insight Global and one from CapGemini.

4. Resolved a duplication issue in the specialty pipeline caused by Couchbase overwrite conflicts.

5. WoW - Hypercare for the catalog parameterization, fixing some bugs that popped up. Running smoothly now.

Glen-Erik & Brendan

MIAP - Fuel Forecast API

Completed Incinerator implementation

Began implementing performance tuning for data processing by batching predictions by day (in progress)

Completed overhaul of reference drydock calculation

Aligned with GMO team on drydock and hull coating activity dates - updated propulsion models (again) to align with these dates

Performed test cases against Propulsion component of the API

Glen-Erik & Alejandro

PROPEL

Fixed a photo-offers issue in Propel to ensure it reaches the whole fleet.

Recreated the PCD logic to enable dynamic control testing.

Tested an aggregated uplift measurement approach by category.

Uploaded a sample of passenger promotions to the new Kafka topic as part of the pre-cruise integration testing.

Ben & Glen-Erik & Brendan

Supply Chain (IBP): Environment Separation:

Upgraded linked services used across all Customer Solutions ADF projects. Pending testing and implementation.

Pre-requisite for IBP as well.

Clarified missing data access dependencies to use a Service Principal

Created new CICD pipelines for ADF to QA and PRD, not yet turned on.

Next steps for both IBP and WoW: develop data migration script to move data to QA/PRD and identify which tables need and do not need to be migrated in each project. This script will be reusable for other projects as well.

Glen-Erik

RCI Revenue Management: Pricing Automation Operations:

Replaced all CICD pipelines with Databricks Asset Bundles. Solved some parallel development conflicts that arose.

Ben & Mirielle

Contact Center: Lead Prioritization

OFTOCX modeling completed for Royal and Celebrity; productionization for Royal underway.

Lead Prioritization – Offer to Cancel (LP OFTOCX)

Completed

OFTOCX feature engineering for Royal and Celebrity.

OFTOCX modeling for Royal and Celebrity.

In progress/Next

Building the production pipeline for Royal; Celebrity to follow.

Dependencies/Asks

None surfaced beyond standard MLOps enablement to deploy pipelines.

Ben & Mirielle

Contact Center: Workforce Planning – North America

Workforce Planning NA data refresh pipeline built; app improvements in motion; International Markets scoping started.

Completed

Built the ETL process to refresh data feeding both Main Page and Data Visualization components of the app.

Conducted testing session with Jason Atkerson and team to validate updates.

In progress/Next

App improvements:

Enable historical display by Line of Business (LOB) on the Main Page.

Update Main Page to display percentages.

Set up baseline assumptions per LOB (to be provided by Jason).

Review incoming data sources with Darelle that feed the app.

Dependencies/Asks

Baseline assumptions per LOB from Jason.

Data source review with Darelle.

Workforce Planning – International Markets

In progress/Next

Held kickoff meeting with Nico and team; project outline under development.

Schedule next alignment meeting to confirm scope and next steps.

Dependencies/Asks

Alignment on scope, timelines, and data availability with Nico’s team.

Ben & Camila

Supply Chain:

Next-gen HF&B modeling progressing with expanded feature set and rigorous seasonal backtesting plan. Multiple analytics deliverables completed and pending stakeholder review (Yan). Finance automation and medical par levels advanced; uniform demand file integration ongoing.

Next-generation HF&B models (RCI/CCI) – feature engineering and selection

In progress

Feature engineering supported by Cursor using all existing production features plus the following new features:

Weeks since first consumption

Consumption growth since first four weeks average

Category level consumption

Product share of category

Ship total consumption

Ship consumption trend

Consumption skewness (13 weeks)

Consumption kurtosis (13 weeks)

Consumption percentiles: 10th, 90th, IQR, Range

Weeks with zero consumption

Trend cycle consumption

Consumption seasonal component

Passenger seasonal component

Consumption detrended

Consumption exponential moving average

Consumption average, standard deviation, is spike, is drop, weeks since last spike, weeks since last drop, is recovering

Feature selection plan:

Stratified sample of 500 products: 50% high, 30% medium, 20% low consumption; 300 food & beverage and 200 consumable/replaceable products.

Five backtested seasonal test sets with SHAP and recursive feature elimination using 5-fold cross-validation:

P1 Summer 2024: 2024-07-01 to 2024-09-30 (cut at 2024-06-30)

P2 Fall/Winter 2024: 2024-10-01 to 2024-12-31 (cut at 2024-09-30)

P3 Winter/Spring 2025: 2025-01-01 to 2025-03-31 (cut at 2024-12-31)

P4 Spring/Summer 2025: 2025-04-01 to 2025-06-30 (cut at 2025-03-31)

P5 Summer 2025: 2025-07-01 to 2025-08-31 (cut at 2025-06-30)

Governance/documentation:

Delivered documentation on adjusting consumption forward to “next Monday minus 7 days” to prevent target leakage, including a 30-second summary plus detailed explanation, examples, and FAQs for stakeholders.

Ben & Camila

Supply Chain

Deliverables completed and pending review

Order Creation – Last Purchase Price for RCI/CEL and SSC delivered; pending review from Yan.

Min and Max Par Level Unit Cost and Total Value for RCI/CEL and SSC delivered; SSC unit cost logic being finalized post-review with Yan:

Use shipboard inventory unit cost if not null and not zero.

Else use consumption unit cost (same conditions).

Else use spend report unit cost.

Else unit cost = null.

Ben & Camila

Supply Chain (IBP)

Finance and inventory analytics

Finance automation (food, beverage, consumables):

Updated dev_datascience.ibp_sso.SSC_FINANCE_AUTOMATION:

Loaded Excel category mappings into NEW_CAT_1..5.

Cleaned and filled consumption AREA/AREA_CODE.

Joined consumption, voyage, and passenger data to build 2024 historical and 2025 future datasets.

Aggregated 2024 to one row per ship/item to compute UNIT_COST and QTY_PER_PAX.

Projected 2025 TOTAL_QTY and TOTAL_PRICE using UNIT_COST_2024 carried forward.

Filtered to MAIN_STORE categories: Food, Beverage, Consumables; appended NEW_CAT_1–NEW_CAT_5.

Medical Min and Max Par:

Loaded dev_datascience.ibp_sso.medical_min_max_par_level.

Computed per-voyage daily demand = voyage_demand / sailing_nights (if >0, else 0).

Added year/month; converted sailing_nights to sailing_days = sailing_nights + 1.

Aggregated by year/month for average consumption duration; joined back to voyage records.

Grouped by product/ship to compute average days of consumption and average daily voyage demand (filling missing daily demand with zero).

Calculated MIN_PAR = avg_days *avg_daily_demand**; MAX_PAR = 2 *MIN_PAR.

After review with Yan, set avg_days to 21 (3-week delivery frequency) in place of previous calculation.

Uniform demand files:

Working to make versions 5 (PRDs modified) and 6 (crew) compatible with code built for version 1 (ship/item level).

Two uploads completed; additional uploads and logic adjustments still needed due to added steps/conditions.

Ben & Camila

Supply Chain

Next Steps

Complete feature selection and seasonal backtesting; move to model training/selection.

Incorporate Yan’s feedback on LPP and Min/Max Par deliverables; finalize SSC unit cost selection logic.

Finish uniform demand file v5/v6 compatibility and complete remaining uploads.

Dependencies/Asks

Timely review/feedback from Yan on LPP and Min/Max Par deliverables.

Ben & Caleb

CLV: DMA-level Power BI dashboard under development to address CEL Q1 softness; new feasibility flags and NPS analyses being tested; cross-team validation in progress; data hygiene fixes underway.

Customer Lifetime Value (CLV)

DMA-level CLV dashboard and demand diagnostics (CEL Q1 focus)

In progress

Building a Power BI dashboard with DMA-level cuts, aggregating by cabin class, meta product, and booking-to-sail window.

Targeting fertile DMAs based on feasibility, penetration, NPS, income, value indices, and volume.

New analyses:

Fly/drive flag to assess feasibility by flight frequency, pricing, and distance.

“Price of living” filter to explore relationships with NPS.

Data validation and hygiene

Coordinating with eCommerce, OBR, and Revenue teams to validate counts of pax, bookings, and PCDs.

Fixing cruise_experience columns curated by brand and segmented journeys.

Next

Complete validations; finalize dashboard visuals/filters; prep recommendations for CEL Q1 targeting.

Dependencies/Asks

Timely validation from eCommerce, OBR, and Revenue on pax/booking/PCD counts.

Ben & Carlos

E-Commerce: Customer Targeting

LLM-driven feature engineering research completed in dev; features added to store; early evaluation is promising.

LLM-augmented marketing models

Completed/In progress

Researched use of LLMs’ intrinsic domain knowledge to improve models.

Added LLM-suggested engineered features to the existing marketing feature store (dev).

Evaluated initial results; early performance is promising.

Next

Continue evaluation and readiness assessment for downstream testing/operationalization in alignment with model governance.

Dependencies/Asks

None at this time.

Doug

CEL Revenue Management

**DUAL | Inventory Optimization Opportunities**

**CEL | Groups Berthing Xfer to Databricks**

**Completed:**

Price Upload Refactor – closed early October.

Data Quality Review – partial work done; next meeting scheduled.

Doug

CEL Revenue Management

**In Progress:**

**Groups Berthing Transfer to Databricks** – blocked pending Eswar’s return.

**Upcoming:**

**Dual Inventory Optimization** – reduced scope to 5 points; meeting with Kevin next week to strategize.

New ticket for Celebrity Alaska Open Jaw “Good Side/Bad Side” refinement.

Michelle

RCI Revenue Management

**DART | GTY-LEAD 2.0**

- Deploying to production for RCI today.

GTY-LEAD models predict trade up behavior at a meta, cat-class, wts level. Individual sailing demand varies due to more granular characteristics such as capacity, ship, time of year, or unexpected demand coming in such as groups. The DART layer analyzes the booking behavior at a sailing level, calculates the differences between the predicted and actual trade ups, and adjusts the model predictions for the next weeks.

DART is adjusting the optimal gaps for about 64% of RCI sailings. This leads to enhanced predictive modeling with recent booking data. With the added DART logic, the recommended optimal gaps have lowered about 2% to account for this missed demand.

Michelle

CE Revenue Management

**DART | GTY-LEAD 2.0**

- Awaiting final approval from product managers for CEL. Anastasia and team have reviewed and approved DART logic and gap adjustments. Testing in qa and ready to deploy. There is also an issue in qa with the TAP pipeline where a redeployment of the optimization flow caused an error due to a platform access. Eswar raised a ticket and is helping to resolve the issue

GTY-LEAD models predict trade up behavior at a meta, cat-class, wts level. Individual sailing demand varies due to more granular characteristics such as capacity, ship, time of year, or unexpected demand coming in such as groups. The DART layer analyzes the booking behavior at a sailing level, calculates the differences between the predicted and actual trade ups, and adjusts the model predictions for the next weeks.

DART is adjusting the optimal gaps for about 56% of CEL sailings. This leads to enhanced predictive modeling with recent booking data. For example, for CEL's Asia sailings, the model was consistently overpredicting tradeup. With the added DART logic, the recommended optimal gaps have lowered about 2% to account for this missed demand.

Michelle

RCI Revenue management

**GTY-LEAD 3.0**

- Created DART framework for CEL 3.0 models. Created updated datasets of actual performance for each of the three tradeups at their respective gaps. Used 3.0 models to predict on those cases and calculated residuals to assess weak points of the models. Found consistent over predictions of tradeup, specifically in EG Short Caribbean for the lower-upper tier tradeup and SL Alaska for the upper-premium tradeup. Currently adjusting models to improve accuracy and output valid demand values for the gap optimizations.

Lamis

RCI Revenue Management

**Weekly Booking Demand Estimation Framework**

**Objective:**
Estimate upper bounds on weekly bookings by aggregating demand across similar sailings.

**Methodology:**

**Customer Choice Context:**

Each week-of-year (WOY), customers choose among sailings that match their search criteria:

Same meta_product_code, cat_class, sail_month, and sail_year.

Future enhancement: incorporate web behavior data.

**Demand Aggregation Logic:**

For each WOY, identify all sailings accepting bookings.

Map each sailing to its corresponding **Weeks to Sail (WTS)**.

Aggregate total **new bookings** across these sailings to estimate shared demand.

**Visualization Example:**

Shared for sailings in **March 2025**:

7N, EUROPE, MEXICO, SHORT CARIBBEAN - B

**Booking Bounds – CEL Data Summary**

Bounds generated using:

**new_bk_bkg**: total bookings over 5 weeks → optimization should track every 5 weeks.

**lam**: weekly average bookings → supports weekly granularity.

Both bounds are calculated; granularity preference to be finalized with stakeholders Monday

Lekha

CEL Revenue Management

**CEL | Reporting Work to show the impact of new features on the model OCT**

**Model Enhancement Summary:**

**Feature Analysis:** Created feature-importance heatmaps to show how the new features influence demand prediction.

**Model Comparison:** Built Databricks dashboards to compare metrics between current and improved models, segmented by meta_product_code.

**Error Evaluation:** Assessed error metrics across configurations:

With/without dynamic "weeks to sail" binning

With/without price transformation

Using current vs. new feature sets

**Validation & Reporting:** Used backtesting framework to validate improvements. Stored per-meta_product_code summary metrics in Hive metastore for reporting to Anastasia and team.

**Model Expansion:** Included catclass D in the upgraded model to enable elasticity estimates for the suite category.

**Outcome:** Presented results to Anastasia and team—approved. All meta_product_codes improved except **Short Caribbean**, which showed no gain.

**Next Steps:**

Investigate Short Caribbean performance issue and identify remediation.

Retrain model using **2024 data only** (excluding 2023) per Anastasia’s recommendation.

Re-evaluate metrics to confirm improvements.

Aagam

**CEL | MTRB Pipeline Updates**

**Status: Closed on 10/08/2025**

Updated the base table to read off the new table that was created in  , and bug fixes identified during QA as follows:

stop overwriting sailing baskets

Ensuring the MTRB Process runs on the quarterly MTRB table with the latest date

Fixed the datetime issue

CEL | MTRB Updates | Sharepoint + PROD

**Status:** Ticket closed as of 10/03/2025
**Summary:**

**Eswar:** Successfully pushed MTRB basket changes to production.

**Aagam Shah:** Initially faced a QA failure due to a missing table in the expected environment. After investigation, resolved the issue by coordinating with the business team to ensure proper table setup. Also implemented a SharePoint-based Excel file system for analysts to update data, which his process now reads from directly for efficient updates.

Atefeh

RCI Revenue management: PRE

**PRE 4.0 Model Deployment**

Tested in DEV and QA; fixed code errors and prepared pipeline for production.

Deployed and began monitoring outputs for flagged recommendations.

Atefeh

RCI Revenue management: PRE

**Flagged Recommendations – Root Cause**

Identified occupancy split issues due to how tracks are built (quads first, doubles as remainder).

Example: IC 05/30/26 Balcony Doubles track = 0 due to curve adjustments.

Atefeh

RCI Revenue management: PRE

**Logic Fix for Zero Tracks**

Implemented PRE fallback logic to use most recent non-zero track (e.g., WTS = 13 or 14) when current track = 0.

Ensures PRE recommendations are still generated.

Atefeh

RCI Revenue management: PRE

**VPS Dataset Enhancement**

Started integrating occupancy data into VPS to enable occupancy-level training and recommendations.

Ignacio

PCP Pricing Automation

**1. Splunk Training & Dashboard Access**

**Training Completed**: Required Splunk training has been successfully completed.

**Next Step**: Awaiting approval for dashboard access to monitor errors from automated promo uploads. This approval is critical to ensure that promotions/pricing writeback is robust.

Ignacio

PCP Pricing Automation

**2. Automated Promo Uploads – Workflow Enhancements**

**New Condition Added**: *Qualifying Group Types* condition (especially useful for dining promos) was added to:

The SharePoint-driven spreadsheet format.

The code logic for promo rule processing.

The Hybris promo extraction logic.

**Bug Fixes**: Corrected string cleaning issues affecting *LOYALTY* and *CASINO* conditions.

**Status**: All changes were QA tested and deployed to production.

**Ignacio**

**PCP Pricing Automation**

**3. Promo Upload Testing (Hybris Extracts)**

**QA Environment Limitations**:

QA lacks full production data (e.g., sailings, product codes), requiring filtered testing.

Example: Only AL & EG ships with Sunday sailings in the near future were used.

**Testing Strategy**:

Collaborated with OBR and digital/product teams.

Decided to test only available data in QA, ensuring each condition is tested in some form.

Digital team provided clarity on which condition values are testable in QA.

**Validation**:

Automated uploads using the SharePoint format were successfully tested in QA.

Validated by the digital team to ensure correct promo publishing.

**Next Step**: Ready for P2-level implementation in production (Preview mode).

Kevin

Loyalty

Rough timeline socialized with Lauren and Dhanita, showing best case scenario for simulator updates. First simulator intermediate data expected monday morning. This is the base data before the tier calculator that assigns guests to future sailings. To be validated in collaboration with Dhanita's team, while Kartik works on the tier calculator for preferred points.

Kartik

Kartik proposed points conversion logic and shared with the business.

Loyalty

**Completed:**

Choice Benefits Pilot investigation closed early October.

Preferred Point Selection ticket closed after meeting with Loyalty team.

**In Progress:**

Monitoring ticket for October – ongoing updates expected.

Simulator work for Preferred Points – started, may require subtask breakdown.

Jesse

SSC Revenue management

**PRE Validation**

1. Solved PRE Validation Error 7, the most significant source of remaining SSC Reservation system rejections of PRE price recommendations. Rule 7 dictates that cabin category prices follow an ordered price hierarchy inside the reservation system. Price recommendation rejections, originating from pause file and business rules (e.g., PRE excludes upper category codes), created category code inversions within voyage farecodes. Our new solution, entails raising or lowering all prices for a given voyage + farecode price grouping. Should Revenue managers reject a cabin category price recommendation through the pause file, that cabin category will still be raised/lowered by the same magnitude as the accepted price recommendation from the highest cabin category below the rejected recommendation. The same logic applies for UPPER category codes (e.g., suites). SSC Revenue Teams agreed to this change.

2. Investigated PRE validation Error 8. Although not as significant as error 7, this validation error impacts discounted farecodes TA and T5. I discovered that price recommendations for these farecodes re-arrange themselves for UPPER cabin category codes. I am currently determining an appropriate solution. Once a viable solution is found, I will seek stakeholder buyin.
