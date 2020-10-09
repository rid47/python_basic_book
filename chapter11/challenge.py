import os
base_dir = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".py"):
            # print(os.path.join(root, file))
            full_path = os.path.join(root, file)
            # print(os.path.getsize(root, file))
            print(f"path: {full_path} & size = {os.path.getsize(full_path)}")
