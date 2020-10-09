import os

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"


for file_name in os.listdir(path):
    if file_name.lower().endswith(".gif"):
        full_path = os.path.join(path, file_name)
        new_file_name = full_path[:-4] + "_backup.gif"
        os.rename(full_path, new_file_name)
