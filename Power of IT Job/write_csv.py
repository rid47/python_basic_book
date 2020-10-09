import csv
import os

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"

with open(os.path.join(path, "movies.csv"), "w") as my_file:
    writer = csv.writer(my_file)
    writer.writerow(["Movie", "Rating"])
    writer.writerow(["Rebel Without a Cause", "3"])
    writer.writerow(["Monty Python's Life of Brian", "5"])
    writer.writerow(["Transporter", "6.7"])


