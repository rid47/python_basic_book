import os


path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"

files_and_folder = os.listdir(path)
print(f"files and folder: {files_and_folder}")

for folder_name in files_and_folder:
    full_path = os.path.join(path, folder_name)
    print(full_path)
    if os.path.isdir(full_path):
        os.rename(full_path, full_path + " folder")
