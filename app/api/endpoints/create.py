import sqlite3
from fastapi import APIRouter, Depends, status
from typing import Annotated
from app.api.db.transaction import get_user


router = APIRouter()

@router.post('/insert_athlete')
async def insert_athlete(data:dict, user: Annotated[str, Depends(get_user)]):
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT role from User WHERE username = ?", (user,))
    result = c.fetchone()
    if result[0] != 1:
        return "Access denied"
    try :
        c.execute(f"INSERT INTO Athlete ('first_name', 'last_name', 'weight', 'age', 'height' ) VALUES (?, ?, ?, ?, ?)", (data["first_name"], data['last_name'], data['weight'], data['height'], data['age']))
        conn.commit()
        return "OK"
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()


@router.post('/insert_performance')
async def insert_performance(data:dict):
    conn = sqlite3.connect('database.db')

    c = conn.cursor()
    try :
        c.execute(f"INSERT INTO Performance ('athlete_id', 'power_max', 'hr_max', 'vo2_max', 'rf_max', 'cadence_max' ) VALUES (?, ?, ?, ?, ?)", (data["athlete_id"], data['power_max'], data['hr_max'], data['vo2_max'], data['rf_max'], data['cadence_max']))
        conn.commit()
        return "OK"
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()
