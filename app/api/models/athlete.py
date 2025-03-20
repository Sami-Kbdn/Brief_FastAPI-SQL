import sqlite3


def create_athlete_db():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    requete = """ CREATE TABLE IF NOT EXISTS Athlete (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        weight INTEGER NOT NULL,
        age INTEGER NOT NULL,
        height INTEGER NOT NULL
    ); """

    cursor.execute(requete)
    conn.commit()
    conn.close()
