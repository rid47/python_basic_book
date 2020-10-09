import os
import csv

base_path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"

with open(os.path.join(base_path, "wonka.csv"), "r") as my_file:
    reader = csv.reader(my_file)
    next(reader)
    for data in reader:
        print(data)

