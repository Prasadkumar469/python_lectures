#while
#for
# break, continue, pass
for num in [1,2,3,4,5]:
    print(num) # 1 2 3 4 5
for num in set([1,2,3,4,5]):
    print(num) # 1 2 3 4 5
for key, value in {'a': 1, 'b': 2}.items():
    print(key, value) # a 1 b 2

l1 = [1000,2000,3000,4000,5000]
print(list(range(0,100))) # 0-99
print(list(range(100)))
print(list(range(0,100,2))) # 0-98
index = 0
while index < 100:
    print(index) 
    index += 1 # index = index + 1
#0-99
index = 0
while index < 100:
    print(index) 
    index += 2 # index = index + 1
# 0-98

while True:
    agent = input("Enter agent message: ")    
    if agent == "exit":
        break
    customer = input("Enter customer message: ")
    if customer == "exit":
        continue
    print(f"Agent: {agent}")
    print(f"Customer: {customer}")


