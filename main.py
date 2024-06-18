import os, sys, io, contextlib

# Steps:
# 1. Setup basic stdin → stdout pipes 
#    - I/O from prompt
#    - from file arg
#    - through pipes
# 2. SQLite setup (tables, columns)
#    - Function that puts to SQLite
#    - Function that gets from SQLite
# 3. Create a function that logs to stdout or to a file

