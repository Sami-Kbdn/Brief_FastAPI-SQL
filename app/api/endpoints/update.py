import sqlite3
from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.db.transaction import get_user

router = APIRouter()

@router.put('/update_athlete')
async def update_athlete(data:dict,user: Annotated[str, Depends(get_user)]):
    conn = sqlite3.connect('database.db')
    clefs = data.keys()
    c = conn.cursor()
    if 'first_name' in clefs:
        c.execute("UPDATE Athlete SET first_name=? WHERE id=?", (data['first_name'],data["id"],))
        conn.commit()
    if 'power_max' in clefs:
        c.execute("UPDATE Athlete SET power_max=? WHERE id=?", (data['heilast_naùeght'],data["id"],))
        conn.commit()
    if 'age' in clefs:
        c.execute("UPDATE Athlete SET age=? WHERE id=?", (data['age'],data["id"],))
        conn.commit()
    if 'height' in clefs:
        c.execute("UPDATE Athlete SET height=? WHERE id=?", (data['height'],data["id"],))
        conn.commit()
    if 'weight' in clefs:
        c.execute("UPDATE Athlete SET weight=? WHERE id=?", (data['weight'],data["id"],))
        conn.commit()
    conn.close()


@router.put('/update_performance')
async def update_performance(data:dict, user: Annotated[str, Depends(get_user)]):
    conn = sqlite3.connect('database.db')
    clefs = data.keys()
    c = conn.cursor()
    if 'athlete_id' in clefs:
        c.execute("UPDATE Performance SET athlete_id=? WHERE id=?", (data['athlete_id'],data["id"],))
        conn.commit()
    if 'power_max' in clefs:
        c.execute("UPDATE Performance SET power_max=? WHERE id=?", (data['power_max'],data["id"],))
        conn.commit()
    if 'hr_max' in clefs:
        c.execute("UPDATE Performance SET hr_max=? WHERE id=?", (data['hr_max'],data["id"],))
        conn.commit()
    if 'vo2_max' in clefs:
        c.execute("UPDATE Performance SET vo2_max=? WHERE id=?", (data['vo2_max'],data["id"],))
        conn.commit()
    if 'rf_max' in clefs:
        c.execute("UPDATE Performance SET rf_max=? WHERE id=?", (data['rf_max'],data["id"],))
        conn.commit()
    if 'cadence_max' in clefs:
        c.execute("UPDATE Performance SET cadence_max=? WHERE id=?", (data['cadence_max'],data["id"],))
        conn.commit()
    conn.close()