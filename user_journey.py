from collections import defaultdict, Counter
"""
To understand user behavior, your product team wants to know the most common 3-step path users take on your website.
Given a list of page view events sorted by timestamp, find the most common sequence of three consecutive pages visited by users. 
The input is a list of tuples (user_id, page_url).
"""
# Example Input:
page_views = [
    ('user1', '/home'),
    ('user1', '/products'),
    ('user2', '/home'),
    ('user1', '/cart'),
    ('user2', '/products'),
    ('user1', '/checkout'),
    ('user2', '/pricing'),
    ('user3', '/home'),
    ('user3', '/products'),
    ('user3', '/cart'),
]
# Slow Thinking: group by user, get the 3-page seq, count the freq of each 3-page seq
def most_consecutive_page_vists(page_views):
    users_pages = defaultdict(list)
    seq_counts = Counter()
    for user,page in page_views:
        pages = users_pages[user]
        pages.append(page)
        # check if we have  > 3 items in the pages for the user
        if len(pages) >= 3:
            # Only look at the last 3 pages to form a sequence
            seq = tuple(pages[-3:])
            seq_counts[seq] += 1
    return seq_counts.most_common(1)[0][0] if seq_counts else None
print(most_consecutive_page_vists(page_views))

# ...existing code...

# Additional test cases
test_cases = [
    # Test 1: Common pattern with multiple users
    [
        ('user1', '/home'), ('user1', '/products'), ('user1', '/cart'),
        ('user2', '/home'), ('user2', '/products'), ('user2', '/cart'),
        ('user3', '/home'), ('user3', '/products'), ('user3', '/cart')
    ],
    
    # Test 2: Different patterns
    [
        ('user1', '/home'), ('user1', '/about'), ('user1', '/contact'),
        ('user2', '/products'), ('user2', '/cart'), ('user2', '/checkout'),
        ('user3', '/home'), ('user3', '/products'), ('user3', '/about')
    ],
    
    # Test 3: Short sequences (edge case)
    [
        ('user1', '/home'), ('user1', '/products'),
        ('user2', '/home')
    ],
    
    # Test 4: Single user multiple visits
    [
        ('user1', '/home'), ('user1', '/products'), ('user1', '/cart'),
        ('user1', '/checkout'), ('user1', '/home'), ('user1', '/products')
    ]
]

# Test all cases
for i, test in enumerate(test_cases, 1):
    print(f"\nTest {i} result:", most_consecutive_page_vists(test))