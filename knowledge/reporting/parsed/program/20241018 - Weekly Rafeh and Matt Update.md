**Proud**

- **RCG-GPT:** Public roll-out of RCG-GPT this week (10/15/2024). MLOps team updated RCG-GPT’s terms-of-use to allow users to upload non-public data and eliminated PII filters based on alignment with IT/Legal leadership.

- **App Incremental Revenue Analysis (Digital): **Presented initial channel shift results to Senior Leadership members (including Heather, Kira, Michael, and Brian) with constructive feedback. *Next steps are to share a regression analysis that will identify if there is likely incremental revenue uplift with the App.*

- **E-Commerce:** DS team completed integration of new precruise and onboard purchases data into E-Commerce targeting models (spend and propensity models). *Next steps are to retrain models and validate performance before productionizing the enhanced models.*

- **Loyalty: **DS team completed major enhancements to a new *in-house* clustering model that more accurately captures the customer journey over time (spend and return rates) over the Deloitte clustering model. Next steps are to validate the approach and incorporate both SSC Onboard Revenue + Future Deployment data into the Loyalty Simulator. *The new clustering segments will be used in the Loyalty Simulator and by our Corporate Planning teams to calculate Customer Lifetime Value (New Q4 Delivery).*

- **Supply Chain: **DS team delivered short-term demand models for Utopia of the Seas and enhanced SSC demand forecasting models (reducing forecasting error by a substantial 10%). Also, completed major updates for upcoming 2024-2025 Supply Chain CAR submission. *New CAR will provide capital funding for ongoing activities to expand** demand forecasting **into new business categories.*

- **Revenue Management (RCI):**** **DS Team created data quality checks for pricing automation to share with Data Governance team and shared new SPI scores for business feedback.  PRE output enhancements/fixes requested by RM. *Planning to productionize MVP SPI model soon and begin integrating SPI into TAP automation projects. *

- **Revenue Management (****SSC****):**** **DS Team reviewed MVP elasticity model with SSC RM team and completed revisions on elasticity work and PRE pricing change logic. *Next steps are to **integrate** pricing elasticit**y model **into** PRE** pricing recommendations** **and begin **BPO planning to optimize pricing gaps through TAP automation (e.g. Port-to-Port vs Door-to-Door fares). *

**Excited**

- **Lead Prioritization (****Contact Center****)****: **DS team validating RCI BK2CX Lead Prioritization and developing a comparable CEL model for BK2CX and CTI leads. Also helping Contact Center with communications to Contact Center agents on best practices for RCG-GPT.

- **Deployment:** DS team shared preliminary results of mapping Cruise Mapper ports to standardized port codes using our new Gen-AI based Port Mapping tool.

- **Medallia GenAI Pilot Use-Case (Hotel Operations): **DS team working on building AI-generated drill-drown reports to monitor KPIs (e.g. aggregating sentiment, topic counts, etc). Asked to put together a deck highlighting use-cases for Medallia Survey data that will be shared broadly (first with RCI Operations teams and then CEL/SSC). *Expecting delivery of the Medallia GenAI pilot by end-of-year and a pilot ready for crew testing by early November.*

- **Marine Operations:** DS team completed data tag mapping for ML-class ships and working to extend coverage of “digital twin” performance monitoring solutions to ML-class ships. *Preparing to submit the Fuel Forecasting CAR soon.*

- **NPS Target Setting (Hotel Operations):** Completed a report to summarize feature importance of Medallia metrics predicting NPS and beginning to adapt NPS Target Setting tool for the RCI guest Strategy & Analytics teams.

- **PCP “****MyCruise****” Product Recommendations (Digital): **DS team is adapting the PCP Product Recommendations for additional use-cases by the Emails team. *Working with business units to create an automated workflow that makes product recommendations available in Salesforce for usage by the Email team. **Still waiting for Front-End Dev Teams to approve production testing of the API for the primary Digital App/Web use-case.*

- **PCP Pricing Automation:** DS Team completed the MVP Cabanas Elasticity Pricing Model and *Dynamic Pricing Algorithm* for RCI. *Next steps are to** **adapt model for CEL** and** productionize initial MVP models.*

- **Revenue Management (CEL):** DS Team completed elasticity model upgrades for minor products (e.g. Canals and Repositioning Cruises) and shared PRE-forecasting errors with business teams. *Kicking off** AB Test to identify revenue-optimizing gaps for the TAP **Perks automation **project.*

- **Win-on-Waste Forecasting (FPMS):** DS team completed model integration work for Coastal Kitchen and Giovanni’s Italian Kitchen, which will extend demand forecasting coverage to two additional specialty dining venues. *Next steps **will be** validation of the new demand forecasts** and finalizing **our forecasting approach **for the Main Dining Room **(**November** 7**th** deadline**)**.*

**Concerned**

None

GSCBP:
CAR:
• Completed the updating of the 2024 Business Planning CAR Memo along with the CAR Financial Model. First stakeholder review is completed and the Director is now reviewing. 
RCI/CEL
• Implemented short-term demand models for Utopia, so that it is going to start using its own consumption for demand forecasts instead of mapping demand forecasts from Wonder to Utopia.
• Beginning work on the cost based adaptive model to see if we can improve model forecasts through calibration, via learning from historical residuals on a cost basis. The prior excellent work on the unit based adaptive model did not improve model forecasts, so there is no guarantee this cost based approach will yield improvement. 
o Aggregation / wrangling of historical forecasts, with consumption data in process this week.
Silversea Models:
• Reduced model error of AI models by approximately 10%, through a stratified sampling approach based on Product Sub-Category and implementing recursive feature elimination with SHAP on the sampled records to have a unique feature set for each Product Sub-Category, along with introducing monotonicity constraints on select features to constrain the model training process. 
• Worked with Data Engineering to identify challenges in the point of consumption data, and working to improve quality assurance processes.
Uniform models:
• Delivered improvement to the models by using recursive feature elimination with SHAP for feature selection along with monotonicity constraints resulting in a 12% reduction in model error.
• Updated stakeholder dashboard with uniform model metrics at the bottom of the dashboard
• Created a notebook for mlflow logging metrics for easier access. logs metrics such as mdape and logs artifacts for metrics in the result of tables such as mdape by microcategory.

Medical models:
• Filtered consumption data to these categories: MEDICAL CREW SUPPLIES and MEDICAL
Similar to uniform, instead of COUNT_CREW, it is now COUNT_PASSENGERS to normalize consumption
• Created a notebook for mlflow logging metrics for easier access. logs metrics such as mdape and logs artifacts for metrics in the result of tables such as mdape by microcategory.
• Features selected by random forest seem to be overfitting the model for giving such a low mdape for comfort. 

Pending Work:
• Create CAR Fact Sheet.
• Update CAR Roadshow PowerPoint.
• Filter Medical model down to only include the Medical Category and not Medical Crew Supplies.
• Integrate recursive feature elimination and Monotonicity constraints into the medical model.
• Normalize SHAP values based on prediction values first for uniform and then for medical.

E-Commerce:
Maintenance of Models: 
• Cleaning and Feature engineering of precruise and onboard purchases data.
Pending Tasks
• Train and Test Marketing models after adding precruise and onboard purchases features
Loyalty:
Work Completed this week
1. Rework Clusters
1. Created POC clustering model that more accurately captures the customer journey over time. This approach is a large improvement over previous iterations by isolating spend driven by customer persona, while removing effects driven by itinerary and other confounds.
2. This approach is still being validated, but should be applicable across brands as guest metrics are measured against their peers on the same sailing.
3. These clusters will help to simulate future guests that are new to the company in the forward looking model, as they are now a strong indicator of spend and return rate in our spend model.
2. Integrate SSC Data
1. Received SSC OBR, Pre/Post cruise spend, and future itinerary. Data is being validated but will soon be added to the simulator pipeline as SSC integration work progresses.
3. Customer Lifetime Value
1. Data Collection and aggregation along with steering meetings on CLV calculations and segmentation approach
Next Steps
1. Validate and refine clusters, SSC data, and CLV data
2. Integrate POC Spend Model and Clustering Model in simulator framework
3. POC Model to calculate proportion of new guests from each cluster for future sailings.

Marine Operations

Working for integration of ML class machinery and hotel power models. Completed tag mapping and feature engineering.

 Progress with bug fixes of curve fit package.

Updating power plant and hvac analytics with the new dynamic model package.

Continuing fuel forecast CAR data quality controls prior to car submission

Port Mapping

Ran the port code matching function for the cruise mapper data Daniel provided and shared the results with him

Medallia COE

The team began working on analytics queries (aggregating sentiment, topic counts, etc) and dashboarding. The team is also planning out reporting capabilities which are planned to be ready at the go-live date.

- The team was asked by Gang to run Validations against existing Medallia topics

- The team was asked to put together a deck that highlights the use cases that the Medallia COE can facilitate

- Jorge & team will own PowerBI dashboard development

- To Do:

- Need to improve redaction/replacement strategy

- Work to improve the sentiment scoring

- Work towards normalizing people/places

Lead Prioritization – CTI

Working on framing the code structure for Celebrity Lead Prioritization project based on RCI implementation.

Lead Prioritization – BKTOCX

Target leakage investigation persists as the model is still not performing as expected. We need to explore the possibility of the import ETL being incorrect. The team is training the CEL model to compare a CEL BKTOCX model performance against R.

MyCruise Recommender

POC recommender is under review by frontend dev teams to assess feasibility of production testing the Recommendations API.

Emails Recommender

Created an ETL which updates all Product Recommendation data including product image url, inventory, interaction features, descriptions,etc. Continuing to work with ecommerce to transfer data to Salesforce.

Target Setting

Compiled initial findings into a draft report sumarizing the feature importance of Medallia metrics as it relates to NPS. Collaboration with Royal Guest Strategy & Analytics team continues as the team is motivated to use the Target Setting model for 2025.

- Discuss added value of Comments Analytics

- Correlations

- Point based impact

- Force plot / shap feature importance

- Explanatons of decrease in quality of service

- Share code

- Matching logic (celebrity)

- Naïve Matches

App Analysis for Incremental Revenue

The team gave senior leadership an introduction to the Channel Shift analysis that was conducted to measure any Incremental lift gained by the App starting mid 2023. Pending to share the regression based analysis.

- Approach 1

- Created Naive clustering model to segment booking by age groups

- Ran dozens of regression models on segments to evaluate the impact of app vs web

- Approach 2

- Exploratory analysis focused around Channel Shift from Web to other channels

- Analysis shows that

- the introduction of App is correlated with a decrease of Web to Web bookings YoY

- when combining App with Web, Web to Web bookings increase YoY

WoW

Added Coastal Kitchen and Giovanni’s Italian Kitchen from the Crunchtime database and model integration work is complete, pending PR approval by Ayon.

CEL

Recently Completed

TAP Perks 2.0 Test Begin

GTY-Lead Trade-Up Models (Story Generation)

Elasticity Model Minor Metas

Data Provided to CEL team for first analysis of PRE forecast errors (for DART)

In Progress

GTY-Lead Test Results Analysis

GTY-Lead Trade-Up Models (Model Development)

Basket-based Track Adjustments Logic Updates

DART Model Integration (Kalman Filters)

To Begin

SPI CEL-specific Rework

Elasticity-based Track Adjustments

RCI

Recently Completed

Created Data Quality Checks (Work with Data Governance)

SPI Scores Review by Business & Feedback

GTY-Lead 2.0 (Meta, CatClass, WTS) Model Story Generation

In Progress

SPI – Add New Years to Considerations

Additional Elasticity Model Upgrades (MLFlow, Re-Training, Metrics)

GTY-Lead 2.0 (Meta, CatClass, WTS) Initial Model Fitting

To Begin

SPI – Production Model and Reports

SPI – Findings Integration into Data-Driven TAP Groups

Data-Driven Mandatory Occupancy

SSC

Recently Completed

Initial Elasticity model review with Camille

Elasticity-based Price Change logic created for use in PRE (still need to code)

Elasticity-based Track Optimization SPIKE

Round 4 Code Changes

In Progress

BPO : ESS Fare Class – Initial Analysis

PRE Integration of Pricing after Promos

PRE: Initial Dashboards and Reporting for PRE Recommendations

PRE: Integrate code for elasticity-based price changes

To Begin

PRE Price Upload for Res 2.0

BPO: P2P vs D2D

BPO: Category Gapping

BPO: ESS Fare Class Optimization

PCP/OBR

Recently Completed

CEL OBR Cabanas Work – Kickoff and Planning

Cabanas Dynamic Pricing Algorithm / Optimization – MVP code developed, still need to finish production-ready code

Cabanas Dynamic Pricing Algorithm / Optimization – Algorithm Development finished for the linear program

In Progress

Cabanas Dynamic Pricing Algorithm / Optimization – Production Code Development

Cabanas Dynamic Pricing Algorithm / Optimization – Output Review

CEL Cabanas – Story Generation

To Begin

Dilution Model Improvements

Work on Improving Cabana Elasticity Model Accuracy

Drink Package Price Optimization
