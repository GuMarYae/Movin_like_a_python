# List MUST be sorted for binary search
myList = [1, 4, 6, 8, 10, 15, 20]

# Number we are looking for
key = 11


# LOW = first index
low = 0

# HIGH = last index
# len(myList) = 7
# Last index = 7 - 1 = 6
high = len(myList) - 1


# CURRENTLY:
#
# INDEX:  0  1  2  3   4   5   6
# VALUE:  1  4  6  8  10  15  20
#
# low = 0
# high = 6


# Find the middle INDEX
mid = (low + high) // 2

# (0 + 6) // 2
# 6 // 2 = 3
#
# So:
# mid = 3


# myList[3] = 8
#
# We want 11
#
# 11 > 8
#
# Therefore 11 CANNOT be at index 3 or anything below it.


if key > myList[mid]:

    # mid = 3
    #
    # low = mid + 1
    # low = 3 + 1
    # low = 4
    low = mid + 1


# AFTER FIRST ITERATION:
#
# low = 4
# high = 6
#
# We eliminated indexes:
# 0, 1, 2, 3
#
# REMAINING:
#
# INDEX:   4   5   6
# VALUE:  10  15  20
#
# So the answer is:
#
# low = 4
# high = 6
#
# ANSWER: D