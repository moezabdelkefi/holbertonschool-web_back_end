#!/usr/bin/env python3
"""create a emty class SessionAuth"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """class sessionauth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id.

        Args:
            user_id (str): The user ID.

        Returns:
            str: The generated Session ID or None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Get a User ID based on a Session ID.

        Args:
            session_id (str): The Session ID.

        Returns:
            str: The User ID associated with the Session ID or None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """
        Get a User instance based on a session cookie.
        Args:
            request: The Flask request object.

        Returns:
            User: The User instance or None if not found.
        """
        session_cookie_value = self.session_cookie(request)
        if session_cookie_value is None:
            return None

        user_id = self.user_id_for_session_id(session_cookie_value)
        if user_id is None:
            return None

        user = User.get(user_id)
        return user
