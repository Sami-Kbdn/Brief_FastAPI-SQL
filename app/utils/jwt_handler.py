from datetime import datetime, timedelta, timezone
import jwt
from app.core.config import SECRET_KEY, ALGORITHM

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Creates an access token using JWT (JSON Web Token) with a specified expiration time.

    This function generates a JWT token with the provided data and an expiration time.
    If no expiration is provided, the token will expire in 15 minutes by default.

    Args:
        data (dict): A dictionary containing the data to encode into the token. 
                      Typically, this would include user identification or roles.
        expires_delta (timedelta, optional): The duration after which the token should expire. 
                                              If not provided, defaults to 15 minutes.

    Returns:
        str: A JWT token as a string, encoded with the provided data and expiration time.

    Example:
        - create_access_token({"sub": "username"}, timedelta(hours=1))
        - create_access_token({"sub": "username"})
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """
    Verifies and decodes a JWT token to extract the payload.

    This function attempts to decode a given JWT token using the secret key and algorithm
    defined in the configuration. If the token is valid, it returns the decoded payload.
    If the token is invalid or expired, it returns `None`.

    Args:
        token (str): The JWT token to verify and decode.

    Returns:
        dict | None: The decoded payload from the token if valid, otherwise `None`.

    Example:
        - verify_token("valid_jwt_token")
        - verify_token("invalid_jwt_token") -> None
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None