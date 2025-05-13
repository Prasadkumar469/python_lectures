# Simple function to print a greeting message
def greet():
    print("Hello, World!") 

greet()

# Parameterized function
def add(a, b):
    result = a + b
    print(result)

add(10, 10)

# Parameterized function with return value
def full_name(first_name, last_name):
    result = first_name + " " + last_name
    return result
result = full_name("Ramesh", "Ravuri")
print(result) # Ramesh Ravuri

# Function with default parameter
def area_of_circle(radius, pi=3.14):
    area = pi * radius * radius
    return area

result = area_of_circle(5)
print(result)
result = area_of_circle(10,pi=3.18)
print(result) # 314.0

# Function with variable number of arguments and keyword arguments
def catch_args_kwargs(*args, **kwargs):
    print(args) # (1, 2, 3, 4, 5)
    print(kwargs) # {'a': 1, 'b': 2, 'c': 3}
catch_args_kwargs(1, 2, 3, 4, 5, a=1, b=2, c=3)

def sum_numbers(*args): # (1,2,3)
    result = 0
    for num in args:
        result += num
    return result
numbers = list(range(1,101))
result = sum_numbers(*numbers) # 15sum_numbers(1,2,3,4,5..100)
print(result)

num = 10
simple_lambda = lambda : "Hello World"
print(simple_lambda()) # Hello World

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Ramesh", "Ravuri")) # Ramesh Ravuri

