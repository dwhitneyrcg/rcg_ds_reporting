Ayon Ghosh

Win on Waste:

Explored data, conducted tests, and initiated development to incorporate Transatlantic, charter, and repositioning voyages into the WOW forecast.

Development in progress for reporting on the most frequently asked questions by chefs to support the Mainalla support team effectively.

Working on modeling and forecasting future xDining guest counts for venues supported by xDining data.

Implemented hotfixes to include voyage departure date in the cold start orchestrator, enabling grouping of guest counts and kids by voyage departure date to prevent duplicates in Couchbase.

Mert

MIAP

Enhanced the digital twin model API: migrated it to a standalone Python package and implemented voyage-summary functionality.

Migrated the MIAP API from Flask to FastAPI to support streaming and asynchronous operations.

Attended the annual Decarbonization workshop with the GMO and Newbuild Maritime Technology teams. Discussed MIAP Phase 5 and 6 funding via newbuilds. Agreed to add funds to each upcoming newbuild after 2027 to support and recapitalize the existing team; further approvals and alignment are needed.

Met with the IT Shipboard Product team to discuss a potential PoC for a CCTV camera in-house computer-vision people counter running onboard MIAP servers.

Implemented logging for the MIAP API.

Arya

MIAP

Added utopia to AHU, chiller, HVAC, OFB, hotel, etc.

Created a job to pull risk management data from SharePoint directly into Databricks.

Mahshad

MIAP

Investigated deviations for IN, SM, and IC. For IC, the absorption chillers are back online, so the deviation should be resolved.

Worked on models and baselines for HVAC, hotel, and machinery.

Obtained a Gurobi license; will migrate code from OR-Tools to Gurobi.

Reza

MIAP

Tuned propulsion hull performance and degradation models. Ran a fixed-period hyperparameter grid search on the DynamicSGDModel (tuning initial_alpha, learning rate, lookback window, and epochs) using an SGD optimizer inside the OnlineResidualBoostingModel + DynaTorch pipeline; evaluated performance with SMAPE.

During tuning found hyperparameter combinations that prevented dynamic scaling from being applied. To mitigate this, I logged SMAPE and model outputs, changed initial values, clamped alpha, and reduced the learning-rate and epoch settings for final runs to ensure reliable dynamic predictions.

Identified an unbalanced-data issue in propulsion hull performance and degradation datasets that caused poor model performance. Fixed it by applying filters and balancing the training data.

Debugged the digital twin: implemented a new get-data function to work inside Databricks and fixed bugs caused by typos.

Evaluated the performance of new fuel-forecast models and compared them to the previous model. Studied the differences and developed hypotheses to further improve performance.

Will

MIAP

Completed FACTS 2.0 ETL.

Fixed a path error in the power-plant workflow.

Identified a solution for an issue in the rcg-marineanalytics MLflow module that caused production failures.

Identified a solution to a PAT issue that caused the miap-api release pipeline to fail.

Helped Arya develop a new GMO SharePoint workflow.

Coordinated with the Decarbonization team to identify and fix a failure in the production workflow.

Added FACTS 2.0 data to the common features table to enable verification of model predictions against actuals during training.

Added voyage-phase timestamps to the FACTS 2.0 table.

Added local-port UTC conversion offset to the FACTS 2.0 table.

Erick

**Project Axiom**

Project Axiom refers to a set of capabilities designed to be applied across various datasets such as Medallia Survey responses, Guest Logs, call center transcripts, call center IVR survey data, Qualtrics, etc. The core capabilities include: (1) Meta data extraction which is the process of converting unstructured data into structured data. (2) Reporting capabilities which encompass email alerts, web applications, dashboards, etc. (3) Modeling efforts include identifying NPS Drivers, setting targets, clustering text embeddings, etc.

Erick

**Project Axiom**

**Meta Data Extraction**

The Medallia survey has +40 questions of which about ~25 are numeric (0-10) questions and ~15 open ended questions. We currently fit the 15 open ended questions into 39 topic areas. However the business has asked to create new topic areas that match the 25 numeric fields. For example "Staffs ability to resolve issues" is a numeric field and the business wants us to label Medallia comments with these topics in addition to the 39 topic areas.

Following last weeks update on the new topic areas that the business wants us to track - we are testing our new Data Extraction framework. The framework has several benefits:

Most importantly this is a generalized framework designed to be reused for meta data extraction across ALL of our use cases.

The framework is modular in several directions

flexible use of various models, model parameters

We use LLM judges in Databricks to assess the quality of our meta data.

The framework uses pydantic to properly map the API response to an expected schema format.

The framework uses the latest OpenAI Async client implementation allowing for the fastest possible API call pattern.

The framework is functional. The team is now optimizing the framework for compute time and cost. With the current implementation the team found that a single day of sailings costs about $5 and about 30 minutes to process.

The framework is going to backfill 1 weeks worth of data. The new contractor starting on Monday will be assigned to start working on the downstream reporting for the business.

Erick

**Project Axiom**

**Reporting**

This week we went live with a new email template focusing on negative feedback received with 36-48 hours of sailing return date.

As of Wednesday this week the entire Royal fleet is receiving our GenAI emails including hotel director, guest services manager, cruise director, food & beverage director, marketing & revenue manager, and executive housekeeper, etc.

Erick

**Project Axiom**

**Modeling**

Delivered feature importances to RCI Consumer Insights related to NPS drivers for families and non families.

Working on delivering feature importances to CEL Consumer Insights related to couples above the age of 45.

Erick

**PCP**** Product ****Recomme****ndations (****MyCruise****)**

Calendar Recommendation engine is functional in Databricks and has been deployed to dev model serving endpoint. This latest version of the model serving endpoint points at a Postgresql instance in Azure which lays the groundwork to moving away from storing recommendations in memory. However upon testing the deployed endpoint it was found that Azure Postgresql firewall blocks the model serving instance. We will need to work with platform to resolve this issue.

The team is working on properly migrating all production processes to prod environments.

Erick

**PCP**** Product Recommendations (****MyCruise****)**

Royal Caribbean Shore Excursions Recommendation Campaign is going live this week in collaboration with Ecommerce email marketing team. This email curates the *perfect onshore adventures* for each guest using our rich CRM data layers. It dynamically recommends the most popular excursions still available for each port day, and adapts in real time based on any excursions already booked — ensuring guests only see experiences that complement their plans. Our team provides daily Hybris recommendation model imports into Salesforce for the E-Commerce Team to consume for the email.

Cihan

PCP Pricing Automation
Project: OBR Waterpark PRE (Gang Wang)
Completed:
Updated the initial elasticity model and presented to the stakeholder.
Code review completed for the optimization notebook.
In Progress:
Initiated optimization phase for price recommendations; met with Ignacio for an optimization overview.

Cihan

Royal Sales & Trade Team
In Use:
Last year’s clustering algorithm and metrics pipeline remain actively utilized.
Completed:
Met with the team’s new data analyst to review the project end-to-end.

Mirielle

Contact Center: Lead Pipeline (LP OFTOCX)

Ongoing:
Testing the production pipeline from the master branch in both QA and PRD.

Project: Lead Data Pipelines – Agency ID & Phone Suppression Automation
In Progress:
Coordinating with Data Science, Siebel, and Engineering to automate identification/flagging of agency ID and phone-number suppressions; OB Ops continues to insert suppressions in Siebel.
Key enhancement requests:
Suppress leads from Chat agents for two days post-creation where agency numbers start with 0080.
Block leads from the Future Cruise Onboard Team identified by AS400 login IDs beginning with SLOC.
Status:
Shan, Chandra, and teams are identifying relevant columns, implementing code changes, and testing. Update will follow after Siebel review.

Carlos

E-Commerce Customer Targeting
Completed/In Progress:
Fixed training report data-type mismatches; upgraded to latest LightGBM API; refactored distributed data loading into a utilities module.
Monitoring generative-AI features in auto-scheduled production training.
Reviewed Silversea booking propensity models and data (from David Whitney).
Presented progress on days_to_book models.
Provided custom analysis on Celebrity past booking data for Pia Panero and Kristin Villasusa.

Cihan
Royal Community One (Digital)
Project: Qualtrics Survey (Jaime Stoelar)
Completed/In Progress:
Updated topic list and descriptions per stakeholder feedback.
Ran classifier on one month of data.
Running all past 2025 data and preparing model deployment.

Cihan
Royal Community One (Digital)
Project: Guest Services Chatbot (Eunha Kim)
Pending:
Identify the percentage of guests who prefer connecting directly with a live agent instead of using the chatbot.

Ben and Camila
Supply Chain Optimization (IBP)
Project: Finance Tool Validation Dataset
Completed:
Delivered new 2025 Finance Tool dataset (monthly snapshots) to Finance for validating 2025 demand forecast predictions.
Finding: Demand forecast consistently predicts lower than true needs; vs. Celebrity actual spend over 9 months, identified up to $44M cost-reduction opportunities (pending Finance validation). Celebrity-specific value is being calculated. For the Finance Tool for Supply Chain, CEL is definitely the focus since  we're working towards a pilot of Order Creation on 3 CEL ships; however RCI will be included in a subsequent phase.

Ben and Camila
Supply Chain Optimization (IBP)

Project: HF&B Demand Forecasting (RCI/CEL)
In Progress:
Feature selection (five training periods/five holdout sets, cost-based sampling) identified 27 leakage-free features across four of five periods; three overlap with production.
Microcategory demand model built; MdAPE improved to 15.7 vs. 16.2 on the same data compared to production.
Product-level demand model training underway; results expected overnight.

Ben and Camila
Supply Chain Optimization (IBP)
Project: Data & Reporting
Ongoing:
Merging HF&B and CocoCay datasets for unified reporting.
Expanded HF&B RCI/CCI and HF&B SSC pivot tables with additional spend-report columns for Paige’s dashboard.

Ben and Camila
Supply Chain Optimization (IBP)
Project: Uniforms and SSC
In Progress:
Built initial uniforms order-creation table (uniforms v1).
Developed PAR-level uniforms dataset (uniforms v5), standardizing and adjusting consumption using similar product names.
Advanced SSC uniforms crew consumption analysis.

Caleb
Program: Customer Lifetime Value (CLV)
Completed:
Delivered DMA Optimization Tool with dynamic, composite attractiveness scores per DMA to CEL Revenue.
Created and validated the first iteration of a clean analytics table to democratize CLV methodology/data; collaborating with Ben on documentation (origin, meaning, proper usage). Further iterations planned.
In Progress:
Drafting alternative branded cruise experience segmentation logic (e.g., casino, avid, frequent; exploring order and department-specific variants for product vs. revenue).
Initiated work on the forward-looking table (cleaning, feature importance); coordinating with OBR team to acquire 2025 data and specific OBR category spend.

Mirielle

Contact Center: Workforce Planning
Project: North America
Completed:
Investigated September call-volume discrepancy vs. Databricks (prd_silver.mkrpops.v_cms_dsplit_daily_all) with Nico, Augusto, Antonio, and team; root cause: tables stopped refreshing around Sept 30. Antonio’s team (not owners of the original refresh) is creating a new refresh process.
Call Volume Forecast Models (12 LOBs): Reviewed GEM and Groups skill mapping with Darren to align volumes between the Excel report and the app; refactored feature engineering into modular functions for maintainability and scalability.
Provided baseline assumptions table for each LOB; reviewed weekly office-hour grids for each LOB.
Ongoing:
Trend analysis across 12 LOBs to categorize by seasonal patterns, volatility, and growth behaviors.

Databricks apps support on Workforce management project by MLOPs
Pending/Blocker:
Darren Andree’s access permission.

Mirielle
Contact Center: International and Casino App
Completed:
Set up project outline with Nico, Zed, and Xavier; shared sample data.
Designed the app interface starting with historical data display.
Accounted for Royal, Celebrity, and Casino views—each brand shows markets and related LOB components.
Home page overview delivered: dynamic date picker (defaults from available data); four categories (Royal, Celebrity, General, Casino) with distinct colors (Light Blue, Powder Blue, Peach, Thistle); key metrics per category (Total Calls, Avg AHT, Avg Abandon Rate); Casino sub-brands (Royal Casino, Celebrity Casino) shown separately.
Ongoing:
Building the data visualization section to explore/filter by market; display by LOB and date; show call volume, AHT, abandon rate, etc.

Glen-Erik & Eswar

PCP Pricing Automation

Debugging and fixing the workflows which is failing in QA and production

Deployed clear_OBR_SharePoint_promo_price_upload, obr_automated_promo_uploads_SharePoint_driven_CEL, obr_automated_promo_uploads_SharePoint_driven_RCI workflows which are OBR project related

Updated liked service Oracle conections in ADF

Alejandro & Glen_Erik

PROPEL

Uplift model new variables: is_summer, meta_product_code, ship_class_code

BY troubleshooting to generate offers when itinarary missing

Alignment of integration with Hybris to generate offers notifications in the App

Adjustments to alpha package to upload document to RCI sharepoint site

Doug

RCI Revenue Management

**Deliverables:**

Review of reberthing process completed. KPI measurements logical and sound. Findings and recommendations for improving KPI metrics provided to the business.

Delays: None.

Potential future issue: None.

Michelle

**CEL**** Revenue Management: ****Category-Gapping 3.0**** (Optimizing Category Tiers)**

**Issue Identified**: Optimization results misaligned with business logic due to **insufficient data** for certain ships/metas.

**Solution**:

Mapped weak sailings to **other cat-classes or brand-level models**.

Resulted in **stronger predictions** and **adjusted gaps** without needing caps.

**Impact**:

Improved outputs for CEL’s flagged sailings and additional cases found during review.

**Next Step**: Review findings with CEL business team this week for feedback.

Michelle

**RCI**** Revenue Management**** | Category-Gapping 3.0/4.0**

**3.0 Review**:

Analyzed **category stack** across three meta–ship class combinations.

Identified differences in **deployment vs. end-of-sailing pricing** and **category prioritization**.

Will use this logic as foundation for **future validations**.

**4.0 Strategy Shift**:

Moving from **sequential trade-up logic** to **multi-label classification**.

Reflects real-world booking behavior where customers choose from all available categories.

Mirrors website funnel where only trade-up is **you-pick vs. we-pick**.

**Next Step**: Begin testing classification models (e.g., **EBM, XGB**) for category-level recommendations.

Lamis

**RCI**** Revenue Management**** Optimization Validation & Refinement**

**Objective**: Validate optimization results, refine the model, and compare against current PRE logic and actual outcomes.

**Price Change Regulation Scenarios Tested**

**Hard Bounds Enforcement**:

Applied ±50% upper/lower bounds as strict constraints.

Resulted in **price change peaks at the bounds**.

**Penalty-Based Smoothing**:

Penalized large price movements while enforcing bounds.

Produced **smoother curves**, closely matching actual magnitudes.

**Direction of change** still under investigation.

**Freeze Logic**:

Prices frozen when targeted bookings are within ±1 of current.

Reduced **tail-end volatility**.

**Next Steps**: Continue analysis at **sailing–cc–occ level** to determine optimal approach.

**Handling Counter-Intuitive Demand Predictions**

Developed logic to **hold predictions constant** when price increases lead to higher bookings.

Will be validated at **individual sailing level**.

**Model vs. Actual Decision Discrepancies**

Investigating cases where model suggests price changes **outside bounds** or **contrary to actual decisions**.

**Residual-Based Priors**

Created **priors dictionary** at:

**mets****–ship class–cc–sail month–****wts****–occ level**

Used to **adjust predictions** at the **sailing–cc–occ level**.

**Category-Level Pricing Concerns**

Current model applies **fixed ****price**** across all categories** within a class.

Booking adjustments based on **track proportion**, not actual bookings.

E.g., 5 new bookings × 50% track proportion → 2.5 bookings for doubles.

These assumptions are **impacting optimization accuracy**.

**Eddie** is addressing underlying **data issues**.

Lekha

CEL Revenue Management

**SPIKE:CEL**** | Validating the price changes with new model**

**Pricing Notebook Implementation & Investigation**

**Objective**: Update pricing notebook to consume **latest elasticities and predictions** directly from the model output table (not MLflow object).

**Logic Applied**:

Selected rows where read_date = max(read_date) partitioned by (sailing_date, ship_code, cat_class).

Applied **meta filtering** for key regions:

ALASKA, EUROPE, 7N CARIBBEAN, SHORT CARIBBEAN.

Used **MAX_WTS logic** to assign bin_str:

If MAX_WTS > 59 → bin_str = 58–59 for SHORT CARIBBEAN.

Else → bin_str = 79 or '78–79'.

**Output**:

Created new prices_3_0 table containing expected values like price_change, elasticities.

**Blocker Identified**:

In the **business rules notebook**, after reading from pause_para_query, all price changes become **zero**.

Currently investigating root cause with **Eduardo (Celebrity team)**.

Aagam

RCI Revenue Management

**RCI**** | PRE Track Read Logic Analysis**

**Objective**: Evaluate multiple methodologies for reading track data into the RCI PRE to identify the most accurate approach.

**Approach**:

Calculated and compared **price change impact** of each method on **uncapped PRE prices**.

Assessed accuracy and alignment with expected outcomes.

**Outcome**:

Identified the **optimal track read method** based on accuracy and price impact.

Presented findings to **stakeholders** for review, but there was some confusion on some findings where error for RCI is higher than CEL (which we know it is not from prior presentations).

**Next Steps**:

**Refine analysis** based on stakeholder feedback to further improve PRE logic.

Atefeh

CEL Revenue Management

**1. Normalization Constant Testing (Celebrity Track)**

**Objective**: Identify normalization constants that reduce extreme price changes in Celebrity pricing logic.

**Approach**:

Tested norm constants from **5 to 15**, plus a **variable norm** formula.

Defined **track variance %** as:

Bucketed data by variance ranges to assess impact on price change magnitude.

**Findings**:

Higher norm constants **consistently reduced extreme price changes**:

Norm = 5 → 7.61% extreme cases

Norm = 15 → 1.52% extreme cases

Price change distribution shifted toward **milder adjustments**.

CEL team is interested in **adopting variable norm** approach.

**Additional Testing**:

Explored **scaling factors** (2, 5, 8, 10) in variable norm formula.

**Scaling factor = 10** yielded the **least extreme outcomes**.

**Atefeh**

**RCI Revenue Management**

**2. Promotion-Based Price Change Logic**

**Objective**: Integrate active promotions into pricing logic.

**Discussion**:

Evaluated **booking ID vs. pax-level** aggregation.

Chose **pax-level** due to promo code variability within bookings.

**Progress**:

Extracted all promo keys and compiled into a spreadsheet.

Collaborating with **Eddie** to categorize promotions into **hierarchical groups**.

**Status**: Task is **ongoing** due to large volume of promo codes.

**Ignacio**

**PCP Pricing Automation**

**Automated Promo Upload Spreadsheet & OBR Training**

**Meetings Held**:

Walkthrough with **Jimmy and RCI OBR team** on using the spreadsheet for **automated promo uploads**.

Follow-up training with **OBR teams from both brands** to ensure proper usage and understanding.

**Issues Identified & Resolved**:

Spreadsheet safeguards were corrupted due to users not clicking **“Enable Content”** in .xlsm files.

Fixed corrupted logic and finalized spreadsheet for **Black Friday readiness**.

**Enhancements Made**:

Improved **user-friendly design** and **efficiency**.

Updated **code and workflows**:

Brand-specific dropdowns.

Separate job workflows per brand.

**Additional Engagements**:

Met with OBR team to understand **QA process** for promo uploads.

Met with **Jean** to begin planning **mass promo extraction** from Hybris.

Shared existing notebook as a starting point.

**Ignacio**

**PCP**** Pricing Automations**

**Waterpark PRE Modeling & Optimization**

**Collaboration with Cihan**:

Shared expertise on **feature engineering**, **model selection**, **evaluation metrics**, and **MLflow**** logging**.

Supported setup of **optimization routine** using trained model coefficients.

**OBR Team Engagement**:

Presented trained model, elasticity coefficients, demand-price plots, and performance metrics.

Discussed alignment of model outputs with business expectations.

Kevin

RCI Revenue Management

After substantially simplifying the SPI model and adding better feature engineering of categorical features, the SPI model is now performing substantially better. The team is able to predict NTR Yields with a 9% MAPE on a hold-out dataset (2025). This is substantially better than before and there are less concerns on overfitting from the prior SPI model. We will be presenting to stakeholders next week.

Kartik

Loyalty

Continued refinement of points transfer methodology and simulator. Final evaluation on choice benefit pilots.

Jesse

SSC Revenue Management

Developed a **SQL pipeline** for the second portion of the PRE process, executed **Tuesdays post pause file and Revenue team input**.

Pipeline **moves table joins upstream**, removing them from the pre_upload notebook that formats price recommendations for the **SSC Reservation System**.

This restructuring **simplifies the notebook**, enabling future logic enhancements.

Lays foundation to ensure **100% recommendation delivery** to the reservation system (currently at **98% success**).
