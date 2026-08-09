Ayon

Win-on-Waste WOW Update 9/11:

Provided extensive support to all 26 ships during FPMS rollout.

Implemented multiple hotfixes in MDR across all modeling utilities to correct forecast inaccuracies, addressing both inflated and low item forecasts by centering predictions around average consumption while accounting for real and random patterns in historical data.

Applied code optimizations in key modules to reduce processing time and improve pipeline efficiency.

Conducted technical briefings with chefs to demonstrate how geographic location data was leveraged to enhance forecast

Ben Fowler

Contact Center Lead Prioritization  (cross-portfolio only)

Context: The following work was motivated by a failure this week in production, where Lead Prioritization failed on Tuesday and was down 9 hours due to the job being run on a Data Scientist’s work cluster and a perfect storm that the user account was temporarily disabled due to a Data Scientist’s international travel and near a restricted zone (Nigeria).
Alignment: No production jobs on personal compute; all production compute must use Databricks Job Clusters managed by a Service Principal.
Access: Glen-Erik is provisioning Databricks Service Principal access; ADF pipelines already use Service Principal via Managed Service Identity.
Version control: Follow-up scheduled with Glen-Erik to adopt Databricks Asset Bundles for pipeline change management.
Adoption: All team members are either on Job Clusters or actively migrating.
Update: Supply Chain ADF Job Cluster test failed due to Unity Catalog access to dev_datascience; working with Glen-Erik to resolve.
Next: Parameterize table read/write code with environment variables to enable promotion to prod without code edits.

Ben & Camila

Supply Chain / IBP
Completed:
Delivered spend regions to Yan (derive country from first two letters of city code; map to region via pycountry-convert).
RCI/CEL order creation: corrected inbound orders and consumption calculations to reflect actual quantities needed.
Added CocoCay to HF&B reports; results will flow when Ben runs the pipeline.

Ben & Camila

Supply Chain / IBP
In progress:
Update pivoted files to align with voyage files (addresses maiden-voyage zeros).
Job Cluster migration via ADF Service Principal: Testing on my ADF pipeline failed due to inability to read from the dev_datascience catalog in Unity Catalog. Working with Glen-Erik to resolve the catalog access issue.
Next:
After issue is resolved and tests pass, roll out Job Cluster migration to RCI/CCI HF&B, Silversea, and Finance Tool pipelines.
Parameterize notebooks ahead of production ADF migration.
Update Health and Medical Databricks pipelines to use Service Principal (remove user account dependency).

Cihan

PCP Pricing Automation (Onboard Revenue)
Completed:
Demand model feature identification; feature store updated with WTS bins specific to waterpark demand.
Waterpark repeater analysis for Royal Product:
Finding: ~14% of waterpark guests are repeaters, stable over time.
Context: No evidence of a decline in repeater participation post-Hideaway Beach opening.

Cihan

PCP Pricing Automation (Onboard Revenue)

In progress:
Elasticity model for Water Park: feature engineering and data preparation.
Next:
Schedule and conduct brainstorming with Dave and Kevin on elasticity approach.
Build and validate the elasticity model based on workshop outcomes.

Cihan

Digital App (Community One)
Completed:
Classifier model deployed to production.
Developed ai_classify_rcg() advanced classification agent:
Supports user-selected models (e.g., OpenAI).
Accepts topic descriptions.
Constrains outputs to provided labels and mitigates hallucinations.
Adoption: Digital team is using the agent for ad hoc topic classification.
Next:
Meet with Jaime’s team to share the notebook and ensure maintainability.
Begin Qualtrics survey work with Jaime’s team.

Cihan

Digital App (Community One) — Guest Services Chatbot
Completed:
Validated metrics presented by Eunha to Star HD.
Next:
Add Star to the average chatbot adoption-rate visualization.
Update dashboard color scheme to align with Royal Caribbean brand.

Carlos

E-Commerce Customer Targeting
Completed:
Resolved Genie permissions error.
Expanded Databricks Consumer Dashboard (more decile options; optimized refresh rate).
Upgraded Databricks runtime 13.3 → 16.4 for reporting; resolved SHAP library conflicts (0.41.0 → 0.46.0).
Created and shared MLflow model management snippets.

Carlos

E-Commerce Customer Targeting

In progress:
Cost optimization of train/predict pipelines (route ingestion/reporting to lower-cost clusters).
Update production pipelines to comply with new Job Cluster policy.
Next:
Meet with e-commerce data science to integrate itinerary recommender into marketing models and plan the consumer transition-cause study.

Ben & Caleb

Customer Lifetime Value (CLV)
Completed:
Normalized value vs. LTR and sentiment analysis:
Within-category z-scoring of VALUE_INDEX_CABIN by CABIN_CATEGORY_CODE to create NORM_VALUE_CABIN.
LTR bucketing (Promoter 9–10; Passive 7–8; Detractor else).
Topic explosion; limited to top 50 topics.
Uplift (Promoter − Detractor) on NORM_VALUE_CABIN with n≥1,000 per class; Welch’s t-tests for top positives (p=0.27–0.68; not significant).
Pearson correlations between SENTIMENT_SCORE and NORM_VALUE_CABIN with n≥1,000; r≈0 to 0.051 (negligible).
Interpretation: Effect sizes are very small; topic sentiment is not a meaningful predictor of normalized cabin value at the topic–experience level. CASINO shows consistent negative uplift (detractors higher normalized value) and merits separate validation.
Prepared C-suite deck for Celebrity (Mon 9/15) focusing on 2–3 high-performing cohorts, including behaviors, summary stats (product/shorex preferences, DMA, NPS drivers, seasonality, value index), and associated marketing targeting strategies.

Ben & Caleb

Customer Lifetime Value (CLV)

In progress:
Combine Oracle and Alpha Databricks systems using Marimo notebooks; enhance connections; deepen understanding of casino flag, cabin linking, OBR categories.
Adjust logic inconsistencies for RCI cruise experience, casino cabin transfer, and casino flagging.
Develop automated checks for PAX, PCDs, and NTR.

Mirielle

Contact Center Lead Prioritization
Completed/In progress:
BKTOCX outbound lead scoring: Resolved ~7-hour production block by migrating compute off a personal account (with Eswar).
OFTOCX: Feature engineering for Royal and Celebrity is progressing.
Workforce Planning: Implementing save/edit functionality in the Streamlit app to persist user inputs and modified results.

Ben & Carlos

Customer Targeting (Journey Orchestration)
Completed:
Held calls with Salesforce regarding Journey Orchestration for guests; Ben also met with Salesforce individually on 9/11.
In progress:
Pending call with Braze.
Salesforce to schedule a follow-up call in two weeks with one of their contact center experts to explore leveraging their AI solutions (e.g., AgentForce) in the Contact Center.
Next:
Attend Salesforce follow-up; assess fit and integration considerations.
Proceed with Braze discussion once scheduled.

Kevin & Kartik

Loyalty:

Kartik presented initial findings on choice benefits to the Steerco. Early signs point to a lift in bookings for the treatment groups, but it is still too early to determine statistical significance. SteerCo has decided to test both CC spend and CC acquisition for the next pilot, although the data will not support a statistically significant test on acquisition due to low historic acquisition rates. POS data is still in UAT testing with the business. CEL UAT is progressing and close to completion. Will be following up with RCI today. The tier simulator is in progress of refactoring. This week the inputs to the simulator have been adjusted to reflect data corrections discovered during pilot testing. The next step on the simulator is configuring the tier calculator to use tier progression from the existing program, rather than the proposed spend based program.

Kevin & Ignacio

PCP Pricing Automation

We are still facing challenges getting promotion/pricing uploads tested in hybris lower environments. DS teams have built the data to digital requirements, but data is falling off. The working hypothesis is that there is an error in the Kafka transmission. Ignacio is working closely with digital and DE teams to resolve this quickly. In the meantime, he is also working closely with the business teams to make mass promotions simpler from a UX perspective. This week we met with Alex Correa to discuss Alaska ShoreX products. Cihan will be starting with a labeling and clustering exercise to simplify the data and draw initial insights. I will be presenting a shoreX playbook for discussion with the business in next week's alignment meeting. This playbook will center on business unlocks including bundling, SKU rationalization, pricing strategies accounting for substitutable demand with baskets, customer economics and targeting among others.

Erick & Parimala

Contact Center: Lead Scoring CTI:
- Last week the team managed to improve RCI CTI model performance. This week the team is focusing on refining the CEL CTI model as the conversions are still mediocre for CEL. Team is experimenting with introducing more recent 2025 data, different probability thresholds, experimenting the impacts of Call Transcripts, and finally iteratively validating feature importance to understand model impact.

Erick
Axiom - Medallia Reporting Automation
- Last week the team introduced the new Preliminary email report for both the ship/shoreside audience. Since then there have been 10+ users that have been added to the distribution including (Jay Schneider, Ed Artiles, and other VP/Directors). 
- Up until now the Medallia meta data extraction process has only processed survey responses greater than 100 characters. This week we started processing shorter responses (actively backfilling data, once complete will include in the reporting pipelines). 
- Received greenlight from Evan on new email format for Celebrity to highlight top 5 newly trending negative topics. This report is pending a few tweaks. Evan wants the a draft copy of the report early next week to see what August would have looked like. This report will be sent once a month.

Erick & Gaurav

Axiom - Thresholds modeling (Medallia)
- Gaurav is leading the effort in adapting the feature importances coming out of the Medallia Drivers model to create thresholds that can be used for alerting purposes. The idea is to inform the business about the key thresholds for each metric afterwhich there is an impact on NPS. Work continues.

Erick and Christian

PCP Product Recommendations 
- Several new initiatives are being explored including productionizing all parts of the existing recommender pipeline, implementing a Lakebase backend in prepartion of real time data updates, working on logic to implement product weighting based on business rules, and planning discussion on recommendations for non revenue products for the calendar.

**Reza Bahadori**

**MIAP**

Deployed new workflows for Hotel and HVAC in production, resulting in runtime reduction to approximately one-third to one-half of the previous duration.

Implemented new logic for deviation and expected power calculations in HVAC and Hotel areas.

Completed development of parallel pipeline for Machinery area and successfully tested it in QA; deployment to production is planned next.

Initiated automatic baseline definition for hull performance as requested by Nicola.

**Brendan Turpin**

**MIAP**

Created report of MIAP models and versions across all catalogs in Databricks

Created presentation on DynaTorch, our in-house built Dynamic Modeling framework, for bi-weekly sync with Dave

Attended mentorship circle meeting

Created script to delete models versions older than 30 days to prevent our Databricks account from going over the maximum limit of model versions; deleted around ~20k unnecessary model versions

Troubleshot multi-faceted issue with access to the MIAP REST API in GMO Prod

Resolved access issue with the Crosser job in Databricks; made changes to asset bundle to prevent this job from being executed in QA

Provided support to various members of the MIAP team, assisting with merge conflicts, mismatches between environments, code reviews, etc.

**Will Borges**

**MIAP**

Implemented stg model configuration in power plant

Testing implementation of STG models

Working on fix to outlier removal method causing issues in STG models. Current outlier removal method removes too many values not leaving enough for modeling

Documenting issues with both STG and GTG models

**Arya Cheeti**

**MIAP**

Reconfigured chiller analytics features and results to be able to handle null value cases to prevent divide by zero errors

Found a period in explorers data of null values and configured analytics to work alongside this

Added explorer of the seas to all the analytics config files, tested and pushed to prd

Worked on improving the accuracy of work order classifier

Fixed data saving bugs with fire incident classifier

Built graphs in GMO app for safety incidents

Replaced all analytics folders with new model search code

Added fire_safety_incidents in azure data storage

**Ramu ****Sirusanagandla**

**MIAP**

This Week -

Worked on the new Silver Eniram notebook, tested it in the development environment, and collaborated with the MLOps engineer to resolve blockers in QA.

Addressed the fix for the MIAP API, which was causing data delivery issues for all vendors.

Granted permissions to the Wärtsilä team for accessing the MIAP API.

Discussed all recent implementations for the MIAP API and Silver Analytics Notebook, including the addition of checkpointing mechanisms to enhance reliability.

Investigated issues with the Eniram API, which is not functioning as expected from the server side. Tested various scenarios and reached out to the Eniram team for assistance.

Next Week's Focus-

Resolve the ongoing Eniram API issues.

Move the new Silver Eniram notebook to QA and verify if all dashboards are populating correctly.

Fix issues identified in the QA environment, deploy updates to the MIAP API and Silver Analytics notebooks, and conduct thorough testing in QA.

**Mehdi ****Assefi**

**MIAP**

Fully integrated the regressor with the AI Agent for Symphony Revamp Analysiss.

Managed to extract features from vector search tool, mapped the "space", "items", "material", and "location" features to consistent clusters with the regressor. applied consistent encoder to the clusters, and made the regressor work properly with the resulted input.

I am working to run tests to compare the results and also making further improvements on the predictions.

**Mahshad Shariatnasab**

**MIAP**

Worked on a grid optimization problem to find the best itinerary for ships and ports based on various constraints. Implemented the solution in Python and conducted testing.

Created plots for ventilation fans on all ships to help identify anomalies in machinery.

Assisted a teammate in troubleshooting their code and data issues in the table.

Atefeh & Lamis

RCI Revenue Management: PRE:

Made continued progress to integration of elasticity 4.0, correcting the price change calculation to properly account for linear model outputs and point elasticities.

Atefeh & Lamis

RCI Revenue Management:

Track Optimization:

Applied a version of DART to elasticity 4.0 for volume forecasts. However, further work is required to fully integrate DART in elasticities. The new demand model is being used for track optimization and track shapes are closely matching business generated tracks, but there are necessary improvements to the pricing recommendations including accounting for residual errors.

Atefeh & Lamis

RCI Revenue Management: PRE Logic:

Updated the analysis by using the following: 4.0 model for elasticities for RCI, using all occupancies for both CEL and RCI, using the WTD expectations for the analysis, and analyzing the booking window where we beat or miss track consistently

Kevin

RCI Revenue Management: SPI:

Initial EDA results are continuing to be shared with business teams. The current focus is on analyzing cancellations by WTS with respect to booking time. Using SPI outputs we are analyzing track recommendations by meta and quarter vs current track and how we built in 24 and 25.

Michelle

RCI Revenue Management: Category Gapping

Sent over results for the entire fleet to Eddie for review last week. Met with Alexa on Tuesday, still awaiting feedback.

Srilekha

CEL Revenue Management: PRE:

Developed a more sensitive way to build WTS bins so that bins can be more precise during the prime booking window. This was a requirement from the business as they thought the spline based windows were too large and not capturing true price demand relationships, since pricing could be updated many times in the old windows.

Kevin

CEL Revenue Management: SPI:

Actively investigating over-normalization of SPI scoring model.

Michelle:

CEL Revenue Management: Category Gapping

Presented to the three product teams and all managers aligned on implementation. 3.0 will use all occupancies and net availability. Europe manager requested an additional view of a Med vs North sailing. Caribbean manager requested a comparison of a 6 vs 8 night sailing.

Aagam

CEL Revenue Management: MTRB/Baskets:

Sent MTRB baskets to Tristan for review, everything looked good except some new deployments weren’t picked up due to issues in the ICLSMD table. As a workaround, we’ll manually update the deployment table in DB with each new deployment. Waiting on Tristan to upload the table so I can run the analysis. Plan to push to PRD next week. This will create static baskets while proposing changes to the baskets based on new data.

Jesse

SSC Revenue Management: PRE

Considerable code refactoring to make the pipeline more robust and stable. Added configurations for different modeling algorithms based on sailing segments. The pipeline now fully accounts for new fare codes to ensure stability after cutover
