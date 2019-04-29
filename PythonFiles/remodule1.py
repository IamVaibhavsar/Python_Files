'''
regular expression module
RE (regex, regular expression)are powerful language for matching text patterns pattern
RE is used to identify whether a pattern exists in a given sequence(string) or not.
manipulates textual data which is required for data science.
server side: to validate username , email and passwords

'''

import re

pattern=r"cookie"       #raw string
sequence="cookie"

if re.match(pattern, sequence):
    print("match!")
else:
    print("print not found")

#match


