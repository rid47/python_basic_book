import os
import glob

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11/images"

# root, dirs, files = os.walk(path)
# about walk: https://stackoverflow.com/questions/10989005/do-i-understand-os-walk-right

for root, dirs, files in os.walk(path):
    for file_name in glob.glob(os.path.join(root, "*.png")):
        print(file_name)
        os.rename(file_name, file_name[:-4] + "_backup.png")

