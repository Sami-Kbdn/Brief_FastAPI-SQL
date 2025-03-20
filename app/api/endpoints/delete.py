import sqlite3
from fastapi import APIRouter


router = APIRouter()

@router.post('/delete_athlete')
async def delete_athlete(data:dict):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try :
        c.execute(f"DELETE FROM Athlete WHERE id=?", (data["id"],))
        c.execute(f"DELETE FROM Performance WHERE athlete_id=?", (data["id"],))
        conn.commit()
        return "OK"
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()

@router.post('/delete_performance')
async def delete_performance(data:dict):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try :
        c.execute(f"DELETE FROM Performance WHERE athlete_id=?", (data["id"],))
        conn.commit()
        return "OK"
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()