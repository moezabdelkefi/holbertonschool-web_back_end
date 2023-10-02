#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
import re
from typing import List


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
