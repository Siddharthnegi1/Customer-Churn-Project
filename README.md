                                                  Customer Churn Analysis – Data Analytics Project

1. Project Title
Customer Churn Analysis Using Python, SQL, and Power BI

2. Problem Statement
Customer churn is a major challenge for subscription-based businesses. High churn rates directly impact revenue and growth. The organization needs a data-driven approach to identify patterns behind customer attrition and take proactive measures to improve retention.

3. Project Objective
The objective of this data analytics project is to:
•	Analyse customer data to identify churn patterns
•	Perform data cleaning and preprocessing
•	Build meaningful KPIs for business insights
•	Visualize churn trends using dashboards
•	Support decision-making with data-driven insights

4. Dataset Description
The dataset contains customer information, including:
•	Customer demographics (Gender, Senior Citizen, Partner, Dependents)
•	Account details (Tenure, Payment Method, Billing Type)
•	Services subscribed (Internet, Streaming, Tech Support, etc.)
•	Financial data (Monthly Charges, Total Charges)
•	Target variable: Churn (Yes/No)

5. Tools & Technologies
•	Python (Pandas, NumPy) – Data cleaning & preprocessing
•	SQL (PostgreSQL) – Data storage and querying
•	Power BI – Data visualization and dashboard creation
•	DAX – KPI and metric calculations

6. Methodology
6.1 Data Collection
•	Imported dataset from CSV file (Customer.csv)
6.2 Data Cleaning & Preprocessing
•	Checked dataset structure and data types
•	Handled missing values in Total Charges
•	Converted data types from string to numeric
•	Removed duplicates
•	Renamed columns for consistency
6.3 Data Transformation
•	Created structured dataset (clean_file.csv)
•	Standardized column naming conventions
•	Prepared dataset for analysis
6.4 Data Storage
•	Loaded cleaned data into PostgreSQL database
•	Created table: customer

7. Data Analysis (Power BI)
7.1 Key KPIs
•	Churn Rate (%)
•	Customer Count
•	Average Monthly Charges
7.2 DAX Measures Used
•	Churn calculation (Yes → 1, No → 0)
•	Percentage calculations using DIVIDE()
•	Segmentation using SWITCH()

7.3 Analysis Performed
1. Customer Demographics
•	Churn by gender
•	Churn by senior citizen status
•	Impact of partner and dependents
2. Tenure Analysis
•	Customers grouped based on years
•	Identified high churn in early-stage customers
3. Service-Based Analysis
•	Churn vs services like:
o	Tech Support
o	Online Security
o	Streaming Services
4. Payment & Billing Insights
•	Impact of payment methods on churn
•	Paperless billing behaviour

8. Key Insights
Based on the analysis, the following deeper insights were identified:
8.1 Customer Lifecycle Insights
•	New customers (0–1 year tenure) show the highest churn rate
•	Indicates weak onboarding experience or unmet expectations early in the journey
8.2 Service Adoption Insights
•	Customers without Tech Support and Online Security are significantly more likely to churn
•	Value-added services play a critical role in retention
8.3 Customer Engagement Insights
•	Customers using multiple services (bundled services) have lower churn
•	Higher engagement = higher retention
8.4 Revenue & Pricing Insights
•	Customers with higher monthly charges but low perceived value tend to churn
•	Pricing without value justification increases attrition
8.5 Behavioural Insights
•	Certain payment methods (e.g., month-to-month contracts) show higher churn
•	Customers prefer flexibility but are also more likely to leave

9. Solutions & Recommendations to Reduce Churn
Based on the insights, the following actionable strategies are recommended:
9.1 Improve Customer Onboarding
•	Introduce guided onboarding programs for new customers
•	Provide early support (first 30–60 days critical)
•	Offer tutorials, welcome offers, or onboarding calls

9.2 Promote Value-Added Services
•	Bundle Tech Support + Online Security with core plans
•	Offer discounts on service upgrades
•	Educate customers about benefits of these services

9.3 Introduce Customer Retention Programs
•	Loyalty rewards for long-term customers
•	Special offers for high-risk churn segments
•	Personalized retention campaigns

9.4 Optimize Pricing Strategy
•	Align pricing with perceived value
•	Offer flexible plans with clear benefits
•	Provide discounts for long-term contracts

9.5 Enhance Customer Engagement
•	Use targeted communication (emails, notifications)
•	Recommend services based on customer usage
•	Increase touchpoints with customers

9.6 Predictive & Proactive Approach
•	Implement churn prediction models using machine learning
•	Identify high-risk customers in advance
•	Trigger automated retention actions

10. Conclusion
This project demonstrates how data analytics can be used to:
•	Identify customer behaviour patterns
•	Detect key drivers of churn
•	Provide actionable solutions to improve retention
By combining Python, SQL, and Power BI, the project builds a complete analytics pipeline and transforms raw data into meaningful business strategies.


11. Project Outcome
•	Cleaned and structured dataset
•	Database-ready customer data
•	Interactive Power BI dashboard
•	Actionable business insights and retention strategies

12. References
•	Pandas Documentation
•	PostgreSQL Documentation
•	Power BI & DAX Documentation

13. Screenshot of the Dashboard
•	Main page- Customer Demographics.
( https://github.com/Siddharthnegi1/Customer-Churn-Project/blob/main/Screenshot%20Folder/1.%20Main%20page%20-%20customer%20demographics.png )

•	Customer Overview.
( https://github.com/Siddharthnegi1/Customer-Churn-Project/blob/main/Screenshot%20Folder/2.%20Customer%20account%20overview.png )

•	Customer Subscribed Services.
( https://github.com/Siddharthnegi1/Customer-Churn-Project/blob/main/Screenshot%20Folder/3.%20Customer%20subscribed%20services.png )





