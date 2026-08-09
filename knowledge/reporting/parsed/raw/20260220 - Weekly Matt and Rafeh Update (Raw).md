Ben and Camila

IBP - SUPPLY CHAIN
Beyond Pilot -- Early Results Exceed Projections
$161,000 reduction in purchase order costs (Master Order Template) from the first two pilot sailings with no impact to NPS.
Extrapolated over 52 weeks, annualized savings on Beyond would reach $4.2M, slightly exceeding the $3.9M originally projected before the pilot launched.

Ben and Camila

IBP - SUPPLY CHAIN

Codebase Refactoring -- Performance & Maintainability
Largest notebook: Refactoring complete; validation against production tables in progress. ~4-hour reduction in compute time.
Second-largest notebook: Refactoring complete with ~3-hour compute-time reduction. Validation pending.

Ben and Camila

IBP - SUPPLY CHAIN

Medical Category Model Improvement
Continuing to iterate on demand model performance for medical categories (currently 46% MdAPE). This week's iteration did not outperform the production baseline; will continue iterating with adjusted strategies.

Ben and Camila

IBP - SUPPLY CHAIN

Royal Beach Club -- Consumption Forecasting
Exploring how to forecast future consumption using pre-cruise purchase data as a proxy for guest count, since traditional sailing-based consumption history is unavailable for new destinations.

Ben and Camila

IBP - SUPPLY CHAIN
Order Creation Pipeline -- Automated & Orchestrated
Delivered a fully orchestrated Order Creation pipeline on Databricks with purpose-built notebooks attached to a job pipeline.
Stage 1 -- CHECKPOINT_INTERMEDIATE_TABLES (System Stability & Data Preparation)
Job Concurrency Logic: Detects simultaneous Order Creation jobs (Scheduled, Purchase, or Production updates) and enforces strict priority rules based on time of day to prevent resource conflicts or data overwrites.
Maintenance Safety Check: Verifies the database is not undergoing maintenance (e.g., Vacuum operations) before processing; halts immediately if detected.
Data Checkpointing: Creates frozen snapshots of Consumption and Spend datasets, isolating reporting from live data changes and improving downstream performance.
Financial Standardization: Applies current accounting rules to historical data, mapping legacy Cost Center and GL Account codes to the modern format.
Stage 2 -- ORDER_CREATION_MASTER_NOTEBOOK (Workflow Orchestration & Scheduling)
Dynamic Scheduling: Adjusts workload by calendar cadence -- Daily (operational reports/scorecards), Weekly on Tuesdays (baseline backups), Monthly at End of Month (baseline calculations).
Tiered Execution: Manages dependencies in sequence -- Independent Variables > Baselines > Scorecards > Snapshots.
Error Handling & Logging: Tracks success/failure of every step; non-critical failures do not block the remaining pipeline.

Caleb
CORPORATE STRATEGY DEMAND MODEL
Completed:
Finalized data cleaning across all model inputs, incorporating latest iterations on cabin mix, ship-level capacity for all competitors, and internal media spend.
Defined final filters for the 21 brands and 4 segments within the model's scope.
Established region mappings using embarkation port as the primary key.
Aligned with Jordan and Gaby on the distinction between key and supplementary inputs, as well as normalization methods for feature engineering.
In Progress:
Developing an adjustment process to address data gaps and approximate competitor-level details where direct data is unavailable (e.g., leveraging RCG booking-curve fill rates and pricing by book-to-sail window, then overlaying onto competitor BOTS pricing to estimate filled capacity rates).
Continuing to refine ship-name mapping between CS's fleet model and Revenue Planning's deployment tables.
Validating deployment, capacity, and pricing figures across the full cruise industry to ensure consistency before modeling begins.

Carlos
E-COMMERCE Customer Target
Completed:
Platform modernization: Updated all marketing model notebooks to Databricks Runtime 17.3 (Scala 2.13, Spark 4.x, MLflow 3.x); migrated Pandas from fast-parquet to Arrow by default; migrated storage from dbfs://filestore to ADLS volumes.
Manual regression testing: Completed validation of refactoring changes, resolving try_cast to cast migration, syntax errors, and other compatibility fixes.
Epsilon feature ingestion: Delivered initial implementation for ingesting new Epsilon columns as features, incorporating data back to January 22. For 3-month models, earliest usable data begins in April, ensuring proper alignment and preventing data leakage.
Epsilon data integration: Fixed casting errors and adjusted union logic to allow newest Epsilon data to be appended to existing history.
Ranking feature scaling: Completed scaling of the main ranking feature and documented all key metrics and processes to reliably reverse the scaling, preserving interpretability.
Consumer dashboard: Continued advancing the low-level consumer dashboard to enhance consumer decision analysis capabilities.
In Progress:
Journey scoring model: Reviewed documentation and discussed implementation details with stakeholders.
Upcoming:
Expecting to receive app and clickstream data tables soon, broadening the data foundation.
Initiating feature analysis to explore how new data can be integrated into propensity models, targeting improved accuracy ahead of journey scoring model deployment.

Mirielle
CONTACT CENTER
Workforce Planning -- North America (Royal)
MAPE View Added to the App: Implemented functions to fetch forecast accuracy metrics (including MAPE), built visualization functions with formatted dates and percentage scaling, and integrated the new MAPE chart into the "3 Months Call Volume Forecast" tab.

Workforce Planning -- North America (Celebrity)
Celebrity Dataset LOB Mapping Complete: CASINO_SALES, CASINO_SERVICES, CO_RIVER_SALES, CO_RIVER_SERVICE, CO_SALES, CO_SERVICE, CVP_GROUP_SALES, CVP_GROUP_SERVICE, CXC_INBOUND, CXC_RETREAT, PCP_SALES, PCP_SERVICE, WEB_BOOKING_SERVICE.
Next Steps: Ongoing call volume data cross-validation with Darren and the North America team.
Stakeholder Engagement
Aligned with Jason and team on a single unified app with a home screen offering two entry points (Royal and Celebrity), each routing to its corresponding section.
Confirmed plan to maintain one app for North America encompassing both brands.
App Redesign for Celebrity Integration (In Progress)
Added brand-first landing flow allowing users to choose Royal or Celebrity before data loads; selection persisted in session state and used to route all app behavior.
Updated all data retrieval to use brand-aware loader functions ensuring each section queries the correct brand dataset.
Revised save/writeback logic to be fully brand-specific, including table naming conventions using brand + LOB to prevent overwrite conflicts.
Verified the app consistently passes the selected brand through all key fetch/save pipelines (LOBs, forecast/historical data, adjustments).
Built and iterated a dedicated landing UI module with aligned cards, color-coded brand visuals, centered headers, and properly placed logos.
Added a restorable snapshot for stability and safety during major changes.
Expected Outcome: A single unified app supports both brands with isolated reads and writes, and the user's brand selection drives all data-loading, UI, and persistence behavior end to end.
Workforce Planning -- North America (International & Casino)
Platform & Azure Container Support: Submitted a Service Principal request for the application (ServiceNow ticket: RITM0498119).

Doug

**Revenue Management CEL**

**CEL | PERKS | 4 Weeks + Supplemental DS Analyses + February Readout | FEB**

Preliminary final analysis and recommendations presented by Nikita to Irena this morning. Full end of test scheduled for 2/24/26 following collection of data for extended test metas.

Data correction required for business-supplied pricing gaps due to overlaps caused by end-of-test price changes populating into test. Mitigation successful.

Completed code that consolidates price uploads into a single process within Databricks (Milestone 1 of 5 of PRE consolidation). Will be monitoring and adjusting over the next 2 weeks in production as the rollout requires a couple weeks of phased pull requests. Next milestone is common data ingestion and updated validation framework for both.

Michelle

CEL Revenue Management

**Category-Gapping** 2.0

Upgraded the optimization that selects optimal gap. Goal was that when multiple gaps produced similar revenue, the lowest gap was chosen even if it was not the most revenue optimal. For example, if the lower gap had a revenue within 1% of the max, pick the lowest gap. We wanted this to apply if the gap vs revenue curve was flat. However, this was not successful because when the curve had a strong peak, and a lower gap was selected, the APD dropped too much.
The new approach is dynamic: it looks at the shape of the revenue curve around the optimal gap to decide how aggressively to prefer lower gaps.
o When the revenue curve shows a sharp peak, we trust the optimizer and keep the precise optimal gap.

When the curve is flat (i.e., many gaps yield similar revenue), we automatically prefer the smallest gap that still delivers near max revenue.

This reduces unnecessary price uplift when it doesn’t increase revenue, improving tradeup without sacrificing revenue.

Business impact:
o Revenue stability: We keep value when the peak is strong; we avoid overpricing when the gain is negligible.
o Robustness: Fewer edge-case failures and more resilient optimization under noisy or uncertain model predictions.
- Working on complete list of sailings to send to business.

- Michelle

- CEL Revenue Management**
Category-Gapping 3.0**
Working on back tested sailing examples comparing the multiclass model that includes all tiers vs combined approach (GTY decision is a trade-up choice using the 2.0 model and the EBM Classifier only includes the physical tiers)
Meeting with team to plan out optimization framework and how it will interact with Lamis’ demand curves.
**Model Upgrades:**
o Additional features added to training dataset:
§ Availability Shares
§ Seasonality
§ Departure DOW
§ Weekend Overlap
§ Pricing
• Log Price
• Difference from LAF
• Price rank of available options
• Cheapest/Most Expensive Flags
§ Number of Options
o Feature Selection: two stage
§ Variance Thresholding: removing features with constant values
§ Mutual Information Selection (SelectKBest): keeping top K most informative features using mutual information
o GridSearchCV
o Sample weights
- Exploring binary model approach, which could lead the way for category level modelling.
o Customers do not choose from a universal list of cabins, they choose one option from the specific set of rooms available at the time of booking which vary by sailing, ship, rdss, and date.
o A multiclass model assumes a fixed set of categories but a binary model treats each cabin option as a choice and predicts the probability that the customer selects it.
o Multiclass classification assumes there is one consistent set of classes and classes exist independently of context
o In reality, each booking sees a different set of options, chooses exactly one option from that specific set, and categories are not universal (some categories won’t appear on some ships)
- Binary model structure:
o multiple rows per booking, one for each option, with features describing: that option’s price, characteristics (meta, season, etc), relative features (Is it cheapest? % premium vs. alternatives?)
o binary model predicts a utility score for each option
o softmax within the booking to get proper choice probabilities.
o Can better handle missing categories in the choice set

Lamis

CEL Revenue Management | Track Optimization FEB

**Revise Formulation to use demand curves rather than directly calling the demand model object and perform .predict() operations**

Completed this first part of this sub-task this week. Starting today and tomorrow with the validation part specially to handle potential sources of infeasibilities

**Lekha**

**CEL Revenue Management**

**Data gathering for Dashboard**

Identified that the exact demand prediction values (y_pred) used to make price changes were not being saved earlier in the price changes history table, and the elasticity output table gets overwritten every time the model runs, which is why y_pred is missing for older run dates.

Because of this setup and Delta vacuuming that deletes data after 7 days, older versions of the elasticity output table are no longer available, so we cannot go back and join past prediction values with the price history. This limitation was discussed with Kevin

To fix this going forward, we updated the production logic to save the prediction values (y_pred), price changes, and all model feature columns directly in the price changes history table.

Proceeding with dashboard development using the currently available post-change data,

**Overview of Dashboard Development and Evaluation Logic**

Developed a demand forecast model health-check dashboard to monitor weekly model performance across major and minor meta products.

Implemented SQL logic to deduplicate multiple production runs per week, retaining only the final weekly run

Aligned weekly predictions with next-week actual demand to calculate accurate forecast errors, excluding future weeks without ground truth.

Computed key evaluation metrics including Absolute Error, sMAPE, accuracy %, and error buckets (Low / Medium / High).

Added Weeks-to-Sell (WTS) booking window buckets to analyze forecast performance by booking horizon (Close-in, Medium, Far-out).

Built interactive visualizations showing forecast deviation trends, error distribution by cabin class, price vs demand behavior, and performance by ship class and port..

Evan

RCI Revenue Management

**Factor Models**

Stagewise feature introduction approach tested

Checked feature sensitivity testing to evaluate impact of new variables

Confirmed approach for controlled feature entry into base estimator

Double ML method introduced to evaluate features

Estimated Average Treatment Effect (ATE) and CATE

Isolateed causal treatment effects to validate feature relevance

Feature Impact Analyzer built and tested

Rolling backtest with per-sailing perturbation across all ships

Sweeping 15 controllable features of a percent change to measure change in yield

Ranked features by optimal delta and elasticity to identify highest-impact levers

Queries added for additional methods

Standardized pullbacks from .sql for consistency and reproducibility

Model design and pipeline steps

Continued refinement of end-to-end scoring and factor workflows

Pipeline modularity to support multiple estimation strategies

Evan

SSC Revenue Management

**AB Testing Framework**

Framework completed for core testing infrastructure

Synthetic data updated to align with latest pipeline outputs

Main class methods debugged and finalized

Unit tests evaluated and completed

Package development (.whl) for distribution / deployment

Jesse

SSC Revenue Management

**Universal AB Testing**

**Unit Testing   **I collaborated with my data science colleagues to complete the unit testing segment of the universal AB testing framework. The unit testing module utilizes synthetic data to test the 25+ key functions that comprise the UAB Framework. I also ensured that all unit testing functions successfully run with synthetic data, meaning that any unsuccessful future test will indicate a bug in the code and not a faulty module. Version one of the UAB Framework is now viable and ready for rollout.

Jesse

SSC Revenue Management

Bug Fix

Two weeks ago, PRE inverted 5000+ price points contrary to PRE Reservation System rules. Through careful planning, I utilized PRE to revert these prices back to their original amounts so that SSC Reservation Team did not have to revert them manually. I pinpointed the underlying issue and corrected the issue.

Kevin & Glen-Erik

PCP Pricing Automation

We refined the target population and the offer to account for existing promotions. Offer: 50% off Deluxe Beverage package (up from 45%) Population: 50 Balcony Cabins on IC 3/7 Low casino and CAS loyalty all guests in cabin US Market No Beverage purchased in cabin Non-GTY Completed: Audience Selection First pass Data formatting Pending: Guidance on Hybris data requirements from digital team. We need inputs from the Marketing copy and imagery for takeover and other messaging. (Requirements shared on alignment call today) Once completed we can rapidly test the promotion. My understanding of the things left contract-wise besides the new Kafka topic setup: (1) have a mapping of the contract to what is shown to the user on the app and web (with images of the front end) so we understand what we are putting in the data fields, (2) remove any unnecessary fields (after looking at mapping from #1, like redemption text, introduction text, offer text, lots of texts maybe not all are used?, (3) verify what the columns mean (id's and such). For the Id's specifically we were confused to what the difference is between ID and correlationId, and what their implications are in Hybris.

Our understanding of the things left contract-wise besides the new Kafka topic setup:

(1) have a mapping of the contract to what is shown to the user on the app and web (with images of the front end) so we understand what we are putting in the data fields,

(2) remove any unnecessary fields (after looking at mapping from #1, like redemption text, introduction text, offer text, lots of texts maybe not all are used?,

(3) verify what the columns mean (id's and such). For the Id's specifically we were confused to what the difference is between ID and correlationId, and what their implications are in Hybris.

If we get the contract documentation, AI team will be likely starting testing of the Targeted Offers with Digital next week. Data Engineering will be pushing records to a Kafka topic for 1:1 targeted offers. Data Engineering will need a replicator from IT, similar to what we did for promotions, so the Digital team can consume them.

Ayon

Win-on-Waste:

Conducted initial back testing of the segmentation logic across multiple ships and routes.

Early results indicate clear separation between High, Regular, and Low demand regimes, with minimal overlap in model routing.

Verified feature consistency and stability for:

Seasonality and day-of-week effects

Demographic- and geolocation-based demand drivers

Holiday and special-event proximity

Confirmed that the pipeline is correctly allocating historical observations into regime-specific datasets for downstream training.

Early Insights:

Models trained on segmented datasets show reduced regime-mixing bias, particularly around high-variance days (e.g., embarkation, holiday voyages).

Initial error reductions observed in preliminary prototypes; detailed metrics to follow once full validation is complete.

Next Steps (In Progress):

Expand backtesting to a wider set of itineraries.

Compare segmented vs. non-segmented models on accuracy, stability, and responsiveness during high-demand periods.

Prepare documentation for integration with the broader Interport forecasting workflow.

**Mert:**

**MIAP**

Completed RD-class multistack chiller tag mapping.

Met with the IBP and Asset Management teams and aligned on the path forward for marine supply chain optimization. Agreed that consumables present the greatest near-term opportunity, while capital and maintenance solutions will require more time to develop.

Met with the Newbuild IT product team to review MIAP change orders for *Hero* and all subsequent newbuilds. A $55K per-ship CAPEX will be added to all newbuilds, enabling the MIAP team to charge integration hours and develop ship-specific models.

Met with the Decarbonization team and aligned on the strategy for digital twin model productionization. Agreed to demonstrate model accuracy on a per-ship basis and engage the fuel forecast team to begin the transition toward using digital twin models for fuel forecasting.

Met with the IT and Network teams to review Koja cabin automation system data integration into MIAP.

**Arya:**

MIAP

Started testing a deep learning model to predict individual diesel generator (DG) output from total power.

Tested across varied sample sizes and ships with different engine configurations (DG vs DG, DG vs GTG, and DG vs DG/GTG/STG).

Fixed AHU and chiller pipeline issues.

Researched methods for incorporating engine distinction as a model feature.

Prepared presentation for Tuesday.

Added RA and EQ to HVAC.

Fixed bugs in the HVAC notebook run.

**Will:**

**MIAP**

Added shore power support to the MIAP web app.

Fixed a bug where passing None for shore power capacity caused the optimization to fail.

Added new metrics to break down CO₂e and power consumption (power plant vs shore power).

Started work on a new FACTS model mode for fuel forecasting. This will enable forecasts for ships without adequate fuel metering.

**Mahshad****:**

**MIAP**

Finalized a solution with Marcio to prevent out-of-disk-space errors in MIAP pipelines. All pipelines now run on fresh agent instances, and compute is no longer shared across pipelines.

Investigated and resolved data issues impacting workflow stability and model reliability.

Identified ship-level anomalies, analyzed deviations, and coordinated follow-ups with the ML, WN, and AD teams.

Continued building the new agent and resolved a branch-related issue requiring troubleshooting.

**Reza:**

Optimized the digital twin / power plant optimizer to speed up processing for identical rows. Verified runtime improvement from over 4 hours (workflow timeout) to approximately 1.2 hours on sensor-based workflows.

Reviewed and refined error logging for fuel forecast pipelines (FACTS-based and sensor-based) to ensure both general and row-level errors are captured.

Debugged the sensor-based fuel forecast workflow in the QA environment.

Finalized the FACTS-based script in preparation for workflow integration.

Mert

New Build

Newbuild:

Newbuild team provided access to few historical project files on SharePoint for us to demo the AI assistant solutions.

We've requested full suite of Azure resources to be created for Newbuild (DataBricks, Data Lake Storage, Keyvault, Container Apps, Service Principals, Security Groups), to be used to pilot the AI solutions. Platform team completed the creation of Azure resources. Waiting for IT to finish creating service principal creation, to be able to start reading from SharePoint.

Agreed with Newbuild that an NDA will only be needed with contractors and not existing FTEs.

Met with DNV Synergy Life team who hosts Newbuilds risk assessment data and discussed how we can integrate this data to Alpha Platform. They have a solution to push directly to blob storage but there is a subscription cost that Newbuild has to internally align on paying.

Henry Drescher

Contact Center: Conversational AI

**Accomplishments – Last 7 Days**

**Cresta Program**

Completed SQL rework enabling the transition from SpeechIQ to Cresta, ensuring continuity of speech analytics and preparing for topic activation to enhance performance insights.

Advanced Phase 4 rollout with updated mappings for non-Casino lines of business, supporting full contact center alignment.

Updated Cresta performance dashboard visuals and data model to improve accuracy of KPI tracking across brands.

Finished app deployment and SSO activation for Phase 1.2 rollout, enabling training and early user adoption.

Submitted required access and deployment requests for upcoming rollout phases to maintain momentum.

Launched aligned workstreams for training, QM, and reporting to ensure coordinated execution.

**Conversational IVR / Copilot Migration**

Continued ETL development for Copilot data ingestion to preserve analytics continuity post-migration.

Conducted UAT readiness sessions across business, testers, and developers to ensure a smooth migration path.

Progressed integration of Guest Profile API and GenAI modules to bring personalization and intelligent responses into IVR flows.

Estimated IVR concurrency and AHT to support accurate infrastructure and capacity planning.

**Other Initiatives**

Supported call volume forecasting and FTE modeling to strengthen workforce planning.

Provided analysis for calls-per-booking to support Casino operations.

Maintained leadership-level presentations to ensure visibility and alignment on program status and strategy.

**Currently Working On**

**Cresta Program**

Continuing refinement of topics and optimization of hints and behaviors to improve agent guidance effectiveness.

Completing user application validation and resolving access discrepancies to ensure a smooth launch experience.

Advancing discovery for future use cases aligned with operational needs.

Tracking issues, trends, and root causes to support clean rollout execution.

Collaborating on performance analysis, including evaluating efficiency and sales improvements driven by Cresta.

Building a unified production rollout plan covering skills, timing, and dependencies.

Delivering call skill extensions required for Phase 4 readiness.

**Conversational IVR / Copilot Migration**

Beginning UAT execution for Copilot migration, supporting stability and readiness for production.

Continuing integration of Guest Profile API, enabling more personalized guest experiences in the IVR.

Advancing GenAI response logic within legacy flows to improve self-service quality and containment.

**Assessment and planning for 1****-way SMS integration** to expand guest communication options and reduce call demand.

**Planning analytics parity with Nuance** to ensure reporting continuity and maintain visibility into contact center performance.

**Evaluating the addition of GTS and GEM to existing bots** to expand automation opportunities and enhance guest self-service.

**Other**

Continuing management of monthly and quarterly leadership materials to ensure clear communication of program status.

Erick Alfaro

**Project Axiom**

*AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.*

**Meta Data Extraction**

**Divisions Meta Data Framework** *(David M.)*: Split oversized result files into smaller parts for reliable processing. Batch jobs running for Q3 of previous year on OAI batch processing. Fixed slow venue prefix function with significant performance improvement. Unified division mapping confirmed complete.

**Quantized Embeddings Pipeline** *(Erick A.)*: Created API to compute embedding clusters on the fly, deployed on Lambda server alongside the Drivers Model API, now serving real-time to the Axiom webapp.

**Silversea Email Reports** *(Erick A.)*: Iterating on Silversea email reporting. Short-term hard-coding valid rows while awaiting unified division mapping table from David for long-term fix.

**Reporting**

**GSO Safety Email** *(**Danusio** G.)*: Implemented two-step LLM classification pipeline: sentiment filter → onboard/shore excursion classification → hazard type, location, cause, and seriousness extraction → LLM summaries. Added third "not safety related" classification to reduce unnecessary API calls. Excel template submitted for Melissa's approval before automating.

**Guest Strategy Email** *(Rodrigo B.)*: Found metric discrepancies (up to 3 points) versus Jose's reports, traced to data refresh timing differences and field usage (prediction vs. actual fields). Preparing specific examples for business review and scheduling alignment meeting on load factor methodology.

**RBC Email Follow-up** *(Erick A.)*: Forwarded RBC email to stakeholder Gang for feedback. Gang may prefer a simpler format (topic summary only). Awaiting response to determine next iteration.

**Power BI Dashboard** *(**Danusio** G.)*: Dashboard deployed to Data Science Premium workspace and shared with Silversea stakeholders. Issues identified: data is stale and only Royal brand is represented. Actively adding Celebrity and Silversea brands and focusing on "Trends" and "Reporting Topics" tabs. Gateway setup needed for production deployment.

**RBC ****PowerBI**** Dashboard** *(Rodrigo B.)*: Generating topic and subtopic descriptions and weekly summaries. Connected to Databricks. Gateway setup needed for production authentication.

**Modeling**

**Lambda Server Deployment** *(Erick A.)*: Drivers Model API and Clustering API both deployed to in-house Lambda server (8 GPUs) using agentic-first coding, replacing Databricks endpoints for significant cost savings. Both APIs now powering the Axiom webapp in real time.

**Drivers Model API Migration** *(Osvaldo V.)*: Successfully migrated API logic to Lambda server. Deployed two MLflow models (Celebrity and Royal brands). Previous GPU cluster endpoints removed.

**Drivers Dashboard & Axiom Integration** *(Osvaldo V.)*: Finalizing API connection, addressing remaining visualization issues, and preparing PR for code review. SHAP values showing only positive contributions — investigating calculation logic to ensure both positive and negative impacts are represented.

**Medallia Keyword Correlation Tool** *(Osvaldo V.)*: Prototype working in dev Axiom app, enabling business users to select features and view correlations with sentiment and comment analysis. Minor display issues (label overlap) remain.

**Weather Satisfaction Correlation** *(**Danusio** G.)*: New task to map longitude, latitude, and weather metrics against satisfaction scores. Exploring a map-based visualization tool in the Axiom webapp using Python geospatial libraries.

**Guest Logs Categorization** *(David M.)*: Continuing adjustments to improve classification results based on stakeholder feedback. Batch jobs planned once current division processing completes.

**AI Pivot *****(Qualtrics Topic Extraction)***

*Self-labeling framework for automatic topic discovery from survey data.*

**Topic Drift Analysis** *(Rodrigo B.)*: Jensen-Shannon divergence analysis confirmed topic distributions remained stable across most months (2024 vs. 2025), validating that 2025 topics can reliably label historical data. Embeddings and cosine similarity used to reduce hallucinated and unlabeled comments.

**Abandoned Cart Dashboard** *(Rodrigo B.)*: AIP dashboard generated and confirmed visible in Axiom. Renaming from "topic performance" to "abandoned cart performance" for clarity. Pending stakeholder consultation on actionable insights.

**Abandoned Cart Data Aggregation** *(**Danusio** G.)*: Presented dashboard structure with overall metrics, cluster-based trend detection, and topic-level sentiment analysis. Submitting detailed plan to Erick for review before implementation.

Erick & Cristian

**PCP ****MyCruise**** Recommender**

*Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app.*

**Recommendations Engine *****(Cristian V.)***

**AB Test Methodology Review**: Identified discrepancy with Rosie's analysis methodology — Rose filtered out users who didnt interact with Shorex products, producing measurable uplift, while the DS team's analysis included all users, diluting the effect. Planning rerun with Shorex-specific filter; confident sample size remains sufficient for statistical significance.

**Product Co-Occurrence Visualization**: Developing chord diagrams and network graphs to show product co-occurrence from user interactions, enabling the business to identify bundling and promotion opportunities.

**Graph-Based Recommendations**: Investigating GCN, bipartite graphs, and Louvain community detection to address data sparsity in the current Apriori model (most baskets contain only 1 product).

**Prod Job Failures**: Root cause identified — missing DROP IF EXISTS statements caused failures when tables were absent. Cristian fixing code-side handling; Erick investigating potential API data retrieval failures separately.

Glen-Erik

PROPEL (CEL)

Dynamic Test/Control measurements missing categories and overall uplift: reviewed the full measurement notebook and master table logic, Power BI code and automation refresh. Refactored test/control assignment into a backward-compatible, version-aware system with category-level targeting. Reviewed Uplift model for potential dependencies with the latest measurements code that need to be reverted. Reviewed metrics (Revenue, PCD, APD) with filtering for statistically sound measurements. *(Javier)*

Offer Template: *(Glen-Erik)*

refined how casino offers display and tested on reflection in dev

Started testing all offers in dev in other regions, beginning with Infinity

General support including weekend inquiries. *(Glen-Erik)*

*Hiring: *Made offer to candidate who accepted and starts in March.

Eswar

Revenue Management

SPI: (Eswar)

Code review and modified code to be production ready.

Working session on writing production ready code, CI/CD process, walking through best practices

Data Validation Framework: (Eswar)

Reviewed existing PRE data validation code to identify its functionality and ways to replace it with Validation framework developed

Support: (Eswar)

Reviewing and monitoring PR's. CI/CD

Providing MLOps support in bypassing issues, enabling developers by providing guidance and productionizing workflows.

Databricks Asset Bundle upgrade (ACR): (Javier)

Track RCI and Track CEL pushed to production.

Automated Code Review rules enhanced to reduce false positives and account for different scenarios.
