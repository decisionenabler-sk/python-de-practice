# write a solution to calculate 
customer_interactions = {
    'support_tickets': {
        'Alice': [15, 22, 10],
        'Bob': [5, 8, 12],
        'Charlie': [20, 7, 15]
    },
    'interaction_types': {
        'Alice': ['email', 'phone', 'chat'],
        'Bob': ['chat', 'email', 'phone'],
        'Charlie': ['phone', 'email', 'support']
    }
}
# Write a function that identifies the customer(s) with the longest average support ticket time. 
# The input is a nested dictionary where the key support_tickets contains customer names as keys and a list of ticket times as values. 
# Return a list of customer names with the longest average ticket time.

# def get_longest_avg_ticket_time(customer_interactions):
