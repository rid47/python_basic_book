import csv
import os

base_path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"

lines = [
["Name", "Favourite Pastime", "Type of Pasttime"],
["Dua", "YES", "Excellent"]
]

with open(os.path.join(base_path, "new.csv"), "w") as my_file:
    writer = csv.writer(my_file)
    writer.writerows(lines)
