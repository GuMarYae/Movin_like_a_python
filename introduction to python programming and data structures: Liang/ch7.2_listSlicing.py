# LIST SLICING
# Format:
# listName[start:end:step]

myList = [10, 20, 30, 40, 50, 60, 70]

# Print the original list
print(myList)
# Output: [10, 20, 30, 40, 50, 60, 70]


# ----------------------------------
# START
# Starts at index 2 and goes to the end
print(myList[2:])
# Output: [30, 40, 50, 60, 70]


# ----------------------------------
# END
# Starts at index 0 and stops BEFORE index 5
print(myList[:5])
# Output: [10, 20, 30, 40, 50]


# ----------------------------------
# START AND END
# Starts at index 2 and stops BEFORE index 5
print(myList[2:5])
# Output: [30, 40, 50]


# ----------------------------------
# STEP
# Take every 2nd element
print(myList[::2])
# Output: [10, 30, 50, 70]


# ----------------------------------
# START, END, AND STEP
# Start at index 1
# Stop BEFORE index 6
# Take every 2nd element
print(myList[1:6:2])
# Output: [20, 40, 60]


# ----------------------------------
# REVERSE THE LIST
# A step of -1 goes backwards
print(myList[::-1])
# Output: [70, 60, 50, 40, 30, 20, 10]


# ----------------------------------
# COPY THE LIST
# [:] creates a copy
copyList = myList[:]

print(copyList)
# Output: [10, 20, 30, 40, 50, 60, 70]


# ----------------------------------
# USING NEGATIVE INDEXES

# Last element
print(myList[-1])
# Output: 70

# Last three elements
print(myList[-3:])
# Output: [50, 60, 70]

# Everything except the last element
print(myList[:-1])
# Output: [10, 20, 30, 40, 50, 60]


# ----------------------------------
# INDEX REFERENCE

# Index:   0   1   2   3   4   5   6
# Value:  10  20  30  40  50  60  70


# ----------------------------------
# REMEMBER:
# start = where to begin
# end   = where to stop (NOT included)
# step  = how many indexes to skip

# list[start:end:step]