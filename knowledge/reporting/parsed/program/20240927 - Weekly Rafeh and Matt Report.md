**Proud**

• **Deployment Port Code GenAI Mappings****: **Presented Port Mapping tool (using GenAI) to Deployment Teams with highly positive feedback. The tool will enable Deployment Teams to standardize port-mappings across different vendor data. Now working to integrate the Port Mapping tool into existing Deployment pipelines.

• **E-Commerce Targeting: **DS team delivered new enhancements for CDP Customer Targeting dashboards based on business feedback (i.e. functionality enhancements to Audience Calculator tool). *Should have latest Epsilon Spend/Demographics integrated into production targeting models next week.*

• **Marine Operations: **RCG and Wartsila signed contract to monitor 37 ships for 5 years. Teams have aligned on going forward to approve single ship API access for the Wartsila Engine Experience Insight contract, which will reduce ship engine monitoring costs by $2.6M-5.5M (i.e. saving $70K-150K per ship). *DS team optimizing our power plant optimization models to account for scrubber limitations, which has been identified as an important requirement for upcoming work to enhance Fuel Forecasts. *

• **Supply Chain:** DS Team has completed an initial draft submission for a 2024-2025 Business Planning CAR, which will officially expand Demand Forecasting to Silversea HF&B, Uniforms, and Health Areas and increase value-creation by Supply Chain by +$2M annually. Team also shared pilot demand forecasts for the Silversea HF&B models with business teams and received positive feedback. *Team continuing to **enhance demand forecasts for Silversea HF&B and Uniform areas. *

• **NPS Target Setting (CEL):** DS Team has completed exploratory analysis for identifying NPS drivers for a subset of Edge class sailings using Medallia data. *Will be sharing these findings with business teams soon and expanding scope of analysis afterwards. *

• **PROPEL:** MLOps team has delivered the Backup Promotions Feature (Preparing Offers for Multiple Future Sailing Days to Mitigate Downtime Risk) and an Alerting/Scheduling Framework to automate timezone scheduling changes, giving ships more advance notice of offers and onboard new ships faster. Added two additional pilot ships to PROPEL offers in DEV (RF and IN).

• **Revenue Management (CEL): **DS Team completed revisions for the MTRB Track Optimization process based on business feedback and will be sharing updated MTRB track adjustments with business teams soon. The Track Optimization pilot is adapting RCI’s MTRB solution to incentivize sailing alignment for sailings sharing substitutable demand. Team is also beginning exploratory analysis for developing a Mandatory Occupancy Inventory Automation solution for CEL.

**• Revenue Management (RCI): **

- DS team has updated Berthing & Inventory Automation for ADA Compliance and completed upgrades to the SPI model to improve scoring performance on smaller products. *DS Team t**o share updates with business teams soon and are actively working on additional enhancements to SPI model (that will incorporate relevant Sailing Management factors)**.*

- MLOps team ready to release the Group Gapping Framework next week.  *The MLOPs team is working to streamline Automation operations with **PRE code**-refactoring and Unity Catalog migration partnering with Data Engineering.*

**Concerned**

Nothing new

**Excited**

• **Loyalty: **DS** **Team is taking over ownership of the Deloitte loyalty member clustering model and improving integration with Silversea and the Forward-Looking model.* This week Corporate Planning and Revenue Planning have requested to use the model clustering segments to identify profitable channels and segments based on Overall Lifetime Value that accounts for consumer spend and acquisition cost.*

• **MyCruise**** Production Recommendations:** Preparing to share PoC product recommendations, plus associated data (e.g. including product image URL, product description, inventory availability, interaction features) into Salesforce cloud for usage by the E-Mail Marketing team. The PoC recommender is actively being reviewed by our IT Front-End Developer teams to assess feasibility of Recommendations Engine API. *If approved, the team will be able to conduct AB Testing to evaluate the effectiveness of the PoC Product Recommendations to increase conversion. *

• **Revenue Management (SSC**): DS Team completed gathering additional business feedback for optimizing PoC Pricing Recommendations and Business Rules. Working on integrating additional business feedback into future Pricing Recommendations, completing initial Pricing Elasticity model.

• **Win-on-Waste:** Team has onboarded a new WoW resource and, based on stakeholder feedback, are adjusting the forecasting approach for the Main Dining Room through a more nuanced model. *A**ccurately forecast**ing** Main Dining room consumption** has been challenging** due to inconsistent scheduling in historical data**.*

MEDALLIA COE

Initial Topic classifier using embeddings approach has been determined to not perform well due to the quantity of topics being classified. Three additional approaches are being evaluated and my extend the topic classification delivery by an additional week.

LOYALTY

The team is adopting the Deloitte clustering model and is seeking to improve the implementation with added features.

MYCRUISE RECOMMENDER

POC recommender is under review by frontend dev teams to assess feasibility of production testing the Recommendations API.

EMAILS RECOMMENDER

Created an ETL which updates all Product Recommendation data including product image url, inventory, interaction features, descriptions,etc. Working with stakeholders to ETL data to Salesforece.

WOW

Main Dining Room forecasting model requires a change in modeling approach as a result of the historical meal schedule being non deterministic tic, therefore with undiscernible pattern. The team has come up with a 4 step approach to modeling and is in the midst of completing step 2. The new WoW team member is working code review and code documentation.

TARGET SETTING

Compiled initial findings into a draft report sumarizing the feature importance of Medallia metrics as it relates to NPS.

PORT MAPPING

Met with stakeholders to present Port Mapping tool which was met with excitement. Will be working with technical teams to integrate into existing port mapping pipelines.

LEAD PRIORITIZATION – BKTOCX

Retrained BKTOCX model with initial performance results showing conversion that is above expectations. The team is continuing to validate model performance with expectations that there may be target leakage.

Marine

Onboarding new DS Atefeh and Ignacio to support MIAP project and general onboarding of DataBricks and local development environment setup.

Created a re-usable Python package for curve fitting and deployed on Azure DevOps as a pip installable package. Integrated options for curve fitting with splines such as B-splines, Natural Cubic Splins and Smoothing Splines. New DS Ignacio is assisting in unit testing the package and optimization.

Continuing work on power plant analytics feature engineering and LNG ship integrations to prepare for the fuel forecast CAR.

Ongoing recuiting activities for new MIAP hires.

Held several meetings arround Wartsila Engine Expert Insight contract to monitor 37 ship's engine performance via MIAP API. Internal alignment on to go forward with a single ship API access. MIAP API to reduce project cost by $70-$150K/ship.

Met with fuel forecast CAR stakeholders on a requirement to include different max load constaints to power plant optimization module to account for scrubber limitations.

Starting to work on MIAP dynamic modelling feature engineering framework.

CEL
Recently Completed​
MTRB Round 1 Code + Algorithm Changes​
TAP Perks 2.0 Story Generation (Optimal Gaps by Meta, WTS)​

In Progress​
Elasticity Model Addt’l Granularities (EUROPE, CARIB)​
MTRB – Round 2 Feedback​
TAP Perks 2.0 Initial EDA​ (To gague whether or not test needed)
Mandatory Occupancy – Initial EDA​

To Begin​
TAP Perks 2.0 AB Test Construction​ and/or Modeling
GTY-Lead Trade-Up Models​
Mandatory Occupancy – Algorithm Development​
Baskets Web Data – Story Generation​
SPI CEL-specific Rework​

RCI
Recently Completed​
SPI Minor Metas​
Berthing Rules Updates for ADA Compliance​
Inventory Automation Code for ADA Compliance​

In Progress​
SPI -- Management Feedback and Review/Final Approval
SPI -- Sailing Management Factors​
Additional Elasticity Model Upgrades (MLFlow, Re-Training, Metrics)​
GTY-Lead 2.0 (Meta, CatClass, WTS) Model Story Generation​

To Begin​
SPI – Production Model and Reports​
SPI – Findings Integration into Data-Driven TAP Groups​
Data-Driven Mandatory Occupancy​

SSC
Recently Completed​
Round 3 Feedback – Code Changes​
Additional Elasticity Model Features (LF %)​

In Progress​
Fit initial regressions for Elasticity Models by Area + Additional Granularities​
BPO : ESS Fare Class – Initial Analysis​
PRE Business Feedback Round 4 + Story Generation​
PRE Integration of Pricing after Promos​

To Begin​
Dashboards and Reporting for PRE Recommendations​
BPO: P2P vs D2D​
BPO: Category Gapping​
BPO: ESS Fare Class Optimization​

​
OBR/PCP
Recently Completed​
Exploration. Familiarization, and EDA of new Transaction-level hybris data in Alpha Platform​
Exploratory Analysis of Dilution impact to Cabana Bookings​
Initial Elasticities by type, Tour Month, WTS Bin​

In Progress​
Cabanas Dynamic Pricing Algorithm / Optimization – Algorithm Development​

To Begin​
Cabanas Dynamic Pricing Algorithm / Optimization – Production Code​
Drink Package Price Optimization​

**GSCBP:**

*Silversea:*

1.      Business presentation with Director of Procurement for H,F&B on Tuesday to present demand model results. Presentation went well.

2.      In process of feature selection using advanced approaches to infer the best predictors to use for each main category to improve model accuracy.

*RCI Uniform Modeling:*

Working on better feature selection as the previous process gave a higher mdape for the features selected.

Reran the models to use the first features that continue to give best mdape.

Debugging code that gave me all zeros. Working on confirming that this was done correctly and ready.

*RCI/CEL H/F&B*

1.      Unified the code that was used for Silversea to RCI/CEL for creating challenger models, to ensure the error percentage for each challenger model ties back to the row level data.

Next Steps:

1.      Continue Feature Selection work for Silversea

2.      Investigating with Yan, why the predicted cost number from the finance tool is short of the actual expenditure for August. It appears this is an issue with calculations of cost, and not an issue with the demand model incorrectly predicting consumption. Yan has been working with Mario on adjusting the cost calculation which was supposed to have increased the estimated total cost, but the new calculation didn’t do that.

**Loyalty:**

Continued stabilization and modularization of loyalty pipeline, including the creation of a develop branch and test pipeline to be used to QA future updates.

Deep review of Deloitte Clustering code

Substantial debugging and code cleanup

Very close to completing etl and feature datasets likely to have a clean dataset by 9/27

Deloitte dataset was a point in time snapshot with many hardcoded configurations. There were also incorrect assumptions made that could result in poor clusters

Next Steps:

Cluster integration to the pipeline

Inclusion of SSC data in cluster dataset

Eda on cluster features to create new clustering algorithm that is based on spend drivers

** **

**E-Commerce**

Improve dashboard:

Add sendable swith to audience calculator

Add model recommended threshold information to audience calculator

Fix sendable by brand in scoring report

Models maintenance:

Integration and validation of  newest epsilon data (txspend and demographics) in models, should be in production next week
