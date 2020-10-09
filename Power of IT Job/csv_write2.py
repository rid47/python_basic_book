import csv
import os

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter11"

ratings = [

["Movie", "Rating"],
["Rebel", "3"],
["Monty", "5"],
["Santa", "0"]

]

with open(os.path.join(path, "movies.csv"), "w") as my_file:
    writer = csv.writer(my_file)
    writer.writerows(ratings)
