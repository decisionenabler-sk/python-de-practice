# Transform a nested list of food orders into a dictionary that groups orders by restaurant.
# Input: [['Pizza Hut', 'Pepperoni Pizza', 25.99], ['McDonald\'s', 'Big Mac', 15.50], ['Pizza Hut', 'Margherita Pizza', 22.50], ['Subway', 'Italian BMT', 12.75], ['McDonald\'s', 'Chicken McNuggets', 10.25]]
# Output: {'Pizza Hut': [['Pepperoni Pizza', 25.99], ['Margherita Pizza', 22.50]], 'McDonald\'s': [['Big Mac', 15.50], ['Chicken McNuggets', 10.25]], 'Subway': [['Italian BMT', 12.75]]}
from collections import defaultdict
# Scenario 1: if the list looks like this i.e. the restauarant name, item and price in same list
orders = [
    ['Pizza Hut', 'Pepperoni Pizza', 25.99],
    ['McDonald\'s', 'Big Mac', 15.50],
    ['Pizza Hut', 'Margherita Pizza', 22.50],
    ['Subway', 'Italian BMT', 12.75],
    ['McDonald\'s', 'Chicken McNuggets', 10.25]
]
# Scenario 2: if the list looks like this i.e. the restauarant name, item and price in separate lists
restaurants = ['Pizza Hut', 'McDonald\'s', 'Subway']
items = ['Pepperoni Pizza', 'Big Mac', 'Margherita Pizza', 'Italian BMT', 'Chicken McNuggets']
prices = [25.99, 15.50, 22.50, 12.75, 10.25]
def group_orders_by_restaurant(orders):
    orders_by_restaurants = defaultdict(lambda: defaultdict(float))
    for restaurant, item, price in orders:
        orders_by_restaurants[restaurant][item] = price
    return orders_by_restaurants
# print(group_orders_by_restaurant(orders))

def transform_orders(restaurants, items, prices):
    orders_by_restaurants = defaultdict(lambda: defaultdict(float))
    orders = list(zip(restaurants, items, prices))
    for restaurant, item, price in orders:
        orders_by_restaurants[restaurant][item] = price
    return {restaurant: dict(items) for restaurant, items in orders_by_restaurants.items()}
print(transform_orders(restaurants, items, prices))
