class Employee:
    def __init__(self, name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def bonus(self):
        return self.salary * 0.1

    def total_salary(self):
        return int(self.salary + self.bonus())

employee1 = Employee('Ramesh', 30, 50000) # reference -> 100
print(employee1.name)
print(employee1.age)
print(employee1.salary)
print(employee1.bonus())
print(employee1.total_salary())

class Employee:
    def __init__(self, name,age,salary):
        self.__bonus_value = 0.1
        self.name = name
        self.age = age
        self.salary = salary
    # private method -> encapsulation -> data hiding
    def __bonus(self):
        return self.salary * self.__bonus_value

    def total_salary(self):
        return int(self.salary + self.__bonus())

employee1 = Employee('Ramesh', 30, 50000) # reference -> 100
print(employee1.name)
print(employee1.age)
print(employee1.salary)
print(employee1._Employee__bonus_value) # Data Mangling
print(employee1._Employee__bonus()) # Data Mangling
# print(employee1.__bonus_value) # AttributeError: 'Employee' object has no attribute '__bonus'
# print(employee1.__bonus())
# print(employee1.total_salary())

# Inheritance

