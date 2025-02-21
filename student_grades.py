#  Analyze trends of students’ grades. Given a list of student grades as input, write a function that determines each students’ trend. 
#  Trend is defined as:
# * Higher: latest value is higher than all previous grades
# * Lower: latest value is lower than all previous grades
# * Inconsistent: any other combination of grades
# Input = [ {“John”: 85, “Jane”: 90}, {“John”: 92, “Jane”: 88} ] Output: { “John”: “higher”, “Jane”: “lower”, }

def student_grades_trends(semesters):
    student_grades = {}
    trends = {}
    # First, collect all grades for each student
    for grades in semesters:
        for student, grade in grades.items():
            if student not in student_grades:
                student_grades[student] = [grade]
            else:
                student_grades[student].append(grade)
    print("Student grades: ", student_grades)
     # Let's analyze trend for each student
    for student, grades in student_grades.items():
        latest = grades[-1]
        previous = grades[:-1]
        print("latest:",latest, "previous:", previous)
        if len(student_grades) < 2:
            trends[student] = "not enough data"
            continue
        if latest > max(previous):
            trends[student]  = "higher"
        elif latest < max(previous):
            trends[student] = "lower"
        else:
            trends[student] = "inconsistent"
    print(trends)
# Test Case
student_grades_trends([ {"John": 85, "Jane": 90, "Sally": 99}, {"John": 90, "Jane": 88, "Sally": 91}, {"John": 92, "Jane": 89, "Sally": 99}])