# 1. Given a sentence, count the distinct words in the sentence

from collections import defaultdict


def word_count(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] = word_count.get(word,0) + 1
    return word_count
# Test the function:
sentence = "This is a test. This is only a test."
# print(word_count(sentence))

# 2. Given a sentence, calculate the average word length

def average_word_length(sentence):
    words = sentence.split()
    total_length = 0
    for word in words:
        total_length += len(word)
    # average length is calculated by dividing the total length by the number of words
    average_length = total_length / len(words)
    return average_length
# Test the function:
sentence = "This is a test. This is only a test."
# print(average_word_length(sentence))

# 3. Given a list of integers, find the maximum product of any two numbers in the list

# 4. Count the number of times a string appears in a sentence
def count_substring(sentence, substring):
    count = 0
    for i in range(len(sentence)):
        # Check if the substring matches starting from the current index to length of the substring
        if sentence[i:i+len(substring)] == substring:
            count += 1
    return count
def count_substring_by_find(sentence, substring):
    count = 0
    start = 0
    # When str.find() returns -1 (no more matches), the loop terminates.
    while start >= 0:
        start = sentence.find(substring, start)
        if start >= 0:  # If a match is found
            count += 1
            start += 1  # Move to the next character to continue searching
    return count
# Test
sentence = "This is a test. I'm only a testing."
substring = "test"
# print(count_substring_by_find(sentence, substring))

# 5. Given a list of ints, balance the list so that each int appears equally in the list. 
# Return a dictionary where the key is the int and the value is the count needed to balance the list.
#[1, 1, 2] => {2: 1}
# [1, 1, 1, 5, 3, 2, 2] => {5: 2, 3: 2, 2: 1}

# Slow thinking: first, count the ints and store in default dict, then find the highest value and do the operation max count - current count for the final output

def balance_list(integer_list):
    # Count the number of times an integer appears in the list
    int_count = defaultdict(int)
    for i in integer_list:
        int_count[i] += 1
    # Get the max count  
    max_count = max(int_count.values())
    # target_count = max_count - current_count
    output = {i:max_count - count for i,count in int_count.items() if max_count - count > 0}
    return output
# Test
# print(balance_list([1, 1, 2]))
# print(balance_list([1, 1, 1, 5, 3, 2, 2]))

# 6. Write a function to count the number of times each character appears in a string and rewrite the string in that format. 
#  “I am back.” should become “i1 2a2m1b1c1k1.1”

# Slow Thinking: 1. Count each char by iterating over the sentence 2. Append the count with char to the output list 3. constrcuct the sentence back using the output list

def rewrite_string(sentence):
    char_count = defaultdict(int)
    output = []
    for char in sentence.lower():
        char_count[char] += 1
        output.append(f"{char}{char_count[char]}")
    return ''.join(output)

# Test
# print(rewrite_string("I am back."))
# print(rewrite_string("This is the year 2025"))

# 7. Given a string, determine if it is a valid IP address. 
# A valid IP is follows the format x.x.x.x, where each "x" is a number between 0 and 255, and it must have exactly four sections separated by periods. 
# Each section represents a decimal value, and leading zeros are not allowed within each section. 

# slow thinking: We'll do 4 checks - 1. The length of ip address list should be exact 4 2. all integers 3. wihtin the valid range 4. no leading 0s when 
def is_valid_ip(ip_address):
    ip_address_list = ip_address.split(".")
    # Check 1: number of octets not be more than or less than 4
    if len(ip_address_list) != 4:
        return False
    for octet in ip_address_list:
        # Check 2: Each octet should be an integer
        # Check 3: Each octet should be within the valid range
        # Check 4: Each octet should not start with leading zeroes
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255 or (len(octet) > 1 and octet[0] == '0'):
            return False
    # If the function hasn’t returned False by this point, it means all octets are valid
    return True
# Test
# Valid IP Address
# print("The ip address 192.168.1.1 is valid?",is_valid_ip("192.168.1.1"))
# Invalid IP Address
# print("The ip address 256.300.1.01 is valid?", is_valid_ip("256.300.1.01"))

# 8. For given lists of whether data, if the value is none replace it with the last non none value, consider the edge case of consecutive Nones.

# Slow Thinking: 1. None is first element and there is no last non none value 2. Consecutive None values so grab previous non none value 3. All none values and no None values
def fill_in_list(weather_list):
    # Check for all None
    if all(w is None for w in weather_list):
        return weather_list
    # Initialize previous value
    previous_value = None
    for i,value in enumerate(weather_list):
        # When first element is None
        if value is None:
            weather_list[i] = previous_value
        else:
            previous_value = value
    return weather_list
# Test 
weather_data_1 = [20, None, 22, None, None, 25]
# Expected Output: [20, 20, 22, 22, 22, 25]
# print("weather_data_1",fill_in_list(weather_data_1))
weather_data_2 = [None, None, 18, 20, None, 22]
# Expected Output: [None, None, 18, 20, 20, 22]
# print("weather_data_2",fill_in_list(weather_data_2))
weather_data_3 = [15, None, None, 18, None, None, 20]
# Expected Output: [15, 15, 15, 18, 18, 18, 20]
# print("weather_data_3",fill_in_list(weather_data_3))
weather_data_4 = [None, None, None]
# Expected Output: [None, None, None]
# print("weather_data_4",fill_in_list(weather_data_4))
weather_data_5 = [10, 12, 15, 18, 20]
# Expected Output: [10, 12, 15, 18, 20]
# print("weather_data_5",fill_in_list(weather_data_5))

# 9. Create a function that returns a list containing mismatched words in two strings.
# Slow thinking: first convert the list to set to remove dupes if any
def get_mismatched_word(arr1,arr2):
    # ideal case when the length of the lists are same
    for word1, word2 in zip(arr1,arr2):
        if word1 != word2:
            result = [word1, word2]
        else:
            result = None
    if len(arr1) > len(arr2):
        result = arr1[len(arr2):]
    elif len(arr2) > len(arr1):
        result = arr2[len(arr1):]
    return result
# Test 1
arr1 = ["this", "is", "my", "test"]
arr2 = ["this", "is", "my", "array"]
# Expected output: ["test", "array"]
# print("Mismatched words in arr1 and arr2 are:",get_mismatched_word(arr1,arr2))
# Test 2
arr3 = ["this", "is", "my", "test", "extra"]
arr4 = ["this", "is", "my", "array"]
# Expected Output: ['test', 'array', 'extra']
# print("Mismatched words in arr3 and arr4 are:",get_mismatched_word(arr3, arr4))

# 10. Write a function that returns the key of the nth largest value in a dictionary
def n_largest(dict,n):
    sorted_values = sorted(set(dict.values()), reverse=True)
    if n > len(sorted_values):
        return None
    nth_largest_value = sorted_values[n-1]
    return {k:v for k,v in dict.items() if v == nth_largest_value}
# Test: 
test_dict = {'a': 1, 'b': 2, 'c': 100, 'd': 30, 'e':100, 'f':30}
# Expected Output: n : 2 (2nd largest value) d
# print(n_largest(test_dict,2))

# 11. Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not.

def is_monotonic(arr):
    inc = True # initialize the array as non-decreasing
    dec = True # initialize the array as non-increasing
    if len(arr) <= 1:
        return inc or dec
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            inc = False # If an element is greater than the previous, it's not non-increasing
        if arr[i] < arr[i-1]:
            dec = False # If an element is smaller than the previous, it's not non-decreasing
    return inc or dec
# Tests: 1 2 5 5 8 > true , 9 4 4 2 2 > true, 1 4 6 3 >false, 1 1 1 1 1 1 >true
int_list1 = [1, 2, 5, 5, 8]
int_list2 = [9, 4, 4, 2 ,2]
int_list3 = [1, 4, 6, 3]
int_list4 = [1, 1, 1, 1, 1, 1]

# print("is int_list1 monotonic?", is_monotonic(int_list1))
# print("is int_list2 monotonic?", is_monotonic(int_list2))
# print("is int_list3 monotonic?", is_monotonic(int_list3))
# print("is int_list4 monotonic?", is_monotonic(int_list4))

# 12. Find the Median of Two Arrays
# Slow thinking:
def get_median(array1, array2):
    merged_array = sorted(array1 + array2)
    n = len(merged_array)
    if n % 2 == 0:
        median = (merged_array[n // 2 - 1] + merged_array[n // 2]) / 2
    else:
        median = merged_array[n //2]
    return median
# print("The median is:", get_median([1,2,3,5] , [2,3,6,1,9]))

# 13. You have an array of integers, nums of length n spanning 0 to n with one missing. 
# Write a function missing_number that returns the missing number in the array.

def find_missing_number (nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = total_sum - actual_sum
    return missing_number
# Test
# print("The missing number is:", find_missing_number([0, 1, 2, 3, 4, 6]))  # Output: 5

# 14. Given a list of strings of letters from a to z, create a function, sum_alphabet, that returns a list of the alphabet sum of each word in the string.

# The alphabet sum is the sum of the ordinal position of each of the string’s letters in the standard English alphabet ordering.
# So, the letter a will have a value of 1, z will have a value of 26, and so on.
# As an example the string 'sport' will have an alphabet sum of 19 + 16 + 15 + 18 + 20 = 88.

def sum_alphabet(words):
    aplhabet_dict = {k: v for v, k in enumerate('abcdefghijklmnopqrstuvwxyz', start=1)}
    result = 0
    for word in words:
        word = word.lower()
        for char in word:
            if char in aplhabet_dict:
                result += aplhabet_dict[char]
    return result
# Test
# print("The alphabet sum of the words is:", sum_alphabet(['sport' , 'good' , 'bad']))  # Output: 88 + 41 + 7 = 136

# 15. Given a list of integers, find the length of the longest consecutive subsequence.
# Input: 
nums = [100, 4, 200, 1, 3, 2] # Output: 4
# slow thinking: 1. make the list as set to remove duplicates and sort the list 2. Iterate through the list and check if the current number is consecutive to the previous number, if yes, increase the count
def find_longest_consecutive_seq(nums):
    nums = sorted(set(nums))  # Remove duplicates
    print("The sorted list is:", nums) 
    # Initialize the streak to 1
    longest_streak = 1
    streak = 1
    if not nums:  # If the list is empty, return 0
        return 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]  + 1:  # Check if the current number is consecutive to the previous number and skip the first element
            streak += 1
            longest_streak = max(longest_streak, streak)
        else:  # If not consecutive, reset the streak to 1
            streak = 1
    return longest_streak # Return the maximum of the longest streak and the current streak

# Test
print("The length of the longest consecutive subsequence is:", find_longest_consecutive_seq(nums))  # Output: 4
# Test 2
nums2 = [9, 1, 7, 3, -1, 0, 5, 8, -2, 6, 2] # Output: 6
print("The length of the longest consecutive subsequence is:", find_longest_consecutive_seq(nums2))  # Output: 6