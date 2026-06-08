# --- OLD VERSION (commented out) ---
# This was the earlier approach where one variable was reused.
# First input was stored in userInput,
# then copied into stringEntered,
# then userInput was reused for a second input.

# userInput = input("Enter a word (string) :")
# stringEntered = userInput
# userInput = input("Enter a substring, like consecutive words in the last word: ")

# ------------------------------------------------------------

# Ask the user to enter the main string
theString = input("Enter a word: ")

# Ask the user to enter the substring to search for
theSubString = input("Enter a substring: ")


# Check if the substring exists anywhere inside the main string
if (theSubString in theString):

    # If it exists, tell the user
    print("The substring is in the string. The string does contain the substring")

    # Count how many times the substring appears
    howMany = theString.count(theSubString)
    print("It contains", howMany, "instance(s)")

    # Find the index of the first occurrence of the substring
    where = theString.find(theSubString)
    print("The first occurrence starts at", where, ".")

    # Check if the main string starts with the substring
    if (theString.startswith(theSubString)):
        print("The string starts with the substring")
    else:
        print("The string does not start with the substring.")

    # Check if the main string ends with the substring
    if theString.endswith(theSubString):
        print("The string ends with the substring.")
    else:
        print("The string does not end with the substring.")

# If the substring is not found at all
else:
    print("The string does not contain the substring.")
