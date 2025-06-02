import os

print(os.path.exists('C:\\code\\training\\python_lectures\\employee.json'))
print(os.path.exists(r'C:\code\training\python_lectures\employee.json'))

folder_path = "C:\example"

# os.remove('C:\example\example1.txt')

# for filename in os.listdir(folder_path):
#     print(filename)
file_list = []
for dirpath, dirnames, filenames in os.walk(folder_path):
    file_list.extend(filenames)
print(file_list)



