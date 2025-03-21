import sqlite3


def create_user_db():
    """
    Creates the 'User' table in the SQLite database if it does not already exist.

    This function establishes a connection to the SQLite database, defines the SQL query to create
    the 'User' table, and then executes the query. The table is created only if it doesn't already exist.

    The 'id' column is the primary key for each user. The 'username' column is unique and required (NOT NULL),
    used to identify each user. The 'password' column is required (NOT NULL) and stores the hashed password for authentication.
    The 'role' column is an integer that determines the user's role (e.g., admin, user, etc.).

    Steps:
    1. Connect to the SQLite database.
    2. Create the 'User' table if it does not exist.
    3. Commit the transaction to save the changes.
    4. Close the connection.

    This function does not return any value.

    Example:
    - Calling this function will ensure the 'User' table is created, if necessary.
    """
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
