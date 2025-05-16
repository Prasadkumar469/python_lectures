print('one')
print('two')
try:
    number = int('100')
    result = 9/0
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
print('three')
print('four')



print('one')
print('two')
try:
    number = int('100')
    result = 9/0
except Exception as e:
    print(e)
print('three')
print('four')

print('program started')
try:
    # result = a + b
    result = 10 + 10
    print(result)
    # connection = DatabaseConncetion('root:root://mydomain.com/employee')
    # using connection fetch the employee data from database
except Exception as e:
    print(e)
finally:
    # connection.close()
    print('program is completed')

from loguru import logger
print(logger.info('It is test sentence'))
print(logger.warning('it is a warning'))
print(logger.error('it is a error'))
print(logger.debug('it is debug'))
try:
    9/0
except Exception as e:
    logger.exception(e)
# class Employee:
#     employees = []
#     def insert(self, employee):
#         try:
#             Employee.emploees.append(employee)
#         except Exception as e:
#             print(e)

