#!/usr/bin/env python3
"""Basic - Base64 part"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class for basic authentication"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization
        header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header.

        Returns:
            str: The Base64 part of the Authorization header.
        """
        if authorization_header is None or\
                not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """Decodes a Base64 string and returns
        the decoded value as UTF-8 string.

        Args:
            base64_authorization_header (str): The Base64 string to decode.

        Returns:
            str: The decoded value as a UTF-8 string.
        """
        if base64_authorization_header is None or\
                not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_value = decoded_bytes.decode('utf-8')
            return decoded_value
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str) -> (str, str):
        """Extracts the user emailand password
                from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str): The Base64 decoded value.

        Returns:
            tuple: A tuple containing user email and user password.
        """
        if decoded_base64_authorization_header is None or\
                not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_password = decoded_base64_authorization_header.split(':', 1)
        return user_email, user_password
