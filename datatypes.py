#mutable list, set, dictionary
#immutabe tuple string , all primitive datatptes(int, float,bool)
l1 = []
# l1 = list()
l1.append(1) 
print(l1) # [1]
l1.append(2)
print(l1) # [1,2]

l1.extend([4,5])
print(l1) # [1,2,4,5]

l1.insert(2,3) # [1,2,3,4,5]

# Removal
l1.remove(3) 
print(l1) # [1,2,4,5]

remved_element = l1.pop() # [1,2,4]
# remved_element = 5
removed_element = l1.pop(0) # [2,4]
# # remved_element = 1

del l1[1]

l1 = [1,3,4,5,2,6]
l1.sort() # [1,2,3,4,5,6]
l1.sort(reverse=True)

for num in l1:
    print(num)

l1 = [1,2,3]
for num in l1:
    print(num*num)
#1
#4
#9
l1 = [1,2,3,2]
l1.count(2) # 2

l1.clear() # []

l1 = [1,2,3,4]
l1.reverse() # [4,3,2,1]

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2 # l3 = [1,2,3,4,5,6]
l1.extend(l2) # l4 = [1,2,3,4,5,6]

l1 = [1] * 10 # l1 = [1,1,1,1,1,1,1,1,1,1] 
print(l1)

l1 = [1,2,3,4] #[0,1,2,3] 
print(l1[0])

# Set
s1 = {1,2,3} # 1-> 100 2-> 200
print(s1)
s1.add(4) # {1,2,3,4}
s1.update([5,6]) # {1,2,3,4,5,6}
s1.remove(5) # {1,2,3,4,6}
s1.discard(6)  #{1,2,3,4,6}
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1.intersection(s2) # {2,3} 
s3 = s1 & s2
s3 = s1.union(s2) # {1,2,3,4}
s3 = s1 ^ s2 # 
s4 = s1 - s2 # {1}
s5 = s2 - s1 # {4}
s1.difference(s2) # {1}
s2.difference(s1) # {4}
s1.clear() # remove all the elements s1 = {}

# dictionary
# d1 = {'id': 1, 'name': 'ABC'}
d1 = dict()
d1['id'] = 1
d1['name'] = 'ABC'
print(d1)
d1.update({'age':26,'salary':34000})
print(d1)

d1.pop('id')
print(d1)
removed_item = d1.popitem()
print(removed_item)
print(d1)
# d1.clear() # {}
print(d1.keys())
print(d1.values())
print(d1.items())
for key, value in d1.items(): # key = id, value=1
    print(f"Key: {key} Value: {value}") # "Key: id Value: 1"

d2 = {'id': 1, 'name': 'ABC', 'age': 26, 'salary': 34000}
# print(d1['id']) # 1
dept = d1.get('dept',None) # None

# Tuple -> Immutable data type
t1 = (1,2,3)
t1[0] = 100 
for num in t1:
    print(num)
#1
#2
#3
t1.count(1) # 1
t1.index(3) # 2


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















