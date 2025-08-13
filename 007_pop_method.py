from turtle import st


student_list = ['Pradeep', 'Ravi', 'Rajesh', 'Anita',
                'Kiran', 'Lakshmi', 'Rajesh', 'Ramesh',
                  'Kiran', 'Lakshmi', 'Rajesh']

# remove the last time
item = student_list.pop()
print(f"Removed item: {item}")
print(student_list)

# remove the item at index 3
item = student_list.pop(3)
print(f"Removed item at index 3: {item}")
print(student_list)
