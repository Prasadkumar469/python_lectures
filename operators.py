# Arithmetic Operators
#+, -, *, /, //, %, **
a = 10
b = 20
print(a+b)
print(b-a)
print(a*b)
print(b/a) # 2.0000
print(b//a) # Floor division # 2
print(b%a) # Modulus #0
print(2**2) # 4
print(3 % 5) # 3


# Comparison Operators
# ==, !=, >, <, >=, <=
a = 'abc'
b = 'abc'
print(a == b) # True
a = 10
b = 20
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a <= b) # True
print(a >= b) # False

# Logical Operators
# and, or, not

a = 10
b = 20
print(a > 5 and b < 30) # True
print(a > 30 or b < 10) # True
print(not (a<20)) # False

# Assignment Operators
# =, +=, -=, *=, /=, //=, %=, **=
a = 10
a = a + 5
a += 5 # a = a + 5
a -= 5 # a = a - 5
a *= 5 # a = a * 5 
a /= 5 # a = a / 5
a //= 5 # a = a // 5
a %= 5 # a = a % 5
a **= 5 # a = a ** 5

# Membership Operators
# in, not in
l1 = [1,2,3,4,5]
print(4 in l1) # True
print(6 in l1) # False
print(4 not in l1) # False
print(6 not in l1) # True

#Identity Operators
# is, is not
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 == l2) # True, because the values are same
print(id(l1), id(l2))
print(l1 is l2) # True
print(l1 is not l2) # False, because the values are same