Kevin

Loyalty:

Data Warehouse is having issues with etl pipelines that build intermediate aggregated tables on onboard revenue that are used by Austin Schladant to create the tables used for loyalty pilots. Austin is able to tie to total revenue dollars, but the spend cannot be assigned to a booking. This has caused a minimum two week delay on generating early peeking outputs from the first sailings of the "Spend to Save" pilot, but does not affect FCC issuance. Ricky has resolved most issues in Alpha tables but they still persist on Oracle where Austin's workflows exist. Even with the fix provided by Data Engineering, there are still issues with recently completed sailings, that will likely cause delays throughout the pilot process. Data Science team has prepared a temporary analysis using end of voyage reports and FCC files with Austin's help. This allows us to get APDs by spend category as a whole, but does not allow us to understand the distribution of spend.There has also been additional analyses completed on cross-brand sailings, but findings must be altered due to the data quality concerns.

Kevin

CLTV:

Continued use-case roadshow with follow ups for loyalty, RM and OBR teams. Defined CAR roadmap in collaboration with corporate strategy and data engineering including timelines for all-phases of work to be completed.

Ben and Camila

Supply Chain: Integrated Business Planning (IBP)

Key Accomplishments:

• Demand Forecast Accuracy: Advanced our Order Creation process for RCI/CCI, refining demand forecast allocation methods to better address product unavailability across sailings and improve procurement planning.

• Data Integrity: Ongoing collaboration with Data Engineering to address persistent Silversea data issues (truncated/unrefreshed data); regular documentation and escalation are in progress.

• Enhanced Guardrails: Implemented new controls for Medical, Uniforms, and Cococay by comparing month-over-month predictions, increasing forecast reliability.

• Pipeline Enhancements: Expanded analytical pipelines to include new columns as requested and developed a SharePoint integration for seamless data sharing; delivered an updated model results version.

• Model Maintenance: Identified and troubleshooting errors within the Uniforms forecast pipeline (related to output files and missing backtest dates). Actively developing a new Cococay consumption model.

• Data Delivery: Delivered Silversea cabin, guest, and voyage-related forecast tables, and initiated work on RCI/CCI inventory depletion analytics.

Ben and Camila

Supply Chain: Integrated Business Planning (IBP)

Planned/Pending Initiatives:

• Leveraging AI to trigger email notifications based on model results.

• Developing volatility reports to highlight forecast shifts for specific ship/product combinations.

Ben and Kevin

Customer Lifetime Value (CLV)

Key Accomplishments:

• Resonate Dataset POC Restart: Re-engaged CLV, E-Commerce, Data Engineering, and external vendor Resonate to restart the previously shelved Resonate dataset POC. Confirmed licensing flexibility, unlocking broader dataset usage compared to alternatives.

• Strategic Analysis: Conducted and delivered a new analysis uncovering a previously unidentified, significant relationship between Net Promoter Score (NPS) and CLV—a departure from past corporate strategy findings.

Ben and Kevin

Customer Lifetime Value (CLV)

Planned/Pending Initiatives:

• Deep dive analysis to quantify the impact of NPS fluctuations on CLV at the guest and brand levels.

• Sensitivity analysis to identify incremental CLV gains per NPS increase.

Carlos

E-Commerce

Key Accomplishments:

• Completed baseline feature engineering from targeted offer data.

• Initiated uplift model training for measuring targeted offer effectiveness.

Carlos

E-Commerce

Planned/Pending Initiatives:

• Meet with the E-Commerce data team to further improve targeted offer feature set.

Mirielle

Contact Center

BKTOCX (Contact Center Data Pipeline)

• ETL Monitoring: Developed ongoing ETL monitoring framework, resolved data mismatches, implemented zero-lead conditional scoring, and enhanced sequence ID tracking.

• Data Alignment: Preparing for a full SBCXED data refresh and alignment to support subsequent ETL and SFTP testing with the Siebel team.

Mirielle

Contact Center

Next Steps:

• Finalize SBCXED data refresh to enable ETL enhancements, live monitoring, and SFTP transfers.

• Configure and debug the hourly ETL trigger.

Mirielle

Contact Center

Workforce Planning Simulation (North America)

• Data Preparation: Secured access to critical Power BI reports, completed dataset mapping, and initiated data migration for automating the Excel-based workforce planning model in Databricks.

• Process Improvement: Initiated call volume analysis, identified department labeling sources, and opened a Jira for ongoing data needs.

Mirielle

Contact Center

Next Steps:

• Develop proof of concept in Databricks to automate staffing calculations.

• Investigate interim solutions (“Plan B”) for office shrinkage data accessibility.

Ben

Contact Center Learning Leadership Conference

• Participated in strategic discussions regarding AI-driven performance coaching content for the upcoming Learning Leadership Conference. Awaiting final determination on scope and role for our participation, as leader availability and approach are under review.

Mert

• Optimized compute for automated voyage phase, port, and leg identification algorithm.

• Interviewed candidates for SY Stability CAR.

• Performed labor budgeting for MIAP Phase II and III CARs.

• Met with Valmet to negotiate the MIAP Phase IV quotation.

• Deployed Allure to MIAP.

Reza

• Updated IC model/baselines for HVAC and HOTEL due to m_pow_fan_fcu_total power correction.

• Working on the pipeline for electrical power consumption anomalies within the HVAC Diagnostics Platform.

• Attended meeting with the new build team regarding ongoing R&D projects.

• Updated the QN ship model for the HVAC area.

• Attended the energy-saving meeting concerning IN.

Ram

27th May

• Worked on the Python script for the ENIRAM API, modifying concurrency logic from chunk size to a combination of day length and chunk size.

• Conducted tests across various scenarios and communicated with the ENIRAM team via email, sharing error logs, execution times, and suggestions for improvements.

28th May

• Implemented changes to the logic on the ENIRAM side within Databricks, based on team feedback.

• Attended a seminar on Couchbase DB.

• Reviewed the workflow bundle deployment process through an instructional video.

29th May

• Currently working on transitioning the load factor dataset from QA to production.

• Preparing to move historical data to production before executing the pipeline.

Will

23rd May 2025

• Continued working on MGO equivalent features.

27th May 2025

• Fixed a bug in the power plant results notebook that caused FAT ISO SFOC calculation to fail.

• Further optimized code that combines individual ship dataframes into one resultant dataframe.

28th May 2025

• Completed MGO equivalent features.

• Met with GMO app development team to discuss requirements for dynamic rules in the web app, allowing more flexible dropdown filters on plots.

• Began testing MGO equivalent features.

• Fixed a bug accessing the config YAML file from the power plant master notebook.

29th May 2025

• Continued testing the implementation of MGO equivalent features.

• Fixed incorrect mapping of VY fuel temperature files.

• Discovered missing fuel temperature data in flow meter 1 and 2 tags in Eniram flow; contacted Eniram regarding a possible fix.

• Removed RD from the power plant analytics workflow until Eniram restores the missing fuel flow meter tag.

• Added fuel cell power to total power feature.

• Started working on the power plant model for the Fuel Forecast project using new MGO equivalent features.

Brendan

Completed:

• Deployed initial Propulsion Hull Degradation Model to production.

• Created visualization for hull degradation across all ships by coating type and dry dock date; working to deploy it to the GMO app.

• Performed ad-hoc analysis of propulsion power changes on IC with Mert for the Chief Engineer.

• Brainstormed with DE team member on techniques for backloading large amounts of data from the Eniram API.

• Assisted DE team member in troubleshooting Databricks asset bundle deployment.

• Had a collaborative discussion with the MIAP team about our dynamic modeling process and its application to dynamically set baselines (instead of using the current manual/static method).

• ChatGPT Usage Chargeback POC: Collaborated with Utkarsh and Eswar to create a methodology to track API usage and costs at team and project levels (work in progress).

Brendan

In Progress (Next Week):

• Add updated dry dock details to configs for the propulsion hull degradation model.

• Add multithreading to the hull degradation visualization endpoint to reduce response times.

• Complete the first phase of the ChatGPT Usage Chargeback POC.

• Deploy the hull degradation visualization to the GMO app.

• Create an API endpoint integrating propulsion dynamic model predictions with adjustments from the hull degradation model.

• Save tables for hull degradation results for GMO team usage.

Mashad

• Following up with the ship, saved 800 kW in AHU power consumption for WN.

• Addressed excessive power consumption issues in IN AHU, WN pump, HM Hotel, and SY Hotel systems.

• Analyzed ship events and incident datasets, focusing specifically on fire incidents, power loss, and life-saving events.

Ayon

WOW updates 5/29:

Team worked to:

1) Add ICON specialty restaurants

2) Add ICON MDR

3) resolve OOM issue with existing cluster

Henry Drescher

Accomplishments:

[Cresta]

Finalized supervisor dashboard for RCI – track cresta impact and optimize features.

Finalized supervisor dashboard for CEL – track cresta impact and optimize features

Finalized new hire dashboard design – track cresta impact and optimize features

Provided insights to Cresta on changes for auto summary, genKA and use case performance optimization. - Increase auto summary and genKA usage.

Sent first data transfer

Henry Drescher

Accomplishments:

[Conversational IVR]

Royal deployment for FAQs, post cruise changes, casino routing outwards

Knowledge transfer on how analytics reports work from Jesse to Jake

[Workforce planning]

Reviewed international team the call volume forecast for 2026 and FTE needs

Henry Drescher

What is currently being worked on:

[Cresta]

Avaya upgrades to resolve Cresta issues

Data validations for cresta dashboards

Data reviews for optimizations

Data transfers

Analyze the Cresta data dump now that resolution rate fixed

Henry Drescher

What is currently being worked on:

[Conversational IVR]

Celebrity UAT for River, loyalty grammar changes and FAQs. - expected to increase minutes automated by 10%

CoPilot Migration contracts

HCL vendor onboarding

HCL T&M contracts

Update analytics for the IVR for booking details task, new FAQs, new routings

Continued UAT for RCI

Copilot backlog development, potential FAQs, generative AI, new self-services and multi-modal use cases

Creation of analytics once on coPilot studio

Henry Drescher

Blockers

Latest data dump from Cresta

HCL vendor onboarding

HCL T&M contract sign offs

Avaya OneX integration

CoPilot Contract Signature

IT team post go live support for CoPilot

Knowledge base setup for generative AI use cases on coPilot Studio

Erick Alfaro + Cristian

# Recommender

- Team worked extensively in testing API performance to confirm API response frequency and speed.

- Eventually managed to work with Databricks to increase prod workspace level API request limit to the previously established 2.5k RPS.

- Also tested the Route Optimized API endpoints which natively support use cases with high throughput and low latency. We will have to consider moving to a Route Optimized endpoint eventually. The only difficulty is that Route Optimized endpoints only work with Oauth which is a hassle to implement for front dev team.

Erick Alfaro + Parimala + Gaurav

# Medallia GenAI

- Composed two sets of automated reports for Evan. First report is a sailing level report which has also been shared with Royal. Second report is a fleet level report which summarizes all sailings across at the ship level in a given month.

- Met with Steering Committee and prioritized next 30 days of deliveries. Focus is now on integrating Guest Service log into Medallia reporting.

Erick Alfaro + Parimala

# Lead Scoring

BKTOCX

- DE will be providing DS with new UC tables containing near real time data refreshes. The is a short term and a long term solution. Short term involves DE creating a job that will connect via JDBC directly to oracle and retrieve data for DS via an intermediary table. The long term solution involves setting up Lakehoue Federation.

- Will need to make a final update to BKTOCX pipeline to adjust for changes to Ingestion process as mentioned in previous bullet point.

- Will need to set up Siebel with a mapping to new incoming lead categories. Without setting up siebel with the mapping for Mireilles files - the incoming data is rejected.

Erick Alfaro + Parimala

CTI

- DE will be providing DS with new UC tables containing near real time data refreshes. The is a short term and a long term solution. Short term involves DE creating a job that will connect via JDBC directly to oracle and retrieve data for DS via an intermediary table. The long term solution involves setting up Lakehoue Federation.

- Will need to make a final update to CTI pipeline to adjust for changes to Ingestion process as mentioned in previous bullet point.

- Once new data is made available and integrated - all other parts of prod process will be ready to test end to end.

Atefeh

RCI | Dynamic Binning Strategy for WTS Based on Booking Density on VPS Data

The goal of this algorithm was to develop a dynamic binning approach that adapts to demand patterns using a scoring function. The score is defined such that a higher score reflects a strong concentration of demand over a shorter range of weeks. This enables us to identify dense demand regions and assign smaller bin sizes accordingly. I Explored bin ranges using bin size lists like [1, 21] to allow flexibility in bin adaptation across different meta products and cabin class combinations. The algorithm iteratively evaluates all allowed bin sizes (e.g., from 1 to 20 weeks) starting from the current week (WTS pointer). For each possible bin, a score = average normalized demand / bin size is calculated. The bin with the highest score that satisfies a minimum total demand threshold is selected. Once selected, the WTS pointer moves to the end of that bin and the process continues until the full WTS span (e.g., 70 weeks) is covered.

I Compared average price (avg_vps_laf_plus_nccf_apd) instead of using weighted average price using standard bin sizes (e.g., fixed bin size = 5) versus the dynamic binning strategy.

Tested StandardScaler normalization. Although R², RMSE, MAPE, and SMAPE metrics did not show significant improvement over fixed binning, the QQ plots revealed reduced nonlinearity. MLFlow Logging of Training Metrics: For each meta and cat class, the model is saved along with its metrics and artifacts

Bernard

RCI SPI Factor Model:

Groups:

•Group targets revised with updated SPI scoring methodology

•Group booked position 5-10 percentage points greater off-peak relative to peak.

•Sweet spot for groups between 15-20% booked position off-peak and 10-15% during peak.

•Group/FIT APDs ~5-10 percentage points higher during peak relative to off-peak.

•Target between 60-70 off-peak and 70-80 for peak season.

•Association with SPI less significant compared to group booked position.

Bernard

RCI FIT Track:

•Updated track model to weigh recent years more heavily (exponential decay)

•Demonstrated that model generated tracks adhere very closely to historical high-performing sailings across meta product, WTS, booking WOY, category class, ship class, sailing nights, and RDSS product code.

Bernard

CEL SPI Scoring Model:

• Updated SPI scoring methodology to more heavily weight recent years (exponential decay)

• Recent shift in business practices such as greater emphasis on T4 demand better reflected in new SPI model. Specifically, spring break and summer are now more offset relative to off-peak season due to extra T4 volume.

• After validation of scores by CEL rev strat, focus will begin on integrating work into MTRB and starting on SPI factor modeling

Doug

CEL | FIT Re-berthing

The pipeline was fully built and tested successfully in the development environment, with final product team feedback pending (May 23, 2025).

Successful testing was confirmed in QA, followed by minor adjustments in the development environment (May 28, 2025).

The reberthing algorithm was completed and deployed into production (May 29, 2025).

Occupancy and category corrections were incorporated into the system.

There were no delays during the process, and no potential future issues were identified.

Doug

RCI | PRE Outputs to Unity Catalog

Identified 38 million rows needing to be moved into Unity Catalog; developed an ETL pipeline for this process.

Completed coding of the pipeline and prepared for testing in development (May 27, 2025).

Development testing was successful; preparations began for QA testing (May 28, 2025).

QA testing confirmed successful deployment; system went live for the June 2, 2025 PRE run (May 29, 2025).

A one-time process to transfer the entire PRE history into Unity Catalog will be executed on June 3, 2025, prior to price uploads.

Going forward, PRE price uploads will also append to the history table in Unity Catalog (prd_revenue_mgmt_bu.pre_rci.pre_archive_hist).

There were no delays during the project, and no potential future issues were identified.

Jesse

SSC RM A/B testing: voyage selection

We are expanding A/B testing to include voyage areas outside of Alaska. Therefore, this ticket will be pro-longed.

Jesse

SSC RM Bookings Analysis:

Presented to Claire Mason and Teresa Ignacio and received constructive feedback on recent analyses to identify potential revenue leakage and "gaming of the system" by our Travel Partners.

Michelle Manfrini

RCI | CAT-GAP 3.0

- Met with business 5/28/25. Explored results with Eddie. Received positive feedback on initial cat-gap model. Will expand training data to include “all-above” bookings as was done for CEL model. Team requested plots of gaps to understand frequencies in historical bookings.

- Discussed implementation of 2.0 model. Eddie confirmed they are not waiting on any deliverable from my end. His team is in process of validating results and will integrate to TAP as soon as Alexa has finished.

- Reviewed revenue formula logic. Meeting with business again on Tuesday to further discuss how to apply model output for their use. Will introduce idea of incorporating track as is being done for CEL. Initial integration of model and optimization for CATGAP complete, will continue to update in following spring.

Michelle Manfrini

CEL | CAT-GAP 3.0

- Worked out formulas and proof of concept for integrating demand (track) into revenue optimization. Beginning to work into current model and optimization code, will continue in following sprint.

Michelle Manfrini

GTY-LEAD 2.0 | Maintenance and Monitoring

- CEL full implementation set for next week.

- Built out master sailing list and confirmed expectations from business. Adjusted functions to identify health metrics such as duplicates, nulls, sailing and category falloff, optimal gaps outside desired range.

- Table health metrics, row validation logs, and falloff dataframes are being saved to SharePoint in CATEGORY_GAPPING folder.

- Logs over 3 months old are deleted.

- In progress --> table specific validations.

Michelle Manfrini

CEL | IMPLEMENTATION OF BINNING STRATEGY ON MODEL USING VPS DATA

Developed a binning strategy for VPS price data based on demand patterns observed during exploratory data analysis.

The “weeks to sail” variable was segmented into three categories: close-in, mid-range, and far-out, each with approximately equal data points.

Tested various bin sizes per meta-product; smaller bins improved fit but increased prediction errors.

Identified an optimal binning scheme:

Larger bins (15–20 weeks) for sparser, far-out periods.

Smaller, balanced bins (5–10 weeks) for peak booking windows and closer-in periods.

The approach effectively balanced capturing booking trends with stable prediction accuracy across different meta-products.

No anticipated future issues with the developed binning strategy.

Kartik

Performed power analysis for T4 Test with T4 APD as the metric and will discuss findings with business team. Looked into number of sailings across Meta Product, Ship Class and Sailing list

Performed analysis for OBR Evergreen test across various segments. Looked at entire dataset and also just evergreen discounts and filtered other promos. Reported the results to the business team.

Doug met with Anastasia today and she passed along that she's been very happy with the help Karik's given her team regarding testing. Solid work and feedback getting tests up and running and monitoring progress. Great job!

Lamis

RCI | Elasticity-based Track Optimization

Developed multiple optimization models, including Linear Programming and Dynamic Programming.

Validated model performance using randomly selected sailings to destinations such as Alaska, Short Caribbean, 7N Caribbean, and Europe.

Created a Stochastic Programming Model that incorporates uncertainty in price predictions, generating a set of optimal track options within a confidence region.

Planning to close the track optimization task for May.

Further modeling enhancements will be pursued once a more refined elasticity model is finalized.

Feature Engineering: Bkg Woy - Bkg_wave_flg

I created a bkg_wave_flg column based on the bkg week of year where we are getting bookings that are higher than 90%ile for each meta, class, and sail_month. The column appears to be highly significant. Incorporating this feature in average increases the model metrics such as r2 from 0.55 to 0.79

Dave and Jake

RCI | Elasticity Upgrades

Created elasticities using newer elasticity approach and presented to business.

Z scoring price by Ship Class, Cat Class, WTS Bin

Transforming Y Variable (New Total BK over 5 Weeks) using Power Transformer (This is done on the entire dataset, not a groupby)

Fit using just a Ridge Regression (alpha=1) using transformed target regressor (with the PowerTransformer) as opposed to doing the Poisson Regression

as opposed to doing the Poisson Regression

R2 is higher, fits seem better. (Residuals are better distributed, Seems to be capturing more in the scatter plots as well)

still some oddness in it I have to dig into (Likely caused by the Z scoring of prices and not being a lot of data for that bin, etc)

Maybe it is what is needed to correctly deal with how much prices change by WTS as well as average bookings
