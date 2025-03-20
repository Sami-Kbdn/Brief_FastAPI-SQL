import sqlite3


def create_user_db():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    requete = """ CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        role INTEGER NOT NULL
    ); """

    cursor.execute(requete)
    conn.commit()
    conn.close()
