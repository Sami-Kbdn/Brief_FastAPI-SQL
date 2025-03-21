import sqlite3
from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.db.transaction import get_user

router = APIRouter()

@router.get('/all_athletes')
async def all_athletes(user: Annotated[str, Depends(get_user)]):
    """
    Fetches all athletes from the database and returns them as a list of dictionaries.

    This endpoint queries the 'Athlete' table in the SQLite database, retrieves all rows, and
    formats the data into a list of dictionaries where each dictionary corresponds to an athlete
    with column names as keys. The response will contain a list of all athletes or an error message
    in case of a failure.

    Args:
        user (str): The user making the request. The value is fetched via dependency injection 
                    using the `get_user` function.

    Returns:
        dict: A JSON response containing either:
            - A list of athletes in the form of dictionaries with column names as keys, or
            - An error message in case of an exception during the database query.
    
    Raises:
        sqlite3.Error: If there is an error during the database query execution.
    """
    print("#############################")
    conn = sqlite3.connect('database.db')

    c = conn.cursor()
    try:
        c.execute("SELECT * FROM Athlete")
        columns = [desc[0] for desc in c.description]  # Récupère les noms des colonnes
        rows = c.fetchall()
        athletes = [dict(zip(columns, row)) for row in rows] 
        return {"athletes": athletes}
    except sqlite3.Error as error:
        return {"error": str(error)}
    finally:
        conn.close()




@router.get('/max_vo')
async def max_power(user: Annotated[str, Depends(get_user)]):
    """
    Endpoint for retrieving the athlete with the highest VO2 max value.

    This function queries the database to find the athlete who has the highest VO2 max value,
    by performing an inner join between the 'Athlete' and 'Performance' tables.
    It then returns the first name of the athlete with the highest VO2 max value.

    Arguments:
    - user (str): The username of the currently authenticated user (extracted from the JWT token). 
      This is used to verify the user's identity and ensure that the request is authorized.

    Returns:
    - dict: A dictionary containing the first name of the athlete with the highest VO2 max value. 
      Example: {"first_name": "Athlete Name"}
    - str: An error message in case of a database issue.

    Raises:
    - sqlite3.Error: If there is an issue with the database during the query process.

    Example request:
    GET /max_vo

    Example response:
    {"first_name": "Athlete1"}
    """
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    try :
        c.execute(f"""SELECT 
                Athlete.first_name
            FROM 
                Athlete
            INNER JOIN 
                Performance
                ON Athlete.id = Performance.athlete_id
            GROUP BY
                  Athlete.id
            HAVING 
                Performance.vo2_max =MAX(Performance.vo2_max);""")
        result = c.fetchone()
        return result
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()


@router.get('/max_power_weight_ratio')
async def max_power():
    """
    Endpoint for retrieving the athlete with the highest power-to-weight ratio.

    This function calculates the ratio of an athlete's weight to their maximum power output
    (i.e., power_max) and retrieves the athlete with the highest ratio. The ratio is calculated
    as the weight divided by the maximum power value. The result is ordered in descending order
    and limited to the top athlete.

    The function joins the 'Athlete' and 'Performance' tables based on athlete ID and performs
    the necessary calculations to find the athlete with the highest power-to-weight ratio.

    Returns:
    - list: A list containing the first name, weight, and power_max of the athlete with the highest
      power-to-weight ratio along with the calculated ratio. 
      Example: [{"first_name": "Athlete Name", "weight": 70, "power_max": 400, "rapport poids/puissance": 0.175}]
    - str: An error message if there is an issue with the database during the query process.

    Raises:
    - sqlite3.Error: If there is an issue with the database during the query process.

    Example request:
    GET /max_power_weight_ratio

    Example response:
    [{"first_name": "Athlete1", "weight": 70, "power_max": 400, "rapport poids/puissance": 0.175}]
    """
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    try :
        c.execute("""
SELECT first_name, weight, power_max, 
       a.weight / CAST(p.power_max AS FLOAT) AS "rapport poids/puissance"
FROM Athlete a
INNER JOIN Performance p ON a.id = p.athlete_id
ORDER BY 4 desc
LIMIT 1;
""")
        result = c.fetchall()
        return result
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()

    
@router.get('/max_avg_power')
async def max_power():
    """
    Endpoint for retrieving the athlete with the highest average maximum power.

    This function calculates the average of an athlete's maximum power output (i.e., power_max) 
    and retrieves the athlete with the highest average power. The result is ordered in descending 
    order and limited to the top athlete.

    The function joins the 'Athlete' and 'Performance' tables based on athlete ID, calculates 
    the average of the 'power_max' for each athlete, and finds the athlete with the highest average.

    Returns:
    - list: A list containing the first name of the athlete and their calculated average maximum 
      power (Puissance moyenne max).
      Example: [{"first_name": "Athlete Name", "Puissance moyenne max": 350}]
    - str: An error message if there is an issue with the database during the query process.

    Raises:
    - sqlite3.Error: If there is an issue with the database during the query process.

    Example request:
    GET /max_avg_power

    Example response:
    [{"first_name": "Athlete1", "Puissance moyenne max": 350}]
    """
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    try :
        c.execute("""
SELECT first_name, avg(power_max) as "Puissance moyenne max"
FROM Athlete a
INNER JOIN Performance p ON a.id = p.athlete_id
GROUP BY a.id
ORDER BY 2 desc
LIMIT 1;
""")
        result = c.fetchall()
        return result
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()