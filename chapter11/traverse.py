import os

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"

print(f"Walk: {os.walk(path)}")

for current_folder, subfolders, file_names in os.walk(path):
    for file_name in file_names:
        print(os.path.join(current_folder, file_name))
