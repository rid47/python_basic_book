import os

base_path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11/"
os.mkdir("Output")
new_path = base_path + "/Output/python.txt"

file_object = open(new_path, 'w')
file_object.writelines("I'm put here by python")
file_object.close()]
