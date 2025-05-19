with open('students_marks.txt', 'w') as file:
    file.write('Student Name|English|Maths|Physics\n')
    file.write('ABC|80|70|80\n')
    file.write('XYZ|89|67|87\n')

with open('students_marks.txt', 'r') as file:
    print(file.read())
print('*'*50)
print('Reading file line by line')
with open('students_marks.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)
# Read all line in a list from a file
with open('students_marks.txt', 'r') as file:
    print(file.readlines())

with open('students_marks.txt', 'a') as file:
    file.write('Ramesh|90|78|80\n')
    file.write('Kiran|67|56|80\n')

with open('students_marks.txt', 'r+') as file:
    data = file.read()
    print(data)
    file.write('Test content')

with open('students_marks1.txt', 'w+') as file:
    file.write('Test content')
    file.seek(0)
    data = file.read()
    print(data)
    
with open('output.bin', 'wb') as f:
    f.write(b'\x00\xFF\x00\xFF')

with open('output.bin', 'rb') as f:
    print(f.read())
import json
with open('employee.json','r') as file:
    emp_data = file.read() 
    print(type(emp_data)) # str
    converted_json = json.loads(emp_data)
    print(type(converted_json)) # dict
    print(converted_json)

employee = {'name':'ABC','age':30,'salary':45000}

with open('employee1.json','w') as file:
    employee_str = json.dumps(employee)
    print(employee_str)
    file.write(employee_str)

