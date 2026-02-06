
"""
Question 1: Load Balancer Task Distribution
Company Context: You're building a task scheduler for a distributed data pipeline.
Problem:
Your team runs hourly Spark jobs with varying processing times. You've noticed that when heavy jobs cluster together, they cause memory pressure and failures.
Design a function distribute_tasks(task_times: List[int]) -> List[int] that reorders tasks so they alternate between shortest and longest remaining tasks. This ensures the system never processes consecutive heavy jobs.
Requirements:

First task should be the shortest
Second task should be the longest
Third task should be second-shortest
Continue alternating...
"""
# Test Cases:
# Test 1: Standard case
task_times_1 = [120, 5, 45, 200, 10, 90, 3]
# Expected: [3, 200, 5, 120, 10, 90, 45]

# Test 2: Empty pipeline
task_times_2 = []
# Expected: []

# Test 3: Single task
task_times_3 = [50]
# Expected: [50]

# Test 4: Two tasks
task_times_4 = [100, 25]
# Expected: [25, 100]

# Test 5: Already sorted ascending
task_times_5 = [10, 20, 30, 40, 50]
# Expected: [10, 50, 20, 40, 30]

# Test 6: All same duration (edge case)
task_times_6 = [60, 60, 60, 60]
# Expected: [60, 60, 60, 60]

# Test 7: Negative values (representing priority debits)
task_times_7 = [-10, 50, -5, 100, 0]
# Expected: [-10, 100, -5, 50, 0]


def ditribute_tasks(task_times: list[int]) -> list[int]:
    if not task_times:
        return task_times
    sorted_tasks = sorted(task_times)
    short = 0
    long = len(sorted_tasks) - 1
    result = []
    while short <= long:
        result.append(sorted_tasks[short])
        short += 1
        if short <= long:
            result.append(sorted_tasks[long])
            long -= 1
    return result
# print(ditribute_tasks(task_times_7))

"""
Question 2: Content Feed A/B Testing
Company Context: You're an analytics engineer at a social media company building experimentation infrastructure.
Problem:
The content ranking team wants to run an A/B test measuring position bias. They need a feed arrangement that alternates between low and high engagement content, so they can measure if users engage differently based on position vs. content quality.
Design a function create_test_feed(content: List[Dict]) -> List[Dict] where each dict has {'content_id': str, 'predicted_engagement': float}.
The output should alternate: lowest engagement, highest engagement, second-lowest, second-highest, etc.
Requirements:

Sort by predicted_engagement
Maintain the full dict in output (not just scores)
Handle ties gracefully (order doesn't matter for equal scores)
"""
# Test 1: Standard feed
content_1 = [
    {'content_id': 'post_A', 'predicted_engagement': 0.95},
    {'content_id': 'post_B', 'predicted_engagement': 0.20},
    {'content_id': 'post_C', 'predicted_engagement': 0.60},
    {'content_id': 'post_D', 'predicted_engagement': 0.85},
    {'content_id': 'post_E', 'predicted_engagement': 0.10},
]
# Expected order of content_ids: ['post_E', 'post_A', 'post_B', 'post_D', 'post_C']

# Test 2: Empty feed
content_2 = []
# Expected: []

# Test 3: Single post
content_3 = [{'content_id': 'post_X', 'predicted_engagement': 0.50}]
# Expected: [{'content_id': 'post_X', 'predicted_engagement': 0.50}]

# Test 4: Two posts
content_4 = [
    {'content_id': 'viral', 'predicted_engagement': 0.99},
    {'content_id': 'flop', 'predicted_engagement': 0.01},
]
# Expected order: ['flop', 'viral']

# Test 5: All same engagement (tie-breaker)
content_5 = [
    {'content_id': 'A', 'predicted_engagement': 0.50},
    {'content_id': 'B', 'predicted_engagement': 0.50},
    {'content_id': 'C', 'predicted_engagement': 0.50},
]
# Expected: Any valid order (all same score)

# Test 6: Large feed (performance check)
import random
content_6 = [
    {'content_id': f'post_{i}', 'predicted_engagement': random.random()}
    for i in range(10000)
]
# Expected: Function completes in < 1 second

# Test 7: Engagement scores with decimals
content_7 = [
    {'content_id': 'A', 'predicted_engagement': 0.001},
    {'content_id': 'B', 'predicted_engagement': 0.999},
    {'content_id': 'C', 'predicted_engagement': 0.500},
    {'content_id': 'D', 'predicted_engagement': 0.501},
]
# Expected order: ['A', 'B', 'C', 'D'] or close (0.500 and 0.501 are adjacent)

def create_test_feed(content: list[dict]) -> list[dict] :
    if not content:
        return []
    result = []
    sorted_content = sorted(content, key=lambda x: x['predicted_engagement'])
    low = 0
    high = len(content) - 1
    while low <= high:
        result.append(sorted_content[low])
        low += 1

        if low <= high:
            result.append(sorted_content[high])
            high -= 1
    return result
# print(create_test_feed(content_7))

"""
Question 3: Data Quality Audit Scheduler
Company Context: You're a data engineer building monitoring infrastructure.
Problem:
Your data lake has partitions of varying sizes. Small partitions might have data quality issues (incomplete loads), while large partitions might have duplication or schema drift.
Design a function schedule_partition_audit(partitions: Dict[str, float]) -> List[str] that returns partition names ordered for audit. The audit should alternate between smallest and largest partitions to catch both edge cases early.
Input: {'partition_name': size_in_gb}
Output: List of partition names in audit order
"""

# Test 1: Standard monthly partitions
partitions_1 = {
    '2024-01': 50.0,
    '2024-02': 120.5,
    '2024-03': 10.2,
    '2024-04': 200.0,
    '2024-05': 75.8,
}
# Expected: ['2024-03', '2024-04', '2024-01', '2024-02', '2024-05']

# Test 2: Empty table
partitions_2 = {}
# Expected: []

# Test 3: Single partition
partitions_3 = {'2024-01': 100.0}
# Expected: ['2024-01']

# Test 4: Two partitions
partitions_4 = {'small': 1.0, 'large': 999.0}
# Expected: ['small', 'large']

# Test 5: Zero-size partitions (empty loads)
partitions_5 = {
    'empty_1': 0.0,
    'empty_2': 0.0,
    'normal': 50.0,
    'large': 100.0,
}
# Expected: Starts with one of the 0.0 partitions, then 'large'

# Test 6: Very similar sizes
partitions_6 = {
    'A': 100.001,
    'B': 100.002,
    'C': 100.003,
    'D': 100.000,
}
# Expected: ['D', 'C', 'A', 'B'] (or valid zigzag based on sort)

# Test 7: Regional partitions (string keys)
partitions_7 = {
    'us-east-1': 500.0,
    'us-west-2': 50.0,
    'eu-west-1': 300.0,
    'ap-south-1': 25.0,
}
# Expected: ['ap-south-1', 'us-east-1', 'us-west-2', 'eu-west-1']
def schedule_partition_audit(partitions: dict[str, float]) -> list[str]:
    if not partitions:
        return partitions
    sorted_partitions = sorted(partitions.items(), key = lambda x:x[1])
    small, large = 0, len(partitions) - 1
    results = []
    while small <= large:
        results.append(sorted_partitions[small][0])
        small += 1

        if small <= large:
            results.append(sorted_partitions[large][0])
            large -= 1
    
    return results
# print(schedule_partition_audit(partitions_7))
"""
Question 4: Creator Payout Batch Processing
Company Context: You're building financial data pipelines for a creator monetization platform.
Problem:
Your payment system processes creator payouts in batches. To minimize cash flow impact, you want to alternate between smallest and largest payouts. This smooths out the bank's transaction load.
Design a function order_payouts(payouts: List[Tuple[str, float]]) -> List[Tuple[str, float]] where each tuple is (creator_id, payout_amount).
Requirements:

Alternate smallest/largest by payout amount
Preserve the creator_id with each amount
Handle negative amounts (clawbacks) correctly
"""
# Test 1: Standard payout batch
payouts_1 = [
    ('creator_001', 5000.00),
    ('creator_002', 150.50),
    ('creator_003', 25000.00),
    ('creator_004', 750.00),
    ('creator_005', 12000.00),
]
# Expected order by amount: [150.50, 25000.00, 750.00, 12000.00, 5000.00]
# With IDs: [('creator_002', 150.50), ('creator_003', 25000.00), ...]

# Test 2: Empty batch
payouts_2 = []
# Expected: []

# Test 3: Single payout
payouts_3 = [('solo_creator', 999.99)]
# Expected: [('solo_creator', 999.99)]

# Test 4: Includes clawbacks (negative values)
payouts_4 = [
    ('creator_A', 1000.00),
    ('creator_B', -500.00),  # clawback
    ('creator_C', 2000.00),
    ('creator_D', -100.00),  # clawback
]
# Expected order: [('creator_B', -500.00), ('creator_C', 2000.00), ('creator_D', -100.00), ('creator_A', 1000.00)]

# Test 5: All same amount
payouts_5 = [
    ('c1', 100.00),
    ('c2', 100.00),
    ('c3', 100.00),
]
# Expected: Any order (all equal)

# Test 6: Decimal precision
payouts_6 = [
    ('a', 0.01),
    ('b', 0.02),
    ('c', 0.03),
]
# Expected: [('a', 0.01), ('c', 0.03), ('b', 0.02)]

# Test 7: Large batch performance
payouts_7 = [(f'creator_{i}', float(i * 100)) for i in range(50000)]
# Expected: Completes in < 2 seconds
def order_payouts(payouts: list[tuple[str, float]]) -> list[tuple[str, float]]:
    payout_count = len(payouts)
    if payout_count == 0 or payout_count == 1:
        return payouts
    sorted_payouts = sorted(payouts, key = lambda x:x[1])
    small, large = 0, payout_count - 1
    result = []
    while small <= large:
        result.append(sorted_payouts[small])
        small += 1
        if small <= large:
            result.append(sorted_payouts[large])
            large -= 1
    return result
# print(order_payouts(payouts_6))
"""
Question 5: API Rate Limit Bucket Assignment
Company Context: You're designing infrastructure for an API gateway.
Problem:
Your API has clients with different request volumes. You're implementing a "fair queuing" system where you process requests alternating between lowest-volume and highest-volume clients to prevent any single client from monopolizing resources.
Design a function fair_queue_order(client_volumes: List[Dict]) -> List[str] where input is [{'client_id': str, 'pending_requests': int}] and output is a list of client_ids in processing order.
"""
# Test 1: Standard client mix
clients_1 = [
    {'client_id': 'startup_app', 'pending_requests': 50},
    {'client_id': 'enterprise_corp', 'pending_requests': 10000},
    {'client_id': 'medium_saas', 'pending_requests': 500},
    {'client_id': 'hobby_project', 'pending_requests': 5},
    {'client_id': 'growing_app', 'pending_requests': 1000},
]
# Expected: ['hobby_project', 'enterprise_corp', 'startup_app', 'growing_app', 'medium_saas']

# Test 2: Empty queue
clients_2 = []
# Expected: []

# Test 3: Single client
clients_3 = [{'client_id': 'only_one', 'pending_requests': 100}]
# Expected: ['only_one']

# Test 4: All clients with zero pending
clients_4 = [
    {'client_id': 'a', 'pending_requests': 0},
    {'client_id': 'b', 'pending_requests': 0},
    {'client_id': 'c', 'pending_requests': 0},
]
# Expected: Any order (all equal)

# Test 5: Two clients (edge case)
clients_5 = [
    {'client_id': 'small', 'pending_requests': 1},
    {'client_id': 'large', 'pending_requests': 1000000},
]
# Expected: ['small', 'large']

# Test 6: Duplicate volumes
clients_6 = [
    {'client_id': 'a', 'pending_requests': 100},
    {'client_id': 'b', 'pending_requests': 100},
    {'client_id': 'c', 'pending_requests': 200},
    {'client_id': 'd', 'pending_requests': 200},
]
# Expected: One of [100, 200, 100, 200] pattern with corresponding IDs

def fair_queue_order(client_volumes: list[dict]) -> list[str]:
    if not client_volumes:
        return client_volumes
    client_count = len(client_volumes)
    if client_count == 1:
        return ['only_one']
    low, high = 0, client_count - 1
    result = []
    sorted_client_volumes = sorted(client_volumes, key = lambda x:(x['pending_requests'], x['client_id']))
    while low <= high:
        result.append(sorted_client_volumes[low]['client_id'])
        low += 1
        if low <= high:
            result.append(sorted_client_volumes[high]['client_id'])
            high -= 1
    return result
# print(fair_queue_order(clients_1))