from fastapi import APIRouter, HTTPException
from app.utils.jwt_handler import create_access_token
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from app.core.security import verify_password, get_password_hash
import sqlite3


router = APIRouter()

@router.post("/login")
async def login(data : dict):
    """
    Endpoint for user login. This function allows a user to authenticate by providing their username and password. 
    If the provided credentials are correct, a JWT access token is generated and returned for further API access.

    Arguments:
    - data (dict): The request body should contain a dictionary with the following fields:
        - "username" : The username of the user trying to log in.
        - "password" : The password of the user.

    Returns:
    - dict: A dictionary containing the following fields:
        - "access_token" : The JWT access token generated for the authenticated user.
        - "token_type" : The type of token, which is always "bearer".

    Raises:
    - HTTPException: If the login is unsuccessful (wrong username or password), a 401 Unauthorized error is raised.

    Example request:
    POST /login
    {
        "username": "john_doe",
        "password": "password123"
    }

    Example response:
    {
        "access_token": "<JWT_TOKEN>",
        "token_type": "bearer"
    }
    """
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    requete = f"""SELECT * FROM User WHERE username = ?;"""
    c.execute(requete, (data['username'],))
    result = c.fetchone()
    result = dict(result)
    if not result or not verify_password(data['password'], result['password']):
        raise HTTPException(status_code=401, detail='wrong login or password')
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": data["username"]}, expires_delta=access_token_expires
    )    
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register") 
def register(data: dict):
    """
    Endpoint for user registration. This function allows a new user to be registered by providing a username, password, 
    and role. The password is hashed before storing it in the database. If the username already exists, a 400 error is raised.

    Arguments:
    - data (dict): The request body should contain a dictionary with the following fields:
        - "username" : The username of the user to be registered.
        - "password" : The password of the user to be registered.
        - "role" : The role of the user (integer value).

    Returns:
    - dict: A dictionary containing the following field:
        - "message" : A success message indicating that the user has been created.

    Raises:
    - HTTPException: If the username already exists, a 400 Bad Request error is raised with the detail "User already exists".

    Example request:
    POST /register
    {
        "username": "john_doe",
        "password": "password123",
        "role": 1
    }

    Example response:
    {
        "message": "User created"
    }
    """
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