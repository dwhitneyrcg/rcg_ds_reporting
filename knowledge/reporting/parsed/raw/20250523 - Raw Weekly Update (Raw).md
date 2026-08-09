"

Henry Drescher

Accomplished

Integrated passanger forecast into call forecast and workforce planning model for International and Casino. - Impact is a more accurate forecast and satisfied business request.

Accessed Cresta data dump - Availability to assess feisability of replacing speech IQ with Cresta.

Approval for 2 new FAQs for Celebrity IVR (Check-in time and arrival time)

Completed agent ab test dashboard for cresta – allows us to to assess and improve on cresta based on impact to hit our 60s target.

Approval for supervisor ab test and new hire ab test methdology – allows us to assess and continually approve on cresta system to hit our 60s AHT reduction target

Identified loyalty issues with Celebrity IVR which will lead to a 12% increase in successful loyalty automations.

Identified a potential new self-service where we identify cruise details.

Identified a new user behavior – can be a potential fradulent activity and allows us to assess user behvaior for either system/data error or bad actor behavior.

Completed GenKA initial rollout for Cresta

Conducted feedback loop meeting for IVR – generates new FAQs and self-services to use; lead to the discovery of 6 new FAQs.

Henry Drescher

Working on

Cresta fixing summary issues (coordinating) - will lead to a near 100% usage up from 28%.

Updating to avaya one x and assessing impact – will allow cresta to handle first call

Converstaional IVR contracts – allows us to move forward with copilot and have continued support.

Cresta new hire dashboard – allows for assessment and improvement of Cresta

Cresta supervisor dashboard – allows for assessment and improvement of Cresta

Enhancements to conversational IVR dashboard using Jake as a resource

Transition of forecasting to Nico and team as well as modeling to enterprise ds team – allows for more scalability in process to more teams.

UAT for Royal IVR: FAQs, Disambiguation and casino transfer outs

UAT for Celebrity IVR FAQs, disambiguation and river cruises

Assess copilot studio and work with utkarsh and team to determine best way to setup knowledge sources.

Ayon Ghosh

WOW Update 5/22:

1) Ongoing development to include breakfast in MDR

2) finished ETL for cold start pipeline in MDR - developing features

3) completed first version of metrics for all implemented venues

Ben Fowler + Camila

Integrated Business Planning (IBP)

Key Achievements

• Finalizing EDA on “2× last-month” guardrail for demand models (completion today); results to be presented to Mario and Lauren tomorrow.

• Deployed new guardrail logic for HF&B forecasts (cap at 2× prior-month when exceeded).

• Updated Silversea backtested reporting to include all ships for April 2025.

• Revised Order Creation logic to compute days-to-next-container-load based on the next eligible load date for each product—foregoing previous market-name alignment—to better spread demand per stakeholder request.

• Established new repositories for uniforms, medical supplies, and private-destination data (CocoCay):

– Uniforms pipeline executed successfully; cleaned extracts and preparing final review for Sunday run.

– Medical model updates pushed; added historical-product filters and scheduled Sunday pipeline execution.

• Advanced CocoCay challenger models: filtered consumption data to CocoCay, introduced ship_name feature; observed MDAPE rise from 42% to 60%, now investigating passenger-focused features.

• Enhanced automated vessel-consumption reports with currency formatting and brand headers.

• Filtered 2024 training dates for the new medical model (aligned product set); Sunday pipeline scheduled.

• Drafted additional-columns notebook for Yan’s analysis; integrating into main workflow.

In Progress

• Finalizing uniform and medical pipeline tweaks and code pushes

• Completing CocoCay challenger steps: consumption-table filter and deployment-table rename

• Integrating the new analysis notebook end-to-end

• Preparing high-level model-performance report (baseline vs. challengers)

Upcoming/Pending

• Manus AI Agent, Genie-Databricks and Optiguide integrations

• Merging Silversea, Celebrity and private-destination brands; category clean-up

• Rolling out guardrails across all product categories

Carlos:

E-Commerce

Key Achievements

• Improved uplift models by removing sampling bias

• Added consumer-market, recommendation-threshold and “email-able” flags to both marketing-genie pipelines

• Built proof-of-concept for “trusted answers” via SQL functions in Databricks

• Completed EDA on targeted-offers table

Upcoming/Pending

• Ingest targeted-offers into training and scoring pipelines

• Integrate Genie with Epsilon (Phase 2)

Mirielle:

Contact Center

A. Leads-Scoring ETL (BKTOCX)

Key Achievements

• Parameterized child notebooks for six Royal and eight Celebrity lead types

• Parent notebook orchestrates scoring; outputs to Unity Catalog in S/H/M/L splits (CSV)

• Established conditional SFTP upload (transfers only when leads exist)

• Finalized data-format and file-naming conventions

• Built sequence-ID control logic and initial ETL-monitoring framework (ref-data snapshots, lead counts)

In Progress

• Pipeline refresh and data alignment with Kiana and Erick

Upcoming/Pending

• SFTP transfer testing with Siebel team

• Configure hourly ETL trigger; commence live monitoring and debugging

Mirielle:

B. Workforce-Planning Simulation

Key Findings

• Existing Excel model is manual: inputs (volume, AHT, shrinkage) drawn from Power BI/external files; updated quarterly and monthly

• Data granularity: volume/AHT to 30-min intervals (since 2015), shrinkage daily, headcount monthly (since 2012)

In Progress

• Identifying datasets to replicate in Databricks (pending Jason’s feedback)

• Drafting automation notebook for staffing calculations

Upcoming/Pending

• Explore web-based interface for real-time manager input

• Conduct weekly/daily analysis to refine forecasts and reduce abandonment rates

Kevin

Lifetime Customer Value (LCV)

Key Achievements

• Engaged e-commerce, revenue planning, corporate strategy and loyalty stakeholders on CLV progress

• Reviewed CLV codebase; scoped Medallia NPS data integration with Gaby and Jordan

Upcoming/Pending

• Define NPS-to-CLV linkage and feature engineering

• Develop Medallia-data ingestion pipeline and pilot analysis

Kevin:

CLV:

Conducted first round of use-case roadshow with RM(Tyler Rand, Bar Brieman, Irena Meyer, Brittany Briggs Dafnos), Marketing (Sam Riepe, Jill Weiss), E-Commerce (Jordan Corredera and Dhanita Rhamlochan) to circulate initial findings and identify areas in the business that could benefit from the tool. There is generally more enthusiasm from the Celebrity brand, as they know less about their existing customer base, but the Royal brand has found some potential implementations as well. There will be more roadshow meetings next week with OBR teams and a follow up with loyalty.

Had several deep-dive sessions with Kiana, corporate strategy, and Austin from OBR to better define the industrialization road map in preparation for a CAR to support the project.

Actively working on a second drivers analysis focused on what behaviors influence higher value index. The first round of drivers was focused on guest characteristics ("the who"), where this analysis focuses on behaviors ("The why"). This analysis is somewhat limited to what is currently available in the existing POC dataset. We are exploring potential gains from expanding the POC dataset to include things like OBR spend categories and AI/Rate Only.

We are also exploring the added benefits of external datasets (Epsillon, Resonate) and working closely with Kristin Villasuso and data warehouse to ensure long-term support.

Kevin:

Loyalty:

Prepared an update on PCP for in-market sailings. Developed analysis to provide "principled peeking" on OBS for completed in-market sailings (RF 5/16). There are current data quality issues in Austin Schladant's OBR tables that aggregate OBS, so we are awaiting resolution there before providing any updates to the steering committee on initial trends. This data quality issue does not affect source data or any of the processes to issue FCC's to the guests.

Updated choice benefit pilot to consider only post-covid guests at the request of the SteerCo.

Next weeks steering committee will focus on an update on early trends in spend to save, status-match across channels, and cross-brand guest spend behavior. Lauren informed me that the next pilot, will likely be on the topic of credit card spend, given the focus on the co-brand card.

Mert

Created a new algorithm to replace Eniram’s automated voyage phase and port/leg name identification.

IoT timestamped data now includes voyage phase (Port, Sea, Maneuvering) and arrival/departure port information.

The data is generated based on the ship’s distance to global ports, speed, and duration near the closest port.

This algorithm enables generation of expected weather data for ports and legs, as well as leg speed profile data for the Fuel Forecast CAR.

Interviewed 4 Data Science candidates for the Newbuild Stability Modelling CAR.

Assisted in preparing content for Rafeh’s presentation to GMO All Hands.

Provided general guidance to the MIAP team and their deliverables (Will, Reza, Mahshad, Brendan, Cathy, Wesley, Ram).

Will

5/19/2025

Completed refactoring of sfoc_results.

Created a notebook to combine individual ship results notebooks and save the combined DataFrame to the power_plant_analytics table.

5/20/2025

Implemented new model loading logic in the monthly SFOC report notebook.

Updated analytics workflow YAML for the refactored power plant pipeline.

Cleaned up the power plant analytics folder structure.

Tested different configurations of the new power plant workflow to maximize efficiency.

5/21/2025

Conducted testing of power plant refactor in QA environment.

Fixed various bugs in the power plant job configuration.

05/22/2025

Fixed bugs in the new power plant workflow where NO failed due to the power plant metadata table not being updated; now metadata is implicitly loaded via SQL query.

Productionized power plant analytics pipeline refactor, reducing ETL compute time by 56%.

Updated Factory Acceptance Test SQL table with test data for Nova.

Updated engine room mapping in PowerPlantConfigs.yaml for upcoming MGO equivalent mass flow rate feature.

Fixed error in sfoc_monthly_reports notebook related to loading diesel engine factory acceptance test models in the production environment.

Impact

Pipeline refactor reduced ETL runtime by 56%, enabling faster analytics delivery and better resource utilization.

Engine room mapping and SQL data uploads pave the way for future fuel forecasting model enhancements.

Reza

Completed and submitted the case study report for the new build project; presented findings to the new build team.

Finished proof of concept and testing for the HVAC diagnostic system focused on the AHU area, using the ship Wonder as a test case. Next step: replicate for other ships.

Fixed coefficient issue for the AHU system on the ship Icon.

Mahshad

Investigated ship fire incidents, identifying zones 6 and 7 as the most frequent locations, with primary causes being electrical faults and issues in the food preparation area.

Analyzed power consumption deviation (~700 kW) on WN; contacted ship crew and awaiting response. Resolving this could save approximately $70,000 per month.

Investigated AD power consumption deviation related to a chiller; observed a drop in the chiller’s COP and continuing analysis to determine root cause.

Corrected the formula for boiler fuel consumption power deviation.

Brendan

Completed:

Analyzed increased propulsion power demand at constant speeds due to hull degradation:

Found deviation is constant across speeds despite the cubic relationship between speed and power.

Determined ship position (Caribbean, Alaska, Australia) significantly impacts degradation rate, likely due to varying seawater solute concentration.

Created presentation on MIAP Propulsion model for GMO stakeholders.

Assisted IT developer in troubleshooting new crosser sync workflow in Databricks for automatic tag list updates to ships.

Fixed missing IC data in Machinery due to gaps in historical Eniram voyage phase data.

Updated baselines for MIAP Machinery power models (ships IC, MA, SY) in response to changing environmental conditions.

Researched ~500 kW machinery power consumption deviation for IC; found cause was lack of shore power in Miami since April, resulting in elevated consumption (non-claimable savings). Findings forwarded to Chief Engineer.

Ram

Resolved internal server error and rate limit issues with the Eniram API by coordinating with Eniram team and implementing recommended fixes.

Analyzed the remaining four Gangway notebooks, discussed possible edge cases with the team, and prepared them for production deployment.

Investigated and fixed frequent datatype and schema change issues causing MIAP ETL failures, now ensuring smooth production operation.

Aagam

EDA on GTY-Lead Gap Perc

This week I focused on seeing the interaction between the weighted score (helps to understand the gty and lead bookings along with gty_lead gap).

•	Ran a XGBoost Regression that helped me understand the impact of this score on the individual cat-class SPI score, without considering the interaction between multiple cat-classes.

o	Drawback: Did not consider the impact of other cat-classes on the SPI score of an individual cat_class

•	In order to counter it, I factored in for other cat-classes and ran a XGBoost model, that gave me better results and helped me identify some baseline targets.

•	Next Steps:

o	Factor in the pricing to further understand how gty_lead gap changes with change in price

o	Meeting with the business postponed till next week

Atefeh

RCI | Dynamic Binning Strategy for WTS Based on Booking Density on VPS Data

•	Analyzed booking density using a specific data table, calculating average bookings per WTS across product and cabin categories.

•	Detected inconsistencies and sparse booking patterns, such as low average bookings in certain segments.

•	Applied a moving average to smooth demand fluctuations and identify stable trends.

•	Established fixed bin size thresholds based on the smoothed demand data.

•	Assigned bin size labels to data points according to segment behavior.

•	Sequentially grouped rows based on these labels, re-evaluating partial groups if label changes occurred mid-bin.

•	Grouped remaining rows at the dataset tail into final bins.

•	Tested an alternative approach with a dynamic binning algorithm that adaptively selects bin sizes based on demand:

•	Calculated a score as the average normalized demand divided by the bin size.

•	High-demand areas resulted in smaller bins; low-demand areas in larger bins.

•	Restricted bin sizes to specific values (e.g., 5, 10, 15, 20) for smoother adaptation.

•	Rules set smaller bins for high demand, medium for moderate, and larger for low demand.

•	Currently evaluating both strategies on a newer version of the dataset.

Bernard

RCI | Data Driven Scoring Baskets

•	 Generated sailing baskets for RCI and delivered table (dev_revenue_mgmt_bu.mtrb.rci_baskets) on 5/15

•	Quantified data-driven basket similarity with heuristically defined baskets using:

o	Hungarian algorithm used in assignment problem optimization to match the data-driven basket labels with the business rules labels followed by using an adjusted normalized mutual information criterion score. Average score of 0.46 indicates good overlap.

o	Calculate average basket purity of data-driven baskets when joined by sailing to the rules defined baskets. An impressive 81% average purity was determined across the major meta products.

•	Reviewed findings with Eddie on 5/15. He will continue reviewing, but is happy with initial set

•	Data-driven basket algorithm includes only soft constraints and is still in proof-of-concept stage. Future refinement with business rules and hard constraints is likely.

Bernard

CEL | SPI Scoring Model Improvements

•	Refactored codebase to allow for brand/meta product specific normalization of SPI

•	Experimented with different normalization strategies, significantly reducing systematic bias in SPI scores as quantified through SHAP plots using XGBoost regression model to predict normalized scores.

•	Presented findings to CEL. Feedback is to weight recent years more heavily for seasonality analysis

Doug

RCI | Move PRE Archive & Exception Tables

•	Status: This ticket is complete as of 05/20/2025

•	Deliverables:

Weekly PRE archive and exception tables now being written to Unity Catalog.

•	Delays: None

•	Potential future issue: None

Doug

RCI | PRE Augmentation + Efficiency Improvements

•	RCI | PRE Inversion Business Rules Application

•	Status: The ticket was marked as complete on 05/20/2025.

•	Deliverables: The inversion issue has been resolved.

•	Delays: No delays occurred.

•	Potential future issues: None identified at this time.

•	Additional notes: Business is satisfied with current PRE performance regarding price inversions; any remaining concerns have been addressed through parameter tuning. A more comprehensive review of PRE inversions is planned as part of a future system rework.

Doug

CEL | FIT Re-berthing

•	Table privileges have been fixed, but investigation is ongoing regarding Utopia appearing in Celebrity data.

•	The table currently lacks read privileges needed to fetch data when executed in a pipeline.

•	The revenue planning correction for the PlusGrade table was completed, but it now contains fewer ships than expected; further investigation has been requested.

•	Efforts were made to combine occupancy and category correction processes into a single output, with coding and testing completed for de-berthing, re-berthing, and logging functionalities.

•	Validation data has been sent to the business for review and feedback.

•	An issue was identified where Celebrity revenue planning data for PlusGrade mistakenly contained RCI data instead; resolution is pending.

•	A plan is being developed to incorporate forecasted load factors to better identify low, medium, and high sailing demand.

Jesse

SSC | PRE | Final PRE upload table

•	Status: This ticket is complete as of 5/22/2025

•	Deliverables:

Input table bug repaired

PRE runs to completion

PRE Reservation Upload table passes all Data Engineering checks. It’s compatible with SSC Reservation System.

•	Delays: None

•	Potential future issue: None

Jesse

SSC | PRE | SSC Cryptic Re-bookings

•	Conducted a detailed review of basic input tables containing passenger and booking data.

•	Faced challenges linking passengers to booking IDs due to frequent recycling of booking IDs.

•	Successfully linked the relevant input tables.

•	Currently performing exploratory data analysis (EDA) on passengers and travel agencies that canceled trips and re-booked under different booking numbers.

•	The task is taking longer than expected, but progress is ongoing.

•	A presentation to stakeholders is scheduled for Tuesday.

Michelle

CEL | GTY-LEAD 3.0 | CATGAP Inter-category Gaps Stage 2

Inter-category tradeup model code

•	Status: The ticket was completed as of 05/21/2025.

•	Deliverables: A meeting with Anastasia confirmed the team is satisfied with the initial results; requested fitted curve plots to better understand relationships in data; the current model is being used for optimization.

•	Potential future issues: None identified.

•	Additional notes: The team is currently utilizing the GTY-Leads 2.0 trade-up model for Europe and the main meta model for the category gap 3.0. A separate optimization code was developed for Europe sailings, integrating the Europe trade-up model with other meta models for different trade-up levels

Michelle

V.1 - Optimization + Model integration into CATGAP

•	Status: This ticket is complete as of 5/21/2025

•	Deliverables:

Integrated all sailings into optimizations. Code written for main meta optimizations, minor metas using brand level models, and europe sail using euro specific tradeups. Met with business today to review logic and results. First version is approved. Next steps are to include track into optimization.

•	Potential future issue: None

Kartik

CEL | PERKS/NO PERKS AB TEST | Monitoring Analysis 2.0

•	Added Ship Class for 7N Caribbean offpeak and Short Caribbean 3N and 4N

Kartik

RCI | AB Testing | Sailing Selection Upgrades Q2

•	Investigated different libraries for the optimization

•	Researched GEKKO, Google OR tools, SciPy, Pyomo

•	Moved forward with Gekko because it has the best documentation and performance

Lamis

RCI | Elasticity-based Track Optimization

Model Testing and Validation on sample sailings where p(d) model is trained

Based on my discussion with the biz last week I made the following adjustments this week:

•	Tested the model on larger sample of sailings to include Alaska and Europe

•	Run scenarios where we start optimizing at a particular week to sail and at certain booked position.

•	Incorporate the uncertainty around the price prediction in the optimization framework - rather than the greedy approach-> Stochastic optimization. Pass price as a distribution rather than a point estimate to the optimization model.

Future adjustments and additional scope will be based on business feedback and discussions.

Lamis

Optimization Models with Price Uncertainty

•	Based on my discussion with the biz last week - I have developed a stochastic optimization model to account for uncertainty around the price predictions. In this model I am passing a distribution of the price (the mean is the predicted price point, and the sigma is based on the residuals) → this model generated multiple optimal tracks / in other words, a range within which the optimal track falls.

•	I tested this on multiple sailings including 7N CARIBBEAN, SHORT CARIBBEAN, ALASKA and EUROPE.

•	Visualized the generated tracks and will be presenting the results to the biz tomorrow.

Lamis

EDA on the current elasticity model o/p and feature engineering to upgrade it

•	This week I’ve been working on additional EDA and feature engineering that might improve the elasticity model specifically by leveraging web data and investigating latent demand vs the actual bookings (converted demand)

•	I performed cleaning by aggregating all web events (clicks or page visits) for each rwd_id (device), sailing_date and ship_code. Also, aggregated at the wts level in order to be able to compare against bkgs.

•	Computed the time a single device spent watching a particular sailing (from first event to last event) - to test/validate the hypothesis of the lagged response to price changes.

•	I noticed three consistent peaks in the latent demand - and are also reflected in the bkgs curves. These need to be investigated further in order to be incorporated in the elasticity model. My assumption is that these are based on promotions/marketing campaigns? Will discuss with the biz tomorrow.
