**Proud**

- **New Hires: **Mert Ersoz will be join team within the next week and lead the teams’ analytics for Marine Operations (i.e. MIAP + Fuel Forecasting). Within the next two weeks, three additional Data Scientists will be joining the team to accelerate business deliveries for approved capital projects in Revenue Management & Onboard Revenue. Team is preparing an offer for a new Senior Data Scientist to start in Revenue Management.

- **Revenue Management (RCI and CEL): **Team is now scoring entire RCI fleet with a Sailing-Performance Index (SPI) to evaluate revenue performance. Working to integrate SPI into ongoing track optimization projects for RCI + CEL.* Team continues to support ongoing AB Testing and Pricing Automation code changes to handle when discount pricing schedule is retired next month. *

- **Loyalty Simulator: **Updated simulator to reflect latest business requirements when assigning ticket and onboard spend to Loyalty members. *Team is preparing **a major analytics** update that will be forecasting future Loyalty Program state (i.e. # of Loyalty Members Per Tier, Fraction of Deployment, and Forecasted Spend/Return Rate) with the Forward-Looking Simulator.*

- **Win-on-Waste:** In advance to an onboard ship visit with Specialty Dining chefs, the team completed developing out model interpretability metrics to help the end user (our chefs) understand how demand forecasts are generated. *Team is also continuing to work on Main Dining Room pipeline.*

- **Supply Chain:*** *Delivered a Demand Forecast Fall-Off Report (to identify products without a demand forecast) and a new Demand Order Details Report to provide better visibility into consumption for procurement teams. Demoed enhanced Demand Forecasts for Uniforms and received new requirements for price web-scraping tracking report. *Team is preparing to enhance demand forecasts using the DART algorithm, which has been showing to improve forecasting accuracy in Revenue Management and Marine Operations. *

- **E-Commerce:***** ***Completed major enhancements to Targeting Models and Audience Calculator metrics. Working to validate newest epsilon data and reintegrate spend date into targeting models (if validated).

- **Medallia NPS Targets (CEL):** Delivered both naïve and AI-generated targets for key Medallia metrics. Team is now working on a Power BI Dashboard to share targets with business in an ongoing way.

- **Deployment:** Demoed a Port Code mapping PoC to enable Deployment teams to dynamically map port codes to standardized codes using GenAI.

- **Marine Operations: **Identified 3 potentially new cost-saving using-cases with ships demonstrating large energy deviations to “Digital Twin” performance models. Enhanced new local time feature with over 98% accuracy, which will help reduce reliance on vendor data (i.e. Eniram) for historical and new MIAP-related projects. Team has integrated new time feature into total service power, hotel, and machinery performance modeling models.

**Concern****s**

None

**Excited**

- **Revenue Management (SSC): **Team continuing feature engineering for the Silversea pricing elasticity model. Team received constructive feedback on *MVP Pricing Recommendations (without pricing elasticities applied) **by RM product teams and beginning to update pricing recommendations**.*

- **STEER Officer Recommendations:** Updated the sources with new Data provided by HR. *Next steps are to write officer recommendations to a secure **Sharepoint** for Marine Operations leadership.*

- **Medallia GenAI Pilot Use-case: **Finalized list of Medallia Topics/Sub-Topics with Onboard Revenue Teams. *Expecting delivery of the Topic Summarization pilot by end-of-year with a pilot delivered for crew testing in early November. *

- **PCP Personalization:***** ***Working with Platform Engineering team to serve Naïve product recommendation models on CosmosDB.

MyCruise Recommendations
- Working with Platform to implement CosmoDB POC as a swap for Naive Recommendations

Medallia (GenAI COE)
- Worked on the Medallia project to finalize the list of topics and subtopics.

Loyalty
- Implemented changes to assigning PCP/OBR spend to return date 
- Exploratory analysis: 
  - to understand the fraction of PCD's made up by tiers over the last 14 years
  - to project APCD, PCD, and Pax Counts into 2030
  - to begin working on strategy to answer questions required for insights readout

WoW
- Model decomposition and interpretability in DB and offline version with subroutines complete 100 %
- MDR modelling 15%

Medallia Target Setting
- Provided business with naive and advanced targets for key medallia metrics
- Started work on PowerBI target setting Dashboard

Deployment 
- Demoed POC of Port Code mapping tool which will allow teams to map port codes using various GenAI workflows

Steer 
- Updated the source table with the new table provided by HR for the Steer project.
- Blocked due to lack of permissions to write to Sharepoint

Digital GS Chat 
- Fixed a bug in the GS Chat daily refresh table.

Crew HR (Project NAVI)
- Began identifying proper data sources and mapping topics to key words

Update for E-Commerce

1.	Models maintenance:

•	Add flag SCORE_SEGMENT FLAG  to model scores (High or low) based in model threshold that maximizes F1

•	Temporally remove txspend data from production models until latest batch is validated

•	Improve feature importance computation for multi-class models by removing out-layer classes from computation

2.	Improve dashboard:

•	Improve accuracy of estimated audience calculator metrics, by computing conversion for each distribution bin instead of assuming that score distribution is the same in validation and prediction.

•	Speed up estimated metrics for audience calculator, by  building helper datasets in databricks during score time.

Pending Tasks

•	Continue Improving Audience Sizing Calculator (bp+destination)

•	Validate newest epsilon data (txspend and demographics)

Update for Loyalty

1.	Generated new guest sailing scenarios using latest available pcd counts from RM, spending definition from Erick and clusters from Deloitte

Update for GSCBP

1.	Demand Forecast Fall Off Report:

•	New report in the Voyage Pivoted Demand by Sailing Date suite of reports that identifies product/ship combinations that were not written to SharePoint in the main reports, and provides the historical consumption and forward looking demand forecasts for those products/ships.

•	This is very unusual, as currently, 275 ship/product forecasts out of 158,493 are on this fall off report.

2.	Delivered New Demand Order Details Report in Sharepoint for Brenda Almengor

•	This report provides a pivoted view of product/ship demand forecasts by voyage departure date / voyage number along with ordering details for that product.

3.	Productionize Silversea Demand Models:

•	Developed code for model performance reporting, and ETL of product level forecasts relative to actuals to archival table, deep cloining data to Yan’s database in Databricks for accessibility in PowerBI, and orchestration of code in Azure Data Factory.

4.	Gathered new stakeholder requirements and actively refactoring prompt engineering to generate automated monthly reports for inflation tracking. Developed code to send automated report via email. Currently awaiting platform team to enable email access from Databricks.

5.	Data Preparation and ETL for dynamic forecast adjustments similar to DART in revenue management and MIAP's dynamic model

**Marine:**

Further validation and refinement of new local time feature achieving over 98% accuracy with Eniram calculated local time. Local time expanded to include full history of MIAP data across fleet. This drastically reduces our reliance on Eniram provided data for MIAP projects.

Integration of new local time feature in total service power, hotel, and machinery models.

Ad-hoc analyses on 3 ships investigating large energy deviations. Still in communication with ships to diagnose cause and resolve deviations. To be determined if deviations are model error or true deviation.

Developed logic to calculate necessary fuel flow rates, in preparation for upcoming fuel forecasting capital project.

Corrected historical fuel efficiency reports submitted by ship personnel to improve accuracy of SFOC page in MIAP web app

Commissioned OY IoT Data Flow

Bernard

RCI:

SPI scoring for entire RCI fleet year-round. Logic included for meta-specific holidays (e.g., Chinese New Year)

Track recommendations based on SPI on meta, week of year, and weeks to sail granularity along with a quantification of the asymmetrical cost-associated with missing track.

CEL:

Kickoff of mandatory occupancy project. Expectation is to use data-informed limits based on meta, time of year and hardware.

Provided SPI track optimization using RCI model as POC for deployment track recommendations. Continuing to work on dynamic track adjustments based on sailing baskets.

Doug

Celebrity Testing: Wrote a notebook that calculates Sample Ratio Mismatch so they're able to measure statistically whether test group volume is being generated equally or if a group is causing volume to be diverted/skewed more than is acceptable.

RCI PRE: Finished writing/testing code changes required to handle when discount pricing schedule goes away. Reviewing with Eddie Baffa.

Jesse

I'm finishing up the feature engineering that I have been working on last week. By weeks end, I should have it completed.
