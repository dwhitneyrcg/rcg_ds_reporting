**Proud**

- **Marine Operations:** RCG and Wartsila signed contract to monitor 37 ships for 5 years. MIAP API is planned to be used to share data with Wartsila. Up to $5M capital savings due to in-house IoT solution. DS Team completed feature engineering for adapting HVAC models to ML-class ships and next steps will be model optimization. Also completed IoT pipeline deployments for additional ships (OY and AN) and mapped ID data tags for fuel mass flow meters.

- **Revenue Management (RCI): **DS +MLOPs teams achieved zero downtime for RMA pricing automation as the discount pricing schedule was retired by RCI this week. MLOps team completed an Azure Data Factory Crawler tool that identifies RM datasets still needing to be migrated to Unity Catalog.* **DS Team **working on ensuring ADA Compliance (Berthing Rules and other Inventory Automation algorithms) and SPI model enhancements (that account for Sailing Management factors), while MLOPs team is testing Group Gapping enhancements.*

- **Deployment Port Code GenAI Mappings: **DS Team deployed a Port Mapping API for sharing the “Port Code” PoC with the Deployment Tams, which uses GenAI to adaptively correct port-code mappings scrapped online.

- **PCP Pricing Automation:** Team shared initial pricing-elasticity model for CocoCay Cabanas with Onboard Revenue teams with constructive feedback. Digital teams met with Onboard Revenue teams. *Next steps are to integrate business feedback and begin development of a Dynamic Pricing model for Cabanas.*

- **PCP “****MyCruise****” Product Recommendations:**** **DS team has adapted the PCP Product Recommendations for additional use-cases by the Emails team. *Next week we will begin work on **AI-Based** Recommendations using a combination of demographics based clustering and collaborative filtering.*

- **PROPEL:** MLOps Team launched PROPEL on additional pilot ship this week (Constellation). *Will productionize major enhancements early next week: **(a) Workflow + Alerting framework to help teams ensure targeted offers are shared with shipboard teams at the right team and (b) back-up framework that will enable offers to be pre-generated (in case ship is unable to communicate with shoreside systems).** **DS + Platform teams in discussion **with BCG on AI requirements for PROPEL Phase 2 CAR, which would extend PROPEL offers to RCI, the Digital/App (vs **Physical** Offers), and PCP.*

- **Supply Chain: **DS Team completed productionizing Silversea Demand Forecasting model and added model performance metrics (overall and by category areas) on a Dashboard. Actively working towards enhancing the Uniform Demand Forecasting model with additional feature engineering.

- **Win on Waste: **DS team presented an overview of the demand forecasting methodology during last week’s onboard ship visit with Specialty Dining chefs. *Team is accelerating delivery of main dining room** demand forecasts** after onboarding a new contractor** this week**. *

**Concerned**

- **PCP “****MyCruise****” Product Recommendations:** Digital has requested that the DS+MLOps teams deploy the Product Recommendations PoC API before Cyber code-freeze (9/27). The Data Science and Platform teams will be ready to deliver a daily refresh of the product recommendations through a secure front-end-facing middle layer. However, if the current middle layer implementation is not promptly approved by Front-End Development Teams we will likely miss a release before Cyber code-freeze.

- **Contact Center (Crew HR):***** ***Intent Classification use-case is on hold, until stakeholder approves the purchase of call recording licenses for the crew specific phone calls.

**Excited**

- **Revenue Management (****SSC****):**** **DS and SSC RM Teams identified a workaround “writeback” approach (a manual, bulk upload process) that will enable SSC to achieve daily pricing automation within the next 6-9 months and without additional funding. DS Team completed gathering additional business feedback for optimizing PoC Pricing Recommendations and Business Rules. *Working on integrating** additional** business feedback into future Pricing Recommendations**, **completing initial Pricing Elasticity model. *

- **Contact Center:** DS team actively retraining BK2CX Lead Prioritization model for RCI/CEL and beginning discussions to enhance CTI Lead Prioritization model using Transcript data.

- **E-Commerce: **DS team improved reporting for Model Performance metrics and completed exploratory analysis to improve destination propensity scores by separating booking propensity scores from destination preferences. Team to continue validating audience sizing calculator and validate newest Epsilon spend + demographics datasets.

- **Loyalty:** DS Team planning next phase of analytics work to enhance the forward-looking simulation based on constructive feedback by the Loyalty leadership teams (i.e. include pricing inflation, automatically adjust tiers every 2 years, and more accurately simulate guest spend). *All Loyalty work is being actively transitioned to fall under **the new Loyalty Data Science leader (Kevin Diaz)**.**** ****DS team completed productionization of current Loyalty Simulator with scheduled weekly refreshes and has taken ownership of the Deloitte clustering model (making modifications to adapt for Silversea).*

- **Medallia GenAI Pilot Use-****C****ase: **DS team implemented an initial topic classifier model, but actively refining topics with the Hotel Operations teams and refining classification thresholds to avoid low confidence topics being falsely assigned. *Expecting delivery of the Topic Summarization pilot by end-of-year with a pilot delivered for crew testing in early November.*

- **NPS Target Setting (CEL):**** **Craig Hardeman has requested a deeper dive into actionable NPS drivers to enable business teams to optimize operations. DS team has started building an AI Interpretability module to help business teams identify meaningful relationships between NPS and drivers.

- **RCG-GPT:** MLOps team actively debugging code-blocker for RCG-GPT. *Once this is completed, team will release two versions of ChatGPT (one for business users that includes the code blocker and a second version for software developers without the code blocker).*

- **Revenue Management (CEL):** DS Team completed a pilot MTRB Track Optimization process using Sailing Baskets and shared initial outputs with business teams. *The Track Optimization pilot adapts RCI’s MTRB solution to incentivize sailing alignment for sailings sharing substitutable demand.* *Next steps are to incorporate business feedback into the MT**RB Track Optimization and develop a Mandatory Occupancy Inventory automation solution for CEL. *
