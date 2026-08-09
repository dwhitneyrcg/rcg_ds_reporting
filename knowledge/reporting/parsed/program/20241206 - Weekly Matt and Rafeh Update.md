**Proud: **

**• Global Marine Operations:** DS team productionized Dynamic Service Power monitoring models and completed development of a novel outlier removal algorithm (to be integrated in all MIAP models) and a working prototype of the Power Plan Optimization model. Team identified $135K/month excess cost from Air Handling Units on 10 ships (Anthem, Ovation, Spectrum, Harmony, Wonder, Beyond, Millenium, Summit, Constellation, Infinity) with a total excess to cost to date of $600K. Reached out to each ship to resolve excess energy consumption.

**•Generative AI Pilot (Medallia Text Summarization Tool):** DS team demoed a suite of new AI-infused business tools that will enable our business teams to quickly extract guest feedback on specific topics. Feedback from Gang Wang was highly positive and team preparing to share with broader RCI onboard teams and CEL within the next 2-4 weeks. Evaluating feasibility to create an App, which will enable business teams with no-coding experience to generate ad-hoc reporting.

**•PCP Personalization:** DS team completed first "For You" AI-Recommendation model achieving 30ms inference times and demoed GenAI-based natural product search with Digital Technical teams. DS and MLOPs teams actively working to achieve higher RPS (>200) for our Databricks API endpoint, which will be serving Naive + AI recommendations to the Digital teams.

**•Revenue Management (CEL): **DS team delivered important PRE enhancements that will enable PRE Automation to properly function when the Discounted Fare type is retired next week for CEL (like it was with RCI earlier this year). Team shared positive results for the AB Test to optimize the fare gap between  All-Inclusive and Cruise Only Fares (Meta-Product Level). Team continues to develop out a bi-branded AI automation optimizing the GTY-Lead Tradeup (~$4M revenue impact), prioritizing elasticity enhancements, and planning a second Groups Berthing AB test.

**•Revenue Management (RCI):** With the GTY-Replenishment automation now fully operational and stable ($3M revenue impact), the DS team removed remaining guardrails and minimized exceptions preventing full deployment across the majority of the fleet. MLOPs team delivered (a) new Automated PR checks for new code validation and (b) automation to convert SQL queries in ADF to Databricks (accelerating migration to Unity Catalog). DS Team continues to develop out a bi-branded AI automation optimizing the GTY-Lead Tradeup (~$7M revenue impact), prioritizing bi-branded elasticity enhancements, and actively refining PRE Business Rules.

**Excited:**

**•CLTV Analysis (Corporate Planning):** DS team delivered new improvements to the CLTV dataset for upcoming readouts with Leadership teams. Added flags for consumer life stage, nps, geography, cruise experience and travel companions. These flags will allow the corporate strategy teams to build stratifications on CLV that will inform later stage segmentations. A preliminary meeting with Kara Wallace and Michael Figgis will be scheduled for late next week to discuss initial stratifications prior to the larger group readout on 12/19.

**•Lead Prioritization (RCI/CEL):** Preparing to productionize the CTI and BK2CX Lead Prioritization models. CTI model (CEL) will be delivered first and then BK2CX models (RCI/CEL), but Contact Center may delay go-live date into Q1-Q2 of next year (after Wave).

**•Loyalty Simulator:** DS team completed integrating new AI-spend models for FTC/RPT guests into Loyalty Simulator. Team running 6 "forward-looking" modeling simulations with different parameters, including sampling vs modeling, normalizing spend to remove effects of inflation, and spreading predicted spend distributions to match historical distributions. These modeling scenarios will be evaluated next week based on 1-year back-testing (training up to 2023 and tested on 2024).

**•PCP Pricing Automation:** DS team completed outlier detection for Cabanas Pricing Recommendation model. Next steps are to validate pricing recommendations in AB Test and team is working with the onboard revenue teams to select test and control sailings.

**•PROPEL:** MLOps Team working on enhancements to the PROPEL offers (e.g. increased offer variety and preventing offers going to guests already bought an item) and increasing the percentage of guests that receive PROPEL offers (from 50% to 80%).

**•Supply Chain:** DS team actively working on (a) data validation as data sources for Demand Forecasts switch from Synapse to Unity Catalog, (b) delivering enhancements + bug-fixes to Uniform and Health demand forecast models, and (c) investigating if a network optimization approach can improve demand forecasting. Next week team will be presenting Supply Chain CAR to the Finance teams and Capital Committee.

**•Revenue Management (SSC):** DS Team delivered enhanced pricing recommendations incorporating business feedback. Team is focused on delivering PRE pricing recommendations by end of this month.

**Concerns:**

None

ATEFEH

**Tracks: **

RCI/CEL/SSC | Inventory Automation Improvements

RCI/CEL/SSC | Pricing Automation Improvements

Adjusted the code to use MLflow to fit a logistic function instead of custom logistic model

For each meta product I have created a separate notebook

Developed the code to save the model  under catalog to make it ready for production

I have started working on optimization development to determine the optimal gap, maximizing revenue.

AAGAM

**Tracks:**

RCI/CEL/SSC | Pricing Automation Improvements

RCI/CEL/SSC | Track Optimization

Revenue Strategy Support

Identified a capping rule that is getting triggered incorrectly in the business rules code of the PRE. Actively working to create a new business rule and code into the PRE. Additionally, there is a need to quantify the impact of this change in business rule. Scheduled meet with the revenue team on Thursday(12/5) to align on the solution for this

Completed analysis and presented on the importance of purchasing  a PCP for retention. Please note, Week over week, a customer purchasing a PCP is almost a guaranteed build.

The new reservation team needs to understand the different types of analytics projects, so a document was created to address this need.

Michelle

**Tracks:**

RCI/CEL/SSC | Pricing Automation New

Closed out GTY-LEAD 1.0: modelling testing data and analyzing price gaps by meta, wts, and cat-class

Continued working on GTY-LEAD 2.0: Optimizing price gap for highest revenue. Meeting with CEL team 12/5 to confirm granularity desired for predictions as well as the format required for them to integrate model results into their processes.

Ignacio

**Tracks:**

RCI | Inventory Automation Improvements – OBR

Added a method of logging an outdated/previous Champion model as an "old Champion"

Adjusted feature engineering & feature store table creation based on updated changes to features used in the model

We have started initial attempts to quantify the model improvement obtained from outlier detection and began researching and brainstorming ideas of control vs test group testing on certain sailings (for validating the model's impact on revenue)

Douglas

**Tracks: **

RCI | Inventory Automation Improvements

RCI | Pricing Automation Improvements

CEL | Support Initiatives

Product teams are asking that we Identify where and why PRE generates a $0 final price in cases where raises and lowers can be minimal. Researching to finalize next steps- Rev Strat team will reevaluate the specific recommendations for possible adjustments.

Found an issue early November where junior suites are inverted with balconies due to rec based on only occupancy. Working to resolve this issue.

Worked with the business to formulate Groups berthing test #2. Test coded and scheduled to run on Wednesday, 12/5 at 12 pm

Loyalty: 
Integrated Spend Models for Repeat and new guests. Running 6 different modeling scenarios (~24hr run time) with different parameters to be analyzed next week, including sampling vs modeling, normalizing spend to remove effects of inflation, and spreading predicted spend distributions to match historical distributions. The different scenarios will have one year of backtested data to compare results and illustrate improvements from different model iterations. 

CLTV:
Continued improvements to the dataset for the upcoming readouts. Added flags for consumer life stage, nps, geography, cruise experience and travel companions. These flags will allow the corporate strategy teams to build stratifications on CLV that will inform later stage segmentations. A preliminary meeting with Kara Wallace and Michael Figgis will be scheduled for late next week to discuss initial stratifications prior to the larger group readout on 12/19.

GSCBP:
• Data validation of Unity Catalog datasets, comparing to known correct Synapse datasets and then migrating code to use Unity Catalog after validation. So far have validated 23 datasets and migrated to Unity Catalog. Only 5 datasets left for validation and code migration. One dataset appears to have a problem as row counts in Unity Catalog are 3 times greater than Synapse. Met with DE on 12/5 to review the problem and they are aware and reviewing. 
• Correct package error last week, and after correction, Uniform and Medical models completed successfully 
• Adding updated metrics in the email notification for the Medical model available to Ben and Yan.
• Prototyping and early exploratory work on developing a network optimization approach for supply chain incorporating demand forecast, shipboard inventory, vendor, voyage and PO data.
• Prepare uniform's unpivoted table for uniform model bid.
• Prepare new adjusted demand forecast averaging current demand forecast with the 12-month rolling average consumption for uniform model.
• Provide a Supply Value for Uniform Model joining shipboard inventory and decrementing the demand forecast for the upcoming sailing less shipboard inventory. 
Pending Tasks
• Awaiting feedback from stakeholder Mario on price scraping
• Add Celebrity data to be added for uniform model
• Document all datasets being written to SharePoint and then meet with Stakeholder Yan to identify code that can be sunsetted
• CocoCay demand forecasting
• Researching adding GenAI tool for procurement to engage with demand forecast and potentially a future network optimized value to better inform what if modeling on total procurement costs when adjusting vendors and ordering strategies. 

E-Commerce
• Models maintenance: 
o Fixed bug causing duplicated records being uploaded to oracle for sister brand models. (Sajan and Alissa found it)
• Dashboard: 
o Research on adding GenAi capabilities to the dashboard.
o Support Camila on the creation of the reports for new models
• Working on cluster configuration to be able to upload the report for bp x destinations for e-commerce.
Pending Tasks
• Complete sister brand models reports for the dashboard
• Debug error from ecommerce where run id does not exist when searching to download artifacts.
Update for Loyalty
• Add spend prediction model to guest simulator
• Optimize simulator performance: 33s to 17s per day
• Improve validation 
Pending 
• Source spend from historical distribution by consumer type (prospects and past guests)

GMO:

* Completed new Kalman Filter based outlier removal method implementation for MIAP models.
* Completed deployment of Service Power models to the new dynamic model framework, continuing parameter tuning of each ship.
* Added a multithread multi-plot generator method for MIAP API, to allow returning multiple plots in a single query to enhance load performance of web app plots.
* Started re-factoring MIAP WebApp to use MIAP API for plot generation.
* Completed creation of a working prototype power plant optimization model, solving mixed integer non-linear program for finding optimal power distribution of engines, given efficiency of each generator and fuel/scrubber limitation constaits.
* Working on CI/CD pipeline development for MIAP API Management.
* Adding Crosser remote tag update functionality to DataBricks.
* ~$700K pre-liminary fuel savings on Wonder based on MIAP Data and models in-collaboration with CdA shipyard. Team is currently onboard and ship is optimizing parameters to achive sustainable HVAC savings without effecting guest confort. 
* Identified $135K/month excess cost on Anthem, Ovation, Spectrum, Harmony, Wonder, Beyond, Millenium, Summit, Constellation, Infinity. Total excess to cost to date is $600K, from Air Handling Units. Reached out to each ship to find resolution for excess energy consumption.
* Met with Captain Henrik (RCI Fleet Captain) and data engineering team to discuss development of port and berth database on Alpha Platform.

Medallia COE
- Met with Gang to review and demo our LLM solution.
- Demo of unstructed to structured transformation 
- Demo of dashboards and aggregations
- Demo of email template
- Demo of summarization capabilities
- Making some modifications
- Backfilled data to August 1st, 2024 to now
- Will be collecting feedback through early December
- Dashboard and email job are pending feedback/approval
- Need to work towards creating a deck for onboard operations leadership. 
- Will work to measure correlation between LLM outputs & numeric survey metrics. 
- Will work to create a Fleet wide summary email for Gang. 

Lead Prioritization – Celebrity CTI
- Model performance on train/test is good enough to push to production.
- Met with Will Arango and was asked to ready CTI ASAP. 
- However it is unlikely the business will want to go live with CTI model prior to Wave. 
- Met with Shan Garg and confirmed that CEL CTI should mimic the existing RCI CTI process which will simplify production execution. 
- Updated the production notebook:
- Organized the project by creating separate folders for training and other related tasks, and moved the training notebook files alongside other notebooks used for feature engineering and training related to the lead prioritization model.
- Enhanced MLflow artifacts by improving the decile graphs and adding line and scatter plots to provide better visualizations and interpretations of lead conversion results.
- Adapted SQL scripts for leads and quotes creation, making them compatible with Databricks by replacing datetime functions and modifying the min/max X_RCCL_LOAD_ID input parameters.

Lead Prioritization - RCI/CEL BKTOCX
- Model performance on train/test is good enough to push to production.
- Met with Will Arango nad was informed that BKTOCX should be slated to be released after CTI. 
- Met with Shan Garg and Augusto and agreed on an additional task which is to revamp the data sources coming from the system which may cause deployment delays. This is to both fix bugs with legacy tables which will also assist the efforts to lead score leads. 
- Production Notebooks and refresh process complete. However we will have to sync with Augusto and Shan to re-engineer the source raw tables to fix data discrepancies prior to moving to prod. 

Emails Recommender
- Was granted access to Salesforce. Need to find the time to test sending data. 

MyCruise Recommender
- Completed the first version of the "For You" model achieving inferencing times under 30 milliseconds.
- Working toward integrating the new "For You" model with the existing Naive recommender and API endpoint. 
- Performance test the API
- Achieved 200 RPS and discovered that we are rate limited by Databricks. We need to reach out to Databricks to ask about cost of current implementation and cost of increasing RPS to over 200. 
- Rosie and Taylor mentioned peak RPS to be at around 220 RPS.
- However I am concerned that the 220 RPS might be an underestimate given the feedback received from frontend engineering. 
- Also concerend about adhoc requests from frontend engineering which lead to major changes to API. For context, I met with frontend engineering last week who asked to modify expected API response to specific JSON schema format which is completely different from the original architecture. Need to work to make these changes. 

MyCruise Product Search
- Met with technical teams to demo cruise search. 
- Action items from meeting: 
- Redeployed search with fresh data
- Generated synthetic data from product descriptions which summarize Tour activities to improve search precision
- Added a sailing_id filter
- Replaced Cosine Similarity with FAISS which vastly improved search speed. 
- Performance test the API - Pending

WoW
Ayon
WOW team update: working on updating separate guard rail model for lunch (lunch doesn't have a pattern because the schedule of restaurants open during lunch is not fixed)

Gourish
Calculated the moving average and lagged moving average for all meal periods.
Added a daily consumption ratio for lunch and dinner.
Calculated additional moving average forecasts.
Computed the highest reservation count.

RMA: (Eswar/Javier)

1. Unity Catalog Migration: Eswar created an automated conversion script to do the initial changes to the ADF queries to convert them to databricks queries. As well as streamlining the process to compare the output of the ADF queries to the databricks queries. 30 queries in progress. Benefit: This will greatly speed up the migration. 
2. Automated PR Checks: Javier got a first pilot test working, triggered by the PR creation and adding the comment in the right place in the code only checking the code that is changing. Next step is to build out the simpler naming convention checks and test out. Benefit: automated quality and standards checks before code is merged to develop or main. The immediate feedback encourages developers to follow best practices rather than identifying and fixing technical debt or issues after they are already in production. It also avoids raising all existing issues unrelated to the developer’s current effort. Can be reapplied in other projects as well.

PROPEL: (Alejandro)

1. Evaluation and adjustment of guest data logic (Bug fix). Benefit: Resolved the issue of algorithms sending offers with the name of a past guest, improving personalization and guest satisfaction.
2. Implementation of ShorEx logic for pre-cruise buyers (In Progress) Benefit: Provides personalized ShorEx offers, enhancing relationships with repeat buyers and avoiding the perception of financial loss by the customers and potential revenue loss for us through cannibalization.
3. Adjustments to packages and BOGOs as a provisional measure. Benefit: Increased the variety of potential offers during the cruise, boosting guest spending potential.
4. Established plan to move away from 50/50 test to full coverage. First step to turn one ship on at 80/20 is ready, then other ships at 80/20, and in tandem develop the product level test/control logic so there are control groups but everyone can still get offers outside of their group. Benefit: move towards making offers to all guests on the ship without sacrificing measurability of the outcome and lift impact.

PCP: (Alejandro)

1. Created load testing scripts for MCR and MCS endpoints with detailed reporting Benefit: Provides clear awareness of API operational ranges, enabling confident deployment to production

HIRING: (Glen-Erik)

1. Lead: 1 interview and take home test. Take home could have been better. 
2. Senior RMA: 3 interviews and 1 take home tests completed Wednesday, 1-2 take home tests this coming weekend. Hiring decision ETA end of next week.
3. Senior PROPEL: Off-track. Need Rafeh’s approval to hire. Have candidates in the pipeline for the other senior role that could potentially be hired for this one as well.

RCGGPT: (Eswar)

A lot of planned work but no time dedicated these past couple weeks to development efforts. Still on track to deliver TechGPT by the end of January 2025.

MIAP: (Brendan)

1. Began migrating the MIAP WebApp to the MIAP REST API: completed python class to interface with API, currently working on migrating individual applications.

Other: (Glen-Erik)

1. Aligned Unity Catalog naming conventions with DS Managers. Benefit: bring clarity and organization to the projects through standardized naming conventions of the data at each step in the process (input, config, output).
2. Implemented new cluster policies for the Data Science workspaces to meet the needs of the platform users and reduce costs without impacting productivity.
3. Automated PR checks (see RMA bulletpoint, the pilot for this).
