import sqlite3
from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.db.transaction import get_user


router = APIRouter()

@router.delete('/delete_athlete')
async def delete_athlete(data:dict, user: Annotated[str, Depends(get_user)]):
    """
    Endpoint for deleting an athlete record from the database, including their associated performance data. 
    This function removes the athlete's information from the 'Athlete' table and all related performance data 
    from the 'Performance' table.

    Arguments:
    - data (dict): The request body should contain a dictionary with the following field:
        - "id" : The ID of the athlete to be deleted.
    - user (str): The username of the currently authenticated user (extracted from the JWT token). This is used to verify the user's identity.

    Returns:
    - str: A message indicating the status of the operation:
        - "OK" if the athlete and their performance records are successfully deleted.
        - Error message if an exception occurs during deletion.

    Raises:
    - sqlite3.Error: If there is an issue with the database during the deletion process.

    Example request:
    DELETE /delete_athlete
    {
        "id": 1
    }

    Example response (for successful deletion):
    {
        "message": "OK"
    }
    """
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
    """
    Endpoint for deleting performance data associated with an athlete. 
    This function removes the performance records for a specific athlete from the 'Performance' table 
    based on the athlete's ID.

    Arguments:
    - data (dict): The request body should contain a dictionary with the following field:
        - "id" : The ID of the athlete whose performance data is to be deleted.
    - user (str): The username of the currently authenticated user (extracted from the JWT token). This is used to verify the user's identity.

    Returns:
    - str: A message indicating the status of the operation:
        - "OK" if the athlete's performance data is successfully deleted.
        - Error message if an exception occurs during deletion.

    Raises:
    - sqlite3.Error: If there is an issue with the database during the deletion process.

    Example request:
    DELETE /delete_performance
    {
        "id": 1
    }

    Example response (for successful deletion):
    {
        "message": "OK"
    }
    """
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