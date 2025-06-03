from collections import defaultdict
# Given two nonempty lists of user_ids and tips, write a function most_tips to find the user that tipped the most.
# Input example:
user_ids = [103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102] # 105
tips = [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2]

def most_tips(user_ids, tips):
    user_tips = zip(user_ids, tips)
    tip_count = defaultdict(int)
    for user_id, tip in user_tips:
        tip_count[user_id] += tip
    max_tips = max(tip_count.values())
    for user_id, total_tips in tip_count.items():
        if total_tips == max_tips:
            return user_id
# Test
print(most_tips(user_ids, tips))  # Output: 105