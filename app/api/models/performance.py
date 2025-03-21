import sqlite3

def create_performance_db():
    """
    Creates the 'Performance' table in the SQLite database if it does not already exist.

    This function establishes a connection to the SQLite database, defines the SQL query to create
    the 'Performance' table with columns for the performance metrics of an athlete, and then executes
    the query. The table is created only if it doesn't already exist.

    The 'id' column is the primary key and will auto-increment with each new record. The 'athlete_id'
    column is a foreign key that references the 'id' of the 'Athlete' table. The other columns represent
    various performance metrics: 'power_max', 'hr_max', 'vo2_max', 'rf_max', and 'cadence_max', all of which
    are required (NOT NULL).

    Steps:
    1. Connect to the SQLite database.
    2. Create the 'Performance' table if it does not exist.
    3. Commit the transaction to save the changes.
    4. Close the connection.

    This function does not return any value.

    Example:
    - Calling this function will ensure the 'Performance' table is created, if necessary.
    """
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
