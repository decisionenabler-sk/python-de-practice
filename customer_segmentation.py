from collections import defaultdict


customers = [
    {
        "customer_id": "C001",
        "age": 35,
        "gender": "M",
        "location": "New York",
        "membership_level": "Gold",
        "purchases": [
            {"date": "2023-01-15", "product_category": "Electronics", "amount": 599.99},
            {"date": "2023-02-10", "product_category": "Clothing", "amount": 129.50},
            {"date": "2023-03-05", "product_category": "Electronics", "amount": 349.99},
        ],
    },
    {
        "customer_id": "C002",
        "age": 28,
        "gender": "F",
        "location": "Los Angeles",
        "membership_level": "Silver",
        "purchases": [
            {"date": "2023-01-20", "product_category": "Beauty", "amount": 89.99},
            {"date": "2023-02-15", "product_category": "Clothing", "amount": 199.99},
            {"date": "2023-03-10", "product_category": "Home", "amount": 149.50},
            {"date": "2023-04-05", "product_category": "Beauty", "amount": 75.25},
        ],
    },
    {
        "customer_id": "C003",
        "age": 45,
        "gender": "M",
        "location": "Chicago",
        "membership_level": "Bronze",
        "purchases": [
            {"date": "2023-01-25", "product_category": "Home", "amount": 299.99},
            {"date": "2023-03-15", "product_category": "Home", "amount": 199.99},
        ],
    },
    {
        "customer_id": "C004",
        "age": 32,
        "gender": "F",
        "location": "New York",
        "membership_level": "Gold",
        "purchases": [
            {"date": "2023-01-10", "product_category": "Electronics", "amount": 799.99},
            {"date": "2023-02-20", "product_category": "Beauty", "amount": 129.99},
            {"date": "2023-03-20", "product_category": "Electronics", "amount": 449.99},
            {"date": "2023-04-10", "product_category": "Clothing", "amount": 249.99},
        ],
    },
    {
        "customer_id": "C005",
        "age": 50,
        "gender": "M",
        "location": "Los Angeles",
        "membership_level": "Silver",
        "purchases": [
            {"date": "2023-02-05", "product_category": "Home", "amount": 599.99},
            {"date": "2023-03-25", "product_category": "Home", "amount": 399.99},
            {"date": "2023-04-15", "product_category": "Clothing", "amount": 159.99},
        ],
    },
]
# Questions:

#1. Calculate the total spending and average purchase amount for each customer.
#2. Create a function to identify each customer's preferred product category (most purchased).
#3. Implement a function to segment customers into groups based on their spending behavior (low, medium, high) and membership level.
#4. Design an algorithm to find purchasing patterns, such as customers who buy products from the same category consecutively.
#5. Create a function to calculate the monthly spending trend for each customer.

def calculate_per_customer_spending(customers):
    customer_total_spending = defaultdict(float)
    customer_avg_spending = defaultdict(float)
    for customer in customers:
        for purchase in customer["purchases"]:
            customer_total_spending[customer["customer_id"]] += purchase["amount"]
        customer_avg_spending[customer["customer_id"]] = customer_total_spending[customer["customer_id"]]/len(customer["purchases"])
    return customer_total_spending, customer_avg_spending
print("Total spending and average purchase amount for each customer = ",calculate_per_customer_spending(customers))

def get_customer_preferred_category(customers):
    customer_category_count = defaultdict(lambda: defaultdict(int))
    for customer in customers:
        for purchase in customer["purchases"]:
            customer_category_count[customer["customer_id"]][purchase["product_category"]] += 1
    customer_preferred_category = {}
    for customer, categories in customer_category_count.items():
        preferred_category = max(categories, key=categories.get)
        customer_preferred_category[customer] = preferred_category
    return customer_preferred_category
print("Each customer's preferred product category = ",get_customer_preferred_category(customers))