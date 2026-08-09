**Erick & ****Garauv**

**Axiom - NPS Driver, Thresholds Analysis**

Both CEL and RCI are asking to revive the target setting model from last year to set targets for 2026.

Additionally, continuing to refine Drivers & Thresholds model. Experimenting with new feature groupings and ship and meta product hybrid models.

Exploratory analysis and documentation of modeling steps

Expanded Medllia training datasets to include data starting from 2015

Ongoing dashboard code review and template updates

**Erick**

**Axiom - Medallia (Post Cruise Summaries)**

Implemented k-means clustering of survey embeddings.

This clustering pipeline allows the user to

select some subset of data such as specific sailings, by topic, demographic, etc.

LLM generates meta data and embeddings to create high level representation of the given subset of customer feedback.

k-means/knn/umap to cluster the data into clear plottable segments and allows user to quickly understand the subtopics within selected text.

using cudf k-means which allows extremely fast clustering of high dimensional data.

this approach be used as either one-off analysis or also integrated into Axiom app for self serve analytics.

Celebrity is expanding the audience for Post Cruise summary emails to include Cornelius Gallagher Jr cgallagher@rccl.com; Jason Montes DeOca jmontesdeoca@celebrity.com; Guillermo Taleno gtaleno@rccl.com; Jonathan Meyer jmeyer@celebrity.com; Kami Dietz kdietz@celebrity.com

Aiming to deliver Division reports be December 15th

**Erick & Parimala**

**Axiom - Guest Logs**

Temporary pause on Guest Logs as the guest logs source data is being migrated to new systems. Aiming to deliver new guest logs pipeline by december and initial reporting in Q1 2026.

**Erick & Parimala**

**CTI Lead Scoring (Royal + Celebrity)**

Experimenting with wide range of new features.

**Erick & Christian**

**MyCruise**** Recommender**

Enabled API recommendation input/output tracking.

Preparing documentation and slides in anticipation of call with Rafael Toro.

Exeperimenting with Postgres/Lakebase as backend data.

Refining the requirements for Calendar recommendations.

**Mert:**

**MIAP**

Wrote the MIAP Phase IV CAR memo and financials; submitted to the GMO/IT finance team for review. Targeting October 20th for CapCom.

Met with the American Bureau of Shipping (ABS) and followed up on the joint development of safety KPIs with leading indicators. Agreed to create a list of potential KPIs and narrow it down to what’s feasible and measurable with MIAP.

Followed up with Asset Management Director Patrick regarding adding an additional Data Scientist via their G&A to support Asset Management initiatives.

Met with the Supply Chain IBP team to identify the approach to start the supply chain optimization project for marine.

Productionizing the development of the RD/ML class power plant optimization package.

**Reza:**

**MIAP**

Completed and delivered the baseline vs. drydock autodetection algorithm for the Energy Management team. Had a meeting with them to discuss deliverables.

Completed the parallel workflow for service power.

Started working on AHU workflows to make them integrated and parallel.

Started a proof of concept for the AHUs drift resistance algorithm.

Made changes to hotel/machinery/HVAC/service power workflows to avoid race conditions on ships using other ships as reference ships.

Added the fail feature to the HVAC workflow.

Helped team members debug deviation issues in service power and issues in common feature calculations.

**Mehdi: **

**MIAP**

Here is my contribution during the past week:

Worked on integrating the regression model with the AI Agent.

Worked on MLflow registration and deployment.

Performed initial EDA on the new build price data.

**Arya:**

**MIAP**

Found issues with service power.

Investigating collision data in the sea events table.

Added and cleaned up safety figures in the GMO web app.

**Mahshad:**

**MIAP**

Worked on IC and NO data issues for calculating ship port.

Worked on optimization mathematical formulation.

Worked on anomalies in the ventilation fan for SM, WN, and SY.

**Will:**

**MIAP**

Fixed issue calculating MGO Equivalent SFOC on IC.

Investigating outliers in IC of the seas data.

Presented the Power Plant part of the Fuel Forecast Project.

Fixed issue affecting the accuracy of GTG models.

**Brendan:**

**MIAP**

Found and deployed a solution for "Concurrent Append" errors we were receiving across multiple MIAP workflows in Databricks. Root cause: too many Spark executors writing to the same table without a partition.

Compiled a list of all MIAP REST API endpoints and example POST requests for the security team for testing purposes.

Tagged all personal and job compute clusters in Databricks for the MIAP project to help with cost tracking and chargeback to CAR from the platform team.

Deployed a new mechanism for workflow failure notifications on partial successes to Hotel and Service Power workflows (already in place for Machinery and HVAC).

Did knowledge transfer of asset bundle parameterization to a developer on the GMO team; provided support for troubleshooting Git merge conflicts and pipeline compilation errors.

Fixed the MIAP cost anomaly detection job and deployed it to production to enable alerts when daily spending goes above the norm. Asked the Capgemini support team to monitor this process in addition to checking MIAP's cost breakdown dashboard in Databricks to ensure we stay on top of fluctuations in compute costs.

Created a query to quantify the cost of all MIAP-related jobs and streaming pipelines in the Data Engineering Databricks workspaces (joint effort with Ram S.); modified the MIAP cost management dashboard to include these costs.

Created a data quality dashboard for MIAP that shows data gaps at the tag level for each ship in the fleet. This will be used for identifying "silent" pipeline failures by locating missing data (joint effort with Ram S.).

**Ayon **

**Win-on-Waste****:**

Integrated new profit centers, "Omakase" and "Hot Pot," into the forecasting pipeline with customized deployment to reflect their applicability across different ships.

Developed and prepared new modifier (add-on) functionality for pipeline integration; unit and integration testing planned for next week to validate stability and performance.

Collaborated with FPMS engineering team to identify and resolve Couchbase write conflicts, successfully preventing overwrite issues and ensuring improved data consistency.

Implemented multiple targeted hotfixes to enhance model forecast accuracy and alignment.

Deployed a hotfix to the MDR rules engine enabling dynamic selection of the optimal prediction model (stacked, Xdining, or POS) based on proximity to the last seven days' consumption within a 0.5 standard deviation threshold and tolerance factor, thereby improving forecast precision.

Glen-Erik

Win-on-Waste:

Environment Separation:

Parameterizing dev/prod catalogs for Win-on-Waste environment,

Wrote queries to surface tables used in the last 30 days to pinpoint key datasets per environment, and consolidating an inventory to improve governance and deployment consistency. This will be critical for maintaining the FPMS forecasting assets that are used for the venue-level forecasting for shipboard chefs.

Operations & bugfixing:

Proposed a solution for Databricks packaging/path issues (copied the wheel to /databricks/driver, installed with %pip --no-deps, restarted Python), clarified set -e and Workspace/DBFS/driver differences, and proposed publishing our package to Azure DevOps Artifacts for reproducible pip install across orchestrators.

**Glen-Erik:**

**IBP Environment Separation:**

Pushed ADF changes to point all databricks notebooks to a user agnostic location instead of a personal repo.

Tested databricks CICD deployment to PROD.

Aligned ADF CICD strategy with Jose from the Platform team to ensure any new best practices from DE are used, nothing new no using same strategy as RMA.

Established plan for reviving the prd-da2i-customersolutions-adf workspace since it hasn't had a deployment since Sept 05, 2024.

Glen-Erik & Brendan:

MIAP

Cost Management:

Tagged all personal and job compute clusters in Databricks for the MIAP Project to help with cost tracking and chargeback to CAR from platform team

Created query to quantify cost of all MIAP-related jobs and streaming pipelines in the Data Engineering Databricks workspaces (joint effort with Ram S.); Modified MIAP cost management dashboard to include these costs.

Fixed MIAP cost anomaly detection job and deployed to production to enable alerts when daily spending goes above the norm. Asked Capgemini support team to monitor this process in addition to checking MIAP's cost breakdown dashboard in Databricks to ensure we are staying on top of fluctuations in compute costs.

Operations, support and bugfixing:

Deployed new mechanism for workflow failure notifications on partial successes to Hotel and Service Power workflows (already in place for Machinery and HVAC)

Did knowledge transfer of asset bundle parameterization to developer on GMO team; provided support for troubleshooting Git merge conflicts and pipeline compilation errors

Created data quality dashboard for MIAP that shows data gaps at the tag level for each ship in the fleet. This will be used for identifying "silent" pipeline failures by way of locating missing data (joint effort with Ram S.)

Found and deployed solution for "Concurrent Append" errors we were receiving across multiple MIAP workflows in Databricks. Root cause: too many Spark executors writing to the same table without a partition.

Compiled list of all MIAP REST API endpoints and example POST requests for the security team for testing purpose

Glen-Erik & Eswar

RMA:

Developed SPI-guided track recommendations for every quarter in 2026 (sailing dates) for FIT track. These results will be used by RCI team in order to forecast demand and adjust prices accordingly.

Moved SPI codebase from feturestore to a separate SPI-dbricks repo. (Productionizing SPI workflows is pending)

Modifications and re-deploying workflows:

ssc_pre_monday, obr_automated_base

Price_uploads_PRE_driven

obr_automated_promo_uploads_SharePoint_driven

obr_automated_promo_uploads_PRE_driven

Glen-Erik & Alejandro

PROPEL

Dynamic offer templates: Received very positive feedback on the first customized offer template for SPA with personalized imaging and formatting. Alex is excited to see this expanded for all other offer categories.

Michelle

**Celebrity ****Revenue Management: ****Category Gapping**
Ticket completed as of 2/23/2025.

Gathered actual sailing performance data to compare applied prices, GTY-lead trade-up behavior, and booking shares across weeks.

Ran predictions using the 2.0 model at actual prices and compared predicted vs. actual trade-up behavior.

Calculated residuals and applied a weighted moving average over the past five weeks, emphasizing recent weeks.

No issues identified; ticket fully closed.

Michelle

**Celebrity ****Revenue Management: **

**Branded Dart Updates**
Work began this week and is progressing well.

Celebrity ticket is nearly complete;

Michelle will provide a descriptive summary of DART work for future planning and reuse.

Michelle

**Celebrity ****Revenue Management: **

**Branded Dart Updates**
Work began this week and is progressing well.

RCI model expected to close by Friday.

Michelle will provide a descriptive summary of DART work for future planning and reuse.

Lamis

**RCI ****Revenue Management **

**PRE 4.0 – Pricing Optimization Model**

Developed a **Linear Programming (LP) formulation** to optimize pricing across sailings. This is really critical and will improve pricing recommendations, making them not as extreme.

Completed a **preliminary run** on sample test sailings including EUOPE/7N/SHORT/ALASKA.

The LP model aims to **minimize the gap between predicted bookings** (from the demand model) and the optimized price point.

Implemented a **Piecewise Linear Approximation (PWL)** to linearize the integration of the demand model: For each week-to-sail (WTS), the model samples demand at various price breakpoints.Between breakpoints, demand is interpolated linearly.The LP activates one segment per WTS and interpolates to find the price point closest to the track ask.

Incorporated **week-to-week price change constraints** (±10%) to ensure smooth transitions.

Adjusted prediction error at the **occupancy level** to improve accuracy.

Generated visuals comparing: Optimal prices vs. elasticity-based calculated prices (p_need) under different dampening constants.

Track ask vs. predicted bookings at optimal price points, highlighting any gaps.

These results will inform future iterations and stakeholder discussions.

Lamis

**RCI ****Revenue Management **

**RCI Track Optimization**

Computed **data-driven bounds** on booked position using mean ± 2 standard deviations at 20 and 40 WTS.

These are interim bounds; future iterations will use more dynamic, data-driven thresholds.

Created visuals comparing:

Optimal track for a sailing vs. historical SPI-based top performers.

Booked positions at 20 and 40 WTS to assess alignment with performance benchmarks.

Found that for some sailings, the optimized track is **closer to top performers** and falls within expected bounds.

Shared findings and representative visuals with stakeholders, and documented results in Jira.

Lekha

CEL Revenue Management

**Elasticity Model Enhancements (Celebrity)**
Ticket completed as of 09/24/2025.

Engineered several new features to improve demand modeling:

**SEASON**: Captures peak and off-peak periods tailored to each meta product (e.g., Caribbean, Alaska, Europe), improving demand representation beyond simple month flags.

**Holiday_Name**: Groups major holidays and adds port-specific effects (e.g., Thanksgiving by origin).

**Sailing_Nights_Groups**: Clusters sail nights with similar demand patterns by meta product and category class.

Implemented a **dynamic binning strategy** that adjusts bin granularity based on demand levels, improving pattern detection and model accuracy.

Enabled **automated binning strategy selection** based on R² performance to ensure optimal fit.

Applied **seasonal price transformations** to normalize and stabilize price features, reducing skewness and improving model sensitivity to nonlinear effects.

These enhancements led to a measurable reduction in median absolute error (0.5–1.5%).

**Sky Suites Elasticity Analysis**
Provided initial support to Eduardo on mapping Sky Suites to Cat Class A.
Full analysis will continue in October following PTO.

Aagam

RCI Revenue Management

**PRE Logic pt 3** Completed presentation and shared analysis with stakeholders.

**PRE Logic pt 4** Began follow-up work analyzing percentage price changes from different track methodologies.Completed comparison of historical RCI sailing prices vs. generated prices.

**RCI Pricing Analysis** Partial September effort; remainder planned for October.Ticket to be split for visibility.

Aagam

CEL Revenue Management

**MTRB Updates** Received correct deployment dates from the business.Will update the table, test in dev and QA, and deploy to production by end of week.

**Basket Analysis** Dependent on MTRB completion; scheduled for October.

Atefeh

RCI Revenue Management

**Track Value Substitution Logic**
Addressed a critical issue in the price equation where zero or null TRACK values caused undefined results. Built a historical TRACK table and implemented logic to replace missing future values with the most recent valid historical entry, ensuring model continuity.

**Historical Price Change Recommendations**
Developed a notebook to replicate PRE’s price-change logic for historical sailings. Outputs are stored for optimization and comparative analysis.

**Exploration of Extreme Price Changes**
Conducted exploratory analysis across multiple scenarios (with/without norm constants, production model).
Investigated how track variance (TRACK – Y_PRED) influences price change behavior.
Created variance buckets and visualized summary statistics to identify patterns driving extreme pricing shifts.

**Production Readiness**
Final validations for price change logic are underway, with expected closure by Tuesday.
Other items, including overfitting mitigation and active promotion logic, are deferred to October.

Jesse

SSC revenue management

**PRE Pricing Table Consolidation & Script Update**
Consolidated multiple pricing inputs into a single, stable configuration for PRE.

Created a new archive table with ordered pricing priorities and a latest pricing table capturing manual updates.

Delivered a master file format supporting voyage, farecode, and category-level configuration.

Began updating the PRE upload script to support the new format and coordinate with Data Engineering for system integration.

Jesse

SSC revenue management

**Farecode**** Unbundling Integration**
Integrated unbundled farecodes into PRE infrastructure and feature store tables.

PRE now supports price recommendations based on S3 farecodes, per SSC product team direction.

Jesse

RCI revenue management

**Booking Behavior Analysis**
Analyzed passenger cancellation and survival rates across 12-week booking windows.

Segmented data by sailing area and booking period to mimic sales funnel dynamics.

Research was stakeholder-driven and presented in a high-level meeting.

Jesse

SSC revenue management

**Guest Eligibility Investigation**
Investigated bookings flagged as ineligible:

Most were linked to guests who received promotional emails.

Identified cases of system gaming and loyalty account mismatches.

Findings will inform improvements to eligibility logic and promotional targeting.

Kartik

Loyalty

**Guest Booking Investigation & Eligibility Analysis**

Completed a deep dive into bookings flagged as ineligible.

Found most cases involved ineligible guests linked to others who received promotional emails.

Identified a few instances of system gaming and loyalty account mismatches.

Findings will inform improvements to eligibility logic and promotional targeting.

Kartik

Loyalty

**OBR Data Verification**
Currently validating newly received OBR data to unlock dependent October tasks.

Verification work will be credited for September.

Kartik

Loyalty

**Benefit Usage Analysis**
Analyzed booking data across brands and menus.

Created visualizations showing **onboard credit** and **drink packages** as the most sought-after benefits.

Insights will support future benefit strategy and personalization efforts.

Ignacio:

PCP Pricing Automation

**SharePoint-Driven Promo Uploads**
Split the original spreadsheet into brand-specific sheets to streamline input and processing. Updated the notebook to handle each brand separately and merge results before API upload.

Ignacio:

PCP Pricing Automation

**Hybris Promo Extraction for OBR Teams**
Automated daily extraction of promos from Hybris into a standardized format. This provides OBR teams with up-to-date reference promos for efficient creation and modification.

Ignacio:

PCP Pricing Automation

**Testing of Price Changes and Promo Uploads**
Conducted additional validation using dummy data to ensure both price changes and promo uploads are functioning correctly. Coordinated with the digital team during testing.

Ignacio:

PCP Pricing Automation

**Beverage Package Optimization – Missing Output Investigation**
Diagnosed missing optimization outputs by analyzing the feature store pipeline.
Found that the update query for the binned feature store was producing faulty data due to zero-filled transactional records.
As a temporary fix, ran the full overwrite query to restore accurate recommendations for the OBR team. Further debugging of the update logic is planned.

Henry Drescher

Contact Center

Conversational IVR

Legacy conversational IVR

Monitoring - ensure the status quo is maintained ie no downed API's, no bad actors, etc.

Insights

was just asked about correlation of conversational IVR and reduction in conversion is an example.

Reviewing PCP analysis with Breanna around routing issues they are seeing.

Migration to copilot

Gap analysis for RCI and CEL - making design decisions based off the fact that copilot and nuance mix have different functionalities and there are limitations in copilot on some items compared to mix.

Infrastructure considerations - working with IT team to ensure infra meets requirements for the application.

Design considerations for reporting on copilot - understanding how the data is logged and how we can setup a framework in designs to automate reporting.

Coordinating setting up ETL pipelines for data feed

Reviewing existing logging structure to understand what is possible with existing system.

General research and learning of copilot studio to ensure when we create designs or make suggestions in aligns to the technology.

Conversations around post go live support structure - RACI diagrams, backup plans, roles and responsibilities, etc.

Post migration support

Coordination of the guest profile API development. - Working with Amit gupta and team to make concessions based off what we want and what is possible.

Designs for guest profile API integration

Authentication

Reservation selection

Self-service reservation details

Loyalty rework based on multiple account returns

Payment intent predictions

Designs for Generative AI for FAQs

Implementation designs

Working with IT on centralized knowledge source through azure ai search (Tagging, structure of data, data sources, etc. )

General coordination of contracts and agreements

HCL Professional service agreement

Extension for migration contract

Stakeholder managements

Answering questions like how is it going, what are the issues, timeline questions, etc.

Henry Drescher

Contact Center

Cresta:

AB test rework

Pilot

Created agent pilot

Due to non conforming of business needs to experiment requirements we created supervisor pilot

Due to data availability issues and non conforming of business needs to experiment requirements we created agent-date pilot

Result analysis for statistical significance and impact

Generation of ROI calculations and overall impact

Data and status report generation for both Cresta and internal stakeholders.

Ongoing efforts

Coordination of Infinity CTI integration efforts

Validation of infinity CTI integration efforts impact

Coordination for new genka solution, ie factoid vs. vague answers and offering articles vs. direct answers and validation of improvements.

Coordination for new auto summary implementation and validation of improvements.

Full rollout

Negotiation of rates for both ongoing software costs and professional services.

Creation of full rollout view, how many use cases, behaviors, etc. based off analysis and product understanding.

Sunset of speech IQ

Assessment of outcoming data structure

Setting up of ETL for data generation

Coordination of project scoping for building out necessary artifacts to replace existing reporting (GenAI behavioral topics)

Understanding the current usage across the org for speech data in reports and adhoc reporting

Experimentation

AI analyst

Unsupervised topic discovery for adhoc questions

Conversion models and correlated insights to conversion models

General training and product learning for full rollout

Coordination to setup the post go live support structure with business, IT and analytics.

Henry Drescher

Contact Center

Other items:

Workforce planning and forecasting

Still consulting on international with Data Science Team

Working to coordinate with enterprise data science for the full rollout

Omnichannel

Assessing vendor vs. internal solutions with IT

CCAS

Consulting on questions for level of effort on certain items for the CCAS switch around analytics, agent assist and conversational IVR

Adhoc speech analytics requests

Requests related to speechIQ data or reporting someone on the team has built.

Ben & Henry

Contact Center

Journey Orchestration and Salesforce Data Cloud

Completed: Held call with Henry, Ben, Utkarsh, and Salesforce after Journey Orchestration meetings; discussed using Salesforce Data Cloud to unify disparate customer data for omnichannel communications.

Mirielle

Contact Center

LP OFTOCX (Royal and Celebrity)

In progress: Feature engineering (ongoing).

Next: Confirm with Augusto whether a subset of lead types is categorized as BKTOCX.

Mirielle

Contact Center

Workforce Planning – Staffing Model Development

In progress: Implement save functionality in the app; add a new section to capture and persist key assumptions (AHT, in-office shrinkage, out-of-office shrinkage, abandon target) in UC.

Completed: Eswar confirms Jason Atkerson has access to the app.

Next: Meet with Jason Atkerson to test app updates; build ETL to refresh data feeding the Main Page and Data Visualization sections.

Ben & Caleb

Customer Lifetime Value (CLV)

Completed

CLV stakeholders and Caleb presented Celebrity CLV to Laura and Michael.

Brainstormed and presented next steps on validating casino populations, product-journey populations, and cross-brand credit-card exploration.

Built visuals: popular product sequences; cohorts and value indexes across sailings; casino populations and flags; credit-card holders and cruise experience; loyalty-status mappings.

Assisted Project Catalyst (Shivani) with data conversions/transformations; loaded Projects, Budgets, Classifications, and more into templates.

Ben & Caleb

- Customer Lifetime Value (CLV)

In progress

Add total value to visuals to provide magnitude context alongside indexes.

Update tables to minimize confounding elements affecting value indexes (same-cabin passengers on the same sailing, sailing-to-sailing spend changes, product differences).

Carlos

E-Commerce Customer Targeting

In progress

EDA on Itinerary Recommender data.

Feature engineering: add market and brand to Itinerary Recommender inputs.

Start consumer-behavior tracking ticket (requirements and data gathering).

Test cursor.ai commands and refactor agent.

Next

Deploy Itinerary Recommender data/results integration to production after validation.

Ben & Camila

Supply Chain

Completed

Authored stakeholder documentation on how Supply Chain reports were created.

SSC Min/Max Par: reconciled average days via alternate source tables for exact-match accuracy; added unit cost and total value columns using last purchase price from consumption data.

Medical Model: completed without error after adding crew count to total passengers.

Finance automation: food, beverage, and consumables categories completed.

Uniform matching runs completed:

Original (normal time range)

PRDS Modified V1 (extreme, first-word matching; ~44 minutes)

PRDS Modified V2 (simple, improved matching; ~2 hours)

PRDS Modified V1 Crew (~6 hours, one step run manually)

Model Results workflow and channel created for faster accuracy answers.

Documentation completed on all uniform versions for Yan.

Warehouse-to-ship mapping built (port code and region by sailing date from warehouse transfer and voyage tables).

Ben & Camila

Supply Chain

In progress

SSC Order Creation Data: added last purchase price by ship and item level; will modify to use spend table and fleet price if ship history is unavailable.

Finance automation for remaining categories pending review with Yan on approach.

Uniform runs still processing: Original Crew (25 hours so far) and PRDS Modified V2 Crew (16 hours so far).

Cihan

PCP Pricing Automation

Revenue Management – Waterpark (Gang & Rafa)

In progress: Feature engineering to improve model performance and predictive accuracy.

Note: Encountered a data issue currently blocking progress; working with Data Engineering and stakeholders to resolve.

Alaska ShoreEx

Completed: Labeled all shore excursions; presented findings to Gang, Alex, and team; met with Kevin to discuss next steps.

Cihan

Digital App

Digital – App Reviews (Jaime Stoelar)

Completed: Met with Chris Sanu to review the notebook; transferred topic-classification ownership to Jaime’s team; provided access for the team to run the notebook in their environment; scheduled meeting with Jaime to begin Qualtrics survey analysis.

Pending: Collaborate with Jaime’s team on Qualtrics surveys.

Digital – Guest Services Chatbot (Eunha Kim)

Completed: Added ST to the Adoption Rate by Stateroom plot; adjusted date intervals for multiple plots to YTD; removed blank filter and limited dashboard to current ships.

Pending: Revise the dashboard color scheme to align with Royal Caribbean brand guidelines.
