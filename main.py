from fastapi import FastAPI
from app.api.endpoints.test import insert
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


@app.post('/insert_performance')
async def insert_athlete(data:dict):
    conn = sqlite3.connect('database.db')

    c = conn.cursor()
    try :
        c.execute(f"INSERT INTO Performances ('athlete_id', 'power_max', 'hr_max', 'vo2_max', 'rf_max', 'cadence_max' ) VALUES (?, ?, ?, ?, ?)", (data["athlete_id"], data['power_max'], data['hr_max'], data['vo2_max'], data['rf_max'], data['cadence_max']))
        conn.commit()
        return "OK"
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()

    
@app.get('/all_athletes')
async def all_athletes():
    conn = sqlite3.connect('database.db')

    c = conn.cursor()
    try :
        c.execute("SELECT * FROM Athlete")
        result = c.fetchall()
        return result
    except sqlite3.Error as error:
        return str(error)
    finally:
        conn.close()


from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.jwt_handler import create_access_token
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, pwd_context, get_password_hash
import sqlite3

router = APIRouter()
@router.post("/register") 
def register(data: dict):
    print(data)
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    hashed_password = get_password_hash(data["password"])
    try:
        c.execute("INSERT INTO User (username, password, role) VALUES (?, ?, ?)",
                     (data["username"], hashed_password, data["role"]))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists")
    finally:
        conn.close()
    return {"message": "User created"}