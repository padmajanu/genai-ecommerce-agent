import pandas as pd
import sqlite3

# Paths to your CSVs
ad_metrics_csv = "data/ad_metrics.csv"
total_sales_csv = "data/total_sales.csv"
eligibility_csv = "data/eligibility.csv"

# Output DB file
db_path = "ecommerce.db"

# Connect to SQLite DB
conn = sqlite3.connect(db_path)

# Load and insert each dataset
print("Creating tables and loading data...")

df_ad = pd.read_csv(ad_metrics_csv)
df_ad.to_sql("ad_metrics", conn, if_exists="replace", index=False)

df_sales = pd.read_csv(total_sales_csv)
df_sales.to_sql("total_sales", conn, if_exists="replace", index=False)

df_eligibility = pd.read_csv(eligibility_csv)
df_eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)

print("✅ Database created and data loaded into tables.", flush=True)

conn.close()
