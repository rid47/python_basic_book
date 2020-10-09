import os

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11/images"

directory = os.listdir(path)

print(directory)


for folder in directory:
    full_path = path + "/" + folder
    print(full_path)
    for file in os.listdir(full_path):
        file_path = full_path + "/" + file
        print(file_path)
