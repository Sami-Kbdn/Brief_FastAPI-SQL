import jwt
from app.core.config import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

def get_user(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return (payload["sub"])

