from fastapi import FastAPI
import sqlite3
from app.api.endpoints import user_authentification
from app.api.endpoints import create
from app.api.endpoints import read


app = FastAPI()

app.include_router(create.router, prefix="")
app.include_router(user_authentification.router, prefix="")
app.include_router(read.router, prefix="")
    
