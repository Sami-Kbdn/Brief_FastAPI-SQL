import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

requete = """ CREATE TABLE Athlete (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255) UNIQUE NOT NULL,
    last_name VARCHAR(255) UNIQUE NOT NULL,
    weight INTEGER NOT NULL,
    age INTEGER NOT NULL,
    height INTEGER NOT NULL
); """

cursor.execute(requete)
conn.commit()
conn.close()
