---
tags:
  - aagam_shah
  - arya_cheeti
  - atefeh_mahdavi
  - ayon_ghosh
  - brendan_turpin
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/revenue_management_automation_(ssc)
  - business_area/supply_chain_optimization
  - business_area/win-on-waste_(hotel_operations)
  - camila_aichele
  - erick_alfaro
  - evan_mcfall
  - jesse_bausell
  - kevin_diaz
  - lamis_amer
  - mahshad_shariatnasab
  - mert_ersoz
  - michelle_manfrini
  - project/a_b_testing_framework
  - project/asset_management_expansion
  - project/automation_upgrades
  - project/category_gapping_optimization_3.0
  - project/division-level_medallia_reports
  - project/elasticity_model_enhancements_(pre4.0)
  - project/forecasting_pipeline_expansion
  - project/gty-lead_fare_optimization_model
  - project/gty-lead_fare_optimization_model_3.0
  - project/historical_data_integration
  - project/inventory_optimization_for_silversea
  - project/loyalty_simulator_framework
  - project/miap_operating_efficiency_enhancements
  - project/pre_4.0_elasticity_enhancements
  - project/workforce_planning_tool
  - raw
  - reza_bahadori
  - weekly_update
date: "2025-12-12"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2025-12-12

## Update 1

**Date:** 2025-12-12
**Business Area:** Medallia
**Business Project:** Division-Level Medallia Reports
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

Project Updates
Presenting the "emerging topics" report to Laura Hodges next week on Dec 16th. The report is sent out once a month to CEL leadership. Meta Data Extraction
Meta data extraction for new Division level report is complete.

### Raw Update

Project Updates
Presenting the "emerging topics" report to Laura Hodges next week on Dec 16th. The report is sent out once a month to CEL leadership.
Meta Data Extraction
Meta data extraction for new Division level report is complete.
Guest Logs data is being evaluated prior to starting work early next year.
Reporting
Port-of-call specific report is delayed due to data mismatch between Unity Catalog and Medallia.
Division level email templates have been created and are on track to be delivered by end of December.
Planning to deliver the first Silversea weekly report by end of next week.
Distribution list for Fleet detractor report is expanding to include Hotel Ops leadership: (Raimund Gschaider, Jocelyn Lloret, Joao Mendonca, Richard Nentwich, christos Karavos, Nayoung Kim, IVELIN HRISTOV, FERNANDO CRAVO JORGE, Andreas Zachariou)
Extracted "Positive Shore Excurson Verbatims" by Shore Ex product for Digital. The idea is to add a new feature to app/mobile that emphasizes guest feedback for each excursion (i.e. "The scuba diving was incredible! I saw my first shark!")
Working to identify safety related commentary within the Medallia comments for Risk Management.
The team is re-exploring Genie. The team is primarily concerend with creating an evaluation dataset to baseline Genies ability to respond to questions. If Genie is found to be value-added, it could be integrated to the Axiom web app.
Modeling
The new booking level drivers model is slated for delivery by end of year.
POC Drivers Webapp integration will be the final delivery of the year.
Erick & Cristian
PCP MyCruise Recommender
Project Updates
Maintenance on ForYou-Calendar as the dev backend db was accidentally deleted by platform. The team is working on enabling a dev and prod postgres db to ensure separation of environments.
AB testing framework is being finalized this week to validate prior AB tests and to support all future AB testing needs for the Recommender (MCR).

---

## Update 2

**Date:** 2025-12-12
**Business Area:** MIAP
**Business Project:** Asset Management Expansion
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

Improved the AI agent for stability; converted the agent to use Azure AI Foundry and GPT-5.1. Conversion of the MIAP API to the MCP Server is in progress. Added fuel curve generation functionality to digital twins.

### Raw Update

Improved the AI agent for stability; converted the agent to use Azure AI Foundry and GPT-5.1.
Conversion of the MIAP API to the MCP Server is in progress.
Added fuel curve generation functionality to digital twins.
Met with Decarb team and aligned on strategy for presenting Diagnostic Tools in the Decarb section of the GMO App.
Met with Jan Solum and discussed using IT Newbuild Innovation funds for real-time safety KPIs. Pending NDA signing with the American Bureau of Shipping; afterwards we will discuss a partnership in which they act as consultants.
Met with Brian Sørensen to discuss Asset Management AI initiatives. Brian recommended Patrick van Zandwijk, Sr. Director of Asset Management, as an AI ambassador.
Met with Newbuild Mission Control to discuss AI initiatives.

---

## Update 3

**Date:** 2025-12-12
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** Unidentified

### Summarized Update

This week:
Loaded data for the missing days in the shipboard table. All data is now available in the shipboard table. Changed the DLT approach for stream shipboard to the Federation framework and deployed it to production for the stream shipboard table.

### Raw Update

This week:
Loaded data for the missing days in the shipboard table. All data is now available in the shipboard table.
Changed the DLT approach for stream shipboard to the Federation framework and deployed it to production for the stream shipboard table.
Added additional fields such as environment and dataframe size to the log file for the MIAP REST API.
Added columns and curated data in the silver table for the MIAP logging mechanism.
Next week:
Recreate the stream shipboard table in production and trigger the workflow.
Deploy the logging mechanism to production.
Refactor the shipboard code so it handles data from different sources.

---

## Update 4

**Date:** 2025-12-12
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[arya_cheeti/overview_arya_cheeti|Arya Cheeti]]

### Summarized Update

Finished optimizing power plant FACT models. Optimizing parameters for DG, GTG, and STG power plant models. Built a prototype chatbot for New Build that uses agentic orchestration.

### Raw Update

Finished optimizing power plant FACT models.
Optimizing parameters for DG, GTG, and STG power plant models.
Built a prototype chatbot for New Build that uses agentic orchestration.
Developing a methodology to track degradation of windings and bearings for Azipods.

---

## Update 5

**Date:** 2025-12-12
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

Completed the new total propulsion power implementation in the Fuel Forecast API. Fixed various implementation bugs in total propulsion power. Created 13 tests for total propulsion power to cover edge cases.

### Raw Update

Completed the new total propulsion power implementation in the Fuel Forecast API.
Fixed various implementation bugs in total propulsion power.
Created 13 tests for total propulsion power to cover edge cases.
Redesigned the ALS Compressor Power component of the Fuel Forecast API to match the format of the new total propulsion power component; implementation is still in progress.

---

## Update 6

**Date:** 2025-12-12
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]]

### Summarized Update

Completed the metric comparison between the old Fuel Forest model and the digital twin for the service power area. Started the pipeline for accuracy comparison of fuel consumption between actual values in FACTS and predictions from the digital twin voyage model simulator.

### Raw Update

Completed the metric comparison between the old Fuel Forest model and the digital twin for the service power area.
Started the pipeline for accuracy comparison of fuel consumption between actual values in FACTS and predictions from the digital twin voyage model simulator.

---

## Update 7

**Date:** 2025-12-12
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** [[mahshad_shariatnasab/overview_mahshad_shariatnasab|Mahshad Shariatnasab]]

### Summarized Update

Identified the root causes of high error and low accuracy for NO and EG by fixing issues in the service power model and related data. As a result, overall model accuracy has improved. Discovered plotting issues for GMO and inconsistencies in table naming; corrected those where possible.

### Raw Update

Identified the root causes of high error and low accuracy for NO and EG by fixing issues in the service power model and related data. As a result, overall model accuracy has improved.
Discovered plotting issues for GMO and inconsistencies in table naming; corrected those where possible.
Worked on the digital twin library and traced the OFB data issue to a function that assumed all ships lack boilers, causing the output to be zero. Currently implementing a fix for this assumption.

---

## Update 8

**Date:** 2025-12-12
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** Unidentified

### Summarized Update

Completed testing of the new GMO Dynamic Filter for the MIAP web app and proposed functional improvements. Fixed an issue where ships that do not use LNG still had the pilot fuel heat power ratio feature enabled. Fixed an issue with the virtual GTG power calculation.

### Raw Update

Completed testing of the new GMO Dynamic Filter for the MIAP web app and proposed functional improvements.
Fixed an issue where ships that do not use LNG still had the pilot fuel heat power ratio feature enabled.
Fixed an issue with the virtual GTG power calculation.
Fixed an issue in the mapping of power plant serial numbers to configuration numbers in the power plant info database (this was causing issues in service power).
Completed the MVP of the pilot fuel heat power model on IC, ST, NO, and UT. Still waiting on PR approval; further model performance improvements are required before it is useful.
Guided Arya in tuning individual and overall power plant models; Arya has been a great help.
Fixed an issue in calculating features for ships without VPS fuel reports.

---

## Update 9

**Date:** 2025-12-12
**Business Area:** Loyalty
**Business Project:** Loyalty Simulator Framework
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Collaborated with Revenue Planning, Revenue management and loyalty teams to refresh category mapping and conversion rates following feedback from Michael Bayley to base mappings off GTR APDs, rather than NTR. GTR calculations were provided by Rev Planning as the field is not readily available in VCAP. Specific category mappings changed slightly with the new methodology, but general guidance remains unchanged.

### Raw Update

Collaborated with Revenue Planning, Revenue management and loyalty teams to refresh category mapping and conversion rates following feedback from Michael Bayley to base mappings off GTR APDs, rather than NTR. GTR calculations were provided by Rev Planning as the field is not readily available in VCAP. Specific category mappings changed slightly with the new methodology, but general guidance remains unchanged. The data has been refreshed several times and APD values and matching shift slightly as pricing updates. This reiterates the need for an annual refresh supported by the data science team. Laura Hodges directed loyalty teams to convey the annual recalculation of conversion to guests.

---

## Update 10

**Date:** 2025-12-12
**Business Area:** Unclassified
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

PCP:
Developed Initial EDA on RBC pricing. Further validation of data inputs is required before drawing any conclusions, but initial methodology to be presented to Gang and team Friday 12/12. Onboard product teams are regularly changing promotions by tour date trying to ensure RBC is as close to capacity as possible.

### Raw Update

PCP:
Developed Initial EDA on RBC pricing. Further validation of data inputs is required before drawing any conclusions, but initial methodology to be presented to Gang and team Friday 12/12. Onboard product teams are regularly changing promotions by tour date trying to ensure RBC is as close to capacity as possible. Because of the near-term launch (12/23 first tour date), I am proposing a two stage approach:
(1)A TAP project proposing promotional changes for close in management based on percentage to capacity, recent pricing action, booking velocity and segment indexing supported by deep EDA and dashboarding. This will provide a quick win replicating what the product teams are manually doing in a more sophisticated way.
(2) A/B testing base price and promotion changes for a set number of sailings. This will take longer to develop, implement and measure, but will provide a more scientific approach to price points for RBC in peak season. The A/B test should be supported by findings from the TAP project and EDA.

---

## Update 11

**Date:** 2025-12-12
**Business Area:** Revenue Management (RCI)
**Business Project:** Automation Upgrades
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Black Friday rules are being disabled after the Holiday Break, meaning raises will no longer be paused for Wave. As a follow up to the Tri-branded meeting on planning, we met with Nick and Anastasia to discuss Q1 planned deliveries. Nick and Anastasia agreed with the current priorities but will review the list of projects and provide more detailed feedback after review.

### Raw Update

Black Friday rules are being disabled after the Holiday Break, meaning raises will no longer be paused for Wave.
As a follow up to the Tri-branded meeting on planning, we met with Nick and Anastasia to discuss Q1 planned deliveries. Nick and Anastasia agreed with the current priorities but will review the list of projects and provide more detailed feedback after review. We are also creating a "wishlist" of all future automation projects for long-term planning.
We conducted a half day meeting with the Itravel product team, Data Engineering and revenue strategy teams to build alignment on automation projects and requirements for iTravel to support existing automation and releases planned prior to iTravels planned release.

---

## Update 12

**Date:** 2025-12-12
**Business Area:** Revenue Management (CEL)
**Business Project:** Elasticity Model Enhancements (PRE4.0)
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Elasticity 4.0 Model has been released for CEL with vast improvements in model performance and a brand level model correcting overfitting concerns. This release will be quickly followed by the release of DART for the celebrity brand to account for recent demand. Both brands are now caught up and operating on the same version of the base elasticity model.

### Raw Update

Elasticity 4.0 Model has been released for CEL with vast improvements in model performance and a brand level model correcting overfitting concerns. This release will be quickly followed by the release of DART for the celebrity brand to account for recent demand. Both brands are now caught up and operating on the same version of the base elasticity model.
As a follow up to the Tri-branded meeting on planning, we met with Nick and Anastasia to discuss Q1 planned deliveries. Nick and Anastasia agreed with the current priorities but will review the list of projects and provide more detailed feedback after review. We are also creating a "wishlist" of all future automation projects for long-term planning.

---

## Update 13

**Date:** 2025-12-12
**Business Area:** Supply Chain
**Business Project:** Inventory Optimization for Silversea
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Caleb
CLV
Key accomplishments
• Finalized the weekly update to Cory, covering CAR updates and Celebrations Deep Dives:
o Continued Celebrations EDA, cutting celebrators by product, ship class, cabin class, season, product, channel, etc., to better understand inventory preferences of celebrators vs. never-celebrators and why celebrators may under-index despite relatively high spend. o Identified consumers who have celebrated and tracked their preferences when celebrating vs.

### Raw Update

Caleb
CLV
Key accomplishments
• Finalized the weekly update to Cory, covering CAR updates and Celebrations Deep Dives:
o Continued Celebrations EDA, cutting celebrators by product, ship class, cabin class, season, product, channel, etc., to better understand inventory preferences of celebrators vs. never-celebrators and why celebrators may under-index despite relatively high spend.
o Identified consumers who have celebrated and tracked their preferences when celebrating vs. not celebrating, to explore Cory’s question of whether a celebrating sailing brings out the “best version” of the customer.
• Assisted with the West Coast × CLV project, comparing drive guests in CA vs. NY + TX.
• Assisted with McKinsey survey work: pulling, cleaning, validating data, sizing customers’ interest in different trip types, and comparing across regions.
Carlos
E Commerce
Key accomplishments
• Completed analysis of consumer scoring transition causes:
o Performed EDA and segmentation of shape values.
o Manually analyzed correlation vs. causation after segments were created.
o Presented findings to stakeholders, confirming that expected score changes are driven by changes in top features (consumer activity signals and new data).
Mirielle
Contact Center
LP OFTO CX (Royal & Celebrity / Siebel)
Key accomplishments
• Completed iterative testing with the Siebel team.
• Tested the ETL production pipeline for delayed agencies (2 day delay for phone numbers starting with 0080%) and normal agencies (no delay).
• In a stakeholder meeting, aligned on treatment of delayed agencies that may have already converted:
o Acknowledged that offers from delayed agencies can convert before processing.
o Confirmed that, with the SBOFRD table, we currently cannot check conversion status prior to processing.
o Given the very low number of such leads per day, agreed (per Amy) to proceed to production now and later design an approach to filter out converted leads from delayed agencies.
Production readiness (target: 9–10 December 2025)
• Received from Siebel the max PROD sequence_id to start with: 4154168492.
• Executed production setup steps:
o Set the max sequence_id for Royal.
o Set the max sequence_id for Celebrity.
o Set the max sequence_id for leads from delayed agencies (Celebrity).
o Switched file sources from stage (_test files) to production (removed _test).
• Confirmed there were no new leads at the shared max sequence_id = 4154168492.
• Assessed expected number of leads to process before new leads begin flowing:
o Royal: Max saved sequence_id is 4151544286; difference to PROD max (4154168492) is ~2,624,206.
o Celebrity: Max saved sequence_id is 4151544283; difference to PROD max is ~2,624,209.
In progress / next
• Next: Trigger the pipeline with all available leads (no filter at max sequence_id 4154168492).
o Deployment of Royal propensity model.
o Deployment of Celebrity propensity model.
• Setting up max sequence_id in the production data science workflow and releasing to production.
• Resolved a permissions issue accessing a volume table in UC and configured notification emails for failures to:
o mfeudjio@rccl.com
o bfowler@rccl.com
o cgonzalezandarcio@rccl.com
o atomszay@rccl.com

---

## Update 14

**Date:** 2025-12-12
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

Mirielle
Contact Center: Workforce Planning – North America (App Migration)
• Ongoing migration of the Workforce Planning application from Databricks to Azure Container Apps. • Held two working sessions with Mukund / Platform team to progress the migration.

### Raw Update

Mirielle
Contact Center: Workforce Planning – North America (App Migration)
• Ongoing migration of the Workforce Planning application from Databricks to Azure Container Apps.
• Held two working sessions with Mukund / Platform team to progress the migration.

---

## Update 15

**Date:** 2025-12-12
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

Workforce Planning – International & Casino (Databricks App)
• Met with Nico’s team to review app content. • Updated the team view within the app. • Next: Integrate call volume forecast into the app.

### Raw Update

Workforce Planning – International & Casino (Databricks App)
• Met with Nico’s team to review app content.
• Updated the team view within the app.
• Next: Integrate call volume forecast into the app.
Cihan
Digital RoyalOne: Digital – Qualtrics Survey (Owner: Jaime Stoelar)
Status: Completed
• Project successfully completed and delivered.
• The model is currently in use by the Digital team.
Digital – Guest Services Chatbot (Owner: Eunha Kim)
Status: In Progress
• Met with stakeholders to provide updates on the current escalation logic for “bot_not_wanted” scenarios.
• Shared relevant data with the Digital BI Analyst, enabling her to generate new data/charts for the main dashboard.
• Participated in the weekly stakeholder stand up, addressing questions on escalation types and discussing strategies to identify patterns in other escalation types.
Cihan
PCP Onboard Revenue – Waterpark
Project: OBR Waterpark PRE (Owner: Gang Wang)
Status: In Progress
• Continued to address the view table performance issue; engaged the Data Engineering (DE) team as queries against the view are significantly delayed.
• Met with Jorge and Anastasia to share current PRE status and gather their input.
• Identified a data issue where waterpark capacity does not consistently equal 1,760 when summing inventories.
• Engaged in debugging to pinpoint the root cause of the capacity discrepancy.
• Met with Ignacio to finalize data preparation for the optimization phase.
• Currently focusing on the optimization aspects of the PRE.

---

## Update 16

**Date:** 2025-12-12
**Business Area:** Win-on-Waste
**Business Project:** Forecasting Pipeline Expansion
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

Developed a backup itinerary for every voyage/ship/restaurant so each itinerary always includes seadays that can serve the forecast when short-notice itinerary changes occur due to weather. This ensures the PAR PULL process and FPMS forecasting run seamlessly without interruption. Testing and Couchbase integration of the backup itinerary for specialty restaurants and MDR is underway and is expected to be completed next week.

### Raw Update

Developed a backup itinerary for every voyage/ship/restaurant so each itinerary always includes seadays that can serve the forecast when short-notice itinerary changes occur due to weather. This ensures the PAR PULL process and FPMS forecasting run seamlessly without interruption.
Testing and Couchbase integration of the backup itinerary for specialty restaurants and MDR is underway and is expected to be completed next week.
Built and tested a separate pipeline for 150+ bar counters per ship; production rollout is scheduled for January per product team plan.
Continued business-as-usual support to ship chefs.

---

## Update 17

**Date:** 2025-12-12
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model
**People:** Unidentified

### Summarized Update

Constructed visualizations to demonstrate brand GTY behavior by meta product.Currently working on tying results to revenue and tracking metrics. Conducted additional EDA to identify the best source for calculating stockout rate for both pre- and post-replenishment periods.Attempted use of feature store data was unsuccessful (insufficient historical data).Built source data from scratch using Revenue Planning availability history, tied to brand-specific virtual guarantee categories. Coding notebook to calculate daily stockout rate due to GTY unavailability.

### Raw Update

Constructed visualizations to demonstrate brand GTY behavior by meta product.Currently working on tying results to revenue and tracking metrics.
Conducted additional EDA to identify the best source for calculating stockout rate for both pre- and post-replenishment periods.Attempted use of feature store data was unsuccessful (insufficient historical data).Built source data from scratch using Revenue Planning availability history, tied to brand-specific virtual guarantee categories.
Coding notebook to calculate daily stockout rate due to GTY unavailability.

---

## Update 18

**Date:** 2025-12-12
**Business Area:** CEL Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model 3.0
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

Due to the availability inaccuracies in the feature stores, my use of these tables in DART was invalidated. To resolve this, I re-ingested all data from verified sources and refactored the code to enforce correct logic and price calculations. Additionally, I implemented manual computation of key metrics to replace the flawed features in the original FS tables.

### Raw Update

Due to the availability inaccuracies in the feature stores, my use of these tables in DART was invalidated. To resolve this, I re-ingested all data from verified sources and refactored the code to enforce correct logic and price calculations. Additionally, I implemented manual computation of key metrics to replace the flawed features in the original FS tables.
To illustrate the importance of this source shift, the newly calculated trade-up for Alaska dropped by 13% compared to the original calculations, revealing how inaccurate the previous data was.
Due to the same Feature Stores issues, I am in the process of refactoring the training data for the 2.0 models to correctly account for GTY bookings that the FS tables did not see. I will pull the pricing and lead category information, verifying it matches other trusted sources.

---

## Update 19

**Date:** 2025-12-12
**Business Area:** CEL Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model 3.0
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

Adjusted weighting in training data for EBM and seeing much more balanced predictions. Validating outputs with business, plotting booking shares and trade-ups for each of the four tiers versus the three relative price gaps. Initial assessment of predictions matches business intuition but a deeper dive into how all 3 gaps interact is necessary and in progress.

### Raw Update

Adjusted weighting in training data for EBM and seeing much more balanced predictions. Validating outputs with business, plotting booking shares and trade-ups for each of the four tiers versus the three relative price gaps.
Initial assessment of predictions matches business intuition but a deeper dive into how all 3 gaps interact is necessary and in progress.
I am also conducting an analysis of the gty booking share predictions from EBM compared to the trade-ups predictions from the 2.0 model that is in production. Slight differences are expected because the new model accounts for the entire tier stack and the interactions of all the prices will pick up different behaviors than the 2.0 model that only considered the gty-lead gap.

---

## Update 20

**Date:** 2025-12-12
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Completed code refactoring, parametrization and reporting structures. One part is still missing related to finalizing the rule to trade-off between PRE4.0 and optimization outputs to finalize final recs to be passed over to the business rules logic, etc. Completed presentation to Stakeholders with visuals and metrics updated to reflect this week's results (in terms of comparing PRE4.0, actual and optimal results.)
For proper comparison against PRE and the optimization price change recs, I refined the logic to pull live RM prices to rule out any promo effects (such as BOGO and replacement values).

### Raw Update

Completed code refactoring, parametrization and reporting structures. One part is still missing related to finalizing the rule to trade-off between PRE4.0 and optimization outputs to finalize final recs to be passed over to the business rules logic, etc.
Completed presentation to Stakeholders with visuals and metrics updated to reflect this week's results (in terms of comparing PRE4.0, actual and optimal results.)
For proper comparison against PRE and the optimization price change recs, I refined the logic to pull live RM prices to rule out any promo effects (such as BOGO and replacement values). This is crucial to ensure we're comparing against the actual price change decisions made by the RM teams and not as a result of promos applied/dropped, etc.

---

## Update 21

**Date:** 2025-12-12
**Business Area:** CEL Revenue Management
**Business Project:** Category Gapping Optimization 3.0
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Completed the logic to quantify the shared demand among similar sailings. Similar sailings are those with similar sail month, year, meta and cat class. For each bkg WOY, the demand for similar sailings is aggregated and mapped to each sailing's WTS and the proportion of total demand is calculated for each sailing/wts in order to use these as upper limits on weekly bookings while building the optimal tracks.

### Raw Update

Completed the logic to quantify the shared demand among similar sailings. Similar sailings are those with similar sail month, year, meta and cat class. For each bkg WOY, the demand for similar sailings is aggregated and mapped to each sailing's WTS and the proportion of total demand is calculated for each sailing/wts in order to use these as upper limits on weekly bookings while building the optimal tracks.
Completed a presentation to stakeholders for this week's progress checkpoint and next week's meeting with the stakeholders.

---

## Update 22

**Date:** 2025-12-12
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Completed the presentation to stakeholder's - scheduled next week.

### Raw Update

Completed the presentation to stakeholder's - scheduled next week.

---

## Update 23

**Date:** 2025-12-12
**Business Area:** CEL Revenue Management
**Business Project:** Elasticity Model Enhancements (PRE4.0)
**People:** Unidentified

### Summarized Update

TESTING in QA
Deliverables:
This is a big win this week. We have achieved updating elasticities for CEL enabling them to enjoy similar capabilities to the RCI Brand. Pushed updated elasticity and PRE notebooks from my branch to develop in ADF and ran QA checks; initial QA failed due to intermediate tables created from a hard-coded environment variable.

### Raw Update

TESTING in QA
Deliverables:
This is a big win this week. We have achieved updating elasticities for CEL enabling them to enjoy similar capabilities to the RCI Brand.
Pushed updated elasticity and PRE notebooks from my branch to develop in ADF and ran QA checks; initial QA failed due to intermediate tables created from a hard-coded environment variable.
Corrected the hard-coded environment variable usage and removed/cleaned the environment-specific intermediate tables, then pushed fixes to develop.
Discovered the PRE pipeline only executed PRE notebooks and did not run elasticity model notebooks that create/update the elasticity model output table (an input to PRE notebooks).
Created a master notebook that sequentially runs all elasticity model notebooks to ensure the elasticity output table is created/updated consistently.
Added a run command for the master elasticity notebook into PRE_Lite_main so the PRE pipeline triggers elasticity processing before PRE notebooks run.
After integrating the master elasticity run, re-ran QA and the pipeline succeeded; the QA output validated as expected.
Worked closely with Anastasia and Monica to validate the QA output file and confirm the new elasticities meet expectations.
CEL Team is Targeting release by Friday so the new elasticities will be live on Monday 12/8
Ran in QA again for sanity check and with help of  @Eswar Chand Thokala  pushed all the changes from dev to prod
Potential future issue: None

---

## Update 24

**Date:** 2025-12-12
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

Deliverables:
This week I worked on creating the automated process for gathering the historical and current prices for the process which will be run weekly. Additionally, I also worked on gathering the mandatory occupancy for the past 3 weeks. Furthermore, I additionally calculated the bundled fare and average prices for the 3 week and 1 week windows.

### Raw Update

Deliverables:
This week I worked on creating the automated process for gathering the historical and current prices for the process which will be run weekly. Additionally, I also worked on gathering the mandatory occupancy for the past 3 weeks. Furthermore, I additionally calculated the bundled fare and average prices for the 3 week and 1 week windows.
Will be presented to stakeholders soon after additional validation.

---

## Update 25

**Date:** 2025-12-12
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

Promo code trends and REPLACEMENT_VALUE deep dive
I analyzed promo code usage across WTS buckets and found that TACTICALS and REPLACEMENT_VALUE promotions have a higher share in close-in windows, consistently across all meta-products. A deeper dive into REPLACEMENT_VALUE—price replacement offers that can be up to 20% below prevailing rates—showed that usage is highly concentrated in 7N Caribbean and Short Caribbean sailings. Historically, these offers were used only within the Final Payment window (≤ 90 days), but due to soft demand, they have recently expanded to sailings through June 2026, particularly on off-peak departures that are harder to fill.

### Raw Update

Promo code trends and REPLACEMENT_VALUE deep dive
I analyzed promo code usage across WTS buckets and found that TACTICALS and REPLACEMENT_VALUE promotions have a higher share in close-in windows, consistently across all meta-products. A deeper dive into REPLACEMENT_VALUE—price replacement offers that can be up to 20% below prevailing rates—showed that usage is highly concentrated in 7N Caribbean and Short Caribbean sailings.
Historically, these offers were used only within the Final Payment window (≤ 90 days), but due to soft demand, they have recently expanded to sailings through June 2026, particularly on off-peak departures that are harder to fill.
For this analysis, I considered bookings from July 2025 onward and confirmed that nearly all REPLACEMENT_VALUE usage originates from just two meta-products: 7N Caribbean and Short Caribbean. I also calculated the share of REPLACEMENT_VALUE within each WTS bucket—for example, in the 0–7 WTS window, 17.5% of all 7N Caribbean bookings came from REPLACEMENT_VALUE, indicating strong reliance close-in.

---

## Update 26

**Date:** 2025-12-12
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

Identification of recent sailings using REPLACEMENT_VALUE and early rule development
To support rule development, I identified all sailings from the last four weekly reads that used the REPLACEMENT_VALUE promotion. These sailings were grouped into intensity buckets based on how many passengers booked under the promotion. The bucketed table shows that Replacement usage is not evenly distributed.

### Raw Update

Identification of recent sailings using REPLACEMENT_VALUE and early rule development
To support rule development, I identified all sailings from the last four weekly reads that used the REPLACEMENT_VALUE promotion. These sailings were grouped into intensity buckets based on how many passengers booked under the promotion.
The bucketed table shows that Replacement usage is not evenly distributed. Instead, it is highly concentrated in the highest-intensity bucket, where sailings have exceptionally large numbers of passengers using this promotion. These sailings represent the strongest candidates for deeper review, as they are most likely to influence performance and may provide clearer insight into whether REPLACEMENT_VALUE contributes to missing or beating track.

---

## Update 27

**Date:** 2025-12-12
**Business Area:** RCI Revenue Management
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

Track performance alignment and next steps for rule development
Based on candidate sailings, I have identified which sailings beat or miss track and quantified how much REPLACEMENT_VALUE contributed to actual bookings for each sailing. With this foundation complete, the next step is to perform deeper analysis on these sailing to understand how promo presence and promo contribution relate to track deviation and integrating these rules into PRE workflows.

### Raw Update

Track performance alignment and next steps for rule development
Based on candidate sailings, I have identified which sailings beat or miss track and quantified how much REPLACEMENT_VALUE contributed to actual bookings for each sailing. With this foundation complete, the next step is to perform deeper analysis on these sailing to understand how promo presence and promo contribution relate to track deviation and integrating these rules into PRE workflows.

---

## Update 28

**Date:** 2025-12-12
**Business Area:** SSC Revenue Management
**Business Project:** A/B Testing Framework
**People:** [[jesse_bausell/overview_jesse_bausell|Jesse Bausell]]

### Summarized Update

Universal A/B Framework
Consistent with our meetings, I created a library that separates potential A/B test subjects according to user-specified “hard constraints”. Through a yaml file, user specifies which fields within the input table should be used to group the test subjects (e.g., voyages) and whether these fields need to be identical, or exist within a range (e.g., sailing dates 10 days apart are still acceptable). This code is universal, yet simple to maintain.

### Raw Update

Universal A/B Framework
Consistent with our meetings, I created a library that separates potential A/B test subjects according to user-specified “hard constraints”. Through a yaml file, user specifies which fields within the input table should be used to group the test subjects (e.g., voyages) and whether these fields need to be identical, or exist within a range (e.g., sailing dates 10 days apart are still acceptable). This code is universal, yet simple to maintain. It requires only two inputs and we should be able to incorporate it within a variety of different frameworks. Once I formally pass this framework to our team (Friday), team members will update it by applying “Gecko” matching capabilities.

---

## Update 29

**Date:** 2025-12-12
**Business Area:** Unclassified
**People:** [[evan_mcfall/overview_evan_mcfall|Evan McFall]]

### Summarized Update

SPI weekly delivery summary
This week we landed a major upgrade to the SPI scoring pipeline and model stack. The refactor replaced hard-coded logic with an adaptive, transformer-based feature pipeline (temporal encoding, feature reduction via SHAP+bagged RF, dynamic selectors), and moved the learner to LightGBM with improved backtesting (time-series CV using single-point splits) to prevent leakage. These changes, along with speed optimizations (standardized dataclasses, faster SQL, pseudo-cache in ETL), materially strengthened stability and accuracy of the SPI predictions.

### Raw Update

SPI weekly delivery summary
This week we landed a major upgrade to the SPI scoring pipeline and model stack. The refactor replaced hard-coded logic with an adaptive, transformer-based feature pipeline (temporal encoding, feature reduction via SHAP+bagged RF, dynamic selectors), and moved the learner to LightGBM with improved backtesting (time-series CV using single-point splits) to prevent leakage. These changes, along with speed optimizations (standardized dataclasses, faster SQL, pseudo-cache in ETL), materially strengthened stability and accuracy of the SPI predictions.
On performance, the overall model shows ~50% improvement on MAE / CORR versus the original baseline, aligned with results from Kevin’s refactor and the new model configuration. Brand-level lifts follow the same pattern: RCI achieved ~62% improvement (normalized MAE / CORR), while CEL delivered ~27% improvement (normalized MAE / CORR). A brand breakout will follow, but the early cuts indicate the gains are consistent across segments. (Metrics provided by you.)
Looking ahead, the team has queued next steps that build on this week’s foundation: enhancing “length-on-meta” and “sailing-nights change” encodings, instituting a hierarchy for segmented models where sample sizes permit, and carefully testing synthetic data (GAN) only for train augmentation—not evaluation. We also established connectors for exogenous signals (FRED macro data, Google Trends) with appropriate normalization (e.g., order differencing) so we can further explain residual variance and continue driving SPI accuracy.

---

_Source: 20251212 - Weekly Rafeh & Matt Updates (Raw).docx_