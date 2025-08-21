from collections import defaultdict, deque
from datetime import datetime, timedelta
# Build an inverted index for stock price alerts. Map each stock ticker to the set of user IDs who have alerts for that stock, considering different alert types.
alerts = [
    {'alert_id': 1, 'user_id': 'u1', 'tickers': ['AAPL', 'GOOGL'], 'type': 'price_above'},
    {'alert_id': 2, 'user_id': 'u2', 'tickers': ['AAPL', 'TSLA'], 'type': 'price_below'},
    {'alert_id': 3, 'user_id': 'u3', 'tickers': ['MSFT'], 'type': 'volume_spike'},
    {'alert_id': 4, 'user_id': 'u1', 'tickers': ['TSLA', 'MSFT'], 'type': 'price_above'},
    {'alert_id': 5, 'user_id': 'u4', 'tickers': ['AAPL'], 'type': 'earnings'}
]

# Expected output:
# {
#   'AAPL': ['u1', 'u2', 'u4'],
#   'GOOGL': ['u1'],
#   'TSLA': ['u1', 'u2'],
#   'MSFT': ['u1', 'u3']
# }

def get_user_alerts(alerts):
    stock_user_alerts = defaultdict(set)
    for alert in alerts:
        for ticker in alert['tickers']:
            stock_user_alerts[ticker].add(alert['user_id'])
    stock_user_alerts = {ticker:sorted(users) for ticker,users in stock_user_alerts.items()}
    return stock_user_alerts
# Test
# print(get_user_alerts(alerts))
# Verify if a user has permission to perform certain trading actions based on their account roles and role permissions.
user_roles = {
    'u1': {'basic_trader', 'options_trader'},
    'u2': {'basic_trader'},
    'u3': {'basic_trader', 'options_trader', 'crypto_trader'},
    'u4': {'premium_trader'}  # premium_trader inherits all permissions
}

role_permissions = {
    'basic_trader': {'buy_stock', 'sell_stock', 'view_portfolio'},
    'options_trader': {'buy_options', 'sell_options', 'view_options_chain'},
    'crypto_trader': {'buy_crypto', 'sell_crypto', 'view_crypto_prices'},
    'premium_trader': {'buy_stock', 'sell_stock', 'view_portfolio', 'buy_options', 
                      'sell_options', 'view_options_chain', 'margin_trading', 'after_hours'}
}
def has_permission(user, permission):
    # Get user's roles
    user_roles_set = user_roles.get(user, set())
    
    # Check if user has premium_trader role (has all permissions)
    if 'premium_trader' in user_roles_set:
        return True
    
    # Check each of user's roles for the permission
    for role in user_roles_set:
        if permission in role_permissions.get(role, set()):
            return True
            
    return False
# Test :
# print(has_permission('u1', 'buy_options')) # -> True
# print(has_permission('u2', 'buy_options')) # -> False
# print(has_permission('u3', 'buy_crypto')) # -> True
# print(has_permission('u4', 'margin_trading')) # -> True

# Aggregating Fractional Share Orders

# Consolidate_orders that takes a list of fill records (each represented as a dictionary). 
# For each unique order_id, you must produce a single summary record that includes:
# The original order_id, total quantity of shares purchased for that order.
# The volume-weighted average price (VWAP) for the entire order. The VWAP is calculated as Σ(quantity * price) / Σ(quantity).
# A list of all unique fill_ids that contributed to the order.

fills = [
    {'order_id': 'o_101', 'fill_id': 'f_2021', 'quantity': 10.5, 'price': 150.20},
    {'order_id': 'o_102', 'fill_id': 'f_2022', 'quantity': 5.0, 'price': 30.10},
    {'order_id': 'o_101', 'fill_id': 'f_2023', 'quantity': 4.5, 'price': 150.40},
    {'order_id': 'o_103', 'fill_id': 'f_2024', 'quantity': 20.0, 'price': 12.80},
    {'order_id': 'o_102', 'fill_id': 'f_2025', 'quantity': 2.5, 'price': 30.05},
    {'order_id': 'o_101', 'fill_id': 'f_2026', 'quantity': 5.0, 'price': 150.25},
]
# Expected Output:
# {
#     "o_101": {
#         "total_quantity": 20.0,
#         "vwap": 150.275,
#         "fill_ids": ["f_2021", "f_2023", "f_2026"]
#     },
#     "o_102": {
#         "total_quantity": 7.5,
#         "vwap": 30.083333333333332,
#         "fill_ids": ["f_2022", "f_2025"]
#     },
#     "o_103": {
#         "total_quantity": 20.0,
#         "vwap": 12.8,
#         "fill_ids": ["f_2024"]
#     }
# }
def get_order_metrics(fills):
    orders = defaultdict(lambda: {"total_quantity": 0, "vwap_sum": 0, "fill_ids": set()})
    for fill in fills:
        order_id = fill['order_id']
        orders[order_id]['total_quantity'] += fill['quantity']
        orders[order_id]['vwap_sum'] += fill['quantity'] * fill['price']
        orders[order_id]['fill_ids'].add(fill['fill_id'])
    return {
        order_id: {
            "total_quantity": metrics["total_quantity"],
            "vwap": metrics["vwap_sum"] / metrics["total_quantity"],
            "fill_ids": sorted(list(metrics["fill_ids"]))
        }
        for order_id, metrics in orders.items()
    }
# Test:
# print(get_order_metrics(fills))

# Detect potentially fraudulent transactions based on:
# - Velocity: >3 transactions in 5 minutes
# - Amount spike: Transaction >5x user's average
# - New device: First time device_id for user

# Input: Transaction history
transactions = [
        {'id': 1, 'user_id': 1, 'amount': 50, 'timestamp': '2024-01-01 10:00:00', 'device_id': 'A'},
        {'id': 2, 'user_id': 1, 'amount': 60, 'timestamp': '2024-01-01 10:02:00', 'device_id': 'A'},
        {'id': 3, 'user_id': 1, 'amount': 500, 'timestamp': '2024-01-01 10:03:00', 'device_id': 'B'},
        {'id': 4, 'user_id': 1, 'amount': 10000, 'timestamp': '2024-01-01 10:04:00', 'device_id': 'C'},
    ]
# Output: Flagged transactions with reasons
# [
#     {'transaction_id': 4, 'reasons': ['amount_spike', 'new_device', 'velocity']}
# ]
# slow thinking: Initialize the fraud_txns, build the logic for reasons for users: 1. avg_user_amt 2. new_device 3. txn_count, txn_time_diff
def detect_fraud_transactions(transactions):
    fraud_txn = {'transaction_id': 0, 'reasons': set()}
    user_history = defaultdict(lambda: {
        'amounts': [],
        'devices': set(),
        'recent_txns': []
    })
    sorted_txns = sorted(transactions, key=lambda x: x['timestamp'])
     # calculate user avg
    for txn in sorted_txns:
        user_id = txn['user_id']
        txn_time = datetime.strptime(txn['timestamp'], '%Y-%m-%d %H:%M:%S')
        # Check amount spike (>5x average)
        if user_history[user_id]['amounts']:
            avg_amount = sum(user_history[user_id]['amounts']) / len(user_history[user_id]['amounts'])
            if txn['amount'] > avg_amount * 5:
                fraud_txn['reasons'].add('amount_spike')
        
        # Check new device
        if txn['device_id'] not in user_history[user_id]['devices']:
            fraud_txn['reasons'].add('new_device')
        
        # Check velocity (>3 transactions in 5 minutes)
        five_min_ago = txn_time - timedelta(minutes=5)
        recent_count = len([t for t in user_history[user_id]['recent_txns'] if t > five_min_ago])
        if recent_count >= 3:
            fraud_txn['reasons'].add('velocity')
        # Flag if suspicious
        if fraud_txn['reasons']:
            fraud_txn['transaction_id'] = txn['id']
        # at last update the txn to history
        user_history[user_id]['amounts'].append(txn['amount'])
        user_history[user_id]['devices'].add(txn['device_id'])
        user_history[user_id]['recent_txns'].append(txn_time)
    
    return [{'transaction_id': fraud_txn['transaction_id'], 
             'reasons': sorted(list(fraud_txn['reasons']))}] if fraud_txn['reasons'] else []

# print(detect_fraud_transactions(transactions))