**DAVID**** **

**Proud **

**CLTV Analysis: DS Team delivered CLTV calculations for the Royal Brand that includes indexing for more profitable segments, which Corporate Planning presented yesterday to the Royal Leadership team with constructive feedback.***** Future work will focus on delivering CLTV calculations for the CEL brand and performing a deeper dive into the unique behavior and drivers for different CLTV segments (from a marketing perspective).***** **

**Global Marine Operations: Completed migration of HVAC, Machinery, Hotel Apps from MIAP to GMO App and delivered an enhanced AI outlier removal tool. *****Actively developing new power plan optimization model for fuel forecasting.***** **

**PROPEL: MLOPs Team delivered enhanced ShoreX logic to be more personalized/granular, instead of a generic offering (private journeys, destination highlights, and any shorex). This delivery will reduces cannibalization and overall shorex margins. **

**Win-on-Waste: Productionized enhanced forecasts for Specialty Dining Venues with XDining Guardrails. Presented a demo of the new forecasting models to WoW Leadership (Lincoln, Patrick, Paul and other stakeholders) on 12/16. **

**Revenue Management (SSC): DS/DE have delivered an end-to-end pipeline for the Silversea Pricing Recommendation Engine that includes limited writeback capability. *****Will be ready next year for a phased-roll out of pricing recommendations across the Silversea fleet.***** **

**  **

**Excited **

**Contact Center: DS Team actively working on productionizing CEL Lead Scoring models. **

**Generative AI Medallia Text Summarization (Hotel Operations): DS team will be presenting our pilot results of the text summarization tools to the operations teams today.  **

**Loyalty Simulator: DS Team completed backtesting the results of 6different modeling scenarios with new forward-looking tier mapping tool and will be sharing results with the Loyalty teams in early January. *****Team actively working to improve spend forecasts, which still don’t capture the full distribution of historical guest spend.***** **

**Supply Chain: DS Team completed revisions of Supply Chain CAR memo and resubmitted to Capital Planning. Delivered performance documentation for all Demand Forecasting pipelines, that altogether generate 100+ datasets, to assist business and data engineering teams to identify process optimization steps and unnecessary datasets.  **

**Revenue Management (RCI): DS Team actively working on enhancements to PRE, elasticities, Mandatory Occupancy, & GTY-Lead models and developed an POC GTY Replenishment algorithm that sensitizes it to Cabin Category class different. *****Team also held multiple planning sessions with business for 2025 deliveries.*****  **

**Revenue Management (CEL): DS Team actively working on delivering the GTY-Lead model and enhancements to the MTRB Track Optimization algorithm that will not only incentivize sailing alignment, but optimize tracks for Sailing Performance targets. **

**PCP Pricing Automation: Completed implementation of the Outlier Removal into the Pricing Recommendations Engine Pipeline for Cabanas and have selected RCI sailings for a January AB Test to evaluate the beneficial impact of AI-generated pricing recommendations. *****Early next year, the team will conduct rigorous testing to ensure pricing recommendations are beneficial to the RCI/CEL onboard revenue teams and, pending positive results, will begin a phased-roll out.  ***** **

**  **

**Concerned **

**None **

** **

** **

** **

**Celebrity Win: No major deliveries this week. **

**GMO**

* Completed migration of HVAC, Machinery, Hotel Apps from MIAP to GMO App.
* Reviewing baselines of service power models.
* Implemented enhanced version of Kalman Filter based outlier removal method.
* Progress with development of new power plant optimization package for fuel forecast project.

**Loyalty: **
Last week we ran 6 different modeling scenarios. Much of this week was spent evaluating results from those and consolidating findings for the business. Overall the models are outperforming the previous iterations in the backtested period. Models tend to follow seasonality well and mirror movements in actual spend. Raw spend models consistently under-predict spend, as tree-based models tend to predict towards the mean and don't preserve distributions well. An initial pass at a post-hoc adjustment to match historical distributions was completed, but now overstates spend. We will continue to iterate on these adjustments. There are several planned feature and data improvements that will further enhance model predictions. These include: 
1. Indexing historic guest spend against other passengers in similar cabins on the same sailing. This will remove confounds from seasonality and product.
2. Adding velocity and historical spend trend instead of relying only on previous spend. The current method does not take into account ramping up or down of spend over time and assumes a steady-state.
3. Inclusion of RM and strat plan NTR and PCD forecasts. This will allow us to put guard rails to ensure total spend matches business expectations. We will allocate expected spend from the business to the guest level based on our model outputs. 
4. Improvements to the scaling algorithm to more closely match historical distributions.

CLTV: 
Initial calculations have been completed for the Royal brand and were presented to brand leaders on 12/19. These discussions centered around methodology and potential use-cases, such as targeting higher indexing segments in net-new guests. A key point of discussion was that all segments are profitable and have value to the business, but a deeper understanding on segment behavior and drivers will improve marketing decisions. The data cuts that have been completed so far, are higher level cuts and need further investigation and refinement. Celebrity brand will be included in the new year and similar conversations will take place with brand leadership. 

The short-term solution relies on marrying tables and views from different business units with manual calculations done by the business. In the new year, work will be done in partnership with data engineering to create a long-term solution that will rely on source tables and automating business calculations.

GSCBP:
• Further review and refinements to CAR Memo and Presentation
• Documentation of our 6 major pipelines.
o Documented the inflows and outflows of data in each notebook along with compute time.
o Work is in progress, but so far have documented over 30 notebooks, with over 100 tables along with for each table created, the notebook that it was created and every subsequent notebook that uses that table.
o Presented work to Yan and Ricky. Ricky wants us to show it to Data Governance when completed. Documentation work is on track for completion before the holiday. Deliverable is an Excel file (GSCBP Data Flow Documentation.xlsx ) and PowerPoint (Data Review and Documentation.pptx)
• Reporting maintenance:
o Correct when a Product Name has a quotation character that adversely affects readability in Excel reports
o Added additional originating port codes for classifying demand by region
• Validation of tables that are being migrated from Synapse to Unity Catalog.
• Optimization of procurement ordering blending demand forecasts, historical PO data, ship location and historical consumption data in progress. Got an initial test working, but need to now bring in master load schedule data with a new objective function to test cost minimization using one ship and product. 
Update for Loyalty guest simulator
• Improve "stretching" of spend model by adding more bins
• Code peer-review with Kevin
eCommerce:
• Completed first version of sister brand models reports for the dashboard

PROPEL: MLOPs Team delivered enhanced ShoreX logic to be more personalized/granular, instead of a generic offering (private journeys, destination highlights, and any shorex). This delivery will reduces cannibalization and overall shorex margins.

Ayon:

WOW Team Update:

1) Completed Unit testing and Integration testing for Hybrid modelling for WOW specialty (AI+ Xdinning Guardrail model) -- Ongoing integration testing for stage

2) Presented to Lincoln, Patrick , Paul and other stakeholders the Hybrid model demo on 12/16

3) Modular code completed so it can be refactored and reused for MDR

-----

Parimala

Working on Celebrity Lead Scoring model's production deployment activities

The lead scoring model's training and prediction code were successfully pushed to the Git repository and merged with the main branch.

Feature branches were created to implement changes to the training and prediction code based on your feedback.

Contact Center: DS Team actively working on productionizing CEL Lead Scoring models.
