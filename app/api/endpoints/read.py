import sqlite3
from fastapi import APIRouter, HTTPException

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