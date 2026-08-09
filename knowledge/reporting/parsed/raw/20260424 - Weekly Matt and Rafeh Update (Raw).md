**Mirielle T.**

**Contact Center**

**Call Volume Forecasting/ Date:** April 23, 2026

**1. Project: International & Casino Call Volume Forecasting**

**Work Completed**

Orchestrated all forecasting functions into a single end-to-end pipeline.

Produced the **first full forecast run** across all international and casino markets.

Completed **backtesting**** for all markets**.

Identified **under****-performing markets** with high forecast error (MAPE).

**Why It Matters**

This milestone confirms that the forecasting pipeline is **operational at scale**.
Running end-to-end forecasts and backtests across all markets allows us to:

Validate model behavior in real conditions

Identify which markets require additional tuning

Build confidence before integrating forecasts into workforce-planning decisions

**Next Steps**

Fine-tune markets with **MAPE > 20%**
*(e.g., France, Spain, Brazil, Italy)*

**2. Project: North America Call Volume Forecasting — Celebrity**

**Work Completed**

**Feature Engineering**

Built and updated the feature-engineering framework by combining:

North America (Royal) features

International & Casino features

**Modeling**

Used the existing call-forecasting orchestration process to generate a **first forecast run for all 14 LOBs**.

**Fine****-Tuning Activities**

Identified lower-performing LOB forecasts and applied targeted adjustments, including:

Enabling or disabling **trend features**
*(trend features are generally more useful for stable call**-volume patterns)*

Adjusting **year****-over****-year growth rates** to reflect recent trends, especially in declining volumes

Enabling or disabling **outlier removal**

Enabling or disabling **call****-volume smoothing**

Investigating **abnormal date ranges** impacting forecast accuracy

**Why It Matters**

This work ensures the Celebrity forecasts are:

Aligned with recent business trends

Adapted to LOB-specific behavior

Ready to support staffing and planning decisions with higher confidence

**Next Steps**

Continue fine-tuning remaining LOBs to improve forecast accuracy.

**3. Project: North America Call Volume Forecasting — Royal**

**Request **From Augusto: split the **Reservation LOB** into: Reservation Sales and Reservation Services

**Work Completed**

Reviewing and updating data queries to support the new LOB split.

Running call-volume forecasts separately for **RES_SALES** and **RES_SERVICE**.

**Why It Matters**

Separating sales and service improves forecast granularity and allows:

More accurate demand modeling

Better alignment with operational staffing needs

Clearer insights for workforce planning and decision-making

**Overall Next Steps**

Complete call-volume forecasting for **Celebrity** and **International** markets/LOBs.

Update the Workforce Planning app with all finalized call-volume forecasts.

Begin building the **dependency datasets** for the **Advanced App Simulation (Royal)**.

**Carlos A.**

**E-commerce ****Customer Targeting**

Added more features to journey score model in order to classify web visits

Review Jakala documentation for Silversea models, and share impressions and requirements for inhouse migration with Silversea team.

Bao

E-Commerce Targeting

identified key columns needed to categorize clickstream activity by session. Not to mention, found key indicators that allows us to see device/browser changes within session.

developed HMM tests with composite features that capture clickstream interactions that roll forward.

clickstream adjusted checkpoint table has been materialized and now contains raw clickstream reduced down to 60 columns with granular data requested by carlos. Cardinality and null count has been adjusted for.

David expressed concerns regarding the legality of targeted consumers. Began developing audit notebook to validate and determine if protected consumer classes are not critical for consumer propensity segmentation

researched new claude code features available to us in copilot and isolated agentic worktrees

Camila

Supply Chain IBP:
Supply Name Consumption Ratio Enhancement

Predicts how much of each supply item a ship will consume on a given voyage, expressed as a ratio to apply to the voyage level of total consumption and total prediction.

The model uses the last 8 comparable voyages for each product/ship combination, weighting recent sailings more heavily (6x/3x/1x for Food & Beverage, 2x/1.5x/1x for other categories) so predictions track current consumption trends.

A 2% floor was added to all ratios, preventing the system from predicting zero consumption for items that have historically been ordered, which reduces missed restocking events.

On the live consumption * ratio level (adjusted actual consumption), the model achieves 72.2% accuracy across all product/ship/voyage combinations.

Finance Tool Consolidated: currently debugging Last Month Voyage Demand, Voyage Demand, and Actuals Voyage Demand

Ben

Supply Chain IBP:

Supply Chain: Working on debugging Last Month Voyage Demand, Voyage Demand, and Actuals Voyage Demand from consolidated table

Delivered analysis to Evan on how Supply Chain Models were built, features considered, process for feature selection with cross-validation across different seasons, features selected and feature importance in models

Camila, Ben, & Nicolas

Supply Chain:

**Project: IBP | Automated Spend Report & Consumption Fix**

[DOE-1565] IBP | Automated Spend Report and Consumption Fix - Jira

**Completed:**

**New report variants**: Implemented the two additional report types requested by Lauren and manually tested outputs against previously generated reporting.

**Naming convention finalization**: Finalized naming convention changes, merged the final PR, and notified Lauren that folders/files were ready.

**Closure**: Moved the story to Done based on no further feedback expected.

**Ongoing:**

**Stakeholder review monitoring**: Continuing to monitor for any follow-up from Lauren post-release.

**Project: IBP | Spend Report Data Quality**

[DOE-1582] IBP | Spend Report Data Quality - Jira

**Completed:**

**Issue escalation**: Raised the Transfer Pair issue to Yan for review.

**Ongoing:**

**Decision pending**: Awaiting Yan’s feedback on the email to determine the best course of action.

**Project: IBP | MOT Metrics Enhancements (MOT/PCD Ratio)**

[DOE-1650] IBP | MOT/PCD Ratio for MOT Comparison - Jira

**Completed:**

**QA validation + PR readiness**: Tested changes in QA, opened a draft PR, and marked ready for Yan’s review/validation.

**Stability fix after overwrite**: Made additional PR changes after data went missing due to a downstream overwrite, then sent the PR for review.

**Ratio logic consistency check**: Validated the fallback logic behind BASELINE_MOT_PCD_RATIO, confirmed negligible variance vs. a “consistent fallback” alternative, and proceeded with the baseline ratio metric.

**Stakeholder validation**: Confirmed Yan’s review looked good, and latest pipeline successful -> Moved to Done

**Project: IBP | SSC Uniforms Model — Ratio Feature Corrections**

[DOE-1644] IBP | Review Aggregate Calculations for Gender/Generation Ratios - Jira

**Completed:**

**Problem framing (data leakage / staleness gap)**: Identified that the Fidelio staleness check only evaluates “last report → today” and doesn’t address historical missing reporting in Uniforms; proposed weekly forward-filling to prevent the model learning from inconsistent feature availability.

**Uniform demographics interpretation**: Documented how prd_silver.client.supply_chain_onboard_uniform_demand represents demographics distributions and how demand must be derived via consumption; proposed a clearer report-date → sailing association window to match cadence and contract assumptions.

**Planned sequential fix set**: Defined an ordered implementation plan (spine creation → fill missing report dates via rolling averages → broaden report-date-to-voyage association window and redistribute).

**Implementation progress**: Reviewed code generation for the planned changes, pushed updates, and prepared for another model run.

**Ongoing:**

**Model performance check**: Planning/continuing a “third run” to evaluate how these corrections affect model performance.

**Project: IBP | SSC Uniforms Model — Combinatorial Gender/Generation Ratios**

[DOE-1645] IBP | Introduce Combinatorial Gender/Generation Ratios for Uniforms - Jira

**Completed:**

**Feature rollout**: Added the combinatorial ratio features across relevant notebooks to support improved signal capture in the model.

**Pre-fill integration**: Merged the aggregation-based gap-filling work and applied the pre-filling to combinatorial ratios to prepare for the next training run.

**Ongoing:**

**Impact validation**: Continuing to evaluate the impact of these features on model performance during the next training run, after higher-priority ratio fixes land.

**Project: IBP | Beverage Product Name Label Extraction (AI POC)**

[DOE-1669] IBP | Remove labels from beverage product names - Jira

**Completed:**

**Requirements clarification**: Captured open questions on whether beverage-specific descriptive extractions are needed, dataset scope, and whether the approach should be wine-first vs. all beverages.

**Recording synthesis + approach alignment**: Summarized the recording into a concrete extraction goal (label extraction from product names), identified uncertainty around the source dataset, and floated using a small/fast AI model for keyword extraction at the data-table level with acceptable error tolerance.

**AI access validation**: Confirmed access to Azure OpenAI via AsyncAzureOpenAI using Databricks vault secrets and validated the API call end-to-end.

**Initial brand extraction POC**: Built an initial POC for brand extraction on beverages and persisted run metadata + results tables; first pass achieved **89%** extraction coverage (5558/6267).

**Ongoing:**

**Stakeholder follow-up + next-phase requirements**: Awaiting feedback after presenting the POC to Yan; updating approach per guidance (use Crunchtime table, rename brand → category_label, leverage active products from procurement_item_master, and plan phase-2 rollups by brand/category).

**Project: IBP | Cost Optimization (Databricks Compute)**

[DOE-1625] IBP | Convert pipeline cluster to job compute to reduce costs - Jira

**Completed:**

**Job compute conversion**: Created the job compute configuration, validated the job ran successfully, and proceeded to close out the story.

**Ongoing:**

*(No ongoing items captured in your comments this week.)*

**Project: IBP | PRD GOLD Decimal Data-Type Change Testing Coordination**

[DOE-1334] IBP | PRD GOLD table paths to test numerical values change - Jira

**Completed:**

**Wrap-up / confirmation**: Confirmed the team is good to proceed and left the story as Done.

**Ongoing:**

*(No ongoing items captured in your comments this week.)*

Caleb S.

CLV:

**In Progress**

Revising the CLV ETL pipeline in preparation for a pull request to formalize data requirements and handoff with Kiana's team

Refining join logic across loyalty, Medallia, dim ship, cobrand, ship costs, and cabin costs tables — resolving duplicate rows through targeted column selection, coalesce strategies, and appropriate aggregation methods

Consolidating the ETL directory by merging redundant notebooks, deprecating obsolete transformations, and eliminating unnecessary intermediate table writes to streamline the pipeline

Documenting the updated pipeline architecture and branching strategy to ensure reproducibility and facilitate onboarding for downstream contributors

**Completed**

Conducted validation and reconciliation of key metrics within Executive-level PowerPoint deliverables, leveraging outputs from the competitive cruise fleet model to ensure accuracy of reported figures

Carlos A.

**Loyalty**

Kicked off the Simulator Work

Improved sailing-guest simulator to better predict the cabin category guest will travel. (model trained and integrated on the simulator), still pending to test different variations implemented.

Research in how to modify the simulator to pair past guest with sailings that better match they probable sailing nights

Kevin D.

Loyalty

Based on recent conversations with Nancy, Mikael and Lauren, we’ve pulled together a phased plan to revisit and modernize the loyalty simulator, with the goal of ensuring it accurately reflects the current programs and provides a scalable foundation for future scenario analysis and program enhancements.

Below is an overview of the proposed scope, timing, and resourcing approach.

**Phase 1: RCI & CEL Loyalty Simulator Retrofit**
*Scope*: Retrofit the existing loyalty simulator to align with the current RCI/CEL loyalty programs. This includes refreshing to the latest deployment data, reconfiguring the points calculator, and shifting the booking propensity model from the sailing level to the category level to better mirror how the program operates in practice.
*Timeline*: ~3 months
*Resourcing & Cost*: Delivered by Carlos (existing FTE) at ~50% allocation. At a rate of $87/hour, this covers the full Phase 1 effort.

**Phase 2: SSC Loyalty Simulator Build-Out**
*Scope*: Extend the simulator framework to support SSC. Given limited prior exposure to SSC data, this phase will be scoped conservatively, with additional time allocated to data discovery, validation, and model calibration.
*Timeline*: ~3–6 months depending on data complexity
*Resourcing & Cost*: Supported by Carlos at ~25% allocation, plus one additional full-time resource. We recommend keeping this new resource full-time beyond initial delivery to support ongoing loyalty scenario planning. The resource options are:
• Long-term contractor at ~$94/hour, or
• Contract-to-hire at ~$94/hour for the first 3 months, converting to ~$73/hour as a full-time employee.

**Phase 3: Ongoing Analytics & Scenario Analysis**
*Scope*: Establish an ongoing capability to run scenario analysis and stress-test potential loyalty program changes. This includes evaluating proposed enhancements (e.g., Royal One) and assessing impacts to the existing loyalty structure under different assumptions. This phase is intended to be iterative and continuous, adjusting the simulator as program designs evolve and new questions emerge.
*Timeline*: Ongoing
*Resourcing*: Primarily supported by the dedicated resource introduced in Phase 2, with selective involvement from Carlos as needed.

This approach allows us to first align the existing simulator to current programs, then expand coverage to SSC, and finally transition into a sustainable analytics capability that can support future loyalty strategy decisions.

Happy to walk through this in more detail or refine assumptions as needed.

David W.

HR – CAM CAR Planning

Over the course of the week, the team—including Utkarsh Patel, Erick Alfaro, Gabriele Dolfini, John Makan, Zizi, and Angela Smith—collaborated to develop an initial draft of the CAM Capital Authorization Request (CAR). The working sessions focused on clarifying the problem statement, refining scope, and stress-testing financial assumptions. As a result, a draft CAR was created, anchored on demand planning and forecasting as foundational enterprise capabilities, while explicitly debating which downstream applications should be included in the current funding cycle.

A major point of discussion was whether to fund the development of an **in****-house Workforce Scheduling Tool** as part of this CAR. While several participants—including Utkarsh Patel, John Makan, and yourself—advocated for building this capability alongside the CEL Entertainment team’s existing Claude-based planning application, Angela Smith ultimately rejected including this scope in the current CAR. Her concern centered on **write****-off risk**, given the possibility that her organization may instead pursue an **off****-the****-shelf workforce scheduling solution** in the near future. As a result, the workforce scheduling capability has been deferred to a future year, pending clearer buy-vs-build direction.

Following that decision, the CAR scope was intentionally narrowed. The revised proposal now focuses on a **12****-month, $886K Capex investment** to build an enterprise demand planning asset on the organization’s cloud data platform, αPlatform. The CAR is structured around tightly integrated capabilities, notably: (1) Demand Automation and AI Forecasting Models that automate the end-to-end demand planning workflow and produce position-level forecasts for hiring, promotions, and contingency planning with governed refresh cycles; and (2) an Agentic Demand Planning application that provides a single planning and decision-support experience, surfacing staffing risks, explaining drivers through variance and root-cause analysis, enabling scenario exploration, and allowing conversational decision support.

Cost discipline was a recurring theme throughout the discussions. Data Engineering flagged a desire for additional resourcing to properly support the platform and pipeline demands, while Angela Smith emphasized a strong preference to keep total run-rate costs **below $750K per year**, expressing discomfort with proposing an expensive CAR. Platform Engineering also raised the need for incremental **compute investment in the range of $50–$75K**, primarily to support scalable forecasting and agentic workloads. These inputs informed further refinement of scope, sequencing, and capitalization assumptions.

Finally, the decision to shelve the Workforce Scheduling Tool surfaced longer-term implications. The CEL Entertainment team has already built a standalone scheduling and planning application using Claude, managing their own cost centers, which several stakeholders believe represents a viable foundation for an enterprise capability. However, with workforce scheduling excluded from this CAR, that work will **not be capitalized** and will instead need to be supported—if at all—through the **GenAI Center of Excellence (****CoE****)** in the interim. This creates a near-term dependency on CoE capacity and leaves open a strategic question about convergence versus fragmentation of planning tools across CAM in future funding cycles.

Doug B.

RCI Rev Mgmt

**Team | Support + Leadership**

**Status:** This ticket is complete as of **04/23/2026**

**Deliverables:**

Assisted strategy team in troubleshooting several high-priority issues observed in inventory automation processes.

Conducted code and data walk-throughs to educate on system interactions and downstream effects.

Follow-up confirmation that all systems are now behaving as expected.

**Delays:** None
**Potential Future Issues:** None

**Apr 21, 2026 — Logging Discrepancy After Scheduling Fix**

**Issue:**
After correcting process scheduling, the strategy team observed that the logging information extracted from AS400 logs (specifically limit reductions for successfully berthed cabins) did not match the originally requested action.

**Root Cause:**
Code responsible for log generation was inserting a time zone definition into the SQL configuration of the compute. This caused queries to evaluate a different time than what was recorded in the logging data.

**Resolution:**
Removal of the offending line of code resolved the discrepancy.

**Apr 20, 2026 — ****Reberthing**** Automation Conflict**

**Issue:**
After reestablishing reberthing automation, the strategy team observed that bookings were deberthed but failed to reberth during that phase of the process.

**Root Cause:**
When the process was added to the scheduler, a time was selected that conflicted with Celebrity FIT berthing and ADA Accessible berthing. Although RCI’s berthing payload uploaded successfully, another process completed before it was processed, overwriting RCI’s payload and effectively nullifying it.

**Resolution:**

**Short****-term:** Moved the process 15 minutes earlier to avoid the scheduling conflict.

**Long****-term:** Recommendation to combine processes into a single payload to mitigate future risk of process interference.

**Apr 17, 2026 — GTY Limits History Confusion**

**Issue:**
Confusion surrounding GTY limits history data not reflecting automated replenishment actions.

**Explanation:**
Observed spikes in the ICGTLD table were not caused by replenishment. These spikes were a side effect of the reberthing process:

For each booking deberthed back to GTY, AS400 automatically increases limits to account for reverted bookings.

AS400 does not immediately reduce limits when bookings reberth into cabins.

This creates a temporary limit spike that remains until the RM_90 process cleans the ICGTLD table.

**Design Note:**
This behavior is intentional and implemented by IT.

**Operational Handling:**
Limits are adjusted by decreasing the count by the number of successfully berthed cabins, followed by running a replenishment process after IT’s RM_90 completes.

**Apr 16, 2026 — Automation Education & Data Flow Walkthrough**

**Issue:**
Strategy team requested a better understanding of how automation impacts backend systems and data flow.

**Action Taken:**
Met with the strategy team to walk through multiple automation scenarios. Compared actions in code to resulting production data to demonstrate cause-and-effect relationships in system updates.

**CEL | PRE | Pricing Automation - Move main ****PRE processing**** from ADF to Databricks**

Status: This ticket is complete as of 04/22/2026

**Deliverables:**

Pull request 7190 removes triggering of PRE main run from ADF execution.

Pull request 7191 adds new scheduled Databricks job to run PRE main code on Mondays at 3:45pm.

Lamis A.

**RCI ****Revenue Management -**** Track Optimization:**
Both projects are running in parallel for RCI and CEL.
1. Completed and tested some updates to the 2nd stage optimization model for smoothing the DP output based on the  feedback received from the CEL SHs. Applied the same logic to RCL and will present results to the team tomorrow.
2. Since track opt is dependent on the demand prediction model it is important to analyze how sensitive the optimal track is to different levels of prediction errors. So I updated the DP logic to allow for running sensitivity and uncertainty analysis. I ran the sensitivity analysis for random sailings at different levels of errors percentages starting from 10% to 140% 10 iterations each run. Obtained and visualized the optimal track shape from each scenario and will discuss results with RCI SH tomorrow and will run the same analysis on CEL next week
3. In response to the SH request to have a better understanding of the price points    associated with the optimal tracks I visualized the price demand curves 1. The curves based on the raw predictions 2.  the monotonically decreasing in price fitted curves and 3. The bounded curves after constraining the price movement to +/-50%
These bounded curves are also integrated in the DP logic.

Neila

RCI Revenue Mgmt **| Baskets | CARBINTL**

**This is considered a significant enhancement ****on**** last year’s basket approach and will likely ****yield**** both RCI & CEL using the same basket methodology.**

**Work Completed / Acceptance Criteria Validation (Dev & QA)**
Platforms: Celebrity and RCI
Environments: Dev and QA

RCI | Baskets | CARBINTL Fully implemented and validated in Dev and QA for both Celebrity and RCI brands.

**Booking Pace Feature Engineering**
A standardized booking pace matrix was implemented to measure occupancy at fixed days-to-departure windows from 360 through 30 days, ensuring consistent temporal comparison across sailings.

**Sailing Trait Matrix Construction**
Sailing trait matrices were built and validated to include ship class, homeport, itinerary, and other relevant structural attributes for both brands.

**Statistical Basket Assignment**
Decision tree–based segmentation was applied to assign sailings into statistically distinct peer groups. Basket separation was validated through significant booking pace differentiation at three key commercial action windows in both Dev and QA.

**Product Basket Derivation**
Operational product baskets were derived with the constraint that they contain only contiguous sailing weeks, ensuring usability for downstream commercial and pricing workflows.

**Velocity Corridor Computation**
P25, P50, and P75 percentile velocity corridors were computed for booking pace at every days-to-departure bucket and validated across brands and environments.

**Pricing Signal Generation**
Each sailing was classified into one of five pricing action categories based on its relative position within the velocity corridors, with a clear and deterministic recommended action.

**Quarterly Recalibration Process**
A quarterly recalibration framework was established using a rolling historical window to refit models and keep baskets and pace expectations current over time.

**Status**
Complete in Dev and QA

**Delays**
None

**Risks / Follow****-ups**
None identified at this time

Lekha

**CEL | Actual Price Paid | Follow Up EDA For CEL**

**Compare sailings on ****Replacement  vs****  Good SPI ****sailings**

**Status**: This ticket is complete as of **4/20/2026**

**Deliverables**:

When I compared completed non-SPI sailings against the SPI booking zone, I saw many cases where booking pace was much slower than SPI booked position zone for that particular group(meta ,season_flag,cat_class) , even though the price curve was already below the SPI price zone, showing that price had already been reduced and further discounting was not fixing demand.

This clearly indicated that for those sailings, weak demand was not driven by price, and continuing to discount only reduced yield without meaningfully improving booked position.

I then looked at future sailings and found cases where the booked position was higher than the SPI booking zone, while the price was either above the SPI median or within the SPI price range, showing that demand was strong even with higher prices.

In those strong-booking cases, the plots showed that promotions were unnecessary, and in fact pricing could be tightened or made more expensive to optimize yield without hurting demand.

To make decisions consistent, I defined price levels relative to SPI as:

High: price above SPI 50th percentile

**Normal**: price within SPI Q25–Q75 range

**Low**: price below SPI 25th percentile

I also defined **booking gap** as the difference between the current sailing’s booked position and the SPI Q25 level, and combined this with **weeks to sail** to determine whether to stop promos, reduce discounts, lower price further, or take no action depending on how much demand still needs to be filled and how much time is left.

The following actions are recommended after evaluating all applicable scenarios.

**CEL | Feedback ****From**** CEL Team on Actual Price Paid Analysis**

Presented the SPI-based booked position framework to Monica and Eduardo from the Celebrity (CEL) team to gather feedback, positioning best-performing SPI booked-position ranges as the ideal benchmark at a granular group level (meta product, cabin class, peak season flag, and WTS bucket).

Aligned with the CEL team that using Best SPI booked-position ranges by group and weeks-to-sail is appropriate for guiding promotion decisions, as it enables apples-to-apples comparison across sailings and demand conditions.

Based on feedback, agreed not to use Best SPI price ranges directly for promotion decisions, since pricing can be influenced by multiple external factors, and instead focus on average prices derived from splits of excited-deal and non-excited-deal builds at the same group level.

Identified that promotions primarily impact GTY cabin pricing, widening the GTY-to-lead price gap, which can drive higher GTY builds; next steps focus on enhancing the GTY-lead dataset to analyze price gaps and trade up probability after promotions

Ignacio
PCP Pricing Automation

**Recurring Business Meetings & OBR DS Meetings**
• Meeting had with Kevin regarding plan for enhancements to PRE for OBR overall, in order to help scale up and expand price recs to all products.
• Meeting had with OBR/PCP OBR team (Dave, Kevin, Glen-Erik, and Erick) regarding gameplan for enhancements to tracks for OBR & the web app integrated and centralized for a variety of different OBR/PCP uses, including promo automation.
• Meeting had with Garrett from CEL to share additional progress on Beverage EDA based on additional things they wanted to explore and perform analysis on.
• Meetings had with Kevin, Aagam, and Anand for the plan for enhanced OBR tracks for RCI and plans for improving it
**Analyze Track from RCI business team for Beverage - identify areas for improvement**
• Analysis of the Track and the logic behind it made sense overall, but a few areas of improvement were identified. First, the groupings for mappings used for Track would ant to be improved slightly; the current methodology can be too granular at times and lead to some groups with very small sample sizes, leading to biased assumptions due to outliers and small number of samples. This would want to be improved overall. From some of the analysis on performance from STLY for example, some of the groupings calculated on my end matched relatively well with the Track curves from the business team while some other groupings varied significantly. This can be possibly due to the small sample sizes used for the groupings. In addition, the addressable population would want to be made more data-driven; currently, certain types of pax (e.g. loyalty & casino) are assumed to not buy beverage at all, which is a very strong assumption that is not exactly correct. Instead, historical trends in what percentage of those pax purchase beverage should be used instead, making the addressable population more data driven. Lastly, after this, some very useful future improvement could involve making track more dynamic, especially with the use of ticket booking data & how it is doing relative to its track (this can help dynamically adjust track accordingly).
**CEL Beverage EDA – Phase 3**
• Some additional EDA was performed on the Beverage Premium package and its booking behavior, in particular a more granular view on elasticity and the trends of 1st time bookings vs. rebooking the same product later vs. rebooking a different product later (this overall tries to analyze dilution and cancellations within the same elasticity plots). In addition, a trend line was fitted on the scatter plots from before in order to obtain a deeper analysis on the elasticity of the Premium beverage package and how it varies across metas & WTS bins.
**Enhanced Promo Automation**
• The “NAME” column was added into the spreadsheet in order to have it automatically fill in the user name of the person on the business team filling out a specific row (promo) on the Sharepoint sheet. This can help keep track of who does what and perform some internal tracking. A new Unity Catalog table was also created to save exact copies of the Sharepoint sheet used for all batches of promos uploaded through automation; this is meant to help save exact copies of the sheet that can later be copy and pasted for creation of similar promos in the future with slight modifications. Lastly, the addition of the 2 additional SAILING TAG columns (for AND Groups conditions) was then also completed, helping maximize the coverage of promo automation tool for the business team. It is tested in lower environment with digital & DE team in order to validate its functionality before pushing the changes to production. It is then pushed to production.

Anand

PCP Pricing Automation

**1. Waterpark A/B Testing: Sailing Selection Table Finalized (ZH01)** Completed the 79-pair presentation table that will be shared with the business team for Control/Treatment assignment. Replaced synthetic sailing keys with real voyage_sk identifiers from the itinerary system so downstream teams can join directly. Swapped out transactional median prices for **official sailing prices** from v_active_pricing ($84–$169 range), which reflect what the business team actually sets per voyage — not what guests pay after promo discounts. Added **Discount 1/2** columns showing the most recent promo applied per sailing (15%–50% off), and discovered that **63% of pairs carry different promos** between the two sailings, confirming discounting varies by booking window. Added **Waterpark Occupancy %** columns that sum ZH01 passes across **all ships docked at PCC** on each port day against the **1,780-seat capacity** (range 9.6%–70.7% — park never near full). Ran a comprehensive QA audit: **21 checks, 0 bugs**, every column cross-validated against source tables. Table is ready for business review.

**2. Celebrity Analytics & Product Segmentation** Designed and shared **executive dashboard mockups** with Alexander and the Celebrity team covering cluster performance comparisons, revenue normalization, price elasticity, booking & cancellation behavior, digital funnel exposure, purchase frequency decomposition, and product segmentation views. Proposed a **collaborative next-steps model** where data science surfaces the key data points while Celebrity analysts build out and iterate on the views. Separately synced with **Nick Kosmo from Celebrity** to align on the shorex analytics roadmap led by me, including automating the product segmentation pipeline — currently writing the **final stages of the automation scripts**. Also synced with **Doreen from Digital** to share our approach and methodology on product segmentation to ensure cross-team alignment.

**3. Alteryx Migration Kickoff (Beverage, ****ShoreX****, Dining)** Kicked off the Alteryx-to-Databricks migration with **Jorge Hernandez** to standardize tracking for beverage, shorex, and dining product sales. Received **7 SQL migration scripts** (DDL, load staging, style mappings, beverage/PCP track, forecasting) and coordinating the migration path into Databricks.

**Upcoming Next Week:**

·       Send finalized sailing pairs table to the business team for Control/Treatment assignment and sign-off

·       Lead and drive the product segmentation automation pipeline to completion

·       Begin reviewing Alteryx migration scripts for Databricks conversion with Jorge

Evan M

RCI RevMgmt

Demand Model Enhancements

Improved from last iteration (~8%) by testing multiple transformations

Lagged / momentum and trend analysis of prior

Demand

Pricing

Technical indicators for certain features add context of signal movement

Finalized query for internet traffic data on weekly basis

Testing integration

Evaluated transformers for additional temporal features and an automatic SHAP feature reduction in the pipeline

Allows for overloading additional features and automatically reducing to relevant in single model

Showcasing model MVP on Friday (4/24)

SPI Factor Models

Completed initial grouping logic and segmentation

Showcased initial capacity query from new UC table and working on last fixes

Built a quick dashboard showcasing these interactions and capabilities

Ayon G.

WOW Win on Waste updates 4/24:

**Smart Gating for ****Interport**** vs Regular Pipelines:**
Designed and implemented a **gate module** that intelligently controls execution of Interport and Regular pipelines. When both interport and regular sailings exist within the next **7 days**, both pipelines run and write results to Couchbase. If no interport sailings are detected, the interport pipeline is automatically skipped, **avoiding unnecessary ****compute**** usage and cost**.

**Upstream Data Validation & Deduplication:**
Built a **validator module** to detect duplicate sailings incorrectly marked as both interport and regular at the same timestamp (originating from upstream itinerary data). In such cases, the system **drops the ****interport**** record and retains the regular sailing**, preventing downstream forecast duplication and data contamination.

**Interport**** Specialty Pipeline – Integration Complete:**
Completed **end****-to****-end integration testing and bug fixes** for the Interport Specialty pipeline. The solution is now production-ready, with a **planned production deployment on 4/27**, aligned with PI team guidelines (no Friday or weekend deployments).

**Bar Pipeline Stability Improvements:**
Fixed critical issues in the Bar forecasting pipeline impacting **139 bar venues**, restoring stability and forecast completeness across ships.

**Flexible Meal Period Framework (Planned):**
Planning development of a **configuration****-driven flexible meal****-hour module** within the Specialty pipeline. This uses a default-dictionary structure in **job parameters**, enabling operational hour changes (e.g., Chops, Izumi) without code changes.
The capability will be reusable across **all ~40 specialty restaurants fleet****-wide**, significantly improving operational agility. Development and testing are planned for **next week**.

Ayon G, David W., Mert E.

Win-on-Waste Planning

Met with Win-on-Waste team to discuss next phases. Discussions are starting to build a GenerativeAI Genie + Knowledge Base (much like MIAP or NewBuild).

Will also wind-down resourcing for WoW (no longer charging resources except Ayon G. to CAR). We will be letting go one contractor, but trying to move other contractor to IBP.

Mert

New Build

Started work on a report-building tool for the Newbuild App where, based on a user prompt, an agent triggers a live HTML-based report editor that can later be saved as a PDF.
Began creating a Python library for Newbuild AI’s RAG process, enabling easy replication across any file-based database and seamless synchronization between ADLS, Databricks, and Azure AI.

Mert
MIAP
Completed a full refactor of the MIAP App using Next.js, FastAPI, and Tailwind.
Aligned with the Decarb and GMO App teams that the MIAP App can fully replace the embedded MIAP data visualizations and data export tool in the GMO App. All users will now be redirected to the MIAP App.
Met with the GMO Safety team to discuss integrating their Genie Apps into the MIAP App. Also provided a demo to Captain Henrik on how to Vibe Code.

Will
MIAP

Completed development of the FACTS model pipeline and integrated it into the web app.
Fixed a bug related to validating ships without generator information.
Implemented logic to force the use of the FACTS model when ships do not have valid individual generator models.
Continued work on integrating the FACTS flow into the digital twin test pipeline to provide visibility into SSC ships.

Mahshad
MIAP
Worked on the MIAP Analytics pipeline.
Identified energy-saving opportunities of approximately 200 kW each for SY and CS within AHU areas and contacted the ships with detailed findings.
Developed models for individual chillers and created a notebook incorporating feature engineering and a dynamic modeling approach; currently refining the base model.
Enhanced the overall chiller COP model to improve accuracy.

Reza
MIAP

Integrated shore power logic into the fuel forecast pipeline.
Updated the “no optimization” mode to correctly account for shore power usage.
Led a change in the comparison approach to use the legacy model instead of finance predictions, per stakeholder requirements.
Diagnosed propulsion modeling issues and improved accuracy through model adjustments, including outlier removal.
Evaluated power plant SFOC models for accuracy and slope to prevent MILP-PWL optimizer failures.
Performed A/B testing comparing FAT models and Dynamic models on the fuel forecast platform.

Ram
MIAP
Optimized the Databricks workflow connecting to Postgres by introducing table partitioning, improving overall read performance. Further testing is needed with TimescaleDB, as the platform team is currently facing enablement issues.
Worked on MIAP batch processing for PEPLINK.
Collaborated with Wesley to finalize the landing data structure for data ingested from different protocols.

***Cristian V., David M., Osvaldo V., ******Danusio****** G., Rodrigo B., Erick A.***

**MyCruise**** Recommender**

**Infrastructure / Postgres & API *****(Cristian V., Erick A.)***

Platform confirmed the dedicated Postgres prod instance on 2026-04-22.

ForYou API expansion deployed — memory footprint dropped from **95% to 52%**, calendar + recommendations synergies integrated at the ETL layer, and the calendar API was delivered to engineering for testing/staging.

Use-case body parameter added server-side to the recommendations API; awaiting Lance (engineering) to integrate on his side.

**ALS Improvements *****(David M.)***

Completed Bayesian cross-validation optimization — training now uses weighted recall, novelty, and serendipity metrics; random train/test replaced with a temporal split so the model must generalize forward; two problematic input features driving empty recommendations were isolated and disabled.

Built a shared entry-point notebook (with MLflow logging) so Osvaldo and Danusio can swap in their new cluster tables and run the ALS pipeline end-to-end; baseline run underway, with a workshop-style walkthrough planned instead of async code review.

**Strategic direction (with Cristian V.):** team agreed the next improvement lane is re-ranking — integrating Carlos' propensity scores (Drivers Model) at the re-ranking layer — rather than adding base-model complexity.

**Product Clustering *****(Osvaldo V.)***

**GPT-5 Nano breakthrough:** switched from the embeddings + GPT-4.1 mini hybrid to a single one-shot GPT-5 Nano (200k context) batch classification across ~300 batches covering 423 ports. QA disagreement dropped from **~30% to ~11%**. Tradeoff is a more imbalanced distribution (some classes with only 2–3 products), to be merged post-hoc. Classification table going to Cristian for downstream ALS evaluation.

Next steps: expand the ETL beyond Shore Excursions to Beverage & Dining using async parallel LLM calls (sequential is too slow for prod) without flooding the shared GraphQL endpoint; wrap LLM calls with the Instructor library (Pydantic schema + allowed values) so hallucinated classes trigger automatic retries.

**Catalog coverage gap** *(with Erick A.)*: Cristian confirmed GraphQL returns details only for actively-offered products (~7k), not historical. Erick reaching out to Ricky and Kiana for a historical product-details source so clustering can scale to the full catalog.

**Guest Segmentation *****(******Danusio****** G.)***

Phase 2 underway — adding features beyond the single source table used today, with MLflow logging for verifiable improvements.

Erick asked for a business-facing cluster-explainability / persona report (e.g., "Cluster A = older couples, 2 passengers per cabin" vs. "Cluster D = younger families, multiple passengers"), with separate passes for Royal vs. Celebrity given distinct segmentation. Danusio has partial code and will demo.

**Apriori**** Model *****(Rodrigo B.)***

Per-rule quality analysis on the complete-basket approach shows only **2% of rules unused**; average support on used rules is **4x–300x over the minimum threshold**. Cristian confirmed basket-level is the classic (and correct) approach and generalizes across categories.

Next: designing an offline harness to evaluate Apriori + CF combination strategies — full fallback (Apriori only when CF is empty) vs. concatenation (Apriori appended below CF) — on coverage, precision/recall@k, and novelty.

***Erick A., ******Danusio****** G., Rodrigo B***

**Project Axiom — Voice 360**

Across Project Axiom / Voice 360, the team focused on materially improving Medallia email reliability and content quality while closing several known gaps. Safety summaries were hardened by fixing a venue “hallucination” issue (by segmenting venue context per prompt) and resolving an edge case where low-volume safety comments were dropped from summaries; both fixes are complete and under review. Ongoing work is tightening safety guardrails to reduce false positives and persisting all LLM outputs for retrospective QA. On the Port Email stream, missing pre-meeting deliverables were shipped, visual consistency was improved, and promoter/detractor/passive indicators were added at the sub-factor level. A venue-replacement function was also introduced to prevent misattribution of onboard venues to ports, with plans to scale coverage following a working session next week. Remaining work includes resolving minor divergences between topic-level sentiment counts and total responses.

In parallel, Erick is addressing intermittent failures in the fleet-wide Medallia email job by replacing Databricks’ ai_query with a custom async LLM summarization approach and isolating an ETL caching issue, improving both reliability and performance. Additional initiatives include evaluating port-level forum data as a potential supplemental signal (early volume appears low, value to be validated), pausing Beach Club email development until Santorini opens (June 2026), and coordinating shore excursion keyword enhancements for the safety pipeline. Separately, Erick is extending the Target Setting framework beyond satisfaction metrics to include onboard revenue targets for Hotel Operations’ Track system, applying the same multi-model, bias-corrected forecasting approach already used for NPS and rebook targets.

**Email Reports**

**Danusio**** ****G. —**** Medallia Safety Email**

**Venue hallucination bug fixed** *(Completed)*: root cause was passing entire venue information to the prompt without segmentation, causing reliable hallucinations. Refactored to segment venue context per prompt; fix sent to Melissa for review.

**Safety standouts edge case fixed** *(Completed)*: when only ~1% of comments were safety-related, the LLM summary pass was skipping them entirely. Fix feeds standouts into the summary prompt as explicit context.

**Ongoing reliability work:** expanding the guardrail list (discriminator words/phrases) per Eduardo's feedback to reduce false positives (e.g., "broken door"), and persisting every run's LLM-generated summaries to a durable table to enable retrospective QA and false-positive measurement.

**Rodrigo ****B. —**** Port Email**

Shipped Matt's pre-meeting deliverables on 2026-04-22 (missing bar chart, consistent color coding, Delta column header) and added promoter/detractor/passive chips to sub-factor sections.

Built a venue-replacement function (Ocean View Cafe, Blue Restaurant so far) to stop the LLM attributing on-ship venues to ports; Erick granted access to David's venues JSON repo so Rodrigo can expand to the full venue list. Matt scheduled a 1-hour workshop for Tuesday — Erick attending in person.

Debugging per-topic promoter/detractor count divergence from response counts — reworked filter ordering (group before filter) significantly increased counts; remaining divergence under investigation.

**Erick ****A. —**** Fleet Medallia Email Reliability**

The fleet-wide Medallia email job fails intermittently. Root causes likely twofold — an ETL caching issue and unreliable behavior from Databricks' built-in ai_query when called across many records. Erick is replacing the ai_query step with a **custom async LLM summarization approach** (more reliable at scale and materially faster) and separately isolating the caching bug.

**Erick ****A. —**** Port-Level Forum Scraping (Additional Data Source)**

Evaluating whether port-specific forum/review content (Matt's suggestion) could feed into the port email as an additional data signal. Erick took this off Rodrigo's plate — he already has working scraping code from Consumer Insights. Caveat: sample volume is very low (~15–20 posts per 4 months for Roatan-related content, many off-topic); will quantify value before investing further.

**Rodrigo ****B. —**** Beach Club Email Templates**

Reviewed the Santorini Beach Club email template — product hasn't opened yet (first sailing June 2026), so all records are currently null; work paused until opening. Santorini and Royal Beach Club share the agreed approach: reserved top 1–2 slots for business-overridden new products via re-ranking rather than retraining.

**Cross-workstream**

**Shorex keywords for safety pipeline** *(Osvaldo V., **Danusio** G.)*: Osvaldo will send Danusio a product_title + tour_code query so the safety pipeline's regex/NER step can better flag shorex-related comments.

**Target Setting *****(Erick A.)***

Extending the Target Setting forecasting framework beyond consumer-satisfaction targets (NPS / rebook) to include **onboard revenue targets for Track** — Hotel Operations' revenue-planning system. Same multi-model + bias-correction + feature-enrichment approach used for satisfaction targets; the validation dashboard will be extended to compare AI vs. naive vs. business revenue targets at the sailing level.

Kevin D. & Glen-Erik C., Erick G.

PCP Pricing Automation

Continuing to work on building out an unified app with PCP Pricing Automation, Targeted Offers, and Product Recommendations.

Kevin D Meeting with Harrison and Yassine on 4/24 to go over the authentication stuff and if we could inherit hybris user permissions

**Mass Promotions:**

Getting access for teams on Mass Promotions Writeback

Table to track everything (Data and Digital team)

Yassine doesn’t have a team staffed yet

Will need to size it up.

Works-In-Progress:

Working on UI Access (DS)

Shipboard Promotions (Digital)

Success/Failure Data set (Digital + Data)

**1:1 Targeted Offers:**

Lots of Testing Last Week

Imagery isnt working. Ability to change images.

How does the routing happen (test could route)

Routing Piece is Fine (Not Coded Differently For Brands), but Name Piece is still outstanding

Still not working for CEL.

**RCI:** Exclusive Offer

**CEL:** CEL is personalized. Not landing on the right page (PDP, but fixed) or displaying name.

Pulls in for Notification than Takeover (Need to Talk to Yassine and Glen-Erik)

Glen-Erik will fix by EoD or CEL will use generic messaging.

Need a Cabin Level List

**Planning Timeline:**

Start initially for one sailing

Next time we'll try something else to cover with the same test

**Key Requirements**:

Scale by Product and Sailing when to 1,000

New Population for New Tests with Suppression

Marketing we need to create an offer bank for pre-canned promotions

Requirement: Simple prioritization rules for offers

Work with Legal Alignment for Future Testing

Look for Patterns in the Segmentation and Secure Broader Approval

No AI Likely to Be Used

**Very positive feedback on ****glen****-****eriks**** UI interface for targeted offers that ****shows OBR teams what the promo will look like for a guest**

Conversions already incorporated for Waterpark, RBC, but not yet for Beverage (but soon likely this week)

Tracks for ShoreX being worked on with Jorge

Conversion Data will be normalized by surrounding sailings (is visibility or price)?

Has conversion started to increase

Rafa: What is the model doing? What is the acceptance of the recommendations (up or down by RCI)

**1:1 Web UI Requirements:**

**Restrictions:** Cannot be Requestor and Approver. If Sick or Out, need a new approver.

Access: Ensure access based on Hybris and connect with Yassine on Offer Integration.

Glen-Erik C. and David W.

PROPEL (SSC)

Shared a draft of the PROPEL sCAR.

The team aligned on how **new fare structures introduced in Sept 2025** change guest behavior, revenue levers, and the data foundation underpinning the Propel sCAR pilot.

**Fare model overview**

Three active fare types now exist: **All Inclusive Plus**, **All Inclusive**, and **Last Minute**, replacing legacy door-to-door and port-to-port fares.

**All Inclusive Plus** is the premium tier and the only fare that includes a **shore excursion (****shorex****) credit**.

**All Inclusive** is positioned as a lower-priced, standard package with no shorex credit.

**Last Minute** opens only when demand is weak, requires full upfront payment, and carries the strictest terms.

**Shore excursion credit mechanics (All Inclusive Plus)**

Credit is defined **per port, per day** but shown to guests as a **total amount**.

Guests can spend the entire credit at once or across ports.

Any unused credit at voyage end is forfeited and returns as **net ticket revenue**.

Positioning is “**Luxury of Choice**,” replacing basic included excursions with flexibility and upsell potential.

**Revenue and behavioral implications**

Shorex now represents **~70–80% of onboard revenue** for SilverSea due to most F&B being included.

Many guests redeem shorex credit **pre****-cruise**, meaning purchase behavior increasingly occurs before sailing.

The new model reveals **true guest preferences and willingness****-to****-pay**, whereas past data was distorted by fully included excursions.

Credit structure creates both **natural upsell opportunities** (spend beyond credit) and **breakage economics**.

**Early demand mix (directional)**

Roughly **60–70% All Inclusive Plus**, **~20% All Inclusive**, remainder Last Minute.

History is limited given the recent rollout, so insights are still maturing.

**sCAR**** / Propel direction**

The sCAR effort should be framed as a **focused, exploratory pilot**, not a full-scale program.

Initial recommendation is to **start small** (e.g., ~5 simple offers) rather than “boiling the ocean.”

Near-term focus should be on **ShoreX**** (and possibly Spa)**, with narrow, well-defined categories.

Primary output is creation of **propensity models and data assets** that can be reused beyond Propel (e.g., targeted marketing), even if full offer automation comes later.

The pilot is intended to **de****-risk and inform a future full CAR**, not replace it.

Glen-Erik C.

PCP Pricing Automation

Apps

Aligned architecture: Kevin, Erick, Eswar, and Glen-Erik

Requested creation all containers (unified front end, recommendations, mass promo, and targetted offers).

Mass promo app: (*Eswar)*

Created v1 of the app

Internal review & ready to present to the business

Targeted offers app: *(Glen-Erik)*

Added validations

Added logging of requests so user can see and clone past submissions

Added  writing to unity catalog in different environments

Targeted offers pilot - App & Web: *(Glen-Erik)*

Tested in production on android & iOS with fake bookings.

Identified cache issue with pricing. If a guest has the app open recently to see those products it will show stale pricing data when the notification is sent. This should not be an issue since the probability of a guest doing this is low.

Separate notification & takeover messaging is working in production

Takeover image works in iOS only - default image in android

PENDING:

Get Terms &Conditions copy and test that it populates correctly

Grainy takeover image

Royal Android

Targeted offers pilot - Email:  *(**Glen-Erik)*

Data model changes: all text fields are now single language and added offer link created dynamically from the passenger data.

Sent new data so DE and Digital can modify their part of the pipelines to SFMC.

Glen-Erik C., Javier, Santiago

PROPEL

Measurements: *(Javier)*

Designed robust data models with hierarchical fallback logic to reliably fill missing booking and passenger attributes

Defined and corrected revenue attribution logic, ensuring accurate splits across test, control, organic, and pre- vs in-cruise revenue

Finalized and documented the measurement_granular table, aligning business metrics and improving stakeholder usability

Conducted data quality investigations in legacy propel code, identifying join mismatches, null propagation issues, and coverage gaps across datasets

Productionalization: *(Javier)*

Researched SQL unit testing framework in Databricks using pytest, including reconciliation, invariant, and duplicate-grain tests

Researched a durable testing strategy for evolving data, avoiding fragile checks and ensuring long-term pipeline reliability

Scheduling issues: *(Santiago)*

Finalized the new scheduling table logic fixing gaps in runs, international dateline issues, and discovered and fixed incorrect port information

Validated all ships running properly with the new schedule in dev.

Ready to push to prod today (Friday).
