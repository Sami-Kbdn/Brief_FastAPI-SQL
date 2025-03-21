import sqlite3
from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.db.transaction import get_user

router = APIRouter()

@router.put('/update_athlete')
async def update_athlete(data:dict,user: Annotated[str, Depends(get_user)]):
    """
    Endpoint for updating the details of an athlete in the database.

    This function allows updating various details of an athlete, such as:
    - First name
    - Maximum power (power_max)
    - Age
    - Height
    - Weight

    The function takes in a dictionary of data containing the athlete's ID and any attributes to be updated. 
    It checks which fields are provided and performs an update accordingly. Only the fields provided in the 
    request will be updated. After each update, the changes are committed to the database.

    Parameters:
    - data (dict): A dictionary containing the athlete's ID and the attributes to be updated.
        Example: {"id": 1, "first_name": "NewName", "weight": 70}
    - user (str): The authenticated username (provided by the `get_user` dependency).

    Returns:
    - str: A success message indicating the athlete's details have been updated.
    - str: An error message if there is an issue with the database or the update process.

    Raises:
    - sqlite3.Error: If there is an issue with the database during the update process.

    Example request:
    PUT /update_athlete
    Request body:
    {
        "id": 1,
        "first_name": "Updated Name",
        "weight": 75
    }

    Example response:
    "OK"
    """
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
    """
    Endpoint for updating the performance details of an athlete in the database.

    This function allows updating various performance metrics of an athlete, such as:
    - Athlete ID
    - Maximum power (power_max)
    - Maximum heart rate (hr_max)
    - VO2 max
    - Respiratory frequency (rf_max)
    - Maximum cadence (cadence_max)

    The function takes in a dictionary of data containing the performance record's ID and any attributes to be updated. 
    It checks which fields are provided and performs an update accordingly. Only the fields provided in the 
    request will be updated. After each update, the changes are committed to the database.

    Parameters:
    - data (dict): A dictionary containing the performance record's ID and the attributes to be updated.
        Example: {"id": 1, "power_max": 350, "hr_max": 190}
    - user (str): The authenticated username (provided by the `get_user` dependency).

    Returns:
    - str: A success message indicating the performance details have been updated.
    - str: An error message if there is an issue with the database or the update process.

    Raises:
    - sqlite3.Error: If there is an issue with the database during the update process.

    Example request:
    PUT /update_performance
    Request body:
    {
        "id": 1,
        "power_max": 350,
        "vo2_max": 55
    }

    Example response:
    "OK"
    """
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