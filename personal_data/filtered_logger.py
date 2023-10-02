#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    parts = message.split(separator)
    for i, part in enumerate(parts):
        key_value = part.split('=')
        if key_value[0] in fields:
            parts[i] = f"{key_value[0]}={redaction}"
    return separator.join(parts)
