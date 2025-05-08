# area of circle πr2

PI = 3.14
radius = 5
area = PI * radius ** 2
print(f"Area of circle is:{area}")

# perimeter of circle 2πr

PI = 3.14
radius = 5
perimeter = 2 * PI * radius
print(f"Perimeter of circle is:{perimeter}")

# find given number is prime or not
input_number = 4 # 1,2,3,4,5
for num in range(2,input_number):
    if input_number % num == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# write a program to print table for given number
input_number = 3 # 1*5 = 5
for index in range(1,11):
    print(f"{index}*{input_number}={index*input_number}")

# write a program to find given number is palindrome or not
paragraph = "This is just simple paragraph"
count = 0
for char in paragraph:
    if char in 'aeiou':
        count += 1 # c
print(f"Number of vowels in paragraph is:{count}")

# write a program to reverse of a string
input_string = "Hyderabad"
#reversed_string = "dabaredyH"
#print(input_string[::-1])
reversed_string = ""
for index in range(len(input_string)-1,-1,-1): # 8,7,6,5,4,3,2,1,0
    reversed_string = reversed_string + input_string[index] #"dab"
print(reversed_string)




