import pandas as pd
import time

# Load the CSV file
customers_df = pd.read_csv('customers.csv')

# Convert the DataFrame into a Python dictionary
customers_dict = customers_df.set_index('CustomerID').to_dict(orient='index')

# Function to filter customers by city using the dictionary
def filter_by_city_dict(customers_dict, city):
    return {customer_id: data for customer_id, data in customers_dict.items() if data['City'] == city}

# Function to filter customers by city using the DataFrame
def filter_by_city_df(customers_df, city):
    return customers_df[customers_df['City'] == city]

# Test the filtering operation using the dictionary
start_time = time.time()
filtered_dict = filter_by_city_dict(customers_dict, 'New York')
end_time = time.time()

print(f"Filtered customers using dictionary: {filtered_dict}")
print(f"Time taken using dictionary: {end_time - start_time} seconds")

# Test the filtering operation using the DataFrame
start_time = time.time()
filtered_df = filter_by_city_df(customers_df, 'New York')
end_time = time.time()

print(f"\nFiltered customers using DataFrame:")
print(filtered_df)
print(f"Time taken using DataFrame: {end_time - start_time} seconds")
