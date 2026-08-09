**Proud:**

- **Revenue Management (RCI):** At RM’s Quarterly All-Hands, Michael Goldner and Nick Desrochers publicly awarded two of the team’s Data Scientists (Bernard Wittmaack and Doug Bedell) with outstanding employee contributions to the department this year. Team also completed massive code changes to eliminate the discount price schedule from PRE (which is being removed from all RCI sailings on Sept 14th) and delivered other automation upgrades requested by the RM product teams. *Team is progressing towards delivery of **a **SPI model scoring all North American Products (delivering all 7N Caribbean sailings this week).*

- **Revenue Management (CEL): **Introduced Week-Of-Year seasonality to Pricing Elasticity Models, which will improve PRE’s nuanced pricing recommendations. *Focus **has now shifted to** quantifying the revenue benefit **for deploying a** track optimization** process** that incentivize**s** **alignment of booked position for sailings sharing substitutable demand **(like RCI has).*

- ***PCP Personalization: ***Delivered *Naïve* MyCruise Product Recommendations (Trending and Popular) for Items Viewed, Added-to-Cart, and Started Checkout. *Team has already delivered Naïve Product Recommendations for** Bought Items completing **delivery of** the team’s** Naïve **MyCruise** Product Recommendations. Now working with Platform Engineering team to enhance “read” performance by transitioning from a Databricks Model Serving Endpoint API to **CosmosDB** PoC**.*

- **Loyalty**** Simulator****:** Joint Deloitte/E-Commerce/DA2I analytics team presented another Loyalty Insights Readout to Nancy/Andrea/Cecillia/Mike this week focusing on Silversea + Casino integration into Loyalty program. Silversea Ticket Revenue data is now incorporated into the Loyalty Simulator. *Additional QA is needed due to poorer Silversea data quality and team is identifying onboard revenue (which will contribute ~33% additional Silversea revenue).** Team is preparing **a major analytics** update that will be forecasting future Loyalty Program state (i.e. # of Loyalty Members Per Tier, Forecasted Spend/Return Rate) with the Forward-Looking Simulator.*

- **Supply Chain: **Completed Uniform Demand Forecasts MVP and preparing to share model performance metrics with Supply Chain teams. Team also completed (1) a PoC, leveraging LLMs, to automate price trending analysis for Commodity items into a monthly report, (2) a 12-month rolling report on historical demand forecasts, and (3) various pipeline maintenance/bugfixes requested by business stakeholders. *Future work will be optimizing Uniform Demand Forecasts + Guardrails and productionizing Silversea Demand forecasts. *

- **Medallia NPS Targets (CEL):** Revised logic for Medallia mappings and optimized processing time by 10x to facilitate higher-quality NPS target-setting.

- **E-Commerce:*** *Completed additional stakeholder requested fixes/maintenance of models & dashboarding tools. *Future focus on improving audience sizing calculator.*

- **Marine Operations: **Delivered service power model baselines on MIAP web application, breaking down total service power into its sub-components.

**Concerned:**

None

**Excited:**

**Revenue Management (SSC): **Team continuing feature engineering for the Silversea pricing elasticity model. *MVP Pricing Recommendations (without pricing elasticities applied) have been shared with the SSC RM teams.*

**Medallia GenAI Pilot Use-case: **Completed exploratory analysis of Medallia Topics/Sentiment against Medallia Metrics and NER Trends (i.e. Extracted Entities, such as Names for Ships, Venues, Crew). *Expecting delivery of the Topic Summarization pilot by end-of-year with a pilot delivered for **crew **testing in early November.** *

**Deployment:** Met with Deployment + Revenue Planning teams to discuss future collaboration opportunities (including sharing updated fuel forecasts, ship berth information, and port code mappings).* Team is nearly done a Port Code mapping PoC to enable teams to dynamically map port codes to standardized codes using GenAI.*

**Win-on-Waste:** In advance to an onboard ship visit with Specialty Dining chefs, the team is actively developing model interpretability metrics to help the end user (our chefs) understand how demand forecasts are generated. *Team is **also **continuing to work on Main Dining Room pipeline and beginning work for a Data Validation Tool to ensure data quality for forecasting inputs.*

MyCruise Recommendations
- Implemented Recommendations for Views, Add-to-cart, Started-checkout
- Working with Platform to implement CosmoDB POC as a swap for Naive Recommendations

Medallia (GenAI COE)
- Plotting Topic and NER Trends as time series
- Correlations of Topics & Sentiment vs Medallia Metrics

Loyalty
- Implemented current version of Silversea data into Simulator. However due to poor data quality the simulator outputs are not reliable

Lead Prioritization
- Working towards updating existing BKTOCX lead scoring pipeline in an effort to assist CCAS teams to kickstart lead scoring initiative

WoW 
- Working to implement model Interpretability pipelines
- Working on implementing Main Dining pipeline 
- Began building a Data validation tool to ensure that our Input data sources are good to use for the modelling process
  - For example to check fields for nulls and flag and log problem results

Medallia Target Setting
- Implemented new revised logic for Medallia mappings
- Implemented the first iteration of parallel processing code to speed up predictions from ~23 mins to only 2-3 mins in total

Deployment 
- Wrapping up development for Port Code mapping POC which will allow teams to map port codes using various GenAI workflows

**E-Commerce**

Models maintenance:

Improve training report metrics for booking propensity models,

Validation of txspend data leakage fix.

EDA  on new epsilon data (issues found transmitted to Data Team)

Integrate  new txspend and epsilon tables on the models after schema changes cause errors

Improve dashboard:

Added metrics Audience Sizing Calculator (BP+Spend)

Added user for bi team (Aliza)

Work Areas for Next Week:

Continue Improving Audience Sizing Calculator (bp+destination)

Add Above/Below threshold flag to scoring results

**Loyalty**

Fix computation of simulated guests that switch cabin type

**Marine**

Developed internal local time calculation converting UTC timestamp using coordinates. This reduces reliance on Eniram provided data. Previous POC using open-source TimezoneFinder package took over 48 hours to convert one month of timeseries data. New tool converts full history in 4 minutes.

Replaced local time features with new internal local time in HVAC and Service Power Models. Further validation is still underway.

Added service power data validations to Miap web application breaking down total service power into its components.

**GSCBP**

*Uniform Demand Modeling*

Completed Uniform Demand Modeling Notebook, trying out different features to see how MAPE improves

Uniform data is updated to 2025 so will run ETL notebook again for any changes

Running code now to have MAPE by micro category and further information such as cost and volume

*Inflation Report Price Scraping*

Completed POC utilizing ChatGPT to automate price trending analysis, to be converted into a monthly emailed report.

*RCI/CEL HF&B*

Delivered 12-month rolling report of historical demand forecasts for the most recent completed month (July)

Resolved instances where Brand value was not complete on Base-Rate Reconciliation Data (Finance Tool)

Pipeline Maintenance: Instituted code change to resolve error that happened when data changed in this weekend’s pipeline run

In progress of delivering Demand Forecast Reporting with Order Details (i.e. Order Frequency Name) to Director, Global Inventory

*Silversea*

Met with Director, Procurement F&B and Hotel to discuss progress on Demand Modeling and get next step work requirements

Work Areas for Next Week:

Enhanced Feature Selection for Uniform Modeling

Uniform Modeling Demand Model Adjustments and Guardrails

Complete Demand Forecast Reporting with Order Details

Productionize Silversea Demand Modeling Code

Productionize Uniform Demand Modeling Code

Jesse

This past week I've been working on generating features for a SilverSea price elasticity ML algorithm. I am focusing on areas that Roberto prioritized in our meeting a month ago. These areas include:

Mediterranean

Northern Europe

Caribbean

Alaska

The features can be broken down into several groups. These groups include:

Features that measure sailing similarity to predetermined clusters  (unsupervised classification)

Features that examine sailing proximity to specific geographic subareas  (unsupervised classification)

Features that examine seasonal anomalies in booking data

Features that examine whether sailings stop at specific ports

I have made a great progress on these features this week.

Doug

**PRE**: RCI is removing the discount price schedule from all ships on Sept 14th. Conducting full analysis and code updates to ensure PRE does not fail once discount prices go missing (top priority directed from Nick/Eddie).

**Automation**: Focused upgrades to RCI automation products based on product team requirements. Added:

Ability to pause specific categories from auto-replenishment in cases where sailing needs specific attention to fix inventory. Auto-unpause to prevent infinite pause times.

Configurable oversell percentages when sailings are outside final payment.

Add names of sailing managers for use in reporting/Power BI filtering.

Bernard

Updates RCI:

Developed proof-of-concept SPI model for 7N Caribbean extending from original summer season to entire year.

Began work on SPI factor model focusing on group load factor relationship with SPI score throughout the year.

Upcoming RCI:

Extend year-round SPI scoring and group load factor model to all North American products

Updates CEL:

Established robust predictors of ship expected volume by time of year on weekly granularity.

Enhanced PRE by introducing week of the year seasonality to the elasticity of all major meta products, improving model accuracy and providing nuanced pricing recommendations.

Upcoming CEL:

Quantifying the revenue benefit of sailing baskets by relating them to variance to track improvements.

Data-driven mandatory occupancy controls based on historical patterns in T4 demand.

Minor meta products introduced to PRE as separate entities as opposed to a brand average.
