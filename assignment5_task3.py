import pandas as pd

# Load the datasets
customers_df = pd.read_csv('customers.csv')
sales_df = pd.read_csv('sales.csv')

# Step 1: Check for duplicates in both datasets
print("Duplicates in Customers DataFrame:")
print(customers_df.duplicated().sum())  # Count of duplicate rows in customers_df

print("\nDuplicates in Sales DataFrame:")
print(sales_df.duplicated().sum())  # Count of duplicate rows in sales_df

# Step 2: Remove duplicates
customers_df_cleaned = customers_df.drop_duplicates()
sales_df_cleaned = sales_df.drop_duplicates()

# Step 3: Verify that duplicates have been removed
print("\nAfter cleaning, duplicates in Customers DataFrame:")
print(customers_df_cleaned.duplicated().sum())  # Should be 0 if duplicates are removed

print("\nAfter cleaning, duplicates in Sales DataFrame:")
print(sales_df_cleaned.duplicated().sum())  # Should be 0 if duplicates are removed

# Optionally, you can save the cleaned data to new CSV files
# customers_df_cleaned.to_csv('customers_cleaned.csv', index=False)
# sales_df_cleaned.to_csv('sales_cleaned.csv', index=False)
