import pandas as pd
# You have the marketing_campaign table, which records in-app purchases by users. 
# Users making their first in-app purchase enter a marketing campaign, where they see call-to-actions for more purchases. 
# Find how many users made additional purchases due to the campaign's success.
# The campaign starts one day after the first purchase. 
# Users with only one or multiple purchases on the first day do not count, nor do users who later buy only the same products from their first day.


# Create the marketing campaign data
data = {
    'user_id': [10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 
                18, 18, 19, 20, 21, 21, 22, 22, 23, 24, 25, 25, 25, 25, 26, 27, 28, 29, 30, 
                31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 43, 44, 44, 45, 45, 46, 
                46, 46, 46, 46, 47, 47, 48, 48, 49, 49, 49, 49, 50, 50, 50, 50, 51, 51, 52, 
                52, 53, 53, 54, 54, 55, 55, 56, 56, 57, 57, 57, 57, 58, 58, 58, 58, 59, 60, 
                61, 62, 63, 64, 65, 66, 67],
    'created_at': ['2019-01-01', '2019-01-02', '2019-03-31', '2019-01-02', '2019-03-31', 
                   '2019-01-02', '2019-03-31', '2019-01-05', '2019-03-31', '2019-01-06', 
                   '2019-01-06', '2019-03-31', '2019-01-08', '2019-01-09', '2019-03-31', 
                   '2019-01-10', '2019-03-31', '2019-01-11', '2019-03-31', '2019-01-12', 
                   '2019-01-12', '2019-01-12', '2019-01-15', '2019-01-16', '2019-01-17', 
                   '2019-01-18', '2019-01-19', '2019-01-20', '2019-01-21', '2019-01-22', 
                   '2019-01-22', '2019-01-24', '2019-01-27', '2019-01-25', '2019-01-26', 
                   '2019-01-27', '2019-01-27', '2019-01-29', '2019-01-30', '2019-01-31', 
                   '2019-01-31', '2019-01-31', '2019-02-03', '2019-02-04', '2019-02-05', 
                   '2019-02-06', '2019-02-07', '2019-02-08', '2019-02-08', '2019-02-10', 
                   '2019-02-11', '2019-03-05', '2019-02-12', '2019-03-05', '2019-02-13', 
                   '2019-03-05', '2019-02-14', '2019-02-14', '2019-03-09', '2019-03-10', 
                   '2019-03-11', '2019-02-14', '2019-03-11', '2019-02-14', '2019-03-12', 
                   '2019-02-18', '2019-02-18', '2019-02-18', '2019-02-18', '2019-02-20', 
                   '2019-02-21', '2019-03-13', '2019-03-14', '2019-02-21', '2019-03-13', 
                   '2019-02-23', '2019-03-18', '2019-02-24', '2019-03-19', '2019-02-25', 
                   '2019-03-20', '2019-02-26', '2019-03-20', '2019-02-27', '2019-03-20', 
                   '2019-02-28', '2019-02-28', '2019-03-20', '2019-03-20', '2019-02-28', 
                   '2019-03-01', '2019-03-02', '2019-03-25', '2019-03-04', '2019-03-05', 
                   '2019-03-26', '2019-03-27', '2019-03-27', '2019-03-27', '2019-03-27', 
                   '2019-03-31', '2019-03-31'],
    'product_id': [101, 119, 111, 105, 120, 112, 110, 113, 118, 109, 107, 112, 105, 110, 
                   116, 113, 107, 116, 104, 114, 113, 114, 117, 105, 114, 113, 118, 119, 
                   114, 114, 115, 114, 115, 115, 104, 101, 111, 111, 104, 117, 117, 110, 
                   117, 102, 102, 113, 120, 115, 114, 105, 102, 104, 105, 102, 119, 105, 
                   102, 102, 102, 103, 103, 110, 105, 115, 105, 106, 114, 112, 116, 118, 
                   118, 118, 118, 120, 108, 117, 112, 120, 105, 119, 110, 117, 117, 115, 
                   116, 105, 106, 108, 103, 104, 101, 119, 102, 117, 114, 120, 106, 120, 
                   105, 103, 107, 102],
    'quantity': [3, 5, 2, 3, 3, 2, 2, 1, 3, 5, 2, 3, 4, 4, 2, 2, 4, 2, 1, 2, 4, 3, 2, 3, 
                 4, 3, 4, 3, 2, 2, 2, 5, 1, 1, 3, 4, 3, 1, 3, 1, 2, 3, 2, 4, 2, 2, 5, 2, 
                 1, 5, 1, 3, 3, 4, 5, 3, 4, 5, 2, 1, 1, 2, 5, 4, 3, 2, 1, 4, 1, 4, 4, 5, 
                 2, 2, 4, 2, 5, 4, 5, 4, 1, 2, 5, 2, 2, 4, 1, 1, 1, 1, 3, 2, 2, 4, 3, 2, 
                 1, 5, 3, 4, 2, 5],
    'price': [55, 29, 149, 234, 99, 200, 299, 67, 35, 199, 27, 200, 234, 299, 499, 67, 
              27, 499, 154, 248, 67, 248, 999, 234, 248, 67, 35, 29, 248, 248, 72, 248, 
              72, 72, 154, 55, 149, 149, 154, 999, 999, 299, 999, 82, 82, 67, 99, 72, 
              248, 234, 82, 154, 234, 82, 29, 234, 82, 29, 35, 199, 199, 299, 234, 72, 
              234, 123, 248, 200, 499, 35, 29, 299, 199, 99, 120, 999, 200, 99, 234, 29, 
              299, 999, 999, 72, 499, 234, 123, 120, 79, 154, 55, 29, 82, 999, 248, 99, 
              123, 99, 234, 79, 27, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert created_at to datetime
df['created_at'] = pd.to_datetime(df['created_at'])

# Data Exploration
print("\nFirst few rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())


# 1. Count of users who made purchases after the Day 1 of their purchase (any purchases on Day 1 do not count)
# 2. Filter out users who purchased same product as Day 1 of their purchase

# Calculate the first purchase 
first_puchases = df.groupby('user_id')['created_at'].min().reset_index()
first_puchases.columns = ['user_id', 'first_purchase_date']
# Merge first purchase dates back to original dataframe
df_with_first = df.merge(first_puchases, on='user_id')
print(df_with_first)
# Find out products purchased on first day for each user
first_day_products = df[df.groupby('user_id')['created_at'].transform('min') == df['created_at']][['user_id', 'product_id']]

# Find users with additional purchases after first day
successful_users = []
for user_id in df['user_id'].unique():
    # Get user's purchases
    user_data = df_with_first[df_with_first['user_id'] == user_id]
    
    # Get first purchase date
    first_day = user_data['first_purchase_date'].iloc[0]
    
    # Get products bought on first day
    first_day_prods = set(first_day_products[first_day_products['user_id'] == user_id]['product_id'])
    
    # Check for purchases after first day with different products
    later_purchases = user_data[user_data['created_at'] > first_day + pd.Timedelta(days=1)]
    
    if not later_purchases.empty:
        later_products = set(later_purchases['product_id'])
        # Check if there are new products (not in first day products)
        if later_products - first_day_prods:
            successful_users.append(user_id)

# Print results
print(f"\nNumber of users who made additional purchases: {len(successful_users)}")
print(f"User IDs who made additional purchases: {sorted(successful_users)}")

