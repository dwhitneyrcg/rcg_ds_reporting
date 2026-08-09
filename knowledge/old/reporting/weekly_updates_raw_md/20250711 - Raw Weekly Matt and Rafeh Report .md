---
tags:
  - aagam_shah
  - atefeh_mahdavi
  - ayon_ghosh
  - bernard_kai_wittmaack
  - brendan_turpin
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/customer_lifetime_value_(corporate_planning)
  - business_area/customer_targeting_(e-commerce)
  - business_area/hr
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/win-on-waste_(hotel_operations)
  - camila_aichele
  - carlos_gonzalez_andarcio
  - cihan_ulus
  - ignacio_villasmil
  - jesse_bausell
  - kartik_ullal
  - kevin_diaz
  - lamis_amer
  - mahshad_shariatnasab
  - mehdi_assefi
  - mert_ersoz
  - michelle_manfrini
  - parimala_kettymuthu
  - project/automated_pricing_expansion
  - project/booking_propensity_models
  - project/conversational_ivr
  - project/cresta_ai_analytics_tools
  - project/cross-brand_credit_card_strategy
  - project/fleetwide_energy_monitoring
  - project/forecasting_pipeline_expansion
  - project/genie_application_enhancements
  - project/historical_data_integration
  - project/improved_forecasting_accuracy
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/miap_operating_efficiency_enhancements
  - project/nps_drivers_analysis_for_alert_system
  - project/offer_to_cancel_(oftocx)_model_(rci_&_cel)
  - project/pre_4.0_elasticity_enhancements
  - project/spend-to-save_pilot_analysis
  - project/workforce_planning_tool
  - raw
  - reza_bahadori
  - weekly_update
date: "2025-07-11"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2025-07-11

## Update 1

**Date:** 2025-07-11
**Business Area:** Loyalty
**Business Project:** Spend-to-Save Pilot Analysis
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Continued early peeking analysis on spend to save pilot. Although the majority of the effort was spent on identifying net new guests through propensity models, this will not be shared with the EC as the loyalty teams, want to wait until more time has passed to allow for more FCCs to be redeemed. We will share early peeking analysis on spend with the EC, highlighting that there has been a more noticeable trend in short Caribbean spend increases than 7N Caribbean.

### Raw Update

Continued early peeking analysis on spend to save pilot. Although the majority of the effort was spent on identifying net new guests through propensity models, this will not be shared with the EC as the loyalty teams, want to wait until more time has passed to allow for more FCCs to be redeemed. We will share early peeking analysis on spend with the EC, highlighting that there has been a more noticeable trend in short Caribbean spend increases than 7N Caribbean. Following the steerco where the EC deck was shared, several more analyses were requested, mostly focused on FCC redemption. Further refined menus and guidance on the second pilot, which will be choice benefits. Brian's last day was this week. He completed knowledge transfer sessions with Kartik before leaving.

---

## Update 2

**Date:** 2025-07-11
**Business Area:** Revenue Management Automation (RCI)
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Kevin
Revenue Management Planning (RCI): Developed a 6 month roadmap for releases approved by both Nick and Anastasia. Began weekly alignment meetings with both brands to build a focus on joint development rather than silod workstreams.

### Raw Update

Kevin
Revenue Management Planning (RCI): Developed a 6 month roadmap for releases approved by both Nick and Anastasia. Began weekly alignment meetings with both brands to build a focus on joint development rather than silod workstreams.

---

## Update 3

**Date:** 2025-07-11
**Business Area:** Revenue Management Automation (RCI)
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Kevin
Revenue Management Planning (CEL): Developed a 6 month roadmap for releases approved by both Nick and Anastasia. Began weekly alignment meetings with both brands to build a focus on joint development rather than silod workstreams.

### Raw Update

Kevin
Revenue Management Planning (CEL): Developed a 6 month roadmap for releases approved by both Nick and Anastasia. Began weekly alignment meetings with both brands to build a focus on joint development rather than silod workstreams.

---

## Update 4

**Date:** 2025-07-11
**Business Area:** HR
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]], [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Experiments (Atefeh): I performed experiments using LightGBM to estimate price elasticity at the meta_cc level. Key points include Applied hyperparameter tuning via Optuna, regularization, and target encoding based on mean target value of categorical features. Achieved high predictive performance with R² exceeding 90% across core meta-products.

### Raw Update

Experiments (Atefeh): I performed experiments using LightGBM to estimate price elasticity at the meta_cc level. Key points include Applied hyperparameter tuning via Optuna, regularization, and target encoding based on mean target value of categorical features. Achieved high predictive performance with R² exceeding 90% across core meta-products.
However, the elasticity outputs from LightGBM were inconsistent in magnitude and sign, indicating the model's focus on overall demand prediction often masks the marginal effects of price. Consequently, I reverted to Poisson regression for better interpretability and stable elasticity curves.

---

## Update 5

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Elasticity Model 4.0 Refinement and Validation
Originally when the model is trained on large bin sizes (Spline-based on hard-coded A bins) metrics are a lot better because aggregating the data over larger bins reduces noise. However, when using this model to predict on smaller intervals and on testing performance is poor - In addition, elasticity plots tend to be ‘more flat’ with nearly 3 steps in most cases (since we have almost 3 large bins between 0-70 wts) which is not visually appealing or accepted by the business team to have constant elasticities over several weeks. On the other hand - training the models on smaller bin sizes (like 5 weeks to sail) yields poorer results.

### Raw Update

Elasticity Model 4.0 Refinement and Validation
Originally when the model is trained on large bin sizes (Spline-based on hard-coded A bins) metrics are a lot better because aggregating the data over larger bins reduces noise. However, when using this model to predict on smaller intervals and on testing performance is poor - In addition, elasticity plots tend to be ‘more flat’ with nearly 3 steps in most cases (since we have almost 3 large bins between 0-70 wts) which is not visually appealing or accepted by the business team to have constant elasticities over several weeks.
On the other hand - training the models on smaller bin sizes (like 5 weeks to sail) yields poorer results.
So, as a tradeoff between these 2 performance criterion that are equally important to the business - Instead of aggregating and averaging the price and bookings over the bin I imported the data at the granularity of 5 weeks to sail while smoothing over each bin to reduce noise (instead of averaging) - So, I am still maintaining more granular data for better visuals and more realistic elasticity values while training the models on larger bin sizes yielding better model metrics.
Additionally - for validation purposes, I calculated the elasticity analytically from historical data (% change in bkgs/ % change in price) over the sailings booking window. Used these Analytical Elasticity curves to validate the model-generated elasticities - Should be discussing results with the biz tomorrow.
I am working on putting together final slides and visuals to present the upgraded model results with the biz for their validation and final approvals - below are some of the results (metrics and elasticity plots)
Production Code Elasticity Refactoring
Working on refactoring the elasticity model codebase to incorporate the following key scalability features:
(1) Data Preparation
→ Pull VPS pricing data from Feature Store
→ Apply filters and joins including max week-to-sale: 70, valid read_date range, etc.
→ Map sail_nights groups and wts spline bins cols (from JSON)
→ Apply smoothing within each WTS bin (rolling window = 3)
→ Write transformed Spark DataFrame to Unity Catalog
↳ (This becomes the input for model training)
(2)Experimentation Data
→ Define experimentation strategy: Vary WTS binning strategies - price transformation techniques
→ Generate experimentation grid: Iterate over all combinations of meta, cat_class, bin, scaling
→ Save grid as experimentation DataFrame and write to Unity Catalog
(3) Model Training
→ Read training data and experimentation grid from Unity Catalog
→ For each row in the experimentation grid:
Train model per meta-product × cat_class × binning × transformation
Compute scores and select best params for each meta - cc model
For the best models - stores betas, alphas, Elasticity, Predictions (train/test)
→ Return two output DataFrames and writes them to uc:
(4) Model metrics + params + pickles + coeffs
Full data + Elasticity + y_pred
Model Evaluation
→ Read model outputs and metrics from Unity Catalog
→ Visualize:
Elasticity curves
Predicted vs. actual (train/test)
Residuals and prediction errors

---

## Update 6

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[kartik_ullal/overview_kartik_ullal|Kartik Ullal]]

### Summarized Update

RCI RM AB Testing
Updated the sailing list for the T4 for test by removing offpeak sailings and creating a new sailing list for Alaska sailings. Re-ran power analysis for spend to save pilot independently for 7N and Short caribbean
Compared booking propensity for 60 days with 12 months to see if there was an increase in bookings for a guest

### Raw Update

RCI RM AB Testing
Updated the sailing list for the T4 for test by removing offpeak sailings and creating a new sailing list for Alaska sailings.
Re-ran power analysis for spend to save pilot independently for 7N and Short caribbean
Compared booking propensity for 60 days with 12 months to see if there was an increase in bookings for a guest

---

## Update 7

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

OBR: Continued E2E testing on both base price and promotions. Promo prices were sent using examples from the API documentation. Will need support from Harrison and Peeto on promotions, as we do not know what unique identifiers are needed for each type of promotions.

### Raw Update

OBR: Continued E2E testing on both base price and promotions. Promo prices were sent using examples from the API documentation. Will need support from Harrison and Peeto on promotions, as we do not know what unique identifiers are needed for each type of promotions. E2E testing on base prices was done by Ignacio by uploading optimized prices on cabanas and drink packages for a test sailing.
(1) Forecasting & Optimization: Updated revenue forecasts and obtained new drink package results. Created exploratory “revenue maximizing” optimization tables. Reformatted optimization outputs for integration, including price adjustment columns.
(2) Data & Feature Store: Fixed errors in production feature store (duplicate merges caused by product code issues). Adjusted merge queries to handle multiple rows and prevent duplication.
(3) SQL & Data Merging: Removed duplicate SQL results by adding product code columns for accurate merges.
(4) Reporting: Prepared a progress PPT for Dave on PCP/OBR activities.
(5) Deployment & Workflow: Pushed updates for optimization tables to dev & prod after QA. Tested and promoted the full OBR workflow to production.
(6) Table Integration: Reformatted and joined tables (drink packages & cabanas) for centralized OBR reporting, including constraint checks and price recommendation outputs. Created filtered tables for current WTS bins.
(7) Back-testing: Updated queries to accurately back-test hybris price uploads with recent table changes.
(8) Code & PRs: Submitted PRs for fixing feature store merges and query adjustments. Managed deployment of workflow updates through QA into production

---

## Update 8

**Date:** 2025-07-11
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

Bernard continued testing on FIT tracks. There is a focus on investigating retentions including a survivor model. We attempted to meet with Lisette to get more information on retention data and model features, but she was unable to meet and sent Christian.

### Raw Update

Bernard continued testing on FIT tracks. There is a focus on investigating retentions including a survivor model. We attempted to meet with Lisette to get more information on retention data and model features, but she was unable to meet and sent Christian. Christian was unable to provide the information needed so we will need a follow up.
Fine-tunned track recommendations through model fine-tunning separately on peak and off-peak booking seasons with hyperparameter tunning on three parameters (learning rate, tree depth, and estimators) simultaneously. Generated deltas in track ask between high and low SPI sailings, highlighting need to push more volume to periods enjoying high organic demand and greater pricing responsivity.
Nick recommends separate models for SPI scoring of winter and summer seasons, which more naturally follows demand patterns rather than segmenting by calendar year.

---

## Update 9

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

CEL - SPI scoring model finalizations
CEL SPI model to be pushed to production in coming week. Anastasia provided final sign off on CEL SPI scores after a productive 2 months of scrutiny and fine-tunning. Enhancements asked for by CEL team will also be used to update RCI scoring methodology

### Raw Update

CEL - SPI scoring model finalizations
CEL SPI model to be pushed to production in coming week.
Anastasia provided final sign off on CEL SPI scores after a productive 2 months of scrutiny and fine-tunning.
Enhancements asked for by CEL team will also be used to update RCI scoring methodology

---

## Update 10

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

RCI - PRE (RM)
* Assisted coordination of testing AS400 fix that will fully enable Mandatory Occupancy for both brands. Final testing successful and AS400 team deployed live. Provided means to get elasticity recommendations into usable Unity Catalog tables.

### Raw Update

RCI - PRE (RM)
* Assisted coordination of testing AS400 fix that will fully enable Mandatory Occupancy for both brands. Final testing successful and AS400 team deployed live.
Provided means to get elasticity recommendations into usable Unity Catalog tables.
*Met with junior members of team to provide guidance in incorporating new elasticity model and forward/backward window study into RCI PRE.
*General troubleshooting and guidance for teams on production systems that demonstrated issues (RCI and Celebrity PRE prices not actioned).

---

## Update 11

**Date:** 2025-07-11
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[jesse_bausell/overview_jesse_bausell|Jesse Bausell]]

### Summarized Update

7/1/2025 - A/B Testing Update
Data Science met with SSC Revenue teams to discuss our initial voyage pairings for A/B testing. Moving forward we agreed to:
Ensure that Alaska A/B pairings use the same ship
Review Caribbean A/B pairings once they are ready
Once we agree on Caribbean and Alaska A/B pairings, we can begin A/B testing with the PRE. We will meet again on Friday, July 11

### Raw Update

7/1/2025 - A/B Testing Update
Data Science met with SSC Revenue teams to discuss our initial voyage pairings for A/B testing. Moving forward we agreed to:
Ensure that Alaska A/B pairings use the same ship
Review Caribbean A/B pairings once they are ready
Once we agree on Caribbean and Alaska A/B pairings, we can begin A/B testing with the PRE. We will meet again on Friday, July 11

---

## Update 12

**Date:** 2025-07-11
**Business Area:** PCP Pricing Automation (RCI/CEL)
**Business Project:** Automated Pricing Expansion
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

Last week, I focused on gathering the necessary data for the analysis. I collected ship-level and category-class level track and projected passenger build data for all sailings from 2019, 2023, to the present. Using this, I established a foundational framework to test different look-back and look-forward windows for the PRE.

### Raw Update

Last week, I focused on gathering the necessary data for the analysis. I collected ship-level and category-class level track and projected passenger build data for all sailings from 2019, 2023, to the present. Using this, I established a foundational framework to test different look-back and look-forward windows for the PRE.
Additionally, this week, I concentrated on understanding how the Celebrity and RCI PREs utilize backward-looking and forward-looking tracks, respectively, and how these approaches impact pricing. During my review of the RCI PRE, I discovered a bug in the code that only captures the track for a single week, instead of calculating a rolling average across multiple weeks. I devised a solution to implement the rolling average and explained this to the business. They are aligned with this change. Before making the update, I plan to review the entire notebook to ensure that subsequent code does not offset this correction.

---

## Update 13

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

GTY-Lead/Berthing: Michelle close to completing GTY-Lead 2.0 for RCI. RCI Strat teams are determining whether to prioritize GTY-Lead 3.0 or Gty-Lead 2.0 for T4 guests. Michelle
RCI | GTY-LEAD 2.0 (Doubles)
Close to completing GTY-Lead 2.0 for RCI.

### Raw Update

GTY-Lead/Berthing: Michelle close to completing GTY-Lead 2.0 for RCI. RCI Strat teams are determining whether to prioritize GTY-Lead 3.0 or Gty-Lead 2.0 for T4 guests.
Michelle
RCI | GTY-LEAD 2.0 (Doubles)
Close to completing GTY-Lead 2.0 for RCI. All work finalized for 2.0 doubles version.
RCI team approved final results. Pushed pipeline to production to retrain model and run optimization daily on updated inventory and prices. Business in progress of TAP integration.
Met with RCI team and reviewed falloff. Explained sailings were dropped in cases gty was not open, categories no longer had cabins left, not valid sailings.
They would like to use retentions in deciding cabin availability instead of AS400 availability and still recommend gaps even when gty category is not open.

---

## Update 14

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

RCI | GTY-LEAD 2.0 (Quads)
RCI Strat teams are determining whether to prioritize GTY-Lead 3.0 or Gty-Lead 2.0 for T4 guests. Built out datasets, model, and optimization for Quads version. Sent over gap recommendations to team for review.

### Raw Update

RCI | GTY-LEAD 2.0 (Quads)
RCI Strat teams are determining whether to prioritize GTY-Lead 3.0 or Gty-Lead 2.0 for T4 guests.
Built out datasets, model, and optimization for Quads version. Sent over gap recommendations to team for review.

---

## Update 15

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

GTY-Lead 3.0 work continues on CEL. GTY-Lead 3.0 outputs should in theory inform berthing decisions, as it tells us what categories we expect demand. It does not however inform us of who to berth in each category when considering different business rules and logic.

### Raw Update

GTY-Lead 3.0 work continues on CEL. GTY-Lead 3.0 outputs should in theory inform berthing decisions, as it tells us what categories we expect demand. It does not however inform us of who to berth in each category when considering different business rules and logic. Anastasia is expecting GTY-Lead 3.0 to provide what is needed based on conversations with Jake, but further discussions are likely needed. Nick is happy with the current state of logic based berthing Doug has already implemented.
Testing optimization results with each tier combination possible.
When compared with DI example from gty-lead, gap is similar as we would like. Further work on historical LAFs is needed. When comparing past sailing optimization results with actual LAFs implemented, there is a difference.
Finished adjusting track calculation to match capacity. Plotted booking curves to illustrate how optimization runs for each example of tier combinations.
Aligned on optimization logic. Moving forward with applying to all sailings.

---

## Update 16

**Date:** 2025-07-11
**Business Area:** PCP Pricing Automation (RCI/CEL)
**Business Project:** Automated Pricing Expansion
**People:** Unidentified

### Summarized Update

Following a meeting with Tristan from the celebrity team, it was agreed that incorporating revenue period columns into the training output tables would facilitate better integration with revenue data for more precise revenue performance analysis. I implemented a proration function to allocate cruise nights revenue across different months and added corresponding columns for revenue month, revenue year, and revenue quarter to both the final training output table and the weekly lag analysis table. These additions enable more granular joins and improve the accuracy of model evaluation against actual revenue figures.

### Raw Update

Following a meeting with Tristan from the celebrity team, it was agreed that incorporating revenue period columns into the training output tables would facilitate better integration with revenue data for more precise revenue performance analysis.
I implemented a proration function to allocate cruise nights revenue across different months and added corresponding columns for revenue month, revenue year, and revenue quarter to both the final training output table and the weekly lag analysis table. These additions enable more granular joins and improve the accuracy of model evaluation against actual revenue figures.

---

## Update 17

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Development of Model Monitoring Tables:
Created a table to store the final output of weekly retraining of elasticity models. This table includes fields for the retraining date and model version, which automatically update during each retrain to capture the exact timestamp and version, allowing for performance tracking over time. Developed a second table to monitor week-to-week model drift, focusing on changes in predictions and errors between recent retrains.

### Raw Update

CEL | PRE | 2. Development of Model Monitoring Tables:
Created a table to store the final output of weekly retraining of elasticity models. This table includes fields for the retraining date and model version, which automatically update during each retrain to capture the exact timestamp and version, allowing for performance tracking over time.
Developed a second table to monitor week-to-week model drift, focusing on changes in predictions and errors between recent retrains. This table is populated by selecting data from the most recent training runs and employing window functions to compare current metrics with previous ones.
Calculated various drift metrics, including percentage changes in price and demand, elasticity variation, deviance (model fit), and prediction error differences. These metrics support ongoing monitoring, enable quick identification of performance shifts, and assist in decision-making regarding retraining strategies.
The drift metrics are stored over time, providing a historical record that enhances governance, tracking, and model performance transparency.

---

## Update 18

**Date:** 2025-07-11
**Business Area:** Project Axiom
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Completed Tasks on Guest Service Chat:
• Dashboard Optimization: Updated the dashboard to exclude incomplete sailings, ensuring that they do not skew the average physical guest logs data. • Question-Answer Relevancy Review: Reviewed and refined the logic for question-answer relevancy to ensure the chatbot provides accurate and contextually appropriate responses to guest inquiries. • Stakeholder Meetings: Held discussions with stakeholders to review progress and align on next steps and upcoming project priorities.

### Raw Update

Completed Tasks on Guest Service Chat:
• Dashboard Optimization: Updated the dashboard to exclude incomplete sailings, ensuring that they do not skew the average physical guest logs data.
• Question-Answer Relevancy Review: Reviewed and refined the logic for question-answer relevancy to ensure the chatbot provides accurate and contextually appropriate responses to guest inquiries.
• Stakeholder Meetings: Held discussions with stakeholders to review progress and align on next steps and upcoming project priorities.

---

## Update 19

**Date:** 2025-07-11
**Business Area:** Project Axiom
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Upcoming Tasks:
• App Reviews Focus: Based on stakeholder meetings, I will focus on analyzing app reviews this week to identify areas for improvement. • Exploratory Data Analysis (EDA): Begin with EDA to uncover patterns and insights within the app review data. • Topic Classification Development: Build a robust topic classification model to categorize app review feedback into actionable themes.

### Raw Update

Upcoming Tasks:
• App Reviews Focus: Based on stakeholder meetings, I will focus on analyzing app reviews this week to identify areas for improvement.
• Exploratory Data Analysis (EDA): Begin with EDA to uncover patterns and insights within the app review data.
• Topic Classification Development: Build a robust topic classification model to categorize app review feedback into actionable themes.

---

## Update 20

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

Weekly Report:
• Received PowerBI report from Augusto showing Conversions for CTI and BKTOCX. • CTI model shows opportunity for improvement in the rank ordering of probabilities. • Augusto connecting with Marketing team regarding CP leads as Will asked us to prioritize this lead, but also this lead may not need to be scored as Augusto has confirmed the business contacts almost all of these leads already.

### Raw Update

Weekly Report:
• Received PowerBI report from Augusto showing Conversions for CTI and BKTOCX.
• CTI model shows opportunity for improvement in the rank ordering of probabilities.
• Augusto connecting with Marketing team regarding CP leads as Will asked us to prioritize this lead, but also this lead may not need to be scored as Augusto has confirmed the business contacts almost all of these leads already.
• BKTOCX: Presentation Preparation for Royal and Celebrity.
Completed:
• Booking_ID Integration in output files: Use an existing column to include the Booking_ID, testing on Databrick environment.
• Collaborating with Chandra for testing process, tracking files drop, and validation on Siebel side.

---

## Update 21

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

Ongoing Task:
• OFTOCX data migration to UC: Collaboration with DE and Augusto team to ensure the migration of the OFTOCX dataset into UC. • Improve CTI model based on opportuities.

### Raw Update

Ongoing Task:
• OFTOCX data migration to UC: Collaboration with DE and Augusto team to ensure the migration of the OFTOCX dataset into UC.
• Improve CTI model based on opportuities.

---

## Update 22

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

Workforce Planning POC
Data Access
• Ongoing: Romeo Anselmo is currently working on granting me the necessary permissions to access the tables. Work Completed / Ongoing – Data Preprocessing / WPS Staffing Model Development
• EDA and reviewed basic daily call volume data for RES
• EDA and reviewed basic daily AHT forecast for RES
• Sourced functions from the international staffing model (ongoing)
• Modifying and adapting the functions to fit the North America context using similar logic (ongoing)
Functions are:
• steady-state probabilities: Calculates the steady-state probabilities for the Erlang A queueing model. • buffer_length: Computes the expected number of calls waiting (queue size beyond capacity).

### Raw Update

Workforce Planning POC
Data Access
• Ongoing: Romeo Anselmo is currently working on granting me the necessary permissions to access the tables.
Work Completed / Ongoing – Data Preprocessing / WPS Staffing Model Development
• EDA and reviewed basic daily call volume data for RES
• EDA and reviewed basic daily AHT forecast for RES
• Sourced functions from the international staffing model (ongoing)
• Modifying and adapting the functions to fit the North America context using similar logic (ongoing)
Functions are:
• steady-state probabilities: Calculates the steady-state probabilities for the Erlang A queueing model.
• buffer_length: Computes the expected number of calls waiting (queue size beyond capacity).
• waiting_prob: Calculates the probability that an incoming call will need to wait before being served.
• occupancy: Calculates the average proportion of agent time spent serving calls.
• abandon_prob: Estimates the fraction of calls that will abandon due to excessive waiting or impatience.
• service_level: Estimates the percentage of calls answered within a target time threshold (ASA = Average Speed of Answer), adjusted for abandon probability and system load.
Next Steps – WPS Staffing Model Development
• Run the model for the RES (LOB) to validate that the orchestration of the functions for the staffing model computations is working as expected.
• Prepare a project status walkthrough to be shared and used as a basis for discussing next steps.

---

## Update 23

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Current & Working on:
• MdAPE fix for uniform, medical and cococay models: Updated demand notebooks and call other consumption tables to see if this changes the product predicted and product actuals columns. No significant change was noticed for medical model, but CocoCay and uniform seem to be having issues. Target leakage was fixed for CocoCay but still a high mdape from my original code before changing the demand notebook.

### Raw Update

Integrated Business Planning (IBP)
Current & Working on:
• MdAPE fix for uniform, medical and cococay models: Updated demand notebooks and call other consumption tables to see if this changes the product predicted and product actuals columns. No significant change was noticed for medical model, but CocoCay and uniform seem to be having issues. Target leakage was fixed for CocoCay but still a high mdape from my original code before changing the demand notebook. Uniform model is running very slow which didn't usually so I believe it's an increase in data that I didn't notice before which I am debugging.
• Mapping Star of the seas and Xcel to newest sister ship in RCI/CCI HF&B model. Code seems to be working as intended. Will figure out a way to make it even more dynamic by using the deployment table for any other new ships and the consumption table as a way to know whether the new ship needs to be mapped or not. Dates to the dictionary are being added for new ships.

---

## Update 24

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Volatility Reports:
Completed:
• (1) Increased the threshold for flagging product + ship combinations with significantly high predicted demand from 100 to 1,000, for faster job execution and more storage. • (2) Added summary slide of Mario’s version of the volatility reports to the agenda. • (3) Presented to Yan on Thursday 7/10 for additional feedback and revisions before delivering to Mario.

### Raw Update

Integrated Business Planning (IBP)
Volatility Reports:
Completed:
• (1) Increased the threshold for flagging product + ship combinations with significantly high predicted demand from 100 to 1,000, for faster job execution and more storage.
• (2) Added summary slide of Mario’s version of the volatility reports to the agenda.
• (3) Presented to Yan on Thursday 7/10 for additional feedback and revisions before delivering to Mario.

---

## Update 25

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Pending:
• (1) A meeting to present the updated version to Mario (to be scheduled by Yan). • (2) Implement Yan's feedback: Add a new column showing the percentage/ratio change in predicted demand (increase/decrease); apply color coding/highlighting to emphasize significant changes; include a metric comparing prediction accuracy against actual consumption after the month ends; remove medical product categories from CocoCay and HF&B models.

### Raw Update

Integrated Business Planning (IBP)
Pending:
• (1) A meeting to present the updated version to Mario (to be scheduled by Yan).
• (2) Implement Yan's feedback: Add a new column showing the percentage/ratio change in predicted demand (increase/decrease); apply color coding/highlighting to emphasize significant changes; include a metric comparing prediction accuracy against actual consumption after the month ends; remove medical product categories from CocoCay and HF&B models.

---

## Update 26

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Uniforms Model:
Completed:
• (1) Updated the product name replacement logic in the ETL notebook to extract fabrics/materials, specific colors (raspberry, keylime, etc.), occupations, ship codes, and remove extra numbers/characters. • (2) Code successfully runs from ETL through Safety Stock Steps 1 & 2 for this model (running into issues starting from the Write Parquet Files notebook through to the Challenger model). • (3) Addressed the data type mismatches with product_name_number (arrays vs.

### Raw Update

Integrated Business Planning (IBP)
Uniforms Model:
Completed:
• (1) Updated the product name replacement logic in the ETL notebook to extract fabrics/materials, specific colors (raspberry, keylime, etc.), occupations, ship codes, and remove extra numbers/characters.
• (2) Code successfully runs from ETL through Safety Stock Steps 1 & 2 for this model (running into issues starting from the Write Parquet Files notebook through to the Challenger model).
• (3) Addressed the data type mismatches with product_name_number (arrays vs. strings) by exploding arrays into separate rows for joining, and will later work on rebuilding them.
• (4) Currently fixing issue where the product actuals were being overwritten by the consumption table.

---

## Update 27

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Pending:
• (1) Provide a file with sample of the product name modifications to Yan for approval. • (2) Continue fixing code. • (3) Prepare the Uniform V3 model overview presentation.

### Raw Update

Integrated Business Planning (IBP)
Pending:
• (1) Provide a file with sample of the product name modifications to Yan for approval.
• (2) Continue fixing code.
• (3) Prepare the Uniform V3 model overview presentation.
Other Pending Work:
• Add CocoCay metrics to dashboard.

---

## Update 28

**Date:** 2025-07-11
**Business Area:** Customer Lifetime Value
**Business Project:** Cross-Brand Credit Card Strategy
**People:** Unidentified

### Summarized Update

Completed:
• Completed data validation of NPS data confirming Ship and Brand NPS matches known values. • Identified indirect cost as the root of solo's value indexing being unexpectedly high by cloning and modifying the analytics table pipeline with altered cost calculations. • Created a per-booking level table for Corporate Strategy, grouped by cabin class, cohort, and sailing displaying sample sailing data on the full math walk for our index calculations.

### Raw Update

Completed:
• Completed data validation of NPS data confirming Ship and Brand NPS matches known values.
• Identified indirect cost as the root of solo's value indexing being unexpectedly high by cloning and modifying the analytics table pipeline with altered cost calculations.
• Created a per-booking level table for Corporate Strategy, grouped by cabin class, cohort, and sailing displaying sample sailing data on the full math walk for our index calculations.
• Met with Trade to detail how CLV can compliment their booking-level information for valuable demographic insights.

---

## Update 29

**Date:** 2025-07-11
**Business Area:** Customer Lifetime Value
**People:** Unidentified

### Summarized Update

Ongoing:
• Began sorting columns by aggregation method for the eventual creation of a clean, booking-level CLV table for future use cases from air, trade, and more…
• Documenting assumptions and calculations in Excel. • Began investigating alternatives to absolute pax or booking indirect cost rates, weighing logical methodology to potentially find a hybrid rate. • Identifying exact area of analytics ETL pipeline where passengers are being duplicated.

### Raw Update

Ongoing:
• Began sorting columns by aggregation method for the eventual creation of a clean, booking-level CLV table for future use cases from air, trade, and more…
• Documenting assumptions and calculations in Excel.
• Began investigating alternatives to absolute pax or booking indirect cost rates, weighing logical methodology to potentially find a hybrid rate.
• Identifying exact area of analytics ETL pipeline where passengers are being duplicated.

---

## Update 30

**Date:** 2025-07-11
**Business Area:** E-Commerce
**Business Project:** Booking Propensity Models
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]]

### Summarized Update

Completed
• Implement algorithm for summarizing SHAP values per feature values. It provides faster computation of SHAP dependency plot and smaller storage footprint. This will allow for dashboard SHAP values dependency plots for all the models-features combination, now only plots for top 10 features are available.

### Raw Update

Completed
• Implement algorithm for summarizing SHAP values per feature values. It provides faster computation of SHAP dependency plot and smaller storage footprint. This will allow for dashboard SHAP values dependency plots for all the models-features combination, now only plots for top 10 features are available.
• Improve feature selection algorithm by automatically detecting optimal number of features for each models, right now a fixed number is been used.
• Optimized Databricks Dashboard queries and adjusted to include past guests and prospective guests.
• Visualized predicted cabin class distribution from next best offer results, visualizing spending and fare based on APD models and PHML distribution.
• Experimented with genie to provide better response along with optimizing sample queries.

---

## Update 31

**Date:** 2025-07-11
**Business Area:** E-Commerce
**Business Project:** Genie Application Enhancements
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]]

### Summarized Update

Upcoming Tasks:
• Meet with E-commerce to iterate through dashboard and tailor visualizations. • After discovering an issue with the top 5 destinations visualization, the data pipeline will need to be adjusted in order to ensure accurate destinstion distribution. • Begin gathering feedback on newly optimized genie space and adjust chat bot instructions for better responses.

### Raw Update

Upcoming Tasks:
• Meet with E-commerce to iterate through dashboard and tailor visualizations.
• After discovering an issue with the top 5 destinations visualization, the data pipeline will need to be adjusted in order to ensure accurate destinstion distribution.
• Begin gathering feedback on newly optimized genie space and adjust chat bot instructions for better responses.

---

## Update 32

**Date:** 2025-07-11
**Business Area:** WoW
**Business Project:** Forecasting Pipeline Expansion
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

1) Supporting FPMS roll out - with MDR rules engine adjusting, Couchbase schema matching and hotfixes
2) Completed accuracy testing of V1 pipeline for specialty - shows 35-40% improvement overall
3) MDR V1 hotfixes

### Raw Update

1) Supporting FPMS roll out - with MDR rules engine adjusting, Couchbase schema matching and hotfixes
2) Completed accuracy testing of V1 pipeline for specialty - shows 35-40% improvement overall
3) MDR V1 hotfixes

---

## Update 33

**Date:** 2025-07-11
**Business Area:** WoW
**Business Project:** Improved Forecasting Accuracy
**People:** Unidentified

### Summarized Update

1) MDR V1 and specialty V1 development, unit, integration, and stress testing  is complete
2) Supporting FPMS roll out in multiple ships
3) specialty accuracy testing is complete
4) MDR accuracy testing  - to be completed next week
5) all rules engines requires to be tweaked next week

### Raw Update

1) MDR V1 and specialty V1 development, unit, integration, and stress testing  is complete
2) Supporting FPMS roll out in multiple ships
3) specialty accuracy testing is complete
4) MDR accuracy testing  - to be completed next week
5) all rules engines requires to be tweaked next week

---

## Update 34

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Conversational IVR
**People:** Unidentified

### Summarized Update

Accomplishments
Deployed new FAQs, Routing changes and NLU changes to both RCI and CEL
Presented analysis of 200 conversations to brand for iterative improvement suggestions in the backlog
Analyzed decrease in automated minutes and determined it is issues with the make a payment flow.

### Raw Update

Accomplishments
Deployed new FAQs, Routing changes and NLU changes to both RCI and CEL
Presented analysis of 200 conversations to brand for iterative improvement suggestions in the backlog
Analyzed decrease in automated minutes and determined it is issues with the make a payment flow.

---

## Update 35

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Conversational IVR
**People:** Unidentified

### Summarized Update

Working On
CoPilot Migration architecture
Development of backlog
Research into generative answers and knowledge sources
Updates to existing mix application for routing
Discussions around post deployment IT structure
Guest profile API initial kick off

### Raw Update

Working On
CoPilot Migration architecture
Development of backlog
Research into generative answers and knowledge sources
Updates to existing mix application for routing
Discussions around post deployment IT structure
Guest profile API initial kick off

---

## Update 36

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Cresta AI Analytics Tools
**People:** Unidentified

### Summarized Update

Accomplishments
Finalized agent and supervisor dashboard
Sent out first cresta insights report and developed automated extraction
Developed analytics tools for outliers for performance
Removed archived articles from genka

### Raw Update

Accomplishments
Finalized agent and supervisor dashboard
Sent out first cresta insights report and developed automated extraction
Developed analytics tools for outliers for performance
Removed archived articles from genka

---

## Update 37

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Cresta AI Analytics Tools
**People:** Unidentified

### Summarized Update

Working on
Research into speech IQ report sunsetting
Research into data integration
GenKA updates for articles surfacing and factoids
AI analyst pilot definition
Determination on how to setup category tracking

### Raw Update

Working on
Research into speech IQ report sunsetting
Research into data integration
GenKA updates for articles surfacing and factoids
AI analyst pilot definition
Determination on how to setup category tracking

---

## Update 38

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** Fleetwide Energy Monitoring
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

•	Tag mapping for ML Class Engine Room Ventilation Fans, Machinery Pumps, DG Waste Heat Recovery, Variable Chilled Water Flow, AHU Cooling TCVs, Reverse Osmosis, Fresh Water, and Energy Recovery Wheel areas. •	Added machinery power breakdown calculations for the fleet. •	Integrated Navigator OPC UA server data into the MIAP platform.

### Raw Update

•	Tag mapping for ML Class Engine Room Ventilation Fans, Machinery Pumps, DG Waste Heat Recovery, Variable Chilled Water Flow, AHU Cooling TCVs, Reverse Osmosis, Fresh Water, and Energy Recovery Wheel areas.
•	Added machinery power breakdown calculations for the fleet.
•	Integrated Navigator OPC UA server data into the MIAP platform.
•	Met with the Maritime Security team and reviewed their requirements for a live fleet monitoring solution combined with future deployments. The team wants to see fleet location live, with a map overlay of important information such as global threats.
•	Reviewed NAPA API data requirements with the Marine Safety team.
•	Reviewed Crosser IoT platform benefits with the Enterprise Architecture team.
•	Attended the monthly Data Science and Decarbonation team meeting. Agreed on accelerating fuel savings in preparation for MIAP Phase IV CAR.

---

## Update 39

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[mahshad_shariatnasab/overview_mahshad_shariatnasab|Mahshad Shariatnasab]]

### Summarized Update

Added incinerator plots to the GMP app. •	Finalized OFB for the GMO app and prepared it for production. •	Contacted the ship for WN regarding 100 kW savings on AHUs in cabins and public areas.

### Raw Update

Added incinerator plots to the GMP app.
•	Finalized OFB for the GMO app and prepared it for production.
•	Contacted the ship for WN regarding 100 kW savings on AHUs in cabins and public areas. They responded that the issue is related to customer complaints, and we are currently investigating optimization.
•	Started working on ML class savings and on new machinery ventilation room fans, as well as the DG high-temperature cooling water waste heat recovery system, exploring potential savings in these areas.
•	After our team’s visit to SM and communication with the engineering team, we identified the following savings:
o	New WN savings of approximately $36k for Chiller A’s extra consumption, ongoing for the past six months.
o	New SM savings of around $100k for machinery water pump issues persisting for the past year.
o	New SM savings of approximately $40k for ventilation fans in the chiller room, ongoing for the past two years.

---

## Update 40

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** Fleetwide Energy Monitoring
**People:** [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]]

### Summarized Update

•	Calculated the Energy Recovery Wheel (ERW) utilization across the entire fleet and added corresponding diagnostic plots for both the fleet and individual ships in the GMO app. This feature helps identify ships that are under-utilizing the energy recovery wheels in air handling units, enabling targeted actions to improve energy savings by contacting those ships. •	Currently working on the calculation of cooling power on the water side, which will be used to monitor the cooling performance of air handling units (AHUs) in future enhancements.

### Raw Update

•	Calculated the Energy Recovery Wheel (ERW) utilization across the entire fleet and added corresponding diagnostic plots for both the fleet and individual ships in the GMO app. This feature helps identify ships that are under-utilizing the energy recovery wheels in air handling units, enabling targeted actions to improve energy savings by contacting those ships.
•	Currently working on the calculation of cooling power on the water side, which will be used to monitor the cooling performance of air handling units (AHUs) in future enhancements.

---

## Update 41

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

•	Updated all MIAP release/deployment pipelines to leverage the new Agent Pools created by the Platform team. •	Performed EDA on ALS data to quantify efficiency gains from ALS utilization per ship. •	Added Eniram weather-normalized power feature to the propulsion features table.

### Raw Update

•	Updated all MIAP release/deployment pipelines to leverage the new Agent Pools created by the Platform team.
•	Performed EDA on ALS data to quantify efficiency gains from ALS utilization per ship.
•	Added Eniram weather-normalized power feature to the propulsion features table.
•	Deployed Hull Degradation chart to the GMO app in production.
•	Created a process that, for each quarter, fits a line to the propulsion power consumed by each ship with ALS on vs. off, and calculates the gross ALS power savings at each speed interval.
•	Created a visualization in GMO (deployed to production) that shows ship-level ALS savings over time.
•	Tuned the AHU Analytics job, reducing runtime by over 50% and preventing consistent failures.
•	Saved Hull Degradation model output to a table to prevent unnecessary scoring of models during API calls, improving response time by over 30%.

---

## Update 42

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** Unidentified

### Summarized Update

•	Added MGO Equivalent SFOC features for individual power plants (DG, GT, Fuel Cell). •	Created individual MGO EQ SFOC power plant base and dynamic models. •	Created a new power plant outlier removal method to remove instances where the engine first turns on or off.

### Raw Update

•	Added MGO Equivalent SFOC features for individual power plants (DG, GT, Fuel Cell).
•	Created individual MGO EQ SFOC power plant base and dynamic models.
•	Created a new power plant outlier removal method to remove instances where the engine first turns on or off.

---

## Update 43

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** Unidentified

### Summarized Update

June 27th
•	Identified an issue with a production workflow in MIAP Analytics. •	Focused on troubleshooting, implemented the necessary fixes, and successfully pushed the updates to production. The workflow completed without issues.

### Raw Update

June 27th
•	Identified an issue with a production workflow in MIAP Analytics.
•	Focused on troubleshooting, implemented the necessary fixes, and successfully pushed the updates to production. The workflow completed without issues.
July 1st
•	Connected with the Ignio AMOS team to perform end-to-end testing.
•	Gathered insights on additional changes needed.
•	Discovered that some tags are missing in production due to transformation issues with Eniram.
•	Addressed this by adjusting the approach to handle missing tags through chunking based on time intervals rather than variables.
July 2nd
•	Tested and validated the new Eniram approach across multiple scenarios.
•	Made adjustments to the logic in the shipcode column.
•	Sent an email to the Eniram team detailing the list of missing tags, vessel-wise.
July 3rd
•	Cleaned up the new approach and raised a pull request.
•	Currently working on the historical load for Eniram.
•	Developing an AutoLoader approach and creating a separate workflow.
•	Experimenting with different strategies to efficiently retrieve data from the API.

---

## Update 44

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[mehdi_assefi/overview_mehdi_assefi|Mehdi Assefi]]

### Summarized Update

•	Working on stability PDF parsing and feature engineering. Kevin:
Loyalty:
Continued early peeking analysis on spend to save pilot. Although the majority of the effort was spent on identifying net new guests through propensity models, this will not be shared with the EC as the loyalty teams, want to wait until more time has passed to allow for more FCCs to be redeemed.

### Raw Update

•	Working on stability PDF parsing and feature engineering.
Kevin:
Loyalty:
Continued early peeking analysis on spend to save pilot. Although the majority of the effort was spent on identifying net new guests through propensity models, this will not be shared with the EC as the loyalty teams, want to wait until more time has passed to allow for more FCCs to be redeemed. We will share early peeking analysis on spend with the EC, highlighting that there has been a more noticeable trend in short Caribbean spend increases than 7N Caribbean. Following the steerco where the EC deck was shared, several more analyses were requested, mostly focused on FCC redemption. Further refined menus and guidance on the second pilot, which will be choice benefits. Brian's last day was this week. He completed knowledge transfer sessions with Kartik before leaving.

---

## Update 45

**Date:** 2025-07-11
**Business Area:** Revenue Management Automation (RCI)
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Kevin
Revenue Management Planning (RCI): Developed a 6 month roadmap for releases approved by both Nick and Anastasia. Began weekly alignment meetings with both brands to build a focus on joint development rather than silod workstreams.

### Raw Update

Kevin
Revenue Management Planning (RCI): Developed a 6 month roadmap for releases approved by both Nick and Anastasia. Began weekly alignment meetings with both brands to build a focus on joint development rather than silod workstreams.

---

## Update 46

**Date:** 2025-07-11
**Business Area:** Revenue Management Automation (RCI)
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Kevin
Revenue Management Planning (CEL): Developed a 6 month roadmap for releases approved by both Nick and Anastasia. Began weekly alignment meetings with both brands to build a focus on joint development rather than silod workstreams.

### Raw Update

Kevin
Revenue Management Planning (CEL): Developed a 6 month roadmap for releases approved by both Nick and Anastasia. Began weekly alignment meetings with both brands to build a focus on joint development rather than silod workstreams.

---

## Update 47

**Date:** 2025-07-11
**Business Area:** HR
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]], [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Experiments (Atefeh): I performed experiments using LightGBM to estimate price elasticity at the meta_cc level. Key points include Applied hyperparameter tuning via Optuna, regularization, and target encoding based on mean target value of categorical features. Achieved high predictive performance with R² exceeding 90% across core meta-products.

### Raw Update

Experiments (Atefeh): I performed experiments using LightGBM to estimate price elasticity at the meta_cc level. Key points include Applied hyperparameter tuning via Optuna, regularization, and target encoding based on mean target value of categorical features. Achieved high predictive performance with R² exceeding 90% across core meta-products.
However, the elasticity outputs from LightGBM were inconsistent in magnitude and sign, indicating the model's focus on overall demand prediction often masks the marginal effects of price. Consequently, I reverted to Poisson regression for better interpretability and stable elasticity curves.

---

## Update 48

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

Elasticity Model 4.0 Refinement and Validation
Originally when the model is trained on large bin sizes (Spline-based on hard-coded A bins) metrics are a lot better because aggregating the data over larger bins reduces noise. However, when using this model to predict on smaller intervals and on testing performance is poor - In addition, elasticity plots tend to be ‘more flat’ with nearly 3 steps in most cases (since we have almost 3 large bins between 0-70 wts) which is not visually appealing or accepted by the business team to have constant elasticities over several weeks. On the other hand - training the models on smaller bin sizes (like 5 weeks to sail) yields poorer results.

### Raw Update

Elasticity Model 4.0 Refinement and Validation
Originally when the model is trained on large bin sizes (Spline-based on hard-coded A bins) metrics are a lot better because aggregating the data over larger bins reduces noise. However, when using this model to predict on smaller intervals and on testing performance is poor - In addition, elasticity plots tend to be ‘more flat’ with nearly 3 steps in most cases (since we have almost 3 large bins between 0-70 wts) which is not visually appealing or accepted by the business team to have constant elasticities over several weeks.
On the other hand - training the models on smaller bin sizes (like 5 weeks to sail) yields poorer results.
So, as a tradeoff between these 2 performance criterion that are equally important to the business - Instead of aggregating and averaging the price and bookings over the bin I imported the data at the granularity of 5 weeks to sail while smoothing over each bin to reduce noise (instead of averaging) - So, I am still maintaining more granular data for better visuals and more realistic elasticity values while training the models on larger bin sizes yielding better model metrics.
Additionally - for validation purposes, I calculated the elasticity analytically from historical data (% change in bkgs/ % change in price) over the sailings booking window. Used these Analytical Elasticity curves to validate the model-generated elasticities - Should be discussing results with the biz tomorrow.
I am working on putting together final slides and visuals to present the upgraded model results with the biz for their validation and final approvals - below are some of the results (metrics and elasticity plots)
Production Code Elasticity Refactoring
Working on refactoring the elasticity model codebase to incorporate the following key scalability features:
(1) Data Preparation
→ Pull VPS pricing data from Feature Store
→ Apply filters and joins including max week-to-sale: 70, valid read_date range, etc.
→ Map sail_nights groups and wts spline bins cols (from JSON)
→ Apply smoothing within each WTS bin (rolling window = 3)
→ Write transformed Spark DataFrame to Unity Catalog
↳ (This becomes the input for model training)
(2)Experimentation Data
→ Define experimentation strategy: Vary WTS binning strategies - price transformation techniques
→ Generate experimentation grid: Iterate over all combinations of meta, cat_class, bin, scaling
→ Save grid as experimentation DataFrame and write to Unity Catalog
(3) Model Training
→ Read training data and experimentation grid from Unity Catalog
→ For each row in the experimentation grid:
Train model per meta-product × cat_class × binning × transformation
Compute scores and select best params for each meta - cc model
For the best models - stores betas, alphas, Elasticity, Predictions (train/test)
→ Return two output DataFrames and writes them to uc:
(4) Model metrics + params + pickles + coeffs
Full data + Elasticity + y_pred
Model Evaluation
→ Read model outputs and metrics from Unity Catalog
→ Visualize:
Elasticity curves
Predicted vs. actual (train/test)
Residuals and prediction errors

---

## Update 49

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[kartik_ullal/overview_kartik_ullal|Kartik Ullal]]

### Summarized Update

RCI RM AB Testing
Updated the sailing list for the T4 for test by removing offpeak sailings and creating a new sailing list for Alaska sailings. Re-ran power analysis for spend to save pilot independently for 7N and Short caribbean
Compared booking propensity for 60 days with 12 months to see if there was an increase in bookings for a guest

### Raw Update

RCI RM AB Testing
Updated the sailing list for the T4 for test by removing offpeak sailings and creating a new sailing list for Alaska sailings.
Re-ran power analysis for spend to save pilot independently for 7N and Short caribbean
Compared booking propensity for 60 days with 12 months to see if there was an increase in bookings for a guest

---

## Update 50

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

OBR: Continued E2E testing on both base price and promotions. Promo prices were sent using examples from the API documentation. Will need support from Harrison and Peeto on promotions, as we do not know what unique identifiers are needed for each type of promotions.

### Raw Update

OBR: Continued E2E testing on both base price and promotions. Promo prices were sent using examples from the API documentation. Will need support from Harrison and Peeto on promotions, as we do not know what unique identifiers are needed for each type of promotions. E2E testing on base prices was done by Ignacio by uploading optimized prices on cabanas and drink packages for a test sailing.
(1) Forecasting & Optimization: Updated revenue forecasts and obtained new drink package results. Created exploratory “revenue maximizing” optimization tables. Reformatted optimization outputs for integration, including price adjustment columns.
(2) Data & Feature Store: Fixed errors in production feature store (duplicate merges caused by product code issues). Adjusted merge queries to handle multiple rows and prevent duplication.
(3) SQL & Data Merging: Removed duplicate SQL results by adding product code columns for accurate merges.
(4) Reporting: Prepared a progress PPT for Dave on PCP/OBR activities.
(5) Deployment & Workflow: Pushed updates for optimization tables to dev & prod after QA. Tested and promoted the full OBR workflow to production.
(6) Table Integration: Reformatted and joined tables (drink packages & cabanas) for centralized OBR reporting, including constraint checks and price recommendation outputs. Created filtered tables for current WTS bins.
(7) Back-testing: Updated queries to accurately back-test hybris price uploads with recent table changes.
(8) Code & PRs: Submitted PRs for fixing feature store merges and query adjustments. Managed deployment of workflow updates through QA into production

---

## Update 51

**Date:** 2025-07-11
**Business Area:** Contact Center Optimization & Automation (RCI/CEL)
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

Bernard continued testing on FIT tracks. There is a focus on investigating retentions including a survivor model. We attempted to meet with Lisette to get more information on retention data and model features, but she was unable to meet and sent Christian.

### Raw Update

Bernard continued testing on FIT tracks. There is a focus on investigating retentions including a survivor model. We attempted to meet with Lisette to get more information on retention data and model features, but she was unable to meet and sent Christian. Christian was unable to provide the information needed so we will need a follow up.
Fine-tunned track recommendations through model fine-tunning separately on peak and off-peak booking seasons with hyperparameter tunning on three parameters (learning rate, tree depth, and estimators) simultaneously. Generated deltas in track ask between high and low SPI sailings, highlighting need to push more volume to periods enjoying high organic demand and greater pricing responsivity.
Nick recommends separate models for SPI scoring of winter and summer seasons, which more naturally follows demand patterns rather than segmenting by calendar year.

---

## Update 52

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

CEL - SPI scoring model finalizations
CEL SPI model to be pushed to production in coming week. Anastasia provided final sign off on CEL SPI scores after a productive 2 months of scrutiny and fine-tunning. Enhancements asked for by CEL team will also be used to update RCI scoring methodology

### Raw Update

CEL - SPI scoring model finalizations
CEL SPI model to be pushed to production in coming week.
Anastasia provided final sign off on CEL SPI scores after a productive 2 months of scrutiny and fine-tunning.
Enhancements asked for by CEL team will also be used to update RCI scoring methodology

---

## Update 53

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

RCI - PRE (RM)
* Assisted coordination of testing AS400 fix that will fully enable Mandatory Occupancy for both brands. Final testing successful and AS400 team deployed live. Provided means to get elasticity recommendations into usable Unity Catalog tables.

### Raw Update

RCI - PRE (RM)
* Assisted coordination of testing AS400 fix that will fully enable Mandatory Occupancy for both brands. Final testing successful and AS400 team deployed live.
Provided means to get elasticity recommendations into usable Unity Catalog tables.
*Met with junior members of team to provide guidance in incorporating new elasticity model and forward/backward window study into RCI PRE.
*General troubleshooting and guidance for teams on production systems that demonstrated issues (RCI and Celebrity PRE prices not actioned).

---

## Update 54

**Date:** 2025-07-11
**Business Area:** Revenue Management Automation (RCI)
**Business Project:** PRE 4.0 Elasticity Enhancements
**People:** [[jesse_bausell/overview_jesse_bausell|Jesse Bausell]]

### Summarized Update

7/1/2025 - A/B Testing Update
Data Science met with SSC Revenue teams to discuss our initial voyage pairings for A/B testing. Moving forward we agreed to:
Ensure that Alaska A/B pairings use the same ship
Review Caribbean A/B pairings once they are ready
Once we agree on Caribbean and Alaska A/B pairings, we can begin A/B testing with the PRE. We will meet again on Friday, July 11

### Raw Update

7/1/2025 - A/B Testing Update
Data Science met with SSC Revenue teams to discuss our initial voyage pairings for A/B testing. Moving forward we agreed to:
Ensure that Alaska A/B pairings use the same ship
Review Caribbean A/B pairings once they are ready
Once we agree on Caribbean and Alaska A/B pairings, we can begin A/B testing with the PRE. We will meet again on Friday, July 11

---

## Update 55

**Date:** 2025-07-11
**Business Area:** PCP Pricing Automation (RCI/CEL)
**Business Project:** Automated Pricing Expansion
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

Last week, I focused on gathering the necessary data for the analysis. I collected ship-level and category-class level track and projected passenger build data for all sailings from 2019, 2023, to the present. Using this, I established a foundational framework to test different look-back and look-forward windows for the PRE.

### Raw Update

Last week, I focused on gathering the necessary data for the analysis. I collected ship-level and category-class level track and projected passenger build data for all sailings from 2019, 2023, to the present. Using this, I established a foundational framework to test different look-back and look-forward windows for the PRE.
Additionally, this week, I concentrated on understanding how the Celebrity and RCI PREs utilize backward-looking and forward-looking tracks, respectively, and how these approaches impact pricing. During my review of the RCI PRE, I discovered a bug in the code that only captures the track for a single week, instead of calculating a rolling average across multiple weeks. I devised a solution to implement the rolling average and explained this to the business. They are aligned with this change. Before making the update, I plan to review the entire notebook to ensure that subsequent code does not offset this correction.

---

## Update 56

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

GTY-Lead/Berthing: Michelle close to completing GTY-Lead 2.0 for RCI. RCI Strat teams are determining whether to prioritize GTY-Lead 3.0 or Gty-Lead 2.0 for T4 guests. Michelle
RCI | GTY-LEAD 2.0 (Doubles)
Close to completing GTY-Lead 2.0 for RCI.

### Raw Update

GTY-Lead/Berthing: Michelle close to completing GTY-Lead 2.0 for RCI. RCI Strat teams are determining whether to prioritize GTY-Lead 3.0 or Gty-Lead 2.0 for T4 guests.
Michelle
RCI | GTY-LEAD 2.0 (Doubles)
Close to completing GTY-Lead 2.0 for RCI. All work finalized for 2.0 doubles version.
RCI team approved final results. Pushed pipeline to production to retrain model and run optimization daily on updated inventory and prices. Business in progress of TAP integration.
Met with RCI team and reviewed falloff. Explained sailings were dropped in cases gty was not open, categories no longer had cabins left, not valid sailings.
They would like to use retentions in deciding cabin availability instead of AS400 availability and still recommend gaps even when gty category is not open.

---

## Update 57

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

RCI | GTY-LEAD 2.0 (Quads)
RCI Strat teams are determining whether to prioritize GTY-Lead 3.0 or Gty-Lead 2.0 for T4 guests. Built out datasets, model, and optimization for Quads version. Sent over gap recommendations to team for review.

### Raw Update

RCI | GTY-LEAD 2.0 (Quads)
RCI Strat teams are determining whether to prioritize GTY-Lead 3.0 or Gty-Lead 2.0 for T4 guests.
Built out datasets, model, and optimization for Quads version. Sent over gap recommendations to team for review.

---

## Update 58

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

GTY-Lead 3.0 work continues on CEL. GTY-Lead 3.0 outputs should in theory inform berthing decisions, as it tells us what categories we expect demand. It does not however inform us of who to berth in each category when considering different business rules and logic.

### Raw Update

GTY-Lead 3.0 work continues on CEL. GTY-Lead 3.0 outputs should in theory inform berthing decisions, as it tells us what categories we expect demand. It does not however inform us of who to berth in each category when considering different business rules and logic. Anastasia is expecting GTY-Lead 3.0 to provide what is needed based on conversations with Jake, but further discussions are likely needed. Nick is happy with the current state of logic based berthing Doug has already implemented.
Testing optimization results with each tier combination possible.
When compared with DI example from gty-lead, gap is similar as we would like. Further work on historical LAFs is needed. When comparing past sailing optimization results with actual LAFs implemented, there is a difference.
Finished adjusting track calculation to match capacity. Plotted booking curves to illustrate how optimization runs for each example of tier combinations.
Aligned on optimization logic. Moving forward with applying to all sailings.

---

## Update 59

**Date:** 2025-07-11
**Business Area:** PCP Pricing Automation (RCI/CEL)
**Business Project:** Automated Pricing Expansion
**People:** Unidentified

### Summarized Update

Following a meeting with Tristan from the celebrity team, it was agreed that incorporating revenue period columns into the training output tables would facilitate better integration with revenue data for more precise revenue performance analysis. I implemented a proration function to allocate cruise nights revenue across different months and added corresponding columns for revenue month, revenue year, and revenue quarter to both the final training output table and the weekly lag analysis table. These additions enable more granular joins and improve the accuracy of model evaluation against actual revenue figures.

### Raw Update

Following a meeting with Tristan from the celebrity team, it was agreed that incorporating revenue period columns into the training output tables would facilitate better integration with revenue data for more precise revenue performance analysis.
I implemented a proration function to allocate cruise nights revenue across different months and added corresponding columns for revenue month, revenue year, and revenue quarter to both the final training output table and the weekly lag analysis table. These additions enable more granular joins and improve the accuracy of model evaluation against actual revenue figures.

---

## Update 60

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

Development of Model Monitoring Tables:
Created a table to store the final output of weekly retraining of elasticity models. This table includes fields for the retraining date and model version, which automatically update during each retrain to capture the exact timestamp and version, allowing for performance tracking over time. Developed a second table to monitor week-to-week model drift, focusing on changes in predictions and errors between recent retrains.

### Raw Update

CEL | PRE | 2. Development of Model Monitoring Tables:
Created a table to store the final output of weekly retraining of elasticity models. This table includes fields for the retraining date and model version, which automatically update during each retrain to capture the exact timestamp and version, allowing for performance tracking over time.
Developed a second table to monitor week-to-week model drift, focusing on changes in predictions and errors between recent retrains. This table is populated by selecting data from the most recent training runs and employing window functions to compare current metrics with previous ones.
Calculated various drift metrics, including percentage changes in price and demand, elasticity variation, deviance (model fit), and prediction error differences. These metrics support ongoing monitoring, enable quick identification of performance shifts, and assist in decision-making regarding retraining strategies.
The drift metrics are stored over time, providing a historical record that enhances governance, tracking, and model performance transparency.

---

## Update 61

**Date:** 2025-07-11
**Business Area:** Project Axiom
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Completed Tasks on Guest Service Chat:
• Dashboard Optimization: Updated the dashboard to exclude incomplete sailings, ensuring that they do not skew the average physical guest logs data. • Question-Answer Relevancy Review: Reviewed and refined the logic for question-answer relevancy to ensure the chatbot provides accurate and contextually appropriate responses to guest inquiries. • Stakeholder Meetings: Held discussions with stakeholders to review progress and align on next steps and upcoming project priorities.

### Raw Update

Completed Tasks on Guest Service Chat:
• Dashboard Optimization: Updated the dashboard to exclude incomplete sailings, ensuring that they do not skew the average physical guest logs data.
• Question-Answer Relevancy Review: Reviewed and refined the logic for question-answer relevancy to ensure the chatbot provides accurate and contextually appropriate responses to guest inquiries.
• Stakeholder Meetings: Held discussions with stakeholders to review progress and align on next steps and upcoming project priorities.

---

## Update 62

**Date:** 2025-07-11
**Business Area:** Project Axiom
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[cihan_ulus/overview_cihan_ulus|Cihan Ulus]]

### Summarized Update

Upcoming Tasks:
• App Reviews Focus: Based on stakeholder meetings, I will focus on analyzing app reviews this week to identify areas for improvement. • Exploratory Data Analysis (EDA): Begin with EDA to uncover patterns and insights within the app review data. • Topic Classification Development: Build a robust topic classification model to categorize app review feedback into actionable themes.

### Raw Update

Upcoming Tasks:
• App Reviews Focus: Based on stakeholder meetings, I will focus on analyzing app reviews this week to identify areas for improvement.
• Exploratory Data Analysis (EDA): Begin with EDA to uncover patterns and insights within the app review data.
• Topic Classification Development: Build a robust topic classification model to categorize app review feedback into actionable themes.

---

## Update 63

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

Weekly Report:
• Received PowerBI report from Augusto showing Conversions for CTI and BKTOCX. • CTI model shows opportunity for improvement in the rank ordering of probabilities. • Augusto connecting with Marketing team regarding CP leads as Will asked us to prioritize this lead, but also this lead may not need to be scored as Augusto has confirmed the business contacts almost all of these leads already.

### Raw Update

Weekly Report:
• Received PowerBI report from Augusto showing Conversions for CTI and BKTOCX.
• CTI model shows opportunity for improvement in the rank ordering of probabilities.
• Augusto connecting with Marketing team regarding CP leads as Will asked us to prioritize this lead, but also this lead may not need to be scored as Augusto has confirmed the business contacts almost all of these leads already.
• BKTOCX: Presentation Preparation for Royal and Celebrity.
Completed:
• Booking_ID Integration in output files: Use an existing column to include the Booking_ID, testing on Databrick environment.
• Collaborating with Chandra for testing process, tracking files drop, and validation on Siebel side.

---

## Update 64

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

Ongoing Task:
• OFTOCX data migration to UC: Collaboration with DE and Augusto team to ensure the migration of the OFTOCX dataset into UC. • Improve CTI model based on opportuities.

### Raw Update

Ongoing Task:
• OFTOCX data migration to UC: Collaboration with DE and Augusto team to ensure the migration of the OFTOCX dataset into UC.
• Improve CTI model based on opportuities.

---

## Update 65

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Workforce Planning Tool
**People:** Unidentified

### Summarized Update

Workforce Planning POC
Data Access
• Ongoing: Romeo Anselmo is currently working on granting me the necessary permissions to access the tables. Work Completed / Ongoing – Data Preprocessing / WPS Staffing Model Development
• EDA and reviewed basic daily call volume data for RES
• EDA and reviewed basic daily AHT forecast for RES
• Sourced functions from the international staffing model (ongoing)
• Modifying and adapting the functions to fit the North America context using similar logic (ongoing)
Functions are:
• steady-state probabilities: Calculates the steady-state probabilities for the Erlang A queueing model. • buffer_length: Computes the expected number of calls waiting (queue size beyond capacity).

### Raw Update

Workforce Planning POC
Data Access
• Ongoing: Romeo Anselmo is currently working on granting me the necessary permissions to access the tables.
Work Completed / Ongoing – Data Preprocessing / WPS Staffing Model Development
• EDA and reviewed basic daily call volume data for RES
• EDA and reviewed basic daily AHT forecast for RES
• Sourced functions from the international staffing model (ongoing)
• Modifying and adapting the functions to fit the North America context using similar logic (ongoing)
Functions are:
• steady-state probabilities: Calculates the steady-state probabilities for the Erlang A queueing model.
• buffer_length: Computes the expected number of calls waiting (queue size beyond capacity).
• waiting_prob: Calculates the probability that an incoming call will need to wait before being served.
• occupancy: Calculates the average proportion of agent time spent serving calls.
• abandon_prob: Estimates the fraction of calls that will abandon due to excessive waiting or impatience.
• service_level: Estimates the percentage of calls answered within a target time threshold (ASA = Average Speed of Answer), adjusted for abandon probability and system load.
Next Steps – WPS Staffing Model Development
• Run the model for the RES (LOB) to validate that the orchestration of the functions for the staffing model computations is working as expected.
• Prepare a project status walkthrough to be shared and used as a basis for discussing next steps.

---

## Update 66

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Current & Working on:
• MdAPE fix for uniform, medical and cococay models: Updated demand notebooks and call other consumption tables to see if this changes the product predicted and product actuals columns. No significant change was noticed for medical model, but CocoCay and uniform seem to be having issues. Target leakage was fixed for CocoCay but still a high mdape from my original code before changing the demand notebook.

### Raw Update

Integrated Business Planning (IBP)
Current & Working on:
• MdAPE fix for uniform, medical and cococay models: Updated demand notebooks and call other consumption tables to see if this changes the product predicted and product actuals columns. No significant change was noticed for medical model, but CocoCay and uniform seem to be having issues. Target leakage was fixed for CocoCay but still a high mdape from my original code before changing the demand notebook. Uniform model is running very slow which didn't usually so I believe it's an increase in data that I didn't notice before which I am debugging.
• Mapping Star of the seas and Xcel to newest sister ship in RCI/CCI HF&B model. Code seems to be working as intended. Will figure out a way to make it even more dynamic by using the deployment table for any other new ships and the consumption table as a way to know whether the new ship needs to be mapped or not. Dates to the dictionary are being added for new ships.

---

## Update 67

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Volatility Reports:
Completed:
• (1) Increased the threshold for flagging product + ship combinations with significantly high predicted demand from 100 to 1,000, for faster job execution and more storage. • (2) Added summary slide of Mario’s version of the volatility reports to the agenda. • (3) Presented to Yan on Thursday 7/10 for additional feedback and revisions before delivering to Mario.

### Raw Update

Integrated Business Planning (IBP)
Volatility Reports:
Completed:
• (1) Increased the threshold for flagging product + ship combinations with significantly high predicted demand from 100 to 1,000, for faster job execution and more storage.
• (2) Added summary slide of Mario’s version of the volatility reports to the agenda.
• (3) Presented to Yan on Thursday 7/10 for additional feedback and revisions before delivering to Mario.

---

## Update 68

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Pending:
• (1) A meeting to present the updated version to Mario (to be scheduled by Yan). • (2) Implement Yan's feedback: Add a new column showing the percentage/ratio change in predicted demand (increase/decrease); apply color coding/highlighting to emphasize significant changes; include a metric comparing prediction accuracy against actual consumption after the month ends; remove medical product categories from CocoCay and HF&B models.

### Raw Update

Integrated Business Planning (IBP)
Pending:
• (1) A meeting to present the updated version to Mario (to be scheduled by Yan).
• (2) Implement Yan's feedback: Add a new column showing the percentage/ratio change in predicted demand (increase/decrease); apply color coding/highlighting to emphasize significant changes; include a metric comparing prediction accuracy against actual consumption after the month ends; remove medical product categories from CocoCay and HF&B models.

---

## Update 69

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Uniforms Model:
Completed:
• (1) Updated the product name replacement logic in the ETL notebook to extract fabrics/materials, specific colors (raspberry, keylime, etc.), occupations, ship codes, and remove extra numbers/characters. • (2) Code successfully runs from ETL through Safety Stock Steps 1 & 2 for this model (running into issues starting from the Write Parquet Files notebook through to the Challenger model). • (3) Addressed the data type mismatches with product_name_number (arrays vs.

### Raw Update

Integrated Business Planning (IBP)
Uniforms Model:
Completed:
• (1) Updated the product name replacement logic in the ETL notebook to extract fabrics/materials, specific colors (raspberry, keylime, etc.), occupations, ship codes, and remove extra numbers/characters.
• (2) Code successfully runs from ETL through Safety Stock Steps 1 & 2 for this model (running into issues starting from the Write Parquet Files notebook through to the Challenger model).
• (3) Addressed the data type mismatches with product_name_number (arrays vs. strings) by exploding arrays into separate rows for joining, and will later work on rebuilding them.
• (4) Currently fixing issue where the product actuals were being overwritten by the consumption table.

---

## Update 70

**Date:** 2025-07-11
**Business Area:** Unclassified
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Integrated Business Planning (IBP)
Pending:
• (1) Provide a file with sample of the product name modifications to Yan for approval. • (2) Continue fixing code. • (3) Prepare the Uniform V3 model overview presentation.

### Raw Update

Integrated Business Planning (IBP)
Pending:
• (1) Provide a file with sample of the product name modifications to Yan for approval.
• (2) Continue fixing code.
• (3) Prepare the Uniform V3 model overview presentation.
Other Pending Work:
• Add CocoCay metrics to dashboard.

---

## Update 71

**Date:** 2025-07-11
**Business Area:** Customer Lifetime Value
**Business Project:** Cross-Brand Credit Card Strategy
**People:** Unidentified

### Summarized Update

Completed:
• Completed data validation of NPS data confirming Ship and Brand NPS matches known values. • Identified indirect cost as the root of solo's value indexing being unexpectedly high by cloning and modifying the analytics table pipeline with altered cost calculations. • Created a per-booking level table for Corporate Strategy, grouped by cabin class, cohort, and sailing displaying sample sailing data on the full math walk for our index calculations.

### Raw Update

Completed:
• Completed data validation of NPS data confirming Ship and Brand NPS matches known values.
• Identified indirect cost as the root of solo's value indexing being unexpectedly high by cloning and modifying the analytics table pipeline with altered cost calculations.
• Created a per-booking level table for Corporate Strategy, grouped by cabin class, cohort, and sailing displaying sample sailing data on the full math walk for our index calculations.
• Met with Trade to detail how CLV can compliment their booking-level information for valuable demographic insights.

---

## Update 72

**Date:** 2025-07-11
**Business Area:** Customer Lifetime Value
**People:** Unidentified

### Summarized Update

Ongoing:
• Began sorting columns by aggregation method for the eventual creation of a clean, booking-level CLV table for future use cases from air, trade, and more…
• Documenting assumptions and calculations in Excel. • Began investigating alternatives to absolute pax or booking indirect cost rates, weighing logical methodology to potentially find a hybrid rate. • Identifying exact area of analytics ETL pipeline where passengers are being duplicated.

### Raw Update

Ongoing:
• Began sorting columns by aggregation method for the eventual creation of a clean, booking-level CLV table for future use cases from air, trade, and more…
• Documenting assumptions and calculations in Excel.
• Began investigating alternatives to absolute pax or booking indirect cost rates, weighing logical methodology to potentially find a hybrid rate.
• Identifying exact area of analytics ETL pipeline where passengers are being duplicated.

---

## Update 73

**Date:** 2025-07-11
**Business Area:** E-Commerce
**Business Project:** Booking Propensity Models
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]]

### Summarized Update

Completed
• Implement algorithm for summarizing SHAP values per feature values. It provides faster computation of SHAP dependency plot and smaller storage footprint. This will allow for dashboard SHAP values dependency plots for all the models-features combination, now only plots for top 10 features are available.

### Raw Update

Completed
• Implement algorithm for summarizing SHAP values per feature values. It provides faster computation of SHAP dependency plot and smaller storage footprint. This will allow for dashboard SHAP values dependency plots for all the models-features combination, now only plots for top 10 features are available.
• Improve feature selection algorithm by automatically detecting optimal number of features for each models, right now a fixed number is been used.
• Optimized Databricks Dashboard queries and adjusted to include past guests and prospective guests.
• Visualized predicted cabin class distribution from next best offer results, visualizing spending and fare based on APD models and PHML distribution.
• Experimented with genie to provide better response along with optimizing sample queries.

---

## Update 74

**Date:** 2025-07-11
**Business Area:** E-Commerce
**Business Project:** Genie Application Enhancements
**People:** [[carlos_gonzalez_andarcio/overview_carlos_gonzalez_andarcio|Carlos Gonzalez Andarcio]]

### Summarized Update

Upcoming Tasks:
• Meet with E-commerce to iterate through dashboard and tailor visualizations. • After discovering an issue with the top 5 destinations visualization, the data pipeline will need to be adjusted in order to ensure accurate destinstion distribution. • Begin gathering feedback on newly optimized genie space and adjust chat bot instructions for better responses.

### Raw Update

Upcoming Tasks:
• Meet with E-commerce to iterate through dashboard and tailor visualizations.
• After discovering an issue with the top 5 destinations visualization, the data pipeline will need to be adjusted in order to ensure accurate destinstion distribution.
• Begin gathering feedback on newly optimized genie space and adjust chat bot instructions for better responses.

---

## Update 75

**Date:** 2025-07-11
**Business Area:** WoW
**Business Project:** Forecasting Pipeline Expansion
**People:** [[ayon_ghosh/overview_ayon_ghosh|Ayon Ghosh]]

### Summarized Update

1) Supporting FPMS roll out - with MDR rules engine adjusting, Couchbase schema matching and hotfixes
2) Completed accuracy testing of V1 pipeline for specialty - shows 35-40% improvement overall
3) MDR V1 hotfixes

### Raw Update

1) Supporting FPMS roll out - with MDR rules engine adjusting, Couchbase schema matching and hotfixes
2) Completed accuracy testing of V1 pipeline for specialty - shows 35-40% improvement overall
3) MDR V1 hotfixes

---

## Update 76

**Date:** 2025-07-11
**Business Area:** WoW
**Business Project:** Improved Forecasting Accuracy
**People:** Unidentified

### Summarized Update

1) MDR V1 and specialty V1 development, unit, integration, and stress testing  is complete
2) Supporting FPMS roll out in multiple ships
3) specialty accuracy testing is complete
4) MDR accuracy testing  - to be completed next week
5) all rules engines requires to be tweaked next week

### Raw Update

1) MDR V1 and specialty V1 development, unit, integration, and stress testing  is complete
2) Supporting FPMS roll out in multiple ships
3) specialty accuracy testing is complete
4) MDR accuracy testing  - to be completed next week
5) all rules engines requires to be tweaked next week

---

## Update 77

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Conversational IVR
**People:** Unidentified

### Summarized Update

Accomplishments
Deployed new FAQs, Routing changes and NLU changes to both RCI and CEL
Presented analysis of 200 conversations to brand for iterative improvement suggestions in the backlog
Analyzed decrease in automated minutes and determined it is issues with the make a payment flow.

### Raw Update

Accomplishments
Deployed new FAQs, Routing changes and NLU changes to both RCI and CEL
Presented analysis of 200 conversations to brand for iterative improvement suggestions in the backlog
Analyzed decrease in automated minutes and determined it is issues with the make a payment flow.

---

## Update 78

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Conversational IVR
**People:** Unidentified

### Summarized Update

Working On
CoPilot Migration architecture
Development of backlog
Research into generative answers and knowledge sources
Updates to existing mix application for routing
Discussions around post deployment IT structure
Guest profile API initial kick off

### Raw Update

Working On
CoPilot Migration architecture
Development of backlog
Research into generative answers and knowledge sources
Updates to existing mix application for routing
Discussions around post deployment IT structure
Guest profile API initial kick off

---

## Update 79

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Cresta AI Analytics Tools
**People:** Unidentified

### Summarized Update

Accomplishments
Finalized agent and supervisor dashboard
Sent out first cresta insights report and developed automated extraction
Developed analytics tools for outliers for performance
Removed archived articles from genka

### Raw Update

Accomplishments
Finalized agent and supervisor dashboard
Sent out first cresta insights report and developed automated extraction
Developed analytics tools for outliers for performance
Removed archived articles from genka

---

## Update 80

**Date:** 2025-07-11
**Business Area:** Contact Center
**Business Project:** Cresta AI Analytics Tools
**People:** Unidentified

### Summarized Update

Working on
Research into speech IQ report sunsetting
Research into data integration
GenKA updates for articles surfacing and factoids
AI analyst pilot definition
Determination on how to setup category tracking

### Raw Update

Working on
Research into speech IQ report sunsetting
Research into data integration
GenKA updates for articles surfacing and factoids
AI analyst pilot definition
Determination on how to setup category tracking

---

## Update 81

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** Fleetwide Energy Monitoring
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

•	Tag mapping for ML Class Engine Room Ventilation Fans, Machinery Pumps, DG Waste Heat Recovery, Variable Chilled Water Flow, AHU Cooling TCVs, Reverse Osmosis, Fresh Water, and Energy Recovery Wheel areas. •	Added machinery power breakdown calculations for the fleet. •	Integrated Navigator OPC UA server data into the MIAP platform.

### Raw Update

•	Tag mapping for ML Class Engine Room Ventilation Fans, Machinery Pumps, DG Waste Heat Recovery, Variable Chilled Water Flow, AHU Cooling TCVs, Reverse Osmosis, Fresh Water, and Energy Recovery Wheel areas.
•	Added machinery power breakdown calculations for the fleet.
•	Integrated Navigator OPC UA server data into the MIAP platform.
•	Met with the Maritime Security team and reviewed their requirements for a live fleet monitoring solution combined with future deployments. The team wants to see fleet location live, with a map overlay of important information such as global threats.
•	Reviewed NAPA API data requirements with the Marine Safety team.
•	Reviewed Crosser IoT platform benefits with the Enterprise Architecture team.
•	Attended the monthly Data Science and Decarbonation team meeting. Agreed on accelerating fuel savings in preparation for MIAP Phase IV CAR.

---

## Update 82

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[mahshad_shariatnasab/overview_mahshad_shariatnasab|Mahshad Shariatnasab]]

### Summarized Update

Added incinerator plots to the GMP app. •	Finalized OFB for the GMO app and prepared it for production. •	Contacted the ship for WN regarding 100 kW savings on AHUs in cabins and public areas.

### Raw Update

Added incinerator plots to the GMP app.
•	Finalized OFB for the GMO app and prepared it for production.
•	Contacted the ship for WN regarding 100 kW savings on AHUs in cabins and public areas. They responded that the issue is related to customer complaints, and we are currently investigating optimization.
•	Started working on ML class savings and on new machinery ventilation room fans, as well as the DG high-temperature cooling water waste heat recovery system, exploring potential savings in these areas.
•	After our team’s visit to SM and communication with the engineering team, we identified the following savings:
o	New WN savings of approximately $36k for Chiller A’s extra consumption, ongoing for the past six months.
o	New SM savings of around $100k for machinery water pump issues persisting for the past year.
o	New SM savings of approximately $40k for ventilation fans in the chiller room, ongoing for the past two years.

---

## Update 83

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** Fleetwide Energy Monitoring
**People:** [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]]

### Summarized Update

•	Calculated the Energy Recovery Wheel (ERW) utilization across the entire fleet and added corresponding diagnostic plots for both the fleet and individual ships in the GMO app. This feature helps identify ships that are under-utilizing the energy recovery wheels in air handling units, enabling targeted actions to improve energy savings by contacting those ships. •	Currently working on the calculation of cooling power on the water side, which will be used to monitor the cooling performance of air handling units (AHUs) in future enhancements.

### Raw Update

•	Calculated the Energy Recovery Wheel (ERW) utilization across the entire fleet and added corresponding diagnostic plots for both the fleet and individual ships in the GMO app. This feature helps identify ships that are under-utilizing the energy recovery wheels in air handling units, enabling targeted actions to improve energy savings by contacting those ships.
•	Currently working on the calculation of cooling power on the water side, which will be used to monitor the cooling performance of air handling units (AHUs) in future enhancements.

---

## Update 84

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

•	Updated all MIAP release/deployment pipelines to leverage the new Agent Pools created by the Platform team. •	Performed EDA on ALS data to quantify efficiency gains from ALS utilization per ship. •	Added Eniram weather-normalized power feature to the propulsion features table.

### Raw Update

•	Updated all MIAP release/deployment pipelines to leverage the new Agent Pools created by the Platform team.
•	Performed EDA on ALS data to quantify efficiency gains from ALS utilization per ship.
•	Added Eniram weather-normalized power feature to the propulsion features table.
•	Deployed Hull Degradation chart to the GMO app in production.
•	Created a process that, for each quarter, fits a line to the propulsion power consumed by each ship with ALS on vs. off, and calculates the gross ALS power savings at each speed interval.
•	Created a visualization in GMO (deployed to production) that shows ship-level ALS savings over time.
•	Tuned the AHU Analytics job, reducing runtime by over 50% and preventing consistent failures.
•	Saved Hull Degradation model output to a table to prevent unnecessary scoring of models during API calls, improving response time by over 30%.

---

## Update 85

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** Unidentified

### Summarized Update

•	Added MGO Equivalent SFOC features for individual power plants (DG, GT, Fuel Cell). •	Created individual MGO EQ SFOC power plant base and dynamic models. •	Created a new power plant outlier removal method to remove instances where the engine first turns on or off.

### Raw Update

•	Added MGO Equivalent SFOC features for individual power plants (DG, GT, Fuel Cell).
•	Created individual MGO EQ SFOC power plant base and dynamic models.
•	Created a new power plant outlier removal method to remove instances where the engine first turns on or off.

---

## Update 86

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** Historical Data Integration
**People:** Unidentified

### Summarized Update

June 27th
•	Identified an issue with a production workflow in MIAP Analytics. •	Focused on troubleshooting, implemented the necessary fixes, and successfully pushed the updates to production. The workflow completed without issues.

### Raw Update

June 27th
•	Identified an issue with a production workflow in MIAP Analytics.
•	Focused on troubleshooting, implemented the necessary fixes, and successfully pushed the updates to production. The workflow completed without issues.
July 1st
•	Connected with the Ignio AMOS team to perform end-to-end testing.
•	Gathered insights on additional changes needed.
•	Discovered that some tags are missing in production due to transformation issues with Eniram.
•	Addressed this by adjusting the approach to handle missing tags through chunking based on time intervals rather than variables.
July 2nd
•	Tested and validated the new Eniram approach across multiple scenarios.
•	Made adjustments to the logic in the shipcode column.
•	Sent an email to the Eniram team detailing the list of missing tags, vessel-wise.
July 3rd
•	Cleaned up the new approach and raised a pull request.
•	Currently working on the historical load for Eniram.
•	Developing an AutoLoader approach and creating a separate workflow.
•	Experimenting with different strategies to efficiently retrieve data from the API.

---

## Update 87

**Date:** 2025-07-11
**Business Area:** MIAP
**Business Project:** MIAP Operating Efficiency Enhancements
**People:** [[mehdi_assefi/overview_mehdi_assefi|Mehdi Assefi]]

### Summarized Update

•	Working on stability PDF parsing and feature engineering.

### Raw Update

•	Working on stability PDF parsing and feature engineering.

---

_Source: 20250711 - Raw Weekly Matt and Rafeh Report .docx_