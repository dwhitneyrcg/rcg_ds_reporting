Mert, Ben, Dave

IBP

Held several meetings with the IBP and GMO teams regarding marine supply chain optimization. The two teams are currently misaligned on delivery pacing, and as a result, progress is stalled.

There is top-level alignment between Jim Wells, Brian Sorreson, and Jessica Ohanian on prioritizing IBP-expansion in M&T, but there are concerns within GMO on prioritization due to the ongoing upgrades to AMOS X and operational challenges in transitioning to new ERP system (Project Catalyst).

There will likely be escalations to Brian Sorresson next week from within M&T. The AI Teams have suggested a STEERING meeting between the senior leaders and mid-level management team leaders to align IBP & Asset Management teams on 2026 priorities and lay down a sustainable IBP roadmap that accounts for other high-value M&T Initiatives.

While the AI Teams have pivoted quickly to deliver on the BY pilot and other 2026 priorities for Supply Chain, our small AI team is working at an unsustainable pace. We have a new Data Science contractor starting to help Ben & Camila, and will continue to monitor the situation.

Dave, Mert, Utkarsh

New Build

Completed the creation of Azure resources for the Newbuild AI Knowledge Assistant project. However, project progress is currently paused due to a review by the Cyber Security team. The BISO requested an architecture review before approving the creation of service principals and is out of office for the entire week, pending their return.

Alfredo from new Build is keen to get started and raised this to me personally yesterday (noting the delays). there are delays in NewBuild, then both IT and AI teams get in the cross-hairs of NewBuild. We want to stop the Cadentia pilot, but if we cant develop a compelling alternative, we just undermined ourselves.

Mert:
MIAP
Met with the GMO team during the monthly AI Steering Committee meeting and discussed the request to understand AI savings potential across all areas of the company. The GMO team will provide estimated savings potentials for their respective domains.
Completed tag mapping for over 1,000 tags for RD-class variable chilled water systems and AHUs.
Met with the Deployment team to review their request to replace and digitize the Prime tool. The Prime tool takes deployment inputs and calculates fuel, cost, and revenue metrics, allowing the team to compare itineraries and select the best option. The current tool is over 10 years old and Excel-based. Digitizing this tool will enable its use for optimization.

Arya:

MIAP
Fixed a Valmet ETL landing bug.
Added RA and EQ signals to propulsion.
Created a statistical expectancy–based model for no-optimization runs for digital twin power plant forecasting.
Currently integrating the model into the digital twin.
Integrated the Shore Power Connect app into the MIAP app and added live fleet tracking (currently enabled for 13 ships).

Will:
MIAP
Updated FACTS features to calculate fuel ratios.
Developed functionality in the Digital Twin API to retrieve FACTS fuel splits over the last N days.
Developed a FACTS model in the Digital Twin API, enabling fuel forecasting for ships with insufficient data.
Implemented FACTS as an option/fallback in voyage simulation. (After discussing with Mert today, this will be refactored so FACTS is a separate option and does not replace the No Optimization case that Arya is developing.)
Began removing non–power-plant consumption from the FACTS model to improve alignment with voyage simulation in the Digital Twin API.
Met with the Deployment team to discuss new initiatives in Deployment Optimization.

Mahshad:
MIAP
Finalized the AHU deviation-detection agent.
Began development of chiller deviation-analysis tools.
Advanced anomaly and deviation analysis for SM and CS AHUs, indicating a potential total energy-savings opportunity of approximately 500 kW.
Collaborated with the GMO team on benefits tracking by providing analytical support and helping refine their reporting approach.
Met with the Deployment team to align on next steps for itinerary optimization and define the upcoming workflow.

Ben & Camila

**SUPPLY CHAIN**

**Voyage Financial Impact Analytics** — Completed & validated.

**Project: Weighted Average Cost Tracker (Step 4: Sea/Port Day APD & Financial Impact)**:

**Built:** Final pipeline answering: *“For every product on every ship, how much more/less are we spending per guest on sea days vs port days vs historical baselines?”* Fleetwide automated sea/port cost performance + forward projections for upcoming voyages.

**Capabilities:**

**Sea/Port Day cost allocation:** Past = actual daily consumption mapped to itinerary-classified sea/port days; future = proportional forecasts (accurate actuals + best-estimate projections).

**Financial impact scoring:** $ impact per **product × ship × voyage** vs blended **2024/2025** baselines (negative = savings; positive = cost pressure).

**Null reduction (yearly fallback):** Fills **80%** of prior missing baseline gaps using yearly averages when month history missing; final Financial Impact.

**5 Power BI-ready output tables:** 1 detail table (**15.6M rows × 30 ****cols**) + 4 drill-down child tables.

**Quality/validation:** **85** automated E2E tests; **94%** pass (**80/85**). 5 failures are low-severity edge cases (sub-penny rounding, floating-point precision, legitimate credit transactions). **Zero logic bugs**.

**Formula correction (PR153):** Fixed prior double-counting in Financial Impact formula; values now mathematically precise.

**SSC Finance Tool & orchestration:** Step 1 complete; Step 2 in progress. Updated master orchestration notebook for dynamic notebook routing by schedule type for order creation.

**Production Order Scorecard — Forecast freshness fix:** Updated prediction vs live consumption to use baseline table w/ current-month overwrite (baseline refreshes month-end; intra-month predictions were going stale as consumption rose → inflated error). New logic merges monthly baseline + latest overwrite (finance tool) forecasts so scorecard reflects current voyage demand. **Awaiting Yan feedback.**

**SSC Total Consumption Value YOY & APD Value YOY — New analytics pipeline (Silversea):**

Aggregate consumption: sum USD values + quantities at voyage level from 2023+; zero-floor negative quantities.

Latest guest counts: most recent non-null, non-zero passenger snapshot per voyage.

Join & calculate APD: **APD = Total Consumption Value / Total Guest Count** (voyage level).

Yearly summary: by year + ship (total consumption, guests, voyage counts, yearly APD).

YOY comparison: self-join for absolute/% changes in consumption value, APD, guest counts.

**Crew count data quality / EDA:** Initial EDA complete—cadence gaps (14/15/30-day patterns), rolling headcount avgs by ship, uniform-to-voyage date alignment stats for completeness. Ongoing: reconcile outdated ship codes + review integration of 90-day contract length logic.

**Additional:** Baseline table updated for ESG items. Investigating CocoCay reporting code error—pivoted table is accurate (forecasts vs consumption) but region-level pivot inconsistent; root cause identified; fix under validation.

**Carlos**

**E-COMMERCE**** Customer Target**

Completed: code quality improvements—explicit zero division via Spark 4.x try_divide; parameterized hard-coded values (most moved to config); auto-set env (dev/qa/prd) from host URL.

Fixed recurrent ADF→Oracle load error by reducing double precision on PySpark save side.

Continued manual QA testing of latest improvements.

Continued stakeholder comms on journey stage model requirements; answered questions on existing models.

Reviewed new Epsilon ingestion w/ Carlos; refactored for readability/interpretability.

Enhanced min-max scaling metric logic for more reliable future use.

Pushed PR for new Epsilon ETL; approved by Carlos.

Initiated Journey Scoring model research—constraints + rule-based vs ML comparison.

Advanced low-level consumer behavior dashboard—historical behavior (market cluster, prior bookings, spend) + connection to propensity scores.

Orchestration experiments w/ delegation agent + subagents; subagents can’t perform inline code edits when invoked through main orchestration agent.

Upcoming: awaiting app + clickstream data from Michelle; then EDA + feature identification. Considering dashboard enhancements (marketing filters + CSV export).

Caleb

**CORPORATE STRATEGY / CLV / DEMAND MODEL**

Completed: organized/structured input pipeline to naturalize granularity; validated sources (competitor bot pricing, fleet deployment, cabin mix, sales/marketing spend, embark-port region mappings).

Ran first model iterations (basic feature transforms): **20% MAPE** (≈20% RCG aggregated error on 2025 forecasted yields per pax per night).

Built APCD-weighted aggregated forecast view for Jordan/Joey sign-off vs naive baseline (assume **3% CAGR** YoY yields).

In progress: reconfiguring to reduce error—80/20 train/test split; metrics (MedianAPE, RMSE, WMAPE); COVID-period flags; APCD-weighted supervision by region/brand/year; exclude low-impact/skewing competitors (e.g., Disney); updating Jordan with consistent success reporting.

**Cihan**

**PCP Pricing Automation**

**Alaska ****ShoreEx**** (Gang & Rafa):** Post review w/ Cel + Royal OBR teams, completed dashboard changes:

Bug fix: incorrect numbers from outdated source booking table; replaced across all **6** plots.

Dashboard: migrated old cluster → current infra; plots updated for new categories.

SQL: rewrote all queries (table structure changes).

Data comparison: all 6 plots moved from static 2024 vs 2025 to dynamic current-year vs prior-year.

Features: visibility into guests not purchasing any ShoreEx during Alaska; port_code filter for bundled products by port.

Source table: modified source category table for accuracy.

Brand unification: merged Royal + Celebrity ShoreEx clustering tables into one table w/ brand filter.

Collaboration/handover: multiple meetings w/ Anand; initiated Alaska ShoreEx handover; reviewed LLM-powered ShoreEx clustering notebook w/ team.

**OBR Waterpark PRE (Gang Wang):** Analyzed participation, pricing, demand by ship class + week-of-year; presented to stakeholders; elasticity deck prepped for Friday; meeting scheduled w/ Ignacio + Anand for handover.

**Mirielle**

**CONTACT CENTER**

**Workforce Planning — NA (Royal):**

Building FTE Forecasting Trade-Off Analysis deck for decision-maker meeting (staffing optimization across **12 LOBs** using **Erlang A**).

Analysis complete (Jan 2024–Oct 2025): calls, headcount, AHT, shrinkage, ABN (all LOBs); volume↔HC correlation by LOB; CV variability; LOB archetypes (Predictable/Reactive/Decoupled/etc.).

Model fine-tuning outcomes: 3-tier trust/buffer/hybrid by correlation; monthly shrinkage validation for GROUPS (60% sensitivity); calibrate ABN targets by LOB (not uniform 5%); lost-call revenue for RES/CASINO to justify FTE ROI; monitor GEM AHT variability (±1.6 min).

FTE modeling: reviewed office hours + call-volume proportion data for Royal.

Next: decision-maker meeting; backtesting to fix initial model; finalize FTE recs per LOB.

**NA Celebrity datasets:** Ongoing data collection w/ Darren (office hours, shrinkage, baseline assumptions).

Dave

Contact Center

Will be meeting with Alper & Kiana next week to discuss upcoming priorities to create  datasets for “next best action” and customer “snapshots” (including a summary of recent interactions/sentiment with us) for Cresta Agent-Assist initiatives. This will involve transforming C360 data and mutli-modal guest feedback using GenAI. These foundational datasets will likely fuel the “memories” module of other guest-facing AI agent initiatives, such as CoCaptain.

Erick

**Project Axiom**

*AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.*

**Meta Data Extraction**

**Guest Logs Categorization** *(David M.)*: Created a mapping table matching old and new guest logs categories with certainty scores. Estimated only ~2% of 22 million records require LLM processing, significantly reducing costs. Implemented a dictionary-based optimization and embedding-based approach that replaces the earlier multi-step hybrid process. Sharing Excel with Erick for review before beginning the open-ended topic extraction pipeline.

**Unified Framework for Topic Extraction** *(David M.)*: Proposed unifying the division, bullet points, and open-ended topic extraction pipelines into a single package for broader team adoption. Meeting with Erick scheduled to review framework design and plan production transition.

**Reporting**

**GSO Safety Email** *(**Danusio** G.)*: Sent draft GSO safety report to Melissa (Global Security) for review. This report focuses primarily on onboard safety issues, with shore excursions as a secondary section. Melissa requested the report be separated into distinct onboard and Shorex sections. Iterating on classification pipeline and email template.

**ShoreX**** Safety Report** *(**Danusio** G.)*: Applied "prompt repeat" technique and two-step classification method to the shore excursion safety report for Eduardo's team. QA completed and results sent to Eduardo for expert validation — initial results appeared satisfactory. This workstream is nearing completion.

**Axiom Power BI Dashboard** *(**Danusio** G.)*: Implemented dynamic date filtering for reporting topics and cruise objects on the official Axiom Power BI dashboard (covering all 3 brands: Royal, Celebrity, Silversea). QA on data sources identified several outdated summary tables (families, nationalities, cabin class, loyalty tier, generations) stuck at November 2025 data. Agreed to filter dashboard data to the last three months initially. Danusio now recreating outdated tables and configuring an automated update job, pending business approval on segment-level granularity.

**Port Email** *(Rodrigo B.)*: Presented port email report to stakeholders including Matt — received positive feedback. First version of the AI report due by 3/27 for the upcoming JV meeting. Coordinating with Alex Moss on data table resolution.

**RBC ****PowerBI**** Dashboard** *(Rodrigo B.)*: Dashboard unblocked and now in progress with two-tab layout (email summary + query-based data). Added total passengers and total service metrics. Target calculation methodology clarified — using only respondents per question. Deployed and awaiting Gang's feedback and mockup for any required changes.

**RBC Recap Email** *(Rodrigo B.)*: Adjusted reporting logic to lag by one week to ensure complete survey response capture. Adding summary table of topic counts with prior-week context. Published to DS Premium workspace and sent to Jose. Awaiting Gang's feedback on format preferences (may prefer simpler topic-summary-only approach). Weekly Monday scheduling pending Gang's confirmation.

**Abandoned Cart Dashboard** *(Rodrigo B.)*: Dashboard unblocked and actively in progress. Demonstrated updated version with topic filtering. Mapped Excel fields from Pia to API fields, resolving discrepancies. Handling temporary/missing survey questions across time periods. Preparing pipeline for weekly Monday updates.

**Casino Smoking ****PowerBI**** Dashboard** *(Rodrigo B.)*: New request from Gang for a Power BI dashboard analyzing casino smoking-related feedback trends over several years to inform decisions about smoking area ratios. Requirements being gathered.

**Modeling**

**Drivers Model Experimentation** *(Osvaldo V.)*: Applied Penalty-Reward Contrast Analysis (PRCA) and Kano model to classify features as basic, performance, or excitement factors using SHAP values. Presented feature categorization results across meta products (Europe, Asia, Caribbean) showing context-specific differences in critical vs. nice-to-have features. Erick proposed training models per meta product to assess whether specialization yields more accurate feature importances.

**Genie Teams Bot Deployment** *(Osvaldo V.)*: Created an agent in Copilot Studio, integrated Genie workspace from Databricks, and demonstrated query processing in the test environment. Agent supports multi-tool integration (Google Search, drivers model, data plotting). **Blocker:** Copilot Studio publishing permissions required before Teams integration can proceed — Erick working to obtain access.

**Genie for PCP** *(Osvaldo V.)*: New request from Gang to deploy a Genie solution for PCP data. Scope and requirements to be defined after the current Genie Teams bot deployment is completed.

**Target Setting Visualizations** *(**Danusio** G.)*: Ramping up on the target setting model and Power BI dashboard. Tasked with conducting exploratory analysis to demonstrate model reliability, identify prediction-vs-actual discrepancies, and prepare evidence for business stakeholders covering both NPS and return rate targets.

**AI Pivot *****(Qualtrics Topic Extraction)***

*Self-labeling framework for automatic topic discovery from survey data.*

**Abandoned Cart Dashboard** *(Rodrigo B.)*: Updated dashboard with topic filtering and descriptions in a separate table. Incorporated Pia's additional KPI requirements and mockup. Field mapping between Excel and API completed. Creating pipeline to run every Monday for updates.

Erick & Cristian

**MyCruise**** Recommender**

*Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app.*

**Recommendations Engine *****(Cristian V.)***

**AB Test Rerun**: Completed rerun with revised logic and expanded user scope — results remained unchanged with no observed lift after normalization. Revenue attribution analysis showed no spillover or cannibalization effects; revenue increase was driven by volume, not price. Identified that Taylor's approach excludes zero-revenue events as a key source of divergence. Next steps: share latest numbers with Rosie and Taylor and align on standardized testing methodology.

**Calendar Staging Date**: Added additional staging sailings to API per QA team request.

**Network Graph API Deployment**: Follow-up task to deploy the updated network graph approach for all product categories in the API, building on the graph-based exploration from previous weeks.

**MyCruise**** Prod Job ****GraphQL**** Failure**: Root cause identified and resolved.

Doug

**RCG | PRE Consolidation Data Input | FEB**

Team established. Initial meeting held on 2/23/26 to review upcoming goals and work needed.
!image-20260224-144136.png|width=590,alt="image-20260224-144136.png"!

Celebrity: Existing PRE has no Oracle dependencies. Work to port ADF pipeline to Databricks scheduled.

RCI: Initial goal is to move as much data input processing as possible to Databricks. First item is to move the “common input” pipeline. Pipeline has the following Oracle dependencies which can be replaced by Unity Catalog equivalents. Code updates to use replacement tables scheduled.

|SCHEMA|TABLE|FUNCTION|UNITY CATALOG|REPLACE BY|LAST UPDATED|NOTES|
|REVSTRAT|RCI_SHIP_CLASS|Map ship code to ship class|NO|prd_silver.edw_core.dim_ship|2/24/2026|RCI only. Table has errors and omissions|
|MKRPUSER|ICSLMD_COMPANION|Active sailings|YES|prd_silver.icslmd_companion.icslmd_companion|2/24/2026|Common|
|MKRP_RMD|META_PRODUCTS|Meta product codes|YES|prd_silver.mkrp_rmd.meta_products|2/24/2026|Common|
|MKRP_RMD|DYN_TRACK_MKT|Active sailings with dynamic track|YES|prd_silver.mkrp_rmd_secure.dyn_track_mkt|2/24/2026|Common|
|REVSTRAT|FUTURE_FIT_TRACK|Active sailings with future FIT track|YES|prd_silver.revstrat.future_fit_track|2/24/2026|RCI only.|

Sweep through Celebrity PRE pipelines in ADF. Confirmed that all can be phased out, ADLS storage reclaimed. Only one single pipeline requires xfer to Databricks.

Prioritized initial set of ADF pipelines to sunset and ADLS storage that can be cleaned. Work towards this to start first week of March 2026.

*Status*: This ticket is complete as of *02/26/2026*
*Deliverables*:
• Team assembled for review and validation of milestone 2 of PRE consolidation.
• ADF resources to be sunset identified.
• Discussion of integrating a data-quality framework for potential tri-branded quality metrics.
• Considered integration effects on the common price upload process in upcoming upgrades.

**Doug **

**CEL Revenue Management**

**CEL | PERKS | 4 Weeks + Supplemental DS Analyses + February Readout | FEB**

Preliminary final analysis and recommendations presented by Nikita to Irena this morning. Full end of test scheduled for 2/24/26 following collection of data for extended test metas.
Data correction required for business-supplied pricing gaps due to overlaps caused by end-of-test price changes populating into test. Mitigation successful.

End of extension reached on 2/24/26.
The following sailings had status changes during the test and will be removed from final analysis to prevent bias due to no bookings received.
!image-20260224-144723.png|width=397,alt="image-20260224-144723.png"!
BY/2-14-27 — Status Red, no bookings
BY/1-9-28 — Closed
BY/3-5-28 — Insufficient booking volume
EQ/7-15-27 — Converted to charter
SM/1-17-27 — Converted to charter
SM/1-24-27 — Converted to charter
Above status changes resulted in removing clusters 18, 19, 48, 136, 245 from final reporting.

Test summary shared with Nikita. She will be consolidating for final presentation in March when back from vacation.

*Status*: This ticket is complete as of *02/26/2026*
*Deliverables*:
• Test closed out as of 2/23/26.
• Supporting metrics discussed with team; recommend retesting several far-window groups for better sample selection.
• For indeterminant groups, recommend trying larger gaps in the next test due to ineffectiveness of smaller price differentials.
• Results support minor upcharge increases with no reduction in booking volume.
*Delays*: None.
*Potential future issue*: Final presentation TBD in March 2026.

Lamis

**CEL ****Revenue Management ****| Track Optimization FEB**

Move from MILP to DP to overcome computational challenges of original framework faced while scaling

Comments:Instead of running an MILP model - reformulate the problem as Dynamic Program where calling a non-linear isotonic function is not an issue. The DP problem is formatted as follows:
States: (wts, current remaining cabins (available to book))
Actions: bkgs to target every time step (between lb and ub)
Transition from current state to next state: next_cumulative = current_cumulative + bkgs
Instant Reward: q * price (from fitted function – current booked position)

Terminal condition: at t=0, cumulative = K (Capacity)
Solve a bottom-up DP solved backward in time (starting at t=0) - fills a Value table by enumerating every possible (i, r) state and every possible feasible bkgs decision (q) at each state.
This approach is fast, can call a non-linear isotonic regression function (unlike linear optimization) - Solved a sample of Europe sailings – was able to generate optimal tracks for ~ 650 sailing-cat class in 45 mins without parallelization (~4 secs/sailing-cc) ~ 9x faster than MILP. It is building on the price optimization logic (can be viewed as an extension to price optimization) - will be easy and very explainable in the future if the business decided to merge the two projects and only use track optimization to generate weekly price recommendations.

**CEL | Track Optimization FEB**

Validations

Comments:

After completing an initial run of EUROPE sailings for CEL - the following sources of infeasibility are identified and handled:This version of track optimization is based on the demand curves. These curves are generated by predicting bookings at multiple price points simulated around a current base price point. There are some instances where the lb and ub on the projected weekly bookings (weekly search space for track optimization) are not located on the curve. This is treated by performing left/right extrapolation to ensure that prices can be computed for the entire search space. There are cases where the calculated remaining capacity at the start of track optimization - based on current WTS and booked position - is (negative). The reason is because the capacity allocated to FIT bkgs is not fixed and could change every week - The optimization considers a fixed capacity - So, this is to be discussed with the business tomorrow. For the time being, for those cases, I am assuming remaining capacity is 0 and track generation is not needed. This generally occurs very close in.There are cases where the cum of weekly allowed lower bounds on bkgs (or upper bounds) is less than (or greater than) the overall remaining capacity → resulting in infeasible problem. In this case - if the optimization decided to go with the lowest feasible bkgs it will not fill the capacity at the sailing week (or if deciding the max allowable weekly bookings is still not meeting the capacity) - These are handled by relaxing the bounds up to a certain limit. Otherwise, problem skipped - solution infeasible.

Revise Formulation to use demand curves rather than directly calling the demand model object and perform .predict() operations

Original MILP Optimization Approach –

At each bookings scenario (between lb and ub) each WTS run the inverse of the elasticity model to predict the price -> store these values in a nested-dictionary (look-up table)

In the MILP optimization, search for the optimal, rev-maximizing combination of weekly-bookings  to target based on price values in that look-up table across all WTS. Decision variable: binary -=1 if a certain weekly bkgs level is decided, 0 otherwise.

This MILP approach is computationally very expensive - For example for 1 sailing/cat class – solving for 60 WTS with an avg of 10 different booking scenarios and booked positions each WTS -> calling model.predict() 6000 times to generate the nested dictionary – even before running the optimization.

It takes an avg of 30-40 secs to generate the look-up table – and solve optimization for one sailing. This is very impractical when scaling the optimization to run on the entire fleet.

As motivated by Price Optimization Logic - In order to scale the track optimization I adopted the following concepts in this updated logic:

Separate the demand curve Piecewise-linearization for all WTS and all different booked positions (discretized every 10%: 0.1, 0.2, 0.3 …. 1.0) This process will store the price and bookings grids for each WTS at all possible booked pos scenarios in a UC table.

In the Track optimization Framework - call the relevant p-q grids from UC - fit an isotonic regression function where q is monotonically decreasing as d increases - store these functions to be used later in the optimization

CEL | Pricing Optimization | Data Adjustments + Price Optimization Readiness (Post PRE4.0 Review)

Generate data-driven factors to convert bookings into pax to replace the existing average-based global factor of 2.08

This EDA is completed and findings presented to stakeholders yesterday. Deliverables include slide decks explaining the process and findings of the EDA + look-up table stored on the UC to be used to convert from pax to bkgs based on certain level of segregation.The table is shared with the stakeholders and is being validated.Minor edits have been requested: use different seasonality features and test the ship_class/code in the segregation.

Jesse

SSC PRE

This week, I continued to updated SSC PRE. The purpose of these updates is to ensure that PRE adaptable for our upper-level suite AB test, requested by SSC leadership.

**PRE Upper-level suites **– Upgraded PRE to enable different pricing algorithms can operate for the same voyage. Farecode and category code-specific pricing recommendation algorithms are now compatible with PRE. As with pervious advancements, these algorithms (and the codes they are assigned to) can be specified in the master excel file, found on sharepoint. This upgrade is an important step in our upcoming ab test for upper level suites because it enables the data team to quickly create any price recommendation algorithm agreed upon by stakeholders and run it for specific voyage category codes without interfering with ongoing PRE recommendations. Additionally, these recommendations can bypass the manual pause file if the business prefers.

**Restoring cabin category priority table  ** - PRE unexpectedly failed its reservation system validation check this week due to duplicate records. Upon investigation, these duplicates were caused by a change in the pre cabin priority table. I worked with Data Engineering to revert this table back to its original format. PRE now passes the Reservation System validation.

SSC Revenue Management: Universal AB Testing

**Wheel is ready **- Evan has completed his work on the UAB Framework installation wheel. Version one of the universal ab testing framework is complete.

Michelle

**CEL**** Revenue Management**** | ****Gty****-Lead 2.0 Updates FEB**

**Business Feedback**

Applied updated curvature method:

o  Identifies genuinely flat tops in the revenue curve, meaning situations where several gap values produce nearly the same revenue.
o  Uses the shape of the curve (curvature), not just the slope, which is more reliable and less sensitive to noise or small modeling wiggles.
o  Looks at the revenue behavior in a tight window around the peak, focusing on the locally meaningful area where decisions matter.

Business impact

o  More accurate detection of when the model is “indifferent” about the exact gap
o  The curvature method tells us when the model thinks multiple gap choices produce essentially the same revenue
o  Reduces overreacting to tiny, meaningless differences in predicted revenue.
o  Fewer arbitrary shifts in recommended gaps and more consistent outputs week over week.

Positive feedback from the business on the approach here.

Michelle

**CEL**** Revenue management**** | GTY Lead 3.0 FEB**

**Model Exploration**

Created presentation for business team and met on 2/24/26 to share updates.

EBM plots are noisy, goal is to create stronger signals by applying monotonicity to force the shape function for the price features. Issue is that in our problem, a price gap does not affect all classes equally. Meaning that if the gty-lead gap increases, this would lower probability of physical bookings but increase probability of gty bookings. Although in an EBM there is one shape per feature per class, monotonicity is applied to an entire feature across all classes simultaneously

o  If a feature has a monotone-decreasing constraint, then every class’s shape curve for that feature must be decreasing.

In category-gapping, we want

o  laf_lower_gap_perc ↑ → probability of class 1 (lower) ↓
o  But NOT:
§  class 2 ↓
§  class 3 ↓

Currently testing One-vs-Rest (OvR) EBMs

o  trains one binary EBM for each class
o  monotonicity works because it allows class specific constraints
o  LAF lower gap increases → Lower decreases
o  LAF upper gap increases → Upper decreases
o  LAF premium gap increases → Premium decreases

Aagam

**PCP pricing Automation**** | CRF Automation FEB**

**Base Data and Historical Price**

**Comments:**
After gathering all the data from the necessary tables to calculate the sailing level stats, along with the number of ships of RIC and CEL on RBC for that RBC call date, I further calculated rbc_call_date_%_to_capacity, this will tell us how occupied RBC is on that day and help us formulate the business rules better.

Additionally, I also gathered the base prices for each of the Alc, Non-Alc, and Deluxe pass, as I will be using them to automate the business rules.

**RCI | OBR | CRF Automation FEB**

**Config and Base Tables**

**Comments:**
This week, I focused on creating the base tables that capture sailings, RBC Passes, Bundles, and Cabanas for all upcoming sailings. I designed the codebase to be dynamic, allowing easy extension to include RBC products for Europe and Australia in the future. Additionally, I made sure that key variables, such as product codes used to identify the products, can be manually configured by the OBR team, thereby improving automation and flexibility. Additionally I am adding the currency dynamic to the process to allow easier integration of any future RBCs.

The initial phase involved setting up automated extraction of base tables for the following components:

Base price of the pass

Base price of the deluxe package

Base price of cabanas

Ship-level statistics, including:

Sailings relevant to the process

Calculating ship counts during the RBC call date

Counting bundles, passes, cabanas, and daybeds for each sailing

In the second phase, I integrated these datasets to compute the {{rbc_call_date_percent_to_capacity}}.

Lekha

CEL Rev Management **| ****SPIKE :**** Promotions Analysis**

**Understand and validate replacement value(promo) vs base price data**

*Status*: This ticket is complete as of *2/26/2026*

*Deliverables*:

SQL query to identify and calculate replacement value shares and total bookings for promotional bookings marked “EXCITING” with brand ‘C’ filtering booking offered date from 2026-01-01 to be more relevant with recent trends of booking pattern

aggregated booking counts by {{meta_product_code}} and {{ship_class}} to calculate replacement and non-replacement booking volumes.

I have seen a pretty good share of replacement values bookings for most of the meta product code ,ship class combinations same with the meta_product_code , cat class combination

Aggregate replacement booking percentages at sailing level grouped by product code and ship class.

Calculate counts and percentages of sailings exceeding a replacement bookings threshold (default 70%)

Since a majority of bookings are replacement value bookings, analyze these bookings further to identify which sailings are on replacement value promotions.

Extract the pre-recommendations (PRE Recs) related to these booking if these bookings are missing por beating the track based on that we have to tweak the replacement prices

Export these adjusted PRE Recs into a separate file to provide business teams with recommendations for appropriate replacement values

.*Potential future issue*: None

**CEL | Elasticity Model Health Check Dashboard**

**Get Feedback ****From**** CEL Team**

Presented the backtesting performance dashboard this week, which initially focused on directional error analysis with respect to price changes and other model features,

Received stakeholder feedback requesting a stronger focus on summary performance metrics that can be reviewed week over week and across all relevant aggregation levels in the model.

Based on this feedback, began refactoring the dashboard to prioritize high-level summary metrics for backtesting, enabling a quick assessment of overall model performance before deeper diagnostics.

Currently focusing on postcard-style summary tiles that show total predicted demand versus total actual demand for a selected week, providing a concise snapshot at any chosen aggregation.

Enhancing downstream visualizations to display week-over-week performance trends, allowing users to track how predictions and actuals evolve over time.

Ignacio

PCP Pricing Automation

**Copy over final optimization changes for bundles & check results with business team**
• The updates done to the optimization routine for one of the beverage packages was copied over to the other notebooks related to beverage package optimizations. These updates to the optimization and schema saved for the delta tables were updated. The optimization results were then shared with Jorge from the OBR team.
integrate shipboard bookings as an additional WTS bin for the elasticity model & optimization routine
• Updates were required on the feature store, the model training, and optimization notebooks in order to incorporate shipboard bookings & shipboard price recommendations into the PRE for beverage. Note that this was only done for the revenue maximizing version of the optimization since the FCST target revenue used in the optimization routine constrained to FCSTs only accounts for forecasted PCP revenue (excluding shipboard revenue). One of the main changes involved adding an additional WTS bin to the aggregated binned feature store. This bin accounts for all bookings at DTS (days-to-sail) of 0 and lower. In other words, it includes only bookings done on the day of the ship departure or later. After this, the new bin also had to be added into the set of bins to train the elasticity model on in the model training notebook. Afterwards, the revenue maximizing optimizations were also modified to also recommend prices for this last bin. This had to involve setting different minimum & maximum price bounds for the recommendations, given that more affordable prices are typically expected pre-cruise and higher prices onboard the ship.**
Recurring meetings with DE for PCP2 projects on Mass Promo Table & Targeted Offers**
• A recurring set of meetings were had for 2 projects: (1) Mass promotion table dataset, meant to be useful for DS and for direct use by business team as well; (2) Targeted offers, a meeting also including the business team and digital as well
**Plots comparing FCST constrained & revenue maximizing price recommendations vs ratio of achieved revenue to target revenue (segmented per WTS bin)**
• A set of plots were created to compare the 2 different optimized recommended output prices for the Beverage PRE: the FCST-constrained & revenue maximizing optimizations. Plots were done comparing the output prices of each to a ratio of current achieved revenue divided by target revenue. These plots show that the FCST-constrained version aligns very well with the business expectations and logic for how to change prices, with the prices aligning very well with what the more tedious business rules logic would have suggested. This affirms that the FCST-constrained version serves as a great automation tool for price recommendations. The revenue maximizing version, however, has room for improvement and wants to be enhanced in the near future to serve a bigger purpose of more complex price recommendations that vary more from those that are similar to the business rules outputs.

R**ecurring meetings w/ RCI & CEL teams on project planning**
• Another meeting was had with Jorge regarding beverage PRE, providing updates and planned future steps on enhancements to the PRE, mainly focused on shipboard price recs, moving average residual model (elasticity drift), improved model (likely nonlinear), and improved version of the revenue maximizing version of the PRE (the FCST/track constrained version performs very well and helps automate the price recommendations; it is more or less consistent with the current business team’s strategy). In addition, another meeting was had with RCI regarding waterpark and next steps, mainly pushing for an A/B test given the limited data on bookings so far that show an inelastic relationship but hinting at a potential elastic relationship at lower price points. This leads to an unknown as to whether a more elastic relationship at lower price points may lead to higher yield than an inelastic relationship at higher price points.

Glen-Erik

PCP Pricing Automation

Testing of real offers: offers flow to hybris but those bookings don't exist to login and see them in the app or web.

Single offer testing:

Manual upload and visibility validated in web and app, mapping of text fields to exact locations on the end user display.

End to End testing to be finished today.

Mass testing of offers in dev/test:

Received booking details, pending E2E testing next week.

New simplified kafka topic in progress in parallel since the current structure maps and remaps columns sometimes to other column names and has many unused fields making the process confusing, prone to mistakes, and more complicated than necessary.

Glen-Erik

PROPEL:

*Dynamic Test/Control Measurements: (Javier)*

Rolled back measurements to legacy process with test/control at sailing level to debug, not compatible with current dynamic structure.

Completed full analysis of legacy BCG measurements table which requires a full redesign to map offers to future purchases in the same category rather than mapping all purchases (past and present) to the offers that day assuming confounding effects.

The existing **BCG measurement table is conceptually wrong**.

It currently:

Links **all purchases (past and present)** to **offers available on a given day**

Assumes any purchase could be influenced by any offer shown that day

This creates **confounding effects** (false attribution), because:

A spa offer might get credit for a dining purchase

A past purchase might be incorrectly attributed to a future offer

**What needs to change:**

Offers should be linked to **future purchases only**

And **only within the same category** (e.g., dining offers → dining purchases)

Began creating a new/separate measurements table that will map offers only to purchases within it's category and do so for all future purchases to quantify the offer impact at the category level.

*Offer templates readiness:* monitoring pre-offer template code in QA to deploy to prod before extensive offer template testing in QA. *(Glen-Erik)*

*24/7 support:* Service now form is being finalized. Next steps: (1) align and understand notification flow with Carlos Zapata, (2) align with OBR team when they want to be notified of issues, and finally (3) communicate to ships to start using the new form. *(Glen-Erik)*

Eswar

PCP pricing Automation

Support:

Separating out OBR project from feature store repo.

Setup all CI/CD needed to deploy bundles

Align with OBR developers what workflows need to be re-deployed from new repo, and what workflows can remain part of feature store.

Eswar

RCI Revenue Management

Data Validation Framework:

Reviewed existing PRE data validation code to identify its functionality and ways to replace it with Validation framework developed

Helping RCI and CEL in identifying tables which are in UC, but still having copy data activities so that we can remove all unnecessary copy data activities in ADF.

Identifying common tables used across PRE and PRE CEL, and have it more of a common ingestion framework

Ayon

Win-on-Waste

we are trying to make this happen  --- (if u have time - u can tread through the weeds of it)..we are in different stages of testing and development for the entire thing ---

Working on next demand forecast. I keep making the PL more advanced ...with this approach this I think will a b state of art demand regime aware forecasting use case. this is a document I created during my team meeting with Luis and Gourish to architect this

so u will not have any updates in the teams form u share every week for this week...

this is my articheture of demand regime aware forecasting

**Step 1 **

Feature Eng--------should Not have clustering

**Def ****Build_Advanced_features_Pos**   in Feature Utils

In addition to existing features in feature eng

Temporal:

Itereray day #

Month of the year#

Week of the Month

Don’t need day of the week

Is Holiday

3 days around Holiday

Quarter of the year

Is Game Night (Please ask JD which day is the Game Night for Playmaker ) – most likely it shud be Sunday ….Playmaker is only impacted by that No other restaurants are impacted by game night

New Features

Residual Avg features

Monthly baseline avg -  Avg for that Month By Metaprod or Voyage Type (for each model group+meal period ) window by month ---- @Gourish help Luis – to see different voyage types such as charter, interport master or regular are identified by metaproduct code or note? If   not then just use the window partitionBy Voyage Type and metaproduct –

For that u will need to add the voyage Type information/ column from the ETL (before base features)

ResiduL Daily Avg (+ and -) daily – meaning meal_period cnt – Monthly BaseLine Avg for each model group + meal_period string

Note Don’t go for -1 to -31 bcoz while 30 days is in a month but the ship might not sail for 30 days ..

Quarterly Baseline Avg for each ship partition By model group + meal_period

Residual Monthly --  Baseine Monthly – Baseline quarterly

Mov Avg of ResiduL Daily Avg (over last 10 sail days wondow – window (-1,-7) or (-1,-10) which gets better results include the signs **(Note: make sure the future day days must be not Null for the feature)**

**Testing Requirement**

**Test** for Nulls and replace all Nulls/Nans will Mode for temporal features and man for numeric features (Idea open to change )

**Step 2- ****segmentaion**

Clustering  - Kmeans  -  Pandas UDF (in the same format like our train predict function

**For each Model Group_ mel period **

Note :

Only on past data

To be placed in POS Modelling Utils

Def demand_Regimes(pass the df features returned from - **Def ****Build_Advanced_features_Pos**    in this UDF)

Kmeans – Kneed ----(into 3 demand regimes  - Low, High, Nomal)

Features to be used in the Kmeans :

Only Use features -----

Itereray day #

Month of the year#

Week of the Month

Don’t need day of the week

Is Holiday

3 days around Holiday

Is Game Night

Quarter of the year

ResiduL Daily Avg

Residual Monthly

Result of this function will give u a new column **Demand_Regimes** for for each model group +  meal_peiod  separately

**Testing Requirement**

Record cnts after clustering for past day (current date _1 till start of of history) == record cnts after **Def ****Build_Advanced_features_Pos**   (current date _1 till start of of history)

# of model_group_meapeiod after clustering == # of of model_group_meapeiod  after **Def Build_Advanced_features_Pos**

**checkpoint**

**Step3 - ****classifcation**

**Note**

Future demand classification

Can be any model – LGBM classifier (preferred, or xgboost )

Place in POS Modelling utils

**Use features for training **

Itereray day #

Month of the year#

Week of the Month

Don’t need day of the week

Is Holiday

3 days around Holiday

Is Game Night

Quarter of the year

ResiduL Daily Avg

Residual Monthly

Mov avgs (features from **Build_Advanced_features_****Pos**  )

Target variable - **Demand Regimes **(the outcome of kmeans)

Note:

The classification will be in Pandas UDF –

For each model_group+ meal_period

No Nans Nulls

Outcome:

The classification predicts the Demand_Regimes for the future

**Testing Requirement**

Total Record cnts after classification == total record cnts after **Def Build_Advanced_features_Pos**

# of model_group_meapeiod after clustering == # of of model_group_meapeiod  after **Def ****Build_Advanced_features_Pos**

Nulls should be fillna with Mode(Most freq cluster # or regime #)

**checkpoint**

Input of PCA will be exactly as what is today – No change

**Step ****4  -**** Dimensionality Reduction (PCA)**

already in place

On

**Step 5 – Collection all features before Regression Demand prediction**

**Aside  -----****à In Pos Configuration ****Currenrly**** we need the following ****chnages**** -----**

Base_Features = [

'number_of_nights',

'itinerary_day_nbr',

'DemPCA',

'TimePCA',

'ItVPCA',

'MostCommonPaxCnt',

'Avg_nights_MAVG',

'Complex_MovAvg',

'Interaction_MAVG_21V14',

'Interaction_MAVG_20V10SV',

'meal_period_naive',

'MinMealPeriodCnt',

'MaxMealPeriodCnt',

'Avg_nights_last_it_cnt',

‘Mov Avg of ResiduL Daily’

‘Demand Regim of past and future’

]

Base_Features_ShapGroup = {

'ItVPCA_Feature_Shap': 'Itineray_descriptor',

'number_of_nights_Feature_Shap': 'Itineray_descriptor',

'itinerary_day_nbr_Feature_Shap': 'Itineray_descriptor',

'MostCommonPaxCnt_Feature_Shap': 'Itineray_descriptor',

'DemPCA_Feature_Shap': 'demography',

'TimePCA_Feature_Shap': 'time',

'Avg_nights_MAVG_Feature_Shap': 'Moving_Average',

'Complex_MovAvg_Feature_Shap': 'Moving_Average',

'Interaction_MAVG_21V14_Feature_Shap':  'Moving_Average',

'Interaction_MAVG_20V10SV_Feature_Shap': 'Moving_Average',

'meal_period_naive_Feature_Shap':  'Moving_Average',

'MinMealPeriodCnt_Feature_Shap': 'distribution_historic_consumption',

'MaxMealPeriodCnt_Feature_Shap': 'distribution_historic_consumption',

'Avg_nights_last_it_cnt_Feature_Shap': 'distribution_historic_consumption',

Update this accordingly

}

Base_Features_suffixed = [col + '_Feature' for col in Base_Features]

model_grouping_cols = ['ModelGroup']

model_naming_cols = ['pipeline_flag','ModelGroup']

base_constant_features = ['shipCode','pax_count','Adults','Kids','voyage_departure_date','PROFIT_CENTER_NAME','profitCenterId', 'MENU_ITEM_ID','cv','order_process_date', 'train_end_date','predict_end_date', 'meal_period_cnt', 'Target_meal_period_cnt','Multiplicative_factor','ModelTune','ModelApproach'] Update this accordingly

Base_Model_Columns = model_naming_cols + base_constant_features + Base_Features_suffixed

Data Collection

Join reduced feature df (outcome of PCA ) with the necessary columns such Demand regime from classification –joining on ModelGroup+meal+period + result_dt/ order_prcess_dt

All features from POS Configuration that are more checkponted result of **Def ****Build_Advanced_features_Pos**    + **checkpointed result of PCA + classification**

**Step 6** Existing Regression demand prediction with added columns  - No change required But test it out)
