**Proud:**

- **Generative AI Medallia Pilot (RCI): **DS Team delivered an ad-hoc 2-page summary for CEL Casino Guest Experiences. Team developed new internal tools to evaluate the effectiveness of different Generative AI prompts to summarize guest feedback and completed a PoC self-service approach for parsed guest comments. *Team now working to deploy prompting to summarize guest feedback (and finish backfilling 2024 surveys).*

- **Revenue Management (SSC):** Presented an overview of new PRE Pricing Recommendations to SSC Revenue Management leadership with positive feedback. *Next steps are to work with teams to test the semi-automated PRE writeback process with SSC, incorporate final feedback on pricing recommendations by the Product Teams, and then setup a pilot test of the new pricing recommendations. *

- **Supply Chain:** DS Team presented the “2025 Global Supply Chain Expansion” CAR to the Capital Committee on Monday with constructive feedback and answered additional CAR questions raised by Capital Planning.  Team delivered a new challenger model for HF&B products (12-month rolling average). *N**ow focusing on **backtesting** SSC demand forecasting predictions.*

- **Win-on-Waste:** Expanded coverage to include a new Specialty Dining Venue (Teppeniaki). *Testing mostly complete on Main Dining Room demand forecasts and will productionize new models after business teams fix menu metrics (TBD).*

**Excited:**

- **Contact Center (CEL): **DS Team nearing completion of productionizing new Lead Prioritization models and next steps are to set up RFP for deployment with IT.

- **E-Commerce:** DS Team focused on integrating new promotional even data into uplift models and add remaining reports for cross/sister brand models into the Dashboard.

- **Product Recommendation Engine (Digital): **DS Team working to enable front-end to request multiple recommendations in a single API request, refresh email recommendations daily (and include current Hybris pricing), and continuing to develop “For You” AI recommender models (i.e. customers who bought x also bought y).

- **Revenue Management (RCI):** DS Team working on PRE capped pricing & inversion gapping business rule adjustments, developing a new PoC pricing elasticity models (by 1/23), updating Category Gapping (GTY-Lead) optimization model based on business feedback, beginning exploratory analysis to build automation to reduce overselling, and developing updated ADA compliance rules for berthing automation.

- **Revenue Management (CEL): **DS Team shared updated Category Gapping (GTY-Lead) optimization model outputs with constructive feedback. Actively working on improving stale-pricing for PRE, updating Category Gapping (GTY-Lead) optimization model based on business feedback and implementing new PRE inversion gapping business rule logic.

- **PCP Pricing Automation:** DS Team created pilot RCI pricing recommendations and model revenue uplift metrics for upcoming Perfect Day Cabanas test.

- Update for GSCBP
1. Answered Capital Committee pending questions on the CAR about the amount of OpEx attributable to prior work done in the RCI/CCI HF&B pilot that could be removed from the CAR. The answer was that the maintenance of the Silversea and RCG Uniform & Health products accounts for 100% of the OpEx costs listed in the CAR. The amount requested is the minimal amount of support required to complete this work and reducing that OpEx amount, will prevent the ability from us to achieve our future goals. As an added benefit, since this dataset is Crunchtime, the OpEx maintenance work for these products also ensures maintenance of the RCI/CCI HF&B products at no added cost. 
2. Added new 12-month rolling average challenger model for RCI/CCI HF&B products and added reporting on our dashboard. 
3. Code update was required on the RCI/CCI HF&B pipeline, as the new year, necessitated an adjustment to prior code that was working, but stopped working in the new year change. 
4. Began work engineering new dataset for Silversea unifying the monthly demand forecasts for a product/ship, with the purchasing dataset from the Silversea Spend Report, and calculating the median value from the AI Demand model, average monthly purchase quantity, and average monthly consumption along with the absolute percent error of this median value for the backtested month from these three data points, relative to the actuals in the backtested month. 

Update for E-Commerce
1. Models maintenance: 
o EDA of new promo events tables planned to be used on uplift computation ticket
(CIU_EM_SENT, CIU_EM_RESPONSE, CIU_EM_SENDLOG, CIU_EM_SENDJOB)
2. Dashboard: 
o Integrate and deploy to production all the pending reports of cross/sister brand models in the dashboard (score, train, and calculator estimator reports)

- Medallia GenAI 
Working towards deploying version 8 of data transformation and back filling 2024 Surveys. 
- Delivered adhoc 2 page summary for Gang relating to CEL Casino guests
- Developed internal EDA notebook for Medallia Surveys which compares data differences between different versions of the Structured data transformations
- For example comparing average length of sentence between Prompt A vs Prompt B
- Gaurav implemented POC Search functionality over parsed_comments which would satisfy the self-serve analytics use case

CTI 
Nearing completion of model deployment to prod environment. Stakeholder is eager to move to prod. Will need to set up RFP for deployment with Shan Garg in IT. 
- Created a new utils folder to house the helper.py file, which assigns a dynamic environment containing the catalog.schema name.
- Updated all highlighted code sections in the training and production notebooks to utilize the function from helper.py.
- Replaced the table creation of cti_base in the feature engineering notebook with a view.
- Enhanced the prediction notebook by adding logic to process leads from the last 12 hours. Adjusted the feature engineering notebook for training to identify the minimum rccl_load_id beyond 12 hours and a created_date later than 2021-12-31.
- Modified the prediction notebook to append every prediction result to the table, with final results fetched based on the most recent execution time.

WOW
1) Added Teppeniaki for specialty
2) MDR hybrid is developed and tested -- status : waiting for business to fix menu metrics so we can productionalize

Addition WoW notes:
MDR - looked into the prediction performance for proteins
Found forecast values are slightly under - but in the right ballpark
Issues: Preds for days that were not valid according to menu assignment and mismatch between records of items actual served vs planned to be served
re-applied the menu assignment filtering for preds later in the PL resolved the wrong day pred issue
investigating the Actual vs Planned issue - found entire menu shifts and substitutions.
captured examples, volumes, and counts of mismatches to share with Paul & team
Tested the MDR pipeline - noticed the menu assignment table has not been updated with future dates - checked with table creator. Will run back tests instead.
Advised Gourish with his 'popular protein items', 'add new specialty venue', & recipe_type tasks

Email Recommendations
- Need to refresh data every day by 4AM 
- Need to test load time to SFMC
- Plan to add price as part of data load
- Data quality corrections such as HTML in descriptions and adding DateTime of run column

PCP
Deployed Urgent adhoc request to enable frontend to request for multiple recommendations in a single request. Additionally frontend can specify the product count limits for each requested column. 
- Working to deploy same-port Aprior model (customers who bought x also bought y)
- Need to brainstorm approach for Aprior model for different-port
- Need additional dev time for ForYou model

Search 
- Meeting with Frontend devs to discuss potential of AlphaPlatform developed Search API
