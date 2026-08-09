**Proud****: **

**Marine Operations:** Team rapidly delivered an AI-clustering algorithm PoC to help deployment teams identify if ships can feasibly dock at a port terminal. *Highly positive feedback by **Captain** **Henrik Soerensen** **(AVP**, Fleet Captain).*

**Loyalty:** Implemented a Sail Nights-based simulator with a 2-year requalification models. *Next step will be to compare how a Sail Nights vs Spending-based approaches differ in rewarding/penalizing different consumers.** These insights with be shared with Nancy, Andrea, and Mike in the Loyalty Insights Meeting. *

**Revenue ****M****anagement (****SSC****):**** **Completed a Geospatial Analysis of SSC Sailing Itineraries to help cluster sailings into basket groups. *Presented clustering to the SSC Business Teams with positive feedback**. Team plans to use these basketed groups for constructing pricing elasticities for SSC Sailings. *

**Supply Chain: **Team delivered 40k new additional Demand Forecasts at a product-level for SSC (HF&B). *Team **continues to** actively refine the **SSC HF&B **demand forecast**s** and is working to deliver on new demand forecasts for Crew Uniforms**.*

* *

**Concerns:**

**Contact Center:*** *Booking* *conversion dropped significantly for CTI leads in 2024. After root cause analysis, team discovered that CTI Lead prioritization had inadvertently stopped at end of 2023. *T**eams are **actively **working towards reviving the CTI lead scoring.*

**Excited:**

**Fuel Forecasting CAR (Marine Operations)****:** Team met with Marine Finance & Decarbonization teams to align on a 2024 CAR submission for delivering an updated Fuel Forecasting Model with a proposed budget of $400K. *The CAR’s benefits include **$1M **in cost-avoidance (paying a** McKinsey advisory service **to advise on** fuel forecast**ing)** and **will improve Finance’s ability to forecast the >**$1B fuel budget.** The team will need to align with Chris Allen (VP of Deployment) before submitting a CAR.*

**Revenue Management**** (****RCI****)****:**** **Team completed PRE fixes (stale pricing, live pricing & mandatory occupancy fixes), development of an Oversell Optimization algorithm to be used in GTY-Replenishment automation, and roadmap planning for SPI. *Both SPI and Pricing Elasticities **will be **critical components of Track Optimization and Automation improvements for the 2024 RMA CAR.*

**Revenue Management**** (CEL)****: **Team completed code enhancements to CEL Pricing Elasticities & GTY Replenishment (first Inventory Automation project). *Team is working on additional elasticity model enhancements and analyzing T4 Testing Results.*

**Onboard Revenue: **Working with CEL Onboard Revenue to assist in setting 2025 NPS targets using AI modeling.

**Digital:** Made enhancements to the initial Product Recommendation Engine API based on feedback from Digital’s frontend engineering team. For evaluating the Guest-Services Bots, team has developed improved classifiers for ~700 specific topics to accurately identify guests’ intents. Team also finalized asks from the Digital team for PCP Pricing Automation.

**E-Commerce: **Conducted exploratory analysis on spend and watchlist/favorites data for calculating Booking Propensity & Spend Forecasts, which will be shared on a Streamlit App with the E-Commerce teams.

**ChatGPT Report:**

**https://oai.azure.com/portal/2fa3cf1b46d24f1ca5bba3c94580f2dd/chat**

You are an AI assistant that helps people summarize information. Please summarize accomplishments for each major area: Revenue Management, Contact Center, Loyalty, Onboard Revenue, E-Commerce, Marine Operations, and Supply Chain. Summaries should be 2-3 sentences maximum.

Output:

**Weekly Accomplishments Summary for Data Science Team**

**Deployment and Integration:**

**IoT Pipeline:** Deployed IoT pipeline on Celebrity Edge ship.

**Port Terminal Identification:** Successfully used KDtree algorithm to identify feasible port terminals for the fleet, aiding Fleet Captains in deployment decisions.

**Carbon Intensity Integration:** Progressed with integrating Silversea's Carbon Intensity rating calculations for the CII Dashboard.

**Energy and Performance Metrics:**

**Service Power Models:** Fixed bugs in service power models and baselines.

**MIAP KPIs:** Created energy KPIs tables accessible via REST API for GMO webapp, including metrics like Service Power Performance, Hull Performance, and more.

**Fuel Budget Forecasting:** Aligned with directors to proceed with the Fuel Forecast Model CAR submission, aiming to save $1M by improving the fuel budget forecast.

**Collaborations:**

**Global Intelligence Team:** Met to discuss using MIAP real-time Kafka data streams for custom map creation.

**Fuel Budget and Decarbonization Strategy:** Aligned on fuel forecast model with a $400K budget, pending VP approval.

**Revenue and Loyalty Initiatives:**

**Onboard Revenue:** Developing fleet-wide NPS targets for 2025, with two modeling approaches ready for review.

**Contact Center:** Extracted call topics back to 10/07/2023 and identified issues with CTI lead scoring and Oracle data access.

**Loyalty Models:** Implemented initial Sail Nights model; next step is merging with the Spend-based model.

**Digital Product Recommendations:** Enhanced API to accept SAILING_ID parameter, and improved GS Bot topic classifier.

**Modeling and Analytics:**

**WoW Modeling:** Updated MDR modeling approach to better account for inconsistent themed nights.

**Elasticity Models:** Deployed retrained elasticity code, continued analysis for T4 test results, and planned additional granularities for elasticity models.

**Technical Progress and Issues:**

**RCGGPT Bug:** Identified a bug via prompt injection QA.

**Contact Center Issues:** Resolved performance drops and data access issues.

**Other Initiatives:**

**GTY-Replenishment and Lead Tests:** Completed code construction and initial tests.

**Track Optimization:** Brainstormed and planned sessions.

**Demand Forecasting:** Delivered new demand forecasts, updated RCI/CEL code, and continued work on the crew uniforms demand model.

**Pending Tasks:**

**Watchlist/Favorites Data Integration:** Continue integrating and implementing front-end models.

**Future Ship Deployment:** Fixed spend and occupancy metrics and generated new deployment scenarios.

**Global Supply Chain Planning:** Delivered new demand forecasts and updated demand models with improved accuracy metrics.

This summary highlights the key achievements and ongoing efforts of the Data Science team over the past week, showcasing their contributions to various projects and collaborations across different business areas.

Deployed Celebrity Edge shipboard IoT pipeline.

Highly successful results with identification of port terminals ships can dock across the fleet using KDtree algorithm as requested by Fleet Captains to answer deployment feasibility questions.

Bug fixes to service power models and baselines.

Progress with MIAP all energy KPIs table creation via REST API for GMO webapp consumption (Service Power Performance, Hull Performance, Voyage Performance, Power Plant Performance, Fuel Budget Variance, Carbon Intensity Rating)

Met with Global Intelligence team on using MIAP realtime Kafka data stream for custom realtime map creation.

Progress with integration of Silversea Carbon Intensity rating calculations for the CII Dashboard

Met with Director of Fuel Budget and Director of Decarbonization Strategy and aligned on going forward with the Fuel Forecast Model CAR submission with $400K budget. Pending alignment with VP of Deployment Chris Allen. This is to save $1M by avoiding McKinsey advisory service on fuel forecast progress and highly improve $1B fuel budget forecast and Carbon Tax forecast.

Updates:

Onboard Revenue:

Collaborating with business to set fleet wide NPS targets for 2025. Two modeling approaches developed and pending to be shared with business early next week.

Contact Center:

Extracted topics for all calls back to 10/07/2023, which were previously missing due to compute constraints.

Loyalty:

Implemented the initial Sail Nights model with a 2 year requalification window (same as spend based model). Next step will be to merge the Spend based model with Sail Nights based model.

Digital

Product Recommendations:

The latest version of the API accepts a new SAILING_ID parameter which allows the frontend to request recommendations at the sailing level. Several new features have been added to the backlog based on feedback from frontend engineering.

GS Bot:

Developed improved topic classifier for 684 specific topics which can be rolled up to 40 general topics.

WoW

Modeling updates to MDR required significant changes to the approach. Initial approach to changes show promising results in accounting for inconsistent themed nights.

Issues

RCGGPT:

Bug identified via prompt injection QA.

Contact Center:

Lead performance dropped significantly for CTI leads in 2024. After root cause analysis, it was found that at the end of 2023 the CTI scoring was stopped. The technical teams are working towards reviving the CTI lead scoring ASAP.

The enterprise topic modeling summary dashboard failed to refresh this week due to issues in Oracle. Technical teams worked to find alternative ways to access the data.

Powerpoint here: I update W2W

07/22/24

CEL
Recently Completed
  Elasticity Re-Training Code now in production. Successfully ran with PRE Monday 07/01/24
  GTY-Replenishment Test and Code Construction Complete, Initial Run to Begin
  GTY-Lead Test Beginning
  Initial brainstorm and planning session for Track Optimization
  Baskets for all Metas
  Elasticity Model Accuracy Metrics with MLFlow (Tracking Error, Training Report, etc)

In Progress
  T4 Test Results Analysis
  Elasticity Model Addt’l Granularities (ALASKA, EUROPE, CARIB)
  Move Elasticity Models to Feature Store (Standardized Bookings & Price Dataset)

To Begin
  APD Track
  Basket Logic in Track Updates (MTRB)
  GTY-Lead Trade-Up Models 

RCI 
Recently Completed
  PRE Stale Prices Code Fixes, using Live Pricing in PL3
  First Data-Driven GTY REPL rules for Oversell Optimization
  Live Pricing Data Fixes
  PRE Changes to use live Mandatory Occupancy information
  SPI Roadmap Planning & Model Brainstorm

In Progress
  Brand Elasticities (To use in Track Opt)
  PRE Code Updates and Refactoring (Biz Rules, Old Accenture Code)
  Interviews

To Begin
  Additional Elasticity Model Upgrades (MLFlow, Re-Training, Metrics)
  SPI Model Testing

SSC 
Recently Completed
  Additional work on Feature Store for D2D, P2P, Essential Logic
  Subarea Geospatial Analysis, Findings presented to Business Team
  Biz Team Alignment on PRE Adjustments and BPO Projects
  Alignment with RM Planning of Track Granularities for PRE

In Progress
  Continued Analysis of Historical Booking Patterns (Area, Subarea, Seasonality) after Feedback
  MVP Code for SSC PRE
  Price, Bookings, Sailing Month, Subarea analysis to following Biz Team Meeting

To Begin
  Fit initial regressions for Elasticity Models by Area + Additional Granularities
  BPO: P2P vs D2D
  BPO: Category Gapping

ORB / PCP
Recently Completed
  Finalized asks for Digital Team based on business needs of Automation
  Aligned with Data Engineering team of data asks from ODS and Hybris

In Progress
  Story and release refinement for Pricing Automation and Track Optimization asks.
  Formalizing Digital Asks into structured document to present.

To Begin
  Initial Exploratory Data Analysis and spikes to support story refinement
  Meet with Digital team to review and prioritize asks of Azure --> Hybris Upload

**Update for E-Commerce**

**EDAs on txspend and watchlist/favorites** **data**

**Understanding of watchlist/favorites** **data** structure and meaning on session with table owner -Sumit from cbp team.

**Progress on front end for model combination on dashboard calculator**: shared with ecommerce team, they liked current status and shared some suggestion.

**Pending Tasks**

Continue with the integration of watchlist/favorites data.

Continue implementing front end for models combination in the dashboard.

**Update for Loyalty**

Fixed spend and occupancy metrics computation for future ships (IC3 and others).

Resolved mismatch issues between meta-product data on ship deployment.

Generate Future Ship Deployment myself from PCD Excel since versions from Merielle and stuart contain issues that highly affect the spend/bookings generator, like sailing nights averaging. also Added the option to select different scenarios from PCD table.

**Update for Global Supply Chain Business Planning**

Delivered 40,578 additional new demand forecasts from 8,792 products for 10 ships through December 2025 using 49 predictors in the MVP Gen 1 demand models.

27% of the total Silversea product cost in June 2024, had demand forecasts with under 40% Median Absolute Percent Error in June 2024.

Updating RCI/CEL code to keep the existing set of demand models with a back tested month for measuring model accuracy, with a new set of models that train all the way up to the last day of prior month, for business and financial reports. Completed model training with updated code and am in progress of updating downstream code on guardrails, with future updates coming on the finance tool code.

Demand Model for Crew Uniforms is still being worked on. Working on debugging code for the train and predict section.
