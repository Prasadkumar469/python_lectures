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












