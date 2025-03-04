# Our library system has four different branches. 
# Sometimes one or more of them needs to close due to repairs or inclement weather. When a branch closes some of the patrons will go to other branches while others just stay home. 
# The dictionary below shows, for each branch, the number of patrons who will go the the branch if it's open 
# as well as the number of patrons who will go to each of the other branches if it's closed. 
# Given a set of the branches closed on a given day, return a dictionary showing the number of patrons expected at the other branches.

branch_data = {
    "Sunnyvale": {"open": 120, "San Jose": 30, "Campbell": 25, "Santa Clara": 20},
    "San Jose": {"open": 140, "Sunnyvale": 35, "Campbell": 40, "Santa Clara": 30},
    "Campbell": {"open": 110, "Sunnyvale": 20, "San Jose": 25, "Santa Clara": 15},
    "Santa Clara": {"open": 130, "Sunnyvale": 40, "San Jose": 35, "Campbell": 30}
}
closed_branches = ["Sunnyvale", "Campbell"]

def get_branch_traffic(branch_data, closed_branches):
    # get regular traffic in the open branch
    open_branches = {b: branch_data[b]["open"] for b in branch_data if b not in closed_branches}
    # get the traffic from closed branches added to the open branches
    for closed in closed_branches:
        if closed in branch_data:
            for branch, patrons in branch_data[closed].items():
                if branch != "open" and branch in open_branches:
                    open_branches[branch] += patrons
    return open_branches
print(get_branch_traffic(branch_data, closed_branches))