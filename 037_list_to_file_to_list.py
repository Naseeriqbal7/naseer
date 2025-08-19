students = ['Alice', 'Bob', 'Charlie', 'David']

with open('students.txt', 'w') as file:
    for student in students:
        file.write(student + '\n')

new_students = []
with open('students.txt', 'r') as file:
    for ln in file:
        ln = ln.replace('\n', '')
        new_students.append(ln)

print(new_students)  # Output: ['Alice', 'Bob', 'Charlie', 'David']


####

years = [2020, 2021, 2022, 2023]
with open('years.txt', 'w') as file:
    for year in years:
        file.write(str(year) + '\n')

new_years = []
with open('years.txt', 'r') as file:
    for ln in file:
        ln = ln.replace('\n', '')
        new_years.append(int(ln))

print(new_years)
