# analysis.py


# Import necessary libraries
import pandas as pd
import numpy as np

# Set display options for better readability
pd.set_option('display.max_columns', None)

# Load the dataset
file_path = '/Users/ranaabuthaher/Documents/Test/myproject/Dataset/Superstore.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Understand the dataset
print("Dataset shape:", df.shape)
print("Dataset columns:", df.columns.tolist())
print("First few rows of the dataset:")
print(df.head())    
print("Dataset info:")
print(df.info())        
print("Dataset description:")
print(df.describe())

# Unique values in one column
# Loop through all object (string) columns
for col in df.select_dtypes(include='object').columns:
    print(f"\nUnique values in column '{col}':")
    print(df[col].unique())

# Data Cleaning and Preparation
# Adjust data types
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce') 
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
print("Dtypes successfully adjusted")
# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values[missing_values > 0])   
# Total number of duplicate rows
print(df.duplicated().sum())

# Create time-based features
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['YearMonth'] = df['Order Date'].dt.to_period('M').astype(str)

# Filter relevant columns
product_df = df[['Order ID', 'Order Date', 'Product Name', 'Sub-Category',
                 'Sales', 'Profit', 'Discount', 'Quantity', 'Year', 'Month', 'YearMonth']]
# Display the first few rows of the cleaned product DataFrame
print(product_df.head())    

