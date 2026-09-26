
# PYTHON BUILT-IN FUNCTIONS, METHODS, AND KEYWORDS CHEAT SHEET

# ============================================================

# BUILT-IN FUNCTIONS

# ============================================================

# These are functions Python already gives you.

# They DO NOT need an object with a dot.

print()      # Prints output
input()      # Gets user input

int()        # Converts to integer
float()      # Converts to floating-point number
str()        # Converts to string
list()       # Creates or converts to a list
tuple()      # Creates or converts to a tuple
set()        # Creates or converts to a set
dict()       # Creates or converts to a dictionary
bool()       # Converts to True or False

len()        # Returns number of items
sum()        # Adds numeric items
min()        # Returns smallest item
max()        # Returns largest item
sorted()     # Returns a sorted copy
round()      # Rounds a number
abs()        # Returns absolute value
pow()        # Raises a number to a power

range()      # Generates a sequence of numbers
enumerate()  # Gives index and value while looping
zip()        # Combines iterables

type()       # Shows data type
isinstance() # Checks an object's type

open()       # Opens a file
help()       # Shows help information

# ============================================================

# LIST METHODS

# ============================================================

# These belong to LIST objects.

# The DOT is the giveaway that these are methods.

list1.append(x)       # Add one item to the end
list1.extend(items)   # Add multiple items
list1.insert(i, x)    # Insert item at an index

list1.remove(x)       # Remove first matching value
list1.pop()           # Remove and return last item
list1.pop(i)          # Remove and return item at index
list1.clear()         # Remove everything

list1.index(x)        # Find index of a value
list1.count(x)        # Count occurrences

list1.sort()          # Sort the list
list1.reverse()       # Reverse the list
list1.copy()          # Make a copy

# ============================================================

# STRING METHODS

# ============================================================

s.split()             # Split string into a list
s.strip()             # Remove spaces from beginning/end
s.lower()             # Convert to lowercase
s.upper()             # Convert to uppercase
s.capitalize()        # Capitalize first character
s.title()             # Capitalize each word

s.replace(a, b)       # Replace text
s.find(x)             # Find position of text
s.index(x)            # Find index of text
s.count(x)            # Count occurrences

s.startswith(x)       # Check beginning
s.endswith(x)         # Check ending

s.isdigit()           # Check if characters are digits
s.isalpha()           # Check if characters are letters
s.isalnum()           # Check if letters/numbers
s.isspace()           # Check if whitespace

# ============================================================

# DICTIONARY METHODS

# ============================================================

d.keys()              # Get all keys
d.values()            # Get all values
d.items()             # Get key/value pairs

d.get(key)            # Get a value
d.update(other)       # Add/update entries
d.pop(key)            # Remove a key
d.popitem()           # Remove last inserted pair
d.clear()             # Remove everything
d.copy()              # Copy dictionary

# ============================================================

# SET METHODS

# ============================================================

s.add(x)              # Add an item
s.remove(x)           # Remove an item
s.discard(x)          # Remove item safely
s.pop()               # Remove an item
s.clear()             # Remove everything

s.union(other)        # Combine sets
s.intersection(other) # Get common items
s.difference(other)   # Get different items
s.issubset(other)     # Check if subset
s.issuperset(other)   # Check if superset

# ============================================================

# COMMON PYTHON KEYWORDS

# ============================================================

if
elif
else

for
while

def
return

class

try
except
finally
raise

import
from
as

and
or
not

in
is

True
False
None

break
continue
pass

with
lambda
yield

global
nonlocal

del
assert

async
await

# ============================================================

# FUNCTION VS METHOD

# ============================================================

# FUNCTION:

# Stands by itself.

sum(numbers)
len(numbers)
print(numbers)
list("abcd")

# METHOD:

# Belongs to an object and uses a DOT.

numbers.append(5)
numbers.index(5)

word.split()
word.upper()

# EASY RULE:

function(object)

object.method()

# ============================================================

# list("abcd") EXAMPLE

# ============================================================

word = "abcd"

letters = list(word)

print(letters)

# OUTPUT:

['a', 'b', 'c', 'd']

# list() is a BUILT-IN FUNCTION.

# ============================================================

# index() EXAMPLE

# ============================================================

list1 = [10, 20, 5, 30]

position = list1.index(5)

print(position)

# OUTPUT:

2

# Because:

# VALUE:  10  20   5  30

# INDEX:   0   1   2   3

# index() is a BUILT-IN LIST METHOD.

# ============================================================

# sum() EXAMPLE

# ============================================================

numbers = [1, 2, 3]

total = sum(numbers)

print(total)

# OUTPUT:

6

# sum() is a BUILT-IN FUNCTION.

# ============================================================

# split() EXAMPLE

# ============================================================

s = "1 2 3"

numbers = s.split()

print(numbers)

# OUTPUT:

['1', '2', '3']

# split() is a BUILT-IN STRING METHOD.

# ============================================================

# append() EXAMPLE

# ============================================================

numbers = []

numbers.append(5)
numbers.append(10)

print(numbers)

# OUTPUT:

[5, 10]

# append() is a BUILT-IN LIST METHOD.

# ============================================================

# MATRIX EXAMPLE

# ============================================================

matrix = []

numberOfRows = int(input("Enter the amount of rows: "))

# If 5 is entered:

# range(5) represents:

# 0, 1, 2, 3, 4

for row in range(numberOfRows):

    # str(row) converts the row number into a string
    # so it can be concatenated with the rest of the string.

    s = input("Enter the numbers for row index " + str(row) + ": ")

    # Example:
    #
    # User enters:
    # 1 2 3
    #
    # s is originally:
    # "1 2 3"
    #
    # s.split() creates:
    # ["1", "2", "3"]
    #
    # float(x) converts each value:
    # [1.0, 2.0, 3.0]
    #
    # append() adds that entire row to matrix.

    matrix.append([float(x) for x in s.split()])

print(matrix)

# ============================================================

# LONG VERSION OF LIST COMPREHENSION

# ============================================================

# SHORT VERSION:

matrix.append([float(x) for x in s.split()])

# LONG VERSION:

numbers = []

for x in s.split():

    numbers.append(float(x))

matrix.append(numbers)

# So:

[float(x) for x in s.split()]

# basically means:

numbers = []

for x in s.split():

    numbers.append(float(x))

# ============================================================

# TWO-DIMENSIONAL LIST

# ============================================================

matrix = [

    [1.0, 2.0, 3.0],

    [4.0, 5.0, 6.0],

    [7.0, 8.0, 9.0]

]

# A 2D list is basically:

# A LIST containing other LISTS.

# ============================================================

# ACCUMULATE EXAMPLE

# ============================================================

def accumulate(m):

    total = 0  # Start total at 0

    # Go through each row in the matrix.

    for row in m:

        # sum(row) is a built-in FUNCTION.
        # It adds all the numbers in the current row.
        #
        # Then += adds that amount to total.

        total += sum(row)

    # Return the final total.

    return total

# ============================================================

# COMPLETE MATRIX PROGRAM

# ============================================================

def getMatrix():

    matrix = []  # Empty list that will hold all rows

    numberOfRows = int(input("Enter the amount of rows: "))

    # If 5 was entered:
    # row will be 0, 1, 2, 3, 4.

    for row in range(numberOfRows):

        # str(row) converts the row index into a string
        # so we can concatenate it with the message.

        s = input("Enter the numbers for row index " + str(row) + ": ")

        # Split the input.
        # Convert each value to float.
        # Create a list.
        # Append that list to matrix.

        matrix.append([float(x) for x in s.split()])

    # Return the completed 2D list.

    return matrix

def accumulate(m):

    total = 0

    # Loop through every row.

    for row in m:

        # Add all numbers in the current row
        # to the running total.

        total += sum(row)

    return total

def main():

    # getMatrix() returns the 2D list.
    # m stores that returned list.

    m = getMatrix()

    # Print the 2D list.

    print(m)

    # Pass the 2D list into accumulate().
    # accumulate() returns the total.

    total = accumulate(m)

    # Print the total.

    print(total)

main()

# ============================================================

# IMPORTANT NAMING WARNING

# ============================================================

# DON'T DO THIS:

list = []

sum = 10

str = "hello"

# Those names already belong to Python built-in functions.

# You would hide/overwrite access to those built-ins.

# DO THIS INSTEAD:

numbers = []

total = 10

word = "hello"

# ============================================================

# QUICK MEMORY RULE

# ============================================================

# BUILT-IN FUNCTION:

sum(numbers)

# function(object)

# BUILT-IN METHOD:

numbers.append(5)

# object.method()

# KEYWORD:

for
if
while
return
def

# ============================================================

# MAIN ONES FROM THE MATRIX PROGRAM

# ============================================================

input()          # Built-in function
int()            # Built-in function
range()          # Built-in function
str()            # Built-in function
float()          # Built-in function
sum()            # Built-in function
print()          # Built-in function
list()           # Built-in function

s.split()        # Built-in string method
matrix.append()  # Built-in list method
list1.index()    # Built-in list method
