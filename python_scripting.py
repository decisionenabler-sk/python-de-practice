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

# 6. Max Product of Three Numbers Given a list of integers, return the maximum product of any three numbers in the array.
# For example, for A = [1, 3, 4, 5], return 60, 3∗4∗5=60.
# For B = [−4, −2, 3, 5], return 40, −4∗−2∗5=40
# def max_three_product(arr,n):
#     max = arr[0]* arr[1] * arr[2]
#     current = 0

# Let's do some quick trasformations   
def clean_words(words):
    """Return uppercase versions of words longer than 3 characters"""
    # Write using list comprehension
    return [word.upper() for word in words if len(word) > 3]

# Test: 
# print(clean_words(["hi", "hello", "world", "a"])) # → ["HELLO", "WORLD"]

def extract_scores(students):
    """Extract names of students with scores >= 80"""
    # Write using list comprehension
    print("Students with scores more than 80 are:",[student for student,score in students.items() if score >= 80])
    pass
# students = {"Alice": 85, "Bob": 72, "Charlie": 90, "Diana": 78}
# extract_scores(students)

def categorize_numbers(nums):
    """Return 'positive', 'negative', or 'zero' for each number"""
    # Write using list comprehension with conditional expressions
    print(['positive' if num > 0 else 'negative' if num < 0 else 'zero' for num in nums])
    pass

# Test: 
# categorize_numbers([1, -2, 0, 3]) # → ['positive', 'negative', 'zero', 'positive']

def extract_initials(names_matrix):
    """Extract first letter of each name in 2D matrix"""
    # names_matrix = [["Alice", "Bob"], ["Charlie", "Diana"]]
    # Write using nested list comprehension
    print([[name[0] for name in names] for names in names_matrix])
    pass
# Test: 
# extract_initials([["Alice", "Bob"], ["Charlie", "Diana"]]) # → [["A", "B"], ["C", "D"]]
def passing_students(grades):
    """
    Convert numeric grades to letter grades for passing students only
    90-100: 'A', 80-89: 'B', 70-79: 'C'
    Use dict comprehension
    """
    output = {}
    for student, score in grades.items():
        if score >= 90:
            output[student] = 'A'
        elif score >= 80:
            output[student] = 'B'
        elif score >= 70:
            output[student] = 'C'
        else:
            output[student] ='Fail'
    return {student:grade for student,grade in output.items() if grade != 'Fail'}

# Test case:
# print(passing_students({"Alice": 85, "Bob": 65, "Charlie": 92, "Diana": 78}))
# → {"Alice": "B", "Charlie": "A", "Diana": "C"}
from collections import defaultdict
def group_by_length(words):
    """
    Group words by their length
    Use dict comprehension with list comprehension as value
    """
    grouped_words = defaultdict(list)
    for word in words:
        grouped_words[len(word)].append(word)
    print(dict(grouped_words))
    pass

# Test case:
# group_by_length(["cat", "dog", "elephant", "fox", "bird"])
# → {3: ["cat", "dog", "fox"], 4: ["bird"], 8: ["elephant"]}

def extract_domains(emails):
    return {email.split('@')[1].lower() for email in emails}
# Test case:
# print(extract_domains(["john@GMAIL.com", "jane@Yahoo.COM", "bob@gmail.com"]))
# → {"gmail.com", "yahoo.com"}


# Given a list of strings, return a set of valid Python identifiers (start with letter/underscore, contain only alphanumeric/underscore).
import keyword
def valid_identifiers(strings):
    """
    Return set of valid Python identifiers
    Use set comprehension with validation
    """
    return {s for s in strings 
            if s and (s[0].isalpha() or s[0] == '_') and 
            all(c.isalnum() or c == '_' for c in s) and not keyword.iskeyword(s)}

# Test case:
# print(valid_identifiers(["var1", "2invalid", "_private", "class", "my-var", "valid_name", None, ""]))
# → {"var1", "_private", "valid_name"}  # Note: "class" is valid identifier but Python keyword

# Given two sentences, return a set of words that appear in both sentences (case-insensitive, ignore punctuation).
def common_words(sentence1, sentence2):
    """
    Find common words between two sentences
    Use set comprehension and set operations
    """
    import string
    common = []
    # translator to strip punctuation
    translator = str.maketrans('', '', string.punctuation)
    # Process both sentences and convert to sets 
    words1 = set(sentence1.lower().translate(translator).split())
    words2 = set(sentence2.lower().translate(translator).split())
    return list(words1 & words2)

# Test case:
print(common_words("Hello world!", "World of Python")) #→ ["world"]