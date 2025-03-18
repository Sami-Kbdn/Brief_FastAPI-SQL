import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

requete = """ CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) UNIQUE NOT NULL,
    role INTEGER NOT NULL
); """

cursor.execute(requete)
conn.commit()
conn.close()
