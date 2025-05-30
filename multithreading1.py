import threading
import time
def function1():
    for i in range(5):
        print(f'Data from function1 value {i}')
        time.sleep(1)

def function2():
    for i in range(5):
        print(f'Data from function2 value {i}')
        time.sleep(1)

print('Processing Started')

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()

t1.join()
t2.join()

print('Processing completed')