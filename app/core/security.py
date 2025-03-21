from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """
    Verifies if a plain password matches the given hashed password.

    This function uses the `bcrypt` hashing algorithm (from the passlib library) to compare
    the plain text password provided by the user with a previously stored hashed password.

    Args:
        plain_password (str): The plain text password provided by the user.
        hashed_password (str): The stored hashed password to compare against.

    Returns:
        bool: True if the plain password matches the hashed password, False otherwise.
    
    Example:
        - verify_password("my_secret_password", "$2b$12$5iK...") -> True
        - verify_password("wrong_password", "$2b$12$5iK...") -> False
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """
    Hashes a plain password using the bcrypt algorithm.

    This function uses the `bcrypt` hashing algorithm (from the passlib library) to securely
    hash a plain text password. The resulting hash can be stored in the database for later
    comparison during login attempts.

    Args:
        password (str): The plain text password to be hashed.

    Returns:
        str: The hashed version of the provided password.
    
    Example:
        - get_password_hash("my_secret_password") -> "$2b$12$5iK..."
    """
    return pwd_context.hash(password)