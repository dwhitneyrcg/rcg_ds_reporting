Henry Drescher

Contact Center - Conversational AI

Cresta:

*Research on moving speech reporting from Speech IQ to Cresta.

*Expansion to additional use cases

*Exporting data and building out PowerBI reporting

*Building out topics

*First contact resolution

*Auto summary updates

*Topics to include two-letter codes

*AI analyst pilot

*Development of pilot for AI analyst for post-cruise team

*Rollout of phase II; awaiting training material and training for agents

*Planning rollout for phase III changes and timelines

*Incorporation of Royal backend data into Cresta

*Linking conversational IVR to Agent Assist tool

*New hire pilot

Henry Drescher

Contact Center - Conversational AI

Conversational IVR

*Royal migration

*Celebrity migration

*Development of backlog

*Optimize existing services

*New self-services

*Generative answers

*Multi-modal

*Infrastructure planning and environment setup

*Defining testing suite and capabilities

*Defining processes, roles, and responsibilities for migration and post-migration

Henry Drescher

Contact Center - Conversational AI

RFP - CCAS

*Assessing integration of technology and reporting for new CCAS vendors

*Assessing framework for omnichannel interactions and technology integrations

Henry Drescher

Contact Center - Conversational AI

Adhoc

*Technology deck

*AOP asks

*Assessing feasibility of technology for various markets and departments

*Update deck for team

*Manilla hiring: Still have 2 open speech analyst positions

Mert

MIAP

Improved the AMOS ETL job and enriched MIAP INFO data to include links to AMOS installation numbers.

Met with Crosser and DataBricks to discuss a POC for the Lakeflow Zerobus solution as an alternative to Kafka for real-time streaming of MIAP data.

Met with GMO Strategy Director Morgan Dowd and IT Shipboard Ben Calero regarding GMO capital funds. It is very difficult to get capital allocation from GMO, where Data & AI and IT are competing for resources. IT is requesting 700K CapEx, while Data & AI needs about 500K to support both Safety and Asset Management. A meeting will be held with GMO leaders to prioritize work.

Improved the MIAP Webapp front-end design.

Arya

MIAP

Improved the accuracy of the fire classification algorithm and its readability (for Marine Safety). Added a delta table to store output and run only on new entries.

Improved the file structure by adding config and feature folders.

Updated AHU job runs to use an environment variable rather than PRD.

Investigated issues with the AHU job run and found tag mapping problems related to AC power that correlate with job errors for HVAC power.

Currently investigating issues with closest_ref_condition and building a visualization for safety analytics to be included in the GMO app.

Brendan

MIAP

Completed a reusable framework for the Fuel Forecast API and conducted a code review with Mert.

Fixed a bug found when filtering ALS off/on in the propulsion power model.

Implemented code changes to fix warnings from sklearn during inference from propulsion power models.

Mentored a Data Science Analyst on fixing environment-related bugs in QA, combining commits from multiple branches, and provided access to QA workflows.

Met with the MIAP Data Engineer to review progress on performance tuning and error reduction efforts.

Created test cases for the Total Propulsion Power portion of the Fuel Forecast API and continue to develop more test scenarios.

Fixed several bugs in the Fuel Forecast API identified by the test cases.

Reza

MIAP

Developed required features and preliminary models for the fuel forecast model based on FVR, FACTS, and Bunkerweb datasets. FACTS2 for RCI ships is still under development. Although Bunkerweb data has issues, we are developing the pipeline based on the current data.

Developed and implemented new logic for calculating baselines and deviations for the entire fleet and all areas. The proof of concept is complete. The next step is to continue QA testing for one area.

Will

MIAP

Refactored the Power Plant workflow by removing input logic for power plants and run flags for the dynamic and base models. That logic is now derived from the configs, and only a list of ships to run is passed.

Identified 18 ships with data issues and began investigation and implementing solutions.

Added missing ships to the Power Plant workflow.

Fixed a bug loading dynamic model parameters in individual models.

Mahshad

MIAP

Added TCV valve visualizations to help diagnose HVAC AHU and chiller anomalies, making it easier and faster to identify root causes and save time.

Detected probabilistic anomalies with TCV valves in compartments CS, BY, SM, and OY. These areas require closer collaboration with the HVAC engineering team to better understand the ship’s situation.

Monitoring ML, BY, IN, and VY compartments to track improvements following communications with the ships.

Investigated and learned about machinery fans to identify potential energy savings. Found a couple of anomalies in EG and CS, which require further investigation.

Ram

MIAP

Worked on optimizing the MIAP ETL process. Discussed cluster utilization with the MLOps Engineer and identified areas for potential improvements.

Developed the Safety Culture Data Feeds API, completing development and enabling incremental data loading into the Silver layer.

Addressed a critical production issue by redesigning the workflow, switching clusters, and deploying the updated workflow via asset bundles.

Eniram data is now being pulled in QA; moving to production is blocked pending AI code review. Raised the concern and the platform team is actively working on it.

Created asset bundles for Ignio AMOS, JDE, and Crunchtime. Identified a repository-level blocker and raised a ticket with the platform team to resolve it.

Ram

MIAP

Next Week's Focus:

Push the Eniram bundle to production and test tagged data with the old Eniram API.

Continue working on MIAP ETL; plan to move the code to production based on improvements.

Begin Proof of Concept (POC) on FastAPI.

Reach out to the Safety Culture Data Owner to verify data consistency and format.

Mehdi

MIAP

Focused on improving classification performance using multiple modeling approaches, data enhancement techniques, and iterative tuning of model parameters.

Assessed model effectiveness with key evaluation metrics including precision, recall, F1 score, and confusion matrix, identifying strengths and areas for further refinement.

Applied logic-driven feature enrichment and targeted data transformations to ensure consistency and quality across inputs.

Refined rule-based systems to organize location data into structured categories.

Prepared datasets for testing.

Working to enhance the reliability and accuracy of predictions on unseen data.

Erick

Guest Feedback (SEAT)

Axiom – App In-Progress / Pending UX/UI Need to better handle when too much data is selected. The app needs better screen resolution scaling for different screen sizes. Filters Add product/venue, promo, and internet/beverage filters. Convert Voyage ID field to dropdown. Implement addition feature requests (random sampling for chat, venue mapping, ability to exclude topics, download data options). Heatmap Pending Celebrity ship deck plan scraping. Heat Map preparation for celebrity ships. Prepare aggregate heatmaps for upcoming Figgis presentation. Other Meet with Product for future partnership scoping. Add Nicole Lukacs to app. Prepare heatmap linkage from feedback data. Completed This Week Deployed additional filters to Axiom App as per user group requests: Consumer-specific filters (cruise experience, age, demographics) NPS comment filter Sailing-specific filters (cabin, channel, market, charter, meta, RDSS) Voyage ID filter Added new model options (gpt4o-mini, gpt4.1-nano) to enable smarter, larger-context analysis.

Erick

Guest Feedback (SEAT)

Axiom – NPS Driver & Thresholds Analysis Mapped missing features and validated Hanna's list of features with what we had been using. Removed the features Hannah asked for. Updated the queries and reran the data prep step for driver analysis. Updated the excel template dashboard for threshold analysis based on feedback from Kristina. Plan is to rerun the analysis and update the dashboard and share it with Hannah by Friday EOD.

Erick

Guest Feedback (SEAT)

Medallia In-Progress / Pending New features for Email Reporting Implement preliminary email delivery logic and refined sorting. Update SVG plots in emails to reflect only latest 5 data points. Modularize sorting logic for reusable emailing. To add SilverSeas brand to AI pipeline. New Types of Reports: Ad hoc Celebrity requests for fleet-wide emerging topics summary for Laura Hodges. Division-level and employee reporting/custom summaries. Comparative analytics (e.g. RDSS, state/NPS differences). Shore Excursion-specific and nationality insight reporting. Other Create RAG for bullet points. Create specific data cuts for PowerBI owned by Gangs team. Explore using Driver Analysis model for smarter email sorting. Develop MS Teams bot integration for feedback. Completed This Week Fixed Issues: Root-cause analyzed and resolved fleet-wide Royal email failure. Identified Root Cause of NPS mismatch in Celebrity email. EDA 80% of email feedback is received within 4 days post-sailing thus preliminary emails will be sent 4 days after return date.

Erick & Christian

PCP Product Recommendations

MyCruise Recommender API testing continues this week with preliminary results showing: slight increase in average purchase amount for recommended products (customers appear to spend more per purchase vs baseline) no discernible effect on conversion (customers dont seem to purchase more frequently vs baseline) In-Progress / Pending Optimize ETL synchronization for recommendation API (merge jobs, reduce cost). Develop granular user segments via clustering; implement online updates and MLflow logging. Develop and deploy online clustering ETL & retrain ALS with new segments. Document and present new segmentation approach to stakeholders. Complete API enhancements: AI categories/interests, sorting/user preference, schema unit tests. Update MCR pipelines with new product categorization. Retrain and deploy ALS model with enhanced product categorization. Integrate live purchasing info into recommender. Finish bug fixes and master branch updates. Completed This Week ForYou: ALS user segmentation design, online update logic, and stakeholder presentation. All research/recurring review tickets closed for this sprint (ALS, metrics, categorizations). Updated/retrained ForYou pipeline and live purchases ETL. Product categorization: generated improved product names/embeddings using GenAI, logged model in MLFlow. Access to Lake Base/Postgres instance provided. Further testing in coming weeks for API integration.

Erick & Parimala

Contact Center

Lead Scoring – CTI In-Progress / Pending Continue root cause analysis for identification of missing LOAD_IDs. It appears we score MORE leads than are available in the conversion tables. This means we are scoring leads that dont actually need to be scored. Completed This Week Optimized probability range mapping for Royal brand. Automated daily email report on lead conversion. CEL requested all Galapagos & River cruises to be pushed to SVAL by default.

Erick & Gaurav

App Digital Use (RoyalOne)

RoyalOne Community In-Progress / Pending Collating first purchase analysis; prepare findings slides. Update app journey analysis data with more precise revenue logic and passenger-level filters. Query/analysis: avg precruise spend and purchase patterns by category. Ongoing app usage deep dives. Completed This Week Updated the queries for customer journey dataset and shared the notebook with Doreen for her review. Reran the purchase behavior analysis to see first purchase and its association with page views, visits, time spend and days prior to sail date.

Erick

Axiom – Guest Logs In-Progress / Pending Pilot mid-cruise NPS forecasting using daily guest log data. Design timezone-aware Guest Logs email reporting workflow. Completed This Week Mapped all initial acronyms to improve LLM context awareness in Guest Logs GenAI preprocessing step.

Ayon

Win-on-Waste

Hotfixes and integration testing in MDR Version1 pipeline

Monitoring and accuracy reporting of version1 of specialty and complementary venues

Developing Logging module for each pipeline

Developing Dashboard for WOW

Kevin & Kartik

Loyalty

Delivered matched pair design and target population for choice benefits pilot. Met with Nancy to further refine earn rates per point for RCI in preparation for co-brand card spend pilot. The second co-brand card pilot will be focused on acquisition. Power analysis is underway for the second pilot, but it is unlikely that we will be able to achieve statistically significant results, because the monthly acquisition rate for the co-brand card is quite low. OBR data delivery has been delayed until 8/18 because Oracle DBAs paused all changes for the Star Shakedown and DE was unable to push changes. OBR teams will validate new data on 8/18 prior to DS usage.

Kevin & Aagam

Revenue Management Automation (RCI):

Aagam further refined the PRE-logic analysis to include variable weighting, week-to-date considerations, and improvements to the data being used for CEL pax builds to more closely match true PRE. Clickstream basket analysis was prepared for the dual branded alignment meeting, to brainstorm on best ways to integrate it in TAP projects, however the meeting was rescheduled due to AOP and Star shakedown. Conducted a training exercise on coding and model development best practices to RM data science and both RM strategy teams to improve deliveries and reduce technical debt.

Kevin & Aagam

Revenue Management Automation (CEL):

Aagam further refined the PRE-logic analysis to include variable weighting, week-to-date considerations, and improvements to the data being used for CEL pax builds to more closely match true PRE. Clickstream basket analysis was prepared for the dual branded alignment meeting, to brainstorm on best ways to integrate it in TAP projects, however the meeting was rescheduled due to AOP and Star shakedown. Conducted a training exercise on coding and model development best practices to RM data science and both RM strategy teams to improve deliveries and reduce technical debt.

Kevin, Michelle, Aagam, Bernard, and Jesse

Revenue Management Automation (RCI):

RCI: VPS lafs were recalculated using the category table to account for neighborhoods separately from balconies. The category table however, does not have sufficient history to model so work is underway to build the data from other sources in collaboration with Chris and Eddie. SPI Track targets were adjusted to remove some of the smoothing effects on holidays, at the suggestion of Nick. This approach proved to be too aggressive, so we are instead reducing some of the smoothing to provide clear and achievable track targets. Cancellation survivor model EDA began development.

Kevin, Doug, Lamis, Atefeh, Lekha

Revenue Management Automation (CEL):

CEL: Elasticity 4.0 model has been tested with the inclusion of the all new RCI features with largely positive outcomes. These were presented to Anastasia and team who provided feedback and requested some additional exploration of features. SPI scoring model was greatly improved by removing normalization and shifting towards a calibration method which moves scores towards 1.0 without disturbing the shape of the distribution. There is additional work that is needed here, but it is a big step in the right direction to improve SPI Scores. Provided guidance to Eduardo on sky suites inclusion where additional exploration of suites builds vs suites track is needed. Inclusion of sky suites in PRE will be a large lift requiring several changes to the PRE architecture. Doug and the strategy teams identified the bug in the ICGLTD table in Alpha that was out of sync with source. This was causing errors in the gty berthing algorithms where limits were not being respected. Doug has made updates to the code to correct for the bug and passed the information on to DE on how to correct the error.

Jesse

Revenue Management Automation (SSC):

SSC: PRE is now in production and running weekly making price changes in the reservation system! Jesse is working on making slight adjustments to the logic to include week-to-date bookings at the request of the business. The business has also green lit the A/B test on PRE sailings that analysts may not adjust.

Ignacio and David

PCP Pricing Automation:

David Continued to refine CAR objectives with OBR Teams, Digital, E-Commerce, Data Engineering. Slide-deck created for communicating high-level goal for promotions automation in upcoming.

Ignacio met with the digital teams to better understand promotion upload processes. He has now developed code that can convert necessary fields into the proper format for mass promotion uploads. The next steps will be 1. Further testing of promotion uploads to hybris 2. Building a sharepoint file where Gang's teams can upload promotions and developing the code to ingest that file. 3. Expanding the logic to include more filters for customer characteristics to get closer to targeted promotions.

Cihan

PCP Pricing Automation:

Met with stakeholders to present the latest exploratory data analysis (EDA) results on ShoreX, collecting actionable feedback.

Developed and published a new EDA dashboard summarizing recent findings to improve visibility and tracking for leadership.

Carlos

E-Commerce

Resolved issue where sister brand model logs were being conflated with owner brand logs, ensuring distinct reporting for each brand.

Deployed enhanced dependency plotting algorithms to the development dashboard. The dashboard now also generates waterfall and feature importance plots, increasing model interpretability for stakeholders.

Completed fix for SHAP dependency plots in “bpxdest” two-step models within development; implementation for “uplift” and “phml” models remains underway.

Cihan

App Digital Use (RoyalOne)

App Reviews Project (Jaime): Updated topic modeling approach, applied to data from the past three weeks.

Reviewed preliminary results with Jaime; jointly discussed refinements.

Planning to finalize topic identification and transition the updated model to production next week.

Cihan

App Digital Use (RoyalOne)

Guest Services Chatbot Project (Eunha):

Responded to Eunha’s request to add an ST to the current chatbot workflow; implementation is in progress.

Identified a non-updating table affecting workflow; actively working on resolution.

Mirielle

Contact Center

Lead Prioritization (BK2CX):

Improved phone number data quality using logic provided by the Siebel team; integrated changes into pipelines for all lead types, though some records still exceed expected digit count.

Coordinated ingestion process for all lead types into Siebel; iterative testing with Siebel team ongoing.

Mirielle

Contact Center

CEL BKTOCX Lead Assignment:

Confirmed with stakeholders: leads canceling River cruises will be assigned to HVAL, Galapagos to SVAL, and others distributed between LVAL and MVAL.

Implementing a scoring model for all leads not related to River or Galapagos cruises, and a separate process for those exceptional cases, allowing for easy future deactivation.

Collaborating with Rene to refine logic for identifying River and Galapagos cruise cancellations.

Mirielle

Contact Center

Workforce Planning – Staffing Model Development:

Completed initial call volume forecasts and FTE modeling for all 13 lines of business.

Developing integrated data visualizations and an application dashboard to support forecasting and workforce planning initiatives.

Ben & Camilla

Supply Chain (IBP)

Continued feature engineering for next-generation demand models using Cursor.

Reviewed existing product cost calculation methodology in the spend report with Yan and clarified current practices.

Silversea Spend Report updated to include City Name column, enhancing data granularity.

Started planning for Silversea Order Creation project.

Compiling and providing updated statistics on model counts, forecasted items, and computations to Yan.

Initiated review of Uniform Model error calculation methodology for Yan.

Ben & Caleb

Customer Lifetime Value (CLV)

Refreshed the CLV_AGENCY table for Javier Del Rio to utilize analytics_cost_by_booking, ensuring correct cost attribution.

Analyzed median sailing counts by brand and cruise experience category, and investigated passenger counts by group size, identifying lower-than-expected values among casino passengers.

Further validation is in progress to determine if the low median sailing count is due to data quality issues."
