PROPEL: (Santiago & Javier)

Measurements:

Enabled measurements_granular_no_filter to provide unfiltered revenue views, meaning revenue is considered even when it is negative.

New Offer Template:

Pre-work readiness: copied all ship exclusion lists from prod to dev (cabin exclusion and offer exclusion lists). Also copied other configurations. Only pending offer config, offering, and category product mapping.

Production issues:

Art/Park West:  Investigated and identified the root cause to be a configuration issue, raised with OBR team and resolved.

Uplift model retraining failure: investigated and found uplift model is using the old measurements table and running on one ship. That ship will be turned off until the uplift model is redesigned to use the new measurements data.

Data Ingestion Auditing: Developed diagnostic queries to identify and resolve data ingestion failures, executing complex validation joins across the sku_mapping_across_tiers_bng, obr_total_revenue, offer_config, and obr_guest_manifest tables.

PROPEL Configuration App:

Finalized the UI for quota configuration and validations.

Designed comprehensive data architecture and application workflow diagrams.

Optimization:

Offer Assignment: Resolved performance bottlenecks in the Assign Offer pipeline, significantly reducing resource consumption by mitigating excessive data ingestion loads and deprecating unnecessary logging (prints). The current process takes 60-90 minutes per ship and is estimated that when finished with this optimization it will take 20-30 minutes.

PCP Targeted Offers: (Glen-Erik)

Launched Celebrity's second pilot using the Targeted Offers UI app. Offer App worked well. Hybris worked better than last time but still took many hours to process all of the records and after the notifications were sent, the fake accounts for testing weren't able to complete the purchase.

Targeted Offers UI App:

Added Audience and audience ID for tracking

Added control group stratification options in the app to ensure a balanced control.

Gathered required materials to start developing the Email UI.

Audience Builder App:

Documented requirements for SQL-based MVP and second phase feature selection to start development.

Eswar & Javier

Revenue Mgmt

TAP Refactoring: (Javier)

QA: ran ADF pipelines to test the refactored code.

Feature store: (Eswar)

Validated 6 new DEV views (ssc_daily_ship_sdt_category_farecode_bookings, ssc_daily_ship_sdt_catclass_farecode_bookings, ssc_weekly_ship_sdt_category_farecode_bookings, ssc_weekly_ship_sdt_catclass_bookings, ssc_weekly_ship_sdt_catclass_farecode_bookings, ssc_weekly_ship_sdt_sailing_bookings) against their PRD counterparts — none are a perfect match yet; consistent ~57% key overlap, 4–5% capacity mismatches, and CURR_* metric variances of 0.4–12% across all tables; root cause investigation needed on key population gaps and TOTAL_CABINS/TOTAL_PAX_CAPACITY logic. Shared this report to Data Engineering team to correct them.

Monitoring CI/CD deployments, helping with PRs (Eswar)

Eswar

Other Projects: (Eswar)

Demand Forecasting:

Integrated ETL, and transformation logic just before model training.

Optimized ETL and model training notebooks and productionized them.

Productionized OBR Web Scraping, Hotel Operations project

DOUGLAS

**CEL | T4 Testing Updates | JUNE**

This work item involved ongoing monitoring and analysis of the T4 AB test for Celebrity, with preparations for the final and near-term tests in progress.

The test time remaining for each meta/window was calculated, and a notebook was provided to the strategy team to estimate test duration and potential early termination.

The Bayesian measurements notebook was finalized and shared with the strategy team for stakeholder presentation.

Bayesian metrics and sequential analysis were planned for near-term test clusters, and a review with the strategy team identified underperforming sailings to be removed from analysis without affecting overall results.

MICHELLE

Rev mgmt.

·  The optimization logic was reworked to prioritize feasibility before attempting to hit target shares.

Previously, the optimizer would try to force alignment to ideal share targets even in cases where those targets were not achievable given the modeled demand.

This led to distorted decisions and unrealistic recommendations.

The updated framework first determines what demand levels are actually attainable from the model and optimizes within those constraints.

This change removes forced gap decisions and ensures that all recommendations are actionable in practice.

·  Another critical enhancement was the redesign of the penalty framework.

Penalties are now scaled as a percentage of LAF price rather than using fixed dollar values.

This ensures that the optimizer behaves consistently across very different sailing types, such as short Caribbean itineraries versus longer European itineraries, or interior cabins versus suites.

By aligning penalties with the underlying economics of each sailing, the optimizer now makes decisions that scale appropriately across the entire portfolio rather than favoring or penalizing certain segments unintentionally.

·  Significant work was also done to address the overuse of GTY as a fallback mechanism.

Previously, GTY could be heavily utilized as an easy way to force demand alignment, largely because penalties were too low and there were no constraints on total GTY share.

The updated optimization introduces:

A soft cap on GTY usage

A progressively increasing penalty once that threshold is exceeded

Differentiated penalties by tier, making GTY usage in premium cabins significantly more expensive than in lower tiers

This ensures that GTY is only used when it is economically justified, rather than as a shortcut.

As a result, extreme scenarios have been eliminated, with no cases exceeding 50% GTY share and overall recommendations becoming more balanced across cabin tiers.

·  These structural improvements directly address the root causes of prior optimization behavior.

In the earlier version, the combination of infeasible share targets, unscaled penalties, and lack of GTY controls created strong incentives for the optimizer to push demand into GTY in order to reconcile mismatches.

By correcting all three of these drivers—introducing feasibility-aware optimization, scaling penalties appropriately, and explicitly controlling GTY usage—the updated framework produces recommendations that are both more realistic and more aligned with revenue objectives.

·  I have been actively working on handing off key components of the project to other team members.

This includes walking through code structure, optimization logic, and pipeline organization.

These sessions are intended to make the framework easier to maintain and extend, while also ensuring that the logic is well understood across the team.

This includes reviewing how different modules fit together, how parameters are passed through the pipeline, and where key business rules are applied, so that ownership can be more broadly distributed.

·  I also met with the Celebrity team to review the updated results and gather feedback.

The initial response was positive.

The team requested more sailing-specific examples to support change management with product stakeholders.

ANNEKE

Rvg mgmt. ssc

**SSC PRE – Dashboard & Pricing Enhancements**

Update Jun 11, 2026:

**Post-Promotional Pricing Logic Enhancements (DONE)**

We met on Wednesday for the recurring weekly stakeholder meeting and reviewed the farecode target change, discount handling for post-promotional price enhancement, and the following dashboard requests which have all been put into production. Now when there is a voyage within 20 weeks to sail, the target for PRE will be the UL (last-minute) fare code which will avoid price changes that are too high and prevent the recommendations from being paused. The handling of percentage-based discounts was also successfully implemented in time for the promotion transition that Silversea recently had, transitioning promotions from absolute value discounts to percentage-based discounts. The logic for dynamically handling these is in the slide below.

**PRE Runtime + Production Stability (DONE): **PRE runtime was optimized to allow analysts a full 24 hours to review recommendations. This has improved the compliance to have pause reasons in on time for the run and allows for the dashboard to accurately report on approval rate, not a falsely inflated rate due to the run being before pause reasons were submitted and requiring rework to scale back exacted price recommendations.

**PRE Dashboard Evolution (Business-Facing) (SCOPE CHANGED**):All of the original scope of this subtask had already been implemented, I have changed the scope to reflect the work to be done for the Performance Visibility and Revenue Tracking Framework.

**Stakeholder Feedback Integration (Continuous Loop) (ONGOING): **We have the recurring stakeholder meeting every week now for which has received great feedback from the SSC team. I will continue hosting these and creating subtasks for any work to be done from these conversations, but closing this subtask for now as the feedback loop is enabled.

**Performance Visibility and Revenue Tracking Framework (NEW):** I also met with Eddie and reviewed objectives and we aligned on the scope of work for Silversea PRE that would be high value. That includes a Performance Visibility and Revenue Tracking Framework to **measure, track, and explain pricing performance. **This will include revenue tracking and track variance analysis and recommendation effectiveness metrics. With alignment from the SSC stakeholders, I started EDA on track variance metrics and developing what those metrics will look like.

**Featurestore**** Fixes (NEW): **In my EDA I found some faulty logic for load factor that was using the sum of the max capacity for all cabins in a voyage as the denominator. However, this is not correct because for a voyage for Silver Moon for example, the maximum number of passenger is 596 but with that calculation it was 672. This was causing us to underestimate the load factor. This fix is currently on my branch, should be in production next week. I also found a bug when comparing our currently booked passenger count to projected passenger counts in the track table. Our number that we were using for PRE was underestimating because of a join in the feature store table that was dropping rows. In the future I’d like to implement QA checks to ensure row counts are as expected.

**Pricing Algorithm Refinement (NEW)**: From our stakeholder conversation this week, Adrien requested that we make some refinements to the pricing algorithms. This includes capping the price changes for expedition cruises to a 3% price change because these already have a very high APD and a 5% price change is seen as too much for the business. Another avenue we want to explore is how we can refine the approach for a last-minute price change to close the gap between the last minute and all-inclusive fare codes over the remainer of the booking curve from the moment last minute fare code is opened. This is likely going to be more work than a 5-point sub-task but my goal is to have a first-pass approach for this by end of June.

Jesse b.

Rev mgmt. ssc

**SSC | PRE | Bootstrap-test upper-level suite model**

**Status**: This ticket is complete as of 06/10/2026

**Deliverables**:

Bootstrapping code that Data Science can utilize to test linear pricing algorithm for top-tier suites (as described in previous tickets)

**Delays**: Data Science management decided not to use bootstrapping approach. Therefore, this ticket should be closed, as optimal LAF, category gaps, and slope of price increase (over booked position) are not optimized for MEDT, CARI, ALAS, or NEUR area codes.

**Potential future issue:** We can resume this project if data science management changes their mind.

Streamlined EDA for XTR suites

The categories we should be evaluating should be driven by the EDA. The relationship between Veranda and lowest suite was brought up to explain the concept of testing premiums and booking relationships. The EDA should have identified where our biggest opportunities are, and what pricing relationships exist today as a starting point for our test.

The amount of price points the consumers are skipping over isn't quite as important as the difference between what the price of the cabin they upgraded into was versus the cabin they originally paid for.

Understanding which categories are being upgraded into (frequency by price difference discussed in the previous bullet point) give us a reference point to understand the following:

What categories can we increase trade up / increase revenue by managing the rates in a way that improves the relationship?

The floor being the price of the category we are setting the gap of the price from + the amount they've paid to upgrade into the category. This represents the "worst" outcome from a revenue perspective. Having a price lower than this doesn't make a sense even if they trade up.

What price relationships are we starting with? Being able to effectively communicate the changes in price to our stakeholders is important for the teams that are responsible for Revenue Management. Understanding that we have seen a X% of cabins that paid for a particular category at a premium of Y, how can we change the value of Y to see an impact to that % of cabins that paid for the category at time of booking vs Upgrading into it.

Aagam

PCP pricing automation

**RCI | PCP2 | CRF Automation - Apply Business Rules, Validation, and Production Deployment for Automated Pricing Pipeline**

This week, I began working on building the foundational configuration and data tables required for CRF automation. The CRF process is multi-step, starting with the CRF Offering, which is created three weeks in advance. This step involves pulling the relevant sailings for the sale, including RBC and PCC sailings, along with generating summary statistics for the flash sale.

My focus this week was on completing the CRF Offering which includes identifying and flagging the appropriate sailings (sailing in question, RBC, and PCC), as well as progressing on the summary statistics needed to complete the CRF Offering.

Once the CRF Offering is finalized, each product team follows its own process to determine discounts and populate the respective tabs. For this week, my primary focus is on the Waterpark product. I’ve taken an initial pass at automating the Waterpark CRF and have generated preliminary results. I plan to further QC these results and aim to close this out by the end of the week. Additionally, I will be validating the Waterpark CRF outputs with the business team (Mateo) to ensure alignment with their existing manual process.

Ignacio

PCP pricing automation

Further debug and clean FS for customer-level Beverage PRE with clickstream data
• After creating the initial feature store, even after lots of clean up, new issues were found with null data that should have been present as well as duplicates that were causing issues in the setup of the model training. This resulted in having to go back and debug the code further for the creation of the dataset
Make model improvements for CEL MNL Beverage PRE/DM
• The model was reconstructed into a more advantageous nonlinear model (rather than simple linear MNL model POC that the business team presented). The model architecture was created to be a LightGBM (objective as lambdarank instead of multiclass, providing better cross-elasticity and interaction/competitive effects across products affecting the probabilities of purchases for each product). This model will be able to predict the probability of a customer purchasing each of the different products, along with the probability of “NO PURCHASE”. A separate LightGBM model is to be trained for each different set of passengers (one for pax with clickstream data & another model for pax lacking clickstream data and purely based off the other remaining features such as transactions, pricing, historical propensities, and other sailing-booking specific feature). The model training joined lots of different data (transactional, clickstream, historical propensities, etc) and model training was set up with temporal cross validation and staged hyperparameter tuning using Optuna (stage 1 tunes structure). This process involved defining each unique “session”. For the LightGBM model using pax with clickstream data, each unique read date (for clickstream/transaction activity), sailing, and pax defined a session, where all products were flagged as whether bought or not in a ranked cross-elastic approach, taking all products into account at once for their interactions. For pax lacking clickstream data, sessions were defined the same way except grouped by WTS instead of read date now since there is clickstream data lacking in the dataset. A holdout test/validation set (20%) was also created for final validation of each of the trained models.
• Once the final corrections and cleaning to the last few bugs identified in the Feature Store, model training will be repeated. An additional possible next step is to also break out even more models, possibly expanding the number of models to be based off the number of unique meta product groups (6: SHORT CARIBBEAN, 7N CARIBBEAN, ALASKA, EUROPE, Aus/Asia, OTHER), therefore resulting in 12 models (2 different pax types x 6 different meta groups). This will potentially be done depending on how first pass model training performance results turn out.
**Recurring meetings with business team & OBR DS team****
**• Monthly kickoff meeting for DS team
• Meeting with the business team over gameplan to add a QA layer to the mas upload to better handle edge cases of accidental incorrect use by the business team (e.g. not specifying product codes, missing % off, etc)
• Meeting among those working on PCP on DS team sharing progress updates
• Meeting sync with digital BI team regarding the clickstream data use cases
• Sync with Kevin on CEL Beverage PRE – demand model & dilution model, both at a granular customer level
• Follow up with Rafa, Alex, and Gaby regarding the CEL Beverage PRE
• Meeting with Gang and the RCI regarding the RCI Beverage PRE

**Lance P**

**Rev ****mgmt**

**Create a high-level dashboard for model performance visualization**

**Images**

**Next steps are connecting the dashboard to live data in Databricks and not hosting it on a local data file. Also, adding ****the data**** for ****RC in**** too and not just Celebrity like currently.**

**Reply**

**Edit**

**Delete**

**Lance Pollack**

**5 hours ago**

**(edited)**

**2 of 3 tabs in dashboard completed (Bookings and Variance). Elasticity tab ****still**** left to be completed. About 80% done.****
****
Meeting with Celebrity team Tuesday (6/16) to introduce and get feedback on the new metrics and dashboard.**

**Lekha**

**Cel rev mgmt.**

**CEL | NEW PRICE CHANGES COMPARSION PLOTS FOR CEL Presentation**

**Status: This ticket is complete as of 6/11/2026**

**Deliverables:**

**Pulled and compared histogram plots of price change % (new vs. production model) after integrating updated elasticity values**

**Analysis performed at overall, meta, ****ship_class****, and ****cat_class**** levels**

**Key insights from plots:**

**Price changes in the new model cluster near zero with long tails**

**Indicates low-to-moderate adjustments for most products**

**Small ****subset**** of ****sailings**** shows extreme price adjustments**

**Analyzed % of price change records hitting caps (new vs. old model)**

**Differences in cap hit rates highlight product-level price sensitivity**

**Lower cap hit rates in the new model (for most meta products)**

**Suggests**** improved handling of high price sensitivity cases via elasticity, reducing reliance on caps**

**Participated in multiple discussions to refine and ****align on**** the presentation storyline**

**Potential future issue: None**

**Promo Action Recs Decision Layer 1 - Promo Action Recs based on Best SPI Benchmark Ranges**

**Status: This ticket is complete as of 6/08/2026**

**Deliverables:**

**Created a sample exciting deals promo recommendation file for last week promo recs and shared it with analysts through Monica received positive feedback.**

**Working on improving the recommendation file so it can be used in Power BI, based on analyst requirements.**

**Updated the SPI benchmarking approach by moving from broader WTS buckets to exact WTS-level grouping to make comparisons more precise.**

**Improved the accuracy of booked position benchmarks by tightening the ranges, making it easier to spot under- and over-performing sailings and ****recommend**** promos for those sailings**

**The final promo action recommendation file was prepared to share with analysts, providing promo recommendations based on booking position ranges compared ****against**** best-performing SPI booked position benchmarks**

**Based on feedback from Anastasia, there is a request to enhance the recommendations by including suggested price change magnitudes for sailings selected for promo actions**

**The enhancement aims to incorporate recent booking trends and determines pace to sell out the inventory to make price change recommendations for the sailings that are on promo in a data driven way**

**Potential future issue: None**

**Evan ****mcfall**

**Rev mgmt.**

**Demand Model**

**Finalized model and deployed to production with business approval**

**Value ****add****: Model is live and ready for PRE**

**Adjusted model to be capable for booked position perturbations (track)**

**Tested and confirmed all instances had no target leakage or bias**

**PRE ****is capable of pulling**** the new demand forecast**

**Business approved the deployment and agreed on the benefits seen**

**Adjusted pipeline and capabilities for the model**

**Value ****add****: Model is improving and aligns with best practices**

**Observed similar methods / behaviors used in other practices**

**Adjusted pipeline to be capable of adjusted parameters**

**Created historical elasticity assumptions for 3% price changes**

**DUAL | Model Improvement**

**Work Completed**

**Refactored production notebook into model.py, data_etl.py, and ****production_****notebook.ipynb**

**Externalized model parameters into ****params.yaml**** with ****load_****params****(****) loader**

**Added ****joblib****-based model persistence (****save_****trained****(****) / ****load_****trained****(****)) with _****EnsemblePredictor**** class replacing closure-based predict functions for pickling**

**Fixed log1p asymmetric error at high-demand sailings**

**Fixed ****ship_code**** target encoder systematic bias for atypical ships**

**Confirmed hit-rate improvement in middle WTS window versus Prior/CEL**

**Added per-occupancy UC output tables: ****pax_history****, ****booking_history****, ****pax_elasticity_backtest****, ****booking_elasticity_backtest**

**Built elasticity pipeline with perturbation levels ±3/5/****10/15****/20% plus -50% to +200%**

**DUAL | Demand Forecast - CI/CD**

**Configured ****Demand_Inference_Run.yml**** under resources/ in the DemandForecast ADO repo**

**Established branch-to-target mapping: dev → dev, ****qa**** → ****qa****, master → ****prd**

**Upgraded cluster from single-node Standard_D3_v2 (14GB) to Standard_E8_v3 workers + Standard_D12_v2 driver, 4 workers, DBR 17.3 LTS**

**Resolved deployment errors: ****autoscale**** policy validation, node type allowlist, ****notebook .****ipynb**** extensions, dependency graph issues**

**Defined full 5-task pipeline sequence: ****Pricing_History_Log**** → ****FSData**** → ETL → Model → Elasticity**

**DUAL | Demand Forecast – Complete PRE Demand Model**

**Pipeline**

**main.py orchestrator with workspace-path resolution that works in both ****spark_python_task**** and notebook execution contexts**

**data_****etl.DataETL****(spark, rebuild=True****).****build****_****all****(****) refreshes ****weekly_features_updated****_{****double, quad} from cco_level_fs_v5 with row-loss assertions at every merge**

**model.ipynb**** runs walk-forward ****backtest****, trains the final model, writes parquet handoff plus the four model output tables**

**elasticity.ipynb**** reads the parquet handoff, computes demand curves and per-sailing elasticities across the perturbation grid (±3% / 5% / ****10% / 15****% / 20% plus -50% to +200% at 10% intervals), writes the four elasticity output tables**

**Ben F**

**IBP**

**One thing I forgot to include in my status report is the meeting I had with Nicole Fernandez-Valle. Good discussion. One thing I had no idea is Laura gets literally like a ****20-50 page**** status report email of product dev status items. Some on product dev are convinced Laura wants this level of detail and reads it all but Nicole thinks perhaps we ****could help there. ****Also**** the product dev team uses ****Asana**** and she’s interested in help using Asana for reporting too. Not sure how Asana works and if this is a good use of our time but wanted to pass this on to you.**

**Mert:****
****MIAP****
Created a knowledge base repository compatible with Obsidian for MIAP and Newbuild to accelerate development and knowledge sharing.****
Standardized vibe-coded content in the MIAP app and added agent instructions to enable coding agents to follow defined rules.****
Released a custom AI agent for AMOS.****
Met with IT and Risk Management/IBP teams on Project TIDE; presented a demo of the TIDE claims workbench app and received positive stakeholder feedback.****
Sailed on Allure of the Seas with a 2nd Engineer who will support tag mapping for the next 4–5 months; provided training on the tag mapping process.****
Interviewed candidates for two contractor roles.****
Met with the deployment team to discuss standardization of deployment development practices.****
****
****
Reza:****
****MIAP****
Completed the capital savings project in the Digital Twin Fuel Forecast platform; updates have been applied to both the MIAP app and REST API.****
Updated query-based models for the incinerator, incinerator fallback, OFB fallback, and thruster within the Digital Twin model.****
Started the hybrid pipeline for per-class tuning of the fuel forecast project; documented and transferred the process to an analyst team member for continuation after delivery of the first ship in the class.****
Updated the common-****config.yml**** file for fuel forecast prediction/tuning to include the entire fleet.****
Added per fuel-type MGO-equivalent calculations to datetime-level Digital Twin outputs.****
Continued maintaining models and baselines for the service power area.****
Participated in a Senior Data Scientist contractor interview.****
Updating the fuel forecast workflow in the QA environment (in progress).****
****
****
Arya:****
****MIAP****
Worked on SORA Swagger documentation and collaborated with stakeholders to improve endpoint responses.****
Resolved pipeline issues.****
Collaborating with the safety team to rebuild workflows for automated KPI classification.****
Conducted working sessions with the safety team to understand KPIs and build a high-quality example dataset for classification; defined a two-layer architecture (classification + validation).****
Developing a pipeline to upload SQM policies and other safety data into Azure AI Search indexes (currently resolving permissions issues for dev-alpha-ai-search with the platforms team).****
Setting up workflows to migrate Confluence documents and metadata cleanly into Azure AI Search for use by an information agent in the MIAP app.****
Working on reverse osmosis model logic: defining features, performing EDA, and studying component mechanics; reviewing research papers for modeling approaches.****
Finalizing pixel agent animations and generative elements.****
Met with the security team to improve the fleet tracking app (weather data sources, port information, general features); working on service principal setup for email ingestion.****
Conducted data science analyst interview testing and prepared a solution notebook and interview questions.****
Collaborated with Reza on diagnosing Digital Twin modeling issues and understanding the codebase.****
Added capital fuel savings workflow integration into the Digital Twin for improved fuel prediction accuracy (implemented as a Delta table within a workflow).****
Co-designed logic with Reza to dynamically distribute capital fuel savings across Digital Twin predictions and reflect them in summary/results tables.****
****
****
Will:****
1. Fleet Expansion****
****MIAP****
Added nine new hulls into EDA (in addition to WN):****
AT (Celebrity Ascent), AX (Celebrity Apex), BY (Celebrity Beyond), EG (Celebrity Edge), FR (Freedom of the Seas), HM (Harmony of the Seas), SY (Symphony of the Seas), UT ****(Utopia of the Seas), XC (Celebrity Xcel), WN (Wonder of the Seas – carried over).****
Includes four years of 10-minute historian data per ship (June 2022 – June 2026), covering all DGs and LT/HT coolant loops, stored in parquet format.****
2. Multi-Ship Tag Extraction Tooling****
****
****ships_****config.json**** maintains per-ship metadata and engine-room mapping. Engine count and MCR are dynamically queried from the silver power plant table.****
query_cac_tags.py enables single or multi-ship extraction via CLI or Python, including coverage reporting and missing tag identification.****
New ship onboarding simplified to updating JSON and executing the extractor.****
3. Data Completeness Audit****
****data_completeness_****eda.ipynb**** evaluates tag coverage, engine status, monthly heatmaps, and gaps; produces PASS/REVIEW verdicts for data quality validation.****
4. v4 Detector Enhancements****
Automated baseline resets aligned with CL70055 cleaning events from AMOS.****
Fleet-relative residual comparisons to identify divergence across sister engines.****
Three detection channels: water-side delta-T (primary), air-side temperature (cross-check), thermostatic valve effort (early warning).****
Physical range gating to filter invalid sensor spikes.****
5. Reproducible Execution Framework****
run_v4_for_all_ships.py generates executed notebooks per ship.****
Reference outputs available for WN, including alarms, baselines, residuals, and v3 vs v4 comparisons.****
6. LT-WHR Valve Tag Rename****
Updated tag naming to ****ratio_open_lt_whr_regulation_vv_de_X**** to align with P&ID.****
Propagated changes through bronze/silver mappings and CAC extraction logic.****
Web App (Analytics Dashboards)****
Completed updates under branch feature/****upgrade_power_plant_figures****:****
Added date sub-range slider with in-memory caching for fast interaction.****
Migrated fleet configuration to YAML for easier onboarding.****
Fixed multiple plotting issues and improved visual styling.****
Resolved “No data available” bug for 10-min and weekly views by centralizing period-frequency mappings.****
Verified full end-to-end functionality across all periods.****
Next: Begin Power Plant performance figure upgrades using the same standards.****
****
****
Ram:**

**MIAP****
This Week:****
Generated MIAP REST API vendor usage reports by ship and shared with Jorge.****
Deployed streaming-related updates to the MIAP package, REST API, and MIAP application.****
Initial validation shows Postgres streaming to MIAP is over 45 seconds faster than Databricks for one ship (Star); further analysis required to confirm latency differences.****
Implemented file count tracking across sources and deployed to production; supports MIAP sample count dashboard for detecting Crosser/internet issues.****
Next Week:****
Integrate historical data retrieval via the stream endpoint and implement deduplication logic.****
Finalize design approach before development.**

**Ayon G.**

**Weekly Update Summary WOW 6/12**

**Completed specialty configuration onboarding for the following venues:**

**Samba Grill (93) – specialty only**

**PSBQQ (233) – modifier + bar**

**Pier 7 (304) – specialty**

**Empire Supper Club (316) – specialty only**

**Lincoln Park Supper Club (329) – specialty**

**Successfully finished the clone job for specialty setups, with standardized meal period configurations applied across all required locations.**

**Unit and integration testing completed and push to production**

**IBP – Ben:**

**1. Headlines — Decisions & Forward Momentum**

**Excellent Steerco meeting on 6/11 with Keith, Juan and team. The meeting with Laura to finalize and discuss rollout to rest of Celebrity and future rollout to Royal is on 6/15 at 4pm. Juan is concerned that we do not have the required staff for supporting the broader rollout to Royal given the volume of ships. Connor understands and agrees there may be need for another team added to support the change management work.**

**This week's ****net-new**** milestones:**

**Two systems crossed into production:**** ****Marine Consumables (unattended weekly job, Sat 01:00 ET) and the Finance Tracking Tool (Sunday-noon schedule, first automated run 2026-06-14).**

**HF&B next-gen demand work went from a design proposal to real, shipped models**** ****—**** error down 29% on the RCI/CCI book ****—**** plus a self-improving "HFB Lab" and a production serving-path corrector running safely in shadow**** *****(its promotion path was independently reviewed and hardened this week)*****; no published forecast touched, full cutover human-gated.**

**The Executive Overview dashboard is now live on real Unity Catalog data, and a material MOT/Savings reporting error (a bogus +$51.2M) was root-caused, corrected, and the live dashboard now shows accurate figures.**

**2. The Week ****at a Glance**

**37 pull requests merged since last week's report (#510–#567). *****(Three earlier CocoCay PRs — #505/#******507/#******508 — were covered in last week's report and are not repeated here.)***

**3. Flagship A — HF&B Next-Gen Demand Models + HFB Lab**

**Why: HF&B demand forecasting drives provisioning and supply decisions across the fleet. Cutting forecast ****error**** nearly a third on the RCI/CCI book (43 ships across Royal Caribbean and Celebrity) directly tightens inventory accuracy and reduces over-forecasting waste.**

**What shipped this week (last week this was only a design ****proposal, #****503):**

**More accurate models, evaluated under the exact official dashboard accuracy recipe.**** ****The RCI/CCI champion lowered error from**** ****14.92 ****→**** 10.57 (****−****29%, winning 10 of 11 months); SSC from**** ****33.87 ****→**** 25.04 (winning 11 of 11).**

**"HFB Lab,"**** ****a self-improving experimentation system that compounds learning from both wins and documented failures ****—**** plus a**** ****Loops Observatory UI**** ****giving leadership plain visibility into how the system works, why it works, how it compounds, and what it costs.**

**The corrector is wired into the production serving path but remains config-gated and defaults to shadow mode.**** ****It**** ****logs**** ****challenger metrics without touching any published forecast; a fail-open design means a production run can never be broken by it.**

**It was**** ****live-verified on production infrastructure**** ****(April-2026:**** ****9.36 vs 12.10, gate precision**** ****0.904), matching the**** ****backtest****.**

**Promotion path independently reviewed and ****hardened (#****565).**** ****A production review confirmed shadow mode was safe as**** ****merged**** ****but the path to flip the corrector to**** ****active**** ****was not. Every critical/high finding was remediated so the cutover is now**** ****safe and reversible: the win-gate now counts**** ****≥****3 distinct settled months**** ****(orchestrator-sourced, 10-day settlement maturity) instead of rows ****—**** closing a ~36-hour gaming hole; the post-activation baseline reads the**** ****pre-corrector**** ****value so the model can never train on its own output;**** ****auto-demote**** ****to shadow triggers after 2 distinct-month losses; and**** ****rollback restores the original forecasts, not just flips a flag. No behavior**** ****change**** ****while modes stay ****shadow****/off.**

**Observatory v2 (#566)**** ****—**** the telemetry view became an**** ****interactive operations console: clickable knowledge tiles (experiments, distilled lessons, open hypotheses), a**** ****live Databricks runs feed, a rate-limited**** ****"Run shadow evaluation now"**** ****trigger, verdict-aware styling that fixed a stakeholder-reported "green box on a losing result" bug, and a ledger-faithful mock with a generator so the demo view can't drift from reality. (#567 fixed a column-name bug that had hidden live challenger metrics behind an empty state.)**

**Concrete metrics:**

**RCI progression waterfall: 14.92 → 14.07 → 10.57; SSC 33.87 → 25.04.**

**Gate-precision floor 0.60 (corrector refuses to apply below it); factor clipped [0, 10].**

**Config seed:**** ****rci**** ****= shadow,**** ****ssc**** ****= off**** ****—**** the merged code changes nothing in production until a**** ****human flips**** ****a config row.**

**Shadow Databricks job scheduled Sat 15:07 ET; UNPAUSED in dev, PAUSED in ****qa****/****prd****.**

**HFB Lab cost telemetry: 1.57M tokens total, ~362K per RCI accuracy point removed.**

**STATUS****: ****🟡**** Shadow**** / monitoring — promotion path now hardened and safe to exercise. The corrector runs in shadow only; full production apply remains human-gated, now formalized as ≥3 distinct settled months of orchestrator-sourced challenger wins (10-day maturity) plus a confirmed config flip, with auto-demote and restore-capable rollback as guardrails. No full rollout has occurred. Governance follow-up: rotate the committed Databricks PAT flagged in the review and set the HFB_LAB_CONFIG table ACLs. (PRs #559, #****561, #563, #564, #565, #566, #****567)**

**4. Flagship B — Marine Consumables: Now Productionized**

**Why: Marine Consumables was validated last week but not yet self-running. Productionizing it turns a research pipeline into a hands-off weekly operational system that produces ship-by-product order recommendations stakeholders can ****actually use****.**

**What shipped this week (the status change from last week's "validated, not productionized"):**

**A scheduled weekly Databricks job on ephemeral job compute, running every**** ****Saturday 01:00 ET**** ****against fresh master-branch code (live job 789714502721179), training**** ****two dates each run**** ****—**** a prior-month**** ****backtest**** ****that reports real accuracy plus the live run-date forecast (auto-advances weekly).**

**The full documented ordering layer deployed into production NB17:**** ****the**** ****P4 activity gate**** ****(drops**** ****likely-inactive**** ****ship-product pairs) and a**** ****pooled q90 safety-stock tail, with final outputs deep-cloned into the access-granted**** ****ibp_sso**** ****stakeholder catalog (NB20).**

**Recovered through two real live-run failures:**** ****a cluster-permissions issue (fixed by attaching the Job Compute cluster policy) and a missing**** ****LightGBM**** ****library (fixed by pinning**** ****lightgbm****==4.5.0**** ****as a task library) ****—**** both diagnosed and confirmed recovered against the live job.**

**Closed real data gaps and realigned the supporting docs to the deployed code**** ****(incl. a catalogue-figure correction, 109,214 ****→**** 113,089), headlining the**** ****order decision metric.**

**Concrete metrics:**

**P4 gate threshold τ = 0.35; removes ~595K units on likely-inactive pairs (demand 4.29M → 3.69M, 0 integrity violations).**

**Out-of-sample robustness (new this ****week, #517/#****518): the**** ****P3 demand point**** ****holds**** ****WAPE 61.5 / bias 0.94**** ****across a**** ****24-month**** ****walk-forward panel (109,062 pair-months); the**** ****P4 gated order**** ****posts**** ****WAPE 59.5 / bias 0.93**** ****on a**** ****17-month**** ****leakage-free panel (78,505 pair-months), beating P3 in all 17 scored months.**

**Finance feed: FORECAST_VALUE now populates**** ****$597M**** ****(was 0), 99%**** ****costed****; 100% product-cost match (10,582/10,582).**

**Supply parity: 45–46 ships, 99.8% MLS-dated, 0 container-after-sailing rows, 0 carryover violations, order value ~$604.7M.**

**8 of 11 published stakeholder tables fully populate; the other 3 have honest caveats + a roadmap for pending data feeds.**

**STATUS: ****✅**** ****In production. Weekly job live on job ****compute****, ordering layer deployed, outputs cloned, docs aligned. (PRs #512****–****#519, #521, #523, #524, #525, #532)**

**5. Finance Tracking Tool — Live**

**Why: Replaces a brittle monolithic pipeline with a modular, automated, cheaper-to-run equivalent that is provably identical in output — removing manual operation and reducing ****compute**** cost while preserving exact financial accuracy.**

**What ****shipped**** this week: Flipped PAUSED → UNPAUSED after the first full ****unsuffixed**** production run succeeded end-to-end. The workstream is now complete and operational.**

**Concrete metrics:**

**June 2026, July 2026, and FY 2025 outputs**** ****bit-exact vs the legacy production pipeline; row-level check of**** ****808,789 keys with 0 mismatches.**

**ACTUALS recovery rows corrected from 259,875 → 0 (matches legacy).**

**3-task split-cluster job; the memory-heavy demand-proration step (NB09) isolated on its own larger cluster to eliminate prior OOM failures.**

**Schedule:**** ****12:00 PM ET every Sunday; first automated fire 2026-06-14.**

**STATUS: ****✅**** ****Live and self-scheduling. (PRs #522, #****539, #****543)**

**6. Executive Overview Dashboard — Live on Real Data**

**Why: Executives need to trust that the numbers are real, current, and honestly presented. Moving off mock data, documenting where it comes from (including known anomalies), and making negative results readable turns the dashboard into a decision tool rather than a demo.**

**What shipped this week (last week it was a mockup on a stable API ****contract, #****493):**

**Wired to live Unity Catalog data**** ****—**** every section now**** ****live**** ****except the Trending Override column, which has no operational feed.**

**Rev-5 stakeholder data-source documentation**** ****with explicit**** ****unusual-data**** ****callouts; the header chips now compute live-vs-mock status**** ****per section**** ****instead of a stale hardcoded label.**

**Eight UX refinements:**** ****accounting-style red negatives, sign-colored bars, per-section PNG (3****×****) + RFC-4180 CSV self-serve exports, per-section data-freshness stamps, color-blind-safe traffic lights, accessible tooltips, skeleton loading.**

**Concrete metrics:**

**5 of 6 sections on live Unity Catalog data; all 6 data sources verified end-to-end in Databricks; MOT data current through 2026-06-08 at cutover.**

**Tests: backend ****pytest**** 13/13, dashboard ****vitest**** 33/33, ****tsc**** + next build clean.**

**STATUS: ****✅**** ****Live on Unity Catalog data (one column intentionally mock). (PRs #542, #****557, #****558)**

**7. CocoCay (PCC) Demand Guardrail — Live in Production**

**Last week's report covered the guardrail in monitoring mode. It is now live.**

**The apply step (****apply_pcc_scaling****) runs as an**** ****active call in the production future-spend guardrails notebook**** ****(****guardrails_daily_breakdown_future_spend****, after seasonality / before the freeze).**

**The go-live cutoff (#510/#511) is set to**** ****2026-06-07**** ****(now passed): every BEYOND sailing calling Perfect Day at CocoCay from go-live forward receives the uplift (capped at +40%) and keeps it even mid-cruise; the single in-process pre-go-live ****sailing (2026-05-31, already delivered to the ship) was deliberately spared (factor 1.00).**

**Verified on dev P8:**** ****PCC sailings from 2026-06-07 scaled at factor 1.40; the 2026-05-31 in-process sailing held at 1.00; recorded actuals and non-food items untouched.**

**Self-decaying by design:**** ****as the weekly-retrained model learns the CocoCay premium, the correction fades toward 1.0 with no manual intervention.**

**STATUS: ****✅**** ****Live in production (go-live 2026-06-07). The deployed default basket is live now; lowering the threshold to widen the eligible set (e.g., pull in Leg Quarter / Drumstick) is left as a ****commented****, optional future enhancement for culinary input**** — ****it does not gate the current deployment. (PRs #505, #****507, #508, #510, #****511)**

**8. MOT Cost-Avoidance — FX Correctness Fix**

**Why: A financial metric shown to executives was overstated by tens of millions of dollars. Correcting it protects the credibility of cost-avoidance reporting and ensures leadership decisions are based on accurate numbers.**

**What was wrong and the fix (full arc this week — discovery to fixed):**

**The Executive ****Overview was reporting**** an impossible fleet 2026 YTD "savings" of**** ****+$51.2M.**

**Root cause: a**** ****currency bug**** ****—**** non-USD purchase lines were never converted to dollars, inflating Asia/Pacific-deployed ships by as much as**** ****~150****×**** (JPY), ~7.8****×**** (HKD), ~1.3****–****1.5****×**** (SGD/AUD), and 10****–****25% the other way (EUR/GBP). (Example: a 2,600-yen case**** ****showed as**** ****~$2,600 instead of the correct ~$17.05.)**

**Fix applied to the source pipeline notebook, re-run across**** ****all 47 ships (1,405 cruises); the live dashboard now reads the corrected data showing a realistic**** ****fleet**** ****2026 YTD of**** ****~****−****$9.5M**** ****(spend modestly over baseline, consistent with inflation).**

**Millennium PRODUCE/DAIRY baseline corrected from ~$21.6M per sailing to $72k–222k; the ****cruise_mot**** table had been ****stale**** since 2026-04-05 and was rebuilt 2026-06-11 (now extending through 2026-10-19); Xcel new-build now covered (−$6.0M).**

**STATUS: ****✅**** ****Live in production (dashboard reads FX-corrected rebuilt tables). Two**** ****people-tasks**** ****outstanding: schedule the rebuild notebook and retire the old artifact. (PRs #552, #****553, #****555)**

**9. Pipeline / ETL Hardening**

**#549 — Forecast-accuracy correctness fix:**** ****date weekly consumption by when product was ****actually consumed**** (reconcile/movement date) rather than voyage-close posting date, removing phantom empty/spiked weeks that inflated May 2026 dashboard error (phantom all-zero weeks cut RCI 59****→****6, SSC 50****→****12). Finance and**** ****voyage-key**** ****joins deliberately keep the posting date.**

**#545 — DPM extracts:**** ****split a 4,420-line monolith into an orchestrator + 10 step notebooks that auto-resume from a failed step; identical outputs,**** ****134 vs 233 min (****−****43%).**

**#550 — Supply Step 2:**** ****cut expected weekly runtime from ~11.4h to ~4h by switching append tables to incremental OPTIMIZE (removing ~7h of full Z-ORDER rewrites); byte-identical across all 9 tables.**

**#544 — Demand-volatility job:**** ****collect Delta stats on the Z-ORDER key columns before**** ****optimizing**** ****(the key sat beyond Delta's default 32-column stats window); row-count parity 169,420 = 169,420.**

**#526 — Deployment-schedule table:**** ****cast the empty SHIP_LENGTH column to numeric before**** ****write****, stopping recurring read failures (no data change).**

**#527 — Inventory dashboard:**** ****dropped junk empty/duplicate CSV header columns before the spend-report write, with a pattern-based guard against future re-exports.**

***The two largest (consumption dating #549 and Supply Step 2 #550) validate fully on their next scheduled weekly production run.***

**10. Next Steps & Asks**

**Laura's fleetwide rollout-planning meeting**** ****(Celebrity + ****Royal) ****—**** within the two-week window from June 3. Meeting on 6/15.**

**Summit rollout**** ****— ****SteerCo****-approved June 3;**** ****Future plans**** ****to be**** ****finalized**** ****in Laura's meeting.**

**Royal-scale staffing**** ****—**** Juan flagged that current staff cannot support the broader Royal rollout given the ship count; Connor agrees an**** ****additional**** ****team may be needed for change-management.**** ****[Ben: carry into the 6/15 meeting.]**

**HF&B shadow → full cutover:**** ****the promotion path is now hardened and ****reversible (#****565). Promotion requires**** ****≥****3 distinct settled-month challenger wins**** ****(orchestrator-sourced, 10-day maturity) plus a human-confirmed config flip; auto-demote and restore-capable rollback are in place. Decision point ****—**** who confirms promotion.**

**Security / governance (HF&B):**** ****rotate the committed Databricks PAT flagged in the serving-path review (****rapid_test****/_v9_oos_headline_rest.py) and set the**** ****HFB_LAB_CONFIG**** ****table ACLs.**

**CocoCay guardrail: live in production since ****the 2026****-06-07 ****go-live****. Optional, non-blocking future enhancement — widen the eligible basket (lower ****min_uplift****) pending culinary input.**

**Monitor the two ****newly-armed**** production jobs**** ****through their first unattended fires: Marine Consumables (Sat 01:00 ET) and Finance Tracking Tool (Sun 2026-06-14, 12:00 PM ET).**

**MOT FX fix follow-ups:**** ****schedule the rebuild notebook and retire the superseded artifact.**

**Camila: IBP:**

**RBC testing enhancements to improve limited history products**

**RCI/CCI Uniform cost center mapping testing to reduce amount of rows and focus on the cost centers that ****actually consumed**** to allocate the prediction for**

**Reduced test pipeline for pilot from 4+ hours to about an hour runtime for all of celebrity fleet for finance tool records**

**Testing shipboard consumption table but found inconsistencies where it can include unapproved orders, making values look inflated per reconcile date**

**Pending: change post inv scheduled date -> reconcile date for weekly consumption reference**

**Began developing uniform finance tool**

**Pending: ****cococay**** enhancement **

**Acquire access to gangway data for a more accurate PAX count**

**Pending: Royal ships testing for pilot**

**Nico: IBP:**

**Fix WRITE_DATE Column Corruption in Product Grouping Aggregation Notebooks**

· Done ✅ · High

**Completed:**

**Root-caused the **WRITE_DATE corruption (Tue 6/9): Traced the issue to prds_modified_unpivoted_table_similar, where WRITE_DATE had been moved from first_cols (taking the first value from a distinct grouping) to group_by_cols (part of the grain that creates the distinct grouping), corrupting its datatype. Created the DOE-2252-Fix-Write-Date branch.

**Propagated fix through the pipeline (Wed 6/10)**: Re-ran the full "Steps to Propagate Fix" (Steps 1–4), refreshing all downstream tables that consumed the corrupted WRITE_DATE. After Step 4, the Move_Current_Month_Demand_To_Archive_Delta_Table notebook ran successfully — unblocking future model development.

**Merged PR into long-running ETL branch (Wed 6/10)**: Merged the fix into the DOE-1846-Silversea-Uniforms-ETL-Demand-Forecast branch. **Story moved to Done.**

**Fix Relative Month Column Calculation to Use MODEL_TRAINING_DATE Instead of Current Date**

· In Progress · New this week

**Completed:**

**Created story and documented the problem (Wed 6/10)**: Identified that PREVIOUS_*_MO and FUTURE_*_MO column naming logic in both SSC_Demand_Model_Adjustments_and_Guardrails and pivoted_table_adjusted uses datetime.now() / current_month as the reference point instead of MODEL_TRAINING_DATE. This causes two issues:

**Temporal misalignment** — if the Guardrails notebook and pivoted_table_adjusted run in different calendar months, the PREVIOUS/FUTURE columns refer to different calendar periods despite having the same column names

**Missing column errors** — consumption data for the current month minus 1 may not yet be available, causing PREVIOUS_1_MO to never be created, breaking downstream .select() calls 
DOE-2312: IBP | Fix relative month column calculation to use MODEL_TRAINING_DATE instead of current…

**Ongoing:**

**Implementing the fix**: Replacing datetime.now() with max(MODEL_TRAINING_DATE) in both affected notebooks, then re-running the full pipeline from Guardrails onwards.

**SSC Consumption and Prediction Ratio Adjustments**

· In Progress

**Completed:**

**Identified missing **MODEL_TRAINING_DATES gap (Sun 6/8): Documented that the pipeline had not run from 2025-10 to 2026-04, meaning the archival tables are missing MODEL_TRAINING_DATES for that entire period — effectively no training runs exist for those months.

**Found **WRITE_DATE type mismatch in archival notebook (Sun 6/8): Uncommenting the final checkpoint_dataframe in Move_Current_Month_Demand_To_Archive_Delta_Table caused a WRITE_DATE datatype merge error. Traced the root cause to prds_modified_unpivoted_table_similar and planned the fix (which became DOE-2252, now Done).

**Confirmed no historical reason for the issue; planned fix (Sun 6/8)**: Found no Git commit history explaining the WRITE_DATE change. Determined the fix requires modifying notebooks in run_adjusted_tables_2.py and ensuring all downstream table writes use overwrite mode.

**Ongoing:**

**Proceeding with **run_adjusted_pivoted_tables: Now that DOE-2252 is resolved and the WRITE_DATE corruption is fixed, continuing through the remaining pipeline steps. The newly created DOE-2312 (relative month fix) was discovered during this work and will be addressed in parallel.

**Investigate Consumables Consumption across SSC at Cost Center Level**

· In Progress · Medium

**Completed:**

**Reviewed Camila's proposed **dept_segment → dept_key mapping solution (Tue 6/9): Camila shared an investigation report proposing a mapping derivation approach and asked for review once the backtested dates work is completed.

**Raised concerns with the proposed mapping (Wed 6/10)**: After reviewing the report, flagged two key concerns:

**Mapping derivation is arbitrary**: The proposed table groups job descriptions for a given dept_segment (derived from COST_CENTER) and associates them with available dept_key values based on similarity. These associations are imprecise — a dept_segment can be applicable to multiple dept_key values, leading to ambiguous or incorrect allocations.

**No data drift analysis**: There was no investigation into whether the dept_segment ↔ job_description relationships change over time, which could cause the mapping to degrade.

**Ongoing:**

**Awaiting alignment on alternative approach**: Need to determine whether the mapping derivation concerns can be addressed or if a different methodology is needed for cost-center allocation.

**RCI/CCI HF&B Order Creation Dashboard MLS Discrepancies**

· Done ✅ · Highest

**Completed:**

**Met with Naren Bandaru and Joao Adami — confirmed MLS ingestion process (Sun 6/8)**: They confirmed the MLS table is populated by: (1) the MLS team uploads the file from the SFTP folder, and (2) Joao takes the MAX(batch_id) from the file and uploads that batch to the table. Each new file upload represents the **current state** of any current or future scheduled deliveries — there is no inherent need to retain historical records.

**Closed out the story (Sun 6/8)**: Verified there are no historical uses of the MLS table that would require retaining prior batches. Concluded there is **no need to consider the MLS from a historical standpoint**. Notified Paolo that the proposed table changes are no longer needed. **Story moved to Done.**

**Silversea Uniforms Crew & Demand Forecast (Cont.)**

· To Do

**Completed:**

**Created feature branch (Tue 6/9)**: Created the DOE-1846-Silversea-Uniforms-ETL-Demand-Forecast branch. The DOE-2252 WRITE_DATE fix PR was merged into this branch, establishing it as the long-running ETL branch for on-the-fly changes.

Ale: IBP: 
**Ale’s Weekly Update**

**GMO Unhealthy Inventory Dashboard — Table Creation** 
Built and delivered the GMO Unhealthy Inventory classification pipeline, adapting the existing SSC (Silversea) workflow to Royal Caribbean Group’s marine MRO parts data. The pipeline integrates three gold-layer sources—shipboard inventory, stock transactions, and completed purchase orders—to classify ~1.1M inventory line items as **HEALTHY, OBSOLETE, or EXCESS**. The final output table has been delivered to dev_datascience.ibp_sso.GMO_UNHEALTHY_DASHBOARD_FINAL, with full technical documentation provided in a Word document.

**Summer Scope Overview** 
Met daily with Camila and Ryan to align on summer priorities. Key workstreams include enhancing the Coco Cay demand forecasting model and developing a new ship forecasting pipeline. Excited to take on larger, high-impact projects in this space this summer!

**Next Steps** 
Awaiting stakeholder (Yan) feedback on the GMO Unhealthy Inventory table, particularly regarding identified limitations. Primary focus for the coming week is onboarding onto the Coco Cay model—understanding its current framework, feature set, and identifying opportunities for improvement through CocoCay shore excursions.

Ryan: IBP: 
RM **Weekly Summary**

Built the GMO Inventory Depletion Dashboard, adapting the existing SSC Inventory Depletion pipeline to serve the Global Marine Operations fleet. The pipeline forecasts when each part on each vessel will run out of stock based on trailing 12-month consumption.

**Key differences from SSC that required new engineering:**

**Ship mapping** — GMO inventory only has numeric DEPTIDs, so I built a lookup layer resolving DEPTID → ship code from transaction history (60 ships mapped cleanly)

**No in-transit signal** — SSC has live PO statuses for pending supply; GMO's completed_po table only shows delivered orders, so the pipeline correctly limits to on-hand inventory

**UOM + category gaps** — GMO lacks unit of measure on inventory (enriched from transactions) and has no category hierarchy, reducing the grouping grain from 7 columns to 4

Output: GMO_INVENTORY_DEPLETION_FINAL_OUTPUT — one row per ship + part with stock position, burn rate, price exposure, and projected out-of-stock date.

**Next week:** Gather feedback from team on final table output. Start to dive into guardrail optimization and enhancements for CocoCay.

Caleb:  
**Consumer Lifetime Value (CLV)**

Completed

Revised goals of final POC versioning before final productionization: refactored entire CLV pipeline into a segmented 4 notebook job, enabling modern feature usage and consistent validations

Created E2E testing for pax count, dupes, and column validity, then profiles the output table, instantly creating metadata for proper usage

Resolved merge conflicts between 2 previous branches, all pushed to dev_caleb

Validated Revenue Planning's vcap stage table, showing a discrepancy of channel props for 2017-2018. We regrouped with them and they are applying the same VCAP MICE channel creation logic for all years, not just 2019 on.

In Progress

Preparing a final test run of our ETL, just awaiting the proper stage table updates.

**Sailing Environment**

Completed

Reported to Joey and Cory a status update

Created an automated script which pulls the quarterly and annual SEC filings for competitor's earnings reports

Standardizes reporting formats and terminology to a succinct table, detailing financial and capacity figures from 2019 - present for RCL, CCL, NCLH, VIK

In Progress

Update additional sources such as CS's cruise industry fleet model, google trends data, blocking file projections, etc.

Triangulating rolled up industry capacity APCDs and PAX to CLIA reports, deployment tables, fleet model and our previous Strat Plan figures

This will then provide an adjustment factor which we can utilize to provide a good estimate on cuts like meta product, brand, corp

Carlos: E-Commerce: 
Ecommerce:

- Moved journey score model to production after code cleaning and testing.

Silversea (Jakala transicion and new models) :

- generated and shared new report of data availability and freshness.

Mireille: Contact Center: 
**Weekly Report — June 11, 2026**

**LP Prioritization**

**Issue****: **** **Files are failing to land at the SFTP destination. The symptom points to a firewall or security-group rule that allows the initial TCP handshake but silently drops the SSH data that follows — so the connection looks like it opens, then never delivers.

**Status:**** **Still actively working this with the  teams to solve.

**WFP Simulator**

**Preparation of the Demo & Feedback Meeting**

Prepared the demo script for the upcoming feedback session. The goal of the session is to validate that the workflow matches how planners actually think about FTE — and to capture early feedback before broader rollout.

**End-to-End Testing — 30-Minute Model**

This week focused on **end-to-end testing and stabilization of the 30-minute version** of the "Run Your Own FTE" simulator. The objective was to make sure the 30-minute mode runs consistently across every step — from inputs (office hours, assumptions, hourly forecast), through the joined view, all the way to the Erlang A engine results and the Compare tab.

The 1-hour version is stable. The 30-minute version is **pending final validation** because of unreliable / inconsistent data flowing through the 30-minute interval preprocessing layer. The root cause traces back to the **migration to Genesys**, which introduced inconsistencies in the source tables (gaps, duplicated slots, and occasional misaligned day boundaries). the upstream data needs to settle before the 30-minute results can be trusted for planning.

**In Progress — Multi-Scenario Comparison (≈70% complete)**

We are expanding the app so planners can explore several "what-if" futures for the same line of business at the same time, instead of running them one by one.

****What ****it will**** unlock****

- Try **different assumptions** (e.g. handle time, shrinkage, service-level targets) and see the FTE impact instantly.

- Plug in **different call-volume forecasts** (baseline vs. adjusted vs. stretch) without overwriting prior runs.

- Test **different office-hours schedules** (current vs. extended hours, weekday vs. weekend tweaks).

****End goal****

- A side-by-side view inside the app where planners can line up several scenarios for the same LOB and immediately see how staffing, cost, and service levels move.

- Faster, more confident decisions — no more juggling spreadsheets or re-running the model from scratch each time**.**

**Why it ****matter**

**-**** **Cuts scenario-planning time from hours to minutes.

- Makes the trade-offs visible: *"if we shorten patience by 10 seconds, how many more FTE do we need?"* — answered at a glance.

- Supports stronger conversations with operations and finance partners by showing options, not just one answer.

**In Progress — Combined LOB Scenarios (≈20% complete)**

Some lines of business are naturally planned **together**, not separately. The clearest example is Casino: in North America, planners think of "Casino" as one team that handles both **Casino Sales** and **Casino Services**. Today the app treats them as two separate LOBs — which forces the planner to run the model twice and add the numbers up by hand. We are fixing that.

****What ****it will**** unlock****

- Pick **"Casino"** in the LOB dropdown and have the app automatically pull together the sales and services pieces — one forecast, one schedule, one staffing answer.

- Plan the way the **North America team actually operates**, not the way the data happens to be split in the source tables.

- Get a single, defensible FTE number for the combined team — no manual addition, no spreadsheet glue.

**Where we are**

- The combined LOB option is already visible in the picker, and the app routes the request through the engine.

- We are now making sure every supporting piece — the call volume, the intraday shape, the handle time, the staffing ceiling — reflects the **combined** team, not just one half of it. This is the part still in flight**.**

****What comes next****

- Once Casino is fully validated end-to-end, the same approach extends naturally to similar pairs like **RES Sales + RES Services**, **Groups Sales + Groups Services**, and any future LOB the business chooses to plan as one team.

- The planner workflow stays identical — pick the combined name, run the model, get one answer.

****Why it matters****

- Plans match how the business is actually run, not how the data is stored.

- Removes a manual step that today is easy to get wrong (and hard to audit later).

- Sets a pattern we can reuse every time operations decides to merge or split a team**.**

**## Next Steps**

1. **Unblock SFTP delivery

2. **30-minute model validation, then re-run the full end-to-end test suite at 30-minute grain.

3. **Run the demo & feedback session

4. **Finish Combined LOB rollout, then extend the pattern to RES and Groups.

5. **Multi-Scenario Comparison, finalize the side-by-side compare view and persist scenario combinations so planners can re-open them later.

**## Executive Summary — June 11, 2026**

- **WFP Simulator — 1h model:** stable, ready for demo and planner feedback this week.

- **WFP Simulator — 30mn model:** end-to-end tested; final validation pending on upstream 30-minute data quality (Genesys migration cleanup).

- **Multi-Scenario Comparison:** ≈70% complete — planners will soon be able to compare assumption sets, forecasts, and schedules side by side, without manual spreadsheet work.

- **Combined LOB Scenarios:** ≈20% complete — Casino is the first case; the same pattern will extend to RES and Groups, matching how the North America team already plans**.**

## MyCruise Recommender
*Personalized post-booking recommendations (excursions, dining, spa) powering the ForYou surface in the app.*

### Recommender Engine

- **Recommendation Engine Build-Out** _(Rodrigo B.)_: The recommender combines two model families — collaborative filtering (CF — "guests like you also booked…") and Apriori market-basket rules ("people who bought X also bought Y"). Rodrigo extended Apriori beyond shore excursions to Dining, Beverage, and Spa and built pipelines to refresh the rules and recompute recommendations across all categories. He also hardened CF with two fallbacks for thin carts (split multi-item carts into single items, and Apriori-based recs off the current cart), capped output at 100 items per booking, and defined a clear stacking order — CF first, then sub-cart CF, then Apriori rules ranked by confidence/lift/support. This is the single biggest jump in recommendation coverage and quality since the ALS work.
- **Coverage Analysis — Royal Beach Club Case Study** _(Rodrigo B.)_: Rodrigo is running coverage checks across both Apriori and CF models — by product and by customer segment — to confirm key products actually surface in recommendations, using Royal Beach Club products as the case study.

### A/B Testing

- **A/B Splitter** _(Cristian V.)_: The recommender is gaining the ability to run its own A/B tests — a splitter that assigns each booking to a stable test group so different recommendation configurations can be compared head-to-head. In progress this week.

### Segmentation & ALS Tuning

- **New Segmentation Models Live in the ForYou Pipeline** _(Cristian V.)_: Bridging the last two weeks' integration push (David's model upgrades and Danusio's guest segmentation), Cristian wired the new client clustering model (`booking_clusters_inference`) and product clustering into the ForYou ALS pipeline — ALS being the collaborative-filtering model behind personalized recommendations. He built a segmentation grid-search framework that benchmarks the new clusterings against the baseline, so we can quantify lift and iterate on segmentation strategies rapidly.
- **One Score to Compare Models End-to-End** _(Cristian V.)_: Cristian introduced a unified pipeline-level metric that evaluates ALS all the way through to the actual product-level recommendations guests see — a single composite score for objectively comparing segmentation strategies. He pointed hyperparameter tuning (hyperopt) at this metric directly, so model tuning now optimizes the real recommendations rather than an intermediate category-level proxy.

### Tooling / Documentation

- **Confluence Docs Now Auto-Synced by AI Agents** _(Cristian V.)_: Cristian built a `sync_to_confluence.py` utility that pushes local documentation to Confluence (Data Center) via the REST API, converting headers, tables, and code blocks into Confluence's storage format. This lets AI agents in our CI pipeline keep Confluence documentation in lockstep with the codebase automatically — replacing manual doc updates.

---

## Project Axiom — Voice 360
*Insight extraction from unstructured customer feedback (Medallia, Guest Logs, Qualtrics) via LLM pipelines — feeds emails, dashboards, drivers analysis, and chat.*

### Guest Logs

- **Realtime Guest Log Classification for SmartService** _(David M. & Erick A., new)_: Today, guest-services agents categorize each guest issue by hand, on the spot, while interacting with the guest — slow and error-prone, especially when there's a line at the desk. Erick scoped a new initiative with Guest Services / Operations to AI-assist that decision inside SmartService (the agent-facing app), and David started building the realtime service behind it — a cosine-similarity lookup that suggests the right category the moment a log is written, reusing the existing reassigned-category logic as its baseline. The result: cleaner guest-log data and faster, better agent-to-guest interactions.
- **Guest Logs Email — First Version Complete** _(David M.)_: Bridging last week's Freedom-of-the-Seas proof-of-concept, the guest-logs report (now branded "Voice of the Guest") is done in its first full version — same structure as the Medallia reports, with topic trends based on mention counts. The generation pipeline is ready, so we can now produce a report per ship and send it to stakeholders rather than hand-building one-offs.

### Meta Data Framework

- **Daily Pipeline Made Crash-Resilient** _(David M., Completed)_: Following last week's milestone of all three extraction pipelines running daily in production, David fixed a reliability gap — the daily job's checkpoint now writes to DBFS, so a lost executor mid-run can recover instead of restarting from scratch. Closes a known fragility in the newly automated pipeline.

### Fleet Reporting

- **Fleet Ship Reports Scaled to 7 Ships** _(Osvaldo V.)_: The dry-dock-style ship report (first proven on Symphony/Icon) now covers seven more ships — six Royal Caribbean (Wonder, Rhapsody, Navigator, Vision, Enchantment, Ovation). Osvaldo reorganized everything into a self-contained per-ship layout and produces two report types per ship: a Medallia shipboard-operations report and a public-sources report. Crucially, the pipeline now **consumes Danusio's scraped data directly** (see Scraping), with the data contract aligned between them. Celebrity ships are Medallia-only for now. **Pending review with stakeholders.**

### Webapp

- **3D Port Map Shipped** _(Osvaldo V.)_: Building on last week's D3.js pivot that fixed the pie-chart zoom problem, Osvaldo pushed a geographic port map that shows excursion-category distribution across all ports at a glance — surfacing category coverage gaps port by port.

### Cost Monitoring

- **LLM Token Logging Added** _(Danusio G.)_: The GPT-5 Mini "Safety" deployment — which powers the Shorex GSO Safety email reports — showed an unexplained token spike (~30M tokens / ~300K requests in a week) flagged in prior weeks. To run that down, Danusio added comprehensive logging to the LLM calls in his own pipeline to track cost and request volume. This turns the one-off GSO Safety investigation into ongoing visibility into his pipeline's caching behavior and anomalous usage.

---

## Project Scraping
*Cross-brand initiative to build a unified scraping platform serving Consumer Insights, Hotel Operations, Product, and Social Media. Phase 1 targets review/forum sources; Phase 2 social platforms.*

- **Reddit Workaround Found; Multi-Source Pulls Resumed** _(Danusio G.)_: The Reddit scraping block from the past two weeks has a path through — the Selenium approach still gets the account banned, but scraping via the TamperMonkey browser script works. With that unblocked, Danusio pulled Cruise Critic, Reddit, and TripAdvisor data for five ships (Wonder, Rhapsody, Navigator, Vision, Enchantment). This output now feeds Osvaldo's fleet ship reports directly.
- **TikTok Harness Functional** _(Danusio G.)_: Bridging the prior TikTok scripting work, Danusio has a working end-to-end harness — find relevant videos from a search query, pull metadata, download the video, and transcribe it. This opens up analyzing what influencers and commenters actually say about our ships.

---

## Project Concept Testing Lab
*Agent-persona framework using LLM-driven synthetic respondents to A/B test ideas and concepts before committing to live tests. Built on TinyTroupe (Microsoft OSS).*

- **TinyTroupe Comparison Delivered** _(Osvaldo V., Milestone)_: Closing last week's in-build comparison, Osvaldo delivered a report weighing TinyTroupe against the team's current concept-testing implementation, documenting TinyTroupe's technical advantages — ready to share with Hannah and the broader group to set direction.
