import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

requete = """ INSERT INTO User ("username", "password", "role") VALUES (?,?,?);"""

cursor.execute(requete, ("test2","test", 0))


conn.commit()
conn.close()

