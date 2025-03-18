





from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwt_handler import verify_token
from typing import Annotated
from jwt import decode
from jwt.exceptions import InvalidTokenError
from app.schemas.auth import TokenData
from app.db.transactions import get_user
from app.core.config import SECRET_KEY, ALGORITHM
import sqlite3

router = APIRouter()

@router.get("/loans/history")
async def prediction_history(user: Annotated[User, Depends(get_current_active_user)],user_id: Annotated[User, Depends(get_current_user_id)], session : Annotated[Session, Depends(get_session)]):
    if user.role != 0:
        prediction_list = session.exec(select(Loan_Request)).all()
    else:
        prediction_list = session.exec(select(Loan_Request).where(Loan_Request.user_id == user_id)).all()
    return prediction_list


conn = sqlite3.connect('utilisateurs.db') # Connexion à la base de données
cursor = conn.cursor() # Création d'un curseur

requete = f"""SELECT nom, email FROM utilisateurs WHERE nom = ?;""" # Requête SQL à executer
cursor.execute(requete, ("Bob",)) # exécution de la requête

resultat = cursor.fetchall() # Récupération de tous les résultats dans une liste

print(resultat) # Affichage des résultats
conn.close() # Fermeture de la connexion