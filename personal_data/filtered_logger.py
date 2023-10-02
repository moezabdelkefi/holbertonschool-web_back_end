#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    pattern = '|'.join(map(re.escape, fields))
    return re.sub(pattern, redaction, message)
