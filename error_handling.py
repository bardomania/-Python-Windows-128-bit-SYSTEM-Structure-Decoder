#!/usr/bin/python

# Import
import typing

# Define
ENCODED_LEN = 32

def display_error(msg: str):
    print(msg)
    exit(code=0)

def is_hex(string: str):
    try:
        int(string, 16)
        return True
    except ValueError:
        display_error("Given argument is not hexadecimal")

def verify_len(args):
    if (len(args) != ENCODED_LEN):
        display_error("Given argument is not a Windows 128 bit SYSTEM Structure")
