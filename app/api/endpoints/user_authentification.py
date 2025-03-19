#inscription

#connexion
    #génération token

#ajout d'un athlète
    #dans base user
    #dans base athlete

from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.jwt_handler import create_access_token
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, pwd_context, get_password_hash
import sqlite3

router = APIRouter()

@router.post("/login")
async def login(data):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    requete = f"""SELECT username FROM users WHERE username = ?;"""
    c.execute(requete, (data['username']))
    result = c.fetchone()
    if not result or verify_password(data['password'], result['password']):
        raise HTTPException(status_code=401, detail='wrong login or password')
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": data['username'], 'role': result['role']}, expires_delta=access_token_expires
    )    
    return {"access_token": access_token, "token_type": "bearer"}

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