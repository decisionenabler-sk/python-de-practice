# 1. Remove Duplicates While Preserving Order
# Given a list of integers, remove duplicates while maintaining the original order of first occurrence.
# Example:
input = [1, 2, 3, 2, 4, 1, 5, 3] # Output: [1, 2, 3, 4, 5]
def remove_dupes(input):
    output = set(input)
    return output
# print(remove_dupes(input))
# 2. Given two dictionaries with integer values, merge them by summing values for common keys.
# Input: 
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 40}
# Output: {'a': 10, 'b': 35, 'c': 55, 'd': 40}
def merge_dicts(dict1, dict2):
    output = dict(dict1) # start with 1st one
    for k,v in dict2.items():
        if k in output:
            output[k] += v
        else:
            output[k] = v
    return output
# print(merge_dicts(dict1, dict2))
# 3. Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Input1: 
# nums = [100,4,200,1,3,2]
# Output: 4

# Input2: 
nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
def longest_consecutive_seq(nums):
    streak = 1
    longest_streak = 1
    nums = sorted(nums)
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1] +1:
            streak += 1
            longest_streak = max(longest_streak, streak)
        else:
            streak = 1
    return longest_streak
# print(longest_consecutive_seq(nums))
#4. Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Input 1:
#  nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Input 2: 
# nums = [1], k = 1
# Output: [1]
def most_frequent_number(nums,k):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    print(dict(frequency))
    sorted_nums = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return [n for n,k in sorted_nums][:k]
# print(most_frequent_number([1,1,1,2,2,3],2))
# 5. Given a list of digits. It is ordered from most significant to least significant digit.
# Return an array of digits of the number after adding another one to the input.
# Example #1
# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]
# Example #2
# Input: digits = [6, 9]
# Output: [7, 0]
def another_one(digits):
    number = 0
    for digit in digits:
        number = number * 10 + digit
    number = number+1
    return list(map(int, str(number)))

# print(another_one([1,2,3]))
