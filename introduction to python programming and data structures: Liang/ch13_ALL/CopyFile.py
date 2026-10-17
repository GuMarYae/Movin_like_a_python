# 💥💥💥💥💥💥💥💥💥 4 💥💥💥💥💥💥💥💥💥 

# This program works similarly to right-clicking a file,
# selecting Copy, and then Paste on Mac or Windows.

# It opens an existing text file and reads its contents.
# It then creates a new file and copies the contents into it.

# Unlike Finder or File Explorer, this program is designed
# for text files, not binary files like images, videos, or Word documents.

# The original file remains unchanged.

import os.path  # Allows us to check if a file exists
import sys      # Allows us to stop the program using sys.exit()

def main():
    # strip() removes spaces accidently from the left side and the right side
    # (1) Ask the user to enter the names of two files
    f1 = input("Enter a source file: ").strip()       # Presidents.txt
    # f1 = the ORIGINAL file we want to copy FROM

    f2 = input("Enter a target file: ").strip()
    # f2 = the NEW file we want to copy TO            # PresidentsCopy.txt

    # strip() removes extra spaces at the beginning and end


    # (2) Check whether the target file already exists
    if os.path.isfile(f2):
        print(f2 + " already exists")
        sys.exit()  # Stops the program to prevent overwriting the file


    # (3) Open both files
    inputFile = open(f1, "r")   # "r" = READ from the original file
    outputFile = open(f2, "w")  # "w" = WRITE to the new file (creates it)


    # (4) Initialize two counters at zero
    countLines = 0  # Counts how many lines are copied
    countChars = 0  # Counts how many characters are copied


    # (5) Read and copy the file ONE LINE AT A TIME
    for line in inputFile:

        countLines += 1
        # Add 1 to the line counter for every line read

        countChars += len(line)
        # Count the characters in the current line
        # Includes spaces and newline characters (\n)

        outputFile.write(line)
        # Write the current line into the NEW file


    # (6) Display the total number of lines and characters
    print(countLines, "lines and", countChars, "chars copied")


    # (7) Close both files when finished
    inputFile.close()   # Close the original file
    outputFile.close()  # Close the new file


main()  # Call the main function to start the program

