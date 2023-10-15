import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ hash password using password hashing algorithm """
    # Generate a random salt
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def _generate_uuid() -> str:
    """ Generates a unique identifier
    for the given password string"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the a
    uthentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Call the standalone function
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Returns True if the given email
        and password are valid for
        the given user account and password combination
        combination combination"""
        try:
            user = self._db.find_user_by(email=email)
            # Check if the provided password matches the stored hashed password
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Create a session from an email address"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        try:
            if session_id:
                user = self._db.find_user_by(session_id=session_id)
                return user
        except NoResultFound:
            return None
