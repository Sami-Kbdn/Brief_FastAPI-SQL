#nouvelle perf

from fastapi import FastAPI
import sqlite3


app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.post('/insert_athlete')
async def insert_athlete(data:dict):
    conn = sqlite3.connect('database.db')

    c = conn.cursor()
    try :
        c.execute(f"INSERT INTO Athlete ('first_name', 'last_name', 'weight', 'age', 'height' ) VALUES (?, ?, ?, ?, ?)", (data["first_name"], data['last_name'], data['weight'], data['height'], data['age']))
        conn.commit()
        return "OK"
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()