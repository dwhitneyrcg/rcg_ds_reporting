Mert and Reza

Met with the Legal team to access the Riskonnect tool, enabling us to build a POC model for predicting the probability of a claim going to litigation. This has high potential savings as the company spends nearly $300M/year on legal payments.

Attended meetings related to new areas such as claim events and new builds. Investigated the preliminary available data.

Mert

Completed expected weather database for legs and ports to be used for fuel forecasting, providing expected climate conditions of each port and leg for each month.

Enhancing MIAP ETL pipelines and fixing bugs in IoT.

Planning MIAP Phase IV CAR and finances.

Brendan

Created a cost monitoring dashboard for MIAP, including a forecast of projected spend; this has already led to an approximate 3% reduction in total annual cloud spend (for the MIAP project only), due to a finding located by Mert via the dashboard.

Added propulsion hull degradation visualization to the GMO app in TEST.

Worked with the GMO dev team to communicate a bug affecting plot rendering with tabs, which impacted deployment of the propulsion hull degradation visualization to PRD.

Created a lookup table for coating type and coating age to predict hull degradation percentage.

Added multithreading into the propulsion hull degradation endpoint in the MIAP API, reducing response time by approximately 60%.

Created a dashboard showcasing Azure platform spend broken down by various categories, including the top 100 most expensive Databricks notebooks, longest running queries, and most expensive jobs.

Reviewed MIAP machinery deviation and informed the data scientist of approximately eight findings that could potentially lead to cost savings.

Performed exploratory data analysis (EDA) on the ALS offset model for fuel forecast CAR.

Will

05/30/2025

Worked on the base model for the power plant fuel forecasting project.

06/02/2025

Continued work on the power plant base model for the fuel forecast project.

Assisted IT developer with the algorithm for extracting OPCUA nodes in Crosser.

Investigated an unusual linear relationship between DG 1 and DG 2 on FR.

06/03/2025

Completed a notebook to help test the base model and its features.

Completed the first iteration of the base model for most ships.

06/04/2025

Completed the first iteration of the base model on all ships; found issues on a few ships.

Investigating issues on FR, AL, LB, NO, EN, VI, GR, RH, EX, UT, IC base models.

06/05/2025

Continued testing and bug fixing on the power plant base model.

Created a figure in the QA GMO app to help the GMO dev team test the new dynamic figures feature in the API.

Reza

Completed the electrical power module of the HVAC diagnostics platform for all ships within HVAC areas. A total of 3,108 models were trained, each corresponding to an individual Air Handling Unit (AHU). To optimize data management, a binning technique was employed to consolidate the results into 17 tables (one per ship). These results have been deployed to production, enabling precise identification of excess energy consumption for each AHU on every ship. Early implementation has already demonstrated measurable energy savings on the ships Infinity and Summit.

Ram

30th May

Worked on deploying the Gangway workflow to Production from QA. Encountered several issues and coordinated with the Platform team to resolve them. Due to permission issues and cluster problems, deployment was delayed.

2nd May

Investigated the root cause for the view v_ssc_consumption_report, which the BI team uses. The view was returning empty data, leading to escalation. Identified a possible error, modified the code accordingly, and tested with various test cases.

3rd May

Deployed the corrected view to Production; the BI team is now able to access the data successfully.

Received a request to change column and table names for Gangway. Paused deployment work and historical data migration to accommodate these changes. Completed all necessary modifications.

4th May

Attended the Anchors Away event near the port office from 9:00 AM to 4:30 PM. No progress was made on regular tasks during the day.

5th May

Completed the ENIRAM workflow and began deploying it in QA.

Once verified, plan to move it to Production, schedule it daily, and complete all related tasks for Gangway.

Next Week

The MIAP ETL process is consuming significant resources and taking longer than expected. I will prioritize resolving this issue.

Mashad

Saved $18K on WN Pump for 200 kW.

Followed up on IN AHU power deviation of approximately 180 kW.

Followed up on AD chillers power deviation of approximately 300 kW.

Revised the ship boiler’s deviation calculation. Since the boiler on the ship is often not operational, the data is unbalanced, and the presence of zeros complicates the deviation calculation.

Updated GMO boiler plots for curve fitting to support the regression model.

Developed additional plots for the classification part related to GMO data, considering data imbalance.

Began analyzing GMO boiler data for OFB fuel consumption deviation from expectation, including:

OFB measured vs. expected fuel consumption

OFB fuel consumption trends (actual fuel consumption and enthalpy)

Air/sea temperature and air humidity.

Kevin

Loyalty:

Continued last week's efforts to validate onboard spend data in collaboration with OBR teams and DW. DW is still working through a solution to make data available for sailings after April 2025. Prepared more analysis on pilot success using financial results from each voyage, but this data does not likely reflect true guest behavior.

Kartik collaborated with Carlos to use booking propensity models to identify guests that would likely not have created a booking unless offered the FCC. The first pass using likelihood scores for all guests indicated that every guest that had redeemed so far, had a higher probability to sail. We identified that results were skewed because time since last sailing is a feature in Carlos's model, meaning most guests on the pilot sailings will have a higher likelihood to sail in the next year. Kartik is working on improvements to take this into account.

Choice benefits pilot is being accelerated with the expectation that emails go out in July for a 60 day booking window in August and September. Brian is working on matched pairs for the target selection based on booking propensity drivers.

Kevin

CLTV:

Continued data validation phases with corporate strategy. Assisting corporate strategy in gathering appending additional data sources to the POC dataset, so analysis can continue while the MVP is being prepared. Met with working group to align on phased delivery (including POC forward looking clv), responsibilities and timelines.

Kevin

Revenue Management (CEL):

Actively working through web traffic data to gain better insights on baskets based on consumer search history and demand throughout the year. Expected POC early next week to be shared with RM teams.

Aagam

RCI | Factor Model | Justification of gaps for GTY Lead and Norm APD

Based on the insights I shared with the business regarding GTY Lead Gaps and Norm APD, I provided additional clarification on why the Norm_APD gaps and GTY Lead gaps aligned with expectations. The business anticipated higher norm APD and GTY Lead gaps in the farther-out windows.

To validate my findings, I examined how norm APDs and GTY Lead gaps vary across sailing weights. I observed that, overall, for all meta_products, category-class, and ship_class, the APDs are consistently a bit lower, which supports the results I presented last week.

Additionally, I have included SHAP plots alongside the PDP plots, which further support and corroborate my results. The SHAP plots illustrate the interactions with the target variable, allowing us to clearly identify the points where the contribution becomes positive.

Atefeh

RCI | Build a Track Variance dataset calculation for RCI PRE

Contacted Eddie to clarify how the PRE should calculate track variances.

Prepared and saved the track variance table in Unity Catalog under dev_revenue_mgmt_bu.pre.track_and_pax_builds. This table includes weekly track variances with a variable rolling window for each Ship, Sailing Date, Catclass, and Occupancy Level.

The price change calculation notebook should not compute track variances, as this dataset will be used when deploying the elasticity model into production.

Held a meeting with Jake to discuss the framework for RCI PRE; started reviewing the current framework and notebooks used in price calculation.

Begin preparing the price calculation notebook and identify necessary modifications.

Bernard

RCI | SPI Factor Model - MAY

Optimal Group Bookings Strategy

The group booked position is typically 5-10 percentage points higher off-peak compared to peak periods.

The optimal "sweet spot" for groups is between 15-20% booked position off-peak and 10-15% during peak.

Group and FIT Average Price Differences (APDs) are approximately 5-10 percentage points higher during peak relative to off-peak.

Target ranges are set at 60-70 off-peak and 70-80 for peak season.

The association between SPI and other factors is less significant compared to group booked position.

Bernard

Present SPI Factor Model Findings to Business 5/29

Key takeaways:

I presented peak/off-peak recommendations for FIT track targets and group booked position targets presented

GTY-Lead insights presented by Aagam

Discussed roadmap and next steps, including combining individual factors (listed above) into global factor model that will estimate the marginal contribution of these individual factors on SPI in presence of all factors.

Feedback from Nick:

Quantify change in track ask from SPI recommendations quarterly for 2025 through 2026 by meta product and overall by load factor percentage.

Examine builds next. An outstanding question is whether T4 demand should be accepted later or earlier in the booking window.

GTY-lead trends not expected by Nick - need closer examination to verify results.

Bernard

FIT Track Optimization Model

Presented findings to Chris on May 29 highlighting the improvements of the newer model

New model output more closely adheres to recent data

Expected signal in booking volume preserved while noise smoothed out

Feedback was positive and Chris will review and advise on next steps.

Bernard

CEL | SPI Scoring Model Improvements MAY

A new SPI output was presented to CEL on May 28.

Recent shifts in business practices, such as increased emphasis on T4 demand, are now better reflected in the SPI model — notably, spring break and summer are more offset relative to off-peak due to additional T4 volume.

Removed 2023 sailings from the model at Anastasia’s request.

SPI scores are awaiting validation from the CEL team.

Jesse

SSC | PRE | Design PRE A/B Test – JUNE

Specifically, I am doing A/B testing for three SSC areas (not just one). Moreover, I did not fully understand the scrip that I was working with; I had to go back into it and correct several errors.

A/B testing: power analysis + ALASKA voyage selection

Deliverables:

Power analysis for combined Alaska, Caribbean, and Mediterranean voyages.

K-means cluster analysis for Alaska sailings.

Identification of eight pairs of Alaska sailings suitable for A/B testing.

Challenges & Notes:

Delayed understanding of the k-means clustering script; had to re-examine to improve comprehension.

Future potential issue: Need tickets for further cluster analysis of Caribbean and Mediterranean sailings.

Power analysis is complete. Voyages from Alaska, Mediterranean, and the Caribbean were normalized and standardized using z-scores and Mann-Whitney ordered ranked sums to unify all sailings.

The power analysis indicates that 50 pairs of sailings are needed to achieve 90% significance at a 10% revenue difference.

Data Science identified eight Alaska sailing pairs for use in power analysis, with plans to source additional pairs from the Mediterranean and Caribbean.

Michelle

**RCI | CAT-GAP 3.0**
- Met with business 6/03/25. Exploring cases with gap inversions. Working with business to decide logic for special tier cases, such as ALASKAOJ. Expanded training data to include “all-above” bookings as was done for CEL model. Sent team requested plots of gaps to understand frequencies in historical bookings and example sailings to illustrate range of tier prices.

RCI | GTY-LEAD | CAT-GAP 2.0
- Team reviewed results, an update requested. Change was made, table and plots were sent over to business for further validations. Awaiting business feedback.

Michelle

CEL | CAT-GAP 3.0
- In progress: Code for track integration for revenue optimization.
**
CEL | GTY-LEAD | CAT-GAP 2.0**
- Maintenance and monitoring table complete. Reviewed with CEL team. Added table for tracking optimal gap changes day by day and flagging changes over 20%. Working with MLOps to chain with TAP workflows and include email notifications.

Srilekha

**Residual Error Analysis Summary**

Explored various FacetGrid residual plots for the new elasticity model to identify sail months with higher prediction errors.

Included the Holiday flag as a feature to assess if it captures demand spikes during holidays.

Findings show the model predicts holiday demand effectively, with residuals close to zero in most cases.

Most extreme residual errors occur during non-holiday sailings.

Used calendar week of year (WOY) as a hue parameter to analyze residual patterns across different cat_classes and meta_products.

Notably, the largest errors are concentrated during the wave season, especially in late October, November, December, and January, indicating consistent seasonal patterns.

Customer booking behavior during these wave months tends to be far in advance.

**Next Step – Cyclical Feature Transformation:**

Implement cyclic transformation on calendar_woy using sine and cosine functions.

This approach will better model the cyclical nature of weeks in a year, accurately capturing seasonality, especially around year-end transitions and peak wave periods where residual errors are high.

Lamis Amer

**RCI | PRE Elasticity Upgrades - JUNE**

I am working with Jake and Atefeh on upgrading the elasticity model for RCI. What I have done this week is as follows:

Testing multiple models for each meta, cat class under diff price column transformations and week to sale binning strategies. I ran multiple experiments and logged the trained models into MLFlow.

My initial version of this testing code is hard to scale as the number of experiments to test grows. So, I stared working on parametrizing my experimentation code - Will leverage some of the architecture Dave shared.

I am also doing some EDA on the Price column and other columns such as sail nights and wts bining. The goal is to improve the model metrics along with interpretable elasticity values.

Gaurav

App Engagement Analysis: Completed data extraction for app engagement analysis for Celebrity Cruises. The end objective is to validate how similar or different our findings are between Royal and Celebrity.  
LTR Matrix Dashboard: Build and delivered the LTR Matrix dashboard for Royal.
NPS Driver Model (Baseline and Residual): Getting up to speed on the baseline and residual NPS driver model developed on Medallia data.
Bot Enablement: Enabled the general-purpose bot application for Eliana and her team.

Parimala

CTI Model Deployments:

Royal Brand: Successfully deployed the CTI model into production with the end-to-end pipeline fully automated. All stakeholders have confirmed receipt of inference data in their respective applications. The Data Analysis team has also verified data availability on their dashboard.

Celebrity Brand: Enabled CTI model inference for the Celebrity brand. The deployment to production is scheduled for today. Coordinating with all relevant stakeholders to ensure inference data is delivered to the CVP application.

Parimala

Guest Logs:

Engaged with stakeholders to gather and clarify requirements for the Guest Logs project.

Qualtrics Survey:

Ongoing discussions with the Qualtrics business team and other stakeholders to address automation challenges. In the interim, we are supporting the business team by generating summarized reports on an ad hoc basis.

Cristian

Recommender System:

Efficiently integrated purchase history into the recommender system API, enabling dynamic exclusion of previously purchased items and categories per use-case logic, with minimal memory overhead.

Updated the ForYou model’s output schema for both the HomePage Mosaics and Order Confirmation use cases, delivering efficiently sorted data structures by categories and items.

Initiated exploratory data analysis (EDA) to enhance customer segmentation and optimize AI-driven product categorization for the ForYou model.

Collaborated with the product team to discuss model performance testing strategies, alternative evaluation metrics, and potential new use cases.

Provided support and maintained code for API integration in lower environments.

Ben and Camila

IBP (Integrated Business Planning) – Supply Chain

Silversea Data Review: Issue with absence of current Shipboard Inventory view (prd_silver) for Silversea. DE is aware. Fortunately the shipboard inventory data just came back this afternoon and we're creating the table used in the unhealthy inventory dashboard now. There was also issues this past weekend with the point of consumption data being a day delayed as well. Unfortunately, the SSC consumption data is still not refreshed through the last day of the month as the max MOVEMENT_DATE is 2025-05-30, which having not a full month of consumption data still make the unhealthy inventory dashboard which is designed to report on last month inaccurate. Unresolved Silversea data issue impacting business users.

Cabin Capacity Data: Three ships showing ship code issues in prd_silver.ssc_cabin_capacity; temporary code fix underway while collaborating with Ricky for permanent correction at the source for Silversea ships.

Spend Report Tables: Updated in Yan’s environment to join Market with Current Region.

Order Creation Data (RCI/CCI): Ongoing optimization of code for large dataset (~750 million rows) to enhance compute time and ensure calculation accuracy, addressing complex scenarios with multi-sailing product demand forecasting.

Onboarding: New intern Jamie Gonzalez started.

Ben and Kevin

Customer Lifetime Value

New Analysis: Delivered insights quantifying incremental spend linked to Likelihood to Recommend (LTR) score changes. Notably, +1 LTR point yields +$23 spend; -1 point results in -$12 spend on next cruise, compared to guests with unchanged scores.

Onboarding: New intern Caleb Sharkey started.

Carlos

E-Commerce

Collaboration: Met with Alisia Sasportas’ team to deepen understanding of targeted offers data.

Feature Engineering: Enhanced EDA and initial feature engineering for targeted offers.

Targeted Offers Conversion: Estimated redeem/conversion rates by linking booking and offer data. Awaiting finalized dataset from revenue team.

Model Development: Ongoing cleaning and testing of uplift models for targeted offers (production readiness not yet complete).

Intern Development: Guided Bao Lee with assignments and integration.

Carlos

E-Commerce

Pending/Priorities:

Development of model scoring and training dashboards for targeted offers.

Collaborating with the eCommerce team to optimize marketing campaigns using historical targeted offers data.

Mirielle

Contact Center

BKTOCX:

Data Refresh: SBCXED table under test in dev (incremental refresh every two hours); plan to promote to production upon successful testing.

Next Steps: Over next 1–2 days, monitor bi-hourly pipeline for stability and accuracy.

Testing: Begin SFTP transfer workflow with Siebel team.

Workforce Planning Simulation (North America):

Data Migration: Jira ticket in progress for transferring required datasets to Databricks (w/Data Engineering).

Model Rebuild: Excel model analysis showed lack of standardization; alignment with stakeholders to adapt international market approach for North America.

Data Preprocessing: Skills list reviewed per LOB/department; identified data mapping gaps for several LOBs.

Blocker: Current dataset insufficient to map all key LOBs.

Solution: Engaging Power BI dashboard owner for additional source data.

Mirielle

Contact Center

Next Steps: Continue liaising on data migration, preprocessing, and begin exploratory data analysis/feature engineering for North America Workforce Planning POC in Databricks.

Challenges: Incomplete dataset covering all LOBs; awaiting additional data sources.

Ayon

WOW Updates 6/5;

Completed development of Cold start pipeline, to be tested

Completed first version of rules engine to choose the best prediction between POS_pred, GR_pred, stacked pred, and Cold start pred, to be tested

developed and tested - project entree count and projected reservation count

Brendan

MIAP

Cost Reduction: created cost monitoring dashboard for MIAP including forecast of projected spend; already led to ~3% reduction in total annual cloud spend (for MIAP project only) forecast due to dashboard finding. This will be added to the AI/ML Catalog for broader use.

Propulsion Hull Degradation:

Added visualization to GMO app in TEST

Worked with GMO dev team to communicate bug with rendering plots with tabs

Created lookup table for coating type and coating age to get predicted degradation percentage

Added multithreading to endpoint in MIAP API to reduce response time by ~60%

Reviewed MIAP Machinery deviation and informed data scientist of ~8 different findings that could potentially lead to cost savings

Performed EDA on ALS offset model for fuel forecast CAR

Alejandro

PROPEL

Migrated HR tool to the Gen AI Center of Excellence.

Integrated Technical Competencies data into the HR tool.

Adapted Propel training scripts to align with Object-Oriented Programming standards.

[In progress] Conducting feasibility spike for high-end customer offers in Propel.

Eswar

Revenue Management:

Migrated the output table CEL_AUTOMATION_ARCHIVE from oracle to databricks.

Operational support:

Fixed mount point expiration, soon to be replaced this with volumes to avoid issue reoccurring.

Productionized TAP_CEL_GTY_Lead_Optimization and TAP_CEL_GTY_Lead workflows via Bundles.

Helped in fixing errors coming due to few schema changes, type errors.

Approved all Pull Requests and Monitored CI/CD deployment release runs across ADF, Databricks repositories, and Bundle releases.

Best practices & guidance:

Provided an End-End demo on creating Workflows in Databricks to productionzing via Asset Bundles with RCI and Data Science team.

Helping CEL team in following best practices like using catalog_env as spark env, and using dbutils.notebook.run instead of %run. Soon will send a notification to all the developers on this aspect.

Help in setting up computes and guiding which catalogs to use when they are writing their outputs for revenue planning team new hires.

Data Validation Framework:

Email notification setup, whenever some condition fails in TAP_CEL_GTY_Lead_Optimization project

Reviewed framework and identified necessary improvements in progress.

Eswar

Contact Center CTI:

Workflow maintenance and deployed additional CEL CTI workflow.

Brendan / Eswar

Generative AI

API Management middleware:

Initial discovery for POC to control which LLM model is used from platform end. So that all the model updates, changes, and access can be centrally managed.

EXCITED:

Automated Code Review tool: (Javier)

Created a report to track compliance with the suggested code changes of standards violations. However, an issue with duplicate comments surfaced so will have to wait to use the report. Issue fixed below.

Improved user experience and traceability by deduplicating comments when changes are made and the checks re-run.

Eswar

TechGPT:

Incorporated Claude sonnet 4 to TechGPT

Website crawling capability where TechGPT can fetch contents from website URLs. Currently only working for open websites like GitHub, wikepedia (Which is in Preview)

Javier / Brendan

AI ML Catalog:

Created dashboard showcasing Azure platform spend across, broken down by various categories. Showcases top 100 most expensive Databricks notebooks, top 100 longest running Databricks queries, and top 100 most expensive jobs in Databricks. (Brendan)

Refined powerBI dashboard to visualize job execution, repository activity and Pull Request metrics. (Javier)
