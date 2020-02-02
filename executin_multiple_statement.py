import sqlite3

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(


        """ DROP TABLE IF EXISTS People;
        CREATE TABLE People(

        FirstName TEXT,
        LastName TEXT,
        AGE INT
        );
        INSERT INTO People VALUES(
        'Ron',
        'Obvious',
        "45"
        );"""

        )
