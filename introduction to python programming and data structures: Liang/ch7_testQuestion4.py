# We are SEARCHING for the number 8.

# 8 is NOT currently in the list.

myList = [2, 4, 7, 10, 15]
key = 8


# --------------------------------------------------
# STARTING LIST
# --------------------------------------------------
#
# INDEX:   0   1   2   3    4
# VALUE:   2   4   7   10   15
#
#          ↑       ↑         ↑
#         LOW     MID       HIGH
#
# LOW = the LOWEST index we are currently searching.
# HIGH = the HIGHEST index we are currently searching.
# MID = the index in the MIDDLE of low and high.


# LOW starts at the first index.

low = 0


# HIGH starts at the last index.
#
# len(myList) = 5
# 5 - 1 = 4
#
# So high = 4

high = len(myList) - 1


# --------------------------------------------------
# FIRST SEARCH
# --------------------------------------------------

# Find the middle INDEX.
#
# low = 0
# high = 4
#
# (0 + 4) // 2
# 4 // 2
# = 2
#
# So mid = 2

mid = (low + high) // 2


# INDEX:   0   1   2   3    4
# VALUE:   2   4   7   10   15
#
#          ↑       ↑         ↑
#         LOW     MID       HIGH
#
# myList[mid]
# myList[2]
# = 7
#
# We are searching for 8.
#
# 8 > 7
#
# Therefore 8 cannot be at indexes:
#
# 0, 1, or 2
#
# So we search to the RIGHT.

if key > myList[mid]:

    # mid = 2
    #
    # low = mid + 1
    # low = 2 + 1
    # low = 3
    #
    # LOW moves to index 3.

    low = mid + 1


# --------------------------------------------------
# NOW THE SEARCH AREA IS:
# --------------------------------------------------
#
# INDEX:   0   1   2   3    4
# VALUE:   2   4   7   10   15
#                      ↑     ↑
#                     LOW   HIGH
#
# We eliminated:
#
# indexes 0, 1, 2
#
# We are now searching:
#
# [10, 15]


# --------------------------------------------------
# SECOND SEARCH
# --------------------------------------------------

# low = 3
# high = 4
#
# Find the new middle:
#
# (3 + 4) // 2
# 7 // 2
# = 3
#
# So mid = 3

mid = (low + high) // 2


# INDEX:   0   1   2   3    4
# VALUE:   2   4   7   10   15
#                      ↑     ↑
#                  LOW/MID  HIGH
#
# myList[mid]
# myList[3]
# = 10
#
# We want 8.
#
# 8 < 10
#
# So we search LEFT of index 3.

if key < myList[mid]:

    # high = mid - 1
    #
    # high = 3 - 1
    # high = 2

    high = mid - 1


# --------------------------------------------------
# SEARCH IS OVER
# --------------------------------------------------
#
# low = 3
# high = 2
#
# low > high
#
# 3 > 2
#
# There is nothing left to search.
#
# Therefore:
#
# 8 IS NOT IN THE LIST.


# --------------------------------------------------
# LOW IS NOW THE INSERTION POINT
# --------------------------------------------------
#
# low = 3
#
# This means:
#
# If we wanted to insert 8 into the sorted list,
# index 3 is where it belongs.
#
# BEFORE:
#
# INDEX:   0   1   2   3    4
# VALUE:   2   4   7   10   15
#                      ↑
#                8 belongs here


# --------------------------------------------------
# THIS IS WHERE -low - 1 COMES IN
# --------------------------------------------------
#
# The book's binarySearch function does NOT simply
# return low when the key is missing.
#
# It returns:
#
# return -low - 1
#
# Why?
#
# A NEGATIVE return value tells us:
#
# "The key was NOT found."
#
# Since low = 3:
#
# -low - 1
# = -3 - 1
# = -4
#
# So binarySearch would return:
#
# -4
#
# IMPORTANT:
#
# -4 does NOT mean index -4.
#
# It is an encoded way of saying:
#
# "The key was not found, and its insertion index is 3."


result = -low - 1

print("Binary search return value:", result)


# --------------------------------------------------
# IF A QUESTION GIVES YOU -4
# --------------------------------------------------
#
# To get the insertion index back:
#
# insertionIndex = -result - 1
#
# result = -4
#
# -(-4) - 1
# = 4 - 1
# = 3

insertionIndex = -result - 1

print("Insertion index:", insertionIndex)


# --------------------------------------------------
# OPTIONAL: ACTUALLY INSERT THE NUMBER
# --------------------------------------------------

print("Before:", myList)

# Insert 8 at index 3.
myList.insert(insertionIndex, key)

print("After:", myList)


# OUTPUT:
#
# Binary search return value: -4
# Insertion index: 3
# Before: [2, 4, 7, 10, 15]
# After:  [2, 4, 7, 8, 10, 15]


# --------------------------------------------------
# EASY WAY TO REMEMBER
# --------------------------------------------------
#
# LOW  = beginning of search area
#
# HIGH = end of search area
#
# MID  = middle index
#
# key > middle value:
# move LOW right
#
# key < middle value:
# move HIGH left
#
# low > high:
# key was NOT found
#
# LOW then tells you the insertion index.
#
# The book returns:
#
# -low - 1
#
# So:
#
# insertion index 3
# becomes
# -3 - 1
# = -4
#
# And if you are GIVEN -4:
#
# -(-4) - 1
# = 3
#
# So the insertion index is 3.