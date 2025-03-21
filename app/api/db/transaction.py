import jwt
from app.core.config import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

def get_user(token):
    """
    Retrieves the username (subject) from a JWT token.

    This function decodes the provided JWT token using the secret key and the specified algorithm.
    It extracts the 'sub' field from the payload, which is assumed to be the username or user identifier.
    The 'sub' field is typically included in the token during the authentication process, and it uniquely identifies the user.

    Parameters:
    - token (str): The JWT token that is passed to the function, which contains the user's authentication details.

    Returns:
    - str: The username or user identifier (the value stored in the 'sub' field of the JWT payload).

    Raises:
    - jwt.DecodeError: If the token is invalid or cannot be decoded.
    - jwt.ExpiredSignatureError: If the token has expired.
    - jwt.InvalidTokenError: For other types of JWT-related errors.

    Example:
    - If the token contains a payload like: {"sub": "john_doe", ...}, the function will return "john_doe".
    """
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return (payload["sub"])

