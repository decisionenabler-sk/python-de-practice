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
print("weather_data_1",fill_in_list(weather_data_1))
weather_data_2 = [None, None, 18, 20, None, 22]
# Expected Output: [None, None, 18, 20, 20, 22]
print("weather_data_2",fill_in_list(weather_data_2))
weather_data_3 = [15, None, None, 18, None, None, 20]
# Expected Output: [15, 15, 15, 18, 18, 18, 20]
print("weather_data_3",fill_in_list(weather_data_3))
weather_data_4 = [None, None, None]
# Expected Output: [None, None, None]
print("weather_data_4",fill_in_list(weather_data_4))
weather_data_5 = [10, 12, 15, 18, 20]
# Expected Output: [10, 12, 15, 18, 20]
print("weather_data_5",fill_in_list(weather_data_5))