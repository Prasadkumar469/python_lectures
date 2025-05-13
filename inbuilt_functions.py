# Mathematical Functions

print(abs(-10))

print(min([1,2,3,200,302,400])) # 1

print(max([1,2,3,200,302,400])) # 400

print(sum([10,10,10])) # 30

print(round(10.6789)) # 11 
print(round(10.6789,2)) # 10.68   

print(pow(2,4)) # 16  # 2 ** 4

print(divmod(10,3)) # (3,1) # 10//3, 10%3

print(int('10')) # 10
print(float('10.5')) # 10.5
print(str(10)) # '10'
print(bool(10)) # True
print(bool(0)) # False
print(bool('')) # False

l1 = [1,2,3]
t1 = tuple(l1)

t2 = (1,2,3)
l2 = list(t2)

l1 = [1,2,3,3,4,5,6,7,8,9]
s1 = set(l1) # {1,2,3,4,5,6,7,8,9}

d1 = dict(a=1,b=2,c=3) # {'a': 1, 'b': 2, 'c': 3}
keys = ['name', 'age']
values = ['Ramesh', 30]
d2 = dict(zip(keys, values)) # {'name': 'Ramesh', 'age': 30}
d2 = dict((('name', 'Ramesh'), ('age', 30))) # {'name': 'Ramesh', 'age': 30}

print(eval('10+20-20')) # 10
print(any([False, False, False])) # False
print(any([True, False, False])) # True
print(all([True, True, False])) # False
print(all([True, True, True])) # 

print(chr(65)) # A
print(chr(97)) # a
print(ord('A')) # 65
print(ord('a')) # 97

print(bin(10)) # 