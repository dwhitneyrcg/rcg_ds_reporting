**Proud**

- **Revenue Management**** (RCI)****:** DS Team delivered substantial enhancements to the SPI Model (i.e. accounting for Holidays and completed a deep-dive analysis to eliminate outliers) and Pricing Automation (to ensure we are ready when the *discount pricing schedule is retired **next week).** MLOPs team working on group gapping framework + data monitoring tools, while DS Team is w**orking on additional enhancements to the SPI Model (to better account for Sailing Management factors and smaller products like Canals/Repos) and General Automation (e.g. Berthing Fixes and develop automation for Accessible Adjoining Cabins).*

- **Marine Operations: **DS Team gained support for Fuel Forecasting CAR submission from Revenue Planning, ESG, and Platform Engineering teams and completed ML HVAC tag mapping. *N**ext steps to gain **IT’s** support prior to **Fuel Forecasting CAR **submission** and actively adapting HVAC chiller + AHU performance monitoring models for Millenium-class ships.  *

- **E-Commerce: **DS team delivered new enhancements for CDP Customer Targeting dashboards (i.e. metrics for determining optimal audience size based on model lift metrics and segmenting audiences based on emailable-only customers). *Validating** audience sizing calculator and newest Epsilon spend + demographics datasets.*

- **Loyalty:** DS Team presented an updated analytics readout on the forward-looking Loyalty Simulator to the Loyalty leadership team with positive feedback. *Team highlighted current accomplishments and ongoing work to better captured pricing inflation, updating tiers frequently, and forecasting future guest spend that captures pricing premiums for different products (e.g. brands, meta-product, upper/lower cabin categories).*

- **NPS Target Setting (CEL):** Completed substantial enhancements to our NPS Target setting tool pipeline (e.g. sped-up processing time, automated parameter tuning, and revamped Power BI Dashboard). To share results broadly with Revenue Planning and CEL Onboard/Marketing teams. *Tool will help hotel operations team more accurately set NPS and other associated-operational targets based on AI forecasts. *

- **WoW:** DS Team provided full-time support this week for the onboard ship visit with Specialty Dining chefs to introduce WoW demand forecasts. *Team continu**es **to work on Main Dining Room pipeline and beginning work for a Data Validation Tool to ensure data quality for forecasting inputs.*

- **PROPEL:** MLOps Team completed Workflow + Alerting framework to help teams ensure targeted offers are shared with shipboard teams at the right team. Team is nearing completion for a back-up framework that will enable offers to be pre-generated (in case ship is unable to communicate with shoreside systems).

**Concerned**

**None**

**Excited**

- **Revenue Management (CEL):** DS Team supporting CEL’s AB Testing (GTY-Lead AB Test just started and completed analyzing T4 Test results) and delivered a SPI PoC adapted for CEL. *Beg**inning** work on Track Optimization **+ Pricing Recommendations Enhancements using **Sailing Baskets and Mandatory Occupancy Inventory Automation.*

- **Revenue Management (SSC):** DS Team completed gathering business feedback for optimizing PoC Pricing Recommendations and Business Rules. *Working on integrating business feedback into future Pricing Recommendations and completing initial Pricing Elasticity model. *

- **Supply Chain:** DS Team actively working on enhancing demand forecasting models and model performance modeling analytics for HF&B (RCI/CEL/SCC) and Uniform Modeling (RCI/CEL). *Work has restarted for a 2024-22025 CAR Submission for HF&B (SCC) + Medical. *

- **Medallia GenAI Pilot Use-case: **DS Team optimizing LLM-based approach for text summarization capabilities with onboard revenue teams (e.g. refining embeddings and optimizing utterances). *Expecting delivery of the Topic Summarization pilot by end-of-year with a pilot delivered for **crew **testing in early November.*

- **PCP “****MyCruise****” Product Recommendations:** DS Team working with Platform Engineering team to develop a REST API endpoint to serve as a middle-layer to serve product recommendations with Digital. *Team also met with E-Commerce **& Digital Engineering **teams** again** to align on a new engagement to provide targeted e-mails with product recommendations.*

- **RCG-GPT:** MLOps team actively debugging code-blocker for RCG-GPT. *Once this is completed, team will release two versions of ChatGPT (one for business users that includes the code blocker and a second version for software developers without the code blocker).*

CEL
Recently Completed
GTY-Lead AB Test In Progress
T4 Test, Analysis
SPI Proof of Concept
In Progress
Elasticity Model Addt’l Granularities (EUROPE, CARIB)
Choice Model Feature Table Construction
MTRB adoption for CEL
PRE Basket Integration
Mandatory Occupancy
To Begin
APD Track
GTY-Lead Trade-Up Models
SPI CEL-specific Rework

RCI
Recently Completed
SPI Holidays Factors
SPI Outliers Deep-Dive
PRE Discount Price Fixes (Continued)
In Progress
SPI Sailing Management Factors
SPI Minor Metas
Berthing Fixes, Accessible Cabins
To Begin
Additional Elasticity Model Upgrades (MLFlow, Re-Training, Metrics)
Data-Driven Mandatory Occupancy

SSC
Recently Completed
PRE Business Feedback Round 2 + Story Generation
Business Rule Refinement of PRE Rules (after Review)
In Progress
Fit initial regressions for Elasticity Models by Area + Additional Granularities
Business Rule Updates to PRE
To Begin
Dashboards and Reporting for PRE Recommendations
BPO: P2P vs D2D (Tracks or TAP?)
BPO: Category Gapping
BPO: ESS Fare Class Optimization

OBR
Recently Completed
Perfect Day Cabanas elasticity by Cabana Type
Optimized APD recommendations by Cabana Type
In Progress
Cabana Dynamic Pricing Recommendations (Recent Trends)
To Begin
Drink Package Price Optimization

Marine

Completed ML class HVAC tag mapping and ran chiller dynamic model. Working updating AHU models to ensure compatability with ML class.

Stakeholder meetings with Nick Rose and Elizabeth Oats on Fuel Forecast and Digital Twin Model CAR. Gained support of the stakeholders and pending CAR memo share with Martha prior to submission

Prepared MIAP dynamic model handover notebook from Kevin Diaz to Mert Ersoz.

Presented shakeholder demo for GMO App MIAP data analytics visuals.

Preperating future dataset for SFOC modelling

**Update for E-Commerce**

Improve dashboard:

**Added global charts of metrics in audience calculator.**  They help to select "best" audience size by better understanding of model performance (dev).

**Added toggle button to prediction reports** to be able to switch between reports for consumers that are emailable only (dev)

**Pending Tasks**

QA last week changes with Michelle, and move to production

Validate newest epsilon data (txspend and demographics)

**Update for Loyalty**

Ran of the guest simulation code and manual validation of results.

**Update for GSCBP:**

*Hotel Food & Beverage:*

·       Refactor Code for ESG Mapping, EU Mapping, Discontinued Products, Aggregating Weekly Consumption to Monthly Consumption for RCI / CEL

·       Created Silversea code to analyze model performance over time and wrangle data in preparation to build Challenger Models to the AI model for Silversea similar to what we’ve already done for RCI / CEL

·       Continued work on productionizing Silversea pipeline to automate the Silversea demand models on a weekly basis

*Uniform Modeling*

Aggregating actuals values to the demand forecast pivoted view to be able to analyze and compare better

Joined the original consumption data in the model to the 167 products given to us with further information. A challenger model to be done with the aggregated features on these 167 products.

Automating the uniform model process by cleaning the code, such as, not having any hardcoded dates and such, etc.

**Loyalty**

·       Kevin is in process of knowledge transferring existing work from Carlos, Erick and Mireille to take ownership of and continue progress going forward

Loyalty

- Prepared read out to provide initial perspective on Forecasted Tier 5 counts

- Working to bring Kevin up to speed on Loyalty backend

GS Bot

- Updated GS Chat GPT model to GPT-4o-mini due to GPT 3.5 being deprecated

Medallia COE

- Working with stakeholder to identify optimal utterances to deliver best in class topic classification model

- Tested Various embedding Models to find the best embeddings model given our domain. Initial results show

- To enable the LLM to provide generalized summaries we worked to replace restaurant names with word "restaurant" and working toward replacing ship names as well.

Liveperson

- Met with LivePerson stakeholder to discuss modifications to existing logic

MyCruise Recommendations

- Need to Work with Utkarsh to create a REST API endpoint as a middle layer between Databricks and MyCruise

Emails Recommendations

- Reusing the MyCruise Popular/Trending logic we will work to integrate Inventory data

- Working with Digital (Lance Thomas) to enrich product details that will be shared with Emails team

Target Setting

- Parallel processing of model training using Spark - saving time / faster iterations

- Automated model param tuning before training

- Revamped PowerBI dashboard with new model results

- Will be presenting PowerBI dashboard to Craig Hardeman, Elizabeth Oates, Evan Lucash, Maria Poznyakova as per requests from the business.

WoW

- Data Validation tool is ~70% complete

- MDR is 40 % complete

- This week the WoW team served in shoreside support capacity for shipboard teams

- sharing analytics, giving explanations, generating fresh data, creating different views of results on demand

Consumer Outreach

- Working to retrain BKTOCX model

Deployment

- Cihan working with Deployment team to set up data sharing and convert raw notebook into API

**PROPEL:**

Alejandro if moving quickly within his first 3 weeks here pushing forward multiple big changes to the solution:

**Alert framework: **Alert test complete, overcame all the IT access and setup hurdles. Now ready to start building the alert framework.

**Backup “in advance” feature: **Successful test in the development environment, with pending improvements to manage control group creation when a new sailing is within the in_advance window.

**Workflow and Alert schedule automation: **Created an output table of what the schedule would be with the new solution based on the port at which the ship is each day (or last was if at sea). Logic to be validated with business and then implemented so offer schedules are automatically maintained.

**Photon de-escalation: **Removal of photon execution in development jobs and currently evaluating the possibility of removing it from production jobs as well. Costs are high due to photon use.

**RMA:**

**Group Gapping Framework (Vikas): **testing outputs with new changes to the code. Will decide if we need to temporarily roll back code in QA or move forward to production tomorrow.

**Unity Catalog conversion (Eswar, Satheesh): **created Unity Catalog conversion tracker based on an automated ADF crawler tool built by Eswar that extracts all input tables (existing and missing from unity catalog) as well as all the queries using those tables comparing them to unity catalog. Data Engineering (Monica, Irmina & Srini K) are working to migrate the missing tables, divide work with Eswar and Satheesh to help migrate and optimize the queries.

**RCGGPT:**

**Code blocker (Eswar): **Troubleshooting why code blocker isn't working so that we can have two versions of RCGGPT, one with the code blocker and one without.

**HIRING:**

**FTE:** Wrote new JD’s for Senior and Lead positions and had the req’s opened by HR. No new applicants.

**Contractors: **reviewed Jose’s test results and interviewed Javier. Javier seems like a better fit than Jose but most of his experience is in AWS not Azure so want to see how he does on the test to better gauge his critical thinking and tech skills to see if he would hit the ground running and learn the new tech quickly.
