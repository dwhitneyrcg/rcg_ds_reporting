**Erick **

**For ****pr****roject**** Axiom**** (***AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data**), Erick and his team accomplished:*

**Meta Data Extraction**

**Venue Identification** *(David M.)*: Hybrid regex + embeddings approach showing promising results for accurately identifying venues in guest comments. This is intended to improve Venue identification with LLMs during meta data extraction process.

**Venue Dictionary** *(Gourish P.)*: Compiling gold-standard mapping of venue names to guest-referenced variations which will feed into Venue identification process.

**Reporting**

**Silversea**: Division-level ETL for SSC is in-progress.

**Royal Beach Club Email** *(Rodrigo)*: Template complete. Blocked on Data Engineering for RBC-specific Medallia field.

**ShoreX**** Safety** *(**Danusio**)*: Delivered ShoreX safety email automation with all requested columns. In stakeholder review. ✅

**Quiet Spaces Analysis** *(New)*: Request from CEL Consumer Insights to analyze guest sentiment on quiet areas (Hideaway/Library) on Celebrity Reflection ahead of dry dock renovations in 2027.

**Modeling**

**Drivers Model** *(Osvaldo)*: POC complete. Deploying to GPU API for real-time SHAP calculations—ensures we deliver a fast responsive tool.

**Guest Logs Classifier** *(David)*: Working with Stakeholder to continually clean up +1400 unique topic combinations of topics in Guest Logs dataset.

**Medallia Genie**: Pending business validation.

**Project AI Pivot *****(Qualtrics Topic Extraction)***

*Self-labeling framework for automatic topic discovery from survey data.*

**Danusio**: Baseline clustering complete (36 clusters). Next: BERTopic comparison.

**Rodrigo**: Generalizing implementation on Abandoned Cart survey so it fits other surveys such as Brand Tracker survey.

Erick & Cristian

**MyCruise**** Recommender**

*For the **MyCruise** Recommender (**Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app**), Erick and Cristian have:*

**A/B Testing *****(Cristian V.)***

Completed testing framework. Brainstorming and knowledge share session meeting Jan 16 to discuss next steps and propose additional testing.

**Calendar Recommendations**

Coordinating with Digital Engineering on stage data access for QA.

Mert

MIAP

Achieved $80K fuel savings on Wonder and Symphony from AHU systems.

Reviewed MIAP Phase IV sensor installations with the electrical team.

Conducted a follow-up meeting with Corporate Strategy, Risk Management, and the Finance Transformation Hub on Project TIDE (Claims Management). The project is currently paused due to the finance team's concerns about the requested headcount. The most likely resolution is to merge Project TIDE with IBP.

Completed the Alarms and Events monitoring ETL pipeline and fully productionized it. This new dataset will allow us to monitor alarms from shipboard systems and help prevent alarm fatigue by analyzing unnecessary alarms. There is about one alarm every ten seconds in the engine control room, which creates a serious safety concern.

Completed RCG's first fully custom and scalable agentic AI framework on Azure Container Apps, served via the MIAP API. The solution uses Azure AI Foundry foundational models, LangChain for tool calling, and LangGraph for orchestration. It enables creation of custom tool-calling agents and multi-agent/supervisor agent architectures. The solution is connected to access resources on Databricks; integration with Azure AI Search and Copilot Studio is next. This will serve as the foundation for advanced diagnostics agents for marine and energy.

Demoed MIAP solutions to Mauricio Lacayo, AVP of the Fuel Procurement team. Agreed to support the team with real-time fuel tank monitoring on the MIAP app.

Mahshad

MIAP

Added boiler plots to the GMO web app.

Implemented an anomaly-detection agent that connects to the API and fetches data from the plots.

Currently developing the prompt-engineering component to extract data from the plots.

Ram This week

MIAP

Successfully deployed the new shipboard streaming approach to production.

Updated the existing "purge MIAP logs" notebook in the Marine workspace to include:

MIAP REST API log clearing

Model clearing logic

Collaborated with the Wartsila team to investigate their issue and identified the root cause.

Migrated Sea Events and VPS jobs to the DE workspace.

Connected with the GenAI Engineer and Data Science Manager to understand cost adjustment requirements for vendor REST API usage.

Next week

Monitor the VPS and Sea Events workflows in the DE workspace.

Update the silver tables for VPS and Sea Events in the Marine workspace to read from the new bronze tables in the DE workspace.

Once the shipboard team completes the SQL Server changes, test the REST API to validate whether the Wartsila issue is fully resolved.

Start implementing vendor cost management and explore options to retrieve and analyze Azure cost data.

Reza

MIAP

Working on the fuel forecast platform to ensure it runs for all ships/legs.

Some steam turbine gas models were causing the optimizer to fail. The issue was identified and resolved. Continuing to run the pipeline and fix bugs as they are found.

Following up on an elevated speed issue in the deployment.legs table for the maneuvering phase. Almost all cases are fixed except for three ports in Norway where Royal has limited data.

Arya

MIAP

Started working on a live ship tracker map, planning to integrate it into the MIAP app soon.

Found bugs with coordinate code and added a temporary fix (multiplying by -1 for some ships).

Gave a presentation on Azure AI Search.

Added EQ to chiller.

Updated the GMO app with XC and EX.

Will

MIAP

Completed the LNG optimization class with testing notebook and mathematical outline.

Added three ships to the power plant workflow (IC, GR, OV); in the process of adding two more and identifying data issues in ten additional ships.

Continuing to productionize the LNG optimizer.

Ben & Camila

Supply Chain AI (IBP)
Supply Chain: Leadership approved using AI demand forecasts as the basis for the rest of year budget on Celebrity Beyond; first full month of AI driven order creation starts in March.
• Celebrity Beyond – AI Forecast Adoption
o Keith Lane and supply chain leaders unanimously agreed to set the rest of year budget for Celebrity Beyond using our AI forecasts.
o First full month of AI driven order creation goes live in March, making Beyond our first fully AI budgeted ship.
• RCI/CCI/SSC Consolidated Spend Report
o Built the consolidated spend report across RCI/CCI/SSC; awaiting final port code and local market mappings from the business team for full deployment.
• SSC Uniforms Demand Forecast
o Completed initial uniform demand forecast model code.
o Identified a data limitation: crew data currently maxes out at Dec 2025, truncating the training window and limiting predictive reach. Debugging why training data is cut off and coordinating with data owners to extend it.
In Progress / Next
• Enhancing medical and uniform models, including incorporating crew consumption adjustments on backtested data to improve accuracy.
• Connecting IBP Intake Form changes to HF&B guardrails so that updates from Fanny’s team are automatically reflected in planning logic.
• Finalizing and communicating the min/max par volatility report to Brenda and team to support tighter inventory controls.
Risks / Needs
• Data dependency: Extended, validated crew data beyond Dec 2025 is required to fully operationalize and future proof uniform forecasting.

Carlos
E Commerce Customer Targeting
Deployed the first iteration of the consumer down selection algorithm, migrated reporting logic to PySpark, and validated correct updates of key tables.
• Scoring Efficiency
o Tested and deployed the first iteration of the algorithm to reduce the consumer population to be scored, improving performance and cost efficiency.
• Spend Stretching Bug Fix
o Found and corrected a bug in spend stretching (bin mismatch between ground truth and predictions), improving calibration of spend based outputs.
• Reporting & Platform Modernization
o Investigated issues in the reporting notebook feeding the Databricks dashboard.
o Converted all reporting SQL queries to PySpark and validated that distribution tables now update correctly with no observed errors.
o Met with e Commerce stakeholders to align on the consumer scoring schedule.
Next
• Begin maintenance and cleanup of the Streamlit dashboard and underlying data sources.
• Implement a Streamlit filter to suppress booked guests, focusing scoring and reporting on incremental opportunity.
• Review and prioritize tickets for ingesting call center data, new Epsilon data, and Genie, to expand feature coverage in future scoring iterations.

Mirielle
Contact Center – Offer to Cancel & Workforce Planning

Resolved a 3 day Offer to Cancel (OFTOCX) outage caused by a Databricks firewall change; restored main workflow and improved resiliency.
4.1 Offer to Cancel (OFTOCX)
Incident & Resolution
• The OFTOCX workflow failed for three consecutive days without email alerts due to a Databricks firewall change that blocked writes to the SFTP location.
• Actions taken:
o Met with Augusto to coordinate triage and remediation.
o Released a temporary pipeline at 11:00 AM to maintain continuity while troubleshooting.
o Built and deployed temporary pipelines for RRI and CC to avoid additional data gaps.
o With support from Marcio, Glen Erick and team, refined and restored the main workflow to production.
Recommendation
• To reduce time to detect and prevent silent failures, add failure notification emails for OFTOCX to:
o mfeudjio@rccl.com
o bfowler@rccl.com
o cgonzalezandarcio@rccl.com
o atomszay@rccl.com

Mirielle
Contact Center Workforce Planning – North America (Call Volume Forecasts)
• Trained, tested, and back tested call volume forecasting models for 3 of 12 LOBs:
o CO_SALES, RES, CO_CE_SERVICES
• Data windows:
o Train/Test: time based 80/20 split from 2023 01 01 to 2025 10 31.
o Back testing window: 2025 10 31 to 2025 12 31.
• Implemented an intuitive forecasting approach:
o Last year baseline (same month + same day of week) plus a dynamic trend adjustment (alpha).
o Preserves structural seasonality while adapting to recent growth/decline.
o Methodology is easy to explain to the business: “last year, adjusted for recent trends.”
Next
• Extend model training and back testing to the remaining LOBs.
• Review performance and calibration with Workforce Planning leadership and refine based on their feedback.

Cihan
PCP Pricing Automation: Digital & Onboard Revenue (OBR)

Advanced Alaska ShoreEx dashboarding, and deepened Waterpark price elasticity analysis (including Celebrity).
5.1 Alaska ShoreEx
This Week / Completed
• Met with Kevin to align on objectives, data sources, and next steps for the Alaska ShoreEx initiative.
In Progress / Next
• Validate the data sources using Kevin’s EDA notebook to ensure quality and coverage.
• Build a Databricks dashboard based on that EDA work to surface Alaska ShoreEx performance and opportunity insights.

5.2 OBR Waterpark PRE
This Week / Completed
• Scope expansion: Included Celebrity waterpark bookings in the PRE model.
• Adjusted logic to group by product_pair instead of product_code to account for structural differences between Celebrity and Royal products.
• Investigated cases where bookings appeared to exceed the 1,760 capacity; identified root causes:
o Duplicate records in the source table.
o Join logic issue when attaching total forecasted pax for a tour date from the feature store table.
• Generated elasticity model plots to understand the price–revenue relationship and inform pricing strategies.
Next
• Review elasticity insights with OBR and Pricing stakeholders and propose pricing tests for upcoming sailings.

Cihan
Digital Royal One Community – Guest Services Chatbot
This Week / Completed
• Investigated and resolved Databricks job failures for the chatbot topic table, traced to an out of memory (OOM) error.
• Optimized the code to reduce memory usage, deployed the fix to production, and kept stakeholders informed throughout the incident.
• Met with stakeholders to present the escalation type logic; agreed to surface new escalation types on the main Power BI dashboard for Guest Services Chat.
Next
• Stakeholders will analyze the sample dataset provided to identify patterns and propose rules for classifying escalation types; we will iterate and then automate that logic.

Kevin

PCP Automation: Hybris Writeback

HUGE concern: Attempted testing of mass promotion tool to preview environment. Payload is not reaching hybris, because digital teams have not enabled the feature. We were told all work was completed approved and released so we were working directly with the onboard product teams on testing. We have scheduled a follow up meeting with Yassine, Viktor, David Buiatti, and Harrison tomorrow to discuss.

Kevin

PCP Pricing Automation: RBC

RBC: Released initial RBC TAP project with baseline promo recommendations. Next step is to provide more granular recommendations and automate CRF.

Henry

Contact Center: ConversationalAI & IVR

**Accomplishments Last 7 days? (Accomplishment + Impact)**

Please include project and business impact

**SpeechIQ**** to Cresta Transition**

Scraped Cresta front-end for blocks and behaviors to identify gaps and align systems.

Initiated data validation process to ensure all use cases are included for transition.

Impact: Supports seamless migration from SpeechIQ to Cresta, improving agent guidance and operational consistency.

**Cresta New Hire Pilot**

Implemented a logarithmic model to estimate learning-rate improvements for new hires, showing positive alignment with expectations.

Reviewed dashboards and pilot results with stakeholders.

Impact: Accelerates onboarding efficiency and reduces Hold + ACW times, improving overall agent productivity.

**Cresta Full Rollout & Optimization**

Defined KPIs for Phase 2 and advanced call skill mapping for Phase 3.

Collaborated with Cresta to identify tailored hints/behaviors for Sales departments.

Impact: Enhances agent performance and optimizes customer interactions across multiple phases.

**Conversational IVR**

Monitored existing IVR solution, noting a significant increase in automation rates due to seasonality.

Supported Guest Profile API deployment and troubleshooting.

Impact: Improves call routing efficiency and enhances customer experience.

**Copilot Migration & Reporting**

Supported testing team with creation of test cases for migration.

Developed best practice guide for bot building and tagging to enable accurate reporting.

Impact: Lays foundation for robust voice agent performance reporting and operational insights.

**Generative AI FAQs**

Continued prototyping for six approved topics (App, Wi-Fi, Dining, Luggage, Ground Transportation, Beverages).

Extended use cases with common questions extracted from Cresta and refined filters in vector database.

Impact: Reduces call volume by enabling voice-based self-service for common inquiries.

**Guest Profile API Integration**

Secured initial approvals from IT and business; awaiting production readiness.

Impact: Enables personalized guest experiences and improves data availability for agents.

**Leadership & Operational Support**

Built senior leadership presentation on Contact Center and project status.

Partnered with IT on disaster recovery planning and coordinated Phase 1 training approach.

Impact: Strengthens operational resilience and ensures leadership visibility on progress.

Henry

Contact Center: ConversationalAI & IVR

**What is currently being worked? (Task + Expected Impact)**

Please list projects and expected outcomes

**SpeechIQ**** to Cresta Transition**

Presenting data gaps to QA team and driving ingestion of data for parity between systems.

**Cresta Rollout & Optimization**

Monitoring New Hire Pilot and reviewing KPIs for Phase 1 and Phase 2.

Pulling Phase 1 data for initial analysis to validate rollout methodology.

Advancing optimization by leveraging SpeechIQ insights for new Cresta behaviors.

**Copilot Reporting & Migration**

Pulling data for Copilot agent reporting and Cresta agent reporting.

Continuing support for migration testing and refining reporting structure.

Impact: Enables accurate performance tracking and actionable insights for voice agents.

**Guest Profile API Integration**

Preparing for production testing and Data Warehouse build once API is live.

**Generative AI FAQs**

Continuing prototyping and expanding use cases for voice-based self-service.

**Research & Insights**

Identifying call deflection opportunities through insights for other business units.

Investigating SMS use cases and efficiencies across FAQs, app, and policies.

**Operational Support**

Developing combined project plan for Cresta production rollout.

Managing leadership-level presentations and supporting 360Learning implementation for training accuracy.

Doug

CEL Revenue Management

Progress in PRE common price upload. Celebrity archive and output histories moved to common output schema. Processing of analyst pause file improved. Cleanup of unused ADLS and Oracle storage begun.
2. Continued monitoring of Celebrity All-in Perks test. Upgraded monitoring tools to include full sequential A/B analysis to determine early stopping for grouped products.
3. Examining requested berthing upgrade for RCI Icon-class ships when berthing into neighborhood cabins.

**RCG | PRE Common Core Price Upload Facility**

Met with Monica and Eduardo from Celebrity Revenue Strategy to align on common PRE strategy and priorities. Also completed PRs 6319 and 6320, creating the pre_common_output schema, moving archive and output history tables, validating structures and row counts, and notifying the business of the updates.

Doug

RCI Revenue Management

**RCI | Data Driven Berthing Optimization – JAN**

Met with the strategy team to review an occupancy/mandatory occupancy issue raised by the Icon team that was not originally in scope. Discussed approach and are evaluating solution options, with a proposed delivery target by the end of January.

Michelle

CEL Revenue Management

**Ad Hoc | ****Gty****-Lead 2.0 Updates**

CEL team requested expanding predictions to include minor metas such as Bermuda, Canals, and Repos. Tested including them in the model and validated the outputs. Further improvements were made to model such as creating dynamic upper bounds for each sailing based on observed gaps and custom mappings for areas of data sparsity. Awaiting final business approval before pushing changes to production.

**Category-Gapping 3.0**

Developing a generalized model class to improve code reusability and traceability. This framework supports training multiple models in parallel at different levels of granularity, and allows flexible use of varying data segments and feature sets as needed. Since we are in the exploration phase of this project, this will make testing more efficient and a cleaner process.
- Refactoring the ETL notebooks to incorporate editable widgets, enabling dynamic data pulls across different brands and grouping levels as needed. This removes reliance on hard-coded parameters and significantly improves flexibility, maintainability, and long-term scalability of the pipeline. This rewrite is a critical step toward creating a more robust, adaptable, and future-proof ETL framework.

**GTY-LEAD 2.0**

Met with Aagam throughout the week to handoff Gty-Lead projects. Created documentation outlining all pipelines in production, notebook and dataset locations, as well as the logic going into the work. This includes bi-branded business rules, model decisions, and optimization formulas. The file covers dashboarding, output validations, and the DART process that adjusts predictions as needed. Illustrated possible future errors and questions from the business that might come up to be best prepared to take over project.

Lamis

RCI Revenue Management

**RCI - Pricing Optimization JAN – Validation adj to DART**

Results are communicated with Nick and the team early this week and we are proceeding with pushing to production. This could substantially improve the quality of pricing recommendations over the coming months

**Apply required Adjustments to PRE 4.0 + QA + Push to ****Prd**

Understanding the Architecture of the current PRE and listing the required changes necessary to integrate the optimization logic. In addition, to adding the logic for comparing and deciding between PRE4.0 vs Optimal recs. (mainly for null optimal results due to missing data). The following blocks highlighted in yellow are the proposed changes that will require the least amount of changes to the rest of the processes downstream.

See image

Finalized the reporting notebooks and the mlflow logging of visuals after both the optimization run and prepared another notebook to be scheduled to run after RM team upload their prices for monitoring purposes.

Currently working on making the necessary changes to PRE and running in dev then planning to test in QA tomorrow and push to prd next week.

**Lamis**

**CEL Revenue Management**

**CEL | Project Kickoff + Optimization**

Met this week with Monica and Eduardo, presented the results from last week’s run of the optimization on RCI data and discussed the technical aspects of the model in addition to the constraints.

Changes between the two brands that will need to be reflected in the code and have been identified so far include:

Change from occupancy level decision-making to cat_class level

Integrate the DART methodology being developed by Lekha (exponential moving average-based strategy).

The current o/p schema from CEL PRE does not have all features required by the elasticity model to run and generate predictions. Because in the optimization we’re using this as an i/p and since we’re calling model.predict() all required features must be present. This change is required. For the time being, I coordinated with Lekha to generate a temporary comprehensive df in dev for me to use during the development phase.

**Update Codebase to reflect CEL requirements + run the initial version of the optimization**

Currently working on the required code changes and integrating CEL’s DART methodology

Jesse

SSC Revenue Management

**RCG | Universal AB Framework**

This week, I handed off primary responsibility of Universal A/B Framework to Data Science team. In doing so, I met extensively with Data Science team to ensure that they understood the code and that they could assimilate new modules (e.g., Gecko) into the coding framework. To this end, I created a readme file that serves as a manual for UABF’s code structure, as well as its use. This manual explains how to initialize the YAML file, which controls UABF test parameters. I also communicated concept of UABF to Silversea stakeholders and management and coordinated its placement in a production-level repository, to ensure seamless updates to the code by the data science team at large.

Also met with Claire and Jill to align on future strategy. We will prioritize both All-Included AB Testing and Optimization of Top Suite Pricing for 2026. Suite Pricing for Premium Suites is problematic as we are potentially losing 40% on revenue through upgrades, where guests have learned they can pay a lot less for premium cabins through upgrades.

Ignacio

PCP Pricing Automation

**OBR | Hybris | test v1 automated promos w/ OBR team in production with preview mode**
The test of v1 of automated promos in production (preview mode) has carried over from December due to write/delete table accessibility issues. Now that this has been fixed, the OBR team will prepare a new batch of promos to upload in preview mode. When it was tested, it was realized that it was not yet enabled and a meeting is scheduled with the product team to address this.

**OBR | Automated Promos | make copy of ****promo_price_upload**** in my workspace for proper production level access**
• A copy of the promo_price_upload table (created by DE) was created in my own workspace in order for me to be the new owner of it. We discovered that this was necessary in order for the production level process of automated promo uploads to work properly; the DS service principal had accessibility issues to the DE table schema for writing/deleting. Therefore, this change was made to have the process ready for production level use.

**OBR | Waterpark PRE | help Cihan and fixing optimization results for waterpark**
I dove into the code used for the model training and optimization to try finding the root issue of the optimization results always reaching the max capacity. The elasticity model data used for training was revised with a second version; instead of including ALL new bookings (whether or not they were later cancelled or not), the data was filtered to focus on count of new retained bookings. Along with this change in the model, a quantile regression model was also created to try forecasting the upper limit of max capacity of bookings based on 2 main variables: seasonality and count of forecasted pax. This was then also implemented as a constraint to the capacity in the optimization routine.

After these changes, however, the optimization results still were not improved. This is when I believed the issue had to be more in the data being used. It was identified that a bit of extra filtering was needed in order to get the proper count of bookings (some examples were having an incorrect higher number of bookings than the count of actual bookings). This change was shared with Cihan for him to explore the required changes to be made in both the model training & optimization notebooks. He fixed the data and the optimization still consistently reached the max price constraint for the recommendations. I encouraged him to try switching to target encoding the categorical features instead of the simplified and cleaner one hot encodings. This can help improve the model for better elasticity values.

Aagam

CEL Revenue management

**DUAL | GTY-Lead 2.0 Handoff and Maintenance**

This week I focused on the remaining parts of the model ie the optimization and business rules and understood the remaining parts of the cat-gapping.

**CEL | MTRB 2.0 | Cat PROD preparation**

Pending alignment with Kevin

**PRE | PRE - Logic Analysis**

Following up from the previous meeting, this week I evaluated how CEL PRE’s price changes would differ if we used the RCI methodology. Since CEL PRE currently does not use y_pred to calculate price changes, I first checked how closely y_pred (the elasticity model output) matches the observed CEL track. I will then use y_pred to compute price changes for this week’s PRE and compared those results with the current method. This comparison will help guide making the PRE more bi-branded.

Aagam

RCI Revenue management

**RCI | PRE | Dynamic PRE Caps JAN**

This week I focused on calculating the track performance, incorporate the kids sail free calendar to the process, I will further work on pulling in the quad floor data and incorporate business rules to finalize the deliverable.

Lekha

CEL Revenue Management

**CEL | DART | Integration JAN**

Integrated DART into the elasticity model, backtested it, and prepared a deck with backtest metrics and sailing-level actual vs. forecast graphs presented to Kevin for go-ahead.

Manager requested additional validation because the metrics appeared unexpectedly strong.

Performed a joint code review with the manager and found no evidence of target leakage.

Next steps: run row-level validation re-apply DART to the output table, verify past residuals are computed and applied correctly, and confirm current-week actuals are not used anywhere before presenting to the Strat team.

Kartik

PCP Pricing Automation

**RCI | OBR | Royal Beach Club Jan**

**Web scraping Issue**

Figured out the issues in the code that was failing for the web scraping live data.

Put in a fix buy figuring out how to install drivers into the cluster and revamping the code

**AB TESTING**

Spent time going through Jesse’s automation code and Ignacio’s automation code to find an easier way to integrate them

Evan

Finalized SPI Scoring model and pipeline updates.

Got approval from both RCI and CEL on moving to factor model.

Started with data ETL for SPI Factor model.

Helped and guided on A/B framework and refactored code.

Presented model updates to team and completed a presentation around SPI.

Built / worked on front end and data ingestion.

**Model moved to QA pipeline (Ticket 5089):**
Work is complete and the model is now fully transitioned to the QA pipeline. A final close-out comment is recorded in Jira.

**Scoring implementation:**
The current scoring scope is complete. While additional iterations are expected later, this phase is finalized and ready for close-out documentation.
