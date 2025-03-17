# Write a function that takes a list of menu items with their categories and returns a dictionary where keys are categories and values are lists of items in that category.
# Input: [("Pizza", "Italian"), ("Burger", "American"), ("Pasta", "Italian")]

from collections import defaultdict


def get_menu_categories(menu_items):
    menu_categories = defaultdict(list)
    for item, category in menu_items:
        menu_categories[category].append(item)
    return menu_categories
print(get_menu_categories([("Pizza", "Italian"), ("Burger", "American"), ("Pasta", "Italian")]))
# Output: {"Italian": ["Pizza", "Pasta"], "American": ["Burger"]}