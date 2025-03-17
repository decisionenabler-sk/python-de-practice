# Write a function that groups orders by delivery area. Given a list of (order_id, area_code) tuples, return a dictionary with area codes as keys and lists of order IDs as values. 
# The order of the order IDs in the lists should be the same as the order of the order_id, area_code tuples in the input list.
# input: [(1001, "94107"), (1002, "94107"), (1003, "94110"), (1004, "94107"), (1005, "94110")]
from collections import defaultdict


def group_orders_by_area(orders):
    orders_by_area = defaultdict(list)
    for order_id, area_code in orders:
        orders_by_area[area_code].append(order_id)
    return orders_by_area
print(group_orders_by_area([(1001, "94107"), (1002, "94107"), (1003, "94110"), (1004, "94107"), (1005, "94110")]))