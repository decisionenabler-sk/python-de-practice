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

# Slow thinking: first, count the ints and store in default dict, then find the highest value and max value - other values will be the final output

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
print(balance_list([1, 1, 2]))
print(balance_list([1, 1, 1, 5, 3, 2, 2]))