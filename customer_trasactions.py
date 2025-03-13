from collections import defaultdict


transactions = [
    {"customer_id": 101, "transaction_date": "2024-01-15", "amount": 120.50, "category": "Electronics"},
    {"customer_id": 102, "transaction_date": "2024-01-16", "amount": 75.20, "category": "Clothing"},
    {"customer_id": 101, "transaction_date": "2024-01-20", "amount": 45.00, "category": "Groceries"},
    {"customer_id": 103, "transaction_date": "2024-01-25", "amount": 200.00, "category": "Electronics"},
    {"customer_id": 102, "transaction_date": "2024-01-28", "amount": 35.50, "category": "Groceries"},
    {"customer_id": 101, "transaction_date": "2024-02-05", "amount": 150.00, "category": "Electronics"},
    {"customer_id": 101, "transaction_date": "2024-02-10", "amount": 65.75, "category": "Groceries"},
    {"customer_id": 102, "transaction_date": "2024-02-12", "amount": 89.99, "category": "Clothing"},
    {"customer_id": 103, "transaction_date": "2024-02-15", "amount": 120.25, "category": "Home & Garden"},
    {"customer_id": 104, "transaction_date": "2024-02-18", "amount": 250.00, "category": "Electronics"},
    {"customer_id": 105, "transaction_date": "2024-02-20", "amount": 45.50, "category": "Books"},
    {"customer_id": 104, "transaction_date": "2024-02-25", "amount": 35.25, "category": "Groceries"},
    {"customer_id": 105, "transaction_date": "2024-03-01", "amount": 78.99, "category": "Books"},
    {"customer_id": 103, "transaction_date": "2024-03-05", "amount": 175.00, "category": "Electronics"},
    {"customer_id": 104, "transaction_date": "2024-03-08", "amount": 299.99, "category": "Electronics"},
    {"customer_id": 102, "transaction_date": "2024-03-10", "amount": 65.00, "category": "Groceries"},
    {"customer_id": 101, "transaction_date": "2024-03-12", "amount": 189.50, "category": "Electronics"},
    {"customer_id": 105, "transaction_date": "2024-03-15", "amount": 120.75, "category": "Books"},
    {"customer_id": 103, "transaction_date": "2024-03-18", "amount": 55.25, "category": "Home & Garden"},
    {"customer_id": 104, "transaction_date": "2024-03-20", "amount": 45.00, "category": "Books"}
]

# 1. Calculate the total amount spent by each customer.

def calculate_amount_spent(transactions):
    amount_spent = 0
    for transaction in transactions:
        amount_spent += transaction["amount"]
    return amount_spent
print("Total amount spent on all trsactions = ",calculate_amount_spent(transactions))

# 2. Find the customer who spent the most in the "Electronics" category.

def get_top_electronics_customer(transactions):
    #initialize a dictionary to store the total amount spent by each customer on electronics
    electronics_spend = defaultdict(float)
    for transaction in transactions:
    # Check if the transaction is in the "Electronics" category
        if transaction["category"] == "Electronics":
            customer_id = transaction["customer_id"]
            amount = transaction["amount"]
    # Add the amount spent to the customer's total
            electronics_spend[customer_id] += amount
    # Find the customer with the highest total using max()
    top_customer_id = max(electronics_spend, key=electronics_spend.get)
    # Return the customer ID and total amount spent
    return  {
        "customer_id": top_customer_id,
        "total_amount_spent": electronics_spend[top_customer_id]
    }
print("The customer who spent the most in Electronics is:",get_top_electronics_customer(transactions))
                
# 3. Create a dictionary mapping each customer to their most frequently purchased category.
def get_most_purchased_category(transactions):
    customer_category_count = defaultdict(lambda: defaultdict(int))
    for trasaction in transactions:
        customer_id = trasaction["customer_id"]
        category = trasaction["category"]
        customer_category_count[customer_id][category] += 1
    customer_most_purchased_category = defaultdict(list)
    for customer_id, category_count in customer_category_count.items():
        print("Customer Category Count:", customer_id, category_count)
        # Find the category with the highest count
        max_count = max(category_count.values())
        # Get all categories with the highest count
        most_purchased_categories = [category for category, count in category_count.items() if count == max_count]
        # Add the customer and their most purchased category to the dictionary
        customer_most_purchased_category[customer_id] = most_purchased_categories
    
    return customer_most_purchased_category
print("The most frequently purchased category by each customer is:",get_most_purchased_category(transactions))
# 4. Calculate the average transaction amount per category, rounded to two decimal places. - Easy (Basic grouping with mean calculation)
def calculate_avg_transaction_amouunt(transactions):
    category_total = defaultdict(float)
    category_count = defaultdict(int)
    for transaction in transactions:
        category = transaction["category"]
        amount = transaction["amount"]
        category_total[category] += amount
        category_count[category] += 1
    category_avg = {category: round(category_total[category] / category_count[category], 2) for category in category_total}
    return category_avg
print("The average transaction amount per category is:",calculate_avg_transaction_amouunt(transactions))