#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join(map(re.escape, fields))
    return re.sub(pattern, redaction, message)
