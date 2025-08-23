"""
You are given a raw log file from a web server as a list of strings. 
Your task is to find the top 3 most frequently requested API endpoints.
Write a function that takes a list of log strings and returns a list of tuples, with each tuple containing the endpoint and its request count, sorted in descending order of count. 
Each log line follows the format: TIMESTAMP [LEVEL] "METHOD /api/endpoint HTTP/1.1".
"""
from collections import Counter
# Input:
logs = [
    '2023-08-20T10:00:00 [INFO] "GET /api/users HTTP/1.1"',
    '2023-08-20T10:00:05 [INFO] "GET /api/products HTTP/1.1"',
    '2023-08-20T10:00:10 [INFO] "GET /api/users HTTP/1.1"',
    '2023-08-20T10:00:15 [ERROR] "POST /api/orders HTTP/1.1"',
    '2023-08-20T10:00:20 [INFO] "GET /api/products HTTP/1.1"',
    '2023-08-20T10:00:25 [INFO] "GET /api/users HTTP/1.1"',
    '2023-08-20T10:00:35 [INFO] "POST /api/users HTTP/1.1"',
    '2023-08-20T10:00:40 [INFO] "GET /api/orders HTTP/1.1"',
]

# Output:
# [('/api/users', 4), ('/api/products', 2), ('/api/orders', 1)]

def three_popular_apis(logs):
    api_counts = Counter()
    for log in logs:
        api_string = log.split()
        level = api_string[1].replace("[", '').replace("]", '')
        method = api_string[2].replace("\"", '')
        api = api_string[3]
        if level != 'ERROR':
            api_counts[api] += 1
    top_3_apis = api_counts.most_common(3)
    return top_3_apis if api_counts else []
print(three_popular_apis(logs))