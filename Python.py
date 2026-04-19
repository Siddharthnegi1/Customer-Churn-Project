# ----         Customer Churn Project Using Python               ------#


import pandas as pd
import numpy as np
df=pd.read_csv("Customer.csv")

print(df.head(5))
print(df.columns)
print(df.info())
print(df.describe(include='all'))

print(df["tenure"].dtype)


print(df["TotalCharges"].dtype)
print(df[df["TotalCharges"].str.contains(" ")])
df["TotalCharges"]=df["TotalCharges"].replace(" ",np.nan)
df["TotalCharges"]=pd.to_numeric(df["TotalCharges"])
df["TotalCharges"]=df["TotalCharges"].fillna(df["TotalCharges"].mean())


print(df.isnull().sum())
print(df.duplicated().sum())


df = df.rename(columns={
    "customerID": "Customer_id",
    "gender": "Gender",
    "SeniorCitizen":"Senior_citizen",
    "tenure": "Tenure",
    "PhoneService":"Phone_service",
    "MultipleLines":"Multiple_lines",
    "InternetService":"Internet_service",
    "OnlineSecurity":"Online_security",
    "OnlineBackup":"Online_backup",
    "DeviceProtection":"Device_protection",
    "TechSupport":"Tech_support",
    "StreamingTV":"Streaming_tv",
    "StreamingMovies":"Streaming_movies",
    "PaperlessBilling":"Paperless_billing",
    "PaymentMethod":"Payment_method",
    "MonthlyCharges":"Monthly_charges",
    "TotalCharges":"Total_charges",})

print(df.info())

print(df.columns)

df.to_csv("clean_file.csv",index=False)

from sqlalchemy import create_engine

username="postgres"
password="abcd"
host="localhost"
port="1111"
database="customer_db"

engine= create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

table_name="customer"
df.to_sql(table_name,engine,if_exists="replace",index=False)

print(f"Data successfully loaded into table '{table_name}' in database'{database}'.")
