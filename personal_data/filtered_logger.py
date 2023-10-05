#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
import mysql.connector
import os
import re
from typing import List
import logging
PII_FIELDS = ("name", "email", "phone", "ssn", "credit_card")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating
    all fields in the log line (message)
    """
    for field in fields:
        pattern = rf'{re.escape(field)}=[^{re.escape(separator)}]+'
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Formatting of log messages before they are emitted """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Create logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to secure database"""
    db_username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    try:
        connection = mysql.connector.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            database=db_name
        )
        return connection
    except mysql.connector.Error as err:
        raise Exception(f"Error connecting to the database: {err}")
