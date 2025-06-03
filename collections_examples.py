from collections import Counter

l1 = [1,2,3,1,2,3]

num_freq = Counter(l1)
print(num_freq)

str1 = "Hello World"
char_freq = Counter(str1)
print(char_freq)

from collections import defaultdict

num_dict = defaultdict(int)
num_dict['100'] += 1
print(num_dict)
print(num_dict["1000"])


from collections import namedtuple

Point = namedtuple('Point',['x','y','z'])
p = Point(1,2,3)
print(p.x, p.y, p.z)