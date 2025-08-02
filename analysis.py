# analysis.py
import pandas as pd

# Use the full path to load the dataset
file_path = "/Users/ranaabuthaher/Documents/Test/myproject/Dataset/Superstore.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Preview the data
print("✅ Data loaded successfully!")
print(df.head())
# Check for missing values
print("\n🔍 Missing values:")
print(df.isnull().sum())

# Check for duplicates
print("\n📑 Duplicate rows:")
print(df.duplicated().sum())

# Group by 'Region' and calculate total Sales and Profit
region_summary = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)

# Format for better readability
region_summary = region_summary.round(2)

# Display result
print("\n📍 Total Sales and Profit by Region:")
print(region_summary)

