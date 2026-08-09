**Mert:**

**MIAP**

**Attended SeaTrade and met with the Valmet team to review their existing support for OPC UA servers for MIAP and discuss resolutions for ongoing issues.**

**Met with Lufthansa and reviewed their Digital Twin solution for the cruise industry, which showed promising results. Agreed to schedule a detailed follow****-up meeting with RCG Data Science teams.**

**Met with IT and reviewed the ****BlueApp**** shared drive and its migration to the cloud, which hosts ship delivery documents. Roadmap from IT is pending.**

**Initiated**** ****MIAP**** GitHub setup.**

**Met with the Decarb team and reviewed progress on digital twin models. ****Agreed**** to prepare a presentation for the Fuel Finance team and review final model results.**

**Nearly completed a full refactoring of the MIAP app using Next.js and ****FastAPI**** instead of the former Flask app. This refactoring improves performance, provides ****a better**** user experience, and enables more seamless agent integration.**

**Mahshad:**

**MIAP**

**Investigated and resolved failures in HVAC, Machinery, and MIAP analytics pipelines.**

**Developed individual chiller models and added new features to improve model performance.**

**Added visualization plots for the overall chiller COP model to the MIAP web application.**

**Identified**** a deviation in SM AHUs of approximately 200 kW; contacted the Marine Engineering team and am awaiting their response.**

**Observed a drop in ERW usage that may impact efficiency; scheduled a meeting with the Marine Engineering team for further investigation.**

**Arya:**

**MIAP**

**Fixed runtime errors for ships AL, RD, NV, ST, NO, XC, and UT.**

**Worked on improving SFOC curves.**

**Identified a tag issue with RD in the power plant where a required tag is not available.**

**Added STG logic to the digital twin.**

**Attended SeaTrade.**

**Ram:**

**MIAP**

**This week:**

**Used Databricks Federation to create a foreign catalog in Databricks pointing to Postgres tables, with support from the platform team.**

**Created a Databricks workflow using the psycopg2 library to perform deletes and updates in Postgres directly from Databricks.**

**While streaming data into Postgres, ****identified**** long read times when ingesting into regular tables and implemented a new partitioning approach to improve read performance. Updated the table name in Crosser and will monitor data comparison and performance for at least 36 hours.**

**Created alerts for the MIAP REST API, dashboards, and queries, and shared them with Mert. Received a new request to provide ship****-wise cost breakdowns for each vendor.**

**Next week:**

**Complete the PEPLINK deployment after Wesley adds the new datatype to the MIAP metadata table.**

**Analyze the streaming process with the new updates and work on further optimizations.**

**Will:**

**MIAP**

**Created new Open****-****Meteo**** weather tables for all ports and legs, enabling digital twin predictions for ships without onboard weather data across the fleet.**

**Integrated new weather data into SSC ship models, significantly increasing the amount of viable training data.**

**Fixed FACTS model issues for Nova and Utopia.**

**Created SSC itinerary tables to enable digital twin model validation for those ships.**

**Reza:**

**MIAP**

**Productionized the Residual Boosting class into the digital twin package. Results were tested and verified after package integration.**

**Performed R&D on potential improvements to residual boosting and added new variable options for residual boosting granularity to the digital twin fuel forecast package.**

**Met with the team to address the Silver Seas ship itinerary issue; gathered required information and tables from the Deployment Systems team and discussed findings with a data scientist to update the internal MIAP table.**

**Discussed fuel forecast accuracy issues on certain ships with a data analyst; provided required information and files to support tuning and accuracy improvements.**

**Presented 2025 digital twin fuel forecast results versus actuals and finance predictions to stakeholders at Decarb Digital ****Solutions, and**** implemented the requested new comparison approach for the final finance presentation.**

**Updated models and baselines for ships NV and RH in the service power area.**

**Mirielle T.**

**Contact Center: ****Call Volume Forecasting Strategies **

**Date:** April 16, 2026
**Project:** International & Casino Call Volume Forecasting

**Markets Covered:**
Singapore, Germany, Ireland, France, Nordics (Sweden, Norway, Denmark, Finland), Italy, Spain, UK, Mexico, Brazil, Australia, APAC, Other EMEA

**Overview**

This work focuses on building a **scalable and reliable call****-volume forecasting pipeline** for International and Casino markets.
The solution is designed to support workforce-planning decisions across markets with very different demand patterns, holiday calendars, and levels of stability.

The approach combines:

Proven forecasting concepts adapted from other domains

Robust feature engineering

Market-specific configuration

Automated model validation and selection

**1. Feature Engineering — Foundation of the Forecast**

**Where the Ideas Come From**

The call-volume forecasting pipeline did not start from scratch. We adapted ideas from a **validated supply****-chain forecasting project** that tested a large pool of candidate features and retained only those that consistently improved accuracy.

The reasoning is straightforward: demand forecasting problems share the same core structure — trends, seasonality, volatility, and anomalies — whether the demand is product consumption or customer calls.

**What Was Implemented**

Adapted and expanded the feature framework to capture:

Trends and momentum

Seasonality and calendar effects

Volatility, spikes, and sustained patterns

Market-specific holiday behavior

Built a broad candidate feature pool of **~130 features**, with automated feature selection applied later to retain only accuracy-driving signals.

**Why It Matters**

This approach improves the model’s ability to:

Detect demand changes earlier

Perform consistently across both stable and volatile markets

Avoid over-reacting to one-off anomalies

**2. Synthetic Forecast Data — Enabling Future Features**

**Purpose**

Machine-learning models require features for future dates, but future call volumes are unknown.
To address this, we built a **synthetic forecast baseline** that provides realistic placeholder values for future periods.

**How It Works**

Uses historical alignment (same day of week, same season)

Applies year-over-year growth assumptions

Generates a continuous daily time series for the full forecast horizon

**Key Improvements**

Preserves weekday vs. weekend patterns

Respects seasonal context when historical data is missing

Applies smooth, compounding growth beyond the first 12 months

Avoids zero-driven bias and unrealistic clipping in growing markets

**Why It Matters**

The synthetic baseline ensures future-period features are valid and prevents distorted inputs from propagating through the model.

**3. Adaptive Configuration by Market Stability**

**Why One Size Does Not Fit All**

Markets behave very differently. Some show stable weekly patterns, while others experience high volatility, short history, or structural changes.

**What Was Implemented**

Automatically classified markets into **Stable, Moderate, and Unstable** tiers based on historical variability.

Each tier controls:

Growth assumptions

Smoothing strength

Outlier handling

Model regularization

**Why It Matters**

This ensures stable markets remain precise while volatile markets remain robust, without manual tuning.

**4. Recap — Feature Engineering Overview (~130 Features)**

The forecasting pipeline uses a broad and structured feature set designed to capture the main drivers of call-volume behavior:

**Calendar & Seasonality:** day-of-week, monthly and cyclical patterns

**International Holidays:** market-specific holidays and proximity windows

**Lag & Trend Signals:** recent call history, rolling averages, momentum

**Volatility & Anomalies:** spike/drop detection and variability measures

**Distribution Metrics:** percentiles and dispersion for realistic demand ranges

**Interaction Effects:** compound signals (e.g., holidays × volume level)

**Time & Growth Signals:** long-term trend and growth indicators

**Why it matters:**
Starting with a rich feature set allows the model to learn complex patterns. Automated selection then retains only features that improve accuracy.

**5. Feature Engineering Pipeline — Function Catalog (Summary)**

The pipeline is implemented as a modular set of reusable functions covering:

**Data Loading & Cleaning** — load historical and backtest data, handle missing values

**Baseline & Growth Computation** — compute year-over-year growth factors and seasonal baselines

**Synthetic Forecast Construction** — generate future-period baseline values

**Holiday Feature Generation** — apply international holiday calendars and proximity features

**Trend, Lag & Volatility Features** — rolling statistics, momentum, anomaly detection

**Market Stability Classification** — automatically assign stability tiers

**Dataset Assembly** — produce the final feature matrix for training and prediction

**Why it matters:**
This modular design ensures consistency, simplifies maintenance, and allows the pipeline to scale across markets.

**6. Modeling and Validation Approach**

**What Was Implemented**

Trained multiple model families using:

Simple train/test splits for fast iteration

Walk-forward cross-validation for robust validation

Selected the best model using **out****-of****-sample accuracy (MAPE)**.

Retrained the winning model on all available data before generating final forecasts.

**Why It Matters**

Models are selected based on proven performance on unseen data, increasing confidence in forecast quality.

**7. Multi****-Market Execution**

**What Was Implemented**

Automated execution across all International and Casino markets.

Each market runs with:

Its own stability tier

Tier-specific configuration

Independent backtesting and model selection

**Why It Matters**

Each market receives a forecast tailored to its behavior, without manual intervention.

**Current Status**

Feature-engineering framework implemented

Synthetic forecast baseline stabilized

Market stability tiers operational

Modular pipeline and orchestration in place

Multi-market execution running

**Next Steps**

Review and validate forecasting functions

Produce a **first end****-to****-end forecast run for all markets**
*(no optimization or parameter tuning)*

Carlos A and Bao

E-commerce:

Expanded web related features for journey score model, more that 20 new features added related booking_funnel, air_funnel, casino_funnel, visited page category...

Evaluated the impact of latest added epsilon txspend categories in all  models we maintain.

**Completed ****backtesting**** for consumer segmentation and targeted offer strategy**, including model comparisons.

Found that the original target definition (low booking propensity + high web propensity) may not hold.

Booking propensity showed a clear linear relationship with actual booking rates (strong signal).

Web propensity did not meaningfully differentiate booking behavior, suggesting it may not effectively capture true booking intent.

**Impact:** Results may lead to refinement of segmentation logic and more effective targeting strategy.

**Next Steps:** Align with Pablo and Carlos to reassess segmentation strategy, potentially adjusting or removing the web model from segmentation criteria.

**Implemented new app-usage–driven features into the booking propensity model (via Azure DevOps pull request).**

Engineered and integrated ML features capturing consumer app engagement behavior, including:

Post-voyage app usage rate

Post-voyage app usage count

Onboard app usage count

Additional engagement-frequency and recency signals

Once approved, these features will be incorporated into the next training cycle.

**Impact:** Positions us to quantify incremental predictive lift from app engagement behavior and better capture post-experience rebooking intent signals.

**Advanced clickstream data preparation for journey scoring model.**

Re-identified ~60 relevant columns.

Built filtering logic to remove redundant, technical, high-null, constant-value, and extreme-cardinality fields.

**Impact:** Improved data quality and streamlined feature space to support more robust journey scoring model development.

Ben F. and Camila A.

Supply Chain IBP:

- Improved prorations of weekly voyage forecasts to monthly level ensuring pro-rated forecasts are improved in their allocation to months and then subsequently get allocated back to the voyage level. Validation of improved prorations are complete and enhancements have been pushed to production.

- Work in process on refactoring finance tool code to have code more efficient, easier to read and segmented from a monolith notebook into 14 smaller notebooks. Data validation and code refinement are pending.

- Delivered visualization to shipboard inventory managers on Beyond identifying how the AI demand model arrived at its recommended procurement amount on the May 3rd sailing. The visualization details why this approach is likely to be more accurate than using a simple rolling trailing average approach, given the AI model has momentum predictors and this product has a downward trend in consumption patterns.
**Freeze Predicted Voyage Demand Finance Tool**
- Fixed an issue where Predicted Voyage Demand values drifted each week as sailings transitioned from forecast to actuals. The fix reads the frozen PVD directly from the SSO overwrite table instead of recomputing it each run.
- Prorates frozen PVD proportionally across department and GL detail rows. Preserves orphan products and their inventory average cost via enriched stub rows.
- Backfilled missing accounts for the 4/5 sailing and replaced already reported predictions with the 4/10 parquet snapshot.
- Validated across all 45 ships with backup written to FROZEN_PREDICTIONS_FINANCE_TOOL.

**Daily Requisition Ghost Row Fix**
- Root cause: completed voyages with no matching consumption records flowed through the past_unmatched path, producing ghost duplicate rows with NULL voyage/consumption that still received baseline values
- This doubled per-guest variance for March 2026
- Fix: Added Step 11b to filter out rows where both TOTAL_CONSUMPTION_DOLLARS and TOTAL_CONSUMPTION_QTY are 0/null
- Followed up with additional fixes for consumption inflation and daily requisition overwrite logic

**Production Order Supply Name/Venue Level Consumption Ratios**
- Replaced the legacy all-time consumption ratio approach with a hybrid voyage-lagged method
- Primary method: computes the consumption share of each supply name using the last 5 completed voyages per ship/product combination. Recent voyages better reflect which supply names are actively being consumed
- Fallback: when fewer than 1 prior voyage exists (new ship/product combos), falls back to an all-time ratio across all history since 2023

**Override Tracking and Scorecard Updates**
- Updated ActualGL_Charged_calc in override tracking (removed 291 lines of legacy code)
- Brought prediction and actuals columns into scorecard components (future_spend_P3, override_tracking, production_order_scorecard)

**Sushi/Raw on 5 ****consumption**
- Venue level daily breakdown consumption and spend tracking. Could then be aggregated up to voyage level so that the integration for override notebook and daily breakdown notebooks is simple

**ETL Bid Data Hardening**
- Accept .xlsm/.xlsb files (not just .xlsx) via updated extension filter
- Added pip install pyxlsb for binary Excel support
- Added Sheet1 fallback when Data sheet not found
- Added empty DataFrame guard to prevent ValueError on files with 0 rows
- Applied to both RCI and SSC bid data notebooks

**SSC Finance Tool Updates**

- Step 3A: Fixed SHIP_CODE derivation for Silversea. Previously defaulted to null. Now joins voyage table on LOCATION_NAME + SAILING_DATE via broadcast to look up the actual SHIP_CODE. Ships without matching voyages (e.g. SILVER CLOUD with no future sailings) retain null SHIP_CODE via left join
- Step 3A: Fixed MOST_RECENT_CONSUMPTION_TRANSACTION_AVERAGE_COST to use ignorenulls=True in the window function, preventing null costs from masking real values
- Step 3C: Added the same voyage-based SHIP_CODE lookup for stub records (forecast-only products). Removed the hardcoded null SHIP_CODE assignment that was overwriting the joined value
- Fixed 2× cost doubling bug and historical drift issues in the Finance Tracking Tool
- Added ML forecast vs. actual consumption tracking columns (PREDICTED_VOYAGE_DEMAND, ACTUALS_VOYAGE_DEMAND)
- Fixed under-reported demand for cross-month sailings
- Split Step 3E into two standalone notebooks: Step 3E (Finance Tracking Tool) and Step 3F (Cost Tracking by Region)
- Added safeguards to prevent debug runs from overwriting production tables

**Project: IBP | SSC Crew Count Model – Downstream Notebook Testing**

**[DOE-1230] IBP | Testing latest crew count changes on downstream notebooks**

**Completed:**

**ETL rerun and CCR integration progress**: Re-ran ETL.ipynb with your latest changes so that CCR crew count can flow into the final training dataset (ssc_uniform_weekly_consumption_voyage_data), while working through multiple execution errors and using Autopilot-driven edits to get to a successful run.

Comment and dataset link:

**SHAP/****backtest**** runs with and without crew count**: Successfully ran SSC_Demand_Model_Consolidated_SHAP.py end-to-end with the **old feature set** (without SCD_CREW_COUNT) and then kicked off a second full run **with the new feature set** (including SCD_CREW_COUNT), with baseline model metrics notebook queued for comparison.

SHAP notebook and metrics links:

Comment:

**Bug investigation and workaround for Databricks repo crash**: Traced a Databricks notebook crash to an interaction between VS Code–pushed changes and the Databricks repo, then documented a workaround by **replicating the repo** to get back to a stable state.

Comments:

**Ongoing:**

**Feature impact + performance comparison**: Building and running a small comparison framework to quantify model performance deltas between: (a) current feature set and (b) feature set including SCD_CREW_COUNT, using SHAP outputs and MdAPE as key decision metrics.

Comment:

**Uniforms distribution & combinatorial features**: Analyzing how gender/generation one-hot distributions are constructed from prd_silver.client.supply_chain_onboard_uniform_demand, identifying scaling issues when ratios don’t sum to 1, and proposing **combinatorial ratio features** so the model can better capture joint distributions (e.g., generation x gender) instead of assuming independence.

Comment and reference tables:

**Project: IBP | Track All Source Tables (Medical, Uniform, CocoCay)**

**[DOE-1333] IBP | Track all source tables from medical, uniform, ****cococay**

**Completed:**

**First****-pass automated table discovery**: Used the existing table-search (regex-based) script to scan target repos and identify candidate table references, then manually filtered out obvious non-tables (e.g., version strings, datetime.now) to produce a cleaned list of likely table names.

Comment:

**Compiled “Tables” sheet**: Consolidated the filtered list into a “Tables” sheet in a shared file, giving the team a concrete artifact listing non-prd_gold tables used in SSC Uniforms, Medical, and CocoCay code paths.

Comment:

**Project: IBP | PRD GOLD Table Paths – Decimal Data-Type Changes**

**[DOE-1334] IBP | PRD GOLD table paths to test numerical values change**

**Completed:**

**Leverage table reference script from DOE-1317**: Confirmed use of your existing table-reference script (from DOE-1317) on the DA2I-RCG_SUPPLY_CHAIN repo to map where the affected PRD GOLD tables are referenced in code, as a prerequisite for testing upcoming decimal data-type changes.

Comment & repo link:

Connect your Github account

**CSV of all affected file references**: Produced and shared a CSV listing all files that reference the impacted PRD GOLD tables, giving the team a concrete starting point for targeted regression testing.

Comment:

**Reference count enrichment**: Augmented the shared file with a sheet counting how many times each source table appears across the codebase, enabling a **least****-mentioned → most****-mentioned** prioritization for testing effort.

Comment:

**Project: IBP | Purchase Order (MOT) Metrics – Future Voyages Extension**

**[DOE-1185] IBP | Purchase Order (MOT) Metrics**

**Completed:**

**Extended voyage base with future voyages**: Implemented a supplemental voyages source to extend beyond what consumption_gold_chkpnt alone provides, concatenating brand code, ship code, YYMMDD, and zero-padded sail nights into a consistent voyage number format to **include spend from future voyages** as requested.

Comment:

PR: Connect your Github account

Table reference:

**Caleb S.**

**CLV Update**

**In Progress**

Supporting competitive intelligence with strategic analysis of MSC's market positioning, specifically examining MSC's initiatives to accelerate private destination and island (PDI) expansion across the Caribbean region

Conducting validation and reconciliation of key metrics within Executive-level PowerPoint deliverables, leveraging outputs from the competitive cruise fleet model to ensure accuracy of reported figures

**Completed**

Delivered hurricane risk analysis findings to the AVP of Corporate Strategy, providing quantitative inputs to inform capital allocation decisions related to private destination investments

Identified and resolved passenger duplication defects within the CLV table pipeline that were propagating erroneous results to downstream reporting

Corrected row count inflation caused by faulty join logic against outdated source tables, and remediated inconsistencies in un-proration calculations

Communicated findings to upstream data owners with reproducible examples of source table defects to facilitate remediation on their end

Ayon G.

Win-on-Waste

Team is busy bug fixing in inter port and specialty V2 this week

Neila

**RCI Rev ****Mgmt****: ****DUAL | Baskets | Short Caribbean, Alaska, Europe, Galapagos (CEL), Mexico (RCI), and**

**West Coast Short RCI**

I completed the development of the metaproduct basket framework within the automated sailing grouping system and successfully implemented it for Short Caribbean, Alaska, and Europe. This included additional completion of Alaska (C/R), Galapagos (C), Mexico (R), and West Coast Short (R), which were not part of the original regional list but were incorporated under the same framework and standards. The implementation is currently in progress for Long Caribbean, following the same modeling, validation, and basket construction approach.

This work standardized the booking pace feature engineering by measuring occupancy at fixed days-to-departure windows (360 to 30 days), constructed the sailing trait matrix including ship class, homeport, and itinerary, and assigned peer groups using decision-tree-based statistical basket assignment validated by meaningful pace separation at key action windows.

I derived operational product baskets containing only contiguous sailing weeks and computed velocity corridors using percentile bands, including P10, P25, P50, P75, and P90, across every days-to-departure bucket. I also implemented pricing signal logic to classify each sailing into one of five action categories with a clear recommended action. The Alaska basket was fully completed and marked as “Completed Alaska.”

All completed regions will move into testing and QA together rather than sequentially. The work is currently at approximately 90% completion, with ongoing validation of basket behavior, pace separation, and pricing signal stability. A quarterly recalibration process has been defined to refit models on a rolling historical window.

Next steps include finalizing QA for all completed regions, continuing development and validation for Long Caribbean, validating end-to-end basket performance, and preparing the completed regions for deployment.

Michelle

**RCI**** Rev ****Mgmt**** | Category-Gapping 3.0**
Utilizing training class I previously built to efficiently train EBM models at multiple granularity levels. Each model uses time-based train/test split, applies balanced class weights, computes train/test AUC metrics and training time, logs to MLflow. The class allows me to train multiple models in parallel, changing features and data sets quickly to test various options.

Explored features and class weights to improve model performance as was done for CEL

Creating lookup tables for all availability cases. Must review shares to assess model performance. Need to meet with team to discuss how this will translate into category level recommendations.

**Michelle**

**CEL**** Rev ****Mgmt**** | Category-Gapping 3.0**
Reviewed initial optimization with business and received feedback. Built out 8 availability dependent formulas. Unified process to run for all future sailings and select appropriate formula for cat-class.
The optimizer evaluates all eligible options, calculates revenue at each feasible scenario, and then selects the best option. For each booking, the optimizer considers:

Eligible tier options

Expected value of each tier

Predicted booking share

Predicted price

Inventory or capacity limits

GTY status

Regardless of GTY status, the optimizer follows this basic sequence:

Filter out ineligible options (closed tiers)

Calculate revenue at each option

Rank options from highest to lowest revenue

Apply constraints and select the best feasible option

In all cases, the optimizer:

Respects capacity constraints: Bookings are only matched to feasible booking share rows

Uses a distance based matching framework: Each booking is evaluated against available booking share distributions. The optimizer selects the closest feasible match.

Operates within eligibility and inventory rules: No invalid tiers, cabins, or options are selected.

The difference lies in how GTY is treated as a constraint.

Feedback:

Predictions for cases when lower, upper, and premium are stable and performing well. Shares were not decreasing smoothly when only 2 tiers are available. For when only lower-premium available, shares were not changing from gaps 1-3%.

Improved predictions by adjusting weights, max bins in training, and input data. Now decreasing smoothly for all availabilities. Team also

Doug

**RCI Rev ****Mgmt**** ****|  Inventory**** Automation KPI - Quantification Model & $ Impact Estimation APR**

Quantification Model Development & Validation

Expanded initial estimates to include a 7-day moving average of expected GTY booking volume had GTY been fully-available. Unmet demand measured by the daily difference in expect vs. actual bookings. Potentially lost revenue equates to twice the fare (double occupancy) * missed bookings on days when stockout in effect. As a conservative threshold, only consider rows where cat class booked position is < 85%.

The KPI modeling ticket will be fully closed this week.

One subtask is being dropped because the analysis was not viable.

The current ticket will not move forward.

A follow-up discussion is planned next week to explore alternative approaches.

Doug

**RCI Rev ****Mgmt**** | Detect, Troubleshoot, Validate Live Data Outage | APR**

**Detection & Initial Reporting**
Live streaming data delays were detected and reported to the RMA – Production Issues Teams channel at 6:28 PM on 4/7/2026, based on two consecutive warnings indicating that five tables had not been updated in over two hours. At the time of reporting, data was approximately four hours out of sync.

**Investigation & Mitigation**
Mobilization of the team to identify the issue began immediately. Kafka streaming was identified as the root cause on the morning of 4/8/2026. Supporting queries and data samples were provided to assist the team in tracking down the issue. Streaming was subsequently restored, and production processes began coming back online.

**Post****-Fix Validation**
Post-fix analysis and validation continued through 4/9/2026. It was determined that after restoration, some tables were missing the most recent data from the source tables. The affected tables were identified, and manual refreshes were performed. By end of day on 4/9/2026, process checks demonstrated that production systems were running as expected again.

**Final Status**
Status: **Complete as of 04/10/2026**

**Deliverables:**

Live streaming of RMA inventory tables was restored.

Post-fix validation of production processes confirmed normal operations have resumed.

**Delays:** None.
**Potential Future Issues:** None.

Sriklekha

CEL Rev Mgmt – Promotions Analysis

Space left vs Replacement value pax  Analysis

**Status**: This ticket is complete as of **4/12/2025**

**Deliverables**:

**Space left vs Replacement Value Pax analysis**

Gathered and consolidated the data needed to calculate booked position with and without retention demand, as a significant amount of time went into building the required base data for the analysis.

Analyzed when exciting deals/promotions are being realized across meta-products, with a focus on whether promos are typically introduced closer to sailing when there is still more inventory left to fill.

Identified a common pattern that for many sailings, replacement-value promos begin around 15 weeks to sail, primarily to fill remaining space rather than based on whether the sailing is beating or missing track.

Evaluated the relationship between remaining space and track performance, and observed that in many cases inventory left to fill appears to influence promo decisions more strongly than the gap to track.

Found examples where sailings were already beating track, but replacement value was still being offered because the focus near sailing shifts more toward filling availability.

Planned next step is to map each current sailing to good SPI sailings with similar characteristics, and then compare the week-over-week booked position against those good SPI sailings to help determine whether a promotion is really needed, should be tightened, or can be avoided instead of adjusting promos with respect to track performance

These plots show that for a sailing, promos are being used mainly to fill the remaining space as we get closer to sailing; even in some weeks where the gap to track without replacement value looks better, promos are still offered because filling space is being prioritized more than track performance.

**Segment****-level conclusions**

Segmented the analysis by **weeks****-to****-sail (WTS), meta****-product, and ship class** to understand whether the observed promo behavior is consistent across different demand and capacity profiles.

Observed that **replacement influence is highly segmented by WTS**, with replacement value being most prominent in the 0–12 WTS window, where booked position is already high but remaining inventory still drives promo decisions. Beyond ~15 WTS, replacement impact materially declines and booked position trends align more closely with organic demand.

**Meta product level**

**Short Caribbean**

Low booked position early

High reliance on replacement closer to sailing

Promos frequently used even when track performance is healthy

**Europe / Alaska**

Strong early booked position

Low replacement dependence

Promos more aligned with true performance gaps

**Ship Class**

**EDGE class**

Consistently high booked position across WTS

Very low replacement impact

**Solstice / Millennium**

Lower early booked position

Ignacio

PCP Pricing Automation

**Recurring Business Meetings & OBR DS Meetings**
Meeting was had with Garrett & Correa from CEL to discuss progressions in the EDA for CEL Beverages
Meetings had with others on the OBR team regarding questions on promo automation & sharing the changes done
**Enhanced Promo Automation via ****Sharepoint**
The “NAME” column was added into the spreadsheet in order to have it automatically fill in the user name of the person on the business team filling out a specific row (promo) on the Sharepoint sheet. This can help keep track of who does what and perform some internal tracking.
The addition of the 2 additional SAILING TAG columns (for AND Groups conditions) was then also completed. It is tested in lower environment with digital & DE team in order to validate its functionality before pushing the changes to production.
All these changes had to be tested in lower env E2E with the digital & DE team to ensure all works as expected before pushing to production
**CEL EDA Phase 2**
Additional EDA was done for the CEL Beverage, mainly focused on Premium package but also covering the other packages as well. Some of the areas of interest from last time were covered, such as focusing on Rate Only pax in a more clear manner. Useful visualizations were derived from analyzing the relationship of average price of weekly bookings with a normalized version of demand (new bookings divided by count of rate only pax). These plots, especially at rounded price intervals, helped capture clear elasticity relationships at different segmentations. Particularly in this case, the elastic relationship was analyzed at the meta product level, ship class level, and WTS bin level.
**EDA into Track curve for Beverage (RCI)**
Some EDA was done on booking & revenue trends for beverage products in order to create some reasonable track curves on how cumulative revenue trends as WTS trends toward zero for different segmentations of sailings from last year. This is meant to then be compared against Jorge’s track and validate/correct/smooth it as necessary.

Aagam

PCP Pricing Automation

**RCI | OBR | RBC Business Rules Driven (Passes and Waterpark) PRE v1**

This week, I started developing an initial version of a pricing recommendation framework for RBC Passes and Waterpark products to support onboard revenue optimization.

As a first step, I conducted exploratory data analysis to understand booking behavior across sailings. Specifically, I identified the points (days to sail) at which each sailing reached 25%, 50%, and 75% capacity. Using these benchmarks, I defined four distinct booking phases that segment the booking window:

**Phase 1 – Initial Booking Period:** ≤ 25% booked

**Phase 2 – Slow Momentum Phase:** >25% and ≤50% booked

**Phase 3 – Prime Booking Window:** 50%–75% booked

**Phase 4 – Final Stretch:** 75%–100% booked

These phases were calculated based on the past 3 months of sailings and assigned for the future sailings at the **meta_product_code**** × ****product_code** level, allowing for more granular tracking of booking progression by product.

Building on this, I created a preliminary **sailing score** to assess performance, defined as: **√(****current booked position × cumulative clickthrough rate)**.
This score is intended to serve as a normalized indicator of how a sailing is performing relative to demand and engagement.

Furthermore, I added another factor that looks at the momentum of web visits and created a business rule where we would raise prices where we see a higher momentum and drop prices if we see a slow momentum.

**RCI | OBR | Ad-Hoc Analysis 04-13 to 04-17**

Completed the analysis to see the impact of the Flash Sale for casino members that was present from 04-09 to 04-13 and submitted my findings to the business team.

**Insights:**

Had a positive impact on the revenue for the alc passes, but it may have contributed to non-alc passes as well.

PRIME loyalty tier had the highest increase in revenue

Most of the meta products saw an increase in revenue except Short Caribbean

Analysis:

Kevin D.

PCP Pricing Automation

Built a prototype app for mass promotions UI. Still very much work in progress on the routing and feel. this is using dummy data / not connected to anything but made some good progress on the upgraded mass promo UI:

Glen-Erik C.

PCP Pricing Automation

I also am working on the UI for 1:1 targeted offers. Here are (1) the mockup for the input so you can see how the text will be displayed on the app, and (2) mockup for the screen showing the user the output after validations pass before sending to dev/stage/prod.

Eddie B. and Kevin D.

RCI Rev Mgmt

Presented to Goldner and Product Team Directors how many of the counterintuitive recommendations (30%) are actually due to demand forecast mostly predicting demand, but there is a disconnect between future track expectation dramatically changing (a change-point). A common situation is Beating Track, but Lowering Rate (due to spiked future track need). This can create a disconnect as analysts tend to look at recent performance to track and don’t manage like PRE does to futuretrack (even though they should).

**Outcome:** This was a pivotal moment of change-management and will likely lead to MUCH higher adoption of PRE by the product teams. Generative AI tools will likely bring even closer alignment of RMA automation with pricing analysts.

**Action Items: **

- instructed we smooth the tracks (a no-brainer since they are noisy). Will be delivered by Chris in Rev Strategy by early May. The process of building it into the track process is complicated and needs to be done for every CCO and needs to match with Dtrack.

- more reporting to highlight when a paradoxical or counterintuitive situation is occurring.

- Provide more education to pricing analyst to see outcomes to learn when PRE was actually right and they were wrong (and vice-versa)

Goldner: Asked if recent performance is directionally misaligned with current rate that hits future track.

10-20% of the natural pickup and drop in the Next 3-Weeks

Were still missing on insides because product team held rate (FIT for 4/17). We are only get 10-11 this week based on trends and demand forecast is closer.

We need to either lower price now or adjust track. They took recommendation this week, but not last week. Now its $569 taking the recommendation.

Quantify how often we are beating/missing track, and then the demand forecast doesn’t think we will get to the volume that track asks. Shape of the track isnt optimal and isnt going to happen from natural demand.

Goldner didn’t like that we beat track to raise rates, but then we couldn’t meet track.

The right answer should have been holding $589 at 3/27 or even lower to $569.

Identify the amount we are making a price change. Breaking down the price change logic

Product Teams look week to week change in performance (L3W of performance).

Wants to account for WTD. Run a quick view

Have we been pausing recommendations (where are the humans going against the machine when its right because of very different future track asks)?

We overshot after lowering price at 3/27 more than PRE recommendation. Shape of the curve was in-line with historical demand.

**Goldner: ****How ****we**** identify when track and demand forecast are misaligned in direction, or same direction but very different magnitude****?**

- Bring awareness of how these examples happen, and what the outcomes.

- Whoever owns that example and a regular report as an analyst where things like that happened. This meeting was a pivotal moment of change-management and will likely lead to MUCH higher adoption of PRE by the product teams. Generative AI tools will likely bring even closer alignment of RMA automation with pricing analysts

***Erick A******., ******Cristian V., ******Danusio****** G., Osvaldo V., David M., Rodrigo B.***

**PCP**** ****MyCruise**** Recommender**

**Collaborative Filtering Improvements**

**Guest Segmentation ETL Shipped** *(**Danusio** G.)*: Delivered both ETL artifacts — model saving and backtest table construction (mcr_team.booking_clusters_base) — with a demo notebook explaining the pipeline. Migrated from Scikit-learn/Pandas to PySpark for scale and switched the time index from return date to booking creation date to prevent data leakage. Code is ready for PR.

**ALS Optimization — 4x Speedup** *(David M.)*: Implemented Bayesian hyperparameter optimization for the ALS model, reducing training time from ~20 min to ~5 min per week with improved RMSE. Currently rewriting the evaluation metric to replace RMSE with a novelty-based metric and refactoring the recommender class. Debugged full-dataset training slowdown with Cristian.

**Product Clustering — Embedding Validation** *(Osvaldo V.)*: Ran LLM validation across three clustering approaches — embeddings (30% misclassification), GPT-4.1 mini (40%), one-hot encoding (50%). Embeddings retained. Identified a data-source gap (6K vs. 35K products) and is testing sailing-level batch classification using GPT-4.1 1M context.

**Apriori**** Model**

**Apriori**** Robustness — FP Growth Breakthrough** *(Rodrigo B.)*: Root-caused the ~40% empty-recommendation issue to pairwise vs. complete-basket support calculation. Built a new FP Growth model achieving **~96% coverage** with better rules. Built a CF empty-recommendation test framework and demonstrated Apriori fallback achieves 80-83% coverage when CF returns empty, with only ~5% overlap (i.e., Apriori surfaces genuinely new products). Next: ticket-size-aware fallback logic.

**Hard-Coded Product Slots** *(Cristian V.)*: New task to support specific business overrides in the recommendations API.

**A/B Testing & Front-End Signal**

**Apigee Use-Case Parameter — Schema Constraint** *(Cristian V.)*: Investigation surfaced that Databricks only reads keys under dataframe_records. Lance and Rosie will embed the use-case parameter at that level. A/B testing is queued behind the calendar and ForYou fixes deploying.

**Infrastructure / Postgres**

**Dev Postgres Performance Recovered** *(Cristian V., Erick A.)*: Dev DB load time improved from 10+ min to **3:54 min** after Marcio's upgrade. Parallel batch loading confirmed. Prod DB was not upgraded in the same pass — Erick is following up with Platform (and referencing Cristian's existing prod scaling ticket) to ensure prod receives the same treatment.

**Databricks ****GraphQL**** Staging — Unblocked** *(Cristian V.)*: Verified outbound HTTP was already enabled. Staging/test GraphQL access integrated directly into the existing job, eliminating manual data pulls. Task closed.

**ForYou**** Model Coverage Fix — Blocked** *(Cristian V.)*: Postgres-side performance work done, but still blocked on calendar schema deployment and prod Postgres provisioning.

***Erick A******., ******Cristian V., ******Danusio****** G., Osvaldo V., David M., Rodrigo B.***

**Project Axiom — Voice 360**

**Meta Data Extraction *****(David M.)***

**Guest Logs Gold Table — Still Waiting** *(David M.)*: No response yet from Alex Kim on input-table discrepancies (single record per guest_log_id, missing log ID column). Erick following up. Final topic categories also still pending from Alessio.

**Azure Grok Model Inconsistencies** *(Erick A.)*: Reached out to Microsoft Foundry Support to inquire about Grok latency concerns. Microsoft to follow up.

**Databricks Asset Bundles** *(David M.)*: GitHub Actions config created; asset bundle tested in dev. Blocked on Databricks tokens (Erick to create).

**Email Reports *****(Rodrigo B., ******Danusio****** G.)***

**Port Report Deployed for Efrain** *(Rodrigo B.)*: Shorex query approach implemented; port report deployed into a Port Operations facing dashboard pipeline.

**GSO Reported Email Bug** *(**Danusio** G.)*: Root cause identified; Danusio QAing the fix and optimizing code before handing off to Erick.

**Gratuity & Tips Email Report** *(Rodrigo B.)*: Email report is complete. Pending business review.

**Guest Logs *****(Erick A.)***

**Guest Logs Data Clean Up Presentation** *(Erick A.)*: Prepared a presentation to share with Hotel Operations on the critical data cleaning efforts that will need to be done to log classifications. The clean up will unlock all future use cases such as tracking trends, summary generation, and predictive modeling.

**Target Setting *****(Erick A.)***

**Target Setting Improvements** *(Erick A.)*: This repo forecasts customer satisfaction and rebook rates at the sailing level for Royal Caribbean and Celebrity Cruises. Recent work focused on building a validation dashboard comparing AI vs naive vs business targets, stabilizing multi-model benchmarking, enriching features with temporal and ship-level data, and improving forecast accuracy through recency weighting and stricter training controls.

**Axiom Web App *****(Erick A.)***

**Web App Migration** *(Erick A.)*: Working towards migrating the Axiom app to Azure Container apps.

Camila A. and Ben F.

IBP

Laura, Juan, Keith, and Evan are impressed with the BY pilot and conversations are shifting to fleetwide adoption. This is a BIG win for the group. I want to take a moment to recognize the exceptional effort Ben and Camila have put into the IBP Pilot. Both have been working extended hours (late nights, weekends, and even during vacation) to ensure the success of the BY pilot, which is a testament to their commitment for our AI mission. I wanted to explicitly acknowledge them for going WAY above and beyond during this critical phase.
To make this sustainable, we’re planning to bring in the backfills for Cihan and Ayon to help support them. While this level of effort was appropriate for an extraordinary moment, we’re intentionally setting things up so the workload can be distributed more evenly going forward. This directly aligns with the point Naftali raised during the EC Steering Committee around the AI Team becoming a potential bottleneck and doubling the IBP capacity should meaningfully reduce the load and improve resiliency.

David W.

Loyalty

For the launch of Co-Brand this week, we recommended Merging 25,300K records. This is all "YES" LLM-Recommended profile merges. Potential merges must fit this criteria:
* Only share cosine similarity with profiles that have a cosine similarity >0.8
* Dont share if a merge contains two major Loyalty Customers within the same program.
* Tweak sharing only one Consumer ID

Lamis

**CEL Track Optimization:**
Both RCI & CEL track optimization projects are running in parallel
1. The output from Dynamic Programming when compared the WoW % change in track ask it fluctuates a lot. While this is the optimal solution, it does not reflect the way the business operates.
Since we are no longer doing an MILP optimization model but DP, in order to control these weekly changes the DP state needs to be revised to memorize past decisions. This is going to grow the size of the problem by a lot.
Instead, I worked on a hierarchical optimization approach such that - (1) in the first stage the DP runs and generates these optimal but noisy weekly track asks then (2) in the second stage an MILP model runs to smooth these weekly track asks while minimizing the deviation from the optimal solution and the week over week change.
While this provides a near optimal solution it is very fast to run. Took 27 secs after the DP to run on CEL EUROPE sailings.
Initial results of the weekly track asks are a lot better compared to the raw DP output and  the overall shape of the track did not deviate much from the optimal shape.
Results will be presented to the SHs next week for both brands.
2. On looking at the SPI based tracks. The CEL team asked to test various grouping to determine similar sailings and so filter for the top performers amongst those. Originally I was analyzing at the meta - peak season - holiday season levels.
CEL team asked to test RDSS level. Results did not change much from the meta level.
Since the overall goal here is to see if we will constraint the optimal to stay close to the SPI based top performers I analyzed both the tracks for the top performers and the bad performers within each group. On different levels I noticed that the shape of the track for these two groups does bot change much. An average different of booked position between the two groups is 3-6%
Since I did not find a big difference I am not sure if it makes sense to constraint the optimization to follow these curves as this is not a guarantee for a top performing sailing. Will discuss my findings also with the SHs next week and decide how we want to use these
3. Been on the side working on fixing some of the issues in the data causing optimization to fail including ensuring that we’re reading availability based on retentions (not actual AS400 available cabins), etc.

Anand

PCP Pricing Automation

**Waterpark A/B Testing: Sailing Pair Matching Refinement (ZH01)**

Refined the sailing pair selection algorithm based on business team feedback. Key updates to the matching constraints: treatment and control sailings must now fall **within 7 days** of each other (down from 21), must depart on the **same day of the week**, and must be on the **same ship**. Added hard filters to **check booked position** and **removed holiday sailings from the EDA on past sailings** to prevent confounded baselines. Soft constraints on penetration (≤20% relative diff) and family penetration (≤30%) remain in place. With these tighter rules applied to the **476 eligible sailings** across 20 ships, we are validating that we still meet the **131 pairs per arm** threshold needed for the experiment.

** Product Categorization: Automated Pipeline Groundwork**

Set up the foundational code for an **automated product classification pipeline** in collaboration with Osvaldo from Erick's team. The pipeline leverages a **multi-pass LLM consensus methodology** (primary classification, adversarial QA, and blind re-evaluation) with rule overrides and strict taxonomy enforcement. Reviewed Osvaldo's work and guided the architecture so it can scale to **Dining and Beverage products** using the same L1/L2 framework. This positions us to run the full categorization end-to-end with minimal manual intervention as new product catalogs come online.** **

**Celebrity Analytics: Dashboard Vision & Collaborative Roadmap**

Met and synchronized with **Alexander from the Celebrity business side** to envision how dashboards will visualize insights derived from the product segmentation. Drew mockups of key views, received feedback, and iterated on layout and metric priorities. Currently building a **collaborative roadmap** that clearly divides deliverables between data scientist and data analyst roles, helping the Celebrity team reach their next goalpost in analytics project management.

Evan

RCI Revenue Management

Factor Model(s)

Began on group segmentations and relevant bins

As requested by CEL, group by a combination of port, meta, rdss when enough samples available

Tested initial model for evaluation of track boundaries

Working with Lamis on integration to Track Optimization

Met with stakeholders to evaluate next steps for models and requirements

Demand Model

Began refactoring and expansion of Kevin’s work and analysis of modeling

Added an automatic feature reduction method (SHAP) for transformer in pipeline

Finalized ensemble of ensemble / stacked regressor approach

Finished External Data repository for

Search Trend (Google)

Macro Economic data (FRED, CPI and Consumer Disposable Income)

Will be adding more features and working with Neila and others to identify potential use cases for other projects

SPI Portal

Transitioned new features to dev portal (dev-spi.rccl.com)

Created and tested local deployment of flask with API solution

Awaiting deployment to dev and should allow for faster analysis with more features / data

Glen-Erik C., Javier, Santiago

**PROPEL**

**Measurements:** (Javier)

Presented measurements approach and dashboard to OBR stakeholders and collected feedback to refinement.

Attribution Logic Fixes: Corrected classification into test, control, and organic groups, ensuring all revenue is properly allocated with no exclusions.

Pre-cruise Revenue Handling: Introduced pre-cruise logic for null purchase days, adding flags and metrics while maintaining full revenue reconciliation.

Join & Data Grain Improvements: Fixed duplication and attribution issues by moving to a stable grain and improving join logic.

Data Integrity Enhancements: Removed unsafe deduplication strategies and ensured no revenue loss or artificial collapsing of data.

Validation Framework: Built checks to ensure consistency between raw and transformed data across all scenarios.

Statistical Validation: Applied Welch’s t-test to compare test and control groups reliably.

**Javier**

**PROPEL****: ****XC Casino Issue:** (Santiago)

Diagnosed the issue by reviewing the casino functions, the business rules file, and the execution of those functions within the business-rule filtering file.

reviewed the execution of each of the 10+ business rules involved in the process.

The main issue was in Rule 1, where there was a significant mismatch between the fields required to generate the correct matches.

Initially, I evaluated a solution based on scanning keywords such as “casino” and “free play.” However, this approach proved to be suboptimal because it increased the execution time significantly.

Instead, implemented a more efficient solution based on a mapping dictionary to force the match between fields and resolve the casino offer generation issue for XC.

**Scheduling Issue: **(Santiago)

1. I reviewed the offer-building folder due to the issue of missing casino offers for ship XC.

2. I 3. I also 6. Additionally, I corrected and smoothed the calendar hours to prevent inconsistencies and potential operational issues.

Eswar

**RCI Rev Mgt: ****RMA (**Eswar)

SPI portal updates and deploying updates to container

PRE feature store workflow fix

Following up on support request adding OBR business team to rev mgmt. databricks workspaces to give access to OBR workflows as er request

Discussed OBR promo uploads process and OBR portal requirements

Databricks Asset Bundle Standards refactoring: (*Javier*) worked on standardizing the PRE-project workflows.

Glen-Erik

**PCP ****Pricing Automation **(Glen-Erik)

Targeted offers:

Testing: Sent offers to fake bookings in PROD, removed blockers to get the offers through to the app, pending re-delivery to the app for notification validation.

Real offers: Almost ready to deliver real offers, need to get new bookings from Royal and Celebrity once all green lights from testing in prod. *ETA we can send offers early next week.*

Front-end web app: Developed front end to submit offers to dev/stage/prd, working pulling real booking data from databricks. Next steps: still needs some UI refinements, writing and validating the output in databricks to be compatible with kafka. And the creation and deployment to a web app container.
