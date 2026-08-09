Erick

Medallia (Axiom)

No Major updates, but working on several deliverables that are due through Q4.

- "Voice of Detractor" report template due end of October which is a fast turn around report sent 36 hours after return date summarizing all 0-6 (detractor) comments.

- Royal and Celebrity shipboard & shoreside.

- Drivers/Thresholds model due end of November.

- Stakeholder is Kristina and Eliana.

- Division level reports due in December.

- Stakeholder is Raimund, Gang, Alessio, shipboard, and shoreside audiences.

Erick and Christian

PCP Product Recommendations: Mycruise Recommender

Held a stakeholder meeting with the onboard revenue with highly positive feedback. *3/5 core recommender models (+ variations) have been** **tested** by Digital** (Customers Also, Viewed, Bought, and Added).*​ Use cases are rolling out through end of 2025.​

+ $5M-$15M p.a initial CAR projection​ for the recommenders

+$8M p.a delivered against initial CAR as of Sept 2025 ​

- Calendar recommender due end of November. The Calendar recommender will find available spots in a guests itinerary and use our AI Recommendations to effortlessly fill planning gaps—creating a more enjoyable and memorable vacation experience for every guest.​

- The big push will be to either:

(a) incorporate a backend db alongside our API to handle a broader range of recommendations

(b) provision a new API endpoint alongside the existing endpoint

- Requirements are still being finalized with DS having several questions/doubts that need to be answered by digital engineering

- Follow up session scheduled for Tuesday October 7th.

Erick & Parimala

Contact Center

CTI Lead Prioritization Model:  Celebrity model needs to be revised and improved.

Glen-Erik & Alejandro

PROPEL

presented to the business a clear framework and comparison of how Propel measurements would work with stronger statistical grounding, improved variability handling, and greater flexibility.

Aligned on a 1:1 development strategy for Propel while awaiting CAR approval for Pre-Cruise.

Proposed a future vision for the MyCruise recommendations API with a more fault-tolerant, high-availability architecture.

Helped identify improvements in photo service promotions, enhancing offer coverage and consistency.

Completed tagging of all Propel resources in both dev and prd environments for better governance and cost tracking.

Glen-Erik and Eswar

RCI Revenue Management: RMA:

Reviewed and updated OBR_fs_GENERATE, OBR_fs_UPDATE, GTY_La Optimizaion ,ssc_pre_monday workflows and productionizing them.

Workflow Quarterly_MTRB_update workflow is in QA pending testing.

Debugging GTY_lead_optimization project and MTRB project in setting up relative paths. There were external paths before which caused failures.

Re-configured Databricks connection to Power BI and changed connection from All purpose compute to Serverless compute which resulted in faster loadings for team RCI.

Handover of the SPI Track outputs to RCI team, to adjust track for year 2026 based on the understanding gaps.

PRE pricing algorithm updates debug in QA, helping team in fixing things, tastings. There were issues with Mlflow versions, plot's generation, data type mismatches.

Shut down Revenue Solutions ADF, both dev and prod eliminating  unnecessary jobs using 160hrs worth of compute clusters per month.

Ayon, Eswar, Glen-Erik

WoW: Environment Separation

WOW - Finished parameterizing the catalog, pending testing and monitoring in prod. This will be necessary to separate production and development work into distinct, sandboxed environments.

Ben, Eswar, Glen-Erik

IBP Supply Chain: Environment Separation

Refined plan to revive the prd-da2i-customersolutions-adf and will send the plan and necessary steps to the DS team for action.

Ben & Camila

**Supply Chain**

**Progress & Updates:**

Advanced development of next-gen tri-branded demand models for Hotel, Food & Beverage using enhanced feature engineering via Cursor.

Validated Silversea’s September consumption data post-voyage; initial concerns about missing data were resolved after deep validation.

Created min/max par level dataset for Medical using daily voyage demand; further logic updates pending based on feedback from Yan.

Refreshed SharePoint files into Azure Blob Storage via a newly built notebook.

Identified and escalated a refresh issue in the medical consumption model (last updated 2025-08-21); DE team is redeploying.

Updated logic for Transfer Order Port Location to ensure correct quantity capture.

Fixed aggregation issue in uniform models caused by a missing column.

Added Uniforms Version 5 to IBP data extracts and adjusted related tables.

Detected inconsistencies in Silversea itinerary data—duplicate port entries due to lack of docking filters.

**Pending Tasks:**

Add price columns to RCI/CCI order creation and Min/Max Par tables.

Carlos

**E-Commerce**

**Progress & Updates:**

Resolved out-of-memory issue in production inference pipeline.

Ingested latest TX Spend and Epsilon demographic snapshot data. This is key for keeping our models attuned to any shifts in demographic or spend data from our third-party vendor.

Generated and shared report on itinerary recommender data impact with stakeholders.

Initiated research on leveraging LLMs for feature combination/mix.

Cihan

**Digital**** App**

**App Reviews (Jaime Stoelar):**

Kicked off Qualtrics surveys project; discussed next steps and implementation.

Fixed bug in topic classification agent.

**Pending:**

Develop initial topics for Qualtrics surveys.

**Guest Services Chatbot (Eunha Kim):**

Pending update to dashboard color scheme to align with Royal Caribbean branding.

Ben

**Contact Center**

**Omni Channel ****Infrastructure****:**

Alper, Henry, Ben and Saleforce team had a good call exploring their Data Cloud product and how it can connect to hundreds of different data sources to provide a unified view of the customer and also a singular view of the customer (eliminating duplicate customer records). Alper requested a second call from Salesforce, which will happen in 2 weeks.

Mirielle

**Contact Center**

**Weekly Report – LP OFTOCX:**

Completed feature engineering for Royal and Celebrity.

Ongoing modeling efforts for Royal and Celebrity.

Currently evaluating ML algorithms for lead conversion prediction:

Random Forest

Gradient Boosting

XGBoost

CatBoost

LightGBM

Expecting delivery within the next 1-2 months.

Ben & Caleb

**Customer Lifetime Value (CLV)**

**Completed:**

Developed long-term strategy for CLV integration across departments.

Presented cobranded credit card analysis comparing cardholders vs. non-cardholders.

Delivered insights via cruise experience and card status flag plots:

Example: Avid cruisers represent 3% of RCI’s population but 33% of cardholders.

Ben & Caleb

**Customer Lifetime Value (CLV)**

**In Progress:**

Building Power BI dashboard with DMA-level cuts by cabin class, meta product, and booking-to-sail window to address CEL Q1 demand softness.

Restructuring logic for RCI’s cruise experience column and indirect cost logic.

Integrating Austin’s CASINO_VIP_FLAG to validate and realign casino population value index.

Expanding DMA analysis with additional Air data.

Ayon

WOW weekly Report Summary - 10/2/2025:

Added JohnnyRockets profit center to the pipeline for the following ships: EX, AD, OA, NV, LB, ID, AL, FR, MA, AN, SY, HM, WN, UT.

Currently developing integration of GioWineBar profit center for ships: WN, ST, OY, IC, UT.

Deployed a hotfix to the specialty rules engine to enable dynamic selection of the optimal prediction model (stacked, xDining, or POS) based on proximity to the last seven days' consumption within a 0.5 standard deviation threshold and tolerance factor; this enhancement is currently under testing to validate improved forecast precision.

Developing three automated test cases based on historical support requests to enhance deployment reliability and extending deployment support to chefs to ensure smooth adoption.

Kevin

RCI Revenue Management: SPI

Created a first pass of a refactored SPI scoring model to reduce overfitting concerns in collaboration with strategy teams. Introduced booked position checkpoints into SPI yield model to be used in "better targets" benefits and measurements.

Kevin

Loyalty

Pilot analysis is being deprioritized to focus on refactoring the simulator from the original spend based design to support preferred point selection at the request of loyalty teams. The simulator will be used to help the Loyalty teams move more aggressively in planning the next phase of Loyalty redesign after taking into account recent EC feedback.

Doug

**RCI**** Revenue Management**** | PRE Ongoing removal of copy data**

**Technical Work Completed**

**PL3 (Australia & non-Australia):**

Defined schema to read from Unity Catalog (UC) for PRE input.Updated references from ADLS to UC for pre_archive reads.Updated pre_exception appends to read category_mapping from UC.

**category_mapping**** Table:**

Successfully copied to Unity Catalog to eliminate ADLS dependency.

**Validation:**

Confirmed that new table replacements produce results equivalent to the previous setup.

Doug

**RCI**** Revenue Management**** | ADA Event Driven Berthing**

**Scope:** Defined and aligned on data and logging responsibilities for on-demand ADA berthing.

**Next Step:** Meeting with Data Engineering to finalize coding, testing, and October deployment.

**Key Outcomes**

**On-Demand**** Berthing:**

Writes to a daily table; scheduled job processes and clears it.

No logging to ensure performance; exceptions reported via Teams.

**Testing Plan:**

Manual production testing approved with triggers paused.

**Automation:**

Reporting bot deployed to Teams; runs twice daily (7:45 AM, 3:45 PM).

Michelle

**RCI**** Revenue Management**** | Model 2.0 Performance Analysis**

Status: This ticket is complete as of 9/25/2025

**Deliverables:**

Gathered data on actual sailing performance to compare prices applied, gty-lead trade up behavior, and booking shares across all weeks. Ran predictions on all sailing with current 2.0 models at the actual prices implemented. Compared predicted and actual trade up each week. Calculated residuals and weighted moving average for the past five weeks where the most recent WTS are more significant.

**Michelle**

**CEL | DART Integration**

Status: This ticket is complete as of 2/29/2025

**Deliverables:**

Incorporated DART into 2.0 models and currently reviewing with business. Taking performance from up to the past 8 weeks into consideration for residuals. Awaiting final approval for push to production.

**Michelle**

**RCI | DART Integration**

Status: This ticket is complete as of 2/29/2025

**Deliverables:**

Incorporated DART into 2.0 models and currently reviewing with business. Taking performance from up to the past 8 weeks into consideration for residuals. Awaiting final approval for push to production.

Lamis:

**RCI ****Revenue Management ****- Develop a Linear Optimization Model to decide prices for PRE4.0 as an alternative to using point elasticity**

**Scope:** Ran pricing optimization on select sailings across 4 core meta products.

**Deliverables:**

Visual comparisons of current pricing (with/without norm_const) vs. optimal solution.

Tested multiple price capping scenarios.

Identified improvement opportunities for future iterations.

**Next Steps:**

Additional tasks to be scoped in October for **CEL** and potentially **RCI**, pending stakeholder direction post-meeting.

For context, the Linear Optimization model may be the second most important update to the PRE this year outside the elasticity model upgrade. This update should reduce unrealistic price changes arising due to using point elasticity approximations for the PRE price change, instead of directly solving for the right price change using the elasticity model with a Linear Optimization model

**Atefeh**

**Elasticity Model Enhancements & QA Complete**

**Model Improvements:**

Implemented **variable norm logic** in the pricing notebook.

Compared **Version 3.0 vs. 4.0** elasticity models across signed track variance buckets (−100 to +100+).

Evaluated **constant norm**, **no norm**, and **variable norm** strategies.

**Issue Diagnosis****:**

Identified and analyzed unexpected pricing behavior in Elasticity Version 4.0 model.

Flagged positive elasticity values to Lamis for correction.

**QA & Deployment:**

Successfully tested Elasticity 4.0 pipeline in QA and integrated into PRE.

Fixed code errors and received stakeholder approval for **PROD deployment**.

Ignacio

PCP Pricing Automation

**Feature Store Enhancements**

**Alaska ****ShoreX**** Products:**
Added top 80% of Alaska ShoreX product codes (both brands) to the OBR feature store. Fixed a file-naming issue in the daily update query. QA passed; ready for production deployment.

**Beverage Package Optimization Fix:**
Resolved missing outputs by switching from UPDATE to CREATE OR REPLACE logic in the feature store query. Updated workflows and notified ML Engineering to shift from UPDATE to GENERATE process in production.

Ignacio

PCP Pricing Automation

**Promo Upload Automation Testing**

**SharePoint-Driven Uploads:**
Initiated lower environment testing for OBR-led promo uploads via SharePoint. Reverse-engineered Hybris promos for reupload testing. Identified and escalated errors for joint investigation with Digital and DE teams.

**Production Readiness Improvements:**
Split SharePoint inputs into separate RCI and CEL spreadsheets. Validated multi-select dropdown functionality for OBR team inputs.

**Concerns:**

There are some concerns that the Digital teams may be delayed to end of month in providing the Data Science & Onboard Revenue teams access to writeback capabilities in prod to validate if the pricing/promotional writeback capabilities work across diverse conditions.

The fundamental challenge is that testing in the lower DEV/QA environments does not include the full diversity of the data in production, and the onboard revenue teams are concerned to go-live without Data Science team rigorously testing the writeback capabilities with Digital.

The concern here is that if testing in Prod takes place in November, we may not go live with automation until after Black Friday.

Kartik & Kevin

**LOYALTY | Choice benefits |Initial analysis of control bookings and treatment bookings**

**Status**: This ticket is complete as of **09/30/2025**

**Deliverables**:

This ticket was for the choice benefits loyalty pilot. That involved building the test and control set for the A/B test, Ad hoc investigative work for when faced with issues, and monitoring the bookings coming through and choice benefits seen.

Kartik & Kevin

**LOYALTY | Spend to Save Additional Analysis**

Status: This ticket is complete as of 09/30/2025

**Deliverables:**

Completed analysis on the new sailings that were completed from the spend to save pilot. Saw not much difference from the other sailings. Pulled latest FCC data and performed analysis on net new bookings from the test and presented to SteerCo. Verified OBS data coming through, and there are still small issues but major OBR areas are close to the EOV report

Jesse

SSC Revenue Management

**PRE Pause**** File**

Added past price and implementation date of the current price to PRE pause file. SSC Revenue teams requested this information to help them make better-informed decisions about accepting/rejecting price points. Previously SSC Revenue teams had to look up these prices prior to their decision. While this addition required an additional input table to PRE, it will save Revenue Teams many hours of tedious work.

Added 3-week booking window business rule. This business rule was formerly agreed upon by SSC Revenue and Data Science teams, but implementation was problematic. Building off item # 1, Data Science upgraded BRE business rules to ensure that a price point can only receive one recommendation every 18 days (there is a 203 day lag between PRE and Reservation System). This business rule assists SSC Product teams in two ways:

Reduces the size of the pause file by filtering out non-qualified pricing recommendations

Prevents SSC Revenue teams from having to look up price points to ensure they weren’t change in three weeks, either manually or by way of PRE

Increases comradery between Data Science and SSC Revenue Teams

Jesse

SSC Revenue Management

**PRE Validation**

Repaired “Data Leakage” in PRE upload file (Validation Rule 1.2). PRE price recommendations must be uploaded to SSC Reservation System. To upload successfully, all price points, grouped within farecodes, currencies, and voyage numbers, must conform to a set of validation rules. Validation Rule 1.2 stipulates that **all price points **must be available within a farecode, currency, and voyage grouping for any price point to upload onto reservation system. Data Science repaired all errors in PRE’s upload stage. Now, all farecode, currency, and voyage combinations are available, ensuring that no price points are rejected because of missing data. Ensuring the presence of all data further opens the door to fixing other validation errors, as we can diagnose their cause correctly.
