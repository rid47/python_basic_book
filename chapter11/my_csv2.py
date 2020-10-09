import csv
import os

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"

with open(os.path.join(path, "wonka2.csv"), "r") as my_file:
    reader = csv.reader(my_file, delimiter="\t")
    next(reader)
    for row in reader:
        print(row)
