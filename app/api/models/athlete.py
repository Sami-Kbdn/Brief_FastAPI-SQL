import sqlite3


def create_athlete_db():
    """
    Creates the 'Athlete' table in the SQLite database if it does not already exist.

    This function establishes a connection to the SQLite database, defines the SQL query to create
    the 'Athlete' table with columns for the athlete's id, first name, last name, weight, age, and height,
    and then executes the query. The table is created only if it doesn't already exist.

    The 'id' column is the primary key and will auto-increment with each new record. The 'first_name',
    'last_name', 'weight', 'age', and 'height' columns are required (NOT NULL).

    Steps:
    1. Connect to the SQLite database.
    2. Create the 'Athlete' table if it does not exist.
    3. Commit the transaction to save the changes.
    4. Close the connection.

    This function does not return any value.

    Example:
    - Calling this function will ensure the 'Athlete' table is created, if necessary.
    """
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
