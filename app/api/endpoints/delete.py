import sqlite3
from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.db.transaction import get_user


router = APIRouter()

@router.delete('/delete_athlete')
async def delete_athlete(data:dict, user: Annotated[str, Depends(get_user)]):
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

@router.delete('/delete_performance')
async def delete_performance(data:dict, user: Annotated[str, Depends(get_user)]):
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