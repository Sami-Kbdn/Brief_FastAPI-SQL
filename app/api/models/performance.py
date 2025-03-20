import sqlite3

def create_performance_db():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    requete = """ CREATE TABLE IF NOT EXISTS Performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        athlete_id INTEGER NOT NULL,
        power_max INTEGER NOT NULL,
        hr_max INTEGER NOT NULL,
        vo2_max INTEGER NOT NULL,
        rf_max INTEGER NOT NULL,
        cadence_max INTEGER NOT NULL,
        FOREIGN KEY (athlete_id) REFERENCES athlete(id) 
    ); """

    cursor.execute(requete)
    conn.commit()
    conn.close()
