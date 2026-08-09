Ben

Agentic AI Engineering
Delivered - Pull request for new Scout–Plan–Build command leveraging the open-sourced Compounding Engineering plugin from Every.
Initial tests show strong results building new UI components and updating guardrails to support many backtested supply chain model training dates.
Team discussion on Compounding Engineering principles: “Stop Coding and Start Planning” and “Teach Your AI to Think Like a Senior Engineer.”
In Progress
Next.js multi-agent observability UI (agents running, tool calls, files consumed/produced, and “thinking” activities across subagents to the orchestrator). UI is operational; addressing minor bugs.

Ben & Camila
Supply Chain (IBP)
*UOM gaps: waiting on the item master table (prd_gold). Yan identified inconsistencies; DE to deliver corrected table and push to production to update the UOM source.

Ben & Camila
Supply Chain (IBP)
*Crew uniforms v6 prepared for SharePoint upload; adding conditions to fit array-type product number column due to SharePoint format constraints.
*SSC Uniforms challenger model notebook: modifying code to handle product numbers as array data type; grouping crew model types by contract length and cost center to ensure accuracy for Yan and Paige.

Ben & Camila
Supply Chain (IBP)
Integrated medical free-of-charge consumption using inbound orders and shipboard inventory (instead of the consumption table); pipeline updated and monitored successfully throughout the week to avoid weekend errors.

Ben & Camila
Supply Chain (IBP)
Followed up with DE on the port itinerary table fix for SSC Warehouse Transfer Order mapped to Region; delivery expected Friday.
Will continue building the finance automation table for all categories once the itinerary table is in production.

Ben & Camila
Supply Chain (IBP)
Completed changes from Yan for inbound order quantity using opj open orders.
Delivered first draft of the SSC warehouse unhealthy inventory table; meeting with Yan needed to review logic and resolve observed inconsistencies.
Completed demand modeling code for seven backtested model training dates using the new HF&B model; refactored guardrails to accommodate the seven backtests and now running. Expect results later tomorrow or over the weekend to confirm model improvements.

Cihan
PCP Automation: Onboard Revenue  
OBR Waterpark PRE (Gang Wang)
Working on optimization for the waterpark.
Blocker: prd_gold view performance; DE is converting the view to a physical table to improve runtime.

*Cihan is waiting on DE to provide data because the views provided are unusable. DE says they will have the tables next week, but I have instructed Cihan to work with the business to get Oracle tables rather than waiting so we can make progress.

*There are some struggles with DE and data availability. We've provided a list of views that are crucial for any analyses and are unusable since they need optimization. These also need extensive validation since there are mismatches with oracle source due to disagreements in logic. Gaby and Gang are a bit frustrated with this and it is blocking some tasks. While they work through this I've instructed Cihan to work with the OBR teams to get the Oracle tables from the business and work off of those.

* DE is giving some pushback on CRF automation as it may delay timelines for other deliverables. I don't entirely disagree but RCI is wanting to strongly prioritize this. Vic from the CEL team is bringing it to Rafa and Alex to make sure the brands are on the same page with priorities. Ignacio will require support from Jean on DE in order to complete the CRF work.

Cihan

Digital RoyalCommunity:
Digital – Qualtrics Survey (Jaime Stoelar)
Updating pipeline to use asyncazureopenai() for batched parallel API calls to speed up processing.
Digital – Guest Services Chatbot (Eunha Kim)
Pipeline updated to include bot_not_wanted escalations; visualizations shared with stakeholders.
Expanding to other escalation types; awaiting stakeholder patterns to identify additional escalation categories.

Carlos
E-Commerce Customer Targeting
Updates
Improved sailing_window/sailing_horizon model accuracy via new custom features in the feature store and better handling of class imbalance.
Developed a 26-month sailing propensity model to complement sailing_window targeting, enabling selection of top consumers likely to sail within a given period.
Deployed both models to production; stakeholders have access to scores and dashboard reports.

Mirielle
Contact Center: LP OFTOCX (SBOFRD sub-lead types)
Completed
ETL process set up for six sub-lead types.
Designed data loading workflow for each sub-lead.
Built feature engineering workflow for each sub-lead.
Developed utility functions to orchestrate all notebooks.
Updated the Agency ID column using the previously empty EVENT_CODE column.
Configured Min/Max Sequence_id so ETL triggers only on new leads.
Orchestrating notebooks to build ETL production for each sub-lead and consolidating into a single master notebook (in progress).

Mirielle
Contact Center: LP OFTOCX (SBOFRD sub-lead types)

Next Steps
Test the production process in DEV, QA, and PRD.
Validate lead ingestion with the Siebel team.
Working Session with Nelson
Walkthrough of ETL production triggers and Siebel ingestion points; assessing feasibility and readiness for production deployment next Monday.

Mirielle
Contact Center: Workforce Planning – North America
Completed: Resolved call volume data discrepancies.
Ongoing: Call volume forecasting for low-volume LOBs (CO_GROUPS_SALES, CO_GROUPS_SERVICE, GEM, CE_SALES), orchestrating training across LightGBM, XGBoost, CatBoost, HistGradientBoosting; configurable via models_to_run parameter.
Pending: Darren Andree’s access permission.

Mirielle
Contact Center: Workforce Planning – International & Casino App
Completed: Visualization app section to explore/filter by market, display by LOB and date, and show KPIs (call volume, AHT, abandon rate).
Updates: Revised display structure to provide a visual breakdown by region (International and Casino), with Royal and Celebrity treated as sub-groups.
Platform/InfoSec: Coordinating migration of the Databricks App to Azure Container Apps; low complexity expected (no local user authentication). Mukund assisting; working with Utkarsh and Platform team.

Caleb
Customer Lifetime Value (CLV)
In Progress
Finalizing SOP documentation to democratize CLV methods and database: refining descriptions of custom fields, simplifying scope language, final revisions on example SQL, join methods, and aggregation instructions; refining inclusion/exclusion (removing POTENTIAL fields and adding opportunity cost caveats).
Revising RCI indirect cost logic for per-booking and cruise experience using an 80/20 infrequent/frequent split; performing detailed validations for proxy years only, carrying over cost-per-booking rates from 2019 and 2023.
Assisting with Cobrand and Loyalty slides for Lisa.

Mert:

MIAP

Completed full integration of Digital Twin models with the MIAP API. Implemented a polling architecture where heavy model initialization (loading up to 15 ML models per ship from Databricks MLflow) is offloaded to an Azure Container Apps job. Clients can poll the main API for initialization status. Once a model is initialized, users can start a voyage simulation with a unique voyage model initialization file. This file is stored in memory and cached in blob storage for fast retrieval.

Started integration of the Digital Twin API into the MIAP web app to allow users to visualize and simulate voyages.

Met with Legal and Risk Management to clarify AI ethics concerns for Project TIDE (claims management) and aligned on not using PII for model training.

Integrated ML and EQ into the MIAP IoT platform.

Met with the Databricks Zerobus team and discussed a POC to replace Kafka with Zerobus for IoT data streams. Replacing Kafka removes a middleman in IoT flows and allows writing data directly from IoT devices to Databricks.

Mehdi:

MIAP

Extracted new weight data from the 2025 Harmony and Symphony reports to support ongoing analysis and model refinement.

Resolved deployment issues for the Stability Agent’s regression model and am finalizing its integration.

Reza:

MIAP

Completed tuning of propulsion and hull degradation models for the entire fleet as the first step in fuel-forecast model performance optimization.

Started tuning models for the Service Power area as the second step; completed BY and AX so far.

Began data ingestion for legal models; next steps are feature recreation and modeling.

Mahshad:

MIAP

Optimized deployment, resolved the Gorubi license issue, and addressed model problems (for example, the model was not assigning a port to every day for all ships, creating gaps).

Identified a potential savings opportunity in the Anthem HVAC system; investigation is ongoing.

Will:

MIAP

FACTs Speed Fuel Curves:

Completed base and dynamic model feature engineering.

Added Port End DTM to the FACTs ETL.

Fixed issues with LNG ship MGO-equivalent mass flow rate calculation in power plant features.

Created AT, IC, and ST overall and individual MGO-equivalent models for fuel forecasting.

F1.0 Fuel Forecast:

Completed IC and AT fuel curves using FAT tests; currently improving these curves using MGO-equivalent models.

Brendan:

MIAP

Evaluated multiple model architectures for ALS compressor power prediction.

Created the final ALS compressor power model using gradient boosting with a monotonic constraint.

Incorporated the ALS compressor power training loop into the existing propulsion workflow in Databricks.

Arya:

MIAP

Worked on making chiller analytics processable in parallel by ship.

Added Azipod tags for IC and ST.

Created documentation for adding tags from Valmet software, the order of deployment for a new ship, and how to resolve tag-mapping issues.

Ram:

MIAP

Updated the existing crosser flow to support the new CSV format.

Fixed issues in the autoloader and backfilled all affected files.

Stabilized the QA ETL workflow by identifying the root cause and pushing changes to the QA branch.

Ayon Ghosh

Win on Waste

Update the code and test to reflect the new 3rd party API

Log entire JSON package into Volume

Pilot creating a moving average pipeline for schooner bar

Worked with Power BI team in FPMS to build reports for the Manilla team

**Erick Alfaro:**

Project Axiom: Overview

Project Axiom refers to a set of capabilities designed to be applied across various datasets such as Medallia Survey responses, Guest Logs, call center transcripts, call center IVR survey data, Qualtrics, etc. The core capabilities include: (1) Meta data extraction which is the process of converting unstructured data into structured data. (2) Reporting capabilities which encompass email alerts, web applications, dashboards, etc. (3) Modeling efforts include identifying NPS Drivers, setting targets, clustering text embeddings, etc.

**Erick Alfaro:**

Project Axiom: **Project Updates**

Met with Product teams (Justin, Pamela) to identify new use cases that could be encompassed under Project Axiom including:

(1) transcription of recorded Focus Group discussions

(2) indexing and generating meta data of images into vector store to allow business users to find images quickly

CEL Consumer Insights sent an email documenting several new collaboration opportunities.

**Erick Alfaro:**

Project Axiom: **Meta Data Extraction**

The Medallia survey has +40 questions of which about ~25 are numeric (0-10) questions and ~15 open ended questions. We currently fit the 15 open ended questions into 39 topic areas. However the business has asked to create new topic areas that match the 25 numeric fields. For example "Staffs ability to resolve issues" is a numeric field and the business wants us to label Medallia comments with these topics in addition to the 39 topic areas.

Initial Contact center IVR transcript work has been prepped for stakeholder review. Additional work is on hold until January to allow the team to focus on Medallia Divisions specific reports.

**Erick Alfaro:**

Project Axiom: **Reporting**

Medallia Divisions reports are different from existing Medallia emails reports due to the topics for Divisions being tied back directly to the Medallia 1-10 survey questions. This will allow the business to match 1-10 scores to commentary.

Divisions Templates will be completed by end of this month and presented to business by mid December.

Additionally the team is working a weekly fleet detractor report to be delivered by end of month.

InfoSec granted access to write to the team Sharepoint via the AlphaPlatform package. This allows us to save our Axiom reports directly to sharepoint in addition to sending via Email.

**Reporting**

The team is working on integrating the Drivers dashboard into the Axiom webapp.

**Erick Alfaro**** & Cristian**

PCP **MyCruise**** Recommender**

**Project Updates**

Continuing to work with platform team to integrate the federated lakehouse the recommender which is a core requirement to deliver calendar recommendations via the MyCruise API.

Michelle

Revenue Management: CEL

**CEL | Category-Gapping 3.0**

Anastasia wants us to have a turnaround on the POC of the model in a couple of weeks to determine feasibility of the multi-class approach. Going to start out with double bookings on a far out sailing where availability will not impact trade up percentages to try to remove additional confounds that may impact modeling accuracy.

Met with business on **11/12/25** to review current strategy and future plan with Anastasia and team.

**Key Decision:** Move away from trade-up approach and begin building a **multiclass model**.

**Planned Steps:**

Create normalized price features and conduct EDA to confirm expected trends.

Build **EBM** (Explainable Boosting Machine), considering outliers, feature interactions, and new itinerary features.

Simplify model for quick integration into optimization.

Use **Greedy Search** or Bayesian approach for optimization.

Anastasia requested **sample predictions** from the initial model to assess improvement vs trade-up approach.

Finalized historical LAFS data with dimensions: **ship-class, cat-class, ****rdss****, WTS bin, currency code, month** (booked position was too granular previously).

** Celebrity 3.0 Model Rebuild**

Normalized prices ✅

Building EBM (will become separate ticket; ~1 week).

Greedy search optimization (2+ weeks; separate ticket).

Optimization approach will replace LP with greedy/Bayesian due to EBM constraints.

**Completed**

Normalization of new dataset prices.

Lamis

RCI Revenue Management: **Track Optimization**

Lamis is likely to release RCI track optimization using tying to the latest SPI scores. I have some concerns here with that approach since we are revisiting the scoring model. Celebrity is also working through track optimization but they are wanting considerable changes to what has been done on RCI. I am fundamentally ok with this but they should be discussed as a group and programmed in a way that makes maintenance simple. We should try to avoid a PRE vs PRE lite scenario if possible.

Finalized **Revenue Lift calculation** comparing optimal track vs business track 0:

Ran inverse demand model to predict prices for business track 0 targets.

Adjusted booked_position feature based on biz track 0 weekly build.

Incorporated Bayesian-smoothed residuals for fair comparison.

Observed **~12% revenue increase** when optimal tracks were targeted.

Addressed gaps caused by new RCI policies for group vs FIT cabin allocation:

Shifted focus from cumulative bookings to **booked position (percent build)** for better comparability.

Eliminated need to convert track pax build to bookings.

**Optimization Model Tweaks**:

Previously enforced starting point at 80 WTS; now:

Start optimal tracks at 0 bookings.

Max WTS aligns with business track 0.

Worked on **two presentations** for stakeholder teams to review progress.

Compared optimal tracks against both **track 0** and **latest track**:

Latest track lacks historical data → business suggested filling historical values using latest track.

Issue: cumulative bookings exceed capacity → scaling applied to align with capacity for accurate revenue lift calculations.

**Other Tickets**

Preparing presentation for RCI team next Friday to finalize deliverables.

Quantify allocated sailing (in progress).

Scale optimization + refactor logic (merged scope; may exceed 5 points).

**Deferred**

Pricing optimization for Celebrity and minor meta products for Royal (likely December).

Lekha

CEL Revenue Management

**CEL | Validating the price changes for major ****metas**** with new elasticities**

**Deliverables Completed**

Presented latest **price-change recommendations for major ****metas** to Anastasia.

Walked through **sailing-level examples** to show new recommendations are less extreme than current changes.

Demonstrated **upgraded elasticity model reduces error** across major metas vs. current model.

Compared **feature importance** between current and upgraded models.

Lekha

CEL Revenue Management

**CEL | Validating the price changes for major ****metas**** with new elasticities**

**Next Steps (Based on Feedback)**

For **minor ****metas**:

Create **separate models for Asia and Australia** (similar to major metas) where data supports.

Consolidate remaining minor metas into a **single model named “BRAND”** after list finalization.

After minor metas finalized:

Generate **output file for all ****metas**.

Once **celebrity team validates**, move model to **production**.=

**Quick fix to include minor ****metas**** in elasticity model for phase 1 release**

**Enhancements**: Added **minor ****metas** for Asia and Australia into the elasticity model.

Developed a **brand-level model** for all other minor metas.

**Backtesting**** Results**: **Australia model** and **brand-level model**: Acceptable performance with **median absolute error below 40–50%**.

**Asia model**: Poor performance with **median APE of 70–80% across all splits**.

**Next Steps**: Investigate Asia model issues.

Combine Asia meta with another **meta_product_code** that shows similar behavior to improve accuracy.

Lekha is working on getting the minor metas in a spot so we can launch the updated model. Once that is in place we need to validate her DART approach to ensure there is no target leakage. The error reduction seems too good to be true. That will be a staggered release so that we can monitor marginal contributions from both the improved model and the DART release. A more robust minor meta product plan to follow.

Aagam

RCI Revenue Management

**RCI | CEL | PRE Logic | NOV**

**Nov 6, 2025**

Tweaked codebase based on stakeholder feedback.

Switched to **daily snapshot table** for capturing bookings.

Completed **price change analysis**; next step: prepare presentation.

**Nov 13, 2025**

Integrated **updated CEL Elasticity model** into analysis.

Discovered bug excluding ~70% of sailings; traced to RCI elasticity output.

Fixed issue and reintegrated corrected data successfully.

BUG

Identified a **bug in the RCI elasticity model** that caused ~70% of sailings to drop from analysis.

Root cause: **null prices for VPS LAF**, which led to predicted demand = 0 for those sailings.

Atefeh

CEL Revenue management

**CEL | Price Change Logic | Testing different ****Norm_Floor**** values**

Atefeh worked through the variable normalization for the price change calculation and it has been reviewed and approved by the business. This is ready for release. A code review with her may be beneficial before pushing to prod to ensure QC. I've made Lekha aware of Atefeh's work here, and warned of potential merge conflicts, but I would not be surprised if she runs into one here.

**Experimentation**: Tested different damping levels (Norm_Floor) in the variable-norm equation and shared findings with CEL team. **Comparison Analysis**: Compared price change distributions: Measured % of price changes within ±5% for:

Current model (constant norm = 5)

Variable-norm model with norm_floor = 8

**Outcome**: CEL team decided to adopt **variable norm** with floor_norm = 8. **Deliverable**: Generated final PRE output file for CEL review. **Next Step**: Integrate changes into **production code**.

**CEL Price Change Logic**

Implemented **variance-preserving adjustment** for negative or zero proj_pax_build and track_pax_build values:

Instead of replacing with a constant (0.1), calculate an offset to lift projected build above zero and apply the same offset to both values.

**Impact:**

Maintains proportional variance between proj_pax_build and track_pax_build.

Prevents divide-by-zero errors.

Ensures consistent price and elasticity calculations across all groups.

Ignacio & Kevin

PCP Pricing Automation: Writeback Testing Capability

Yassine and product have still not greenlit the release that the digital engineering team pushed. Viktor and Gang to follow up. All dev work is completed but its blocking any use of the tool at the moment.

Ignacio

PCP Pricing Automation: **Expanded OBR Promo Extraction for PCP2 Mass Promos**

Enhanced extraction logic to include **missing conditions** (Groups & Sales Application) for accurate promo eligibility at customer level.

Added support for **fixed discount promos** (“dollars off”) alongside percentage discounts.

**Debugged Complex Edge Cases** Investigated and resolved failures in **Group condition** handling:

Nested subgroups.

Multiple repeated definitionIds requiring separate treatment.

**Improved Robustness** Updated logic to handle **both inclusion & exclusion conditions** for:

Ship code.

Cabin class.

Loyalty.

Casino conditions.

Kartik

Loyalty

**Kartik Ullal**

**Current Work**

**Points Choice Pilot**

Nearly complete; adding points for suites.

**Category Mapping for Conversion Rates**

Almost done; minor updates pending.

- Should be straightforward but needs to match the logic used elsewhere. Most similar APD for celebrity average APD for SSC.

- Tier Impacts for RCI/CEL

- Kartik is aware of the tier impact work based on cross-brand leakage (i.e. how many guests right now prefer sailing multi-branded without any incentive) and the methodology used to arrive at those leaked sailings. It is all based on whether a guest has a preference for one brand over another. Preference is first determined by higher tier rank (prior to status match). If a guest is the same rank in both brands, we then determine preference by which brand they are closer to reaching the next tier.

- Dhanita's team has done work to determine tier growth rates and projections through 2030. This was simply carrying recent tier growth year over year. They should apply the additional leakage rate to that growth rate. The loyalty teams expected CEL work as well from Dhanita's teams but this is yet to be completed.

**Tier Impacts for SSC**

Blocked by SilverSea data issue; investigating.

- Kartik is attempting to do a similar Leakage analysis for SSC. The data is quite difficult here. David Ortiz on DE gave some tables to use to match RCI and CEL customers but there are issues with the mappings, where many SSC guests do not have an xref. Kartik is following up on this with SSC and collaborating with David on this.

**Credit Card Acquisition Impact**

Expected completion by tomorrow.

**Deferred**

AB testing and loyalty analysis pushed to December.

Jesse

SSC Revenue management

**SSC | PRE | Manage and Track PRE and A/B Test Progress**

**2025/11/6:**
Data Engineering claims they have fixed issues with the table. Jesse will confirm these corrections ASAP.

**2025/11/4 Meeting with Data Engineering:**
Agreed actions for ssc_price_change_history table:

**Investigate null values** in price_change_source field (determine if manual or pre).

**Correct null values** in current and future iterations.

**Perform QA** to ensure reliability (remove duplicates, validate price_dates, etc.).

**Update Data Science** on origin of null values by **Friday, Nov 7**.

**Provide realistic timeline** for completing this work.

Jesse

SSC Revenue management

**AB testing and track variance**

**Completed (11/3/2025):**

Delivered:

Cleaned AB test data for one month.

Produced definitive PRE performance results with respect to track.

Future Work:

Report findings and incorporate into CAR.

Blockers: None.

**Additional Note (3:14 PM):**

Encountered major difficulties with SSC PRE price recommendation tables (developed by SSC).

Performed temporary data cleaning to enable proper EDA.

Permanent fixes are being addressed through other tickets with Data Engineering.

Kartik & Kevin

PCP Pricing Automation

*Gang Wang requested that a Data Scientist work on pricing for products of the new Royal Beach Club or RBC (in Nassau). Kartik is being assigned to this project.

*Kartik got initial queries from Gaby for RBC. He is starting dev work there by getting familiar with the data. He has already met with the OBR teams and is awaiting full marching orders. He may need help getting the initial EDA started and power analysis.

*Classic cold start problem, but the team thinks there may be enough sailings in the prime booking window to get some initial insights. Almost everything on RBC is short caribbean so relatively low bookings.

Evan & Kevin

RCI Revenue management: SPI Updates

Nick pushed the meeting to next week. Evan is on the right track of improving the scoring model and is trying some new ideas. He needs to be careful to not introduce features with sailing management factors into the scoring model. He's working with Eddie on this regularly.

Atefeh & Eddie

RCI Revenue Management: Promotions

*The goal of this work is to account for the actual price paid accounting for always-on promotions and tactical promotions. The work ultimately may have us create rules to decide whether to adjust promotions vs base-price.

*I think Atefeh is doing a good job here and is getting some good guidance from Eddie. Shes currently working through categorizing all of the promotions and then working through the analysis. Should check in with Anastasia if she wants this done for Cel as well. If so, it will be a substantial lift since the promos are all different and there are many more promos for CEL than RCI.

Glen-Erik & Alejandro

PROPEL

XCEL deployed to Propel dev environment

Dynamic control population pilot for AT and CS running in production

Now extending offers for HHG and Art offers.

ability to do gender specific offers, like spa wellness offers for women.

Eswar & Glen-Erik

RMA

Validation Workflow: Rather than attaching the validation workflow to the end of all workflows, changed the strategy to use a file-based trigger that initiates the validation workflow.

Modified the code to read the job_id from the file dropped into the volumes directory.

Also considering clearing the volume that is used exclusively for file drops, since it serves only to trigger the validation workflow and does not need to store data.

Providing ML support to handle pull requests and to debug issues.

Re-deploying the updated feature store update workflow.

Provided refresh times for certain feature store tables migrated to DE, enabling the governance team to refresh them on a regular schedule.

Javier

Automated Code Review

Standardized and refined the Databricks bundle structure in databricks.yml, organizing variables, consolidating permissions, and introducing environment-specific configurations for dev, QA, and production.

Resolved SP issues by diagnosing missing Access Control List, defining the correct API patches, and validating entitlements.

Applying this improved framework to RMA projects (in progress)

Refactoring the TAP-dbricks codebase to eliminate duplicate functions prior to enabling the duplicate function check (in progress)
