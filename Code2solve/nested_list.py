def nested_lists():
    # Read number of students
    n = 3
    n = int(input().strip())
    
    # Initialize a list to store the student data
    students = []
    
    # Read student data
    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])
    
    # Find the unique grades and sort them
    grades = sorted(set([student[1] for student in students]))
    
    # The second lowest grade
    second_lowest_grade = grades[1]
    
    # Get the names of students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print each name on a new line
    for name in second_lowest_students:
        print(name)

# Call the function
nested_lists()
