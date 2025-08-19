# list of list with 5 rows and 4 columns of departments and their performance
departments = [
    ['HR', 85, 90, 88],
    ['Finance', 78, 82, 80],
    ['IT', 92, 95, 94],
    ['Marketing', 80, 85, 82],
    ['Sales', 88, 90, 89]
]

import csv

with open('departments.csv', mode='w', newline="") as file:
    w_obj = csv.writer(file)
    w_obj.writerows(departments)