"""
To personalize a user's experience, you want to recommend K products that are closest to a price point they have shown interest in.
Given a list of product prices and a target_price, find the k prices that are closest to the target.

Input:
prices = [10, 12, 15, 17, 22, 28, 35]
target_price = 20
k = 3

Output:
[17, 22, 15] # The differences are |17-20|=3, |22-20|=2, |15-20|=5. The three closest are 22, 17, 15.
"""
from collections import defaultdict
# find out list of differnces with the target and then sort by the diff. Keep the element as key and diff as value 
# Then return the keys as list

def get_product_recommendations(prices: list[int],target_price:int,k: int) -> list[int]:
    price_diffs = defaultdict(int)
    for price in prices:
        price_diffs[price] = abs(price - target_price)
    sorted_prices = sorted(price_diffs.items(), key= lambda x:(x[1],x[0]))
    print("These are all the differences relative to the target:", sorted_prices)
    return [price for price, diff in sorted_prices[:k]]
print(get_product_recommendations([10, 12, 15, 17, 22, 28, 35],20,3 ))