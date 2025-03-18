# Write a function that takes two dictionaries: one mapping customer IDs to order counts before a promotion and another mapping customer IDs to order counts after a promotion. Return the customers with the largest increase in order frequency.
# Test data:
from collections import defaultdict
before_promo = {
    "cust_1": [120, 654, 768],                      # 3 orders
    "cust_2": [210, 315, 422],                      # 3 orders
    "cust_3": [101, 203, 305, 407, 509, 611, 713],  # 7 orders
    "cust_4": [867, 909],                           # 2 orders
    "cust_5": [125, 250, 375, 500],                 # 4 orders
    "cust_6": [100, 250, 399, 712],                 # 4 orders
    "cust_7": [543, 299],                           # 2 orders
    "cust_8": [111, 222, 333, 444, 555, 666],       # 6 orders
    "cust_9": [187, 265, 398, 401, 598],            # 5 orders
    "cust_10": [721, 834, 955]                      # 3 orders
}

after_promo = {
    "cust_1": [89, 23, 450, 545, 324, 91, 103],                        # 7 orders (+4)
    "cust_2": [210, 315, 422, 531, 645, 752, 864, 978, 1089],          # 9 orders (+6)
    "cust_3": [101, 203, 305, 407, 509, 611, 713, 815],                # 8 orders (+1)
    "cust_4": [867, 909],                                              # 2 orders (+0)
    "cust_5": [125, 250, 375, 500, 625],                               # 5 orders (+1)
    "cust_6": [100, 250, 399, 452, 501, 625, 712],                     # 7 orders (+3)
    "cust_7": [543, 299, 621, 785, 843, 901, 955],                     # 7 orders (+5)
    "cust_8": [111, 222, 333, 444, 555, 666, 777],                     # 7 orders (+1)
    "cust_9": [187, 265, 398, 401, 598, 612],                          # 6 orders (+1)
    "cust_10": [721, 834, 955, 1023, 1198]                             # 5 orders (+2)
}
def get_customers_with_increased_order_requency(before_promo, after_promo):
    customer_order_frequency_increase = {}
    for customer in before_promo:
        increase = len(after_promo[customer]) - len(before_promo[customer])
        if increase > 0:
            customer_order_frequency_increase[customer] = increase
    return customer_order_frequency_increase
print(get_customers_with_increased_order_requency(before_promo, after_promo))