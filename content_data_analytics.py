from collections import defaultdict
# 1. Process user activity data to identify users at risk of churning based on declining engagement.
# Identify users with consistent decline (each week lower than previous) and calculate their decline rate.
weekly_activity = [
    {"user_101": 8, "user_102": 12, "user_103": 15, "user_104": 5},
    {"user_101": 6, "user_102": 10, "user_103": 18, "user_104": 3},
    {"user_101": 4, "user_102": 18, "user_103": 20, "user_104": 1},
    {"user_101": 2, "user_102": 6, "user_103": 22, "user_104": 0}
]
# Expected output: {
#     "at_risk_users": ["user_101", "user_104"],
#     "decline_rates": {"user_101": 0.75, "user_104": 1.0}  # percentage decline from first to last week
# }
# slow thinking: 
# 1. arrange all user activity in a dict with user as key and activity values 
# 2. compare the elements of the list of values and add to at_risk 
# 3. first and last value pct and add to rates
def churning_users(weekly_activity):
    user_weekly_activity =  defaultdict(list)
    at_risk_users = []
    decline_rates = defaultdict(float)
    # Get all user activity in one dict
    for week in weekly_activity:
        for user,value in week.items():
            user_weekly_activity[user].append(value)
    for user, activity in user_weekly_activity.items():
        is_declining = True
        for i in range(1,len(activity)):
            if activity[i] >= activity[i-1]:
                is_declining = False
                break
        if is_declining:
            at_risk_users.append(user)
            if activity[0] > 0:
                decline_rates[user] = round((activity[0] - activity[-1]) / activity[0], 2)
            else:
                decline_rates[user] = 0.0
    return {"at_risk_users": at_risk_users, "decline_rates": dict(decline_rates)}
# print(churning_users(weekly_activity))
# 2. Given daily content rankings by region, find shows that are consistently popular across regions. 
# Find shows that appear in top 3 of all regions 
regional_rankings = [
    {"US": ["Show A", "Show B", "Show C"], "UK": ["Show B", "Show A", "Show D"], "CA": ["Show A", "Show C", "Show B"]},
    {"US": ["Show A", "Show C", "Show B"], "UK": ["Show A", "Show B", "Show C"], "CA": ["Show B", "Show A", "Show C"]},
    {"US": ["Show B", "Show A", "Show C"], "UK": ["Show A", "Show C", "Show B"], "CA": ["Show A", "Show B", "Show D"]},
    {"US": ["Show D", "Show A", "Show B"], "UK": ["Show A", "Show D", "Show B"], "CA": ["Show B", "Show D", "Show A"], "IN": ["Show A", "Show B", "Show D"]},
    {"US": ["Show A", "Show E", "Show B"], "UK": ["Show B", "Show A", "Show E"], "CA": ["Show E", "Show A", "Show B"], "IN": ["Show B", "Show A", "Show E"]},
    {"US": ["Show F", "Show A", "Show B"], "UK": ["Show A", "Show F", "Show B"], "CA": ["Show B", "Show F", "Show A"], "IN": ["Show F", "Show B", "Show A"]},
]
# Expected Output: 
# Slow thinking: 1. count the occurances of the shows each day for each region and store in dict
# {US: {"Show A": 6, "Show B": 6, "Show C": ...}, UK:
def find_top_shows(regional_rankings):
    # initialize the regional count dict
    regional_count = defaultdict(lambda: defaultdict(int))
    # loop over each day
    for day_ranking in regional_rankings:
    # loop over each region and list of shows
        for region, shows in day_ranking.items():
            # count each show in the list of shows and add to the dict
            for show in shows:
                regional_count[region][show] += 1
    top_shows = {}
    for region, show_counts in regional_count.items():
    # Sort shows by count (descending), then by show name (for tie-breaking)
        sorted_shows = sorted(show_counts.items(), key=lambda x: (-x[1], x[0]))
        top_shows[region] = [show for show, count in sorted_shows[:3]]
    return top_shows
print(find_top_shows(regional_rankings))


