import csv
import os

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"


with open(os.path.join(path, "wonka.csv"), "r") as my_file:
    reader = csv.reader(my_file)
    next(reader)
    for a, b, c in reader:
        print(f"{a} {b} got: {c}")
