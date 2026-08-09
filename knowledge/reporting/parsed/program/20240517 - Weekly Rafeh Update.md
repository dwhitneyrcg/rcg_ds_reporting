PROUD:

- **E-Commerce**** Targeted Offers****:** In early May, the E-Commerce teams delivered 18 new Smart Audience Segments with higher likelihood to book. Many of these consumers segments were selected based on this team’s AI-booking propensity scores (in addition to being active on the website). *The team is actively working with the E-Commerce team to develop quantitative tools that streamline the process of automatically selecting appropriate consumer segments using AI based on E-Commerce’s marketing & conversion targets.*

- **Loyalty Simulator: **The joint DS/E-Commerce/Deloitte team presented a biweekly update to the Loyalty leadership team on Lifetime Status for Pinnacles and Zeniths at Tier 4 (rather than Tier 5). *Feedback was positive and focused on sweeteners that will positively incentivize higher spending behavior by Pinnacles & Zeniths.  *

- **PCP Personalization: **Team developed an MVP API for Trending/Popular products this week that has been shared with stakeholders.

- **Revenue Management**** Automation****:**** **Over the last week, the team completed a substantial back-end rework of the pricing & inventory automation system codebase. *These upgrades enabl**e** compatibility** with newer Databricks run-times**, which **offer greater functionality and stability**.*

- **Win-on-Waste: ****AI Consumption **Forecasts for the pilot venue (Chopes Grille) were shared with Paul Fortin and IT Leadership this week with positive feedback. *Constructive f**eedback revolved around data quality of input data **(such as recipes and product mappings) **and operational inconsistencies that may lead to** forecasting discrepancies.*

CONCERNED:

None

EXCITED:

- **Digital Guest-Services Chat-Bot Evaluation****: **Digital requested the team to evaluate if the Guest-Services Chat-Bot is reducing Guest Services Requests. *Preliminary analyses are indicating that users using the Chat-Bot usage have a 10-20% reduction in Guest-Logs per Booking. Next steps are to explore and rule** **out any confounding factors associated with Chat-Bot usage.*

- **2024 ****Revenue Management**** CARs****:** The Team is beginning preparation & planning work with Revenue Management to begin capital work for the 2024 RMA CARs as soon as the CARs get approved. *Prioritized initiatives include (a) Category Gapping that will enable better pricing management of our cabin categories, (b) Track Optimization that will dynamically reshape track curves based on consumer willingness to pay, and (c) Always-on AB Testing to increase our ability to measure, monitor, and refine automation performance.*

- **Supply Chain:** Supply Chain met with Naftali earlier this week to review Supply Chain’s Finance Forecasting Tool for HF&B. *As a follow-up, Naftali has requested more information on the accuracy of our team’s AI demand forecasts relative to 2024 actuals. *

RCI

**Aligned with product teams for final Groups Berthing rules.**

Implemented changes in code. Presenting early next week to directors/VPs in RCI RM on rules.

**Fixed production issues with PRE, took a lot of time last week + Monday.**

Package issues + Data Issues (whitespace)

**GTY-Lead/Cat Gapping Model Discussions starting. (New 2024 CAR work!)**

CEL

**CEL Track Optimization Logic Fixes.**

Now successfully running v1.0 logic in dev.

Sample output provided to CEL team, awaiting feedback.

**Tested adding ship-class and seasonality to CEL elasticity ****models**

presenting to product teams today. Findings suggest more analysis needs to be done for adding ship class.

After presentation, getting go-ahead to put into effect new CEL elasticity model upgrades utilizing hyperparameter tuning, retraining, and new data.

System + MLOPS

**Always/On AB Test Design Spike.**

Created initial design writeup/spike. Presented to CEL team and got feedback for future plans and rough timeline of implementation.

**Feature Store Design for PRE and CEL / RCI GTY-Lead ****tradeup**** models.**

Working with glen-erik's team to finalize these.

**Data source Documentation for pricing projects.**

CEL PRE. Created shells for other projects and discussed with CEL team. Sharing templates.

**E-Commerce:**

Business Presentations / Meetings:

Had presentation on 5/15 with business, providing an overview of models in production. This meeting was designed to improve stakeholder understanding and collaboration around the use of our 74 production models. With the increase in production models that has added to complexity and this meeting was designed to reduce that complexity and also discuss opportunities for future work that can help the business.

Had follow on business meeting on 5/16

Current Work Priorities:

1) Integrate Epsilon Spending Data to Models

2) Build Calculator to allow the business to input a record count value they want to return and a model or combination of models that they want to use. The calculator will provide the query for pulling these records using the optimal threshold values for the model(s) and the expected lift or model performance from the threshold value in the calculator.

3) Business Dashboard Improvements: Overview of production models, model interpretability from most recent training run with aggregation of model importance into a small grouping of predictors and explanation of model metrics on dashboard.

**Global Supply Chain Business Planning:**

Business Presentations / Meetings:

Meetings are on-going around business adoption of our finance tool.

Last week Supply Chain team met with Finance team twice.

On 5/13 the Supply Chain team had executive meeting with Naf.

As an outcome of this meeting, Naf has asked for more information about how our models are performing in production from January to April.

We delivered results to the supply chain team on 5/14 showing at a product and ship level, detail on the model prediction for consumption, and actual consumption along with absolute percent error.

Had meeting on 5/15 with supply chain team to discuss results and next business presentation. Next presentation is going to show the sum predicted and sum actual consumption by category by month which tracks closely.

Current Work Priorities:

Small refinements to finance tool are in progress and will be completed by 5/17

Writing ETL code for Silversea in preparation of demand forecasting code.

**Marine:**

General Model Improvement:

A. Feature selection on hotel power model: Validated the removal of temperature sea water as a feature, improving base model accuracy.

B. Implementing package updates in collaboration with Jong to remove effects of multi-collinearity between speed through water and eniram voyage phase. - In progress 95% complete.

Additional Projects:

A. Investigated calculations of virtual speed through water to be used in conjunction with a kalman filter to improve hull maintenance. Feature set and math equations created and model development to begin next week. Current annual HPP spend with eniram totals over $1M/annually and generates over $40M/annually in savings.

B. Aligned with data engineering and enterprise architecture on miap phase 3, as well as etl improvements to existing pipelines. Additional topic discussed to test real-time streaming on ships while making live predictions. POC planned on one ship testing various solutions including kafka and utilizing existing OPC UA servers.

- PCP Recommendations
Developed an MVP API for Trending/Popular products. The API has been shared with stakeholders.

- Loyalty
worked with Deloitte to finalize this weeks biweekly readout. The stakeholder was very receptive to the idea of lifetime status at tier 4 for existing P/Z.

- WoW
The forecasting performance was shared to leadership, results were positively received. The feedback revolved around the data quality of input data and operational inconsistencies that may lead to incorrect assumptions as it relates to forecasts. Paul Fortin will follow up with specific action items on what steps the team should take to fix existing inconsistencies and also to mitigate impact of data inconsistencies. Patrick Morin suggested that it might be a good idea for the technical teams to visit the ship to observe how operational processes translate to data being capture.

- Contact Center
For the VTG analytics effort we deployed a table to the Contact Center analytics team that summarizes the VTG agency behaviors down to individual Agent names based on the Siren NER classifier pipeline. The report will enable the business to track how payments related calls are trending starting from October.

- Nuance
Assisted in encrypting and transferring 8000 recordings to Nuance to improve Celebrity specific functionalities.

- GS Bot 
Digital has asked datascience to investigate the impact of the GS Chatbot on Guest Service Requests. This comprises of joining bookings data, chat data, and guest logs data. Initial findings show that that the population of Bookings that used the GS Chatbot had a 10-20% reduced footprint in terms of Guest-Logs-per-booking. The DS team will further explore any confounding variables that might be associated to app usage.

- Liveperson
the exiting topic classifier for the LivePerson classifier was developed by the Contact Center Analytics team. The existing classifier was limited to 7 topics and only scored the first 3 utterances of a given chat conversation. DS team has deployed to Siren to production which is an effort to replace the existing classifer with a more robust pipeline that will score all utterances as well as yield 27 topics as opposed to 7. The broad objective of this effort is to align the "chat volume of topics" to "call center volume of topics" in an effort to track the impact of chat at the topic level on the volume of inbound service calls.
