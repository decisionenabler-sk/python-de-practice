from collections import defaultdict
import string
# Here are 10 Python data structure challenges that are commonly asked in interviews.

# 1. **Group Anagrams**: Given a list of strings, group anagrams together.
#    Example: Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
#    Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def group_anagrams(arr):
    anagram_groups = {}
    for word in arr:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    return list(anagram_groups.values())
test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(test_input))  # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# 2. **Find All Pairs with Given Sum**: Given an array of integers and a target sum, find all pairs that add up to the target.
#    Example: Input: [1, 5, 3, 7, 9], target = 10
#    Output: [(1, 9), (3, 7)]
from collections import defaultdict


def find_pairs(arr, target):
    index_map = {}
    pairs = []
    for i in range(len(arr)):
        num = arr[i]
        diff = target - num
        if diff in index_map:
            pairs.append((index_map[diff], i))
        index_map[num] = i
    return pairs    
# 3. **First Non-Repeating Character**: Find the first non-repeating character in a string.
#    Example: Input: "leetcode"
#    Output: 0 (index of 'l')
def first_non_repeating_character(s):
    char_count = defaultdict(int)
    for char in s:
        char_count[char] += 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return None  # If no non-repeating character is found 
# print(first_non_repeating_character("cycle"))
## If the question was to find out all repeating character, then the code would be:
def repeating_characters(s):
    repeating_set = set()
    repeating_index = {}
    for i, char in enumerate(s):
        if char in repeating_set:
            repeating_index[char] = i
        repeating_set.add(char)
    return repeating_index   
# print(repeating_characters("cycle"))
# 4. **Task Scheduler**: Given a list of tasks and their execution times, find the minimum time needed to complete all tasks considering a cooldown period between identical tasks.
#    Example: Input: tasks = ["A", "A", "A", "B", "B", "C"], cooldown = 2
#    Output: 8 (A → B → C → wait → A → B → wait → A)

# 5. **Top K Frequent Elements**: Given an array of integers, return the k most frequent elements.
#    Example: Input: [1, 1, 1, 2, 2, 3], k = 2
#    Output: [1, 2]
def get_most_req_elements(arr,k):
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_freq[:k]]
# print(get_most_req_elements([1, 1, 1, 2, 2, 3],2))
# 6. **Merge Delivery Windows**: 
# Given a list of time intervals for deliveries (start and end times), merge overlapping intervals to optimize delivery routes.
#    Example: Input: [(1, 3), (2, 6), (8, 10), (15, 18)]
#    Output: [(1, 6), (8, 10), (15, 18)]
# def merge_intervals(deliveries):

# 7. **Log Rate Limiter**: Implement a rate limiter that allows each user to make at most 3 requests within any 1-minute window. Return True if the request should be allowed, False otherwise. Each request comes with a timestamp and user_id.

# 8. **Find Common Delivery Locations**: 
# Given two delivery personnel's routes (lists of location IDs), find the common locations they both visit.
#    Example: Input: route1 = [1, 5, 3, 7, 9], route2 = [2, 3, 5, 8]
#    Output: [3, 5]

# 9. **Package Grouping by Weight**: 
# Group packages into bins where each bin can hold up to a certain weight. Return the minimum number of bins needed.
#    Example: Input: 
weights = [1.5, 2.3, 5.7, 1.2, 3.5, 4.8] 
bin_capacity = 6.0 #    Output: 3 bins
# no. of bins needed = sum of all weights / capacity example - 
def group_packages(weights, bin_capacity):
    if not weights:
        return 0
    weights.sort(reverse=True)
    bins = []
    for weight in weights:
        if weight_sum <= bin_capacity:
            weight_sum +=  weight
        else:
            weight_sum = 0
            bin_count += 1
    return bin_count
# print(group_packages(weights,bin_capacity))
# 10.**Unique Values from Dictionary**
# You are given a dictionary with a key-value of {string: number} where values in the dictionary could be duplicates. 
# You are required to extract the unique values from the dictionary where the value occurred only once.
# Return a list of values where they occur only once.
def get_unique_values(dict):
    value_count = defaultdict(int)
    for value in dict.values():
        value_count[value] += 1
    return [value for value, count in value_count.items() if count == 1]
# Example usage:
example_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# print(get_unique_values(example_dict))  # Output: [2, 3]
# 10. **common words in sentence**: 
# Find words that are present in both the given sentences
# Example: ["Today is a great day to learn something new!", "Is today the day to learn?"]
# Output: ["day", "is", "learn", "to", "today"]

def find_common_words(input):
    sentence1 = input[0]
    sentence2 = input[1]
    # initialize the output list
    common_words = set()
    # strip both the strings of any punctuations
    sentence1 = sentence1.translate(str.maketrans('', '', string.punctuation)).lower().split()
    sentence2 = sentence2.translate(str.maketrans('', '', string.punctuation)).lower().split()
    # find intersection of the words in the sentences converted to set
    common_words = set([word for word in sentence1 if word in sentence2])
    return list(common_words)
print(find_common_words(["Today is a great day to learn something new!", "Is today the day to learn?"]))