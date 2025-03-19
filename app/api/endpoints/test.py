import sqlite3


# def read():
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM athlete')


def insert(first_name: str, last_name: str, weight: int, age: int, height: int):
    conn = sqlite3.connect('database.db')

    c = conn.cursor()
    try :
        c.execute(f"INSERT INTO Athlete ('first_name', 'last_name', 'weight', 'age', 'height' ) VALUES ('{first_name}', '{last_name}', {weight}, {age}, {height})")
        conn.commit()
        return "OK"
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()