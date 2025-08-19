import csv

with open('emp_data.csv', mode='r', newline='') as file:
    r_obj = csv.reader(file)
    for row in r_obj:
        # print(row)
        print(row[0], row[1], row[4])