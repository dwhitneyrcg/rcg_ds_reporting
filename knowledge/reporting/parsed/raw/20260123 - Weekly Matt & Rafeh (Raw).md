Mert
MIAP
Completed the Bronze/Silver ETL pipeline for shipboard alarms and events, where nearly 500K alarms/events per ship are now being synced to the Alpha platform.
Developed and fully productionized the Alarms and Events GUI in the MIAP App, enabling users to export data, filter, and send content to the Alarms and Events AI Agent for further analysis.
Deployed several Databricks function tools for agent-driven analysis of alarms and events, returning summary tables based on user query inputs. Also developed a Genie Agent to enable custom SQL queries on the Alarms and Events database.
Developed a custom AI Agent on the MIAP API using FastAPI/LangChain/LangGraph with tool-calling capabilities to Databricks, including the ability to delegate and supervise the Databricks Genie Agent for custom SQL query creation.
Integrated the AI Agent into the MIAP App and the Alarms and Events SubApp to provide interactive agent capabilities. This project aims to address shipboard alarm fatigue.
Met with Jan Solum and Carlos De Sedas to discuss tool usage. Lloyd’s Register will collaborate with Royal Caribbean to identify unnecessary shipboard alarms to reduce alarm fatigue. The MIAP team will work jointly with Lloyd’s Register on this effort.
Demo of Alarms and Events solution: 
https://rccl.sharepoint.com/:v:/s/EnergyManagement/IQDNy5V8gJjqTap37Sjcs-I9AfWePPAO9zh2qIuRQ6aawGQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=wamoQ6
Reviewed résumés for the Sr. ML Engineer backfill.
Met with the Decarb team and presented Digital Twin model progress; received positive feedback.
Met with the American Bureau of Shipping (ABS) with Jan Solum regarding the Safety KPIs project. ABS’s solution demo was not satisfactory; agreed with Jan to explore internal solutions instead.
Discussed a potential fleet-wide reliability AI project with Mike Tepel.

Will

MIAP
Fixed the ratio heat-power bug in the LNG Optimizer.
Created new overall MGO-equivalent SFOC models for 7 ships.
Identified issues in 3 additional ships.
Created improved individual and overall models for QN using MFM data.
Working on integrating the LNG Optimizer into the Digital Twin API.

Brendan
MIAP
Attended the initial demo of the Fuel Forecast API with the GMO team and discussed feedback and next steps.
Followed up with the GMO team on correcting missing Drydock/Hull coating entries.

Reza
MIAP

Working on the fuel-forecast Digital Twin model to resolve ship-specific issues, including:
Added logic to address negative intercepts/infeasible optimizer constraints in STG models within the Digital Twin API.
Enforced loading of scrubber reference ship data and handled empty scrubber datasets within the Digital Twin API.
Adjusted training dates for ship AD in service power.
Forced use of FAT SFOC models and ensured correct model usage in the optimizer when power plant models are unavailable.
Debugged the Ovation ship issue and resolved the error in the HVAC workflow.

Ram
MIAP

This week:
Worked on Wärtsilä issues, resolved them, and awaiting confirmation.
Worked on the Stream shipboard table and coordinated with the MEMS team to understand the issues they are facing.
Progressed on Sea Events, VPS, DNV, and Lloyd migrations.
Made progress on Modbus data.
Advanced Cococay API data collection.
Next week:
Meet with MEMS to present results of data collection and analysis.
Verify that the Modbus load code works across all sources.
Gather additional information for Cococay and continue development.
Fix the Silver analytics task in the MIAP ETL.

Mahshad
MIAP
Performed deviation analysis for WN AHUs.
Investigated low COP issues for VY-class chillers.
Analyzed ML and CS TCV sensor faults.
Scheduled a meeting with Engineering to discuss VY-class chiller low-COP performance.
Built an LLM- and agent-based notebook to detect anomalies in ship systems.
Resolved data issues in the Digital Twin library related to FACTS datasets.

Arya

MIAP
Built a POC of the ship tracker, now tracking 13 ships live.
Deployed the tool on dev; functionality is stable.
Added a slider to show a 24-hour path and replay system.
Tuned SFOC models.
Created Confluence documentation on using Azure AI models.
Restructured Safety Analytics and redeployed it to the MIAP App.
Fixed minor bugs in the GMO App.

Glen-Erik

PROPEL

Offer Templates:

Created ability to add custom images to each offering

Scaled image process: Refactored code so images are downloaded and converted once per offer bank rather than once per offer (64 images downloaded instead of 1,000-2,000 downloads). Also cut size from10-60mb per image to 100-400kb establishing image size standards.

Generalized new offer template so it can now run for all categories in dev.

Investigating offer assignment issue that is causing linear programming model to sometimes fail to find a feasible solution for assignments and fallback on quota based logic.

Investigating over-assignment of makeover offer within the retail category

Next steps:

Offer templates:

Create custom layout logic in offers since the text and layout isn't correct for most categories except shorex.

Get missing images for some offerings.

Eswar & Glen-Erik

Revenue Management

Data Validation Framework:

Integrated to TRACK-CEL RMA project related workflows

AB Testing:

Discussed the strategy to deploy framework in RMA, so that it can be leveraged by all other RMA, Data science projects.

Packaging project as whl file to catalog and automating CI/CD to deploy as whl file to catalog

Re-deployed ssc feature store generate workflow by adding currency exchange functionality

Reviewing and monitoring PR's. CI/CD

Providing MLOps support in bypassing issues, enabling developers by providing guidance and productionizing workflows. production system that was preventing data from being sent properly for project RCI

ADF prod deployment pipelines broke and all the workflows went into pause, which results in no pipeline getting triggered. Fixed this issue by investigating the root cause and made sure all prd workflow triggers are unpaused. **This was a critical fix and should be ****highlight**** as an accomplishment.**

Javier

Revenue Management

Automated Code Review

Created dashboard view of total repo health for violations of time

RMA: refactored FeatureStore Databricks Asset Bundles to comply with ACR rules.

Glen-ERik

JD AI Tool:

Met with HR and identified better user groups like Brandon Schassberger's team.

Requested Data Engineering to start using the tool and provide any feedback. And assist with establishing the standards in the standards document.

Connected with Austin (recruiter) on testing the tool since recruiters need to create JDs (or know who needs to create them) more often than any specific Hiring Manager.

Ayon Ghosh

**WOW Updates Summary**

**1) Charter & Grooves Voyages Integration Across Fleet**

Completed development of the codebase to incorporate **Charter** (General & Grooves [i.e. non-kids]) voyages into the fleet-wide datasets.

**Testing is in progress**, focusing on validating edge cases and ensuring alignment across all voyage data sources.

**2) Ice Cream Variant Expansion (150 Variants Fleetwide)**

Built a new module to ingest and standardize all **150 ice****-cream product variants** across the fleet.

**Unit testing ****fully**** completed**.

**Integration testing next**, to validate compatibility with downstream forecasting and reporting components.

**3) ****Interport**** / ****Interport**** Master Forecasting Pipelines**

Actively developing **five new pipelines** to bring Interport and Interport Master data into the forecasting ecosystem.

**ETL development is complete**, including extraction, cleaning, validation, and load workflows.

Work has now progressed to the **feature engineering stage**, where predictive variables and transformations are being built for model readiness.

Ben & Camilla

Supply Chain (IBP)

Stakeholder Engagement & Pilot Rollout
• Beyond Pilot Approval: Presented the "Beyond" Pilot strategy to Laura Hodges, securing enthusiastic support to proceed. The roadmap targets a start date next month with a full fleetwide rollout by September. A follow-up session with operations leaders is scheduled for next week to finalize rollout details.

Ben & Camilla

Supply Chain (IBP)
• Operations Alignment: Conducted a successful review with Celebrity F&B operations leaders (Jan Sorensen, VP F&B Ops; Sidney Semedo, Sr. Director Culinary Ops). They are fully supportive of the pilot. We identified specific business nuances—such as cash purchases in ports and FIFO-based consumption—which will require minor logic modifications but are not blockers to progress.

Ben & Camilla

Supply Chain (IBP)

Model Enhancements & Strategic Analysis
• Seasonality Correction (Turkey Product Analysis): Addressed an over-forecasting issue in RCI/CCI H&B seasonal products where forecasts were inflated during non-holiday months (Jan–Oct).
o Analysis revealed that recent consumption trends (last 13 weeks) were aggressively driving forecasts.
o Created an executive presentation and identified 342 products with significant demand misalignment (seasonality ratio > 1.3).
o Implemented "Same Time Last Year" (STLY) guardrails for highly seasonal products. This logic constrains the forecast using passenger-adjusted historical data (bounded 0.5–2.0) to prevent over-ordering in off-peak months.

Ben & Camilla

Supply Chain (IBP)
• Min/Max Par & Volatility: The Min and Max Par logic was reviewed and accepted by Brenda and the team. Additionally, we created a volatility report to track high-variance items. Research is currently pending on a secure method to distribute these reports via email.
• SSC Uniforms: The base model is complete. We are currently reviewing the max date regarding crew data.

Tooling & Data Engineering
• Streamlit Application: Completed Version 1 of the IBP team application, enabling secure SharePoint file management. Features include user login/authentication, SharePoint connection via client credentials, and session management. Version 2 is pending.
• Finance Tool Updates: Added a column for "Average Voyage Consumption from Last 3 Completed Voyages." Based on recent feedback from Sidney, pending work remains to refine this logic to consider a 21-day window for voyage counts.
• Inflation Reports: The dynamic current/last/next year logic is functioning correctly for RCI/CCI (showing row counts). For SSC, the logic works, but row counts are not displaying; further review is pending.
• Consolidated Spend Table: Currently engineering a more accurate solution by joining two distinct source files, as the single SharePoint file lacked necessary columns for integration with demand forecasts.
• Pending:
o Addition of timestamp dates to order creation and min/max par tables.
o Agentic AI enhancements for Uniform, Medical, and CocoCay streams.

Cihan

PCP Automation (OBR)

Alaska ShoreEx (Completed & In Progress)
• Data Validation: Conducted comprehensive validation to ensure the accuracy of data flows feeding the ShoreEx dashboards.
• Strategic Analysis: Developed and shared a detailed insights deck with Alexx Correa based on the Alaska ShoreEx EDA. Key insights included booking analysis by brand/type, historical performance evaluation, booking timelines, sailing performance tracking, and single-product analysis.

Cihan

PCP Automation (OBR)

OBR Waterpark PRE (Completed & In Progress)
• Predictive Modeling: Trained the predictive model utilizing target encoding for meta-products.
• Explainability: Generated and saved SHAP (SHapley Additive exPlanations) value plots in MLflow to ensure model transparency.
• Optimization: Experimented with feature transformation techniques and retrained the elasticity model to drive accuracy improvements.
• Stakeholder Management: Provided status updates to relevant stakeholders on progress.

Cihan

Digital RoyalOne: Guest Services Chatbot (Pending)
• Escalation Analysis: Stakeholders are currently analyzing the provided sample dataset to identify escalation patterns. Once completed, they will share findings to help us refine the chatbot’s escalation detection logic.

Caleb

Customer Lifetime Value (CLV)

Strategic Re-alignment
• Demand Modeling Strategy: Met with Lissette (Revenue Planning) to align our demand modeling approach.
o It was noted that Revenue Planning models have predicted actual revenue within ~1% accuracy over the past year.
o Decision: We will incorporate their models for baseline demand sizing rather than building redundant versions. Our AI focus will shift to estimating "latent demand," utilizing features such as spill/overflow, call center abandonment, social media impressions, and brand equity.
o Action: Drafting data acquisition requests to Consumer Insights, Marketing, and E-commerce to support this new scope.

Data Validations & Analysis
• 2025 Table Refresh: Currently completing full validations for the 2025 CLV Table refresh, documenting the lineage from EPM -> BIMA -> VCAP -> VCAP Stg2 -> CLV Analytics -> Shareable tables.
• Agency Data: Updating the clv_agency table with the refreshed 2025 data, specifically exploding the table to include agent_id and rep_agent_id as required by Trade.
• Market Analysis (NY Fly/Drive): Delivered analysis to Alex F regarding NY fly vs. drive guests. Validated that while drive-in guests have lower initial performance than fly-in guests, they demonstrate strong retention and subsequent performance, representing a key value-seeking segment.

Carlos

E-Commerce

Completed
• Dashboard Features: Began development of the "Consumer Booking Status" feature in the Streamlit dashboard and updated the predicted scoring table to aggregate by booking status and market.
• Bug Fixes & Visibility: Fixed errors on the "Model Insights" tab that were blocking feature visibility.
• Reporting: Applied booking status aggregation to consumer segmentation tables. Presented the second version of the "Booking Propensity Change Drivers" report (focused on targeted offers) and added a "Sailing Propensity" training report to the dashboard.

Pending / Next Steps
• Pipeline Troubleshooting: Working with Glen Erick to resolve failures in the Copy-to-Oracle pipeline.
• Logic Updates: Per E-Commerce team request, we are redefining "Booking Status" logic. Instead of a simple 7-day lookback, we will utilize the status column combined with the sailing date from prd_silver.rcimkt.v_all_brand_sailings.
• New Data Ingestion: Investigating the ingestion of clickstream and call data for future modeling.

Mirielle

Contact Center & Workforce Planning

Operational Stability (LP_OFTOCX)
• Incident Resolution: The OFTOCX workflow experienced failures writing to SFTP over the past two days.
• Action Taken: Released a temporary pipeline at 07:00 PM to ensure business continuity while troubleshooting the main workflow.

Workforce Planning – North America
• Forecasting Models: Successfully trained, tested, and back-tested call volume forecast models for 12 LOBs, specifically completing work for CE_SALES, CASINO_SALES, and CASINO_SERVICES.
o Training Data: Jan 2023 – Oct 2025 (80/20 split).
o Back-testing Window: Oct 31, 2025 – Dec 31, 2025.

Celebrity Scope Definition
• Scope Clarification: Ongoing discussions with Heny and Alper to define deliverables for Celebrity Call Volume Forecasting.
o Confirmed that the App Design is a distinct end-to-end project.
o Datasets must be built to support LOB mapping and office hours computation.
o Forecasting must be executed per LOB (no one-size-fits-all approach), and FTE modeling requires refinement based on specific LOB requirements.

Erick

**Project Axiom**

*AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.*

**Meta Data Extraction**

**Venue Dictionary** *(Gourish P.)*: LLM-based venue classification. Processing all ships and generating JSON output for team review.

**LLM Utils Framework** *(David M., Erick **A.)*: Completed walkthrough of centralized utils framework with Spark-based parallel processing of async API calls. This framework will be adopted to all LLM projects.

**Reporting**

**ShoreX**** Safety** *(**Danusio** G., Rodrigo B.)*: Delivered LLM-labeled safety issues from shore excursion feedback. Stakeholder provided change requests; awaiting official Safety guidelines to improve labeling.

**Celebrity Consumer Insights** *(Erick A.)*: Delivered Reflection "Quiet Spaces" analysis and Xcel venue sentiment research (The Bazaar, The Club, Pool Club, mattresses). Scraped 100+ CruiseCritic forum discussions for supporting evidence.

**Modeling**

**NPS Drivers Model** *(Osvaldo V.)*: Deployed Databricks endpoint using FastTreeSHAP + LightGBM. Response time improved from 40-60s to ~10s. Next: expand filtering (demographics, ports) and begin Axiom webapp integration.

**Guest Logs Classifier** *(David M.)*: Fixed classifier issues per Alessio's feedback. Considering dictionary mapping approach for simplified roll-up. Awaiting stakeholder feedback.

**Project AI Pivot *****(Qualtrics Topic Extraction)***

*Self-labeling framework for automatic topic discovery from survey data.*

**Rodrigo B.**: Reduced Brand Tracker topics from ~100 to 14 using sampling optimization. Phase 1 deliverable defined: Excel with topic counts, sentiment averages, AI summaries.

**Danusio**** G.**: Delivered interactive explainability plot for Brand Tracker. Consolidation meeting finalized 3-step process (discovery → classification → aggregation).

**Architecture**: Two entry points defined (Databricks workflows, Axiom/Teams upload). Target users: Consumer Insights, Contact Center.

Cristian

**PCP**** ****MyCruise**** Recommender**

*Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app.*

**A/B Testing *****(Cristian V.)***

Tested Bonferroni-Holm method; confirmed similar results to Benjamini-Hochberg. Resolved Postgres auth issue. Successfully pulled staging offerings data via GraphQL.

**Blockers:** PDP experiments blocked on engineer availability. Proposed pixel tracker to identify users who viewed recommendations.

Henry

Contact Center: Cresta Pilot & Rollout Preparation
Reviewed New Hire Cresta dashboards for multiple service use cases to confirm readiness and data reliability for frontline monitoring.
Finalized Phase 2 KPIs with the business for both brands, ensuring alignment on success measurement for the full rollout.
Completed Phase 3 call-skill mappings for one brand and initiated Phase 4 mappings, supporting scaled deployment.
Drove user access and IT preparation for the Phase 1 go-live, including all required application access submissions.
Worked with Telecom to secure VDNs needed for Phase 1 and 2, enabling accurate routing and data capture.
Continued refinement of hints and behaviors using speech analytics and intent analysis to enhance agent guidance and improve sales effectiveness.

Henry

Contact Center: Cresta Optimization & Discovery
Analyzed speech data to identify frequent intent clusters and translated them into recommended new behaviors to drive coaching and sales quality improvements.
Participated in discovery workshops to guide governance and set rollout priorities for long-term Cresta adoption.

Henry

Contact Center: SpeechIQ to Cresta Transition
Provided updated topic lists to support transition mapping.
Coordinated ingestion requests for updated Copilot data to ensure continuity of analytics.

Henry

Contact Center: Conversational IVR & API Integrations
Advanced Post-Migration modules, securing cross-functional support to maintain delivery momentum.
Achieved connectivity between Guest Profile API and analytic environments, an important step in enabling deeper personalization insights.
Tracked API deployment and troubleshooting to keep the integration timeline on target.

Henry

Contact Center: Other
GenAI FAQ Prototyping
Continued prototyping approved FAQ topics and tested against common questions extracted from call transcripts, supporting future automation and deflection strategies.
Research & Automation Efficiencies
Investigated SMS use cases, friction points, and automation opportunities across self-service channels to support deflection and digital adoption strategies.
Operational Planning & Workforce Support
Supported workforce planning and staffing modeling for brand operations.
Submitted combined project plans, issue analysis, and operational roll-out needs for Cresta production readiness.
Onboarding:
Prepared onboarding materials and onboarded two new Manila hires, ensuring continuity and team readiness.
Cresta Workshop Participation:
Participated in the Cresta AI Analyst workshop to deepen internal expertise and support autonomous optimization.

Henry

Contact Center: What is currently being worked? (Task + Expected Impact)
New Hire Pilot Monitoring: Ensuring accuracy of metrics and identifying early performance trends to refine training and support.
Cresta Rollout Execution: Supporting Phase 1–4 rollout activities across configuration, user management, issue tracking, and call-skill mapping. Pulling and analyzing Phase 1 data to validate methodology and prepare insights for operational leadership. Continuing joint optimization with Cresta to refine hints and behaviors that improve agent performance and sales outcomes.

SpeechIQ → Cresta Data Transition: Ingesting updated Cresta data and coordinating ETL efforts to enable dashboarding and analytics continuity.
Digitization KPI Definition (Your addition): Building the initial KPI framework to support executive reporting and quantify digital deflection and self-service adoption.
GTS Automation Opportunities (Your addition): Identifying automation use cases that can reduce manual workload within Guest Services, improving efficiency and turnaround time.
Conversational IVR Enhancements: Continuing backlog development, supporting migration efforts, and validating API integrations.
Guest Profile API Data Warehouse Exploration: Evaluating creation of a structured data repository of API responses for enhanced contact-level personalization and performance measurement.
GenAI FAQ Development: Preparing demo sessions and iterating prototypes for upcoming leadership reviews.
Research & Journey Optimization: Continuing evaluation of SMS use cases, friction reduction, and automation opportunities across digital channels.

Jesse

Silversea (SSC) PRE

This week, I updated PRE to make price recommendations for all Silver Sea currencies. Expanding this PRE capability required the following:

coordinating with Data Engineering to access reliable currency exchange data

constructing a feature store table to track evolving currency exchange rates over time

inserting a code block into PRE that converts price recommendations from USD to other SSC currencies

ensuring PRE is still compliant with SSC Reservation System

Ensuring PRE can recommend prices across international currencies is an important step in ensuring its full adoption and integration by the SSC brand. It is also important for our upcoming ab test on upper-level suites, as SSC clients may pay for their suite in a foreign currency.

*Status:* Completed on 01/22/26

*Deliverables:*

PRE gives price recommendations in five currencies, rather than only USD

currency exchange rate time series tracks currency exchange rates in feature stores

PRE (initially) passes Reservation System validation for all five currencies

*Delays:* No

*Future Issues:* Update stakeholders as necessary

**SSC PRE | Compute PRE Metrics (In Progress)**

Beginning an EDA on PRE success and use metrics

Jsse

Silversea (SSC) PRE

**RCG | Universal AB Framework — Feedback & Rollout (Done)**

*1/12/2026* — Met with data science team to demonstrate my deliverable on UABF and assist them in assimilating the Gecko Module to UABF. Data Science Team asserts that they have all necessary outputs for this task.

*1/12/2026* — Coordinated with Data Science and platform teams to create a Databricks repository for UABF. Repository will serve as the chief instrument for updates. I also handed off the primary responsibilities of updating UABF code to Data Science Team (other members).

*1/13/2026* — Met with Data Science management and created a PowerPoint to communicate UABF progress to SSC stakeholders.

*1/22/2026* — Met with Data Science team to discuss continued rollout efforts for the universal AB framework. Data Science team and lead data scientist are refactoring my code to make it less “bulky.”

*Status:* Completed on 01/22/26

*Deliverables:* Good communication across the data science team regarding UAB Framework; clear understanding of team roles and responsibilities

*Delays:* No

*Future Issues:* Update stakeholders as necessary

**• SSC PRE | Upper****-level Suites — Stakeholder Feedback (To Do)**

*1/13/2026* — Data Science team met with SSC stakeholders to discuss upcoming projects. SSC stakeholders indicated that upper-level suite pricing is a top priority.

Doug

RCI Revenue Management

**PRE Common Output & Price Upload Improvements**

Completed PRs **6319** and **6320**, establishing the **pre_common_output** schema, migrating archive and output history tables, validating structures and row counts, and notifying the business of the updates.

Completed PRs **6299** and **6331**, updating pause file selection, removing ADLS archive writes, appending archive and output to new common histories, and eliminating Oracle copy-back processes.

Completed PR **6392**, removing old pause files, eliminating Oracle dependencies, and fully enabling Databricks-based price upload.

Completed PR **6361**, removing Oracle pipeline steps and shifting Celebrity price uploads fully to Unity Catalog.

Doug

RCI Revenue Management

**RCI | KPI Analysis, Modeling & Automation – Q1**

Added berthing metrics to replenishment analysis to test for possible revenue impact, including reductions in involuntary upgrades and wasted berths after 2024 automation.

Doug

RCI Revenue Management

**RCG | PRE Common Core Price Upload Facility**

Validated outputs from this week’s production run and began progressing with the next sequence of sub-tasks.

Doug

CEL Revenue Management

**CEL | Perks Gap Test Monitoring & Final Findings – JAN**

Analyzed interim RDSS-level results for Australia and Europe sailings; advised caution on groups with low sample sizes and identified where Bayesian and sequential methods offer more meaningful signals.

Michelle

CEL Revenue Management

**GTY****-Lead 3.0 — Code Refactoring & Training Data Updates**

**Code Refactoring (ETL notebooks):**
Refactoring the ETL notebooks to incorporate editable widgets, enabling dynamic data pulls across different brands and grouping levels as needed. This removes reliance on hard-coded parameters and significantly improves flexibility, maintainability, and long-term scalability of the pipeline. This rewrite is a critical step toward creating a more robust, adaptable, and future-proof ETL framework.

**Training Data Adjustments & Features:**
Adjusting training data to include all occupancies, tier prices, and category prices. Working with business from both brands to ensure all occupancy calculations are correct. Prices and gaps must be calculated according to mandatory occupancy, not just grouped by occupancy code.
Created a structure similar to cat-gapping where occupancy_code reflects what is **bookable**, acknowledging that the same category code can have multiple rows due to different occupancies; each occupancy row includes net availability and is grouped by what group can book the space (aligning with the DE ask).
Added features for **bundled** (promotions included; price per person as seen on the website) and **tariff** (base cost) prices; will test which signal is strongest in modeling.

**GTY****-Lead 3.0 — General Model Class & Parallel Training**

**Generalized model class (exploration → parallel training):**
Developing a generalized model class to improve code reusability and traceability. This framework supports training multiple models in parallel at different levels of granularity and allows flexible use of varying data segments and feature sets.

**What’s implemented:**

Developed a class that trains **EBM** models at multiple granularity levels, e.g.:

Brand level: single model for all data

Ship class level: models per ship class (EG, SL, ML)

Category class level: models per cabin category (A, B, C, F, O, I)

Combined levels: ship class × meta product; ship class × cat class; ship class × meta × cat class

Each model uses time-based train/test split, applies balanced class weights, computes train/test **AUC** and training time, and logs to **MLflow**.

Added **model selection** that generates candidate models from coarse→fine granularity, ranks by test AUC (higher is better) then training time (faster is better), and returns the optimal model.

The class enables rapid parallel experiments by changing features and datasets quickly.

Michelle

CEL Revenue Management

**CEL | ****Gty****-Lead 2.0 Updates**

**Minor Meta Additions (Completed):**
Expanded predictions to include minor metas (Bermuda, Canals, Repos). Validated outputs; added dynamic upper bounds per sailing (based on observed gaps) and custom mappings for sparse areas. Awaiting final business approval before production.

**DART — New Deployment (Testing | QA):**
New deployment sailings have low bookings that do not meet DART thresholds. DART is necessary because base model trainings do not catch shifting trade-up behavior quickly enough. Updating DART to capture **group****-level** trade-up performance (vs. per-sailing) to increase the percentage of adjusted sailings in new deployments.

Michelle

RCI Revenue Management

**RCI | GTY****-Lead 3.0 (Dataset)**

**Shared dataset build (Completed):**
Working with Data Engineering and business to create a dataset usable across multiple projects, ideally live and updating availability/pricing as bookings arrive. Emphasis on **mandatory occupancy** so we store not just occupancy codes, but **what each group size can truly book** with net availability.
Example implemented for *cat**-gapping* to compute bookable occupancy rows and remaining inventory accordingly. Handoff to DE scheduled; no potential issues identified.

Lamis

RCI Revenue Management

**• DART Validation & PRE Optimization Adjustments**

Communicated results with Nick and the team earlier this week and began proceeding with pushing the updated approach into production.
*(Validation + Additional adjustments to DART)*

**RCI | PRE 4.0 Integration & Optimization**

Continued work to understand and adjust the current PRE architecture to integrate optimization logic.
Added logic for comparing and choosing between PRE 4.0 and Optimal recommendations, particularly for cases with missing data that yield null optimal values.
Finalized reporting notebooks and MLflow logging for visual outputs after optimization runs.
Prepared a secondary notebook to run after RM uploads for monitoring purposes.
Currently making PRE code changes, running in dev, testing in QA next, and preparing to push to production.
*(Apply required Adjustments to PRE 4.0 + QA + Push to PRD)*

Lamis

CEL Revenue Management

**CEL | Pricing Optimization Kickoff & Requirements**

Reviewed last week’s optimization results with Monica and Eduardo.
Discussed technical aspects of the model and identified differences between the two brands that must be reflected in code updates, including:

Moving decision-making from occupancy level to **cat_class** level

Integrating the new **DART** methodology

Addressing missing feature fields in CEL PRE output schema so the elasticity model can run end-to-end
Coordinated with Lekha to produce a temporary comprehensive dataset in development until an updated schema is finalized.
*(CEL Project Kickoff + Requirements Gathering)*

**CEL | Optimization Codebase Updates**

Currently implementing the required code changes and integrating CEL’s DART methodology into the pricing optimization flow.
*(Update Codebase to reflect CEL requirements + run the initial version of the optimization)*

Evan

RCI Revenue Management

**SPI Factor Model — PAX Build Factor Modeling (Unsupervised)**

Completed methods to:

Standardize pullback

Use a clustering approach to identify the most similar curves

Split the deployment into standard chunks

Included visual diagnostics for curve similarity analysis

*(Work under DUAL | V1 | SPI Factor Model)*

Created a new method to determine the period of time from a sailing date and original deploy as a transformer

Built as a number method for speed optimization that segments periods of data relevant to query

Refactored codebase to include factor models

Began data investigation and modified queries

Built a nearest neighbors that compares builds from similar ships (on the same ship class) and returns their build %

Ensured that the query represents the relevant normalized instance (% of total pax fcst)

Can now leverage this unsupervised approach, with the output of the SPI

Started to identify what may be representative

Investigated and discussed portal development (FastAPI & Flask deployment)

Started to mimic / fork the API instance that was built

Worked on refactor to a QA branch on the A/B testing standardized framework

Started on a Unit Testing notebook

Ignacio

PCP Pricing Automation

**Universal AB Testing Framework: ****integrate Jesse' Greedy Clustering & Power Analysis functions into Class structure into compatible format**
• A few changes were done to Jesse’s code (classes & functions for Greedy Clustering & Power Analysis). The main changes were trying to avoid use of init functions, and instead, relying purely on the ABConfig data class for storing all relevant parameters. In addition, a class object was also created for creating Spark Sessions, in order to avoid those being inputs in any class/function. After making these changes, the creation of the centralized & unified parent framework class was tested. The class, for the first time, was able to be created with no errors.
• Further adjustments still want to be made to further clean the MVP version of this, but this is the first successful pass. Future improvements to be worked on now include:
• removing some of the input parameters within specific functions of the component classes (instead, just use an initialization function to initialize these parameters for the class object overall)
• meet with Jesse to patch up any confusion and clarify any parts of the code that are still not completely understood end-to-end
• create a “GreedyClusterPairing” class to contain the ab_hard_pairing & ab_soft_pairing classes as child classes within it for better overall structure to the AB testing tool

Ignacio

PCP Pricing Automation**
Maintenance on Existing OBR PREs (cabanas + beverage)**
• After talks with both Jorge & Anastasia from RCI OBR, a few checks and maintenance fixes were done for the PREs. The beverage PRE was missing recommendations since late December. After investigating, it was realized that this was due to the revenue FCST for beverage missing, therefore leading to empty outputs for the FCST-driven optimization. For cabanas, the PRE is working fine, but the base prices shown for the optimized prices seem incorrect. This was due to never having updated the source table to the newer version (provided by DE a few months ago) for correct base/system price extraction. The code was updated to correct this and the changes were pushed to QA & PRD

Ignacio & Kevin

PCP Pricing Automation

Ongoing testing of promotion writeback yesterday and today. There was some errors with the Digital Writeback pipeline that are being fixed, and team will try again. Digital is currently working to ensure that OBR Teams are able to approve all pricing/promotions changed, which is required for SOX compliance purposes.

Lekha

CEL revenue mangement

• **CEL | DART Integration — Validation checks to verify the DART logic (Done)**

*(Parent: CEL | DART | Integration JAN)*

*Status*: This ticket is complete as of *1/21/2025*

*Deliverables*:

*Initial assumption:* We initially thought applying DART would be pretty straightforward by using an exponential moving average (EMA) on residuals with a shift(1), so the current week’s actual demand is never used in smoothing.

*Validated the Current logic:* DART was implemented at the row level as a post-processing step on the prediction/elasticity output table (not during training), which keeps the approach easy to validate on row level.

*Early observations:* When residuals were calculated using the *smoothed bookings* column, the error metrics looked better; however, this was later identified as a *target leakage risk* since the smoothed demand is derived from dynamic bin logic.

*Fix for leakage:* To address this, residuals were recalculated using *actual bookings vs. base predictions*, while still enforcing shift(1) to ensure the current week’s actual demand is not used.

*Impact on results:* With the shift(1) setup, DART-adjusted predictions show a natural lag relative to actual demand, which leads to higher point-error metrics compared to the base model, even though sailing-level trends often look visually better.

*Next steps:* Given this , Rethinking alternative ways to apply DART with [~accountid:712020:13cfbba7-dcd6-4342-8763-48fb49d4ff8d] more effectively to better balance stability, and accuracy

*Potential future issue*: None

Kartik

PCP Pricing Automation

**RCI | OBR | Royal Beach Club — Web scraping fix (Done)**

*(Parent: RCI | OBR | Royal Beach Club Jan)*

Figured out the issues in the code that was failing for the web scraping live data.

Put in a fix buy figuring out how to install drivers into the cluster and revamping the code

**• RCI | OBR | Royal Beach Club — AB testing automation (Done)**

*(Parent: RCI | OBR | Royal Beach Club Jan)*

Spent time going through Jesse’s automation code and Ignacio’s automation code to find an easier way to integrate them

**• RCI | OBR | Royal Beach Club — Create aggregated CRF view (Testing | QA | 90%)**

*(Parent: RCI | OBR | Royal Beach Club Jan)*

Created a view for Royal Beach CRF for the team to automate the process

Validating the view created currently

Once validation will publish it and send it over to RBC team
