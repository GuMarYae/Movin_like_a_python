# 💥💥💥💥💥💥💥💥💥 2 💥💥💥💥💥💥💥💥💥

# PURPOSE:
# Checks if Presidents.txt (created by WriteDemo.py) exists.
# Does NOT create, read, modify, or delete the file.

import os.path  # Imports tools for working with file paths

name = "Gu"  # Stores "Gu" in the variable name

# os.path.isfile() checks whether Presidents.txt exists
# Returns True (1) if the file exists, or False (0) if it doesn't
# == 1 checks whether the result equals 1 (True)
# Python checks the current working directory for the file

if os.path.isfile("Presidents.txt") == 1 :
    print("This shyt exists", name)  # Runs if the file exists

else:
    print("Cant find that joint, bro")  # Runs if the file doesn't exist