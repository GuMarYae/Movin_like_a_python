
# 💥 13.8 - CountEachLetterURL.py

# PURPOSE:
# This program retrieves text from a website and counts
# how many times each letter (A-Z) appears.
#
# Think of it like JavaScript's fetch().
# Instead of reading a file from your computer,
# Python retrieves information from the Internet.
#
# MAIN CONCEPTS:
# 1. Retrieve data from a URL.
# 2. Convert the retrieved bytes into a string.
# 3. Count how many times each letter appears.
# 4. Display the results.


import urllib.request
# Imports Python's tools for retrieving data from URLs.


def main():

    # (1) ASK THE USER FOR A WEBSITE ADDRESS

    url = input("Enter a URL for a file: ").strip()
    # input() asks the user to enter a URL.
    # Example: https://www.python.org
    # strip() removes unwanted whitespace from both ends.


    # (2) OPEN THE WEBSITE

    infile = urllib.request.urlopen(url)
    # urlopen() sends a request to the URL.
    # Returns a response object that we can read.
    # Similar in purpose to JavaScript's fetch().


    # (3) READ THE WEBSITE'S CONTENTS

    s = infile.read().decode()
    # read() retrieves the website's contents as BYTES.
    # decode() converts those bytes into a STRING.
    # s now contains the retrieved text (possibly HTML).


    # (4) COUNT THE LETTERS

    counts = countLetters(s.lower())
    # lower() converts uppercase letters into lowercase.
    # Example: "HeLLo" becomes "hello".
    #
    # countLetters() is our custom function defined below.
    # We pass the lowercase string into that function.
    #
    # The function returns a list containing 26 numbers.
    # Each number represents how many times a letter appeared.
    #
    # counts[0] = number of A's
    # counts[1] = number of B's
    # counts[2] = number of C's
    # ...
    # counts[25] = number of Z's


    # (5) DISPLAY THE RESULTS

    for i in range(len(counts)):
        # len(counts) returns 26.
        # range(26) generates numbers from 0 to 25.
        # The loop checks each letter's count.

        if counts[i] != 0:
            # != means NOT EQUAL.
            # Only display letters that appeared at least once.

            print(chr(ord('a') + i) + " appears " + str(counts[i])
                  + (" time" if counts[i] == 1 else " times"))

            # ord('a') returns 97, the Unicode value of 'a'.
            # Adding i moves through the alphabet.
            #
            # Example:
            # i = 0 -> 97 -> a
            # i = 1 -> 98 -> b
            # i = 2 -> 99 -> c
            #
            # chr() converts the number back into a letter.
            #
            # str(counts[i]) converts the count into a string
            # so it can be combined with the other text.
            #
            # (" time" if counts[i] == 1 else " times")
            # is a conditional expression.
            #
            # If the count is 1, display "time".
            # Otherwise, display "times".


    infile.close()
    # Closes the response after we're finished reading.


# ==========================================
# (6) FUNCTION THAT ACTUALLY COUNTS THE LETTERS
# ==========================================

def countLetters(s):
    # s is the string passed from main().
    # This function examines every character in that string.

    counts = 26 * [0]
    # Creates a list containing 26 zeros.
    # Each position represents a letter from A to Z.
    #
    # Example:
    # [0, 0, 0, 0, ...]
    #
    # All counts start at zero.


    for ch in s:
        # Loops through EVERY character in the string.
        # ch represents the current character.
        #
        # Example: "cat"
        # First loop:  ch = 'c'
        # Second loop: ch = 'a'
        # Third loop:  ch = 't'


        if 'a' <= ch <= 'z':
            # Checks whether the character is a lowercase
            # English letter between a and z.
            # Ignores numbers, spaces, punctuation, etc.

            counts[ord(ch) - ord('a')] += 1
            # ord(ch) converts the current letter into a number.
            #
            # Example:
            # ord('a') = 97
            # ord('b') = 98
            # ord('c') = 99
            #
            # Subtracting ord('a') gives the list index.
            #
            # 'a': 97 - 97 = 0 -> counts[0]
            # 'b': 98 - 97 = 1 -> counts[1]
            # 'c': 99 - 97 = 2 -> counts[2]
            #
            # += 1 increases that letter's count by one.


    return counts
    # Sends the completed list back to main().
    # This is the value stored in:
    # counts = countLetters(s.lower())


main()
# Starts the program by calling main().
# countLetters() only runs when main() calls it.


# ==========================================
# BIGGEST LESSON
# ==========================================
#
# URL -> REQUEST -> BYTES -> STRING -> COUNT -> DISPLAY
#
# 1. Get the website address.
# 2. Retrieve its contents.
# 3. Convert the data into readable text.
# 4. Examine each character.
# 5. Count the occurrences of each letter.
# 6. Display the results.
#
# This combines web requests, functions, loops,
# strings, lists, indexing, and return values.
