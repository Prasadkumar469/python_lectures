#Syntax for comprehension
#varaible = [expresions for item in collection condition]
#map & filter
l1 = [1,2,3,4,5]
even_numbers_with_square = [num * num for num in l1 if num % 2 == 0]
print(even_numbers_with_square)

words = ['F','M','M','F']
female_list = [gender for gender in words if gender == 'F']
print(female_list)

words = ('F','M','M','F')
female_list = tuple((gender for gender in words if gender == 'F'))
print(female_list)

names = ['Ramesh','Usha','Kiran','Harini']
genders = ['M','F','M','F']
print(tuple(zip(names,genders))) # (('Ramesh','M'),('Usha','F'))
person = {name:gender for name, gender in zip(names,genders)}
print(person)

words = ('F','M','M','F')
female_set = {gender for gender in words if gender == 'F'}
print(female_set)



l1 = [('Ramesh',30),('Kiran',25),('Suresh',40)]
l1.sort(key=lambda x: x[1])
print(l1)

employees = {'Ramesh':20, 'Kiran':19,'Suresh':50}
print(employees)
sorted_employees = sorted(employees.items(), key=lambda x: x[1])
final_employees = {name:age for name, age in sorted_employees}
print(final_employees)

gender = 'M'
output = "Female" if gender == 'F' else "Male"
print(output)

