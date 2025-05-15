l1 = [1,2,3,4]
l2 = []
for num in l1:
    l2.append(num*num)

result = list(map(lambda x: x * x,l1))
print(result)
names = ['abc','xyz']
result = list(map(lambda x:x.upper(), names))
result = list(map(str.upper, names))
print(result)

l1 = list(range(1,51))
result = list(filter(lambda x:x % 2 == 1,l1))
print(result)

employees = [
             {'id':1,'name':'abc','salary':30000},
             {'id':2,'name':'xyz','salary':40000},
             {'id':3,'name':'hyd','salary':120000}
            ]
result = list(filter(lambda item: item['salary'] > 100000,employees))
print(result)
from functools import reduce
numbers = [1,2,3,4]
numbers = reduce(lambda x,y:x+y, numbers)
number = [1,2,3,4]
numbers = reduce(lambda x,y:x*y, numbers)
print(numbers)



