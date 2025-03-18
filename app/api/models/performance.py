import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

requete = """ CREATE TABLE Performances (
    id INTEGER PRIMARY KEY,
    athlete_id INTEGER NOT NULL,
    power_max INTEGER NOT NULL,
    hr_max INTEGER NOT NULL,
    vo2_max INTEGER NOT NULL,
    rf_max INTEGER NOT NULL,
    cadence_max INTEGER NOT NULL
); """

cursor.execute(requete)
conn.commit()
conn.close()
