
# 💥💥💥💥💥💥💥💥💥 1 💥💥💥💥💥💥💥💥💥

# PURPOSE:
# This program CREATES a text file called Presidents.txt
# and WRITES three presidents' names into that file.
#
# Think of it like opening TextEdit or Notepad,
# creating a new document, typing information,
# and saving it to your computer.
#
# IMPORTANT:
# "w" means WRITE mode.
# If the file doesn't exist, Python creates it.
# If the file already exists, Python ERASES its contents
# before writing new information.


def main():

    # ==========================================
    # (1) OPEN OR CREATE THE FILE
    # ==========================================

    outputFile = open("Movin_like_a_python/introduction to python programming and data structures: Liang/ch13_ALL/Presidents.txt", "w")

    # open() is a built-in Python function that opens a file.
    #
    # The first argument is the file's location (path).
    # The second argument, "w", specifies WRITE mode.
    #
    # outputFile is a variable that stores the file object.
    # We use this variable to interact with the file.
    #
    # At this point:
    # - Presidents.txt has been created if it didn't exist.
    # - Any previous contents have been erased.
    # - Nothing new has been written yet.
    #
    # The path is RELATIVE to Python's current working directory.
    # In your earlier setup, that was:
    # /Users/owner/Documents/coding/python


    # ==========================================
    # (2) WRITE INFORMATION INTO THE FILE
    # ==========================================

    outputFile.write("George Washington \n")

    # write() sends the string into Presidents.txt.
    #
    # "George Washington" is the information being stored.
    # \n means NEWLINE.
    # It moves the next text to a new line.
    #
    # Without \n, the names would run together.


    outputFile.write("John Adams \n")

    # Writes John Adams into the SAME file.
    # Python continues writing after the previous text.
    # \n moves the next name onto another line.


    outputFile.write("Thomas Jefferson \n")

    # Writes Thomas Jefferson into the SAME file.
    # \n adds a newline after his name.
    #
    # Notice:
    # Python does NOT create a new file for each write().
    # All three write() calls use the same opened file.


    # ==========================================
    # (3) CLOSE THE FILE
    # ==========================================

    outputFile.close()

    # close() closes the connection to the file.
    #
    # It also flushes any remaining buffered data,
    # helping ensure everything has been written.
    #
    # After closing, you cannot use outputFile.write()
    # again unless you reopen the file.


# ==========================================
# (4) RUN THE PROGRAM
# ==========================================

main()

# Calls the main() function.
# Without this call, Python defines main()
# but does not execute the instructions inside it.
