transactions = [
    {"customer_id": 101, "transaction_date": "2024-01-15", "amount": 120.50, "category": "Electronics"},
    {"customer_id": 102, "transaction_date": "2024-01-16", "amount": 75.20, "category": "Clothing"},
    {"customer_id": 101, "transaction_date": "2024-01-20", "amount": 45.00, "category": "Groceries"},
    {"customer_id": 103, "transaction_date": "2024-01-25", "amount": 200.00, "category": "Electronics"},
    {"customer_id": 102, "transaction_date": "2024-01-28", "amount": 35.50, "category": "Groceries"},
    {"customer_id": 101, "transaction_date": "2024-02-05", "amount": 150.00, "category": "Electronics"}
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
    electronics_spend = {}
    for transaction in transactions:
        if transaction["category"] == "Electronics":
            customer_id = transaction["customer_id"]
            amount = transaction["amount"]
            electronics_spend[customer_id] = electronics_spend.get(customer_id, 0) + amount
    # Find the customer with the highest total using max() with a key function
    top_customer_id = max(electronics_spend, key=electronics_spend.get)
    return  {
        "customer_id": top_customer_id,
        "total_amount_spent": electronics_spend[top_customer_id]
    }
print("The customer who spent the most in Electronics is:",get_top_electronics_customer(transactions))
                
# 3. Create a dictionary mapping each customer to their most frequently purchased category.
def get_most_purchased_category(transactions):
    customer_category_count = {}
    for trasaction in transactions:
        customer_id = trasaction["customer_id"]
        category = trasaction["category"]
        customer_category_count[customer_id] = customer_category_count.get(customer_id, {})
        customer_category_count[customer_id][category] = customer_category_count[customer_id].get(category, 0) + 1
    customer_most_purchased_category = {}
    for customer_id, category_count in customer_category_count.items():
        most_purchased_category = max(category_count, key=category_count.get)
        customer_most_purchased_category[customer_id] = most_purchased_category
    return customer_most_purchased_category
print("The most frequently purchased category by each customer is:",get_most_purchased_category(transactions))
# 4. Calculate the average transaction amount per category, rounded to two decimal places. - Easy (Basic grouping with mean calculation)
# Beep bop...