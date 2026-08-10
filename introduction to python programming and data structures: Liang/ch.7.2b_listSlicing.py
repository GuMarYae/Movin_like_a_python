# ----------------------------------
# LIST OPERATORS

myList = [10, 20, 30]
myList2 = [40, 50, 60]


# ----------------------------------
# + (Concatenate)
# Combines two lists into one new list.

print(myList + myList2)
# Output:
# [10, 20, 30, 40, 50, 60]


# ----------------------------------
# += (Append multiple items)
# Adds items to the existing list.

myList += [70, 80]

print(myList)
# Output:
# [10, 20, 30, 70, 80]


# ----------------------------------
# * (Repeat)
# Repeats the list a specified number of times.

numbers = [1, 2]

print(numbers * 3)
# Output:
# [1, 2, 1, 2, 1, 2]


# ----------------------------------
# in (Membership Operator)
# Returns a Boolean (True or False).
# True if the item exists in the list.

print(20 in myList)
# Output:
# True

print(100 in myList)
# Output:
# False


# ----------------------------------
# not in (Membership Operator)
# Returns a Boolean (True or False).
# True if the item does NOT exist in the list.

print(100 not in myList)
# Output:
# True

print(20 not in myList)
# Output:
# False


# ----------------------------------
# len()
# Returns the number of items in the list.

print(len(myList))
# Output:
# 5


# ----------------------------------
# sum()
# Returns the sum of all numbers in the list.

print(sum(myList))
# Output:
# 210


# ----------------------------------
# min()
# Returns the smallest value in the list.

print(min(myList))
# Output:
# 10


# ----------------------------------
# max()
# Returns the largest value in the list.

print(max(myList))
# Output:
# 80