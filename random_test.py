import random
import time
# print(random.randint(1, 100))
# while True:
#     print(random.randint(1, 6))
#     time.sleep(3)

colors = ['red', 'green', 'blue', 'yellow', 'orange']
print(random.choice(colors))

l1 = [1, 2, 3, 4, 5]
random.shuffle(l1)
print(l1)

print(random.random()) # random number between 0 and 1