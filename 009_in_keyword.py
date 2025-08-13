student_list = ['Pradeep', 'Ravi', 'Rajesh', 'Anita',
                'Kiran', 'Lakshmi', 'Rajesh', 'Ramesh',
                  'Kiran', 'Lakshmi', 'Rajesh']

print('Rajesh' in student_list)
print('Praveen' in student_list)
print('Rajesh' not in student_list)
print('Praveen' not in student_list)

emp = 'Rajesh'
if emp in student_list:
    print(f'{emp} is in the student list')
else:
    print(f'{emp} is not in the student list')
