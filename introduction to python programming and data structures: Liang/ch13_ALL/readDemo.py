
# 💥💥💥💥💥💥💥💥💥 3 💥💥💥💥💥💥💥💥💥

# PURPOSE:
# This program opens an existing text file (Presidents.txt)
# and demonstrates FOUR different ways to read its contents.
#
# Think of it like opening a document in Notepad or TextEdit.
# You can read everything, a few characters, or individual lines.
#
# IMPORTANT:
# "r" means READ ONLY. Nothing gets erased or changed.


def main():

    # ==========================================
    # (1) read() - READ THE ENTIRE FILE
    # ==========================================

    inputFile = open("Presidents.txt", "r")
    # Opens Presidents.txt in READ mode.
    # inputFile is a variable referencing the opened file object.

    print("(1) Using read():")

    print(inputFile.read())
    # read() reads ALL characters from the file.
    # It returns the entire contents as ONE string.
    # print() displays that string in the terminal.

    inputFile.close()
    # Closes the file when finished reading.


    # ==========================================
    # (2) read(number) - READ SPECIFIC CHARACTERS
    # ==========================================

    inputFile = open("Presidents.txt", "r")
    # Reopens the file and starts reading from the beginning.
    # Python keeps track of your current reading position.
    # Reopening resets that position to the beginning.

    print("\n(2) Using read(number):")
    # \n creates a blank line in the terminal.

    s1 = inputFile.read(4)
    # Reads ONLY the first 4 characters.
    #
    # Example: "George Washington"
    # First 4 characters = "Geor"
    #
    # s1 now contains "Geor".

    print(s1)
    # Displays: Geor

    s2 = inputFile.read(15)
    # Reads the NEXT 15 characters.
    # It does NOT start over at the beginning!
    #
    # Python remembers that 4 characters were already read.
    # It continues reading from character 5.

    print(repr(s2))
    # repr() displays the string's representation.
    #
    # Unlike print(s2), repr(s2) shows:
    # - Quotation marks
    # - Special characters like \n
    #
    # Example: 'ge Washington\n'
    # This helps you SEE characters normally hidden.

    inputFile.close()
    # Closes the file.


    # ==========================================
    # (3) readline() - READ ONE LINE AT A TIME
    # ==========================================

    inputFile = open("Presidents.txt", "r")
    # Opens the file again, starting at the beginning.

    print("\n(3) Using readline():")

    line1 = inputFile.readline()
    # Reads the FIRST line, including its newline (\n).

    line2 = inputFile.readline()
    # Reads the SECOND line.

    line3 = inputFile.readline()
    # Reads the THIRD line.

    line4 = inputFile.readline()
    # Attempts to read the FOURTH line.
    #
    # If the file only contains 3 lines,
    # Python returns an empty string: ''

    print(repr(line1))
    # Example: 'George Washington\n'

    print(repr(line2))
    # Example: 'John Adams\n'

    print(repr(line3))
    # Example: 'Thomas Jefferson\n'

    print(repr(line4))
    # Example: ''
    # Empty means there is nothing left to read.

    inputFile.close()
    # Closes the file.


    # ==========================================
    # (4) readlines() - READ ALL LINES INTO A LIST
    # ==========================================

    inputFile = open("Presidents.txt", "r")
    # Opens the file again from the beginning.

    print("\n(4) Using readlines():")

    print(inputFile.readlines())
    # readlines() reads EVERY line in the file.
    #
    # Unlike read(), it returns a LIST of strings.
    #
    # Example:
    # ['George Washington\n',
    #  'John Adams\n',
    #  'Thomas Jefferson\n']
    #
    # Each line becomes a separate element in the list.
    #
    # Index 0 = George Washington
    # Index 1 = John Adams
    # Index 2 = Thomas Jefferson

    inputFile.close()
    # Closes the file.


main()
# Calls main() to execute the program.
