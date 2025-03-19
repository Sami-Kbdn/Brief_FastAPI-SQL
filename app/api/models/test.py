import sqlite3

# conn = sqlite3.connect("database.db")

# cursor = conn.cursor()

# requete_ath = """INSERT INTO Athlete(first_name, last_name, weight, age, height) VALUES (?,?,?,?,?);"""
# requete_perf = """INSERT INTO Performances(athlete_id,power_max, hr_max, vo2_max, rf_max, cadence_max) VALUES (?,?,?,?,?,?);"""

# cursor.execute(requete_ath, ("Sam","Sa", 90, 30, 160))
# cursor.execute(requete_perf, (2,30,30,30,40,1))


def insert(first_name : str, last_name : str, weight : int, age : int, height : int):
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


# conn.commit()
# conn.close()
