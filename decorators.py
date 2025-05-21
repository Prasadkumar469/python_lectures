# Basic decorator
def prevent_args(func): # func -> add
    def inner(*args, **kwargs): # args -> (10,20)
        print('before calling add function')
        if len(args) > 2:
            print('Arguements are more than two')
        else:
            func(*args, **kwargs) # add(10,20)
        print('After calling add function')
    return inner

@prevent_args
def add(a,b):
    print(f"sum is {a+b}")



add(10,20,30)

# Advanced decorator
def greet_message(frequency): # frequence -> 3
    def outer(func): # func -> greet function reference
        def inner(*args, **kwargs):
            for i in range(frequency): # 0 1 2
                func(*args, **kwargs) # greet()
        return inner
    return outer


@greet_message(10)
def greet():
    print('Hi How Are You')

greet()


l1 = [1,2,3,4] # 1L -> 100MB -> Heap Memory
iterator = iter(l1) 
# print(next(iterator)) # 1
# print(next(iterator)) # 2
# print(next(iterator)) # 3
# print(next(iterator)) # 4
#print(next(iterator))

while True:
    try:
        print(next(iterator)) # 1 2 3 4 
    except:
        break

l1 = [1,2,3,4]

for index, element in enumerate(l1, start=100):
    print(f"index: {index} element: {element}")

