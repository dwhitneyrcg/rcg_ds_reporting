Mirielle

CONTACT CENTER
Workforce Planning - North America (Royal)
FTE Forecasting Trade-Off Analysis: Conducted validation session with business leaders on headcount/FTE model direction. Key decisions reached: the model will reflect true operational need (not budget-constrained), budget adjustments will occur after the model reports true requirements, and the model will support scenario-based trade-offs (e.g., showing the FTE curve for 10% vs. 5% abandonment targets). Cross-LOB interactions will be accounted for, as some LOBs appear adequately staffed only because other teams absorb their demand.
Workforce Modeling Strategy: Identified critical distinction between independent LOBs (Loyalty, STAR) with clean ACD metrics and shared-agent LOBs (CE_SALES, CE_SERVICE, Reservations) where cross-support distorts staffing metrics, forecast accuracy, shrinkage modeling, AHT interpretation, and abandonment behavior. Independent LOBs will serve as baseline calibration targets.
Model Tuning and KPI Strategy: Testing Service Level (SL) as the primary modeling target, replacing Abandonment Rate. SL more directly reflects customer experience, is more stable, is the industry standard, and aligns better with scheduling and capacity planning.
Next Steps: Transitioning to SL-based staffing targets, introducing capacity capping by LOB, and calibrating the model using independent LOBs where data is clean.

Mirielle

CONTACT CENTER
Workforce Planning - International and Casino (All Brands)
Defining the approach for handling call volume adjustments in the International and Casino application. Key design question being resolved: at which level(s) should the app allow adjustments -- Market, Brand, LOB, or a combination. Working session scheduled next week with Nico and team to develop the strategy and ensure alignment with operational reality and stakeholder expectations.

Carlos
E-COMMERCE
Data Source Validation: Implemented a notebook providing visibility into all source tables used for feature building. The code checks for recent DML operations on each table (falling back to DDL if none found) and aggregates metadata into a centralized table (bp_source_updates). Created a data validation PR and integrated the validation task as the first step in the training pipeline.
Streamlit Application: Developed a feature in the Streamlit app that displays all data sources, their recent operations, and highlights tables needing investigation. PR submitted.
Booking Propensity Model Comparison: Met with Pablo to discuss merging web-based booking propensity scores with predictive analytics propensity model scores. Blocked on access permissions -- Pablo cannot access the predictive analytics scores table and data export is restricted. Issue escalated to Michelle for resolution.
Maintenance: Added custom saving location option to ADF pipeline for oracle table copies. Replaced pandas-on-Spark with native PySpark for code reliability. Added logic to set training period (latest 3 years by default). Modified code to avoid replication of source silver tables across environments (dev, qa, prd). Continuing manual testing of latest major refactoring.
New Journey Score Model: Met with stakeholders and defined goals, requirements, expected results, and plan. Decision made to move from classification model to unsupervised clustering, to be used alongside the existing booking propensity model. Researching candidate clustering models prioritizing meaningful and explainable results. Source data gathering and EDA underway.
Stakeholder Support: Created threshold history table per model as requested by Anisa. Participated in meeting where stakeholder presented marketing models catalog, use cases, and future steps to senior leadership.

Cihan
PCP Pricing Automation
Alaska ShoreEx: Updated the dashboard by changing source tables for select plots and refactoring SQL queries. Handed over the Alaska Dashboard and ShoreEx clustering code to Anand (new hire), including code reviews and knowledge transfer sessions.
OBR Waterpark PRE: Handed over the project to Anand with a full project review to ensure smooth transition.

Caleb
CUSTOMER LIFETIME VALUE / DEMAND MODEL
Completed: Implemented visualizations to assess accuracy of key model dependent variable, including rank prediction plots, residual distributions (scatter, box, histogram, heatmap), and SHAP interactive feature plots with feature density. Shared feature importance analysis on preliminary model iterations. Reorganized data loading, cleaning, and transforming pipeline to condense logic, enforce reproducibility, and boost efficiency, building in structural validations from competitor earnings reports (10Ks).

Continued: Iterating through model tuning, optimizing MAPE with moderate regularization and corporate-level supervision. Assessing and interpolating gaps in competitor pricing and deployment data. Beginning thorough cleaning of competitor pricing data (bots pricing).

Camila & Ben
SUPPLY CHAIN
Demand Model Adjustments and Guardrails Refactor: Continued work and validation on the new orchestrator notebook, adding final model metrics post-guardrails. Parameterized the implementation of select guardrails, enabling easy review of model performance with and without guardrails applied.
Finance Tool Refactor: Ongoing refactoring of the finance tool, adding 4 monolith production notebooks to the finance orchestrator. The orchestrator now provides improved readability and compute efficiency, breaking 5 notebooks into 12 smaller notebooks. Final data accuracy validation post-refactor is in process with testing notebooks confirming row counts and data distributions match 100%.
Cococay Reporting Fix: Fixed IBP data extracts for COCOCAY reporting by using AVG instead of SUM for voyage demand pivots (both container-load-date and sailing-date pivots), since COCOCAY is shared across multiple ships.
Cabin and Guest Table Updates: Updated cabin/guest table logic for accurate ship matching.
Pipeline Configuration Updates: Added SSC_CONSUMPTION_YOY_APD to the daily pipeline tier 3 schedule. Changed daily pipeline config to inherit from base config instead of a separate hardcoded tier list. Changed daily pipeline to use the determine_schedule_to_run function instead of hardcoded schedule.
SSC Consumption YOY APD Enhancements: Added voyage-level and ship-level YOY summary tables for SSC consumption. Refined guest snapshot aggregation with itinerary-based day type availability. Computed APD metrics (guest count, PCD, max capacity) per voyage item. Uppercased all output columns for downstream compatibility. Updated port type matching via movement/itinerary date alignment.
SSC Cost Movement V4: Added COST_MOVEMENT_V4 using MAX_CAPACITY instead of PCD for quantity normalization, propagated through all 10 pipeline steps. V4 provides more stable cost movement for ships with volatile PCD/guest counts.
Order Creation Improvements: Fixed ARRAY column to string conversion issue in backup production order baseline notebook for CSV export. Updated order creation notebooks for compatibility with latest Spark runtime and job compute settings. Extracted volatility report section from RCI CEL order creation to run independently. Extracted MIN/MAX PAR logic into its own notebook for weekly volatility comparison. Added RCI CEL MIN AND MAX PAR as a weekly-run step in the master notebook.
Silversea Crew Count Model (Completed): Built end-to-end Crew Count Forecast ETL pipeline joining voyage data with uniform crew reports, implementing temporal matching using window functions to find closest crew count reports before and after each sailing date, calculating crew-to-cabin ratios and voyage gaps. Built ship code mapping ETL to reconcile uniform and voyage ship codes across 14 Silversea vessels, implementing time-based logic for code transitions and deduplication rules. Created cabin capacity aggregation notebook with deduplication, array-based capacity calculations, and dot product validation. Implemented stored procedure for comparing PySpark tables against SQL reference tables using row counts and hash sums. Generated mapping with 6,750 voyage records linking uniform crew snapshots to sailing dates. Created EDA notebook analyzing uniform demand patterns including report frequency, employee count changes, gap distributions, and ship code validation.
Silversea Crew Count Model (Ongoing): Continuing crew count reconciliation after July 2025 due to dramatic increases suggesting potential logic or ETL errors. Reviewing integration of 90-day contract length logic into employee crew count calculations. Filtering usable data for EDA given sparsity across certain ships with inconsistent reporting periods and missing cabin features.

Erick

**Project Axiom**

*AI framework for transforming unstructured guest feedback into actionable insights across Medallia, Guest Logs, Qualtrics, and call center data.*

**Meta Data Extraction**

**Open-Ended Topic Extraction Pipeline** *(David M.)*: Created a new GitHub repo dedicated to metadata extraction, moving away from Azure DevOps. Pipeline uses the bullet points table as input to extract topics without constraining to predefined categories. Designing modular repo structure with base class inheritance for automated pipeline creation; Databricks GitHub app integration resolved.

**Guest Logs Categorization** *(David M.)*: Switched to a BGE-based embedding model for candidate selection, increasing the candidate pool from 10 to 20 and enhancing the final LLM process with higher reasoning effort for more robust results. Results shared with Hotel Ops stakeholders showing much improved classifications. This task is a pre-requisite to step to clean up Guest Logs data.

**Reporting**

**GSO Safety Email** *(**Danusio** G.)*: Global Security requested adjustments completed - pending stakeholder feedback.

**ShoreX**** Safety Report** *(**Danusio** G.)*: Celebrity Destination Experience to begin receiving the safety report weekly.

**Axiom Power BI Dashboard** *(**Danusio** G.)*: Dashboard deployed to DS Premium workspace with daily refresh trigger configured at 7:30 AM UTC. At least one tab (ship/sale date/meta product selection) is now available to business teams ahead of final table decisions.

**Port Email** *(Rodrigo B.)*: First version of the AI report due by 3/27 for the upcoming meeting between Naftali and stakeholders. Coordinating with Alex Moss on data discrepancy resolution.

**RBC Recap Email** *(Rodrigo B.)*: Monday email scheduling confirmed. Erick to confirm email format with Gang before finalizing.

**Abandoned Cart Dashboard** *(Rodrigo B.)*: First version published in premium workspace. Demographics page nearly finished. Adding charts by week and topic (counts and proportions). Load factor query validated against Oracle version. Investigating Power BI filter alternatives for Pia's request.

**Casino Smoking ****PowerBI**** Dashboard** *(Rodrigo B.)*: Gang wants multi-year casino feedback trend analysis to inform decisions about smoking area ratios. Awaiting detailed requirements.

**Target Calculation Methodology for Hotel Ops email** *(Rodrigo B.)*: Identified the correct weighted average method — excludes questions with fewer than 50 responses. Most metric discrepancies between Medallia and Excel resolved; testing additional weeks to confirm correctness.

**Scrape Cruise Critic Comments** *(Erick A.)*: Completed scraping all comments from Cruise Critic for Royal Caribbean, Celebrity Cruises, and MSC Cruises (competitor) and shared data with Consumer Insights across RCI and CEL.

**Modeling**

**SHAP GPU Pooling on Lambda** *(Erick A.)*: Parallelized SHAP explainability computation across all 8 GPUs on the Lambda server. The system now computes 500K rows across 300+ features in ~13 seconds, powering real-time explainability in the Axiom webapp.

**Drivers Model Experimentation** *(Osvaldo V.)*: Calculated APD spend features and tested a two-model residual approach (demographics predict LTR, then feedback features explain residuals) to isolate actionable satisfaction drivers. Compared LTR vs rebooking feature importance — low correlation found, contrary to prior assumptions. New regression model trained with improved explainability. Data leakage check on "max sailings" feature cleared. Unexpected finding: "Overall Family Experience" appeared as top predictor for Celebrity brand — investigating demographic split.

**Genie Teams Bot Deployment** *(Osvaldo V.)*: Copilot Studio integration dropped after discovering ~$50K/year cost for 1,000 users. Decision made to build the solution externally instead of through Teams. Support ticket for workspace also declined — needs resubmission.

**Medallia Keyword Correlation Tool** *(Osvaldo V.)*: Feature correlation calculations added to Streamlit app. Erick advised focusing on a Databricks notebook version for now — migrate to Lambda only if use case is proven. Working notebook version ready for Erick's review.

**Target Setting Validation Notebook** *(Erick A.)*: Implemented a validation notebook comparing Naive targets (which match historical sailings to future sailings using business rules) against model predictions and actuals. EDA quantifies differences between the two approaches to support the case for model-based target setting.

Erick

**Contact Center: ****Lead Scoring**

*Predictive lead scoring using contact center (CTI) data.*

**Fix CTI Large Lead Drop Failure** *(Erick A.)*: Fixed a bug where very large drops of new leads caused the pipeline to fail. Solution: split large file drops into multiple smaller files.

Cristian & Erick

**MyCruise**** Recommender**

*Personalized product recommendations (shore excursions, dining, spa) for the Royal Caribbean app.*

**Recommendations Engine *****(Cristian V.)***

**Graph-Based Item Recommender**: Model overview presented — graph-based approach identifies product relationships even with sparse data, resolving the Royal Beach Club recommendation gap. Segmented by meta product code with improved precision and recall in backtesting. Precomputed recommendations keep API fast.

**AB Test Rerun**: Replication challenges persist — even after matching other team's methodology, significant differences remain. User overlap varies by experiment (attitude card ~100%, PDP ~75%, eyebrows ~45%). Decision: future AB tests will simply replicate the same data transformation logic through DS AB testing code. Test will focus on replicating results based on DS testing methodology (while holding data transformations constant).

Ayon

**WOW Update – March 6**

**1. New Feature Engineering Framework for Demand****-Regime****-Aware Forecasting**

This week, we completed end-to-end development of the new **pre****-feature****-engineering** and **feature****-engineering** modules that support the demand regime–aware forecasting architecture. These modules now generate **three distinct feature streams**, each powering a different model family:

**Outlier Detection Models** – dedicated features for robust anomaly identification

**Clustering & Classification Models (Demand Regime Identification)** – features tailored for regime discovery

**Regression Models for Final Forecasting** – refined predictive features for downstream forecasting accuracy

All of this has been fully implemented and integrated into the **POS Orchestrator Pipeline**.

**2. Upcoming Work (Next Week)**

Replicate and adapt the same feature-engineering architecture for the **Guard Rail Orchestrator Pipeline**.

**3. Final Step Ahead**

Build a new **Rules Engine** leveraging outputs from *both* model families, using **optimization / minimization logic** to drive final, regime-aware forecast decisions.

**4. Additional Deliverable Completed**

The team also built the new **POS PLU Mismatch Reports Pipeline** in Databricks and integrated it with **Power BI** for automated daily distribution to stakeholders.

Development is complete

Testing and validation remain outstanding

Doug

**CEL**** Rev ****Mgmt**** | PERKS | Additional DS Analyses + March Readout | MAR**

For each grouping of meta product, booking window, sailing season and ship class, provide:

Comparative statistics between control and test groups of:
Bookings
Trade up rate
Apportioned per-diem perks revenue
APDs

Probabilistic plots showing which test group “wins” with respect to trade up rates

Weekly overall trade-up plots showing trends across the entire test period for both standard (8-weeks) and extended (12-weeks) groups. [^Celebrity All In Test Final 04Mar2026.xlsx]

**Met with Nikita, Irena, and Anastasia to review recommended actions, considerations for future testing, resolve discrepancies.**

**Future testing considerations:**

Test larger gaps in perks upcharge.

Pretest soft constraint on existing prices and better price drift control on test sailings.

Longer test periods for far booking window to avert challenges collecting sample volume.

Additional validation of Rev. Planning vacation flags which were found to be inaccurate for sailings in far booking window.

**Nikita finalizing estimates for revenue lift for 2026, 2027, 2028 if recommended actions implemented.**

Lamis

**RCI ****Rev ****Mgmt**** ****| Track Optimization: Validation – Scaling the optimization to run on the entire fleet**

Ran the optimization on the entire CEL future sailings (not only Europe) – identifying sources of infeasibilities and treating these. Some of the identified issues include:

The remaining capacity to fill is located outside of the cumulative lower and upper bounds on weekly bookings. For example: cum lower bound at sailing week = 100 and capacity to fill is 80. So, even if the optimal track targets the minimum (realistic) volume every week – we still cannot fill the capacity. Same for Upper bounds. In this case I am relaxing these bounds. After relaxing there are still very few cases where this constraint is still being violated – this may be a result of some input data issues.

There are cases where remaining capacity to fill is negative – no tracks are generated for those

Worked on reporting and visualizing the results including optimal tracks and heat maps for the future values of each state – and how the optimal track is decided based on these values (examples are shown here)
!image-20260305-182427.png|width=615,alt="image-20260305-182427.png"

Prepared a presentation to the SHs to discuss the change in the modeling approach (from MILP to Dynamic Programming) and presented the results.

Currently working on comparing the SPI-tracks, the business tracks against the optimal tracks. Preparing a presentation and report for the SHs for next week.

**Lekha**

**CEL ****Rev ****Mgmt**** ****| ****SPIKE :**** Promotions Analysis**

**Compute**** booking splits promo vs base price**

[^Promotion analysis Deck.pptx]

*Status*: This ticket is complete as of *3/4/2026*

*Deliverables*:

*Identified all sailings using Replacement Value (RV)* by merging VCAP identifiers with promotion data, ensuring we could clearly isolate bookings influenced by Exciting Deals.

*Measured RV vs. Non**-RV passenger volumes* across meta-product, ship-class, and cat-class levels to understand how much of our demand is driven by RV.

*Grouped bookings into G1/G2/G3 performance categories* to reveal which sailings beat track without RV, which beat track because of RV, and which miss track even when RV is present.

*Analyzed the PAX distribution across these groups* to show how heavily our overall performance depends on Replacement Value in different segments.

*Evaluated weekly RV booking patterns* and confirmed that RV meaningfully shifts performance outcomes, proving it is a major driver of whether we beat or miss track.

*Established the groundwork for PRE rule development* by mapping how RV contributes to performance and identifying where PRE should raise, lower, or remove RV based on G1/G2/G3 logic.

*Outlined how new PRE rules will prevent over**-discounting*, ensuring Exciting Deals are applied intentionally rather than by default.

*Presented the analysis to Anastasia*, who agreed the RV share insights (pax + sailings) made sense and requested next steps: compare RV vs non-RV price paid and build a capacity-based view, since track becomes unreliable close-in due to retention behavior.

*Potential future issue*: None

Michelle

**
****CEL Rev ****Mgmt**** | GTY Lead 2.0 | Improvements**

In addition to the curvature method where code is detecting flat revenue plots and lowering gaps where revenue impact is not significant, I also added a check for identifying recommendations that are not “confident”.

Using the residuals already created in the DART process, I find the recommendations that have been missing the true target and lower those gaps. This is only done when tradeup has been overpredicted, is tradeups has been underpredicted hen we would not want to lower prices unnecessarily.

Product manager for Australia also requested to incorporate AUD prices and differentiate markets in the AUST/NZL/SOPAC meta.
Updated feature store tables to include AUD pricing.
Input tables, model, optimization, and DART processes were updated to create separate price recommendations for AUD vs USD markets in Australia sailings.

Anastasia and her team have approved of changes. Awaiting final approval from product managers before pushing to production.

Ignacio

PCP Pricing Automation

- **Improve ****Beverage PRE ****optimization results with ratios for bundle demand & price to be segmented by WTS bins****: **After meeting with Jorge to analyze the results from the RBC bundle adjustments, we noticed some outputs that were questionable and needed improvement. I noticed that it was likely due to how the estimates of how the ratio (for both price & demand) of bundle bookings compare to solo bookings had the option to be calculated specific to the sailing being optimized on if the data existed, which would therefore then lead to a biased output. This is especially problematic since it was noticed that there was a trend of higher bundle bookings further out in the WTS booking window vs higher solo bookings closer in. Therefore, the calculated ratios for both price & demand ratios were adjusted to be only based on exponentially weighted moving average (EWMA) with larger weight on more recent data. This would also be done segmented by the WTS bins in order to capture the different trends found across the WTS bins. These changes were implemented and then set to be shared with Jorge for final review before pushing to production.

- **Recurring meetings with Business Team (PREs, CRF Automation, ****etc****) & DE Team (Mass Promo Table & Targeted Offers)****: **Meetings this week were had with the data engineering team & business team regarding recurring feedback and updates for the mass promo table (including things like flags for restricted vs non-restricted promos) & targeted offers. Additional meetings were had with the business side (RCI & CEL) to discuss and plan the CEL Beverage PRE development along with enhancements to the RCI Beverage PRE regarding RBC bundles & setting up an A/B test sometime in the near future. Additionally, other short meetings were had with Anaand to familiarize him more with the OBR domain knowledge and data as he gets familiar in the new role.

- **Create moving average residual model layered onto the Beverage elasticity model – MAR****:** Some initial work was done for setting up a moving average (EWMA) residual model to add onto the current elasticity model (DART). The intention of this was to correct for drifts in elasticity values (i.e. drifts on consumer behaviors and price sensitivity) that are not present in the data used to train the elasticity model. This would help dynamically correct for any changes in consumer behavior and price sensitivity for beverage purchases. This would be expected to have a robust positive effect on the predicted demand for different price points. Initial work was done to create a rough draft of how this EWMA residual correction model would work, with the code added into the model training pipeline. However, due to changing priorities (i.e. more focus to be spent on CEL Beverage PRE in the upcoming weeks, with the current changes to RCI Beverage PRE good enough for now), these enhancements to the model are being sidelined in priority. This can be revisited after (a) the development of CEL Beverage PRE & (b) the initial A/B test set up for the current RCI Beverage PRE.

Aagam

**PCP Pricing Automation**

I’ve completed the calculation of the final price points for the RBC Alc Pass, RBC Non-Alc Pass, and RBC DX Pass in accordance with the business rules. Since the process relies on the previous week’s discount percentage, and there is currently no table capturing that historical data, I’m working with the team to design and implement a table that will store weekly discounts for future processing.

I also identified that sailings beginning in January 2027 were missing base prices for these passes. This impacted the workflow because the sailing date range for this CRF spans from today through the next 365 days. I’ve been coordinating with the business team to ensure these base prices are added so the process can run as expected.
I also added additional checks based on the discussions with business to set guardrails for the CRF process, these involve - setting caps on the price changes. cap on the gap between the Alc and the Non Alc pass. DX + RBC Bundle Price: Confirms the bundle price is calculated correctly.

Implied RBC Price: Ensures the guest-perceived RBC price stays above ~$30 and below the standalone Alcohol Pass price.

Implied vs. Alcohol Pass: Verifies the implied RBC price is always lower than the standalone Alcohol Pass price.

Bundle Discount vs. Pass Discount: Checks that the bundle discount is ideally higher than the pass discount, with limited exceptions.

Alcohol & Non-Alcohol Discount Changes: Reviews discount movements between sales periods for expected variation.

DX vs. Bundle: Ensures the bundle discount is always higher than the Deluxe discount.

**Next Steps and Blockers**:

**Null Handling**

**2027 Sailings:** Some 2027 rows still return nulls; need business support to update the source table so automation can run cleanly.

**90+ Window Metas:** LONG CAR, CARIBNE, REPOS, and BERMUDA show nulls; proposing to classify them by sail-night similarity (short vs. 7N) pending business confirmation.

**Last Week’s Discount**

This value is still manually sourced. Once a table is created to store weekly discounts, I can fully automate the dependency; for the first run, I can manually read it from SharePoint.

**RCI | OBR | Business Rules based Functions**

Completed the creation of the business rules notebook that would help calculating the new discount % for RBC Alc, Non Alc, and DX Passes for RBC CRF Automation. These rules are developed after discussions with the business teams.

Eswar

RCI Revenue RMA

Separated the OBR project from the Feature Store into a dedicated OBR repository.

Configured all necessary CI/CD deployment pipelines for the new repository.

Implemented Databricks Asset Bundles (DABs) to deploy OBR workflows; successfully transitioned from and disabled the legacy workflows.

Refactored the PRE RCI output validation code, replacing it with the standardized Data Validation framework.

Managed CI/CD monitoring, code quality checks, and Peer Request (PR) reviews.

Provided ongoing MLOps support for the team.

Glen-Erik

PCP Pricing Automation: PCP - 1 to 1 offer pilot

Created and refactored mass upload pipeline with QA checks enabling testing in stage.

End to End testing in Stage: Tested PLP, PDP for both Celebrity and Royal.

PLP – Royal & Celebrity tested End to End. Royal on iOS and Celebrity on Android.​

PDP – Royal & Celebrity test End to End. Royal on iOS and Celebrity on Android.​

**Pending items:**​

**Critical:**​

**Custom splash screen image. **Digital will add this capability so we can test it. Currently not supported. Also need the image to test. (est 3/10)​

**Finalize the copy from marketing: **English copy and if any other device languages will be supported.​

Test what happens if we change the language in the phone​

Retest why discount isn’t making it to the user. And says 50.0 OFF instead of 50% OFF. ​

**Minor:**​

**Categories for products mismatch **between hybris and Unity Catalog. Checking if it is a prod vs staging discrepancy. Ex: The same product code showsas shorex in prd but beverage in staging. *Can set these manually for now but adds chances for mistakes when rolling out more offers.*​

**Next Steps after critical items above are complete:**​

Send full load of 1600 guests to stage (est. 3/10)​

Test in Prod with fake bookings (est. 3/11)​

Send out real offer to real guests in prod (est. week of 3/16)​

Harden solution for reusability and error minimization beyond this pilot beverage offer. (est. 3/13)​

Glen-Erik

Propel (CEL)

Onboarding Santiago (Glen-Erik)

Support: (Glen-Erik)

Fixed port issue causing missed runs and consolidated port scheduling code to avoid mistakes when updating ports.

Investigating why EQ is currently running one day behind schedule with the same settings as other ships. (Santiago). In the meantime we are running this process manually for the rest of the sailing (Glen-Erik).

Javier

Propel (CEL)

Dynamic Test/Control Measurements: (Javier)

Developed a proposal to redesign the measurement framework, aligning it with the new category-level test/control assignment.

Established primary KPIs and guardrail metrics to measure targeted performance, detect cannibalization, and evaluate incremental revenue.

Designed the statistical evaluation methodology, including uplift estimation, Welch t-tests, weighted regression, and multiple testing correction.

Proposed optimization of discount exposure duration to improve incremental profit and reduce cannibalization risk.

Prepared executive documentation and presentation materials explaining the redesigned measurement framework.

Javier

RCI Rev Mgmt: ACR (Automated Code Review):

Improved repository compliance validation logic, updating PR checks, workflow permissions, and failure notifications.

Developed a Databricks SQL pipeline to analyze repository rule violations across commits.

Implemented commit snapshot and ranking logic to track the latest commit state within reporting checkpoints.

Fixed reporting issues so commits with zero violations are included and validated results using the TRACK-dbricks projects.

Evan

RCI Rev Mgmt: SPI

Excited about the enthusiasm and response from RCI and progress on SPI. Seems as if from speaking with Kevin there may be a focus to get a quick win (or evaluate if feasible) on cat gap as a simple POC. Cannot  promise anything and don't want to diminish the efforts elsewise on the project / opinion of it.

But my objectives will be to get what Nick was asking for completed by today or Monday at the latest (I doubt I will need a week to complete a segmentation / portal); to which I am beyond surprised he shifted opinion on!

Then to push on all efforts for a POC towards this as a quick win; not by any means a final project or stepping on anything Michelle is doing; which explainable boosting will be significantly better.

**Mert**

**MIAP**

Created Microsoft AI Foundry, Azure AI Search, Azure Data Lake, Key Vault, Databricks, API Container App, and Web App Container App Azure resources for Newbuild. Set up the Databricks Catalog.

Started developing the Agent Serving FastAPI Container App for Newbuild.

Met with Charlie Sebelle and identified data sources required from Oracle Fusion for the IBP project, focusing on CapEx, OpEx spending, and purchase orders. Worked with Charlie to identify relevant AMOS views on the AWS server.

Met with the Deployment Team and initiated collaboration on the digitalization of the Prime tool. This tool was originally developed by Gang ~10 years ago and serves as a simulator for deployment cost and revenue. The team plans to digitize it using Python. We agreed to build this as a reusable Python package designed for mathematical optimization. The Deployment Team will complete the initial development; once finished, we will perform code review, refinements, and productionization.

Met with the Newbuild team to discuss Agent architecture. Mala raised concerns that her team would like to see marketing material and still has questions about why we cannot work with Credentia, as well as doubts about whether the internal AI team can deliver. We agreed to develop marketing material for the Newbuild team so they can share progress with leadership and build confidence.

Met with GMO leaders from Safety, Asset, Energy, Strategy-PMO, and Navigation to discuss the AI money map. Safety and Energy use cases are fully identified, with nearly **$150M/year** in potential value. Savings opportunities for Asset, Strategy-PMO, and Navigation are still to be identified.

Continued tag mapping for Radiance, Serenade, Millennium, Jewel HVAC area and finished mapping all HVAC tags for these MIAP Phase IV ships.

**Ram**

**MIAP**

Completed integration of OFB data into the MIAP REST API and made the data available through MIAP endpoints.

Added the required permissions for Alfa Laval to consume data via the MIAP API.

Migrated Sea Events pipelines to the DE workspace and removed the Bronze Sea Events schema from the Marine catalog.

Fixed and redeployed the monitoring job that sends missing-data email alerts; the workflow is now running successfully in Production.

Worked on generating Parquet files for Alarm and Events data, as requested.

Created a PostgreSQL stored procedure to automatically remove shipboard stream data older than 24 hours.

**Next Week**

After receiving PostgreSQL DB access, validate stored procedure behavior and make any required adjustments.

Begin generating vendor-wise cost metrics for data consumed through the MIAP API.

Address and resolve MIAP ETL workflow failures.

**Reza**

**MIAP**

Focused on diagnosing issues in the SFOC (Specific Fuel Oil Consumption) models, which appear to be the root cause of fuel-consumption prediction inaccuracies in the digital twin.

Verified that digital twin accuracy remains strong through total electrical power prediction, isolating the degradation to the SFOC layer.

Investigated multiple potential sources of SFOC error, including:

Piecewise linearization logic used in the digital twin versus actual underlying model behavior.

Baseline SFOC model accuracy by comparing predicted values against actual vessel data (potential outlier-removal issues).

SFOC model performance across different voyage phases to identify operating regimes contributing to prediction drift.

Conducted comparative analyses to identify patterns, inconsistencies, or structural issues explaining reduced predictive accuracy.

**Brendan**

**MIAP**

Identified six propulsion-related errors in the Digital Twin library based on recent tests; currently working on remediation.

**Arya**

**MIAP**

Fixed bugs in the RCG boosting model.

Added RA to OFB, FW, and machinery.

Worked on non-optimized power plant prediction.

Integrated the power plant prediction model into the digital voyage workflow.

**Mahshad**

**MIAP**

Added dynamic chiller model features.

Reviewed each ship’s base model features and verified model configurations.

Performed MA tuning on the HVAC model.

Worked on benefit tracking for SM and ML related to implementing variable chilled water and evaluating its impact.

Collaborated with JW and EQ on tag mapping to enable further analysis for benefit tracking.

**Will**

**MIAP**

Fixed bugs in FACTS voyage model integration.

Fixed at port FACTS model bug.

Added missing columns for incinerator and OFB to facts results.

Created data check notebook to check power plant outlier removal quality.
