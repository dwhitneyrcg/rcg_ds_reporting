Henry Drescher

[Cresta] Accomplishments

Fixed data validation errors with supervisor dashboards for Royal and Celebrity.

Finalized GenKA plan for 3 phase rollout

Validated next steps to parody livevox reporting with cresta

Developed AI analyst test use case

Henry Drescher

[Conversational IVR] Accomplishments

Celebrity deployment for river, disambiguation and loyalty fixes. Expected impact is 0.15% of minutes automated increase (Absolute)

Update Royal IVR reporting to include latest changes

Henry Drescher

[Cresta] Working on

Updates from data validation exercise on agent level pilot dashboards

Finalizing new hire dashboard

Follow through on GenKA 3 phrase plan

Analytics parody with livevox speech reporting

Integration of session start metadata

Integration of reservation and other internal data

Plan for AI analyst impact

Plan for reaching ROI with new roadmap features

Henry Drescher

[Conversational IVR]  Working on

Contracts for HCL and migration

Development of backlog items (Cost/Benefit analysis, business approval, designs, etc.)

Research into moving analytics from mix to copilot

Copilot migration

Henry Drescher

[Call forecasting] Working On

Transitioning to Nico and team for analytics

Transitioning modeling to enterprise data science

Ayon

Win-on-Waste

1) FPMS Rollout and forecast roll out to 5 ships -

Voyager (VY)

Symphony (SY)

Anthem (AN)

Independence (ID)

Rhapsody (RH)

Support, hotfixes and enhancements to all 5 ships

2) Testing and Hotfixes on Xdining model in the improved pipeline

3) Windjammer - complementary venue model ETL, feature building complete

Kevin

Loyalty: Prepared spend to save pilot updates using more finance end of voyage reports and FCC generation files. Continued to collaborate with Data Engineering to identify bad data in onboard spend. Data Engineering was given a deadline of one additional week (6/25) to resolve data issues to allow sufficient time for analysis on the data prior to the EC meeting. If the deadline is not met, it is highly likely that the team will be presenting based on finance values and not true data. Adjusted design of choice benefits to ease fulfillment concerns, and began development of power analysis for credit card acquisition.

Ben

Customer Lifetime Value (CLTV) Program
• Data Integration: Successfully incorporated on-board revenue data into the analytics dataset. This will support future exploratory data analysis to identify new revenue opportunities and enhance CLTV modeling accuracy.

Mirielle
Contact Center Booked-to-Cancel BK2CX

• Pipeline Monitoring: Ongoing weekly monitoring and review of core pipeline processes for Productionized Lead Prioritization Model. No interruptions or bottlenecks detected this week.

• Executive Presentations: Developed and refined content for ongoing presentations, highlighting lead prioritization progress and insights (CTI and BK2CX).

Mirielle

Contact Center Workforce Planning Simulator
• Data Preprocessing & Modeling:
o Collaborated with Jason Atkerson to validate the computation of the average handle time (AHT) metric. Explored the rationale for excluding answer time (ANSTIME) from AHT, with findings informing future model accuracy.
o Advanced development of the weekly grid across each Line of Business. This grid now precisely delineates service hours (open/close) and daily call volume proportions—both central for accurate staffing and demand forecasting.
o Continued to coordinate with data engineering regarding critical data migration activities; tracking milestones and ensuring clean data flow for modeling.
o Ongoing preprocessing and feature engineering are enabling more robust and actionable workforce capacity forecasts.

Ben and Camila
Integrated Business Planning (IBP) Program
• Medical & CocoCay Models:
o Completed back-testing and corrected date logic to improve MAPE (Mean Absolute Percentage Error) for both main and challenger forecasting models.
• Order Creation Table:
o Enhanced calculations to more accurately project future voyages; responding to feedback from Yan by adding sailing voyage numbers for precise validation.
o Continued development to modify data joins so sailings without initial loading are captured comprehensively.
• Depletion Table:
o Delivered the final product, with validation underway by comparing stock child tables for reconciliation.
• Volatility Reports:
o Refreshed table calls to better capture historical and current product/ship inventory data. Identified missing combinations due to deletions, with remediation measures being evaluated.
• Uniforms & Product Matching:
o Progressing on a revised version to accommodate expanded and modified uniform/product naming conventions.

Carlos
E-Commerce 
• Targeted Offer Models:
o Deployed targeted offer uplift models into production. However, the CEL version’s predictive performance remains suboptimal due to data sparsity; escalation with Michelle and Alicia is underway to resolve input data constraints.
• Personalization Enhancements:
o Assisted in incorporating epsilon features into the Genie personalization engine and the consumer profile dashboard, improving segmentation granularity.
o Research initiated to implement multi-agent capabilities in Genie, which is expected to further enhance recommendation diversity and engagement.
o Preparing to enrich demographic data available to Genie for deeper customer insight.
• AI Generated Reports: Continued development and deployment of AI-generated analytical reports to stakeholders for actionable insights.

Aagam

**RCI | SPI Factor Model | Norm APD & GTY Lead – June**

Using regression analysis with XGBoost, identified revenue-optimizing gaps for Normalized APD (i.e. GTY-Lead) for good sailings (based on SPI). Delivered an analysis for RCI Leadership.

Atefeh

**RCI | PRE Elasticity Upgrades**

Evaluating improvements in elasticity values and performance metrics through feature enhancements and modeling strategies. Added new features such as:

Cabin occupancy code

Peak season flag

Holiday flag

Weekend sailing flag

Ship class Oasis icon

RSS product group 1

Booking wave flag

Sail year

Integrated these with existing features like cabin occupancy code, ship class, category class, sailing month, booking averages, and booked positions.

Applied target encoding to categorical features to improve model learning.

Trained separate models for each combination of product code and category class.

**Datasets Used:**** **VPS dataset, AS400 dataset

**Results:** The best-performing setup was the upgraded model using the VPS dataset with the new features and modeling strategy, showing significant improvements in elasticity and performance metrics.

Bernard Wittmaack

**CEL | SPI Scoring Model Improvements JUNE**

Incorporated all feedback from Anastasia last week into model

Changed SPI score normalization from multiplicative to additive, preserving spread of scores as well as preventing extreme high/low balancing due to outliers.

Awaiting feedback on new scores

Continuing work on SPI-guided target setting for meeting with Anastasia on Friday 6/20

Bernard Wittmaack

**RCI | SPI Factor Model | Build a Drivers Model**

FIT Track Targets

Researched historical track adjustments as a function of read date for major meta products

Key conclusion is that track is most heavily adjusted during Black Friday and Wave - exactly where the ML model is recommending the largest changes from current track

Current track does not account for historically robust demand patterns from both read week and WTS perspectives.

Jesse Bausell

**SSC | PRE | Forecast PRE Value Added - JUNE**

**Deliverables**: Performed A/B power analysis to determine how many sailings are needed to create statistical significance in A/B testing. Circumvented need for separate “value added” analysis through the power analysis. A/B testing power analysis examined value added by manipulating sailing yields, standardized for days at sea and number of pax.

Jesse Bausell

**SSC | PRE Dynamic Track EDA**

**Deliverables**: Improved knowledge of dynamic track inner workings. **Potential future issue**: STLY will be extremely difficult to implement because SSC voyages singular in itineraries and time of year. It will be extremely challenging to find a viable STLY target for EVERY SINGLE SAILING, especially through an automated process.

Jesse Bausell

**SSC | PRE Coordinate with SSC Revenue & Business Teams**

**6/17/2025 - Feature Store Migration**** **Data Engineering will assume ownership of the SSC Feature Stores, which were previously managed by Data Science.

Jesse Bausell

**SSC | ****Farecode**** Mapping**

SSC plans to introduce new farecodes into its pricing system around mid to late July. A business team member explained the new farecode logic to Data Science and new work is being kicked off to accommodate these mappings in the PRE and future automation projects.

Michelle Manfrini

**RCI | GTY-LEAD 2.0 | JUNE**

Mandatory occupancy flags were incorrect and doubles were not actually able to book these categories. Issue fixed in FS code to recalculate gty-lead gaps and LAF prices. Pull request awaiting approval. Model has been retrained and optimization rerun in dev. Gaps are now 0-27%, averaging about 15%. Meeting with business to review updated results. Tables and plots are updated based on new gty-lead gap recommendations. Gaps are now 0-27%, averaging about 15%.

Michelle Manfrini

**CEL | GTY-LEAD 3.0 | CATGAP Inter-category Gaps Stage 3**

Optimization expansion to all sailings. Met with business and reviewed logic. Track build is scaled to account for cat-class capacity and shares are distributed among tiers dependent on trade-up predictions. Moving forward with applying to all possible tier combinations based on sailing availability.

Lekha

**CEL | Feature Engineering**

**Bucket ****Calendar_woy**** by Business Periods (e.g., Wave Season) for Post-Model Evaluation based on Deviance Error**

Took a first pass at residual errors across calendar_woy for each meta,cat_class and noticed noticeable spikes during certain booking windows.

Saw higher residuals between WOY 10–26 for 7N Caribbean, Alaska, and Europe sailings — which lines up with the peak booking period ahead of their summer departures.

For short Caribbean sailings, the error was higher between WOY 45–10, which aligns with the Wave Season (Nov–Mar).

Decided to switch from residuals to **deviance error**, since residuals don’t adjust for booking volume — deviance gives a clearer, more reliable picture by factoring in both actual demand and prediction accuracy.

Now moving forward with bucketing calendar_woy by business season to evaluate deviance across key booking windows more meaningfully.

Lekha

**CEL | Productionizing Elasticity Upgrades**

Spent some time reviewing the CEL elasticity training code to check if any clean-up was needed before sending it to QA.

Set up a Databricks workflow to run the pre-elasticity model and retraining steps automatically as part of the pipeline.

Created a detailed .yml config script for this workflow to ensure everything runs as expected when triggered w.r.t the environment it is in.

Pushed the YAML file to the ADF develop branch and worked on making sure it connected properly with existing pipeline logic.

Merged the setup into the QA branch to test the same job in the QA environment and confirm it’s ready for further testing and validation

PRE Elasticity Model Code and Retraining pipeline merge to QA and the run was successful

Lamis

**RCI | PRE Elasticity Upgrades - JUNE **

**Feature Engineering** This week I refitted the spline-based wts bins on the recent vps data (the same data we are using for the elasticity model). The bins are generated at the meta - cat_class level, and they will be shared with the business this week for feedback and validation. I am working now on testing them on all the other metas (Alaska. Short Caribbean, and Europe). Also - determining the best model parameters for each rdss_product_group_1 and cat_class

Reza

Marine Operations

Just presented Reza's HVAC Diagnostic to Newbuild Technology Team. They were quite impressed and taked about getting capital funds to build solutions for Legend of the Seas under MIAP. Will be having a meeting next week to discuss in more detail.

Ignacio

PCP Pricing Automation

**Price Constraints:**** **Replaced fixed min/max APD limits with dynamic constraints at 50% below and 30% below the system’s average base price. Price recommendations are based on either current discounts or required system price to meet targets.

**Constraint Checks:**** **Added backend validation to flag violations of price and demand constraints during optimization, with few outliers detected.

**Model & Routine Deployment:**** **Moved to production a simpler Poisson regression model replacing the complex elasticity model, tailored for beverage packages. Trained models per product/meta code, initially focusing on product 3222.

**Pricing Table Update:**** **Updated cabana base price tables for Hybris, calculating recommended prices assuming stable discounts.

**Mert****, Reza and Brendan**

**Medallia GenAI**

Presented EDA and initial modeling results of litigation modeling to Claire Maison. Initial analysis is promising for further investment into Data Science, with great potential as the company incurs $300M/year in litigation costs. The objective is to settle deals with guests/crew before incidents escalate to claims or litigation.

Conducted data analysis for the Legal project: performed exploratory data analysis (EDA), evaluated multiple classification models to predict incident-to-claim outcomes, and presented interim findings to the VP.

Completed exploratory data analysis (EDA) on legal claims and factors influencing their conversion to litigation. Trained initial model to establish baseline performance and presented findings to VP to assess project potential.

**Mert**

**Marine Ops**

Met with GMO leadership team to discuss potential expansion of the MIAP program into Safety and Asset Management areas.

Met with the GMO Safety team to explore potential collaboration opportunities.

Prepared a presentation proposing a navigation risk reporting framework using Fuzzy Logic and IoT data, based on academic research. This framework enables interpretable risk scoring for the fleet by integrating expert knowledge into models using Knowledge-Based AI.

Onboarded a new Data Science contractor for the Stability Project and provided project-specific training.

**Rez****a**

Investigated and resolved a bug in the AHU model within the GMO application.

Conducted data analysis for the Legal project: performed exploratory data analysis (EDA), evaluated multiple classification models to predict incident-to-claim outcomes, and presented interim findings to the VP.

Presented HVAC Diagnostics methodology and deployed predictive models for the Newbuild Technology Team, demonstrating deployment pipeline and use cases. They were quite impressed and taked about getting capital funds to build solutions for Legend of the Seas under MIAP. Will be having a meeting next week to discuss in more detail.

**Ram**

**MarineOps**

*June 16th*

Modified Eniram code, focusing on the autoloader component.

Reorganized data into partitioned folders (instead of a single schema folder) to reduce processing time.

Enhanced code for improved speed and deployed the updated version to QA for testing.

*June 17th*

Connected with platform team regarding permissions for Ignio and GSC tables; issue unresolved, continued analysis.

Reviewed PO and PR notebooks for Ignio to understand data flow.

For Eniram, changed data fetching logic from landing parquet files to CSV files via API, reducing data retrieval time from 40 minutes to 6 minutes per day.

Updated autoloader code based on improvements.

*June 18th*

Followed up with platform team on GSC table permissions; tested cluster switch changes but issue persisted.

Successfully moved Eniram notebooks to QA, tested thoroughly, then deployed to both QA and production.

Raised request for workflow deployment to production.

Explored alternative autoloader approach and began testing for effectiveness.

*Next Week*

Plan to test new Eniram approach once ready.

Begin working on Ignio tasks as soon as permissions are granted.

Collaborate on creating two new datasets requested by the Ignio team.

**Mehdi**

**MarineOps**

Automated extraction of all tables from multiple PDF pages, saving each table as a separate sheet in Excel files, dynamically named by source PDFs.

Adapted workflow for various environments by handling dynamic paths.

Prepared methods for future standardization of inconsistent column names and textual data fields using rule-based and advanced ML/NLP techniques for similarity detection and clustering.

**Mashad**

**MarineOps**

Worked on VY class COP curves and added them to the Excel file.

Developed the incinerator model for fuel consumption; worked on AN and plan to add other ships next week.

Analyzed IN and AD savings: IN AHU consumption data spans 8 months, averaging ~150 kW, resulting in approximately $15K savings per month; awaiting ship’s response.

Monitoring CS, SM, OV for AHU savings.

Added IC and NO to the OFB pipeline.

Currently working on obtaining tags for ML class for OFB, planned for next week.

**Brendan**

**MarineOps**

Developed initial proof-of-concept for cross-company AI Foundry usage: created an APIM endpoint that abstracts LLM model versions from users, enforces team/project-level security, and logs usage details (token counts, model version, team/project name, etc.). This endpoint acts as a proxy, enabling the platform team to enforce standards, monitor usage, and control model access.
