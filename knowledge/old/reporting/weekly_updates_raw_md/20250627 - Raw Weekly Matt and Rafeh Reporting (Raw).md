---
tags:
  - aagam_shah
  - atefeh_mahdavi
  - bernard_kai_wittmaack
  - brendan_turpin
  - business_area/axiom_generative-ai_seats_(hotel_ops,_consumer_insights,_legal)
  - business_area/contact_center_optimization_&_automation_(rci_cel)
  - business_area/hybris_product_recommendations_(digital)
  - business_area/loyalty_program_redesign
  - business_area/marine_insights_analytics_platform_(marine_operations)
  - business_area/newbuild
  - business_area/pcp_pricing_automation_(rci_cel)
  - business_area/revenue_management_automation_(cel)
  - business_area/revenue_management_automation_(rci)
  - business_area/supply_chain_optimization
  - camila_aichele
  - cristian_villamarin-villamil
  - erick_alfaro
  - gaurav_godawat
  - ignacio_villasmil
  - jesse_bausell
  - kartik_ullal
  - kevin_diaz
  - lamis_amer
  - mahshad_shariatnasab
  - mehdi_assefi
  - mert_ersoz
  - michelle_manfrini
  - parimala_kettymuthu
  - project/ada-accessible_berthing_migration
  - project/automated_pricing_expansion
  - project/beverage_package_optimization
  - project/conversational_ivr
  - project/division-level_medallia_reports
  - project/expedition_forecasting_with_silversea_automation
  - project/fleetwide_energy_monitoring
  - project/gty-lead_fare_optimization_model
  - project/historical_data_integration
  - project/lead_prioritization_-_bk2cx_(rci_&_cel)
  - project/lead_prioritization_-_cti_(rci_&_cel)
  - project/miap_phase_iv_development
  - project/nps_drivers_analysis_for_alert_system
  - project/offer_to_cancel_(oftocx)_model_(rci_&_cel)
  - project/real-time_api_optimization
  - project/spend-to-save_pilot_analysis
  - project/warehouse_depletion_model_updates
  - raw
  - reza_bahadori
  - srilekha_reddy_madupu
  - weekly_update
date: "2025-06-27"
type: "raw_weekly_update"
---

# Weekly Update (Raw) - 2025-06-27

## Update 1

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[aagam_shah/overview_aagam_shah|Aagam Shah]]

### Summarized Update

RCI | SPI Sailing | EDA on Track related Metrics (Track Variance)
This week I started working on understanding the impact of track variance on SPI scores. In order to understand the impact of track variance I initially looked at % of times the sailing beats track and magnitude by which it beats track. Based on my initial EDA I noticed that low SPI sailings for Alaska beat track more number of times as compared to high SPI sailing, whereas for all other sailings it is the opposite.

### Raw Update

RCI | SPI Sailing | EDA on Track related Metrics (Track Variance)
This week I started working on understanding the impact of track variance on SPI scores. In order to understand the impact of track variance I initially looked at % of times the sailing beats track and magnitude by which it beats track. Based on my initial EDA I noticed that low SPI sailings for Alaska beat track more number of times as compared to high SPI sailing, whereas for all other sailings it is the opposite.
Next Steps based on our conversation with Nick:
·       Only consider FIT track
·       Instead of considering the direct magnitude, consider weighted magnitude of track variance
·       consider only past 1 year data for any read date

---

## Update 2

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

RCI | PRE Elasticity Upgrades
Investigating Residual Errors
I conducted an analysis of residual plots for the new elasticity model to identify regions with elevated prediction errors across different ship classes. Within each class, I further examined how these errors fluctuate across various booking windows—specifically, close-in, mid, and far-out periods. A notable observation was the occurrence of extreme errors in Balcony categories.

### Raw Update

RCI | PRE Elasticity Upgrades
Investigating Residual Errors
I conducted an analysis of residual plots for the new elasticity model to identify regions with elevated prediction errors across different ship classes. Within each class, I further examined how these errors fluctuate across various booking windows—specifically, close-in, mid, and far-out periods.
A notable observation was the occurrence of extreme errors in Balcony categories. This issue was traced to the grouping of Balcony (B) and Neighborhood (N) categories within the VPS dataset. To improve model accuracy, we subsequently separated B and N into distinct categories, enabling more precise modeling and predictions.

---

## Update 3

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[atefeh_mahdavi/overview_atefeh_mahdavi|Atefeh Mahdavi]]

### Summarized Update

RCI | PRE Elasticity Upgrades
Elasticity sensitivity analysis and comparing price and log-price features
The analysis evaluated the impact of log transformation on elasticity estimates using a Poisson regression model with standard scaling, target encoding, and a WTS bin size of 5. Results showed that log transformation does not affect R² performance, but elasticity curves shift, with log-log models indicating higher (more negative) elasticity values. Separate analysis at the meta product–catclass level tested static bin sizes (1, 5, 10, 20) and a custom strategy to compare against RDSS product code-level models.

### Raw Update

RCI | PRE Elasticity Upgrades
Elasticity sensitivity analysis and comparing price and log-price features
The analysis evaluated the impact of log transformation on elasticity estimates using a Poisson regression model with standard scaling, target encoding, and a WTS bin size of 5.
Results showed that log transformation does not affect R² performance, but elasticity curves shift, with log-log models indicating higher (more negative) elasticity values.
Separate analysis at the meta product–catclass level tested static bin sizes (1, 5, 10, 20) and a custom strategy to compare against RDSS product code-level models.
Findings suggest that bin sizes of 5 and 10 provide good R² and interpretable elasticity estimates, supporting their use for fixed binning at the meta–catclass level.

---

## Update 4

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

CEL | SPI Scoring Model Improvements JUNE
Met with Anastasia on 6/20
Final iteration of SPI scoring model approved for final release
Next step is to push new SPI model into production

### Raw Update

CEL | SPI Scoring Model Improvements JUNE
Met with Anastasia on 6/20
Final iteration of SPI scoring model approved for final release
Next step is to push new SPI model into production

---

## Update 5

**Date:** 2025-06-27
**Business Area:** New Build
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

FIT Track Targets
Met with Chris on 6/20
Chris wants FIT to be separated from group demand, and recommends using the table:
prd_silver.mkrp_rmd.daily_apd_history_bkc_wtd
We want to use projected pax instead of actual pax for RCI
Also, Chris want to see if actual pax builds observe the early March spike for the Caribbean products, or whether that is an artifact of retention model

### Raw Update

FIT Track Targets
Met with Chris on 6/20
Chris wants FIT to be separated from group demand, and recommends using the table:
prd_silver.mkrp_rmd.daily_apd_history_bkc_wtd
We want to use projected pax instead of actual pax for RCI
Also, Chris want to see if actual pax builds observe the early March spike for the Caribbean products, or whether that is an artifact of retention model

---

## Update 6

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[bernard_kai_wittmaack/overview_bernard_kai_wittmaack|Bernard Kai Wittmaack]]

### Summarized Update

RCI | SPI Factor Model
T4 Track targets
Build dataset from vcap snapshot for T4 booking volume
Next step is to perform EDA to find patterns in T4 builds for high and low SPI sailings

### Raw Update

RCI | SPI Factor Model
T4 Track targets
Build dataset from vcap snapshot for T4 booking volume
Next step is to perform EDA to find patterns in T4 builds for high and low SPI sailings

---

## Update 7

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** Unidentified

### Summarized Update

RCI | PRE Ongoing Upgrades | JUNE
Targeted optimization of RCI PRE pipeline 3. Reduced run time by 10 additional minutes and cleaned data storage of obsolete legacy reporting data. Additional clean-up of RCI PRE pipeline 3 Oracle dependencies, to prepare for large-scale move to clean up pipeline 2.

### Raw Update

RCI | PRE Ongoing Upgrades | JUNE
Targeted optimization of RCI PRE pipeline 3. Reduced run time by 10 additional minutes and cleaned data storage of obsolete legacy reporting data.
Additional clean-up of RCI PRE pipeline 3 Oracle dependencies, to prepare for large-scale move to clean up pipeline 2.

---

## Update 8

**Date:** 2025-06-27
**Business Area:** CEL Revenue Management
**Business Project:** ADA-Accessible Berthing Migration
**People:** Unidentified

### Summarized Update

ICOMLD deep dive to understand the reasons for Celebrity mandatory occupancy data submission errors. Adjustments to Celebrity re-berthing and close-out of version 1.0 work. Go-live will occur when Aarish returns from FAM cruise.

### Raw Update

ICOMLD deep dive to understand the reasons for Celebrity mandatory occupancy data submission errors.
Adjustments to Celebrity re-berthing and close-out of version 1.0 work. Go-live will occur when Aarish returns from FAM cruise.

---

## Update 9

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[jesse_bausell/overview_jesse_bausell|Jesse Bausell]]

### Summarized Update

SSC | PRE | Design PRE A/B Test - JUN
A/B testing: power analysis + ALASKA voyage selection
Delivered Power Analysis for combined Alaska, Caribbean, Northern Europe, and Mediterranean voyages. Meeting with Business next week to discuss. K-means cluster analysis for Alaska sailings
In grouping Northern Europe Voyages into similar pairs, we intend to structure our methodology like we did in the Mediterranean.

### Raw Update

SSC | PRE | Design PRE A/B Test - JUN
A/B testing: power analysis + ALASKA voyage selection
Delivered Power Analysis for combined Alaska, Caribbean, Northern Europe, and Mediterranean voyages. Meeting with Business next week to discuss.
K-means cluster analysis for Alaska sailings
In grouping Northern Europe Voyages into similar pairs, we intend to structure our methodology like we did in the Mediterranean.

---

## Update 10

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

RCI | GTY-LEAD 2.0 | JUNE
Optimization Analysis
Met with business 6/24/25 to review updated results. All metas are now included in model and optimization to recommend gaps for entire fleet. Business is happier to lower gaps.

### Raw Update

RCI | GTY-LEAD 2.0 | JUNE
Optimization Analysis
Met with business 6/24/25 to review updated results. All metas are now included in model and optimization to recommend gaps for entire fleet. Business is happier to lower gaps. Results were sent over for further review and verification to ensure there is no falloff.

---

## Update 11

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[michelle_manfrini/overview_michelle_manfrini|Michelle Manfrini]]

### Summarized Update

CEL | GTY-LEAD 3.0 | CATGAP Inter-category Gaps Stage 3
Optimization expansion to all sailings
Met with business today 6/26/25 and reviewed logic. CEL is happy with progress and optimization logic. RDSS groupings were added to historical LAFs and is now limited to only completed sailings.

### Raw Update

CEL | GTY-LEAD 3.0 | CATGAP Inter-category Gaps Stage 3
Optimization expansion to all sailings
Met with business today 6/26/25 and reviewed logic. CEL is happy with progress and optimization logic. RDSS groupings were added to historical LAFs and is now limited to only completed sailings. Track was converted to bookings based on cat-class capacity. Constraints added for low/upper bookings <= tier capacity, deluxe bookings = tier capacity. Bookings curved outputted for capacity and booked position. Formula/calculations visualizations added to PowerPoint to better explain approach.

---

## Update 12

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[srilekha_reddy_madupu/overview_srilekha_reddy_madupu|Srilekha Reddy Madupu]]

### Summarized Update

CEL Elasticity Model | Feature Engineering
Bucket Calendar_woy by Business Periods (e.g., Wave Season) for Post-Model Evaluation based on Deviance Error
Over the past week, I completed a Poisson deviance deep dive, built a new flag feature from the findings to help the model anticipate volatile periods. ran it through our training workflow, and assessed its effect on key metrics, using slightly different week ranges for short-Caribbean products versus all others. Seasonal Segmentation
I mapped each calendar week of the year to one of four business seasons Wave, Spring, Fall, and Winter—based on week number ranges.

### Raw Update

CEL Elasticity Model | Feature Engineering
Bucket Calendar_woy by Business Periods (e.g., Wave Season) for Post-Model Evaluation based on Deviance Error
Over the past week, I completed a Poisson deviance deep dive, built a new flag feature from the findings to help the model anticipate volatile periods. ran it through our training workflow, and assessed its effect on key metrics, using slightly different week ranges for short-Caribbean products versus all others.
Seasonal Segmentation
I mapped each calendar week of the year to one of four business seasons Wave, Spring, Fall, and Winter—based on week number ranges. This allowed us to view model performance in the context of our peak booking periods (Wave), shoulder seasons (Spring/Fall), and off-peak (Winter).
Deviance Calculation and Aggregation
Using the model’s predictions versus actual counts, I computed Poisson deviance for every record. I then aggregated those deviance values both by season (to see which season had the highest average error) and by individual week of year (to pinpoint specific trouble weeks).
Identifying Worst-Performing Weeks
From the weekly aggregation, I extracted the top ten calendar weeks with the highest total deviance. These came predominantly from early Spring (weeks 6–12) and late Fall (weeks 23–28) for most products, with the short-Caribbean routes showing additional spikes around end-of-year holidays.

---

## Update 13

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[lamis_amer/overview_lamis_amer|Lamis Amer]]

### Summarized Update

RCI | PRE Elasticity Upgrades - JUNE
Model Training and Testing
Tested multiple feature transformations and regressors as well as different weeks to sail binning strategies. At the RDSS group level trained models (52 RDSS groups, 4 cat classes, 3 diff scaling strategies for the price feature (z scaling, group z scaling, power trans), 4 diff wts binning strategies (5, 10 weeks to sail, hard coded (0-12, 12-36, 36-60, 60+) , and data-driven spline-based binning). Due to the small sample size for some RDSS cat classes some models fail to train specially with group-based transformations.

### Raw Update

RCI | PRE Elasticity Upgrades - JUNE
Model Training and Testing
Tested multiple feature transformations and regressors as well as different weeks to sail binning strategies.
At the RDSS group level trained models (52 RDSS groups, 4 cat classes, 3 diff scaling strategies for the price feature (z scaling, group z scaling, power trans), 4 diff wts binning strategies (5, 10 weeks to sail, hard coded (0-12, 12-36, 36-60, 60+) , and data-driven spline-based binning). Due to the small sample size for some RDSS cat classes some models fail to train specially with group-based transformations. Running these experiments at the rdss group-cc level took 7 mins, and 3 mins at the meta-cc level without MLFlow Logging. Will only be Logging the selected best models
At the meta, cat_class level I trained 1,824 models (19 meta products, 4 cat classes, 3 price transformations, 4 binning strategies, and 2 regressors Ridge (alpha = 1) and Poisson).
Out of all the trained models I selected the best modeling parameters for each meta-cat class / rdss-cat class based on the r-squared and stored them in a dictionary to use later in our final code.
Currently running comparisons between the trained models and the current model in production and setting up slides to discuss and present results to the business.

---

## Update 14

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[kartik_ullal/overview_kartik_ullal|Kartik Ullal]]

### Summarized Update

CEL | OBR | Evergreen A/B Test Final Analysis
This ticket concluded the evergreen loyalty pilot that was going on. Finished with the analysis on post test data, and even though the results were not significant, the observations were positive instead of negative, and business team is confident with moving forward with the changes as it reduces overhead costs and work towards the call center. Next steps would be for business teams to coordinate with the go live date for the changes.

### Raw Update

CEL | OBR | Evergreen A/B Test Final Analysis
This ticket concluded the evergreen loyalty pilot that was going on. Finished with the analysis on post test data, and even though the results were not significant, the observations were positive instead of negative, and business team is confident with moving forward with the changes as it reduces overhead costs and work towards the call center. Next steps would be for business teams to coordinate with the go live date for the changes.

---

## Update 15

**Date:** 2025-06-27
**Business Area:** PCP Pricing Automation
**Business Project:** Beverage Package Optimization
**People:** [[ignacio_villasmil/overview_ignacio_villasmil|Ignacio Villasmil]]

### Summarized Update

Created PCP/OBR powerpoint on the PCP/OBR progress & accomplishments so far (for Dave to use)
Tried implementing the simpler model & optimization used for drink packages into the cabanas project:
This was done with the intention of comparing the results of the two and seeing if there are any substantial improvements from the simpler model compared to the 2-part model. However, due to higher priority work to be done, and also since the current model & optimization used for cabanas has shown good results anyways, this is being pushed aside to work on more important tasks. This can be revisited later on as possible improvements & advancements for the Cabanas PRE.

### Raw Update

Created PCP/OBR powerpoint on the PCP/OBR progress & accomplishments so far (for Dave to use)
Tried implementing the simpler model & optimization used for drink packages into the cabanas project:
This was done with the intention of comparing the results of the two and seeing if there are any substantial improvements from the simpler model compared to the 2-part model. However, due to higher priority work to be done, and also since the current model & optimization used for cabanas has shown good results anyways, this is being pushed aside to work on more important tasks. This can be revisited later on as possible improvements & advancements for the Cabanas PRE.
Changed the output table format for Cabanas to match what was done for the Drink Package optimization
The format of the optimization table outputs for Cabanas were changed to match the architecture of that for drink packages. This is done with the intention of later combining these optimization outputs into one centralized table for price optimizations of OBR/PCP products. This includes a new column to flag any potential violations of bounds & constraints in the optimization. In addition, the output of recommended price is converted into 2 different possible price recommendations: 1) the new system price that would need to be set if the average discount rate continues to be applied, and 2) the new discount percentage assuming that the system price stays the same. This output already gives the output for 2 different possible PRE automated price changes when implemented into Hybris.

---

## Update 16

**Date:** 2025-06-27
**Business Area:** Loyalty
**Business Project:** Spend-to-Save Pilot Analysis
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

After meeting with DE and OBR teams on Monday, DE team provided a new dataset with transactional spend data with the intention of it being used for spend to save onboard spend measurement. Austin told us validation should be done with end of voyage reports because both EOV Reports and the new dataset were built off of fidelio source. Data Science was not able to get the data to tie back and walked DE through the validation steps taken.

### Raw Update

After meeting with DE and OBR teams on Monday, DE team provided a new dataset with transactional spend data with the intention of it being used for spend to save onboard spend measurement. Austin told us validation should be done with end of voyage reports because both EOV Reports and the new dataset were built off of fidelio source. Data Science was not able to get the data to tie back and walked DE through the validation steps taken. EOV Reports will continue to be used until a dataset is produced that can be tied back to a known source of truth like EOV reports.
Actively working on preparing slides with best available data to give an update on spend to save to the EC.

---

## Update 17

**Date:** 2025-06-27
**Business Area:** PCP Pricing Automation
**Business Project:** Automated Pricing Expansion
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Provided DE with a sample promo upload so the kafka upload functionality can be tested. There is still work to be done to define best practices on generating uuids and other parameters for promotion mass upload. Aligned with Gaby Martell on long term delivery sequencing of obr areas to be optimized.

### Raw Update

Provided DE with a sample promo upload so the kafka upload functionality can be tested. There is still work to be done to define best practices on generating uuids and other parameters for promotion mass upload.
Aligned with Gaby Martell on long term delivery sequencing of obr areas to be optimized.

---

## Update 18

**Date:** 2025-06-27
**Business Area:** RCI Revenue Management
**Business Project:** GTY-Lead Fare Optimization Model
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Focus was mainly on knowledge transfer with Jake, but also worked with the team to facilitate distribution of responsibilities in elasticity modeling and implementing best practices on modeling framework. Updates were shared with both brands on elasticity modeling. Chris and Eddie are convinced the model is better than the prior version but want some more validation on the elasticity values and directional changes over wts bins.

### Raw Update

Focus was mainly on knowledge transfer with Jake, but also worked with the team to facilitate distribution of responsibilities in elasticity modeling and implementing best practices on modeling framework. Updates were shared with both brands on elasticity modeling. Chris and Eddie are convinced the model is better than the prior version but want some more validation on the elasticity values and directional changes over wts bins.

---

## Update 19

**Date:** 2025-06-27
**Business Area:** CEL Revenue Management
**People:** [[kevin_diaz/overview_kevin_diaz|Kevin Diaz]]

### Summarized Update

Anastasia provided feedback that she does not want CEL to fall behind, so if there are feature changes improving results on RCI they should also be tested in CEL at the same time.

### Raw Update

Anastasia provided feedback that she does not want CEL to fall behind, so if there are feature changes improving results on RCI they should also be tested in CEL at the same time.

---

## Update 20

**Date:** 2025-06-27
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - CTI (RCI & CEL)
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

- In Progress: Duplicate-lead bug caused same leads to be scored multiple times. This indirectly caused some leads to also be rescored with a score lower than they actually desereved due to stale data being used to score. - SHAP feature importance prepare deck
- Need to further validate why CTI CEL/RCI performance is lackluster for last ~20 days of scoring.

### Raw Update

- In Progress: Duplicate-lead bug caused same leads to be scored multiple times. This indirectly caused some leads to also be rescored with a score lower than they actually desereved due to stale data being used to score.
- SHAP feature importance prepare deck
- Need to further validate why CTI CEL/RCI performance is lackluster for last ~20 days of scoring.
- Slight change in requirements: CEL SVAL leads should only be Galapagos sailings

---

## Update 21

**Date:** 2025-06-27
**Business Area:** Contact Center
**Business Project:** Lead Prioritization - BK2CX (RCI & CEL)
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]]

### Summarized Update

- Fixed bug with phone number formatting which caused MVAL, HVAL, SVAL to fail SFTP transfer process
- Discussed adding booking_id to file drop
- Fixed towards removing international leads from NA file

### Raw Update

- Fixed bug with phone number formatting which caused MVAL, HVAL, SVAL to fail SFTP transfer process
- Discussed adding booking_id to file drop
- Fixed towards removing international leads from NA file

---

## Update 22

**Date:** 2025-06-27
**Business Area:** Medallia
**Business Project:** Division-Level Medallia Reports
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

- Working on EDA for guest logs in preparation to create bullet-point pipeline similar to Medallia
- Added 'SC' specific hotel directors to email distribution list expanding scope of recipients
- Received feedback from Figgis regarding emailing capabilities
- Received feedback from Matt regarding the use of an ML model in ordering topics

### Raw Update

- Working on EDA for guest logs in preparation to create bullet-point pipeline similar to Medallia
- Added 'SC' specific hotel directors to email distribution list expanding scope of recipients
- Received feedback from Figgis regarding emailing capabilities
- Received feedback from Matt regarding the use of an ML model in ordering topics

---

## Update 23

**Date:** 2025-06-27
**Business Area:** Medallia
**Business Project:** NPS Drivers Analysis for Alert System
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[gaurav_godawat/overview_gaurav_godawat|Gaurav Godawat]]

### Summarized Update

- Met with Medallia vendor data scientists for analytics insights and Q&A (overall lackluster insights from vendor; reinforces DA2I partnership)
- Gaurav will ideate strategies to further improve drivers model
- Experiment various modeling approaches & deck colllation (In Progress)
- Single‐model vs. residual‐split experiments (Todo)
- Promoters/Detractors passives → weighted‐avg score (Todo)

### Raw Update

- Met with Medallia vendor data scientists for analytics insights and Q&A (overall lackluster insights from vendor; reinforces DA2I partnership)
- Gaurav will ideate strategies to further improve drivers model
- Experiment various modeling approaches & deck colllation (In Progress)
- Single‐model vs. residual‐split experiments (Todo)
- Promoters/Detractors passives → weighted‐avg score (Todo)

---

## Update 24

**Date:** 2025-06-27
**Business Area:** MyCruise Recommender
**Business Project:** Real-Time API Optimization
**People:** [[erick_alfaro/overview_erick_alfaro|Erick Alfaro]], [[cristian_villamarin-villamil/overview_cristian_villamarin-villamil|Cristian Villamarin-Villamil]]

### Summarized Update

- In Progress: ETL optimizations, interaction-based retraining, orchestrator notebook build. - Done: App-interaction ETL, API redeploys, hourly segmentation job. - Next: Finalize Dynamic job setup and classification model for custom product GenAI categories.

### Raw Update

- In Progress: ETL optimizations, interaction-based retraining, orchestrator notebook build.
- Done: App-interaction ETL, API redeploys, hourly segmentation job.
- Next: Finalize Dynamic job setup and classification model for custom product GenAI categories.

---

## Update 25

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[parimala_kettymuthu/overview_parimala_kettymuthu|Parimala Kettymuthu]]

### Summarized Update

GenerativeAI Seat - Qualtrics Theme Extraction
- In Progress: UI requirements scoped; Stakeholder expressed interest in traditional topic modeling approaches such as LDA, TFIDF, bert-topic
- Agentic-AI based topic modeling proposed by Parimala. - Need to meet with Stakeholder once again to further refine definition of done.

### Raw Update

GenerativeAI Seat - Qualtrics Theme Extraction
- In Progress: UI requirements scoped; Stakeholder expressed interest in traditional topic modeling approaches such as LDA, TFIDF, bert-topic
- Agentic-AI based topic modeling proposed by Parimala.
- Need to meet with Stakeholder once again to further refine definition of done.

---

## Update 26

**Date:** 2025-06-27
**Business Area:** Unclassified
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]], [[reza_bahadori/overview_reza_bahadori|Reza Bahadori]], [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

Generative AI SEAT
Legal Claims Prediction POC
Presented the Risk Management modeling solution to Claire Mason and the Risk Management team for the second round and worked on finalizing Claire’s presentation for the executive committee meeting in July. Reza worked on EAD/Modeling/Presentation for the Legal project. The models achieved approximately 70% F1 score, which is promising for the proof-of-concept stage.

### Raw Update

Generative AI SEAT
Legal Claims Prediction POC
Presented the Risk Management modeling solution to Claire Mason and the Risk Management team for the second round and worked on finalizing Claire’s presentation for the executive committee meeting in July.
Reza worked on EAD/Modeling/Presentation for the Legal project. The models achieved approximately 70% F1 score, which is promising for the proof-of-concept stage.
Brendan Performed follow-up analysis of the Legal Claims Prediction and presented findings to the VP; collaborated on developing the presentation for the executive committee.

---

## Update 27

**Date:** 2025-06-27
**Business Area:** New Build
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

Joined a workshop with the Newbuild and RCI Product teams on the SY Revite scope for the 2028 drydock scope identification. The team expects results by mid-August. The short timeframe puts pressure on the team to deliver a solution for this experimental project on stability estimations, based on prior project documents.

### Raw Update

Joined a workshop with the Newbuild and RCI Product teams on the SY Revite scope for the 2028 drydock scope identification. The team expects results by mid-August. The short timeframe puts pressure on the team to deliver a solution for this experimental project on stability estimations, based on prior project documents.
Refactored the Webapp from scratch in preparation for hosting Newbuild's stability simulator/chatbot.

---

## Update 28

**Date:** 2025-06-27
**Business Area:** Marine
**Business Project:** MIAP Phase IV Development
**People:** [[mert_ersoz/overview_mert_ersoz|Mert Ersoz]]

### Summarized Update

Prepared a detailed explanatory document on Fuzzy Logic applications in maritime safety as a potential knowledge-based AI solution for creating risk metrics. Presented the HVAC Air Handling Unit automated diagnostic solution to HVAC Manager Eddie Wehus. Received feedback for further improvements.

### Raw Update

Prepared a detailed explanatory document on Fuzzy Logic applications in maritime safety as a potential knowledge-based AI solution for creating risk metrics.
Presented the HVAC Air Handling Unit automated diagnostic solution to HVAC Manager Eddie Wehus. Received feedback for further improvements.
Refactored the MIAP Webapp from scratch in preparation for hosting Newbuild's stability simulator/chatbot and fuel forecast models' APIs for testing.
Conducted a budget review of MIAP Phase III labor.

---

## Update 29

**Date:** 2025-06-27
**Business Area:** Marine
**Business Project:** MIAP Phase IV Development
**People:** Unidentified

### Summarized Update

Implemented a new multivariate outlier removal method in the power plant base model using Isolation Forest and Local Outlier Factor. Added voyage phase calculation to the power plant features. Implemented a category split regressor on the power plant base model, significantly improving performance.

### Raw Update

Implemented a new multivariate outlier removal method in the power plant base model using Isolation Forest and Local Outlier Factor.
Added voyage phase calculation to the power plant features.
Implemented a category split regressor on the power plant base model, significantly improving performance.

---

## Update 30

**Date:** 2025-06-27
**Business Area:** MIAP
**Business Project:** MIAP Phase IV Development
**People:** [[brendan_turpin/overview_brendan_turpin|Brendan Turpin]]

### Summarized Update

Deployed new propulsion models split by ALS into production. Worked with a Junior Data Engineer to resolve Git-related issues in the development environment. Parameterized email notification lists and workflow access controls so all MIAP developers receive alerts when jobs fail and can view/manage workflows.

### Raw Update

Deployed new propulsion models split by ALS into production.
Worked with a Junior Data Engineer to resolve Git-related issues in the development environment.
Parameterized email notification lists and workflow access controls so all MIAP developers receive alerts when jobs fail and can view/manage workflows. This configuration is now centralized within the Databricks asset bundle.

---

## Update 31

**Date:** 2025-06-27
**Business Area:** Marine
**Business Project:** Historical Data Integration
**People:** Unidentified

### Summarized Update

June 20: Completed testing of the new Eniram approach. Made modifications to scripts regarding chunk size, tested in QA, and scheduled deployment. June 23: Verified data consistency via the scheduler workflow.

### Raw Update

June 20: Completed testing of the new Eniram approach. Made modifications to scripts regarding chunk size, tested in QA, and scheduled deployment.
June 23: Verified data consistency via the scheduler workflow. Merged updated scripts into the master branch. Gained permissions to test Ignio and began debugging scripts.
June 24: Coordinated with the Ignio team to clarify new requirements. Adapted logic accordingly.
June 25: Worked on the SQL script to perform 10-minute mean aggregation for fetched Eniram data. Updated the GMO ETL process, changing the source from Azure SQL to the gmo_app schema. Made necessary updates in the bronze notebook, pushed changes, and executed a repair run in RPD.
June 26: Focused on Ignio code for handling two new data streams via API. Addressed a failure in the Silver GMO script in production; implemented necessary changes. Identified an additional view requiring modification—awaiting input before proceeding with the update and deployment.

---

## Update 32

**Date:** 2025-06-27
**Business Area:** Marine
**Business Project:** Fleetwide Energy Monitoring
**People:** [[mahshad_shariatnasab/overview_mahshad_shariatnasab|Mahshad Shariatnasab]]

### Summarized Update

Monitoring IN and AD deviations after contacting the ship; issue remains unresolved. Completed the incinerator model for fuel forecasting across all ships with available data and integrated it into the workflow. Started developing incinerator visualizations for the GMO app.

### Raw Update

Monitoring IN and AD deviations after contacting the ship; issue remains unresolved.
Completed the incinerator model for fuel forecasting across all ships with available data and integrated it into the workflow.
Started developing incinerator visualizations for the GMO app.
Noticed deviations in CS, BY, WN, and QN in the AHU; planning to contact the ships for clarification.
Added VY class to the boiler model; an issue with AD results persists, which I will address.

---

## Update 33

**Date:** 2025-06-27
**Business Area:** Marine
**Business Project:** Historical Data Integration
**People:** [[mehdi_assefi/overview_mehdi_assefi|Mehdi Assefi]]

### Summarized Update

Finalized the data extraction process from project report PDFs, ensuring all key information was captured. Managed data cleaning and adjusted columns across different tables to ensure consistency.

### Raw Update

Finalized the data extraction process from project report PDFs, ensuring all key information was captured.
Managed data cleaning and adjusted columns across different tables to ensure consistency.

---

## Update 34

**Date:** 2025-06-27
**Business Area:** Supply Chain
**Business Project:** Warehouse Depletion Model Updates
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Ben and Camila
Supply Chain Integrated Business Planning (IBP)
Completed
• Debugged “get model” notebooks to ensure correct product-actual consumption for Uniform, Medical and CocoCay models
• Delivered RCI/CEL Inventory Depletion table (warehouse-inventory column fix in progress)
• Updated RCI/CEL Order Creation pipeline to remove deprecated columns
• Completed volatility reports for all IBP models; saved in MLflow and automated distribution via email, SharePoint and Teams
– Evaluating viewing options (Teams UI preferred)
– Testing alert thresholds

### Raw Update

Ben and Camila
Supply Chain Integrated Business Planning (IBP)
Completed
• Debugged “get model” notebooks to ensure correct product-actual consumption for Uniform, Medical and CocoCay models
• Delivered RCI/CEL Inventory Depletion table (warehouse-inventory column fix in progress)
• Updated RCI/CEL Order Creation pipeline to remove deprecated columns
• Completed volatility reports for all IBP models; saved in MLflow and automated distribution via email, SharePoint and Teams
– Evaluating viewing options (Teams UI preferred)
– Testing alert thresholds

---

## Update 35

**Date:** 2025-06-27
**Business Area:** Supply Chain
**Business Project:** Expedition Forecasting with Silversea Automation
**People:** [[camila_aichele/overview_camila_aichele|Camila Aichele]]

### Summarized Update

Pending
• Finalize warehouse-inventory column update (target July 1)
• Decide on final distribution channel and alert-threshold value
Carlos
E-Commerce
Completed
Customer Targeting
• Restored Oracle-authenticated dashboard after password update; data is current
• Enhanced targeted-offer uplift models per business guidance: removed outlier campaigns and extended averaging window from 15 to 30 days
• Deployed uplift-target “Genie” dashboard to production
Carlos and Ben
E-Commerce
Pending
Customer Targeting:
• Add business-recommended epsilon columns to “Genie” (prior attempt conflicted with context)
• Support Bao in building a consolidated marketing-models summary dashboard
Journey Orchestration (Email Automation):
• Completed initial demonstration with Salesforce and held RFI/RFP kickoff call to align on scope, expectations and success criteria
Ben
Customer Lifetime Value (CLV)
Accomplished
• Stitched new OBR data into analytics table with aggregation checks to preserve row counts
• Completed EDA on behavioral drivers: booking channel, inter-booking intervals, loyalty tiers, NPS and cruise experience
Ben
Customer Lifetime Value (CLV)
In Progress
• Rerunning ETL pipeline on updated analytics table (with Gaby)
• Building RCI Cohort Excel sheet (mirroring CEL) and updating both sheets with refreshed data
• Investigating duplicate-row anomalies in analytics table; auditing pipeline to prevent exponential record growth
Mirielle
Contact Center - Lead Prioritization
• Investigated Augusto’s concern: only LVAL leads visible in Power BI dashboard
• Productionized scoring for all lead types in Siebel; initially only CEL leads flowed into the report
• 6/24: Sent test files for all lead types to Siebel; Sridhar confirmed RCI leads passed into production at 11 pm ET
• 6/25: Enabled full pipeline in production; Augusto validating visibility of all leads
Business may require Booking_ID in Siebel output files (new request)
Next steps: Joint review with Siebel and Data Science teams to finalize file format
Mirielle
Contact Center - Workforce Planning POC
• Finalized Weekly Office-Hours Grid for 12 LoBs (Casino; CO Groups; CO Sales; CO & CE Service; GEM (Reservation); Groups; Loyalty; RES (Reservation); STAR; CE Sales; CO Groups Sales; CO Groups Services)
– Captures service open/closed hours and hourly/weekly call-volume distribution
– Combined datasets stored in dev_datascience.workforce_planning.call_volume_rci_north_america_office_hours
Next Steps
– Simulate staffing requirements based on processed call-volume data
– Collaborate with Xavier to adapt international staffing-model functions for North America
– Generate baseline daily forecasts for the RES LoB to validate computational accuracy

### Raw Update

Pending
• Finalize warehouse-inventory column update (target July 1)
• Decide on final distribution channel and alert-threshold value
Carlos
E-Commerce
Completed
Customer Targeting
• Restored Oracle-authenticated dashboard after password update; data is current
• Enhanced targeted-offer uplift models per business guidance: removed outlier campaigns and extended averaging window from 15 to 30 days
• Deployed uplift-target “Genie” dashboard to production
Carlos and Ben
E-Commerce
Pending
Customer Targeting:
• Add business-recommended epsilon columns to “Genie” (prior attempt conflicted with context)
• Support Bao in building a consolidated marketing-models summary dashboard
Journey Orchestration (Email Automation):
• Completed initial demonstration with Salesforce and held RFI/RFP kickoff call to align on scope, expectations and success criteria
Ben
Customer Lifetime Value (CLV)
Accomplished
• Stitched new OBR data into analytics table with aggregation checks to preserve row counts
• Completed EDA on behavioral drivers: booking channel, inter-booking intervals, loyalty tiers, NPS and cruise experience
Ben
Customer Lifetime Value (CLV)
In Progress
• Rerunning ETL pipeline on updated analytics table (with Gaby)
• Building RCI Cohort Excel sheet (mirroring CEL) and updating both sheets with refreshed data
• Investigating duplicate-row anomalies in analytics table; auditing pipeline to prevent exponential record growth
Mirielle
Contact Center - Lead Prioritization
• Investigated Augusto’s concern: only LVAL leads visible in Power BI dashboard
• Productionized scoring for all lead types in Siebel; initially only CEL leads flowed into the report
• 6/24: Sent test files for all lead types to Siebel; Sridhar confirmed RCI leads passed into production at 11 pm ET
• 6/25: Enabled full pipeline in production; Augusto validating visibility of all leads
Business may require Booking_ID in Siebel output files (new request)
Next steps: Joint review with Siebel and Data Science teams to finalize file format
Mirielle
Contact Center - Workforce Planning POC
• Finalized Weekly Office-Hours Grid for 12 LoBs (Casino; CO Groups; CO Sales; CO & CE Service; GEM (Reservation); Groups; Loyalty; RES (Reservation); STAR; CE Sales; CO Groups Sales; CO Groups Services)
– Captures service open/closed hours and hourly/weekly call-volume distribution
– Combined datasets stored in dev_datascience.workforce_planning.call_volume_rci_north_america_office_hours
Next Steps
– Simulate staffing requirements based on processed call-volume data
– Collaborate with Xavier to adapt international staffing-model functions for North America
– Generate baseline daily forecasts for the RES LoB to validate computational accuracy

---

## Update 36

**Date:** 2025-06-27
**Business Area:** Contact Center
**Business Project:** Conversational IVR
**People:** Unidentified

### Summarized Update

Accomplishments
Contact Center [Conversational IVR] 
SOW for copilot migration signed 
Deployed Celebrity River cruise initiative 
Deployed Celebrity changes for Loyalty – 42% increase in minutes automated. Deployed Dining and Check-in FAQs – no finalized data yet not been in a week 

Henry Drescher
In-Progress
Contact Center [Cresta] 
New agent dashboard 
GenKA phases 
Phase 1 – remove archived articles + create hints 
Phase 2 – Provide links + reason for article suggestion 
Phase 3 – Provide links + reason for article suggestion, scroll to appropriate part in article and when an answer is a non nuanced fact the answer will directly be provided. Analytics assessment – Allows for sunsetting Nice analytics platform 
AI analysts use case development – allows for self-service analytics and insights by team 
Targeting post cruise team unlimited access for 1 month 
Need to build topic filters prior to running this pilot.

### Raw Update

Accomplishments
Contact Center [Conversational IVR] 
SOW for copilot migration signed 
Deployed Celebrity River cruise initiative 
Deployed Celebrity changes for Loyalty – 42% increase in minutes automated. 
Deployed Dining and Check-in FAQs – no finalized data yet not been in a week 

Henry Drescher
In-Progress
Contact Center [Cresta] 
New agent dashboard 
GenKA phases 
Phase 1 – remove archived articles + create hints 
Phase 2 – Provide links + reason for article suggestion 
Phase 3 – Provide links + reason for article suggestion, scroll to appropriate part in article and when an answer is a non nuanced fact the answer will directly be provided. 
Analytics assessment – Allows for sunsetting Nice analytics platform 
AI analysts use case development – allows for self-service analytics and insights by team 
Targeting post cruise team unlimited access for 1 month 
Need to build topic filters prior to running this pilot. Waiting on Cresta to determine best way to build topic filters – have heard to use categories, behaviors, etc. 
Monitoring cresta implementation 
New feature or configuration suggestions 
Always want to be able to answer, “How’s it going?” 
Analyzing 
Potential of integrating API’s and reservation data
Henry Drescher
In-Progress
Contact Center [Conversational IVR] 
Working on infrastructure design for data ingestion 
CoPilot backlog items 
Analytics updates for new changes

---

## Update 37

**Date:** 2025-06-27
**Business Area:** Contact Center
**Business Project:** Offer to Cancel (OFTOCX) Model (RCI & CEL)
**People:** Unidentified

### Summarized Update

Ayon
WOW Updates 6/26:
1) specialty V1 hotfixes, code enhancements complete and placed in workflow - accuracy testing to be started from tomorrow
2) MDR V1 hotfixes and code enhancements in place ..completed ETA 7/4
3) Complementary venues Windjammer - ETL, Feature building and Modelling is complete - rules engine yet to complete - ETA on 7/11

### Raw Update

Ayon
WOW Updates 6/26:
1) specialty V1 hotfixes, code enhancements complete and placed in workflow - accuracy testing to be started from tomorrow
2) MDR V1 hotfixes and code enhancements in place ..completed ETA 7/4
3) Complementary venues Windjammer - ETL, Feature building and Modelling is complete - rules engine yet to complete - ETA on 7/11

---

_Source: 20250627 - Raw Weekly Matt and Rafeh Reporting (Raw).docx_