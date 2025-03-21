from fastapi import FastAPI
from app.api.endpoints import read, delete, update, create, user_authentification
from app.api.models import athlete, performance, user


app = FastAPI(title="Cyclist performances")

app.include_router(create.router, prefix="", tags=["Create"])
app.include_router(user_authentification.router, prefix="", tags=["Auth"])
app.include_router(read.router, prefix="", tags=["Read"])
app.include_router(delete.router, prefix="", tags=["Delete"])
app.include_router(update.router, prefix="", tags=["Update"])

athlete.create_athlete_db()
performance.create_performance_db()
user.create_user_db()