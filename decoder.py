#!/usr/bin/python

# Import
from calendar import weekday
import sys
from unicodedata import decimal
import datetime

# Local import
from error_handling import is_hex, display_error, verify_len

# Get all arguments and concatenated them
args = ''.join(sys.argv[1:])

#Verify len of argument
verify_len(args)

# Verify if all groups are hexadecimal
is_hex(args)

# Divided the string into groups of four
args = [args[i: i+2] for i in range(0, len(args), 2)]

# Convert to little indian
for i in range(0, len(args) - 1, 2):
    args[i], args[i+1] = args[i+1], args[i]

args = ''.join(args)
args = [args[i: i+4] for i in range(0, len(args), 4)]

# Translate hexa to decimal
decimal = []
for i in args:
    decimal.append(int(i, 16))

# Nice formatage
result = datetime.datetime(year=decimal[0], month=decimal[1], day=decimal[3], hour=decimal[4], minute=decimal[5], \
    second=decimal[6], microsecond=(decimal[7] * 1000))
print(result.strftime("%A %B %d, %Y at %H:%M:%S.%f")[:-3])