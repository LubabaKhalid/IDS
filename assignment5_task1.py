import pandas as pd

# Load the datasets
customers_df = pd.read_csv('customers.csv')
sales_df = pd.read_csv('sales.csv')

# Display the first few rows of the customers dataset
print("Customers DataFrame:")
print(customers_df.head())

# Display the first few rows of the sales dataset
print("\nSales DataFrame:")
print(sales_df.head())

# Show the shape (number of rows and columns) of each dataset
print("\nShape of Customers DataFrame:", customers_df.shape)
print("Shape of Sales DataFrame:", sales_df.shape)

# Check for missing values in both datasets
print("\nMissing values in Customers DataFrame:")
print(customers_df.isnull().sum())

print("\nMissing values in Sales DataFrame:")
print(sales_df.isnull().sum())

# Handle missing values
# For customers dataset, fill missing Age with the median value
customers_df['Age'] = customers_df['Age'].fillna(customers_df['Age'].median())

# For sales dataset, fill missing Product with the most frequent value
sales_df['Product'] = sales_df['Product'].fillna(sales_df['Product'].mode()[0])

# Check again for missing values after handling them
print("\nMissing values after handling in Customers DataFrame:")
print(customers_df.isnull().sum())

print("\nMissing values after handling in Sales DataFrame:")
print(sales_df.isnull().sum())
