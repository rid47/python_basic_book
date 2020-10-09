import glob
import os

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11/images"

possible_files = os.path.join(path, "*.gif")
for file_name in glob.glob(possible_files):
    full_path = os.path.join(path, file_name)
    print(full_path)
