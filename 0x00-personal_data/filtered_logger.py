#!/usr/bin/env python3
"""
a function called filter_datum that returns the log message obfuscated
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all
    fields in the log line (message)
    """
    pattern = r'({})'.format('|'.join(fields))
    return re.sub(pattern, redaction, message, flags=re.IGNORECASE)
