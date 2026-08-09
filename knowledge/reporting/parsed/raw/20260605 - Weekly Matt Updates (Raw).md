**Ayon Ghosh**

**MIAP**

**Win-on-Waste**

Completed a full cleanup and correction of the **Interport pipeline** and successfully **integrated it with the Specialty pipeline**.

Identified and resolved major issues introduced previously, including:

Schema inconsistencies

Checkpoint failures

Logical errors in feature engineering

Problems in parallel modeling workflows

**MDR Interport corrections are still pending** and will be addressed next week.

Added a new venue, **Chef’s Table**, across **Bar, Restaurant, and Specialty Interport pipelines** and successfully deployed it.

This venue presents unique challenges due to its **low frequency, sparsity, and varying locations across ships**, requiring custom handling.

Continued work on expanding venue coverage by adding **Portside Barbecue**:

Completed integration for **Bar pipeline**

**Specialty pipeline integration in progress**, planned for next week

Mert

Supply Chain IBP

Met with the Capital Planning and IBP teams to discuss building a vector database for eCAR. Currently pending readiness from the IT team to move all CAR memos and financial

David W.

Newbuild

**Newbuild AI Enterprise Observatory / CAR**

Advanced the **Newbuild AI Enterprise Observatory CAR** with a full first draft of the memo now completed and circulated for review, including **~17 pages of content plus financials**.

Current request remains **$1.6M in Capex** with approximately **$680K-$700K in recurring Opex**, framed as a strategic investment to convert fragmented Newbuild knowledge into a durable internal capability.

Continued sharpening the core business case: rather than relying on repeated consulting support, this investment helps **institutionalize knowledge inside RCG**, reduce dependency on external firms, and preserve critical Newbuild learning that would otherwise leave with consultants.

Reinforced the value narrative that this is not primarily a headcount reduction story, but rather a **capability retention, cost avoidance, and reinvestment** story — enabling Newbuild to scale more effectively and potentially grow the team by **8 instead of 10** over time.

Incorporated and refined the positioning around the **three integrated platform layers**:

**Foundational data / knowledge layer**

**Specialized domain AI agents**

**Secure user interface & web application**

Further strengthened the in-house vs. third-party rationale, including prior evaluation of **Cadentia**, emphasizing **IP retention, lower long-term cost, better embedded domain knowledge, and tighter integration with RCG systems**.

Continued to frame the Observatory as a broader enterprise asset, not a siloed Newbuild tool, with natural linkage to adjacent operating domains such as **Marine Operations / GMO** and potential expansion into other knowledge-heavy areas over time.

**Discussion with Hani**

Walked Hani through the draft CAR and broader rationale for the Observatory investment.

Hani aligned with the importance of **retaining knowledge internally rather than repeatedly hiring consultants**, and the discussion reinforced that the platform helps protect institutional learning while supporting long-term cost avoidance.

Discussed potential offsets / return framing; Hani was **cautious about forcing a small partial offset** purely to cover part of the cost, particularly given the scale of the broader Newbuild portfolio.

Acknowledged Mert’s point around possible small capital reductions, but the discussion suggested that a **$200K-level offset is relatively immaterial** against the scale of a roughly **$75B portfolio**, so the focus should remain on the broader strategic case.

Hani asked that we **review the detailed use cases carefully** to ensure the Observatory directly addresses the specific needs that teams have surfaced, which will be important for strengthening support ahead of submission.

Also discussed the importance of positioning the Observatory with **clear linkage between Newbuild and Marine Operations**, ensuring the capability is seen as extensible and beneficial across functions rather than isolated within one department.

**Next Steps**

Hani, finance, and I will continue reviewing the draft and underlying assumptions.

Plan is to **share with Harri next, then Naf**, to build support and align on the submission path.

Need to determine whether any **returns, allocations, or offsets** should be reflected before final submission.

Target remains to **submit the CAR in July**.

Mert

Newbuild

- Reviewed the scope for the Hero of the Seas yard energy solution with MIAP. Agreed to secure funding from Newbuild IT and Newbuild Marine to develop real-time ML solutions for Hero in 2026.

- Created a knowledge documentation repository for the Newbuild AI project, with integration into Obsidian and structured in a format ready for knowledge graphs.

Mert:
MIAP
Completed the AMOS AI Agent, LEIF (Lifecycle & Equipment Intelligence Framework) — a specialized custom agent for AMOS with the capability to answer all user questions related to how AMOS works and its underlying data.
Made improvements to the MIAP AI Agent Python package by introducing a judge agent that determines whether tool call results are sufficient or if Databricks Genie should be invoked as a sub-agent to generate custom SQL queries. Also added a sub-agent to summarize large tool outputs to avoid consuming the main agent’s context window.
documents to an Azure Data Lake account.
Created a mockup app for Risk Management.

Mert

MIAP: **Decarbonization & Energy AI — Strategic Progress Update**

Met with the new Energy Management team, including a new director and manager based in the UK office. We’ve re-established alignment with the broader decarbonization organization following a working session with Sahar and the newly hired UK fleet monitoring leadership, creating direct integration into recurring stakeholder forums and decarb communications that we were previously not included in. This significantly improves visibility, coordination, and our ability to influence enterprise energy strategy.

From a strategic and investment standpoint, we’ve aligned on an **Energy AI “Money Map”** outlining a clear path to ~$56.5M in incremental annual energy savings on top of ~$50M already realized through MIAP, driven by AI-enabled optimization across propulsion, deployment, voyage planning, and power management. Delivering this portfolio requires approximately ~$8M in capital investment and ~$2M in annual OpEx, with additional GMO resourcing required to sustain and scale these capabilities.

As part of this plan, we are incorporating three key initiatives into the 2027 capital roadmap:

Dynamic Energy & Digital Twin Models Phase II (serving as the placeholder for deployment optimization)

Hull and Propeller Performance Models

Marine Insights & Analytics Platform (expansion across Muse, Moon, and Dawn)

These near-term (2027–2028) investments focus on high-confidence, internally developed AI capabilities with multi-million dollar annual savings potential. Critically, structuring these under a coordinated or joint CAR creates an opportunity to optimize funding allocation and offset costs tied to deployment optimization.

Longer-term (2029–2030), the roadmap progresses into more advanced, safety-critical optimization capabilities, including voyage planning, speed/trim advisory, and power plant optimization, which will likely require vendor partnerships and depend on foundational capabilities established in earlier phases.

Overall, this positions AI as the **core intelligence layer for energy optimization**, directly linking operational efficiency, regulatory compliance, carbon accounting, and deployment strategy—with a trajectory toward $100M+ in annual impact by the end of the decade. Key next steps include clarifying what elements are already funded vs. incremental, defining the operating model and GMO resourcing strategy, and formally integrating this roadmap into the enterprise capital and strategic planning process.

Will:

MIAP
This week, I wrapped up the EDA and modeling proof-of-concept for charge air cooler fouling detection on the Wärtsilä 46F fleet (branch: feature/charge_air_cooler). I am still in the research phase, exploring different modeling approaches and performing the necessary data engineering to support them.
I built a first-principles thermodynamic model of the two-stage cooler, calibrated it against factory test data, and validated it using operational IoT sensor data. During this process, I discovered that engines 1 and 3 are a different variant (W16V46F) than the rest of the fleet, so engine-specific reference conditions are now automatically selected.
I benchmarked several approaches:
Flexible ML and symbolic regression achieved high R² when predicting charge-air temperature, but were primarily learning weather patterns (humidity-driven), as the thermostatic control valve masks the air-side fouling response.
Pure first-principles modeling extrapolates well but is sensitive to boost gauge/absolute scaling and the masked LT inlet.
A physics + ML hybrid approach (where ML learns only the residual) appears promising.
V3 (current direction):
Reframed the problem to focus on water-side heat transfer (ΔT_LT) instead of charge-air temperature. The model:
Normalizes against heat load using ΔT_HT
Uses a frozen per-engine baseline trained on a full clean seasonal cycle
Subtracts the cross-engine median residual so seasonal/climate noise cancels out
Applies CUSUM on the fleet-relative signal for fouling detection, anchored to engine 1’s early-2025 cleaning event
Code is organized into three notebooks (CAC_Feature_EDA, CAC_Model_Calibration_EDA, CAC_v3_Baseline) plus a shared Python module. The next phase is productionizing V3 into a monitoring pipeline.
Tickets closed:
Fixed silver ETL exception for AL and OA thruster power tags
Added DE load tags to the ETL

Reza:
MIAP
Completed the bio and biogas fuel blend logic in the Digital Twin.
Updated the MIAP app GUI to allow users to input base and blend ratios for bio/biogas consumption across OFB, Incinerator, and Generators. Also updated the REST API to support these changes.
Conducted brainstorming on the architecture for incorporating capital savings into the Digital Twin. Implementation is in progress following a revised approach.
Evaluated model outputs and explored new ideas for the turbo compressor and charge air cooler model/anomaly detection project.
Updated the model and baseline for Ship ID within the service power area.

Mahshad:
MIAP
Detected a deviation in AHUs of around 150 kW. The issue has been reviewed and approved by the ship team, and they are required to fix the HVAC computer to resolve it.
Added new features to the MIAP app, including:
Inlet and outlet temperatures for chillers
Route mapping
Region tagging (e.g., Mediterranean, Caribbean, U.S. East Coast) in HVAC and chiller plots for improved analysis
Integrated an individual chiller model into the pipeline; however, it is still encountering some errors that need to be resolved.

Eddie B.

RCI Rev mgmt.:

Extra context for some of the things we discussed on what happened this week:

Gained alignment to move RCI PRE cutoff from 12 WTS to 45 DTS, starting with Short Caribbean Meta Product. This is a big deal!!

How are we getting there:

Process that dynamically identifies which ship / sail date / cat classes are on Last Minute Cruises Promotion (more than you think within 90 days)

Coordinating with teams on additional requests. Specifically reviewing recommendations in that window with the Short Caribbean team next week

RCI PRE acceptance over 70%

Recent weeks have been in the low 60's

**Track Smoothing played a big role!** Big swings in expectations were difficult for analysts / PRE to manage to, resulting to high pause rates driven by Track - related reasons

Amount of times tracks being labeled as erratically moving went down from 26% in April to just 14% last week!

Change management content provided for RCI Quad Management Strategy for Off-Peak

I have an interesting use case for Claude I am going to play with QUITE a bit today. some context. Part of the work I had done for RCI was identifying max out situations in off peak, and creating a log on when we would want to basically link and de-link quads. This work has been delivered on my end but is expected to go live at the end of the month (Nick has his team launching like 6 or 7 projects related to this at once instead of incremental which should be fun). I will be adding update details highlighting the process and work I did from top to bottom on it.

Doug B.

CEL PROPEL

The data is now looking good after Doug evaluated and scrutinized it. Doug got a PROPEL offer on his CEL cruise with ML. The program on ML looks to be working as planned. Javier credited an inorganic purchase of WIFI. Purchased beverage without a CEL PROPEL offer. The data looks to be right. Doug is working on the metrics that he needs. What was the lift, what was the number of offers, what can we attribute to the OFFERs.

The measurements data to build the measurement framework is sound. Base data from BCG was deeply flawed like duplicating offers (for something someone already purchased). Doug discovered “duplicates” or rather two bookings assigned to a cabin that had didn’t account for last-minute cancellations. This generates an offer for a booking that doesn’t exist. When measuring after the fact and clean up cancelled bookings and apply the faulty offers to the new booking.

Doug is converting the basic requirements for analytics into action. There was a disconnect with prior work, but Doug is unblocking CEL’s ability to understand how the offer is working. Provide visibility into offer conversion.

Javier & Santiago

CEL PROPEL

Summary

**Documentation & Architecture**: Expanded system documentation to include concurrency, deployment design, and information architecture.

**Performance & Workflow Optimization**: Improved Spark performance and assign-offer logic while enhancing workflow scheduling, environment-based configuration, and operational controls (e.g., uplift model pause flag).

**Production Stability & Data Quality Fixes**: Resolved concurrency write failures, eliminated offer mapping conflicts, and tightened business rules (e.g., preventing duplicate WiFi offers for bundled guests).

**New Capability (In Progress)**: Designing an offer simulation/validation application with scalable backend architecture, governance (permissions, logging, auditability), and flexible rule configuration.

**Data Consistency & Measurement**: Validated SKU/category mappings across key business tables to ensure consistency and reporting accuracy.

1. Documentation:

a. Updated the architecture documentation and diagram set adding concurrency, deployment, and information-architecture.

2. Refactoring:

a.  Optimized assign-offer quota logic and fallback behavior:

i. Identified Spark performance bottlenecks, including expensive count() operations and lineage recomputation.

ii. Worked on improving execution time without changing the expected business logic or output.

iii. Reviewed fallback and expected-value logic to validate when fallback behavior is triggered

b. Workflow / job pipelines:

i. Improved scheduling and failure-notifications on some workflows

ii. Aligned schedules, tags, and notifications with environment variables.

iii. Added a dedicated pause flag for the uplift model.

3. Production Failures & Bugs:

a. Fixed transient concurrent data write failures by adding bounded retry logic.

b. Other minor tickets on failures and prod issues.

c. Prevent Wifi Offers for guests who already purchased a bundle:

i. Reviewed the business rule to exclude WIFI offers when guests have already purchased a related package or bundle.

ii. Analyzed product codes and bundle logic to avoid invalid or duplicated WIFI offers.

iii. Bundle mappings maintained by DE team, requested them to update the mapping table.

d. Intermittent offer mapping issue: offer config ingestion happens twice a day, when it overlaps with an offer run it can cause ID mismatches affecting the offer count. Now the ingestion will not overlap with a run, instead it will happen before a run.

4. New capabilities:

a. Offer simulation/validation app:

i. Started designing the backend structure with FastAPI, Python, and OOP principles.

ii. Defined frontend/backend responsibilities for editable min/max offer rules.

iii. Reviewed production-ready needs such as backend validation, permissions, logging, auditability, and scalable execution patterns.

5. Measurements:

a. Category SKU mapping: analyzed consistency across key business tables, including offers, offering text, category text, revenue tables, and related datasets.

Glen-Erik C.

PCP Pricing Automation

1. Royal Pilot App/Web:

a. Successfully scaled Targeted Offers Hub App that builds, validates, and submits offers to Hybris using it to complete the second pilot for Royal sending 4651 to guests and 1584 tracked for control.

b. Issues:

i. Hybris was unable to keep up with the load taking many hours to complete

ii. 187 guests failed to receive  the offer in Hybris

iii. Unknown number received the notification, the test accounts did not.

2. Royal Pilot Email:

a. 4443 offers sent to SFMC manually after confirmation that the offers exist in hybris. The prod pipeline was expected to be completed but the final step of submitting to SFMC appears to be missing and requires an RFC (request for change) to be completed.

Test Group for App / Web 4651

Control Group 1584

Final Faliure count: 187

Actually Received Offer Discount: 4464

Actually Received notification: N/A

Bookings with mixed guests  21

(some received & some didn't receive the discount):

Test Group for Email: 4443

Not eligible to receive email (test): N/A

Actually sent email: N/A

3. Targeted Offers Hub App Development:

a. Added tracking of fake bookings

b. Scaled to support thousands of offers

c. Scaled to support offers across multiple sailings (control/test split at sailing level)

d. Gave initial training to Celebrity on using the App.

Eswar & Javier

RCI Revenue management

• TAP Refactoring: (Javier)

○ Led a major refactor to reduce duplicated code and centralize shared logic.

○ Created a new framework package with shared modules for:

§ SharePoint

§ Schemas

§ Training utilities

§ IO utilities

○ Replaced %run with proper imports of reusable modules.

Kevin D.

PCP Pricing Automation: Beverage Package Update

Model Refinement & Performance: Enhanced the beverage dilution model by tightening scope (same-day cancel/rebook), improving product mapping, and applying class-level calibration, resulting in strong generalization, accurate guest ranking, and improved total dilution prediction (MdAPE ~30%).

Backtesting Insights: Memorial Day spike (10K events vs. ~1.5K baseline) validated model scalability, with underprediction primarily driven by a single high-volume product (AI Alcohol Upgrades).

Next Steps: Isolate AI Alcohol Upgrades into a separate model, advance to demand modeling (segment-level forecasting + guest-level propensity), and integrate outputs into targeted offer strategy.

Strategic Outcome: Establishes the foundation for the Beverage PRE framework and introduces a data-driven trigger to shift from mass promotions to targeted offers when dilution risk is elevated.

- DETAILS: Continued to refine beverage dilution model addressing stakeholder feedback and incorporating a memorial day sale backtest. The dilution model was adjusted to only focus on cancel-rebook on the same day and improved product mapping. This enhancement required substantial post-hoc class level calibration capturing recent trends while still allowing for oversampling of minority classes in training. This led to a well generalized model that accurately ranked guests based on dilution probability but also accurately predicted total dilution. Memorial Day saw 10,000 cancel rebook events, 5X any week in the training data. While the model did not capture the full 10K predicting 6500, the model extrapolated very well as the average weekly dilution events in the prior 2 months was 1500. The underprediction was driven almost entirely by one high volume low priced product (AI Alc Upgrades). Backtested errors are evenly distributed about zero with a MdAPE of 30%. Next steps will be to segment AI Alc Upgrades into their own model while continuing to model the other products together and advancing to the demand model. A major step towards delivery of the beverage PRE that will serve as the framework for all non-inventory constrained PCP products. The new demand models will be two fold 1. A segment level model predicting demand for the rest of the sailing window across different guest segments. 2. A guest level model predicting booking propensity of current booked guests. The guest level model allows richer data (clickstream behavioral data) and higher prediction accuracy for close in management but will not meet the needs of predicting future demand, since we don't know the booked population several weeks/months from now. The guest level model also generates booking propensities that will be utilized by the audience builder for targeted offers. A plan has been identified using the dilution model to give guidance to the business on when to switch from mass promotions to targeted offers i.e. dilution risk is too high.

Kevin D.

PCP Pricing Automation: TARGETED OFFERS

- Completed pilot 2 of targeted offers. Sending 5000 offers for 50% off deluxe beverage packages to guests. This was completed through Glen-Erik's Targeted Offers Hub Application, with Kevin defining the population. There were several issues identified with the process including:

- 1. latency on Hybris processing the increased volume.

- 2. An error in the source data identifying US only pax, leading to not all pax in the cabin receiving the offer (resolved)

- 3. Inconsistency on displayed discount vs actual.

- The increased QA checks Glen-Erik added to the App caught several more issues during launch that were able to be remedied quickly before submitting the offer. Even with the issues observed, first-day readings are positive with test population converting 4X the control population. **This is a big win to have a functional targeted offer that works and driving behavior.**

- Kicked off new monthly planning session with Rafa and Gang highlighting completed/in-progress/future work with timelines and resource allocation. Feedback to the new meeting format was very positive and the stakeholders are happy with the increased visibility and timelines. Rafa and Alex asked that existing Propel be added not only to the update but also oversight of the PCP2 team, stating that the propensity models should be integrated in the PCP projects.

Erick A., Cristian V.

**PCP ****MyCruise Recommender**

**Summary:**

- **Production Ready & Stable: **Recommender fully migrated to dedicated prod Postgres and stabilized, removing dev dependencies and resolving prior infrastructure blockers.

- **A/B Testing Enabled: **Core capabilities now live (user split logic + hard-coded product slots), with initial experiments defined (margin vs. revenue, business picks vs. pure model) and API performance investigation underway.

- **Model & Feature Integration Advancing: **Actively integrating improved models (David), segmentation (Danusio), with Apriori enhancements next — unblocked by shared notebooks.

- **Visualization Enhancement Delivered:** Atlas webapp blocker resolved via D3.js pivot, enabling clean, scalable port-level excursion visualizations.

*Personalized post-booking recommendations (excursions, dining, spa) powering the ForYou surface in the app.*

**Infrastructure / Postgres & API**

**Postgres Prod Deployment** *(Cristian V., Completed)*: Last week's network/firewall blocker that held up the production Postgres instance is **cleared** — Cristian completed all adjustments and the recommender is now 100% running on the dedicated prod database. The shared dev instance is no longer carrying production traffic.

**A/B Testing**

**A/B Test Splitter** *(Cristian V.)*: Building on last week's "A/B testing becomes possible" milestone, Cristian met with Rosie (Product) this week to align on the first iteration — a user-to-group mapping system. First test: margin-vs-revenue ranking policies. Second: recommendations with vs. without hard-coded business picks. A follow-up sync is needed to understand why Apigee (the API gateway) shows low RPS and whether caching can be disabled for the recommendations endpoint only.

**Hard-Coded Product Slots Deployed to Prod** *(Cristian V., Completed)*: The capability to pass business-selected products into specific recommendation slots is now live in production — a prerequisite for the A/B testing roadmap.

**Productionization**

**Team Model Integration** *(Cristian V.)*: Continuing last week's active integration push, Cristian is productionizing David's model improvements and implementing Danusio's consumer segmentation process into the recommender. Next in queue after these: Rodrigo's Apriori enhancements for all product categories.

**Danusio Segmentation Notebooks Shared** *(Danusio G.)*: Danusio shared his guest-clustering and product-clustering notebooks (with metrics) directly with Cristian, unblocking the integration work.

**Webapp — Atlas Visualization (Port-Level Excursion Categories)**

**D3.js Pivot Resolved the Blocker** *(Osvaldo V.)*: Last week's Three.js zoom/scaling issue is **closed** — Osvaldo switched to D3.js v7 (2D zoomable map) with force-directed declutter for overlapping pie charts. Per-port category mixes (e.g., Cozumel: tours, cooking & tasting, beach day) now render cleanly at all zoom levels. Erick confirmed it looks great.

Erick A., Rodrigo B., David M.

**Project Axiom — Voice 360**

*Insight extraction from unstructured customer feedback (Medallia, Guest Logs, Qualtrics) via LLM pipelines — feeds emails, dashboards, drivers analysis, and chat.*

**Email Reports**

**Port Email — Approximate Frequency Section** *(Rodrigo B.)*: Following Josh Carroll's request to track how topics shift over time, Rodrigo added a new section that uses GPT-5 Nano to estimate how often each complaint appeared in the prior quarter's comments, with evidence. Known limitation: the LLM sometimes confuses similar topics (e.g., tendering vs. disembarkation). Label updated to say "approximate" to set expectations. Continuing work on the remaining Carroll action items (regression-coefficient ranking, quarter-over-quarter tracking).

**Shorex GSO Safety — Fleet Presentation** *(Danusio G.)*: Bridging last week's "going to the fleet" update — report was sent to Melissa for review, ship-name sensitivity addressed (omitted per Melissa's recommendation). Presented to both RCI/CEL Public Safety Officer meeting to present the GSO Safety AI Email. Separately, Danusio identified an edge case: empty report sections when the AI finds zero safety complaints for a period — confirming this is expected behavior rather than a bug.

**Ovation of the Seas Report** *(Erick A., new)*: New request from RCI Product for an Ovation-specific guest feedback report for post dry dock sailings. Additionally, Danusio pulled all Ovation social media data to support the Product team's latest email report.

**Meta Data Framework**

**All Three Pipelines Now Running in Production** *(David M.)*: Last week's divisions-aspect pipeline was the first to go live. This week: bullet points and open-ended topic extraction joined it — **all three projects are now deployed and running daily at 8 AM ET.** Monday's run processed all historical data; going forward only daily deltas are processed, keeping token consumption low. This closes the multi-month effort to get the Meta Data Framework fully automated end-to-end.

**Bullet Points Backfill Complete** *(David M., Completed)*: Historical bullet-points data has been backfilled through 2025 using the production pipeline. The dataset is now fully current.

**Guest Logs Email**

**Guest Logs Backfill In-Progress**: Guest logs back fill is still pending review with the business. Back filling for 2026 only to be able to begin work on automated email reporting.

**Freedom of the Seas POC Report Ready** *(David M.)*: Carryover from last week's "Guest Logs email nearly complete" — David added a guest-score column (1–5 scale), then ran the full Freedom of the Seas backfill for 3 months of short-sailing data. The sailing-level guest-logs email report is ready for review. Next: share with the guest logs team at a sync meeting next week.

**Webapp — 3D Ship Model**

**Major UX Overhaul Delivered** *(Rodrigo B.)*: The 3D ship model received a significant upgrade this week: improved UX, multiple bug fixes, 5 different clustering computation options, a scoring/ordering system for critical clusters (controlled via slider), click-to-LLM cluster analysis with auto-generated CSV and Markdown report per cabin, and temporal complaint tracking visualization.

**Ship Insights Report QA'd and Validated** *(Rodrigo B.)*: Erick reviewed the ship insights report (generated from the 3D model) and flagged that Gang may share it with senior leadership — if they ask "what are those 167 complaints?" we need evidence. Rodrigo conducted manual QA: cabin counts are directly extracted (accurate); complaint counts are LLM-extracted but confirmed directionally correct. Report is ready for business validation.

**Automated Report Generation Scoped** *(Rodrigo B., new)*: Gang wants AI-generated insights reports for every ship in the fleet. Pattern defined: drop new ship data into a folder, reference prior reports as few-shot examples, and the LLM generates the same format automatically. Rodrigo confirmed the process can be automated.

**Symphony of the Seas Validation — Patterns Found** *(Rodrigo B.)*: Bridging last week's "validate new clustering against known noise hotspots" — the tool surfaced plumbing issues in adjoining cabins (shared infrastructure), accessibility/elevator complaints spanning multiple floors, and internet-connectivity complaints in high-density cabin areas. Next: add subtopic labels and time-based trending to distinguish persistent issues from one-off complaints.

**Celebrity Operations Analysis**

**Xcel and Solstice Reports Delivered** *(Osvaldo V.)*: Bridging last week's "both ship reports recreated" — Osvaldo sent the final Xcel and Solstice operations analysis reports to Erick. He now has the query and reporting-topics table access to produce additional ships independently. Gang sent a comprehensive list of ships and the dry dock schedules which we will use to create additional reports.

**SSC Updates *****(Erick A., new)***

**Axiom Ship Scorecard Changes** *(Erick A.)*: Multiple updates queued for the SSC component: remove LTR, remove Hotel Services, add STLY (same-time-last-year comparison based on ship matching), add neutrals breakdown, and add total promoters/detractors/neutrals counts.

Erick A., Osvaldo V

**Project**** AXIOM:**** Concept Testing Lab**

*Agent-persona framework using LLM-driven synthetic respondents to A/B test ideas and concepts before committing to live tests. Built on TinyTroupe (Microsoft OSS).*

**Work Paused Pending Medallia Meeting** *(Osvaldo V.)*: Last week's "first outputs in hand" deliverable — an HTML report testing the CocoCay kid-free zone concept against 2021 real research data — is complete and will be presented to Stakeholders. Osvaldo is building a comparison report (TinyTroupe framework vs. existing approach).

Erick A.

**Contact Center **

**Project**** Siren**

**CCAS Booking ID Extraction** *(Erick A., new)*: Reviving an existing Databricks job to extract booking IDs from 1 year of CCAS calls. The pipeline exists but needs to be brought back online. Blocked on data engineering resolving an upstream dependency.

**Time-to-Topic Pipeline Fix** *(Erick A., new)*: Blocked on data engineering resolving an upstream dependency before the time-to-topic pipeline can be repaired.

**Lead Scoring**

**Trade Segmentation Pipelines** *(Erick A., new)*: Resurrecting and debugging the broken trade segmentation pipelines used for lead prioritization.

Erick A,

**PCP Pricing Automation: ****Target Setting**

**Model Performance Readout for Gang** *(Erick A.)*: The daily target-setting model (forecasting revenue targets for internet, shorex, dining, etc.) has been running in production since mid-May. Gang is expecting a readout next week on forecasting performance. Erick is assembling a summary of key takeaways and forecasting accuracy broken down by product category and by market-level vs. aggregate forecasts.

David W.

IBP Risk Management

Wrote a 50 page reply for the DPIA & AI Assessment and shared with positive feedback from Data Governance & IBP Steering Teams:

**Project TIDES — Legal Summary: What We Can and Cannot Do With AI**

Project TIDES is formally classified as a **high-risk AI system** under the EU AI Act because it processes special-category health data, affects access to insurance and financial outcomes, and—for crew—influences employment-related decisions (screening, task allocation, return-to-work). This classification, combined with GDPR's protections for sensitive health data, sets the boundaries for the whole initiative. The bottom line from both the DPIA discussion and the white paper is consistent: the project is legally viable and deployable at scale, but **only** if it operates strictly as a human-supervised decision-support system rather than an autonomous decision-maker. The recurring legal red lines raised in the working discussion—attorney-client privilege, the privileged status of settlement discussions, and the use of historical/prior litigation and health data for model training—all map onto these same constraints.

**What we *****can***** do:** Use AI to score and triage incidents, predict claim propensity and expected cost, estimate medical/clinical severity, auto-build and summarize claim files, and recommend (not set) settlement ranges and follow-up actions. Health and injury data may be used in controlled ways to assess **clinical severity**—but not behavioral inference—because severity assessment is treated as materially different from profiling. Claims-handling itself is lawful under contractual necessity and legitimate interest (risk management and safety), with explicit consent or an Article 9 condition relied on for health data. Historical claims data may be used for training provided it is bias-reviewed, segregated from operational data, pseudonymized/tokenized, and stripped of protected attributes. Prior litigation and privileged settlement information must be handled with particular care—the DPIA flags that settlement amounts and lawyer-client communications carry privilege concerns and should be escalated to the litigators before that data is pulled into the platform.

**What we *****cannot***** do:** No fully automated decisions with legal or financial effect on an individual (a human must approve every material outcome); no behavioral manipulation, nudging, or exploitation of vulnerable people (e.g., injured or elderly claimants); no social scoring; no real-time remote biometric identification; and no AI emotion-inference in the workplace (crew mental-health screening like PHQ-9/GAD-7 is treated as clinical/medical screening under the safety exception, pending Privacy-team confirmation). Protected attributes—race, ethnicity, gender, socioeconomic proxies, and proxy fields such as loyalty tier or ZIP code—**must not** be used to predict claim likelihood or cost. Data collected for claims cannot be repurposed for marketing or unrelated profiling, and a hard boundary must be maintained between Claims AI and customer analytics. Anonymization must prevent re-identification of any individual, and pre-existing conditions cannot be used as a basis for decisioning. Finally, because RCG is both **provider and deployer**, it must itself complete the EU AI Act technical documentation and conformity assessment (an outstanding action), maintain full audit logging, give claimants explanation and contestability rights, and obtain sign-off from Privacy, InfoSec, Legal, and the named executive approvers before deployment.

Mert E

IBP: Claims Management

Hugely positive reaction from Steering Group (Jessica, Ben Riestra, Nicole, and Randy):

**Project TIDES — Meeting Summary**

**1. Overall Takeaway**

**Very strong positive reception** — stakeholders see clear differentiation in the Claims Workbench and alignment with real operational pain points (fragmented data, manual case review, lack of visibility across lifecycle).

Project is **legally viable but tightly constrained** — must operate as **human-in-the-loop decision support**, not autonomous decisioning.

**2. Strategic Positioning (Aligned to What Was Presented)**

**Core Value Proposition (Validated in discussion + visuals):**

**Single source of truth** across 4+ groups in Naf’s organization

**End-to-end claims lifecycle visibility** (incident → claim → litigation)

**AI-enabled decision support**, not replacement

**Claims Workbench clearly resonated as the differentiator:**

Risk-based triage (probability × cost)

Escalation prevention (incident → claim → litigation funnel)

Embedded recommendations and settlement guidance

Centralized intelligence (CCTV, activity logs, medical, reports)

**3. Product Capability (What Landed Well)**

**A. End-to-End Workflow Integration**

Unified incident → claim → litigation funnel with exposure tracking

Ability to identify:

Incidents at risk of becoming claims

Claims at risk of litigation

Action windows and recommended interventions (e.g., follow-up timelines)

**B. Explainable AI + Auditability (Critical Theme)**

Fully transparent rationale for predictions (e.g., “why” sections)

Evidence-backed scoring (weather, CCTV, witness logs, activity timeline)

Fraud/anomaly signals clearly structured and explainable

Aligns with **legal requirement for explainability + contestability**

**C. Centralized Data Layer**

Integration across:

RiskConnect, SeaCare, GSIMS, CCTV

Guest activity (Fidelio, POS, Medallia, door swipes)

Ship ops data (AMOS, bridge logs, VDR, weather)

Reinforces **single pane of glass vs current fragmentation**

**D. Investigative Acceleration**

Timeline reconstruction (guest movement + activities)

Automatic summarization of incident narratives

Pre-built investigation and risk insights

Direct reduction in **manual case review effort** (time study highlighted)

**4. Legal & Compliance Constraints (Critical Framing)**

**Guardrails (Non-Negotiable):**

AI **cannot make final decisions** (settlement, claim outcome, employment impact)

Must maintain **human approval for all material outcomes**

Strict separation of:

Claims AI vs marketing/customer analytics

No use of protected attributes or proxies

Privileged/legal data requires careful handling and legal review

**Sensitive Areas Raised in Meeting:**

**Attorney-client privilege vs work-product privilege**

Use of:

Prior litigation data

Settlement amounts

Need to escalate these decisions to Legal before inclusion

**Implication:**

Product direction is confirmed but requires:

**strict governance model**

**auditability baked into the platform**

**clear positioning as assistive, not prescriptive**

**5. Enablement & Operating Model**

**Emerging theme: Platform vs Tool**

TIDES is being recognized as **enterprise enablement layer**, not just a claims tool:

Serves multiple teams simultaneously

Standardizes data + workflows

Enables consistent decisioning frameworks

**Key design separation clarified:**

**RiskConnect → system of record (data storage)**

**TIDES → intelligence + assessment + analysis layer**

**6. Refinements / Open Feedback**

**A. Language / Framing Adjustments**

“Fraud” terminology needs refinement

Prefer: **statistical anomaly / risk signal**

Labeling (e.g., “Deck Slip – High”) needs business-friendly wording

**B. Data & Model Considerations**

Introduce **data quality scoring** to confidence-weight outputs

Be explicit about:

signal reliability

model confidence

**C. Process Alignment**

Align outputs with real operational workflows (adjusters, medical, legal)

Ensure explainability is not just technical, but **operationally usable**

**7. Strategic Impact**

**What this unlocks (clearly reinforced in meeting):**

Shift from **reactive claims handling → proactive risk management**

Earlier intervention reduces:

escalation rates

litigation exposure

total cost

**Enterprise value levers:**

Increased VDR coverage and integration

Time reduction in case handling (validated interest via time study)

Improved consistency and defensibility of decisions

Better alignment across Legal, Medical, Safety, and Operations

**8. Key Next Steps**

Finalize **legal boundary conditions** (privilege, litigation data usage)

Refine **terminology and labeling for business adoption**

Define **operating model (human-in-the-loop + governance)**

Continue positioning TIDES as:

**claims intelligence platform**

not just workflow tooling

Advance broader **enablement roadmap and system-level inventory**

**Bottom Line**

Project TIDES is now clearly positioned as a **high-impact, legally viable, enterprise AI platform** that transforms claims from fragmented, manual processes into a **unified, explainable, and proactive risk management system** — with strong stakeholder buy-in, contingent on disciplined governance and compliance.

Evan M

CEL Rev Mgmt: Demand Forecast

Demand Model: Finalized and identified all deployment requirements. We will likely go live with the new demand forecast for PRE starting in two weeks.

**Value add: Model is being pushed to QA & Production**

Identified fixes for elasticity curves

Worked with Lamis on curve evaluation across cat classes and verified outputs match expectations

Perturbation grid covers +/- 3 / 5 / 10 / 15 / 20% to -50 and 250%

Diagnosed boundary spikes in elasticity outputs caused by step-function effects at the perturbation edges and small-denominator instability

Established Unity Catalog schema as the stable endpoint that products consume from on table names

Completed model improvements for historical accuracy and tracking of history

**Value add: Improved model performance without introducing bias**

Confirmed existing safeguards hold against the target and ensured no leakage

Target encoding smoothing on high-cardinality categoricals, and normalized joins on saturation and clickstream features

Walk-forward backtest validates accuracy on the test window (confirmed no leakage)

Respecting temporal causality and avoiding the random-k-fold leakage that could inflate reported accuracy

Confirmed cabin target construction against priror using long aggregates from current-week bookings, validating it matches actual target

**Lamis**

CEL Rev Mgmt: Track Optimization

1. Recalibrating / Refining the UB/LB

Based on convos with the SHs we found that the bounds are misrepresenting the way the business operates in the recent years due to the inclusion of 2023 and 2024 bkgs data in the analysis. Agreed to reestablish the bounds starting at 2025+ sailings

Based on the EDA primarily done on RCI optimal tracks, I found that due to some sparse data or new deployments the bounds on expected wkly bkgs are based on very limited samples and often underrepresent the actual demand that should be targeted specifically for ship classes where capacity has been increased. As suggested by SHs, I revised the bounds to be based on the bkgs represented as a % of capacity such that the realistic demand patterns (defined by the bounds) are maintained and to be multiplied by the ship capacity which should fix issues with new ships/deployment.

Also added a fallback logic to overcome sparse data issues. Fallback to meta, ship class and cat class.

2. EDA on RCI full-fleet run.

completed some EDAs on RCI optimal tracks generated for the core meta products. The EDA focused on evaluating the followings: If optimal tracks fall close to business or SPI tracks - if post optimization smoothing algorithm captures certain wave peaks and post-wave dips (had to add additional constraints to the smoothing model to fix few issues with over smoothing) - if tracks for the sailings within the same basket are similar, and also the price points and track ask

Noticed few issues with the smoothing for cat classes with limited inventory. Agreed with SHs to follow the base DP output for those cases - Also tested an alternative smoothing algorithm results will be validated by end of this week.

developed an alternative smoothing algorithm - A constrained cubic spline smoothing algorithm, constrained by maintaining wave and post wave optimal track ask and ensuring cum track ask == capacity to fill while minimizing distance to the optimal DP output. Initial results on EUROPE look a lot better.

After revising the bounds, integrating model error and  Dynamic price caps, EDA on ALASKA and Caribbeans is mostly within SPI region. EUROPE sailings still suggest a much slower build while pushing most of the demand closer-in where historic price points have been the highest.  Also tracks of sailings within the same basket are different unlike ALASKA or the Caribbeans. Developed an alternative approach to revise the bounds at least for EUROPE based on the SPI top performers while adding a 10% buffer. Results look a lot better and all generated tracks fall within the SPI-based bounds, while still targeting the highest possible demand closer-in but within more feasible limits

**Michelle**

** ****CEL ****Category-Gapping 3.0**

**Summary**

- **Model & Data Improvements**: Strengthened gap-based lookup tables and refined isotonic regression post-processing to ensure stable, monotonic booking share predictions across varying demand scenarios.

- **Optimizer Fixes & Reliability**: Resolved key allocation issues (e.g., over-allocation, booking shares >1, GTY vs. physical cabin double counting) by improving normalization, allocation logic, and constraint enforcement—resulting in more accurate and interpretable outputs.

- **Business Alignment & Enablement**: Conducted walkthroughs with RCI and CEL to align on validation processes and enable deeper technical involvement in production.

- **Production Readiness**: Modularized and restructured the codebase into scalable, configurable components (lookup generation, validation, optimization, etc.), establishing a more maintainable and production-ready architecture.

**Details**
- Primary focus on improving the construction and reliability of gap-based lookup tables. Met with both business teams to receive feedback.
- Conducted walkthrough of structure with RCI so that they can support validation process.
- Conducted walkthrough of codebase with CEL so team can be technically involved in model production.
- Strengthened isotonic regression post-processing to enforce monotonicity in booking share predictions. I worked on refining how monotonic constraints are applied to ensure that share responses behave consistently as gaps change, while also addressing challenges such as flat regions in low-signal areas and over-smoothing in the tails. This was originally done on the separate availability models and had to be adjusted for the single model approach.
- Enhanced optimizer logic and correctness by resolving issues where booking shares exceeded 1 due to double-counting between GTY and physical cabin allocations, and correcting cases where the optimizer over-allocated certain tiers, particularly Premium. Strengthened normalization constraints, refined GTY allocation logic (including improved waterfall behavior), and incorporated clearer penalties and tie-breaking logic. These improvements ensure that optimizer outputs are feasible, interpretable, and consistent with the underlying lookup table predictions.
- In parallel with modeling improvements, I have been actively restructuring and modularizing the codebase to support production deployment. This includes breaking down complex pipelines into reusable, well-defined components (separate modules for lookup generation, post-processing, validation, and optimization), standardizing function interfaces, and ensuring consistent input/output contracts across modules. I have also been making the codebase more configurable and easier to maintain by isolating business logic from processing logic and improving readability. These changes are laying the foundation for more scalable, testable, and production-ready workflows, enabling easier iteration and integration into downstream systems.

Doug B.

CEL Revenue Mgmt

1. Celebrity T4 A/B Test: Updated metrics to monitor test in progress. Met with Celebrity strategy team to review. Test progressing as expected. Some minor adjustments to exclude a handful of sailings with drift, but won't negatively affect findings.
2. RCI/Celebrity PRE & Pricing: Concluded investigation and validation of stale pricing issue. Pricing is behaving correctly again after a couple weeks of elevated stale rate. Working with Data Governance to develop an alert when such situations arise.

Jesse B.

SSC Revenue Mgmt

Overview:

- **Experimental Framework Built**: Developed a bootstrapping infrastructure to evaluate optimal coefficient sets for the top-suite pricing algorithm by simulating performance against traditional SSC pricing methods.

- **Simulation Design**: Models the booking lifecycle across voyages, cabins, and time windows using probabilistic (binomial) demand simulation and historical purchase data.

- **Comparative Evaluation**: Benchmarks algorithm-driven pricing (voyage-a) against legacy SSC outcomes (voyage-b), incorporating sales funnel attrition and realistic booking behavior.

- **Next Step**: Run bootstrapping experiments to identify the best-performing coefficients, which will be used as the treatment group in the upcoming A/B test.

Details:

I have built the code infrastructure to perform bootstrapping to determine the most optimal coefficients for our top-suite pricing algorithm. The bootstrapping code will test the performance of different coefficient sets by comparing the hypothetical results of our algorithm to traditional SSC revenue management methods. Each voyage coefficient will test 10 “voyage pairs”. The iterations of which are described below. The optimal set of coefficients will be utilized for the experimental group in our upcoming ab test. I plan on commencing bootstrapping tomorrow/Monday (contingent on my reserve requirements).

**Bootstrapping setup**

Set up “voyage-a” and “voyage-b”. Each voyage will have 10 “cabins” divided into 5 category codes of increasing priority (like SSC top-suites). Voyage-a represents novel prices, set by our top-suite pricing algorithm, voyage-b represents traditional SSC voyage-booking practices.

Divide booking period into 10 discrete time-bins, corresponding to 10-week intervals inside the 100 to 0 WTS SSC booking window.

Simulate “attempted bookings” for bin10 using binomial distributions. Binomial distributions will utilize booking probabilities derived from a bin’s corresponding booking window (e.g., bin10 = 100-91 WTS) and the number of simulations will correspond to empty cabins on voyage-a (e.g., 10 simulations for bin10).

For each “attempted booking”:

Draw a cabin purchase from 2024-2025 SSC top-suite revenue data

Automatically fill one empty cabin in voyage-b. Report revenue for “booked cabin” as the revenue paid by the actual customer

Use pre-determined passenger assumptions (see below) to assign data point to the correct cabin and report revenue as the cabin asking price, determined by top-suite pricing algorithm. If data point assumptions do not align with cabin price points, discard drawing and leave cabins empty. This discarded drawing represents sales funnel attrition.

Repeat steps a-c for all attempted bookings.

Repeat steps 3 and 4 for nine remaining time bins, or until all voyage-a cabins are filled. For subsequent time bins, the number of simulated attempted bookings will be **total cabins – successful bookings **for voyage-a.

Aagam S.

PCP Pricing Automation

**RCI | PCP2 | CRF Automation - Apply Business Rules, Validation, and Production Deployment for Automated Pricing Pipeline**

**Overview:**

- CRF Automation Foundation: Built core configuration and data tables to support the multi-step CRF process, starting with the Offering stage (3 weeks pre-sale).

- Offering Layer Progress: Identified and flagged relevant sailings (primary, RBC, PCC) and advanced summary statistics required for the CRF Offering.

- Product-Level Automation (Waterpark): Developed an initial automated version of the Waterpark CRF with preliminary outputs generated; currently undergoing QC and business validation (Mateo).

- Next Step: Finalize Waterpark automation and align outputs with existing manual processes before broader rollout across other product teams.

**Details:**

This week, I began working on building the foundational configuration and data tables required for CRF automation. The CRF process is multi-step, starting with the CRF Offering, which is created three weeks in advance. This step involves pulling the relevant sailings for the sale, including RBC and PCC sailings, along with generating summary statistics for the flash sale.

My focus this week was on completing the CRF Offering which includes identifying and flagging the appropriate sailings (sailing in question, RBC, and PCC), as well as progressing on the summary statistics needed to complete the CRF Offering.

Once the CRF Offering is finalized, each product team follows its own process to determine discounts and populate the respective tabs. For this week, my primary focus is on the Waterpark product. I’ve taken an initial pass at automating the Waterpark CRF and have generated preliminary results. I plan to further QC these results and aim to close this out by the end of the week. Additionally, I will be validating the Waterpark CRF outputs with the business team (Mateo) to ensure alignment with their existing manual process.

Ignacio V.

PCP Pricing Automation

Overview

- **Data & Feature Store Stabilization**: Identified and resolved critical issues in the beverage PRE feature store (nulls, duplicates), requiring additional debugging to ensure reliable model training inputs.

- **Model Architecture Upgrade**: Rebuilt the model from a simple linear MNL Beverage approach to a more advanced LightGBM ranking framework, capturing cross-product interactions and predicting both purchase probabilities and no-purchase behavior.

- **Segmentation Strategy**: Implemented dual-model approach (with vs. without clickstream data), with potential expansion to more granular models by product group depending on performance.

- **Robust Training Framework**: Integrated diverse data sources (clickstream, transactions, historical propensities) with temporal cross-validation, session-based modeling, and staged hyperparameter tuning using Optuna.

- **Business Alignment & Collaboration**: Ongoing coordination across DS, BI, and business stakeholders to refine use cases (QA layer, demand/dilution models, clickstream integration) and ensure alignment for CEL and RCI Beverage PRE initiatives.

Details

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

Srilekha

CEL Rev mgmt.

**CEL| Integrate Elasticities into Current Price Change Logic**

**Overview:**

  Elasticity Integration Completed: Deployed the new elasticity-based logic into the current price change framework, generated recommendation scenarios (3% and 5%), and validated compatibility without requiring downstream notebook changes.

  Comparison & Evaluation Framework Built: Created a consolidated output table across the current and new models, preserving apples-to-apples comparison and enabling sailing-level review of recommendation differences.

  Performance Monitoring Gap Identified: Flagged that actual bookings are not currently stored in the archive table, creating a post-production validation gap that will need to be solved through another source (e.g., weekly features table).

  Early Recommendation Pattern Observed: Histogram analysis shows the new models produce a higher share of near-zero/no-change recommendations, which appears directionally consistent with current analyst action files and business context.

  Promo Recommendation & Benchmarking Improvements: Delivered a sample “exciting deals” promo recommendation file with positive analyst feedback, improved Power BI readiness, tightened SPI/booked-position benchmarking precision, and resolved several data quality issues while continuing to investigate null booked-position cases.

**Details:**

**Status**: This ticket is complete as of **06/04/2026**

**Deliverables**:

Generated price change recommendations using current model’s elasticity values, reviewed updated demand forecast output table s with Evan, tested compatibility without any downstream changes in the price change notebook, replaced null elasticities in the new model with -1 cap and made adjustments for smoother integration.

Identified a key gap in performance tracking after this new model goes into production : actual bookings are not stored in the price change archive table due to absence in the demand forecast output table; discussed options to source actuals (e.g., weekly features table ) for post production to validate the performance of the model to see how its performed .

Produced price change recommendations for both 3% and 5% scenarios before applying business rules, creating a consistent framework for evaluation.

Built a consolidated table combining outputs from the current model and new elasticity-based models (3% and 5%), retaining the 3% scenario for apples-to-apples comparison; stored all prediction outputs (y_preds, p_need) so that lamis can pick sailing level examples to demonstrate price change recs difference across these models

Provided histogram analysis of % price changes across all models (as shown above): distributions is similar, but the new models (3% and 5%) show a higher concentration of near-zero/no-change recommendations compared to the current model; if the analyst pre-action file already contains many “no price change” actions for the week, the higher share of zero-change recommendations in the new models is reasonable and consistent with business context.

**Potential future issue**: None

**CEL| Actual Price Paid JUNE**

Created a sample exciting deals promo recommendation file for last week promo recs and shared it with analysts through Monica received positive feedback.

Working on improving the recommendation file so it can be used in Power BI, based on analyst requirements.

Updated the SPI benchmarking approach by moving from broader WTS buckets to exact WTS-level grouping to make comparisons more precise.

Improved the accuracy of booked position benchmarks by tightening the ranges, making it easier to spot under- and over-performing sailings and recommend promos for those sailings

Identified and fixed data quality issues, including duplicates from the SPI table and other inconsistencies affecting the results.

Investigating cases where booked position is showing as null for some rows and working to find the root cause.

Ben F.

**IBP:**

**1. Headlines — Decisions & Forward Momentum**

**SteerCo (June 3) approved rollout to Summit.**** ****Formal GO to expand the IBP pilot onto its next vessel; execution planning underway.**

**Fleetwide rollout planning requested.**** ****Laura has asked to meet within two weeks to build a plan to take the IBP Pilot fleetwide across both Celebrity and Royal. We are assembling the pilot-readiness assessment, dependency map, and resourcing/timeline to support it.**** *****This is the week's most significant signal — the pilot is being pulled toward a multi-brand program.***

**2. The Week at a Glance**

**32 pull requests merged. Two major systems reached production, the flagship Marine forecasting model completed validation and documentation, and six production fixes shipped.**

**3. Flagship — Marine Consumables Demand Model**

**We were asked to forecast monthly consumption for 109,214 ship×product pairs across 46 vessels (31 Royal Caribbean + 15 Celebrity; Silversea pending data acquisition) and hit <40% median error, measured the same way as the Hotel F&B model. We met and beat it — and produced a peer-review-grade account of *****why*****: an IEEE-format technical paper (388 paragraphs, 11 figures, 33 tables) ****, and a plain-English stakeholder summary **** all reproducible from code.**

**The core idea. Marine spare-parts demand is intermittent and failure-driven — a part is consumed when *****that***** part on *****that***** ship fails — so the model forecasts each pair from its own consumption history, not from a machine-learning model pooled across pairs. ****Its primary output is a single point forecast: a low percentile (~40th, deliberately below the average) of the pair's recent active months. It is set low *****on purpose***** — on this mostly-zero, spiky demand the accuracy metric is minimized by a low quantile, not the average.**

**The paper's design principle is to match each job to the method that is mathematically best for it — and the replenishment decision needs *****three***** distinct things:**

**The point forecast**** ****(the expected "typical month") ****—**** the per-pair low quantile above, refined through Phases 1****–****3.**

**An ordering gate (Phase 4)**** ****— ****a machine-learning classifier that zeroes the order for pairs unlikely to consume next month, curbing over-ordering on dormant items.**

**A safety-stock tail**** ****—**** because the point deliberately under-forecasts, order quantities for**** *****sparse***** ****parts are set from a high quantile (q90/q95) estimated by**** *****pooling***** ****across similar parts, which a part's own thin history can't supply.**

**It is not "forecast low / order from the tail" as two interchangeable numbers — it is one deliberately-low point forecast as the headline output, with an ordering gate and a pooled safety-stock tail as the two scoped machine-learning components that turn that forecast into a sound order.**

**Mechanically, the point forecast and ordering gate run as four phases, with the safety-stock tail alongside:**

***Alongside the four phases:***** a safety-stock tail — a pooled machine-learning model estimates a high quantile (q90/q95) to set order quantities for sparse parts, since the deliberately-low point forecast would otherwise under-stock. (A parallel component, not a sequential phase.)**

**Governance note: generative AI is used only to classify part codes *****offline*****; its output is frozen to a table and consumed deterministically — no language model runs in the production forecast path.**

**The honest result — two metrics, measuring different things (see *****Appendix A***** for how each is calculated):**

**Point accuracy — MdAPE: 25.0%**** ****median error on held-out months (vs the 28% benchmark; the simpler predecessor scored 29.3% vs a 38.5% baseline).**** *****MdAPE moves with the cohort measured — the broad active catalogue reads ~28%, the genuinely hard always-active pairs ~50% — so every comparison is run on a fixed cohort.***

**Volume error — WAPE: ~57–65%**** ****at the monthly per-pair grain. WAPE is a**** *****different, volume-weighted***** ****metric — not comparable to the 25% figure, and not "high" merely for being a larger number. In absolute terms it is a large error, but it reflects the**** ****difficulty of the demand, not a weak model: it is the lowest WAPE of any method tested and sits near the irreducible floor ****—**** even a hindsight oracle hits ~92% on**** ****the lumpy majority of**** ****pairs. It also**** ****shrinks at the grain that drives provisioning**** ****—**** ~38% aggregated to the quarter, ~31% in the dense Caribbean season ****—**** and the residual timing error is buffered by the safety-stock tail (order bias ≈ 1.0).**

**Two findings worth carrying to leadership:**

**We rigorously tested machine learning and it lost on accuracy**** ****—**** across the full feature store, advanced**** ****objectives, and Gen-AI features, pooled ML never beat the simple per-pair quantile at predicting quantities. Where ML and Gen-AI**** *****do***** ****earn their place is narrow and deliberate:**** ****generative AI**** ****classifies the opaque part codes (the semantic grouping behind P3), and**** ****machine learning**** ****fills two scoped niches ****—**** the**** ****activity gate**** ****and the**** ****safety-stock tail.**

**The data is the ceiling, not the model.**** ****Further gains require new**** *****signal***** ****—**** firm PO lead times, dry-dock / maintenance calendars, voyage itineraries — i.e. a**** ****data-acquisition initiative, not an algorithm project.**

**Status: validated and documented; not yet productionized. Remaining work is to schedule it for testing and complete final full-pipeline (NB01→NB19) validation before cutover.**

**4. Two Systems Reached Production**

**Supply Model refactor (#492, merged June 4).**** ****Two oversized monolith notebooks were split into orchestrated, deterministic segments, paired-validated against the originals, and cut over in production (both Step 1 and Step 2). Largest file dropped from 2,565 to 619 lines (****−****76%); now auditable and reproducible.**** ****Weekly production pipeline compute time**** ****reduced**** ****~10 hours.**

**SSC MMS→Crunchtime migration (completed end-to-end).**** ****A surrogate item key now flows through consumption, demand modeling, dashboards, finance, and reporting, with a single orchestrator replacing four separate pipeline activities. This closed a 100% silent data-loss gap for Silver Shadow created when the legacy item view was decommissioned post-acquisition.**

**5. CocoCay Forecast Guardrail — Protecting Provisioning on BEYOND's New CocoCay Itinerary**

**Why we built it. Celebrity BEYOND has been redeployed to call Perfect Day at CocoCay regularly for ~6 months. CocoCay is a beach day — guests eat substantially more grilled and beach-picnic food, and the ship loads that extra at the voyage level. Our demand model has no concept of CocoCay: it forecasts from recent consumption trends, so it systematically under-forecasts beach-food items on these sailings. We did test including CocoCay as a feature in our model build in December but it was selected in none of our 5 time-series periods. With CocoCay now a repeated call, that gap would recur on many upcoming voyages — a real under-provisioning risk on a high-visibility new deployment that has focus from leadership.**

**What we found. Comparing CocoCay sailings against comparable non-CocoCay sailings of the same length (at the voyage-total level, since the extra is loaded per voyage), the chef's CocoCay items split into two groups:**

**Group A — consumed on the beach day (handled now).**** ****Clear, measurable lift: Beef Hot Dog +71%, Chicken Leg Quarter +50%, and a beach-picnic basket (buns, ice-cream mix & cones, corn, condiments, American cheese, tortillas, ****melon, lemonade) ranging**** ****roughly +35% to +330%. 37 items, each qualified from its own history.**

**Group B — loaded but carried over (planned follow-up).**** ****Frozen proteins (beef round, drumstick, chicken breast) are loaded extra on the dedicated "BY COCOCAY GUEST FOOD" requisition, but the surplus carries to the next voyage, so measured consumption looks flat. These need the**** ****requisition feed connected**** ****to forecast directly ****—**** a tracked data-pipeline addition, not part of this guardrail.**

**How it works (and why it's safe). For the 40 eligible products on Beyond, the guardrail learns the real CocoCay uplift from history, subtracts the lift the model already captures, and raises the forecast by only the gap — capped at +40%. The eligible products are not hard coded and detected from uplift history of past voyages visiting CocoCay relative to non-CocoCay sailings and most of the products identified by the Chef were detected automaticaly in this architecture. Crucially it self-decays: as the weekly-retrained model learns CocoCay from each completed sailing, the gap shrinks and the correction returns to 1.0 on its own — no permanent over-forecasting, nothing to remember to switch off. It is forecast-only (never touches recorded actuals), food-only, data-driven (no hand-maintained list), and every correction factor is logged for monitoring.**

**Status. Moving it from monitoring into production is pending and should be delivered on 6/5/2026.**

**6. Looking Ahead — Next-Generation HF&B Demand Model (RCI / CCI / SSC)**

**A design proposal is on the table to evolve the Hotel F&B demand model from its current independent per-SKU regression to a discrete-choice / share-allocation structure with a new venue (outlet) grain. The reframe forecasts demand as *****population × category rate × within-category share × portion*****, rather than predicting each SKU in isolation.**

**Why. Today's model is accurate on established products but has four structural limits it cannot solve by tuning:**

**No substitution or budget coherence**** ****—**** per-SKU forecasts**** ****don't**** ****respect that guests choose**** *****among***** ****items within a fixed appetite.**

**Venue is collapsed before modeling**** ****—**** the model never sees outlet structure, so it**** ****can't**** ****set per-venue par levels.**

**Cold start is unsolved**** ****—**** a new SKU or new ship (Icon/Edge class) has no history to lean on.**

**It trains on stockout-censored consumption**** ****—**** items that ran out**** ****look**** ****like**** ****low**** ****demand, perpetuating blind spots.**

**What it buys. Coherent substitution (a true cross-elasticity matrix), attribute-based cold-start for new SKUs/ships, a sum-to-population guarantee, venue-level par levels and assortment what-ifs — and the headline inventory win: because substitutes are negatively correlated by construction, pooled safety stock is far lower than the sum of independent buffers at equal service level, meaning less inventory and weight carried. It is brand-general (RCI / CCI / luxury / expedition) with brand-differentiated parameters, reuses the existing V6 feature and SHAP investment (now explaining choice utilities), and preserves the current forecast contract — the venue grain is additive, reconciled up to the voyage total provisioning actually consumes.**

**Plan. A phased, gated program (P0→P5): instrument the data (choice-sets, stockout flags, SKU attributes), prove the choice layer beats the baseline at ship grain *****on decision cost***** before investing in venue grain, then add substitution depth, a portfolio-newsvendor loadout, and finally brand / new-ship transfer. Every phase runs champion/challenger in shadow, gated on decision-cost metrics (waste %, stockout rate) rather than RMSE, with strict voyage-level validation.**

**Status: proposal / documentation for review **** and **** ** 
**Open items for sign-off: the stockout/availability feed, the SKU attribute master, party-level keying for beverages, and the agreed under-/over-stock cost ratios for the newsvendor gate.**

**7. Production Fixes (Risk Mitigation)**

**Silversea consumption inflation**** ****—**** inverted waste-exclusion filter**** ****was counting**** ****Spoilage/Breakage as consumption (~302K rows full-history; all Silversea ships 2.7****–****4.0%). Corrected.**

**SHAP demand model break**** ****—**** restored a dropped key column.**

**View-creation failure**** ****—**** fixed an ADF service-principal ownership block.**

**Pipeline resilience**** ****—**** added idempotent retry on transient failures.**

**MLS + visualization fixes**** ****—**** corrected MLS table paths, a Z-Order error, and two broken dashboard views.**

**8. Next Steps & Asks**

**Prepare for Laura's fleetwide planning meeting (<2 weeks)**** ****— ****readiness assessment, Celebrity/Royal dependency map, resourcing/timeline.**

**Execute Summit rollout**** ****per**** ****SteerCo**** ****approval.**

**Productionize the Marine model**** ****—**** schedule testing and complete final full-pipeline validation before cutover.**

**Continue code refactoring work on the Finance Tool. **

**Kick off Phase 0 of the next-gen HF&B choice model**** ****(data instrumentation) pending design review.**

**Appendix A — How We Measure Accuracy in Marine Consumables: WAPE vs. MdAPE**

**The two metrics measure genuinely different things, which is why they read so differently on the same forecast.**

**MdAPE — Median Absolute Percentage Error (the legacy Hotel F&B metric)**

**For each ship×product pair, compute the percentage miss:**** ****|forecast ****−**** actual| ****÷**** actual.**

**Conventions: a correctly predicted zero scores**** ****0%; an over-forecast on a pair that was truly zero is**** ****dropped.**

**MdAPE = the median of those per-pair percentages.**

***Answers:***** ****"For a**** ****typical pair, how**** ****far off**** ****is the forecast?" Every pair counts equally regardless of size; robust to the spiky tail.**** ****Gameable:**** ****since correct zeros score 0% and most pairs are zero in any month, a near-zero forecast scores well while under-ordering.**

**WAPE — Weighted Absolute Percentage Error (New Error Metric for Marine Consumables)**

**WAPE = Σ|forecast − actual| ÷ Σ actual**** ****—**** total mis-forecast units divided by total consumed units, across all pairs.**

**One pooled ratio.**** ****High-volume pairs dominate; zero-actual pairs add nothing to the denominator, so you cannot improve it by predicting zeros.**

**Reported with**** ****bias = ****Σ**** forecast ****÷**** ****Σ**** actual**** ****(>1 = over-ordering, <1 = under-ordering).**

***Answers:***** ****"Across the**** ****whole book, what fraction of consumed volume did we get wrong?" ****— ****the**** ****quantity**** ****replenishment depends on.**

**Worked example — 3 pairs. Actuals 100, 1, 0; forecasts 80, 2, 0.**

**MdAPE**** ****=**** ****median(0%, 20%, 100%) =**** ****20%**

**WAPE**** ****= (20 + 1 + 0) ****÷**** (100 + 1 + 0) =**** ****20.8%**

**Pair B is a 100% miss, but it's 1 unit out of 101 — it barely moves WAPE, yet it weighs as heavily as the 100-unit pair in MdAPE. MdAPE counts *****pairs*****; WAPE counts *****units*****.**

**Why WAPE is the right yardstick for Marine Consumables. A performance metric is only trustworthy if a better score genuinely means a better model — and on intermittent spare-parts demand, MdAPE fails that test while WAPE passes it:**

**It can't be gamed by the degenerate forecast this data invites.**** ****Most pairs are zero in any month, and**** ****MdAPE**** *****rewards***** ****forecasting zero. A near-zero forecaster — useless for ordering — scores beautifully on MdAPE (the model's own activity gate drives MdAPE to 0.0% this way), while WAPE keeps reflecting real ordering quality because predicting zeros earns nothing against a total-volume denominator.**

**It measures error where the units and the money are.**** ****The book is bimodal ****—**** a small head of operational consumables carries most volume; a long maintenance tail carries the pair count but little volume. WAPE**** ****weights by**** ****units, scoring the model**** ****where**** ****purchasing dollars, working capital, and weight sit;**** ****MdAPE**** ****is steered by the low-stakes tail.**

**It matches the decision.**** ****Provisioning cares about**** ****total**** ****quantity bought vs. consumed. WAPE answers that directly, and bias flags**** ****systematic**** ****over-/under-ordering.**

**It's well-behaved on a zero-heavy book**** ****(a ratio of sums never divides by a zero actual the way MAPE does) and**** ****aggregates cleanly to any grain**** ****—**** pair, voyage, quarter, season, fleet ****—**** so the same metric reports both the monthly per-pair error and the voyage-level error provisioning uses.**

**Camila A.**

**IBP**** – Supply Chain****:** 
Recovered silently dropped non-DRY load types (FROZEN, CHILL, HAZMAT, BOND) from order-creation output across all 44 ships — a structural undercount now resolved.

fail-fast guard when yesterday's reconcile data is absent and ensuring the live SharePoint file is pushed before the checkpoint notebook can error out.

seasonality guardrail for BY and SM: The seasonality guardrail computes a trend factor per ship and calendar month by dividing the 2025 demand benchmark by the 2024 benchmark, then uses that trend to set a corridor buffer between $0.40 and $0.60 per APD. Months where demand is growing get a larger buffer ($0.60) while declining months get a smaller one ($0.40), creating variable savings that reflect real year-over-year demand patterns rather than a flat fixed number. Every sailing's prediction is then moved into the corridor defined by budget APD − buffer (ceiling) and budget APD − $0.60 (floor): predictions above the ceiling are cut down, predictions already below the floor are boosted up by at most 15%, and predictions already inside the corridor are left unchanged. The result is that SUMMIT and BEYOND predictions always land $0.40–$0.60 below the Finance budget APD which generates true savings per sailing.

**Nico T.**

**IBP:**  **SSC Consumption and Prediction Ratio Adjustments**

· In Progress

**Completed:**

**Resolved **ITEM_CODE type mismatch in run_adjusted_step_2 (Thu 5/29): Hit an error running the unpivoted_table_adjusted file for the unadjusted crew variant. The step that replaces actual consumption with crew-adjusted consumptions was failing due to a column type mismatch — actuals_df has ITEM_CODE as STRING (e.g., "702047") while consumption_actuals_monthly has it as ARRAY<STRING> (e.g., ["702047-M", "702047-L"]). Investigated the dataset origin to ensure consumption is allocated properly across an item code's variants.

**Successfully ran **run_adjusted_step_2 for two variants (Tue 6/2): After confirming with Paige that the variants PRDS_MODIFIED_SIMILAR and PRDS_MODIFIED_SIMILAR_CREW were needed, ran the step successfully. Documented the logic for how: (1) historical demand is replaced with variant-adjusted consumption, (2) forecast is distributed based on average crew count staffing, and (3) historical cost is filled-forward to future forecasts.

**Documented **run_adjusted_step_3 logic (Wed 6/3): Ran through and documented the full logic for the two variants. For _CREW variants: reads the backtest archival tables, applies the product variant transformation (grouping products like Men's White Polo M/L → Men's White Polo), sums predictions across the group, then distributes proportionally according to crew consumption ratios (e.g., Towel Prediction 100; Waiter: 30; Housekeeper: 10 → Towels [Waiter]: 75; Towels [Housekeeper]: 25). For non-CREW variants: same product grouping/summing but without the crew distribution step.

**Documented **run_adjusted_step_4 logic & found commented-out code (Wed 6/3): Traced the full pipeline: (1) Move_Current_Month_To_Archival_Historical_Load.py unions current variant-specific forecast to archival tables and recalculates variance, writing to SSC_UNIFORM_UNPIVOTED_DEMAND_FORECAST_GEN2_BACKTESTED_TRAINING_DATES; (2) Move_Current_Month_Demand_To_Archive_Delta_Table.py deduplicates on MAX(MODEL_TRAINING_DATE) and appends the latest monthly snapshot — **but the append step is commented out**, flagged to Camila for clarification on intent.

**Found outdated table reference bug in **run_adjusted_tables_2 (Thu 6/4): Discovered that prds_modified_unpivoted_table_similar was reading from an outdated table SSC_UNIFORM_UNPIVOTED_DEMAND_FORECAST_10, causing downstream steps to disregard the latest MODEL_TRAINING_DATES. After re-running run_adjusted_tables_2.py, the output should now include the last two MODEL_TRAINING_DATES, though it's unclear whether intermediate dates (2025-10 through 2026-04) will be present.

**Ongoing:**

**Validating outputs for re-run**: Confirming that the corrected table reference produces the expected MODEL_TRAINING_DATES in the variant outputs.

**MOT Data Calculation Change**

· Done ✅

**Completed:**

**Root-caused Summit PCD/enrichment mismatches (Thu 5/29)**: Traced the 5 failed consistency checks (Summit 07/2026 and 08/2026) to a difference in enrichment source tables — MOT_Value_Comparison (ship-level) uses prd_gold.ibp.spend_report as its basis while MOT_Value_Comparison_Monthly (month-level) uses prd_silver.ibp.v_revenue_forecast. Some sailings exist in v_revenue_forecast but not in spend_report, explaining the divergence. Changed the enrichment basis for the monthly table from v_revenue_forecast to spend_report to ensure a consistent ratio calculation.

**Built and delivered two new MOT tables (Tue 6/2)**:

**Table 1** (new_metrics_purchase_order_mot_spend_base_monthly_pilot): Grain of 1 row per Ship × Month × Product_Name_Number, aggregating SUM(MOT_Value)

**Table 2** (new_metrics_purchase_order_mot_cruise_mot_monthly_agg): Grain of 1 row per Ship × Month, aggregating SUM(MOT_Value) and SUM(PCD_Value)

**Add SSC Vendor Code Mapping**

· Done ✅

**Completed:**

**Vendor code mapping delivered (Thu 5/29)**: Added the SSC_Vendor_Code column to dev_datascience.ibp_sso.spend_report_adj by mapping Crunch Time Supplier Code (SUPPLY_CODE) to MMS Supplier Code, with no new rows introduced. Story moved to Done.

**Caleb**

**Customer**** Lifetime Value (CLV)**

Completed

Met with Jessica from Transformation Hub to optimize our cost allocation ingestion and EPM integration.

Decided to ingest a transformed EPM output directly into our pipeline, which will contain the nearest pax-level allocation Catalyst provides (voyage/market/channel).

Waiting on those tables to be built, but the timeline aligns with our CLV build.

Built violin plots using KDE local minima to assign bucketed APD distributions, enabling a view into top-APD RCG guests and their corresponding income and wealth profiles.

In Progress

Validating Data Solutions' initial POC table, which replicates our ideal source structure for the final productionized data asset.

Validating Revenue Planning's updated 2025 test tables — revamped with Lissette's help to use correct channel tagging, now achieving a <1% delta on pax and NTR to VCAP MICE. Once validated, the test table will flow to stg2 for direct ingestion by our pipeline.

**Caleb**

**CLV:**** Sailing Environment**

Completed

Aligned with Neila, Eddie, and Ben on Corp Strategy's June deadline goal:

a yield and revenue forecast by brand × region for 2026–2031, with a confidence range (not a point estimate) and a directional signal on whether RCG is likely to over- or underperform vs. our current internal forecast.

Coordinated with the working team to unify data sources and approach.

In Progress

Acquiring relevant data for integration into the existing pipeline: Strategy Plan estimates from previous years, industry capacity deployment blocking file, and the industry fleet model.

**Mireille**** T.**

**Contact Center:** 
**Focus of the Week**

This week focused on **end-to-end testing and stabilization of the 30-minute Model version** of the “Run Your Own FTE” simulator.

The objective was to ensure that the 30-minute mode runs consistently across all steps — from inputs through final results — and to identify any remaining gaps before integration into the production workflow.

**Key Issues Identified and Fixed**

Several issues identified during testing were resolved:

**Data structure mismatch**

Fixed query logic to correctly derive 30-minute slots from separate hour and minute fields

**Experiment version loading**

Ensured experiment names are passed through all steps so the correct data is loaded

**One-time data write failure**

Confirmed as a non-recurring issue after a successful re-save

➡️ **Result:** 
System behavior is now **stable and consistent across scenarios**

**What Was Achieved This Week**

**1. End-to-End Validation**

The 30-minute workflow was successfully tested across all screens:

Schedule (48 slots/day)

Assumptions

Call distribution

Joined dataset

Erlang A engine

Output structure

➡️ **Result:**

The model runs successfully across the full workflow

However, **an issue was identified in the FTE results**, with outputs differing from expected values

Root cause analysis is currently in progress

To validate the core model independently, a **backtest was run in Databricks**:

All functions and datasets feeding the 30-minute model were verified

**Results produced expected FTE outputs**

➡️ This confirms that the issue is likely **within the app layer or integration**, not the core model logic

**Testing Summary (June 04)**

**Additional Development in Progress**

Work has started on **multi-dimensional scenario integration** (≈30% completed):

Enables running multiple scenarios for the same LOB using:

Different assumptions

Different forecast tables

Different office hours

Target capability:

Allow users to **visualize and compare multiple scenarios side by side** within the app

**Next Steps**

Fix the **FTE output discrepancy** (high priority)

Complete final validation of the **Compare tab** (cross-resolution scenarios)

Proceed with **integration of the 30-minute mode** into the production workflow

Enable **combined LOB scenarios** (e.g., *Casino = Casino_Sales + Casino_Services*):

Build required datasets

Align with North America team usage (combined planning approach)

Extend to similar cases (e.g., RES_Sales + RES_Services)

**Bottom Line**

The 30-minute workflow is **functionally validated end to end**

Core model logic is **confirmed accurate (via Databricks backtesting)**

Remaining work is focused on:

Resolving **FTE output discrepancies within the app**

Completing **integration and advanced scenario capabilities**

➡️ The project is **close to integration readiness**, with targeted fixes underway.

**Executive Summary — June 04, 2026**

30-minute (30mn) workflow successfully tested across all steps

Core model validated independently (Databricks backtest confirms expected results)

FTE output inconsistency detected within the app; investigation in progress

Key reliability fixes implemented (data structure, experiment handling, data writes)

Integration preparation ongoing, with final validation and fixes as next priorities

**Carlos **

**E-Commerce:** Customer Targeting

- Added incremental data ingestion for clickstream data.

- Finished prediction pipeline for journey stage model, (pending of stage holder revision)

**Bao**

**E-Commerce:** Customer Targeting
**Completed This Week**

Ran a full disparate impact audit across all scoring models (BP, PCP, PHML, Uplift, NBO) to assess compliance with the NY AI price discrimination law. All statistical tests were completed and interpreted, covering age proxies, neighborhood wealth proxies, lifestyle/spending proxies, and geographic features. A 11-slide presentation summarizing findings and recommended remediations has been structured and is being built for legal and stakeholder review.

Used the model drift dashboard to measure the impact of the recently integrated app usage features on model performance. The dashboard confirmed meaningful AUC lifts across multiple model categories following the app feature integration.

**In Progress**

**NY AI Compliance Audit:** Presentation build, protected feature removal from training pipeline, and legal review are the remaining steps before NY deployment.

**Model Drift Dashboard:** Active and in use. Ongoing work to add broader monitoring coverage across all model categories.

**Clickstream Feature Implementation:** EDA is complete for 5 new clickstream features with confirmed performance gains on PG models. Three targeted code changes are planned for implementation.

**Clickstream Pipeline Fix:** Root cause confirmed. The clickstream ingestion job has never been wired into the weekly ETL pipeline, meaning all existing clickstream features run on stale data. Fix is scoped and ready to implement.

**PCP App Usage Features:** Development has begun on 4 new features leveraging pre-cruise app engagement, none of which are currently used in the PCP models:

Whether the guest is actively using pre-cruise app features on their current booking

How far in advance they first engaged with the app before their sail date

Recency of their last app interaction relative to sailing

Duration of sustained app engagement across sessions
