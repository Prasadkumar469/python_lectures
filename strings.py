# string 
name = 'ABC'
address = "hyderabad"
print(name.lower())
print(address.upper())
name = 'Ravuri Ramesh'
print(name.swapcase())
name = '  Test word  '
print(name.strip())
name = '  Test word'
print(name.lstrip())
name = 'Test word  '
print(name.rstrip())
name = "Ramesh"
print(name.isalpha())
name = "1234dfdf##"
print(name.isalnum()) # False because of special characters
age = "25"
print(age.isdigit())
name = "ramesh ravuri"
print(name.capitalize())
print(name.title())

paragraph = "This is a test paragraph. It contains multiple sentences. Let's see how it works."
print(paragraph.split(' ')) 
paragraph = "This:is:a:test:paragraph"
print(paragraph.split(':'))
name = "Ramesh Ravuri"
print(name.index('Ravuri'))
print(name.startswith('Ramesh'))
print(name.endswith('Ravuri'))
name = "Ramesh Ravuri"
print(len(name))
print(name.count('R')) # 2
print(name.upper().count('R')) # 3
paragraph = "This is a test paragraph."
print(paragraph.replace('paragraph', 'sentence'))
words = ['This', 'is', 'a', 'test', 'paragraph']
print(' '.join(words)) # This is a test paragraph
first_name = "Ramesh"
second_name = "Ravuri"
print(first_name + " " + second_name) # Ramesh Ravuri
print(f"First Name is {first_name} and Last Name is {second_name}") # First Name is Ramesh and Last Name is Ravuri
print("First Name is {first_name} and Last Name is {second_name}".format(first_name=first_name, second_name=second_name)) # First Name is Ramesh and Last Name is Ravuri
print("First Name is {0} and Last Name is {1}".format(second_name,first_name)) # First Name is Ramesh and Last Name is Ravuri

name = "Ramesh Ravuri"

print(name[0]) # R
name = 'Ramesh'
print(name[2:6])
print(name[2:])
print(name[2:len(name)])
chars = "AaBbDdTt"
print(chars[0::2]) # 0 A, 0+2=2 B, 2+2=4 D, 4+2=6 T, 6+2=8
print(chars[1::2]) # 0 A, 0+2=2 B, 2+2=4 D, 4+2=6, 6+2=8
print(chars[-1])
name = "Ramesh"
print(name[::-1])
from functions import full_name
result = full_name("Hello", "Test")
print(result) # Hello Test


