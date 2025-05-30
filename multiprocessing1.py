import multiprocessing
import time
def function1():
    for i in range(5):
        print(f'Data from function1 value {i}')
        time.sleep(1)

def function2():
    for i in range(5):
        print(f'Data from function2 value {i}')
        time.sleep(1)
        
if __name__ == "__main__":
    print('Processing Started')

    p1 = multiprocessing.Process(target=function1)
    p2 = multiprocessing.Process(target=function2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Processing completed')