# Each summer, the library organizes a summer reading program for students. 
# Each book is assigned to a category and has a point value. 
# Students can read books to score points in up to 3 categories, and can score up to 3 books for up to 10 points in a category. 
# Given a list of books that a student read including their  category and point values, what is the student's maximum possible score?
# # input = [
#     {"title": "The Hobbit", "category": "Fiction", "points": 4},
#     {"title": "Harry Potter", "category": "Fiction", "points": 3},
#     {"title": "A Brief History of Time", "category": "Science", "points": 5},
#     {"title": "Cosmos", "category": "Science", "points": 4},
#     {"title": "The Body", "category": "Biology", "points": 6},
#     {"title": "Sapiens", "category": "History", "points": 7},
#     {"title": "Guns, Germs, and Steel", "category": "History", "points": 8},
# ]
# Expected output: 27 (Fiction: 7, Science: 9, History: 10 (capped) - best 3 categories)
def max_reading_score(books):
    # Dictionary to store points per category
    category_points = {}
    
    # Group books by category and sort by points (highest first)
    for book in books:
        category = book["category"]
        points = book["points"]
        
        if category not in category_points:
            category_points[category] = []
        
        category_points[category].append(points)
    
    # Sort points in descending order for each category
    for category in category_points:
        category_points[category].sort(reverse=True)
        # Take only the top 3 books
        category_points[category] = category_points[category][:3]
        # Cap at 10 points per category
        if sum(category_points[category]) > 10:
            category_points[category] = 10
        else:
            category_points[category] = sum(category_points[category])
    
    # Get the best 3 categories (or fewer if there aren't 3)
    best_categories = sorted(category_points.values(), reverse=True)[:3]
    
    return sum(best_categories)
test_case = [
    {"title": "The Hobbit", "category": "Fiction", "points": 4},
    {"title": "Harry Potter", "category": "Fiction", "points": 3},
    {"title": "A Brief History of Time", "category": "Science", "points": 5},
    {"title": "Cosmos", "category": "Science", "points": 4},
    {"title": "The Body", "category": "Biology", "points": 6},
    {"title": "Sapiens", "category": "History", "points": 7},
    {"title": "Guns, Germs, and Steel", "category": "History", "points": 8},
]
print("Test results:", max_reading_score(test_case))
