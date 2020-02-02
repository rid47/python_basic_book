import sqlite3

people_values = (

    ("Ron","Obvious",42),
    ("Luigi","Vercotti",43),
    ("Mizan", "Ridwan",27)

    )

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO People VALUES(?,?,?)", people_values)
    print(cursor.execute("SELECT * FROM People").fetchall())
    cursor.execute("UPDATE People SET Age=? WHERE FirstName = ? ;", (45, 'Lungi'))
