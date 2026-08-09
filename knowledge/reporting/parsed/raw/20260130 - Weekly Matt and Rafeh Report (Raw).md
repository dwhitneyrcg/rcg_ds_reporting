**Erick**

**Project Axiom**** (****medallia****)**

*AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.*

**Meta Data Extraction**

**Bullet Points Migration** *(David M.)*: Working to release a revamp of base topic table which powers all Axiom reporting (emails, dashboard, app, etc.). Latest task involved a special prefix logic to assist the LLM with venue level context. Deployment ready with backfill plan to process 2024 data using GPT-4 mini batch processing.

**Guest Logs Classifier** *(David M.)*: Blocked by challenges with unmapped legacy subcategories. Consulting with stakeholder about expanding new schema to improve classification accuracy.

**Meta Data Clustering** *(David M.)*: Created Python class comparing quantized embeddings vs raw embeddings; similar cluster results validate approach.

**Reporting**

**Royal Beach Club Analysis** *(Erick A.)*: Delivered RBC topic analysis report for Consumer Insights team. Insights team will be meeting with Michael Bayley next week. Analysis provides quantifiable, evidence-driven insights for week-over-week tracking of RBC topics. Main concerns are around overcrowding, food quality, and pricing.

**ShoreX**** Safety** *(**Danusio** G.)*: Implementing binary classification (yes/no) report for Legal ShoreX safety report. Analyst in the team (Eduardo) asked to resolve missing survey issue (21 surveys filtered due to comment length) and other minor changes.

**Guest Strategy Email Automation** *(Rodrigo B.)*: Email template for Hotel Operations (Gang Wang) is completed. Gang Wang has a team member going on paternity leave and will need automation to take over the email reporting. Building Databricks job to automate generation and send every Sunday to Maria, Alvaro, Jose, and Erick.

**Royal Beach Club Dashboard** *(Rodrigo B.)*: New dashboard requested by Hotel Operations (Gang Wang) combining port of call dates, pass purchases, revenue, and RBC ratings.

**Power BI Access** *(**Danusio** G., Rodrigo B.)*: Rodrigo successfully set up Power BI. Danusio's Mac OS access issue escalated; VM workaround being arranged.

**Modeling**

**NPS Drivers Model** *(Osvaldo V.)*: Created new API with both Royal and Celebrity model endpoints. Celebrity team demo scheduled for Friday 1/30. Implemented caching and performance optimizations for SHAP computation.

**Weather Correlation Analysis** *(Erick A., Osvaldo V.)*: Completed correlation analysis for Supply Chain team. Weather correlates with seemingly unrelated metrics (Food, Music, etc.) but all correlations are low and below 0.22.

**Project AI Pivot *****(Qualtrics Topic Extraction)***

*Self-labeling framework for automatic topic discovery from survey data.*

**Danusio**** G.**: Implemented guided and semi-supervised methods for Qualtrics. Presenting four incremental approaches with recommendations by Friday.

Cristian & Erick

**PCP Product Recommendations (****MyCruise**** Recommender****)**

*Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app.*

**Recommendations Engine *****(Cristian V.)***

**Apriori**** Expansion**: Calendar staging data deployed. Now extending Apriori to other product categories using unified dataset approach (no port differentiation). We are also discussing internally about reserving two business-defined for promoted products that would be set directly by the business. This would be a happy medium where recommendations are kept intact and business still get control in which products to promote.

**Silversea Integration**: New initiative to explore adding Silversea brand to the existing Recommender Engine. Investigating data availability and requirements.

Ben & Camila

SUPPLY CHAIN IBP

Production orders now auto-generated monthly; <0.1% forecast variance

COMPLETED:

- Team met with Laura Hodges, CEL CEL, to finalize the ‘BY’ pilot plan to use IBP Forecasting to set the budget for CEL Beyond.

- Production Order Creation Datasets: Automated ship/voyage datasets now productionized for monthly pipeline runs

- Finance Tool Dataset Enhancement: DAX calculations moved from PowerBI to data layer

- Inflation Report Automation: SSC and RCI/CEL reports now auto-generate for last, current, and next year (aligned with Yan & Christian)

- Demand Forecast Mapping: Enhanced product mapping with improved aggregations; <0.1% impact on forecast quantities

- SSC Voyage Demand Enhancement: Added full port name child table for Paige's forecast dashboard (Yvonne)

- Spend Report Completion: Resolved all missing regions using pycountry-convert; added local/non-local vendor detection

- Purchase Order Backtesting: Created 1-month lookahead predictions by ship-voyage; uploaded to SharePoint

IN PROGRESS:

- New Ship Automation: Updating consumption threshold from 12 to 3 months post-launch

- Master Order Template: Single-file download vs. 25+ downloads (pending Paige review)

- SharePoint-Azure Pipeline: Enhanced duplicate file detection

- Streamlit App Integration: Databricks connection for automated ship/product selection

- Consolidated Spend Table: Row count reduction via item master list filter (pending Yan review)

Mirielle:

2. CONTACT CENTER - WORKFORCE PLANNING (NORTH AMERICA)

3 core forecasting refinements deployed

FORECASTING MODEL ENHANCEMENTS (12 LOBs):

- Automated Outlier Smoothing: Decomposition-based cleaner removes "freak events" while preserving structural patterns

- Robust Partial-Year Growth: YoY alpha calculation using overlapping months only for accurate growth rates

- Monday-to-Monday Baselines: 364-day lag prioritized over 365-day for smoother baselines

NEXT STEPS:

- Apply refinements to Casino, CO_Sales, and CE_Sales LOBs (>20% deviation in anomaly months)

- Deploy App Version II with 2026 volume visualizations (collaborating with Mukund)

- Scope definition for Celebrity and Unified RCG-Wide Forecasting

Carlos Andarcio

3. E-COMMERCE CUSTOMER TARGETING

Multiple critical bugs resolved

COMPLETED:

- Booking Status Filter: New Streamlit feature for filtering by consumers with/without active bookings

- Pipeline Aggregation: Now aggregates by Market AND booking status for improved accuracy

- Bug Fixes: Resolved multiple issues in Model Insights tab

- Conversion Rate Fix: Corrected targeted offer conversion rate history calculation

- Booking Propensity Report: Feature impact now in %; improved BP personas with expanded top-feature segmentation

- Journey Scoring Model: Reviewed requirements and data availability for new model

NEXT STEPS:

- Databricks Dashboard POC: Evaluating flexibility and performance vs. Streamlit

- ETL Best Practices Review: Scheduling meetings with Carlos

- Data Ingestion Assessment: Investigating tickets and data sources for expansion

Cihan

PCP Pricing Automation

7,000+ shore excursions categorized, which facilitated a conversation of OBR Teams with CEL CEO

ALASKA SHOREX CLASSIFICATION (Gang & Rafa) - COMPLETED:

- Delivered data for Alex Correa's presentation to Laura Hodges

- 7,000+ shore excursions categorized into main/subcategories

- Kevin's notebook visuals validated against source table

- In Progress: Creating SQL queries for Databricks dashboard

GUEST SERVICES CHATBOT (Eunha Kim) - PENDING:

- Stakeholder using sample dataset to identify escalation patterns

- Awaiting insights for escalation type classification

Caleb

5. CUSTOMER LIFETIME VALUE

CEL NY FLY/DRIVE ANALYSIS:

- Met with Alex F. to provide deeper demographic cuts (age, income)

- Analyzed behavioral differences: fly vs. drive guests in subsequent sailings

- Delivered actionable insights for market segmentation

Caleb, Ben, and David

6. CUSTOMER LIFETIME VALUE: DEMAND MODEL (NEW INITIATIVE)

DATA COLLECTION PHASE:

- Data Request Documentation: Comprehensive list created; Jordan contacting relevant teams

- Stakeholder Meetings: Initiated with Consumer Insights, Revenue Planning, Data Analytics

- Revenue Planning Alignment: Agreed on approach using their forecasting revenue models

- Fleet Models Integration: Incorporating deployment/fleet models for competitive breakdown

- Feature Engineering: Ongoing EDA with correlation scores across potential indicators

Mert:

MIAP
Visited Silver Ray with the Energy Management team and presented MIAP solutions.
Presented the Alarms and Events AI Assistant to the Marine Safety team and received positive feedback. Next steps are to use the tool during Lloyd’s Register’s work on reducing alarm fatigue onboard.
Joined the GMO AI/DATA/IT biweekly meeting to review the strategy plan ahead of the GMO senior leadership review.
Met with the Asset Management team to review AI strategy with Brian Sorenen.

Brendan:
MIAP
Updated the MIAP cost management dashboard to fully support environment parameterization (including fixes for forecasting issues).
Added a new visualization in the MIAP cost management dashboard showing breakdowns by billing product for Databricks usage.
Started creating new MIAP hull coating models for missing coating types (in progress).
Worked with Will to troubleshoot the MIAP REST API image deployment failure—identified limited disk space on the deployment agent and coordinated remediation with the platform team.

Reza:

MIAP
What Have You Done This Week
Continued work on fixing digital twin issues:
Corrected the bug related to thruster model names.
Forced the use of FAT SFOC models when power plant models are not available for diesel generators.
Fixed the bug affecting ships with only one unique drydock date when fetching the next drydock date.
Collaborated with the team to handle required components in diesel engine, SFOC, and propulsion areas.
Worked on tuning FACTS-based performance.
Started implementing the workflow for digital twin performance comparisons using sensor data (similar to the FACTS-based workflow).
Fixed a bug in the AUH workflow for daily prediction.

Will:
MIAP
Fixed a bug in the ratio heat power pilot fuel calculation that caused the power plant workflow to fail.
Resolved an issue with the GTG MGO Equivalent Calculation.
Added RD to the Power Plant Workflow.
Fixed an out-of-memory bug with guidance from Brendan.
Added support for LNG Optimizer in the MIAP REST API.
Added support for LNG Optimizer in the MIAP App.
Fixed a bug in the CO₂e Carbon Factor affecting LNG Optimizer in emissions mode.
Removed the 2% pilot fuel ratio heat power fallback in the LNG Optimizer.

Arya:
MIAP
Continued tuning the SFOC model.
Began converting the workflow into a pipeline where, after anomaly detection, the plot is saved, written to a PDF, and emailed to specified users.
Learned that “with great power comes great responsibility” when using Graph API for automated emails.
Fixed the power plant job line.
Built documentation for the dynamic model used in MIAP solutions.

Mahshad:
MIAP
Developed an LLM model to detect anomalies by comparing consumption against similar weather conditions, identifying unusually high usage in specific elements within an area, and generating a PDF report to highlight recent deviations.
Detected anomalies in the SY chillers and investigated potential chiller issues on the VY-class ships.

Doug

**CEL**** Revenue Management**** | Perks Gap Test Monitoring & Final Findings**

Added t-test metrics to findings. Prepared for final test output. Discussed test extension for 7N/FAR, LONG/FAR, AK/FAR.

**Doug**

**RCI ****Revenue Management**** | Data Driven Berthing Optimization**

This work is complete as of 01/28/2026.Upgrades to the mandatory occupancy logic generated improved berthing rates on Icon-class ships where previous rules left many bookings requiring manual action.

Reviewed coding changes to implement upgraded mandatory occupancy logic for category-level limits.

Provided feedback for code changes and validated that mandatory occupancy code updates produced correct results.

Met with business to discuss limits and proportions coding and opportunities for improvement to the existing process.

Michelle

**CEL Revenue Management: ****Category-Gapping 2.0**

There are cases where the revenue at different gaps only varies by a couple cents but the optimization will recommend the highest revenue. For example, it would be 13% with raw revenue of $147.30 although a 10% gap has a revenue of $147.09 which is about the same but tradeup changes by 5%.

Team is asking if the revenue is within $2, optimal gap should be the lowest option. Rounded the revenue calculation and added penalty to select the lowest gap as optimal. Made changes and refactored notebook to optimize code and not rewrite the same function. Working on code reusability for all future work. These updates will improve recommendations as minimal changes in revenue will not lead to drastic changes in gaps.

Awaiting business review.

Michelle

**CEL Revenue Management: ****Category-Gapping 3.0**

Built first version of classes that allow to train multiple models in parallel and select best by chosen metrics. Also created helpers for my most commonly used functions and functions for feature selection that try multiple methods such as Mutual Information and RFE.

Refactoring training data. Fixed majority of falloff, still seeing about 1% of bookings do not have matching prices. This is occurring for multiple reasons and solutions vary case by case. For example, some bookings were COVID transfers that have old offer dates that do not match current sailing, so offer date is before sailing were opened and no prices exist.

Lamis

**RCI Revenue Management: ****Apply required Adjustments to PRE 4.0 + QA + Push to ****Prd**

Already completed the changes to the PRE pipeline and today finalizing the QA run triggered through ADF. Debugged and resolved few issues with the QA run. This is expected to be completed today and push to prd tomorrow.

**Few hiccups faced**:

Validation took some time - cause final prices shown on the archive do not exactly match with the optimization recs due to a lot of weighting and capping that are being done in the intermediate business notebooks.

the pipeline takes some time to test through ADF and debug failures.

Needed to add some hardening pieces for the code to ensure the entire pipeline does not break in case optimization fails for whatever reason - and simply fallback to PRE 3 recs.

The pipeline was failing in QA because the optimization solver prints updates on the optimization run - and since optimization is running for each sailing-cc, the output size was exceeding the allowable limit had to do some research to figure out how to turn these updates of.

Evan

**SPI Factor Model**

**Finalized method for ****build**** similarities**

Combined unsupervised model approach with new checkpoint instance

Worked on decomposition of signal

Can be used in future instances

**Evaluated multiple factor models**

Worked to confirm input variables and run initial analysis for GTY

Created EDA and recognized that total GTY % is not representative of SPI diff, thus additional work is required

Completed method to standardize data queries as .sql methods that become part of a class (automatically)

**Built new unsupervised decomposition methods**

Testing instances to cluster trend / momentum or decompose signals

**Began work on supervised “tuning models”**

Working to seek how each independent variable describes the target (being SPI diff)

**Localized Package Management (nearly complete)**

Finished and published a single script that:

Identifies the version of python and curls it

Installs uv and databricks-connect

Installs databricks cli automatically

Instructs the user only once to log in via web page (holds auth now)

Builds the specific version of python matching the cluster

Pulls the packages of the cluster locally as a requirements.txt

Filters these requirements to the needed ones

Installs all combined via uv pip install

Jesse

Silversea Revenue Management

**SSC PRE | PRE Business Upgrades**

**SSC PRE | Pause File Price Flexibility**

Re-affirming the use of “stack” pricing recommendations. If revenue managers reject a price recommendation based on magnitude, PRE will recommend a lesser magnitude price recommendation.

This policy change is based on a previous agreement between Data Science and Revenue teams.

Its purpose is to ensure that price recommendations get accepted by the Reservation System.

**Additional Context:**

It is unfeasible for revenue managers to enter their own price recommendation into the PRE pause file.

Cabin categories must maintain a particular pricing order within voyage, farecode, and currency types.

Revenue managers cannot choose their own pricings because pricing recommendations will re-order these categories and changes will not pass Revenue System validation.

**SSC PRE | Flexible Business Rules**

Flexible rule structure for business rules

Allows business rules to be tailored to sailings or cabin/fare subsets within sailings

**SSC PRE | Refactor Lookback Code**

Variable lookback windows per voyage, farecode combination

Flexible framework that enables new variables to be added or removed to PRE lookback computation

Reduced comments and unutilized memory when running PRE

**SSC PRE | Meeting Tracker**

**1/29/2026:**

Data Science, Data Engineering, and management teams discussed the new feature stores that will populate ITRAVEL. Data Science informed Data Engineering of the feature store fields necessary for PRE utilization. Data Engineering will refresh the new feature store tables daily instead of weekly.

**1/28/2026:**

Met with Data Engineering about PRE updates. Data Engineering will perform extensive validation on PRE price recommendations that use different currencies, as additional currencies were added this week.

Ignacio

PCP Pricing Automation

**T****est v1 Automated Promos w/ OBR Team (Production – Preview Mode)**

The promo uploads were tested after meeting with everyone and enabling the tool.

A batch of promos were pushed to preview mode and checked to ensure they were received properly on the digital side and data engineering side (all data passing correctly into Kafka & Hybris).

The OBR teams (RCI & CEL) were then also asked to check if they received those promos on Hybris on their end as well.

In addition, a few guardrails were added to ensure that no rows left empty in the automated promo uploads resulted in empty promos in the system.

Almost all tested promos succeeded; the few that failed were due to invalid data provided for the promotion conditions (e.g., invalid cabin class code and invalid sailing key for creating the conditions for the promotion).

These invalid data samples were discussed with the OBR teams to clear up what needs to be corrected and to have the proper cabin class code mappings set up.

The cabin class mappings for CEL were also double checked and slightly corrected to ensure they have all the necessary mapped data for automating promos with cabin class conditions.

Ignacio

PCP Pricing Automation

**Help Cihan Fixing Model & Optimization Results for Waterpark**

New nonlinear model was explored to capture more complex demand–price patterns where demand may change at different rates depending on what current price the price increase/decrease occurs.

An XGBoost model was used as a first attempt at this.

This helped improve the elasticity coefficients significantly (no longer inelastic coefficients less than -1.0).

However, there are also some questionable coefficients at certain WTS bins as well; nonlinear elasticity models should be further explored to improve performance and place less constraints on the price–demand relationship.

After these changes, the optimization routine was also adjusted and showed improved results.

The prices no longer always hit the max price constraint, showing improved captured price–demand relationships with better elasticities.

This is improvement but should still be further validated and tweaked appropriately.

Ignacio

PCP Pricing Automation

**Unit Test the Centralized A/B Testing Framework (FEB)**

Some work was started for building notebooks for unit testing the created MVP A/B Testing Framework.

Work primarily started on unit testing the soft pairing component and testing every function of it separately and independently.

However, due to shifting priorities for OBR, this work is to be handed off to Jesse and completed by him in order to free up time for OBR.

The main idea is to:

(a) perform unit testing on each component of the A/B testing framework (testing each function of each component individually and independently)

(b) perform an end-to-end use testing of a pseudo-production use case (involving testing all components together in a use case)

Ignacio

PCP Pricing Automation

**Recurring Meetings with OBR Team – Planning for OBR Priorities**

Has several recurring meetings with OBR team in January to plan priorities of work for OBR moving forward, including:

Automation efforts for promo uploads

Automation of CRF

Completion of waterpark PRE

Enhancements to beverage PRE

Plan of end-to-end automation from model/PRE to CRF to promo uploads

Dashboard for approving/rejecting recommended promotions

This also includes:

Meetings with DE team for data being assembled for promos

Meetings with others on DS team for A/B testing and CRF automation

Lekha

CEL Revenue Management

**CEL | DART | Integration**

**Rethinking DART Logic and Implementation Approach**

**Bias Correction Implementation**

Implemented a Kalman filter as a bias correction layer on top of the existing model to adjust for consistent over- or under-predictions without relying on current week actuals.

Tuned Kalman filter parameters to control the trade-off between how quickly it reacts and the smoothness of adjustments.

Tested different configurations to determine the optimal level of trust in past information and maximum allowed correction size.

Achieved approximately a 3% reduction in overall error after tuning, with remaining errors mainly from noisy, low-volume weeks.

Divided bookings into granular demand buckets to evaluate DART’s impact and found it ineffective in low-demand (0–2 bookings) segments due to noise and less bias.

Calculated error metrics across different weeks-to-sail buckets and observed consistent error reductions after applying DART.

Presented findings to Kevin and jointly decided to explore filtering on track ask > 3 to improve DART performance and avoid increasing errors in low-demand areas.

Planned next steps to implement and validate the proposed filter for better optimization of DART results where it is most effective.

Kartik

PCP Pricing Automation

**RCI | OBR | Royal Beach Club**

**Create automation and validation checks on promotions provided**

Utilizing recommendations from kevins table to build automated CRF for RBC, and validating final promo and pricing recommendations

**Investigating web scraping bugs and put in a fix for it for royal beach club**

there was a bug with royal beach club web scraping algorithm, so I put in a fix by refactoring the code and scheduled it at time whihc works best based on Hybris data

**Power Analysis and Sailing List Creation for initial pricing test**

Conducted power analysis on rbc penetration for a pricing test and help create a sailing list for the pricing test where we test a lower price for rbc products to gain insights on booking patterns

Glen-Erik

PROPEL

New Offer Template:

Presented draft template to OBR team. They are very excited to put this in production, although they recognize there is still refinements and testing that needs to be done.

Resolved issue with HTML tags being interpreted as gibberish.

Resolved formatting issue affecting some categories where the Redemption and T&C text was getting cut off.

Resized all images for the templates

Investigating makeover offer over-assignment:

The product categories that are in the tool don't coincide exactly with the categories of consumer spending. This is an issue not just for makeover, but for things like Retail AT, or Retail AT-BY-RF-SI-SL, which are made up offer categories that help the OBR team segment the offers but are not actual categories in the spend data making the model output inaccurate.

Additionally, makeover is a new category. The pipeline that updates categorical spend on a monthly basis is failing to run due to the query being inefficient so that category is not known by the model yet even if the above issue #1 were to be fixed. I estimate this pipeline will be fixed next week, but that may not fix the issue by itself.

Eswar

RCI Revenue Management

Integrated Data Validation framework to TRACK, Inventory RMA project related workflows

Discussed the strategy to deploy ABTesting framework in RMA, so that it can be leveraged by all other RMA, Data science projects.

Guidance on RMA CI/CD process and code refactoring before productionizing PRE model training updates

Refactored/optimized one of the PRE model training code snippet and bought runtime from 25+min to 20sec.

Reviewing and monitoring PR's. CI/CD

Providing MLOps support in bypassing issues, enabling developers by providing guidance and productionizing workflows.

Guidance on enabling VS Code to Azure devops connection to a developer which can ease the development process.

Glen-Erik

Win-on-Waste :

Identified and analyzed failures in Databricks workflows caused by missing environment-specific storage structures (volumes and tables) required for data migration and CI/CD deployment. Creation of the respective volumes.

Defined the Databricks asset bundles for the WOW repository, clarifying infrastructure and deployment expectations across environments.

Established deployment standards for WOW workflows, ensuring that all workflows in the dev-da2i-alpha-dbricks workspace with the prd_ prefix are bundled and deployed to QA and PRD in a paused state.

Helped align the branch strategy for Databricks deployments, mapping the qa branch to the QA workspace and the main (master) branch to the PRD workspace.
