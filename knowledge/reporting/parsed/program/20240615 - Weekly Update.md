**Proud:**

- **Revenue Management:** Additional products have been added to RCI’s gradual roll-out of Group Berthing automation, increasing the number from 1 to 4 (CARIBNE, CANADA, Australia, and Europe). *Other focus this week h**as been** on 2024 CAR planning and** developing/enhancing pricing elasticities for all three brands (SSC/RCI/CEL), which **has** applications for making** better** revenue-optimizing pricing recommendations and track optimization**s**.  *

- **Marine Operations: **Marine and Finances teams from RCI + CEL have agreed to support a joint partnership with Chantiers de Atlantique ship yard to share data from the MIAP web application (i.e. AI model outputs and raw IoT sensor data) as a tool for continuous monitoring of ship performance by yard energy experts instead of relying on yard's own solution. *Collaboration with Ship Yards for monitoring shipboard energy performance is likely to significantly increase the cost-savings impact of MIAP.** *

**Concerns:**

None

**Excited:**

- **Loyalty:** Preparing for a Phase 2 readout next week that will include a detailed analysis of the expected Program Costs by Tier by considering benefits costs, utilization rate, and sharing of benefits with lower tier members (like immediately family).

- **Marine Operations:** The team recently deployed a new AI model to monitor machinery power. Recent review of machinery outputs has identified significant energy deviations that are now being investigated on three ships. *To-date, MIAP has reduced fuel consumption by $2.5M across the fleet and identified nearly $1M in potential energy savings opportunities.*

- **E-Commerce: **The team is actively working on creating tools to reduce friction between end-users and our AI models. The tools will enable business users to efficiently identify the right consumers needed for marketing campaigns based on AI filters (e.g. propensity scores to sail specific destinations and/or spending forecasts).

For SSC RM:

The team is beginning work on machine-learning models to understand SSC elasticities by Itinerary and Cabin Type. The team has increased the cadence of meetings with SSC business experts to better understand the data sources and business model for the brand that will guide the design and usage of the elasticity models for the SSC PRE.

RCI:

Further work continued on MVP of Elasticity-based Track Optimization.

The team continues to complete more post-production work on Groups Berthing

CARIBNE, CANADA, Australia, (and Europe starting tomorrow) Itinerary products are online.

Further work being done to expand for the rest of the active fleet.

CEL:

New work on data quality fixes for CEL elasticity models.

This is part of a larger set of work in conjunction with MLOPs team for utilizing databricks feature_stores and proper tracking of feature definitions and data quality.

Planning for Phase 2 CAR future upgrades to Elasticity Models.

CEL GTY_Lead AB Test Design nearing completion

This will introduce version 0.5 of GTY Replenishment (Inventory Automation) to aid in enforcement of AB Test.

Weekly Report:

GSCBP:

Silversea ETL Work is still in progress. The voyage and revenue forecast data is nearing completion and should be done by Monday.

Knowledge Transfer and Onboarding of Camila on GSCBP in-progress. So far she has been trained on the ETL code and half of the demand modeling code. Need to complete demand model notebook training and the demand model output adjustments and guardrails to get her prepared to work on her first project which will be Uniform demand modeling. Training sessions are being recorded and are accessible here:

E-Commerce:

Prioritizing the addition of the Epsilon Spend Data, and Data of if a consumer has selected a sailing as a favorite / watched sailing for new predictors in our models.

Also working on enhancing the calculator which guides the business user to the actual output data file from the SQL generated in the UI, based on number of records the business user wants to return along with any models that they want to use in combination (i.e Combination of Booking Propensity Any Destination with a Destination Specific Next Best Destination Selection to enhance targeted offers lift)

Loyalty (from Carlos):

Maintaining future sailing generator, using similar ship spending behavior to model spending on future new ships,

Marine:

Substantial knowledge transfer sessions due to Jong's departure surrounding MIAP AlphaPlatform package. Additional knowledge transfer and onboarding of Arya Cheeti, Intern, who began development work for automated anomaly detection to be used in data validation and saving hunting.

Machinery model placed into production after bug fixes in AlphaPlatform package to remove effects of multi-collinearity between features. Initial review of machinery outputs have identified significant energy deviations that must be further investigated on three ships.
