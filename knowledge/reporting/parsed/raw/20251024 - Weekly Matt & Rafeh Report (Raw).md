**Henry Drescher**

**Contact Center: ****CrestaAI**

**Accomplishments – Last 7 Days**

**Shifted focus from IVR reporting to ****SpeechIQ**** sunsetting**
*Impact:* Aligns team efforts with evolving strategic priorities and supports a smooth transition from legacy systems.

**Validated sample data structure and confirmed topic backfill**
*Impact:* Ensures data completeness and integrity for downstream analysis.

**Secured URL syntax for deep-linking**
*Impact:* Enhances navigation and usability within reporting tools.

**Henry Drescher**

**Contact Center: ****IVR**

**Accomplishments – Last 7 Days**

**Roll-Out plan finalized and approved**
*Impact:* Clears the path for deployment and confirms alignment with leadership expectations.

**Diagnosed dashboard refresh issue**
*Impact:* Identified stale data in Databricks due to ETL delays; resolution is underway to restore dashboard reliability.

**Henry Drescher**

**Contact Center: ****Conversational IVR**

**Accomplishments – Last 7 Days**

**Advanced Gen AI solution prototyping**
*Impact:* Drives innovation in customer interaction and automation capabilities.

**Presented guest profile API integration to business and IT stakeholders**
*Impact:* Strengthens personalization efforts and cross-functional collaboration.

**Reported key metrics to business (e.g., Make a Payment counts since Nov 2024, IVR AHT for both brands)**
*Impact:* Provides actionable insights for performance tracking and strategic planning.

**Feedback Loop**

**Resolved inaccuracies in Gen AI FAQ responses**
*Impact:* Improves trust and reliability in AI-generated content.

**Henry Drescher**

**Contact Center: ****CrestaAI**

**Currently Working On**

**Reworking new hire pilot and developing post go-live measurement plan**
*Expected Impact:* Strengthens onboarding effectiveness and ensures measurable success post-deployment.

**Addressing supervisor/staffing changes and account access issues**
*Expected Impact:* Improves operational continuity and user access reliability.

**Validating data in Databricks**
*Expected Impact:* Ensures data accuracy and readiness for scalable reporting.

**Henry Drescher**

**Contact Center: ****IVR**

**Currently Working On**

**Copilot data review**
*Expected Impact:* Supports improved decision-making and system performance.

**Henry Drescher**

**Contact Center: ****Conversational IVR**

**Currently Working On**

**Continuing Gen AI prototyping and refining knowledge source exclusions**
*Expected Impact:* Enhances AI relevance and user experience.

**Managing HCL T&M contract**
*Expected Impact:* Ensures vendor alignment and resource continuity.

**Follow-ups on guest profile API integration presentation**
*Expected Impact:* Drives adoption and alignment across business and IT.

Carlos

E-Commerce Customer targeting
Delivered
Developed two “days_to_book” model variants:
Variant 1: Calibrated approach leveraging existing booking propensity scores.
Variant 2: Regression model predicting days_to_next_booking.
Completed comparative evaluation of both approaches.

Carlos

E-Commerce Customer targeting
In Progress / Next Week
Present results to the business and promote the top-performing model to production upon sign-off.
Tested a compute-optimization strategy by scoring from prior-week outputs rather than raw data; results improved vs. baseline but are not yet ideal. Will review next week for a go/no-go decision or deferment until more consumer segments are integrated.

Carlos & Camila
Supply Chain
Delivered
HF&B demand model rebuild (Royal + Celebrity) technical assessment:
Deeper validation identified underperformance relative to the production model on high-cost items using cost-weighted MAPE.
Ranked prediction plots show improved recall/precision on zero-consumption items but weaker performance on items with actual consumption.
Cost-weighted MAPE accepted for inclusion in reporting; integration into reporting tables is underway.

Carlos & Camila
Supply Chain
Delivered

Initiated Silversea uniforms crew consumption logic: grouped similar product names and scaled consumption by crew counts.
Migrated compute clusters in production pipelines with help from Glen-Erik to use Job Compute instead of more costly interactive compute. 
CocoCay integration into HF&B demand files nearly complete; Azure Blob Storage save issue resolved.

Carlos & Camila
Supply Chain
Delivered
Testing pipeline updates:
Brand/product substitutions via IBP Intake Form logic completed; identified circular mappings (old → new product) now pending correction.
Region/brand/product substitutions via Product Mapping in Designated Regions completed.
Fixed “Legend of the Seas” first sailing date logic (no longer biased by NONREV meta product code mentions).
Guardrails updates applied; final confirmation will follow after full-file load.

Carlos & Camila
Supply Chain
Delivered

RCI/CCI Order Creation “Actual Quantity Needed” logic expanded:
Past inbound orders: include if anticipated ship date < today and inventory type status ≠ 3 or 4.
OPJ inbound orders: include if post-inventory scheduled date is between today and ship load date.

Carlos & Camila
Supply Chain
In Progress / Next Steps
Rebuild remediation: refine feature engineering and selection to prevent target leakage; use ANNUAL COST as model weights in recursive feature elimination with cross-validation.
Add cost-weighted MAPE to reporting tables.
Pending / Dependencies
Documentation for tables not in the dev_datscience environment.
Default Silversea uniforms contract length to 3 months.
Add weighted MdAPE columns to backtest tables.
Replace nulls with zeros in IBP data extracts.
Medical finance tool; CocoCay finance tool.
Finance automation for remaining categories (requires alternate logic; walkthrough pending).
Port itinerary table: add final-port filter to complete warehouse transfer order mapping to regions.
Uniform order creation logic.
Onboarding of a new contractor on Monday.

Mirielle
Contact Center: Lead Prioritization OFTOCX
Delivered
Completed feature engineering and modeling for Royal and Celebrity.
Built and tested production pipelines in the development environment for both brands.
In Progress
Testing production pipelines from master in QA and PRD environments.
Ongoing Discussion
Incorporation of a new “Agency Id” column under review with the CRM team.

Mirielle
Contact Center: Workforce Planning – North America
In Progress
Data discrepancy investigation: September call volume doesn’t align with Databricks (other months align with Excel/Power BI); root-cause analysis underway on dataset prd_silver.mkrpops.v_cms_dsplit_daily_all with the cross-functional team.
Call volume forecast models for 12 LOBs:
Skill mapping under review (focus on GEM and Groups).
Feature engineering includes:
NorthAmericaHolidayCalendar (US Federal + Canadian holidays).
Enhanced holiday features: basic holiday indicators, major holiday flags, week-based proximity (1–4 weeks pre/post), days to/from major holidays, and special holiday-season indicators (Christmas, New Year, Thanksgiving).
Residual and lag features; additional signals under exploration.
Team operations:
Awaiting baseline assumptions table per LOB.
Reviewing weekly office-hour grids per LOB; office-hours sheet will be shared for review.
Pending
User access permission to the app remains pending.

Mirielle

Contact Center: Workforce Planning – International
Delivered / Setup
Project outline established.
Next Steps
Data handoff; begin drafting the app outline, starting with historical data visualization.

Cihan

Digital App (RoyalOne)
Qualtrics Survey
Delivered / In Progress
Reviewed stakeholder topic lists and descriptions.
Aligned survey topics with app review topics/descriptions for consistency.
Met with stakeholders; topic set is being finalized.

Cihan

Digital App (RoyalOne)

Guest Services Chatbot
Delivered
Transitioned dashboard ownership from our environment to the Digital team’s environment to streamline change requests.
Pending / Next Steps
Quantify the percentage of guests opting to connect directly with an agent versus engaging with the chatbot.

Cihan

PCP Pricing Automation : On-Board Revenue
Waterpark PRE
Delivered / In Progress
Finalized the initial elasticity model.
Logged model and metrics in MLflow for traceability and reproducibility.
Meeting scheduled with stakeholders to review results and gather feedback.

Cihan

PCP Pricing Automation : Alaska ShoreEx
Delivered / In Progress
Resolved data discrepancies in UC tables in coordination with Data Engineering.
Conducted cross-table data validation and fixes.
Removed duplicate product codes; updated feature stores accordingly.

Cihan

Contact Center: E-Commerce Live
Live Person Classifier
Delivered
Implemented requested logic updates to the existing model.
Deployed the updated model to production; delivery and deployment confirmed by stakeholders.

Caleb & Ben

CLTV
Delivered
Built a clean analytics table enabling pre-production cross-functional use.
Joined new columns (celebrations, cobrand, booking type) and consolidated brand-specific columns for clearer features.
Renamed ambiguous fields to match actual content.
Validated casino population and indices with the responsible analytics function; retained current flags based on alignment.
Shared River + credit card cobrand insights with stakeholders:
River guests predominantly fall in the top quartile of their cohorts; strong index and NPS.
In Progress / Next Steps
Final iteration of the DMA/Booking Window BI tool; final review session scheduled.
Finalize callouts covering use cases, interpretation of nuanced proportion fields, and guidance on customizing group-by slicers.
Complete the final weighting solution for the attractiveness score.

Ayon

Win on Waste

Redeveloped the rules engine for both Specialty and MDR pipelines, sunsetting the previous codebase, and implementing a strategy that emphasizes recent consumption data with adjusted weighting for improved forecast accuracy.

Integrated Schooner Bar profit center into the pipeline with necessary schema and processing updates.

Developed and deployed a workaround for Couchbase API write issues in development and staging environments

Mert

MIAP
Prepared the MIAP Phase IV CAR presentation and answered questions on the CAR memo.
Presented MIAP Phase IV CAR to the Capital Committee and received highly positive feedback. This is a BIG win.
Finished the first fully working version of the fuel-forecast API, fixed bugs, and found a solution to run the SCIP solver on Databricks.
Met with the Maritime Safety and Newbuild teams to discuss future AI collaborations.

Mahshad

MIAP
Addressed library issues for the MIAP packages.
Delivered a presentation to the deployment team to share initial results with the OR-Tools library; awaiting the Gurobi license.
Worked on and improved the optimization problem.
Conducted self-study on optimization techniques.
Prepared the MIAP committee meeting presentation.

Mehdi
MIAP

Worked on finalizing the stability agent.
Fixed the registration and deployment issue.
Currently addressing a logical error in the agent.

Ram
MIAP

Highlights:
Investigated and worked on resolving the cluster issue affecting the Crosser job, identifying key failure points.
Collected and documented issues in Eniram by debugging each ship and discussed findings with the Wärtsilä team.
Improved understanding of the MIAP API code and enhanced it by adding logging and exception messages to facilitate troubleshooting.
Initiated a PoC to integrate logs into Databricks for improved monitoring and analysis.

Ram
MIAP

Next week:
Collaborate with the AMOS team to plan the data migration to the Alpha environment.
Migrate all workflows in the DE workspace to the AP cluster to optimize performance.
Develop and test MIAP logging enhancements to ensure comprehensive and reliable log collection.

Arya
MIAP

Finished integrating GMO Safety SharePoint lists into the MIAP database; working on the pipeline.
Researching how to use Azure AI Search for RAG models and how to integrate it with Databricks.

Reza
MIAP

Continued tuning and integrating the fuel-forecast package on Databricks:
Investigated feature transformations to improve propulsion speed–power curve fits (in progress).
Refactored data utilities to support new data-get functions and make them Databricks-compatible (PR open).
Added and configured required optimization libraries in the Databricks environment (setup complete).
Assessed the intercept's impact on regression lines and model bias (initial analysis completed).

Will

MIAP
Finalized and presented SSC fuel curves, improving fuel forecast accuracy from 19.74% MAPE to 11.59% MAPE across the fleet.
Reworked steam turbine generator model features to use a single feature across the fleet instead of depending on onboard power-plant configurations.
Refactored the power-plant modeling pipeline to fix naming-convention errors.
Added notebooks to automatically delete unused power-plant models and tables.
Began creating FACTS data ETL in MIAP to model incinerator and boiler consumption on ships without fuel sensors.
Brendan
On PTO.

Erick

**Medallia ****Project Axiom****:**** Description**

Project Axiom refers to a set of capabilities designed to be applied across various datasets such as Medallia Survey responses, Guest Logs, call center transcripts, call center IVR survey data, Qualtrics, etc. The core capabilities include: (1) Meta data extraction which is the process of converting unstructured data into structured data. (2) Reporting capabilities which encompass email alerts, web applications, dashboards, etc. (3) Modeling efforts include identifying NPS Drivers, setting targets, clustering text embeddings, etc.

Erick

**Medallia ****Project Axiom****:**** Meta Data Extraction**

The Medallia survey has +40 questions of which about ~25 are numeric (0-10) questions and ~15 open ended questions. We currently fit the 15 open ended questions into 39 topic areas. However the business has asked to create new topic areas that match the 25 numeric fields. For example "Staffs ability to resolve issues" is a numeric field and the business wants us to label Medallia comments with these topics in addition to the 39 topic areas.

Erick

**Medallia ****Project Axiom****:**

**Reporting**

This week we created a new email which will focus on negative feedback received with 36 hours of sailing return date. Report should be ready for production next week.

Several other reports have been requested and backlogged.

Erick

**Medallia ****Project Axiom****:**

**Modeling**

Met with RCI Director of Consumer Insights to present initial drivers model. The team is very enthusiastic about the prospect of a tool that can surface NPS drivers. The Acid Test for this model will be its ability to identify Drivers in research cases conducted by Consumer Insights via manual efforts.

Erick & Cristian

**PCP Product Recommendations: **MyCruise Recommender

Calendar Recommendation engine is functional in Databricks and has been deployed to dev model serving endpoint. This latest version of the model serving endpoint points at a Postgresql instance in Azure which lays the groundwork to moving away from storing recommendations in memory. However upon testing the deployed endpoint it was found that Azure Postgresql firewall blocks the model serving instance. We will need to work with platform to resolve this issue.

Aagam

**CEL**** Revenue Management**** Pricing Analysis**

**CEL | PRE Integration of Price Points**

Integrated new CEL price points into the PRE environment across multiple track-reading methodologies.

Enabled week-over-week comparisons of pricing movements by method, improving visibility into pricing trends.

Supports evaluation and selection of the most effective track-processing technique

Atefeh

CEL Revenue Management

**Price Change Logic Presented to CEL**
Shared updated logic using variable norms, with emphasis on handling negative track values. Demonstrated impact via distribution comparisons against constant norms.

Atefeh

RCI Revenue Management

**Archive Table Aligned with PRE 4.0**
Identified outdated columns (elasticity, volume_forecast, track, adjusted_need). After review and alignment discussions with Eddie and Doug, updated archive now reflects both legacy and PRE 4.0 values.

**Promotion Booking Aggregation**
Aggregated VCAP Daily Extreme data by unique promo code keys. Example: 'BOGO60' linked to 412K+ bookings. Shared summary and detailed promo code files with Eddie; now collaborating to group codes for deeper analysis.

Ignacio

PCP Pricing Automation

**Alaska ****ShoreX**** | OBR Feature Store Cleanup**

Removed duplicate product codes causing Cartesian joins and inflated booking counts.

Fix led to significant improvement in booking count accuracy.

Ignacio

PCP Pricing Automation

**Average Price Calculation Fix**

Excluded zero-price bookings from average price calculations in both Daily and Binned FS.

Ensures more accurate pricing metrics and model inputs.

Ignacio

PCP Pricing Automation

**OBR PRE Optimization Validations**

Added backend checks to validate optimization outputs:

Missing outputs vs. expected FCST (beverage only).

Zero/null recommended prices (beverage & cabanas).

Repeated price recs across days, tracked duration (beverage & cabanas).

Ignacio

PCP Pricing Automation

**Promo Upload Automation**

Completed successful E2E testing of promo uploads in lower env across various promo groups.

Filtering logic refined to exclude invalid values.

Enhancement to support GROUP conditions planned post–Black Friday.

Kartik

**LOYALTY | Preferred Point Selection OCT**

**Calculate points conversion for ****SilverSea**

Calculated Silversea APDs by cabin class and benchmarked them against RCI and CEL APDs to establish a points-conversion mapping for consistent loyalty valuation.

Integrated the derived conversion logic into the codebase by adding Silversea-specific categories and mapping rules to the existing conversion module.

Kartik

**LOYALTY |**** ****Analyze Historical Categories: See if Guests book same categories again**

Conducted historical category-retention analysis to assess whether guests rebook the same cabin category on subsequent sailings.

Key findings to date: overall guest cohort rebooks the same category ~60% of the time; Avid Cruises segment shows ~90% retention.

Currently extending the analysis to suite categories to evaluate retention behavior for premium segments.

Jesse

**SSC**** Revenue Management**** **

**| PRE | Validation Testing**

Continued work on validation testing, specifically rules 19.1, 19.2, and 22.2. Encountered unexpected logic issues due to how prices are configured and rejected in the reservation system.

Estimated 2–3 more days to finalize solutions; complexity noted and ticket points adjusted accordingly.

Booking position accuracy ticket was completed and closed. Automated pricing validation improvement ticket remains open but is not a current priority; will be revisited later. October update ticket remains in testing and will be closed next week

Doug

CEL Revenue Management

Data quality review and feedback - ICVCBD

Alaska Open Jaw Good Side/Bad Side added to Celebrity reberthing

All remaining Celebrity inventory automation processes transferred to production Databricks

Michelle

**CEL**** Revenue Management**** | Category-Gapping 3.0**

Resolved result table duplicates and added gty share constraint. Testing lowest-tier price as a feature.

Optimization runtime significantly reduced by replacing direct model calls with surrogate models and auto-differentiation—now runs in minutes vs. hours with comparable accuracy.

Gaps for Gty-Lead and Upper-Premium look stable; Lower-Above gaps flagged for potential adjustment. Testing capped bounds based on current pricing and DART impact.

Review scheduled with Anastasia on Friday.

Michelle

**RCI**** Revenue Management**** | Category-Gapping 3.0**

Met with Kevin and RCI team to define strategy for category-level recommendations.

Plan: Extend 3.0 optimization to derive tier gaps, then apply business rules and data-driven logic for granular category pricing.

Currently analyzing Oasis 7N Caribbean 2025 data (pricing, category order, bookings) to identify patterns and inform rule creation.

**Lamis**

CEL Revenue Management: Track Optimization (Lamis)
Refactored optimization codebase to align with current CEL model in production. Ran sample sailing and reviewed results with stakeholders. Identified directions for validation and scaling.

**Lamis**

RCI Revenue Management: PRE Price Optimization
Scaled optimization across full fleet for weeks of 10/13 and 10/23.

Focused on validation and refinement:

Identified and resolved constraint violations in closer-in cases.

Tested parameter variations (e.g., allowed price change %).

Compared optimal prices to lowest available fares from vps_pricing_flat.

Defined and quantified “counterintuitive” pricing cases based on model logic vs. business expectations.

Generated KPIs and visuals to evaluate optimal outputs vs. PRE 4.0 and actual pricing decisions at meta-cat class and occupancy levels.

Key Findings are that it drastically reduced the % changes of the price as compared to PRE4.0. This is a big-win, as there have historically been larger price change magnitudes for the RCI PRE model and this should reduce the magnitude of price changes on the edge-cases.

**Lekha**

CEL Revenue Management

Near completion on **elasticity guardrails ****investigation**; monitoring price changes to adjust ranges if needed.

Working on **validating price changes using the new elasticity model** (without Dart); started this week and expected to close in October.

Dart-related work will be split into a separate ticket for November, as the model is not yet being productionized.

Confirmed that **productionizing upgraded elasticity model** and **finalizing PRA elasticity model** are duplicates and will be merged. Dashboard-related ticket was marked as complete, with future updates to be tracked under new tickets as needed.
