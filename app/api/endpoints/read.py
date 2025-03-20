import sqlite3
from fastapi import APIRouter

router = APIRouter()

@router.get('/all_athletes')
async def all_athletes():
    conn = sqlite3.connect('database.db')

    c = conn.cursor()
    try :
        c.execute("SELECT * FROM Athlete")
        result = c.fetchall()
        return result
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()


@router.get('/max_power')
async def all_athletes():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    try :
        c.execute("SELECT MAX(power_max) FROM Performances;")
        max_power = c.fetchone()
        max_power = dict(max_power)
        c.execute(f"""
                            SELECT 
                Athlete.first_name, 
                Athlete.last_name
            FROM 
                Athlete
            INNER JOIN 
                Performances 
                ON Athlete.id = Performances.athlete_id
            WHERE 
                Performances.power_max ={max_power['MAX(power_max)']};""")
        result = c.fetchone()
        print(result)
        return result
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()