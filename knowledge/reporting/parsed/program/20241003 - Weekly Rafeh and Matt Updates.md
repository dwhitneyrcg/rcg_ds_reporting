**Proud****:**

- **Demand Forecasting (Supply Chain):** Delivered a new forecasting approach that has significantly improved the quality of financial forecasting accuracy of the Base-Rate Reconciliation Tool (RCI/CEL) from ~75% to 80%. *Next steps are to productionize Uniform Demand Models**, continue preparation of the 2025 Supply Chain CAR, and resume enhancements for Silversea HF&B models. *

- **Medallia GenAI Pilot Use-Case**** (Hotel Operations)****: **DS team delivered the initial topic classifier model, which includes text summarization, sentiment, entity recognition, and topic classification. The team is now focusing on building AI-generated drill-drown reports to monitor KPIs. *Expecting delivery of the **Medallia GenAI** pilot by end-of-year **and** a pilot **ready** for crew testing **by** early November.*

- **Loyalty Simulator (Loyalty)****: **Presented Loyalty Simulator overview to Silversea leadership teams and aligned on upcoming Simulator deliverables for Silversea. Also identified a new use-case for the Loyalty Simulator Clustering model, which will help our Corporate Planning teams in a LTV profitable analysis by channel. DS Team has completed a major simulator improvement (normalizing for pricing inflation) and working to integrate Silversea onboard spend. *Next week team should have clustering model updated to include Silversea customers.*

- **PROPEL:** MLOPs team relaunched PROPEL on Reflection and focused on a bug-fix for Infinity. Robust backup process prevented bug-fixes from delaying PROPEL offers being shared with guests on Infinity. *Next steps are to continue scaling **PROPEL **solution across the CEL fleet.*

- **Revenue Management (CEL):** DS Team completed revisions for the MTRB Track Optimization process based on business feedback. The Track Optimization pilot is adapting RCI’s MTRB solution to incentivize sailing alignment for sailings sharing substitutable demand. Completed initial design for enhancing TAP Perks automation (that will optimize the gap between Cruise-Only and All-Inclusive Fares). *Beginning development of an AB Test to identify revenue-optimizing gaps for the TAP project.*

- **Revenue Management (****SSC****):**** **DS Team completed MVP elasticity modeling for SSC and received positive feedback on PRE pause file reporting. DS/DE teams met with SSC to plan out a Q4 delivery of a workaround “writeback” approach (a manual, bulk upload process) that will enable SSC to achieve daily pricing automation without additional funding. *Next steps are to review pricing elasticities with the Silversea RM team and begin **BPO planning to optimize pricing gaps through TAP automation (e.g. Port-to-Port vs Door-to-Door fares). *

**Excited****:**

- **App Incremental Revenue Analysis (Digital): **Team is assisting Andrew Smith and Liz Oates in estimating the incremental revenue benefit of the Digital app.  Team is developing regression models to isolate the incremental impact of the app on ticket bookings and precruise revenue from environmental confounds. *Early results of the regression analysis expected within 1-2 weeks.*

- **Customer Targeting (E-Commerce): **DS** **Team working on dashboard enhancements and model maintenance. *Conducted planning sessions for Q4 and 2025 deliverables with E-Commerce teams. Planning to prioritize development of look-a-like models to identify multi-**branded customers for Cruise-Match and enrich targeting models with ongoing market campaign data).*

- **Marine Insights Analytics Platform (Marine Operations):** Met with new Marine Operations VPs (Brian Sorenson, Han Solum and Ashlee Aleman) to introduce MIAP and DA2I. DS Team beginning development for new Digital Twin models of Power Plant and SFOC for new LNG-based ships and refactoring MIAP dynamic modeling approach for Digital Twin and Fuel Forecasting.

- **Lead Prioritization**** (Contact Center)****:** DS team validating model performance for new Booked-to-Cancel model and beginning a code review to develop a new CTI lead prioritization model. *By end of year, **we **will **have **introduce**d** Lead Prioritization for CEL (a high priority by the CEL Contact Center**)**, but** will also** update** and benefit Lead Prioritization** models **used by** RCI**.*

- **PCP “****MyCruise****” Product Recommendations**** (Digital)****:**** **DS team is adapting the PCP Product Recommendations for additional use-cases by the Emails team and created a workflow this week that updates all Product Recommendation Data. *Working with business units to create an automated workflow that makes product recommendations available in Salesforce for usage by the Email team. *

- **PCP Pricing Automation:** DS Team completed the MVP Cabanas Pricing Optimization Algorithm and a supporting Dilution Model. Also introduced model to CEL Onboard Revenue teams for their constructive feedback. Next steps are to productionize initial MVP models and begin work on a Dynamic Pricing Algorithm for Cabanas.

- **Revenue Management (RCI):** DS Team focused on fixing Production Bugs this week and actively working on enhancing the (a) SPI model with Sailing Management Factors and (b) Elasticity Models with model retraining. MLOPs Team continued to work on PRE code-refactoring, conducted Group gapping testing, and Unity Catalog Migration. *Planning to productionize MVP SPI model soon and begin integrating SPI into TAP automation projects. *

- **Win-on-Waste Forecasting (FPMS):** DS team actively experimenting with different approaches for forecasting consumption in the Main Dining Room. *One MVP approach is already displaying promising accuracy and team will finalize our forecasting approach by **our **November** 7**th** deadline**.*

**Concerned:**

None

MEDALLIA COE

The team has delivered the topic classification component which completes the AI modeling portion of the work. This includes summarization, sentiment, entity recognition, and topic classification. The team will now begin the next phase which includes building analytical reporting to monitor the key KPI's.

MYCRUISE RECOMMENDER

PCP contractor has been identified and will join the team next week.

EMAILS RECOMMENDER

Added a workflow to the ETL which updates all Product Recommendation data. Working with stakeholder to implement one additional ETL to move data to Salesforce.

WOW

LEAD PRIORITIZATION – BKTOCX

The team is continuing to validate model performance with expectations that there may be target leakage.

LEAD PRIORITIZATION - CTI

The team is conducing extensive code review over legacy code base to train/retrain CTI models for RCI/CEL

DIGITAL APP INCREMENTAL REVENUE ANALYSIS

Team is performing regression analysis three strategies:

- consumer, booking, and sailing level regressions on ticket booking rev and affect of channel,

- consumer, booking, and sailing level regressions on precruise onboard rev and affect of channel,

- first version comparing avg APD app vs web

- Working on additional lookalike model

LOYALTY:

Feature Engineering on SSC and combined with Royal and Celebrity data (ongoing).

WOW:

- Approach 1 for MDR is complete with a fair accuracy so we already have a deliverable ready for Nov

- Approach 2 which is the 7D aggregated guard modelling is complete however the results are dismal due to very very low number of records. Team continue to work to improve accuracy (have time till Nov 4)

- Data validation Tool prototype review complete

Working towards factoring MIAP dynamic modelling framework to prepare for digital twin modelling and fuel forecast. Completed feature engineering and base model pipelines. Residual learning model re-factoring is remaining.

Building feature dataset for power plant analytics for new LNG based ships and preparing for dynamic SFOC modelling.

Bug/stress testing curve fitting Python package, fine tuning fits with splines.

EDA work in progress for power plant signals in preparation for fuel forecast CAR.

Progress with live data streaming capability of MIAP API for shipboard data.

Ready to move first iteration of MIAP data visuals of GMO App for HVAC Analytics

Met with GMO VPs Brian Sorensen, Jan Solum and Ashlee Aleman to introduce Data Analytics & AI and MIAP

On-going interviews for Sr. ML Engineer position and GMO IoT Program Associate role

GSCBP:
1. Base-Rate Reconciliation Tool (Finance Tool): Identified that we can make the variance in units and dollars less by improving the way we join historical model predictions to the finance tool by aggregating the historical voyage level predictions to the monthly level and then prorating the monthly level historical predictions down to the finance tool at the voyage level. 
a. We discussed this solution with our stakeholders and aligned on the new process and implemented the code to achieve our objectives. 
b. The impact of this improvement is that for the back tested month of August, the Prediction accuracy for Royal improved from 75% using the previous approach to 81% and the improvement for CEL was from 74% with the previous approach to 79%. 
2. RCI/CEL Demand Forecast Reporting: Made small refinement to the unreconciled demand forecasts report for procurement. 
3. Uniform Demand Modeling: 
a. Modifying historical consumption table to fix final MdAPE
b. Reported to Yan the final MdAPE using original model with 57%
Next Steps:
1. Resume feature selection work for Silversea HF&B models
2. Onboard contractor who will be starting Monday on the project of continuing our meta-model work which attempts to calibrate our demand forecasts by learning from historical errors. This new approach will be designed to predicted at a cost level instead of a quantity level. Since product costs continually change, there will be some significant work to create the dataset to identify the cost of the product at historical time steps. Yan has provided an overview of the three step process she uses to calculate costs, which will have to be dynamically calculated for each historical model training date. 
3. Uniform Demand Models Productionization using Databricks pipeline
E-Commerce
1. Improve dashboard: 
a) Deploy experimental functions to dev-stage dashboard , in order to be evaluated by eCommerce team before moving to prod dashboard
2. Models maintenance: 
a) Update and evaluate production pipeline with latest epsilon data -txsend and demographic.
b) create scoring summary table as a wide version of current scoring table - alpha only
c) Implement destination propensity models improvement in dev, by converting bp_dest model to bp model + dest model
Loyalty:
Model Improvements:

• APD growth has been normalized in prior periods to remove effects of economic inflation on tier distribution. Still awaiting pipeline run to visualize new tier distribution in prior periods, and get stakeholder feedback. 

• Kiana Almira has provided some preliminary SSC onboard spend queries. The existing data available for SSC only has ticket revenue, so this will be a big improvement and vital to the integration of SSC.

• Further pipeline stabilization and modularization efforts including automation of dev and prod table updates driven by working environment.

• Integration of SSC data in clusters is close to completion. New clusters should be updated and deployed in the pipeline next week.

• Designed spend model framework to be implemented in the next 6 weeks. This is a major improvement to the existing historic spend sampling, that does not take itinerary effects on spend into account. EDA has begun this week.

Concerns:
De-duping of SSC guest data and identifying guests cross-sailing on SSC with another brand is still not possible. For the time being we have GCP_Key for SSC guests on a very limited basis. We can use the current individual id field for SSC, but this field has known flaws and dupes. This makes scoping guest tier composition somewhat unreliable when using a tri-branded spend approach.

**PROPEL**

Re-launched PROPEL on RF (Reflection).

Fixed bug issue in Dev Environment for Infinity, which is launching in prod on Oct 7.

Issues:

The workflow (job) to process new data for OBR Total Revenue was not finishing after 23 hours. Re-enabling Photon specifically for that job fixed the problem (runs in 1hr again). All other workflows running well without photon.

A change in the offer text caused pipelines to fail since it is used as a join column. To avoid this issue in the future, Alejandro is converting that to use an offer id.

*Fortunately** the backup process finished last week kept everything running smoothly while these issues were resolved. Without it, offers would have failed to go out.*

**RMA**

PRE Lite Framework (Eswar):

Framework in production on Monday.

Group Gapping Framework (Vikas):

Group gapping testing planned to finish this Friday to release to prod next week.

Unity Catalog Migration:

3 tables refactored throughout all projects to use Unity Catalog: v_df_categories, suite_classes, and mkrt_groupings. (Eswar)

Latest v_availability_history and latest availability_history views are now on hold (Satheesh). Availability_history needs to be partitioned in prd_silver by read_date so it can be used. This is being delayed by an upgrade to the CIF to allow partitioning data. (DE team working on it)

Data Engineering got approval from Rafa to ingest the needed tables to Unity Catalog, however, the access group needs to be cleaned up, delaying access to the RMA users. (Monica Aversa & team)

Issues (eventful week):

PRE failure: a missed reference to v_df_categories due to outdated code in QA caused the changes to Unity Catalog in the PRE to pass QA but fail in PROD on Monday. It was fixed Tuesday in time for the recommendations to go out on Wednesday. The QA branch is now up to date and will be monitored ongoing.

TAP failure: the number of allowed concurrent connections to oracle was exceeded. To avoid this in the future, the queries in that pipeline will be prioritized for Unity Catalog Migration.

Track prod failure: The output table being written to in oracle was updated in DEV and QA to support the new column, but was not changed in PROD causing the process to succeed in DEV & QA but fail in PROD. Moving away from writing to oracle would reduce the chances of the output table being out of sync.

**HIRING**:

Contractors:

Javier Buitrago to start next week. (CAP build)

FTEs:

Ajay Kumar - pending interview with Mert & David W for MIAP role.

Other candidates pending interviews

**OTHER**:

1. RCGGPT

Shared usage metrics with InfoSec for estimating load on their prompt security tool.

Pending - need to fix the code blocker bug and implement separate coding GPT.
