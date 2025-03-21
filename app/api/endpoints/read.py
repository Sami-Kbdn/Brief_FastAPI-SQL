import sqlite3
from fastapi import APIRouter

router = APIRouter()

@router.get('/all_athletes')
async def all_athletes():
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
async def max_power():
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