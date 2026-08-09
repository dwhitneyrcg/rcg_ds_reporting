Erick

**Axiom: Medallia ****Meta Data Extraction**

Following the last few weeks of updates on the new Data Extraction framework, we are working to implement the Native Batch Processing capability. OpenAI allows for Batch Processing of data using the slower bulk offline processing - with the added benefit that it comes at a 50% discount. The idea is that we can slash the cost of scoring historical data as opposed to using the online real time API endpoint.

On the contact center front, the team is doing some early EDA on contact center IVR survey data to understand the scope of work. Delivery of Axiom summarization processing is slated for January 2026.

Erick

**Axiom: Medallia**** ****Reporting**

Held a +20 person workshop to showcase the new shorex tour specific AI summaries (using Medallia consumer feedback). The AI summaries are in partnership with Gangs team. Following the short workshop, several new reports were requested and have been backlogged.

Working with Eliana and CEL consumer insights team we were finally able to access Qualtrics survey data directly. The survey data contains thousands of wide ranging consumer surveys that have historically only been analyzed manually. On Monday we will also share this work with Kristina Murray and Justin Birzon.

InfoSec granted access to write to the team Sharepoint via the AlphaPlatform package. This allows us to save our Axiom reports directly to sharepoint in addition to sending via Email.

Erick

**MyCruise**** Recommender**

Worked with platform to create a new federated lakehouse connection to our postgres instance. This should allow us to resolve our issue with the Azure Postgresql firewall blocking the model serving instance.

The team is finalizing the migration of all production processes to prod workspaces.

Discussed the idea to use Medallia tour code level feedback from guests as a feature to improve the product recommendations.

Mert

MIAP

Added the Digital Twin Python package and its methods to the MIAP API to allow digital twin models to be shared with third parties such as GMO, Revenue Planning, and Deployment.

Implemented Server-Sent Events (SSE)-based real-time streaming capabilities in the enhanced MIAP API.

Met with Risk Management and the Corporate Strategy team and began drafting the Project TIDE Phase I CAR memo (Claims Management).

Successfully negotiated with Nacos (automation system provider) to reduce cybersecurity upgrade costs for the Silver Muse, Moon, and Dawn machinery automation systems, and secured MIAP's OPC UA servers free of charge on Muse (over $100K cost savings). Received approval from SVP Brian Soerensen to fund the Silver Muse upgrade for this month’s drydock. This aligns with Bert's request to add MIAP solutions to the Silversea fleet.

Coordinated the new AMOS migration to the Alpha platform with IT, Data Engineering, and GMO teams, a requirement for supply chain optimization in marine.

Coordinating Koja cabin automation system data integration into MIAP on Quantum Class to provide cabin occupancy and AC set points. This will help detect fake energy-saving key cards by comparing occupancy with guest shore status and enable hotel ops to remove fraudulent cards—yielding significant cost-saving potential—and will improve decision-making across the company.

Arya

MIAP

Finished adding UT to all pipelines except service power; waiting for the duplication error to be resolved before pushing.

Currently working on tag mapping for Icon and Star azipods and lube oil. After tag mapping is complete, I will begin implementing a monitoring algorithm to track azipod performance.

Mehdi

MIAP

Working on the stability agent and continuing to add the regression tool to the agent.

Trying multiple approaches to get the regressor tool working.

Mahshad

MIAP

Followed up with SM regarding the TCV valve sensor issue and machinery ventilation setpoints; they will replace some sensors, so we expect to see savings afterward.

Implemented the optimization using Gurobi and resolved integration issues.

Held several meetings with the deployment team to coordinate the optimization rollout.

Defined next week’s hackathon topic, assigned tasks to teammates, and prepared the hackathon presentation.

Created a deployment presentation to share results with the team.

Brendan

MIAP

Identified the root cause of a cost spike in the MIAP production workspace: significant data duplication causing extra compute time.

Troubleshot the propulsion dynamic model to fix ALS On/Off models that were returning the same prediction (in progress).

Worked with Mert to create a new design for the ALS compressor power model; currently developing (in progress).

Reza

MIAP

Improved model accuracy in the propulsion area (new model vs. old model).

Debugged issues in related areas such as HVAC, hotel, and machinery.

Attempted to resolve a duplication issue in the common feature table. Although the issue was resolved there, duplicates still persist in the service power area; working with the team to troubleshoot the workflow.

Will

MIAP

Performed root cause analysis on a hotel analytics failure.

Added a UTC conversion factor to the FACTs table.

Refactored date columns to timestamps and postfixed them with "UTC_DTM".

Completed FACTs speed-fuel model data engineering.

Completed outlier removal for FACTs speed-fuel model data.

Renamed all columns related to methane from "METH" to "MeOH".

Fixed an issue with XC tag mapping that caused the MIAP ETL to fail.

Collaborated with Energy Management to deliver new fuel curves for Forecast 1.0.

Added the missing ship Silver Spirit to the 2025 SSC fuel curves.

Updated Factory Acceptance Test models to include "MDO" fuel-type data by converting values using the IFO conversion factor.

Kevin

RCI Revenue Management Automation: 
PRE recommendations and some TAP projects were paused for the week. A planned upgrade to the Oracle-Databricks connectors was released that truncated all floating point numbers to whole numbers, including track and currency exchange for all Oracle data pulls. The error was discovered by an analyst on the revenue product team when evaluating AUD PRE that runs over the weekend. Data Engineering reacted quickly and corrected the data transfered to Alpha in a couple of days. A more proactive approach and stronger QA should have prevented the issue.

Kevin

RCI Revenue Management Automation:
PRE price raises are being capped or auto-paused, depending on sail date, during Cyber sales. There is concern from the business on aggressive targets and the current demand environment. Price lowers remain unaffected at this time. We are flagging these pauses to remove from KPIs as they are likely to have a negative effect on absolute variance to track, our main KPI for PRE performance. This change will be in effect through mid-December and will be re-evaluated for Wave depending on our booked position at the time.

Kevin

RCI Revenue Management Automation:
A refactored SPI was presented to the business strategy teams this week addressing concerns with overfitting, over-normalization, and target leakage with the model previously designed. There is further feature engineering and work needed to finalize the scoring model, but this is a substantial step in the right direction.

Kevin 
Loyalty:
Presented updated Tier conversion rates and tier impacts to loyalty VPs and Kara Wallace. Kara was supportive of the strategy, but requested a more granular view on category points mapping and tier impacts. Kartik delivered the category points mapping and the tier impacts will be shared during next weeks steering committee meeting. There are delays on SSC impacts because the data is maintained separately and is more difficult to use for cross-brand sailing behavior.

Carlos

E-COMMERCE
• Implemented new training approach for the sailing_horizon model based on stakeholder feedback and intended downstream use cases.
• Completed exploratory data analysis (EDA) on journey_stage model input data (provided by Anisa).
• Continued refactoring marketing model code:
– Extracted all common configurations and hard-coded values into a shared configuration file
– Added comprehensive doc-strings to every function for improved maintainability

Carlos
LOYALTY
• Conducted research on multi-task model architectures to predict metaproduct, cabin_class and sailing_propensity simultaneously for the sailing-generator use case.

Ben & Camila
SUPPLY CHAIN
• Resolved silent-failure in Silversea pipeline by correcting an improperly set environment variable.
• Next-generation RCI/CCI HF&B model:
– Built initial version on one back-tested month, reducing MdAPE from 17.6% to 15.1% (14.2% error reduction) – lowest ever recorded for a single month
– Six-month backtests in progress; completion expected next week to validate consistency
• Uniforms RCI/CCI V6 (with crew count):
– Discovered crew table max-date limitation (9/26) blocking adjusted-consumption calculations; escalated to Yan and Dom for data refresh
– Populated UOM column for Lauren/Fanny; awaiting item master file path from Yan for remaining product
• Uniform Order Creation: V1 and V5 completed; Uniform Par Level logic (using V5) completed; both pending Yan’s review
• SSC Uniforms pipeline: steps 1–4 (consumption adjustments, demand table adjustments, back-tested tables, archival table creation) completed; step 5 (challenger model back-tested tables for versions 1, 5, 6) initiated
• Medical Free-of-Charge Items logic:
– Defined monthly consumption = (beginning inventory + inbound orders – ending inventory) for “free-of-charge = yes” items
– Distributed monthly consumption evenly across weeks via ETL notebook, aligned to Monday of each week
– Integrating logic into all affected notebooks to prevent overwrite by POS-based consumption
• Finance Tool automation: added new ships, removed hard-coded “Utopia of the Seas” and static brand mappings
• SharePoint HF&B files: cleaned all nulls, replacing with zeros
• SSC Unhealthy Inventory Dashboard enhancements:
– Added transaction order counts column
– Added quantity received from PO column
– Added quantity received from warehouse column
– Recomputed unhealthy $ by multiplying unit cost by unhealthy quantity
• Warehouse Transfer Order → Region mapping: awaiting updated port-itinerary table from Emanuelle (DE) to resume
• Inbound order quantity refinement for RCI/CCI creation: pending correct table from DE (inconsistencies noted in two validations)
• HF&B & CocoCay demand file merging: ongoing development

Caleb
CUSTOMER LIFETIME VALUE (CLV)
• Released SOP and data dictionary for the new “clean pax-level” table, including:
– ETL pipeline flow, metadata definitions, VCAP validations
– Use cases, filters & SQL examples, joining instructions
– CLV methodologies, known caveats, sample table excerpts
• Validated DMA Optimization Tool outputs; addressed Cory/Joey’s concerns on booking-window and DMA proportions
• Confirmed booking-window differences are marginal at DMA level (Miami is an exception)
• In progress:
– Reworking “branded cruise experience” logic to align with authentic cruising behaviors
– Incorporating temporal cohort evolution in passenger segmentation and index recalculations

Ben
CONTACT CENTER
A. Conference & Stakeholder Engagement

• David presented ta AI Day at Contact Center Annual Leadership Conference overviewing our AI resources (Big Rocks vs Little Rocks, AI Ambassadors Program, GenAI CoE, AI Academy, and a detailed tutorial of Copilot Capabilities. Feedback was highly positive. 
• Ben Attended AI Day at Contact Center Annual Leadership Conference; engaged Cristy and Michele—received strong endorsement for AI initiatives

Mirielle

Contact Center: Lead Pipelines (BK2CX & OF2CX)
• Designed enhancement to include Agency ID in “EVENT_CODE” field:
– BK2CX: map “BNAGID” → EVENT_CODE
– OF2CX: map “BMAGID” → EVENT_CODE
• Coordinating testing with Siebel team; preparing for BK2CX production release

Mirielle

Contact Center: OFTOCX Lead Types
• Met with Augusto and Shan to identify sub-lead types in the SBOFRD (oftocx) table across 20 SFTP files
• Initiated: ETL process setup, data-loading workflow design, feature engineering pipelines, orchestration utilities

Mirielle

Contact Center: Workforce Planning – North America
• Completed investigation into September call-volume discrepancy (Databricks vs. Excel/Power BI); Jira ticket in place, tables under update by Antonio’s team
• Launched call-volume forecasting for four low-volume LOBs (CO_GROUPS_SALES, CO_GROUPS_SERVICE, GEM, CE_SALES):
– Multi-model orchestration (LightGBM, XGBoost, CatBoost, HistGradientBoosting)
– Configurable via models_to_run parameter
– Comprehensive comparison report (R², MAE, RMSE, MAPE) plus 4-panel metric visualizations and historical vs. forecast plots
• Pending Darren Andree’s access permissions to complete final model validation

Mirielle

Contact Center:
Workforce Planning – International & Casino App
• Project outline, sample data and initial interface design shared with Nico, Zed and Xavier
• App section for historical data display scoped (markets, LOB, date filters; call volume, AHT, abandon rate)
• Based on recent feedback, revised display hierarchy to group by region (International vs. Casino) with Royal/Celebrity as sub-groups

Cihan
PCP Pricing Automation
A. OBR Waterpark PRE (Gang Wang)
• Delivered feature-importance analysis using SHAP in stakeholder review with Ignacio
• Initiated optimization work: created week_bins for waterpark usage modeling
• Identified performance bottleneck in prd_gold view; engaged DE to persist it as a table for faster queries

Cihan

Digital Royal Community: Qualtrics Survey (Jaime Stoelar)
• Updated and delivered deployment notebook to stakeholders
• Ran topic-classification pipeline on sample data; benchmarked multiple GPT models for accuracy
• Added new survey topics per stakeholder request
• Implemented asyncazureopenai() to parallelize API calls, reducing end-to-end processing time
• Topic classifier now deployed and running in production

Cihan
Digital Royal Community: Guest Services Chatbot (Eunha Kim)
• Presented current live-agent escalation logic to stakeholders; captured requirements for three escalation types:
– Type 1: “Bot-not-wanted” (user explicitly requests “agent” or “help”)
– Type 2: Intentional (bot cannot execute task, e.g. issue new SeaPass card)
– Type 3: Bot failure (unrecognized query)
• Developing and integrating new escalation-flagging logic into the production pipeline
• Updating stakeholder data feed to populate Power BI dashboard with escalation metrics

Ayon

Win on Waste

Explored data, conducted tests, and initiated development to incorporate Transatlantic, charter, and repositioning voyages into the WOW forecast.

Developed Power BI reports for reporting on the most frequently asked questions by chefs to support the Manilla support team effectively.

Developed and integrated existing MDR pipline for repositioning, charter, and transatlantic voyage types

Implemented hotfixes to include voyage departure date in the cold start orchestrator, enabling grouping of guest counts and kids by voyage departure date to prevent duplicates in Couchbase.

Alejando

PROPEL

New categories supported by propel Engine: Art and HHG. Now offers can be created for products, product classes or the whole category.

Montecarlo simulation of +100 Campaign to review stability and overall behavior of new logic for dynamic control groups assignment

Eswar

CEL Revenue Management:

Applied Data Validation checks to TAP SUITES, testing in QA in-progress.

Production fixes TAP Combined, TAP price uploads, and TAP CEL cruisetours codebase

Deployed the modified workflows of TAP CEL cruise tours, feature store avail features updates workflows

Deployed new workflow TAP CEL GTY LEAD Bookings, which generates reports everyday
