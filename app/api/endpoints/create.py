import sqlite3
from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.db.transaction import get_user


router = APIRouter()

@router.post('/insert_athlete')
async def insert_athlete(data:dict, user: Annotated[str, Depends(get_user)]):
    """
    Endpoint for inserting a new athlete into the database. This function requires the user to be authenticated and have 
    an admin role (role = 1) in order to insert the athlete's data. If the user does not have sufficient privileges, 
    an "Access denied" message is returned.

    Arguments:
    - data (dict): The request body should contain a dictionary with the following fields:
        - "first_name" : The first name of the athlete.
        - "last_name" : The last name of the athlete.
        - "weight" : The weight of the athlete (in kg).
        - "age" : The age of the athlete.
        - "height" : The height of the athlete (in cm).
    - user (str): The username of the currently authenticated user (extracted from the JWT token). This is used to check the user's role.

    Returns:
    - str: A message indicating the status of the operation:
        - "OK" if the athlete is successfully inserted.
        - Error message if an exception occurs during insertion.
        - "Access denied" if the user does not have the necessary privileges.

    Raises:
    - sqlite3.Error: If there is an issue with the database during insertion.

    Example request:
    POST /insert_athlete
    {
        "first_name": "John",
        "last_name": "Doe",
        "weight": 70,
        "age": 25,
        "height": 180
    }

    Example response (for successful insertion):
    {
        "message": "OK"
    }

    Example response (for access denied):
    {
        "message": "Access denied"
    }
    """
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
async def insert_performance(data:dict, user: Annotated[str, Depends(get_user)]):
    """
    Endpoint for inserting a new performance record into the database. This function allows inserting performance data 
    for a specific athlete, including metrics such as maximum power, heart rate, VO2 max, respiratory factor, and cadence.

    Arguments:
    - data (dict): The request body should contain a dictionary with the following fields:
        - "athlete_id" : The ID of the athlete associated with the performance record.
        - "power_max" : The maximum power output of the athlete (in watts).
        - "hr_max" : The maximum heart rate of the athlete (in bpm).
        - "vo2_max" : The maximum VO2 (in ml/kg/min) achieved by the athlete.
        - "rf_max" : The maximum respiratory factor of the athlete.
        - "cadence_max" : The maximum cadence (in rpm) achieved by the athlete.
    - user (str): The username of the currently authenticated user (extracted from the JWT token). This is used to verify the user's identity.

    Returns:
    - str: A message indicating the status of the operation:
        - "OK" if the performance data is successfully inserted.
        - Error message if an exception occurs during insertion.

    Raises:
    - sqlite3.Error: If there is an issue with the database during the insertion of the performance data.

    Example request:
    POST /insert_performance
    {
        "athlete_id": 1,
        "power_max": 350,
        "hr_max": 180,
        "vo2_max": 60,
        "rf_max": 1.5,
        "cadence_max": 95
    }

    Example response (for successful insertion):
    {
        "message": "OK"
    }
    """
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
