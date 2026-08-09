Gaurav

**App Engagement Analysis – Celebrity Cruise**

Completed SHAP analysis to identify key drivers of pre-cruise spend.

Conducted regression analysis to estimate the incremental spend per app engagement.

Consolidated findings and shared a presentation deck with insights, delivered to Doreen.

Gaurav

**NPS Target Setting Model**

Assessed the accuracy of various NPS target-setting approaches, including: Statistical modeling, Business-defined targets, Average NPS from the previous N sailings.

Experimented with building separate target-setting models for Royal and Celebrity, and compared their performance against the current combined model.

Gaurav

**Medallia Topic-Level Thresholds for NPS**

Held requirement discussions with Hannah.

Cristian

PCP Product Recommender System:

Conducted research on enhancing customer segmentation (ForYou ALS input) to more accurately capture customer interests and preferences within each segment.

Collaborated with the product team to explore new personalization use cases, including the integration of AI-generated personalized product categories into our web and app platforms.

Refactored the API input and output schemas, as requested by stakeholders, to improve interpretability.

Developed new unit tests to support the updated schemas.

Updated the OpenAPI contract service to reflect these changes.

Parimala

**Contact Center (****CTI ****Lead Prioritization ****Model Deployments****)**

CTI model for Royal and Celebrity brands is performing as expected

Continuously monitoring execution time across pipelines and optimizing trigger configurations as needed.

Developed a comprehensive presentation deck on CTI for the upcoming presentation.

Parimala

Medallia Generative AI Pilot

**Guest Logs**

Generated initial topics from Guest Log data.

Collaborated with stakeholders to clarify and gather detailed requirements.

Scope shifted from topic generation; currently developing an application to present topics and subtopics derived from the Guest Log dataset.

**Qualtrics Survey**

Held a call with the Qualtrics Business Team and internal stakeholders to review the Qualtrics API configuration and its limitations.

The platform team is creating a POC for integrating with the Qualtrics API, while Royal/Celebrity teams are aligning on the use case.

Mert, Reza, Brendan

Legal

Met with Legal team to discuss a potential project predicting litigation from ship-related injuries.

Worked on ETL for Risconnect data related to legal litigations.

conducted preliminary data evaluation, including assessment of a classification model.

Mert

Marine Ops (MIAP)
Deployed a class for finding the closest port/leg with available weather data to be used with fuel forecasting.
Completed loading raw data into Databricks and started exploratory data analysis (EDA).

Will

Marine Ops (MIAP)
Completed the power plant base model.
Completed the power plant residual boosting model.
Integrated the power plant dynamic model into the existing power plant analytics ETL.
Currently building model visualizations in the GMO app.
Working on individual power plant dynamic models (at the power plant level, unlike the ship-level models mentioned above).

Ram

Marine Ops (MIAP)
6th June
Migrated Eniram notebooks and workflows from Marine workspace to DE workspace.
Cloned necessary notebooks and functions due to artifact feed pointing away from Marine.
Modified API code to add columns in control table for fetching exact chunk number and failure time.
Encountered unauthorized request issues; reached out to platform team for support.
9th June
Coordinated with the platform team to set up Key Vault for Eniram in DE workspace.
Began analyzing Ignio notebooks related to new column additions.
Engaged with Ignio and Strategy teams to gather new requirements.
Attended the RX monthly program review.
10th July
Addressed two production issues where BI team received null values from views (SSC_poc_consumption and shipboard_inventory).
Implemented two alternative approaches that improved speed by approximately 60%.
Collaborated with Ignio team to understand session workflows.
11th July
Fixed data type discrepancies and schema mismatches in Eniram API.
12th July
Developed a modified version of Eniram for incremental data loading.
Preparing to move this implementation to QA and production environments.

Reza

Marine Ops (MIAP)
Developed and fixed bugs in the AHU Diagnostic Platform workflow, enabling monthly model updates and daily predictions.
Deployed updates to AHU Diagnostic results in GMO app, including improved plot formatting for better visualization.
Started integrating load factor data into HVAC and Hotel models to improve accuracy.

Brendan

Marine Ops (MIAP)
Fixed scikit-learn version issues causing failures in several MIAP model runs.
Hardcoded package versions across multiple packages/repos to prevent breaking changes in production.
Deployed two AHU workflows to production using Databricks Asset Bundles.
Resolved authentication token issues preventing DE Databricks workspace from installing Marine Analytics Python packages.
Assisted MIAP Data Engineer with leveraging Databricks Secret Scopes.
Created 30+ tables in Databricks for a POC with the Legal team and fixed several data quality issues.

Mashad

Marine Ops (MIAP)
Added NO and IC parameters to the boiler model.
Started work on the incinerator model.
Followed up on IN AHU, achieving savings of approximately 200 kW.
Investigating potential chiller savings for AD, estimated around 300 kW.

Ignacio

**PCP Pricing Automation**

**Hybris Cabanas Price Table Improvements:**
The base price upload table for cabanas was refined to support automated updates in Hybris. Changes included updating the displayed base price based on average discounted prices and actual booking data, calculated by multiplying the recommended price-to-be-paid by the ratio of average base price to average paid. The table was reformatted (renamed columns, added fields like age group and tax), and null base price values—originating from missing booking data—were filled using historical averages per product and month.

Ignacio

**PCP Pricing Automation**

**Incorporating Target Revenues into Optimization:**
Additional penalty weights based on target revenues from OBR were added to the optimization's objective function to better align prices and revenues with expectations. Mismatched data and complex constraints initially caused poor results; after correcting data issues, a simplified optimization routine was developed.

Ignacio

**PCP Pricing Automation**

**Simplified Elasticity Model:**
A new, more straightforward Poisson Regression model replaced the complex two-part elasticity model, incorporating data transformations like target encoding, polynomial features, and scaling. Focused on key product lines (e.g., Deluxe 21+, Refreshment, Soda), this model showed more promising results, with plans to expand to additional products later.

Ignacio

**PCP Pricing Automation**

**New Optimization Routine:**
The updated routine minimizes differences from OBR revenue targets, avoiding issues from overconstrained models. It includes an alternative revenue-maximizing approach as a reference, delivering more reliable and aligned pricing outcomes.

Kartik

RCI | T4 AB TEST | Design AB Test JUNE

Worked on T4 Sailing list. Met with Nick, Nicholas and Kevin to work on the constraints and decide which ones we can relax a little bit because we were not getting enough sailings. Created a version 1 of sailing list based on the discussions. Will send it over to the business team and wait for feedback on it.

Lamis

RCI | PRE Elasticity Upgrades - JUNE

Feature Engineering

Model Training and Testing

Based on the Revenue Strategy team's feedback last week I have worked on the following updates in the elasticity model:

1. Trained separate models at the rdss_product_group_1 and cat_class level.

2. I ran multiple experiments over diff wts bin sizes: 5, 10, 20 and accustom (0-12, 12-36, 36-60) with a total of 228 models trained.

3. I refitted the spline regression to create wts spline-based binning on data with sailing dates > 1/1/2024

4. I re-though the target column transformation. The new_bk_bkg distribution is least skewed at the rdss, cat_class, ship_code and bkg_wave_flag level - so, I considered these to run conditional power transformation for the target.

5. By the end of this week I will have tested integrating the spline_based wts binning into the elasticity model, and identify the best model from all the performed tests for each rdss group and cat_class.

Srilekha

CEL | Elasticity Model Feature Engineering

Feature Engineering: Developed a custom function to convert calendar week of year (calendar_woy) into a cyclic feature to better capture yearly demand patterns in the elasticity model. Integrated this into the sklearn pipeline for automation.

Model Evaluation & Analysis: The cyclic transformation improved R² and error metrics, but overall total error remained higher than expected. Detailed error analysis revealed significant errors during high-demand periods in November and early months (Jan–Mar), aligning with wave_period calendar weeks.

Feature Testing: Created a new feature, wave_flag, to explicitly mark high-demand weeks (Nov, Jan–Mar). However, adding wave_flag did not lead to improvements in R² or other error metrics.

Next Steps: Will continue experimenting with calendar-related features and transformations to enhance the elasticity model’s performance.

Michelle

CEL | GTY-LEAD 2.0
Fully launched this week for CEL. This is a big delivery for the Revenue Management team.
Will be monitoring results.

Michelle

CEL | GTY-LEAD 3.0
Future sailings dataset completed. Includes track/demand and capacity.
Initial optimization code almost written. Subjected to constraints for booking shares, cabin totals week by week and at end of sailing. Instead of week-by-week recommendation's, optimization is based on total bookings across all future weeks based on predicted track.

Michelle

RCI | GTY-LEAD 2.0
Met with Eddie and identified issue where quad categories were open to book for doubles. This is true based on mandatory occupancy flags, but business would like to exclude prices from gap calculations as this will be more closely controlled by analysts in the future. In process of editing feature stores code to recalculate gaps, this should decrease the gaps we were seeing.
Will retrain model and rerun optimization based on new data.

**Jesse**

**SSC | PRE | Design PRE A/B Test**

Had a constructive discussion with business and they are aligned now to use Dynamic Track for PRE A/B Testing.

I have created a notebook that pairs voyages for A/B testing, using hard and soft constraints. User can modify these constraints according to the suggestions of business and revenue teams. It uses a combination of masking and cluster analysis (k-means) to match sailings. I have also taken a deep dive into the workings of dynamic track.

**Doug ****Beddell**

**RCI | ****PRE Eliminate**** remaining copy ****datas**** JUNE**

PRE archive and archive history replaced by copy to Unity Catalog

** **

**Doug ****Beddell**

**RCI | PRE Ongoing Upgrades | JUNE**

Pipeline 3: Legacy post-processing quality report from Accenture was incorrectly reporting select quality measures. Fixed report table and redirected it from ADLS to Unity Catalog

**Doug ****Beddell**

**CEL | Re-berthing Adjustments and Launch**

Demand-based adjustments coded and tested successfully.

Awaiting final validation from business/product teams before moving version 1.0 into production.

Feedback from business to add a low-tier second pass through the data for bookings that can be re-berthed.

Bernard Wittmaack

**RCI | SPI Factor Model | Build a Drivers Model**
- Updated dataset to train track generation model from vcap to historical dynamic track data where the delta in projected cumulative track pax is used instead of new bookings. The prior method, which used bookings, did not capture signal coming from T4 demand.
- Newly trained model much better fits behavior expected during Black Friday and during wave season.
- I identified a repeated, characteristic second wave season peak in booking volume in March. Kevin's analysis on web date corroborated findings, but track never accounts for this second peak. Chris and team will investigate.
- Track chronically underestimates final payment demand for most meta products
- Recommendation is to adjusts track to account for patterns found in actual booking volume not currently incorporated into track.

Bernard Wittmaack
**CEL | SPI Scoring Model Improvements JUNE:**
- Updated SPI scoring model for Europe to adjust for Mediterranean port groupings, significantly reducing SPI score bias among port.
- CEL additionally wants to account for day of week that Short Caribbean sailings debark in the normalization process as well as early and late Easter holiday in 7N Caribbean product.

Atefeh

RCI | PRE Elasticity Upgrades

I have conducted a proxy comparison between the VPS dataset and the AS400 LAF per day price. As part of this analysis, I performed a side-by-side comparison of the original model setup using the same set of features:
1. At the occupancy level, using log-transformed LAF per day from both AS400 and VPS, I compared the elasticity values and performance metrics.
2. Without occupancy, I re-ran the original model (one model per meta product) using both AS400 and VPS LAF values.
The results show that the VPS data leads to better elasticity estimates and improved performance metrics in both setups.
In addition, I developed the following extensions:
• New Approach with TE Features, CatClass Individual Models, and AS400 LAF
• New Approach with TE Features, CatClass Individual Models, and VPS LAF (current approach)
I’ve compiled all findings and discussed them with Eddie this week.

Ben and Camila

Integrated Business Planning (IBP)
• RCI/CCI Order Creation
– Fixed a critical join, reducing the dataset from 64,000 to 7,000 rows (–89%).
– Reconciled allocation math by grouping on ship, product, voyage number and ship_load_date, matching Ben’s manual calculations.
• Volatility Reporting
– Built a volatility table using SQL window functions (lag) to capture month-over-month changes in Prediction_AI.
– Automated CSV generation per ship/category; deploying both email distribution and a Teams/SharePoint channel for easy access.
• CocoCay Consumption Model
– Completed “Guardrails” version 2 with improved MdAPE; launched version 3 workflow to refine ship-arrival consumption sums.
• Data Cleansing & Automation
– Populated blank local-market values per Fanny’s ship specifications.
– Enhanced automated reports with Lauren’s ship-branding subtotals; scheduled monthly Teams alerts and folder uploads.

Ben and Camila

Integrated Business Planning (IBP)

Pending
• Finalize SharePoint upload for corrected local-market data.
• Standardize product names—resolving string vs. array-type mismatches.
• Prototype AI-generated Medallia reports (pending Erick’s guidance).
• Review RCI/CCI inventory-depletion table.

Carlos

E-Commerce
Main Project: Consumer-Propensity Dashboard

Accomplishments
• Optimized Databricks dashboards by replacing built-in aggregations with custom SQL queries—significantly improving load times.
• Mapped consumer net-worth and niche segments (0–9) to their true definitions using SharePoint documentation.
• Limited user filters to model selection and decile only—balancing flexibility with clarity.
• Developed and tested the first targeted-offer uplift model; corrected feature-engineering errors to align offer dates with consumer snapshots.
• Built preliminary dashboard reports for uplift models.

Carlos

E-Commerce

In Progress
• Deploy uplift models to production.
• Integrate epsilon demographic data into Genie.
• Iterate dashboard enhancements based on Carlos’s feedback.
• Explore additional data sources to deepen consumer-profile insights.

Ben

Contact Center
3.1 Leadership Workshop
• Delivered a 4-hour innovation workshop to 25+ leaders across Training Delivery, Content, Knowledge Management and QA & Analytics.
• Workshop included icebreaker and three ideation breakout sessions; received exemplary feedback from Chuck Baker.
• Jessica Marmolejo-Perez expressed high interest in partnering on a CAR to fund pilot solutions drafted during the session.

Mirielle

Contact Center

3.2 Lead Prioritization Data Pipeline Stabilization
• Monitored and debugged the SBCXED pipeline (2-hour cadence) with zero production-stage errors.
• Completed SFTP integration tests with the Siebel team.
• Executed end-to-end stage-environment runs for all Royal and Celebrity lead types (14 total); no errors to date.

Mirielle

Contact Center

Lead Prioritization Data Pipeline Stabilization

Next Steps
• Transition final testing to the Siebel team for production cut-over.
• Establish ongoing model performance monitoring post-go-live.

Mirielle

Contact Center

Workforce Planning Simulator (North America POC)
Achievements
• Staffing Model POC—mapped 2025 call volumes across all LOBs (Casino, Groups, Reservations, Loyalty, Service) with Jason Atkerson; validated against existing Excel and Power BI models.
• Data Migration—coordinating with Antonio Ciuccolini on office-shrinkage dataset migration to UC (60% complete).

Mirielle

Contact Center

Workforce Planning Simulator (North America POC)
Next Steps
• Request migration of REVSTRAT.SOURCING_CHANNEL.
• Continue data ingestion and preprocessing.
• Develop POC in Databricks: exploratory analysis and feature engineering (AHT, ASA, service level, abandon rate, etc.).

Kevin

CLTV:

Relatively light week, as corporate strategy is in the midst of annual strat plan review. Met with Gaby to troubleshoot and validate concerns on index calculations and logic. Met with Pascale and Ricky to better understand Customer 360 and OBR projects and how they will act as a foundation to CLV dataset. Providing Austin's OBR datasets to be stitched into this projects.

Kevin

Loyalty:

There continue to be delays in measurement and analysis of the first completed Spend to Save pilots due to issue's with POS transaction data in Exadata. Continued to build temporary analyses using finance end of voyage reports that may not represent true differences in spend patterns driven by the pilot. Additionally prepared analysis on FCC redemption from the initial sailings. Discovered a handful of sailings are holiday sailings and needed to be replaced. Adjusted clustering algorithm to find similar replacement sailings. Presented these initial views to Kara and Rafeh during core loyalty meeting. Kartik is adapting Carlos's booking propensity model adjusting feature selection that is skewing results on propensity scores for recent guests to provide guidance on if a guest likely would have made a booking without the FCC. Significant progress has been made with expected delivery on Friday 6/13.

RM:

Built an initial view on web-based baskets for celebrity using clickstream data. Worked with Eddie, Michelle and Alexa to determine causes of high predicted category gaps. Worked with Kartik and Nick to relax constraints on T4 A/B test for sailing selection.

Ayon

Win-on-Waste

1) prd_silver.mkrpops.booking_channel_revenue has refresh problem which caused PL failure at some days. Added code module to combat failure

2) Developed rules engine to select best prediction out of POS pred, GR Pred, Stacked Pred and Cold start pred and integrated that to the test Pipeline

3) Refactored some code modules in specialty test pipeline

4) Build upsert insert capability for stacked and coldstart pipeline in test

5) Unit testing and integration testing of both specialty V1 and MDR_V1 pipelines

Ayon

Win-on-Waste

Future Steps: Note: Next week will be totally focused on unit and integration testing and hotfixes on both specialty V1 and MDR_V1 pipelines
