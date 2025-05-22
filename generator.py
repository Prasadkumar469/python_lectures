# special type of function if a functions
# contains yield it is a generator function
def read_bank_data():
    with open('bank_data.txt', 'r') as file:
        file.readline()
        for line in file: # 'ABC|Hyd|1000|20000'
            data = line.strip().split('|') # ['ABC', 'Hyd', '1000', '20000']
            yield {
                'name': data[0],
                'address': data[1] if data[1] else 'Pune',
                'debit': float(data[2]),
                'credit': float(data[3])
            }

for record in read_bank_data():
    print(record)


# print n numbers using generator
def print_n_numbers(n):
    for i in range(1,n+1):
        yield i

# for number in print_n_numbers(10):
#     print(number,end=' ')
print_n_numbers_gen = print_n_numbers(10)
print(next(print_n_numbers_gen)) # 1
print(next(print_n_numbers_gen)) # 2
print(next(print_n_numbers_gen)) # 3 

while True:
    try:
        print(next(print_n_numbers_gen))
    except StopIteration:
        break




