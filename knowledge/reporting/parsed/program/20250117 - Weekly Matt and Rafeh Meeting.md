**Proud: **

- **Generative AI Medallia project:** DS Team formally presented “Text Summarization” tool capabilities to CEL Onboard & Marketing teams with positive reception. *Team also finished developing a PoC** **Streamlit** app leveraging Databricks Lakehouse Apps to create a friendly front-end UI for business users, developed an **approach to explain low-NPS sailings**, and will be discussing next week to expand coverage of our text summarization tools to summarize Q**ualtrics** feedback for CEL**. *

- **Loyalty**** & CLTV****:** Delivered preliminary power analysis & testing recommendations for Pilots 1a and 1B (Taste of Tier) and Pilot 2 (Rewarding Spend) to the Loyalty Steerco and Working groups this week with positive feedback. Next steps will be to refine testing recommendations by expanding the test to include lower-spenders (in addition to high-spenders identified through our CLTV spending-index and rolling 2-year spend thresholds from the Loyalty Simulation). *Team is enhancing the underlying onboard revenue data used for the Loyalty Pilots, validating SSC onboard and land spend for the Loyalty Simulator, and improving the logic used to allocate indirect costs*

- **PROPEL:*** *MLOPs team has extended coverage of PROPEL offers to nearly 85% of the CEL Fleet, and just launched the solution of Eclipse and Millenium*.* *Team is actively working on offer enhancements (integrated **shorex** logic and dynamically adjusting offers based on sailing-length) and achieving expand-coverage of PROPEL offers to **sailed** guests by reducing the size of control groups from 50% to 20%.*

- **Revenue Management ****(CEL):** The DS team presented the new CEL MTRB Track Optimization algorithm to RM leadership with highly positive feedback. The new CEL version is a major enhancement to the RCI model, as the algorithm optimizes load factors and ticket revenue (in addition to incentivizing sailing alignment) and could have up to a $30M impact on CEL Ticket Revenue if the new load factors can be achieved. *DS Team also delivered **PRE fixes** for stale-pricing and continuing to work on updating Category Gapping (GTY-Lead) optimization model based on business feedback and implementing new PRE inversion gapping business rule logic.*

- **Revenue Management (RCI): **

- **Data Science: **The DS team delivered targeted enhancements for the MVP Sailing Performance Index (SPI) model that address key edge-cases and received positive feedback from RM. Team shifting focus to created SPI-guided business targets (e.g. optimizing track, setting FIT/group and Trf/T4 pricing gaps, and using for automation uplift metrics). *DS Team is **also continuing to work on PRE capped pricing & inversion gapping business rule adjustments, **PRE explainability waterfalls charts, **developing a new PoC pricing elasticity models, updating Category Gapping (GTY-Lead) optimization model based on business feedback, and developing updated ADA compliance rules for berthing automation.*

- **MLOPs:** MLOPs teams delivered Automated Pull Request Checks, which will reduce the number of errors that make it into our production environment. *Team continuing work on migrating RM data over to Unity Catalog from scheduled ADF jobs (reducing costs).*

- **TechGPT****: **MLOps teams are ready to deliver TechGPT. *The **TechGPT** container apps are ready** with the code-blocker functionality removed** and waiting for SSL certificates and URL.*

**Excited:**

- **E-Commerce:**** **DS Team setup and tested new Databricks Genie designed to help marketing stakeholders interact with customer targeting model outputs. *Working to educate **and support marketing team**s** to** correctly** use **the propensity **models** in marketing campaigns.*

- **PCP Pricing Automation:** DS Team is kicking off pilot testing for pilot RCI pricing recommendations for Perfect Day Cabana products. *Team is now actively beginning planning next phase to expand pricing recommendations to RCI + CEL Alaska **ShoreX** projects, targeting a delivery date near end of Q1/early Q2 to boost PCP revenue for the 2024 Alaska season.*

- **Revenue Management (SSC):** DS Team completed last changes for final round of PRE feedback. Actively working with SSC RM teams to discuss pilot testing (discussing a 3-4 month testing periods) and performance testing on the new pricing upload functionality.

- **Supply Chain:** Responded to follow-up questions by the Capital Committee and completed engineering work on a new Silversea dataset unifying monthly demand forecasts and spending data.

- **Win-on-Waste:** Expanded coverage to include a new Specialty Dining Venue (Teppeniaki) and now focusing on improving MDR forecasting + expanding coverage to additional specialty dining venues. *Testing mostly complete on** MVP** Main Dining Room demand forecasts and will productionize new models after business teams fix menu metrics (TBD).*

**Concerned:**

- **Loyalty & CLTV: **Aggressive timelines and understaffing are becoming a concern for delivery sustainability. The team just received all the necessary CEL data from Revenue Planning and is expected to still deliver insights by next week to a Steerco meeting, in addition to providing revised estimates for the Loyalty Pilots. The team ultimately needs either (a) an extra experienced hand from the BCG teams to help in Loyalty Pilot design or (b) to extend the delivery schedule to provide enough time to accommodate the dual needs of the Loyalty & CLTV projects.

- **Revenue Management (RCI): **DS Team’s key focus this week is completing an emergency fix to get the Pricing Recommendation Engine off Colonial & Optimus pricing data and use-Live Pricing data, which have caused problems with outdated pricing and ultimately resulted in PRE being paused this week by Revenue Management. *The team is working with Revenue Planning to ensure stable pricing data next **week, but** expediting migration of all pricing automation projects to Live-Pricing data** by end of next week**.*

Cihan
- Developed approach to testing GenAI solution by attempting to explain low performing sailings
- Created 20k row dataset containing consumer complaints about beverage package prices for Evan/Gaby
- Adhoc presentation preparations for readout with Evan
- Met with Gaurav to learn App development process

Gaurav
- Developed streamlit app leveraging Databricks Lakehouse Apps to put a frontend on last weeks Similarity search logic. 
- Will continue to add new filter criteria and summarization capabilities. 
- The app will be designed to be fully self serve. 
- Built-in security features allow for user access controls. Will likely still need to check in with info-sec on sec compliance of apps deployed via Databricks. 

Mireille 
- Version1 of ForYou MyCruise recommendations will be based on popular products at the segment level.
- Mireille is assisting with segmentation logic which is a booking level rule based segmentation of Age and pax count. 

Cristian
- Recommendations for add-to-cart module and product-detail-page (PDP) have been deployed on dev API. 
- Included various input validations to handle errors.

Parimala
- Successfully tested the CTI Celebrity Lead Conversion model in the prod-alpha-d2ai environment; all current functionalities are working as expected.
- Erick to schedule deployment alignment meeting with IT. 

WOW Updates:

Ayon
1) Added Teppeniaki for specialty
2) MDR hybrid is developed and tested -- status : waiting for business to fix menu metrics so we can productionalize

Alex
- After taking a look at the MDR pipeline back test results, moved on to adding additional forecast logic
- generating a min and an avg forecast using the ~8 overlapping predictions leading up to the final prediction day, with Gourish
- Using historical data - determine the best forecasts by item popularity rankings, use this to determine the logic for forecast switching
- Addressed an absent meal period issue
- Turned the experimentation notebook into a production ready NB
- Presented prior forecast vs new forecast - improvement on prediction error
- Investigated causes of previous forecast error 

Gourish
1) Added 8 additional forecast for specialty 
2) created Rule-Based Engine
3) Utilizing data analysis to develop a solution for correcting inaccurate predictions.

Loyalty Pilots: Conducted Power Analyses on Pilots 1a and 1B (Taste of Tier) and Pilot 2 (Rewarding Spend), to get initial sizing and recommendations on feasibility. Pilots 1a and 1b were presented to the steering committee, whose feedback included broadening scope and size of testing populations to include more than just the highest spenders. Adjusted numbers for pilot 1 and pilot 2 will be presented in next week's steering committee. 

Additional improvements to the pilot data sets include:
1. Corrected data sources from onboard revenue teams
2. A New version of the spend index that relies on spend vs. expected spend. Expected spend is calculated with a machine learning model, as opposed to performance against similar guests on the sailing. This will not only enable us to identify high value guests but also to use the index as a KPI in our pilots, since expected spend comes from a pre-trained model and not the guests on the sailing that also received the treatment.

Loyalty Tier Simulator: Concern on validating SSC onboard and land spend. Data Engineering was able to gather data on both of these and have been working closely with the business but are struggling to validate the revenue amounts. It has been difficult to find the right individuals in the business to identify and explain the logic needed to get the data right. 

CLV: There has been considerable progress made since the previous steering committee to improve the logic on the allocation of indirect costs. CEL data is in hand as of 1/6/25 with an ambitious goal to integrate the data in time for a meeting with CEL leadership next week. The purpose of this meeting will be to get any feedback from the brand prior to the next steerco meeting.

**RMA**

**Automated Pull Request Checks:*** (Javier)* the functionality for many of the checks is now complete and comments are added to the code in the PR automatically.  Now the focus is on implementation since the checks must run against other repos not code within the same repo.

*Benefit: *fewer errors make it to production. Encourage standards and best practices seamlessly in the development process.

**Bugfix: (Satheesh & Glen-Erik) ****mulitple**** processes were updating the same dataset/table. During some period of time during each week the mkrp_****rmd.v****_availability_history_l15w was pointing at stale data from 2023 until other processes would run and replace that reference.**

**UC Migration: (Satheesh) Two views using ****v_availability_history**** are in progress and should be in QA next week. *****Note: RCGGPT is taking precedence over Eswar's time until this is launched at the end of January.***

*Benefit:* after the views are created the code can be refactored to use those views and shut down copy data activities from ADF.

**PROPEL **(Alejandro):

**Ship Launches:** Currently 85% of ships have PROPEL. Celebrity Eclipse launched Jan 2nd and Millenium launched Jan 16th.

**Moving to full coverage (away from 50/50 test control):**

**Celebrity Beyond is running 80/20 test control as the first pilot ship to do so.**

**The overall strategy for full coverage is aligned. Test/control at the product category level. More analysis must be done to determine sizing.**

**Technical Improvements:**

**Integrated ****ShorEx**** logic and sailing-length-based adaptations to dynamically adjust offer eligibility based on voyage duration. ****A celebrated achievement by Alex and team.**

*Benefit: *ability to apply offers to specific times during the sailings regardless of how long the sailing is (dynamic).

All configurations are now done in sharepoint lists for all ships.

*Benefit: *moving to database tables instead of excel files eliminates many opportunities for human error and production failures.

Creation of access groups for SharePoint Lists at the ship level and cross-functional control.
*benefit*: Improved control and access management across different ships and teams, minimizing human error.

Creation of landing page for RMDs.
*benefit*: Easier access to all propel-input information, with a future capability to display important updates to the Team Onboard.

Creation of offerings for Starboard.

Initiation of sampling planning under new 80/20 distribution model.

Initiation of production deployment for control/test at 80/20 in BY.
*benefit*: Live validation for the 80/20 distribution model in BY, ensuring accurate results and identifying necessary operational adjustments.

Fault Tolerance Mechanisms Added to Propel Jobs
*Benefit: *Enhanced system resilience by introducing automated error handling and job retry strategies.

**PCP **(Alejandro):

Load testing on endpoint for production environment.
*benefit*: Ensured robustness and scalability of the endpoint in production at 2.5k RPS.

**RCGGPT / ****TechGPT**

Code blocked bug fixed (not deployed to production yet) *(Eswar)*

Removed code blocker for TechGPT *(Eswar)*

TechGPT container apps ready, waiting for SSL certificates and URL* (Marcio)*

Document upload: the OpenAI functionality only supports image files, it does not support.docx, .xlsx, .txt, .rtf, .pptx. Parsing the documents and pasting the contents as a prompt would be the only way to support some file types. *(Alejandro)*

**Hiring**

Screened candidates and had 5 complete the take home assignment. 4 tests pending review.* (Glen-Erik)*

Update for GSCBP
1. Completed work engineering new dataset for Silversea unifying the monthly demand forecasts for a product/ship, with the purchasing dataset from the Silversea Spend Report, and calculating the median value from the AI Demand model, average monthly purchase quantity, and average monthly consumption along with the absolute percent error of this median value for the backtested month from these three data points, relative to the actuals in the backtested month. 
The MAPE from this new approach (second column in below table) is better than the other Silversea challenger models, but is still significanly higher than our AI model
Month MAPE_Using_AI Forecast MAPE_Using_Median of AI Forecast, Purchase Qty and Consumption MAPE_Using_Last_Month Challenger Model MAPE_Using_3_Month_Avg Challenger Model MAPE_Using_12_Month_Rolling_Avg of Consumption
12/1/2024 37.37 48.88 85.37 67.69 57.22

2. Fixed error on Uniform pipeline that was occurring on table that contains voyage demand and monthly voyage demand. This is to have a temporary solution on excluding celebrity data. The table is accessible under dev_datascience (UNIFORM_SUPPLY_MODEL_BEFORE_SUPPLY_VALUE_CALCULATION)
3. Working on adding the additional columns Yan wanted by joining spend, demand, and consumption
4. Temporary fix on price scraping error due to several websites that can no longer be found and returns an error.

Update for E-Commerce
Models maintenance: 
• Plan with Kiran in how to use (and get in alpha) new emails promo tables.
• Setup and test new databricks genie designed to help marketing stakeholders to interact with models output
• Educate and support marketing team in correct ways to use the models.
