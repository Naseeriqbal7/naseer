# Create a list of lists for student scores and names with 5 rows and 3 columns
student_scores = [
    ['Pradeep', 88, 92],
    ['Anjali', 85, 90],
    ['Ravi', 79, 85],
    ['Sita', 95, 98],
    ['Rahul', 82, 87]
]

# Print the list of lists
for student in student_scores:
    print(student[0], "Scores:", student[1], student[2])

print()

for student in student_scores:
    for item in student:
        print(item, end='\t')
    print()  # New line after printing all items in a student list

