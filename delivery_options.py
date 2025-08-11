# Write a function that takes a list of delivery times where index is the order id and returns a list of pairs of orders where the delivery can be done in 1 hour.
# The function should return the pairs in the order they appear in the list.
def find_pairs(arr):
    index_map = {}
    target=60
    plans = []
    for i in range(len(arr)):
        num = arr[i]
        diff = target - num
        if diff in index_map:
            plans.append([index_map[diff], i])
        index_map[num] = i
    return plans
# Example usage:
arr = [1, 59, 60, 10, 35, 50]
print(find_pairs(arr))
