good_credit = True;
bad_credit=False;
price = 1000000;
down_payment = 0
if(good_credit == True):
    down_payment = price * .10
    print("down payment is ",down_payment)
elif(bad_credit == True): 
    down_payment = price * .20
    print("down payment is ", down_payment)
    
#printint the last elements or element from the back

myList = [2,4,6,8,10]
lastElement = myList[-1]
secondToLastElement = myList[-1-1]
thirdTolast = myList[-3]

print("last element = ", lastElement, " and the second to last element is = ", secondToLastElement,"\n now, third to last is: ", thirdTolast)

################# more fire shyt #########################
 
# LISTS CHEAT SHEET

# ==================================================
# LISTS CHEAT SHEET
# ==================================================
print("starts here 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 starts here")
# Create an empty list

myList = []

print("Empty list:", myList)

# ==================================================
# Create a list with values
# ==================================================

myList = [1, 2, 3]

print("List with values:", myList)

# ==================================================
# len()
# Number of elements in a list
# ==================================================

count = len(myList)

print("Number of elements:", count)

# ==================================================
# = SHARES THE SAME LIST
# ==================================================

values = [1, 2, 3]
prices = values

prices[0] = 99

print("\nUsing = (SHARE)")
print("values =", values)
print("prices =", prices)
print("Changing prices changed values too!")

# ==================================================
# list()
# MAKES A COPY
# ==================================================
#the word "list" is a key word in python
values = [1, 2, 3]
prices = list(values)

prices[0] = 99

print("\nUsing list() (COPY)")
print("values =", values)
print("prices =", prices)
print("Changing prices did NOT change values!")

# ==================================================
# .copy()
# ALSO MAKES A COPY
# ==================================================

values = [1, 2, 3]
prices = values.copy()

prices[0] = 99

print("\nUsing .copy() (COPY)")
print("values =", values)
print("prices =", prices)
print("Changing prices did NOT change values!")

# ==================================================
# values * num
# Repeat a list
# ==================================================

values = [1, 2]

result = values * 3

print("\nRepeated list:", result)

# ==================================================
# values + moreValues
# Combine lists
# ==================================================

a = [1, 2]
b = [3, 4]

c = a + b

print("\nCombined lists:", c)

# ==================================================
# SLICING
# l[from:to]
# Starts at from
# Stops BEFORE to
# ==================================================

values = [10, 20, 30, 40]

part = values[1:3]

print("\nOriginal list:", values)
print("values[1:3] =", part)

# ==================================================
# sum()
# Add all values
# ==================================================

values = [1, 2, 3]

total = sum(values)

print("\nSum of list:", total)

# ==================================================
# min()
# Smallest value
# ==================================================

smallest = min(values)

print("\nSmallest value:", smallest)

# ==================================================
# max()
# Largest value
# ==================================================

largest = max(values)

print("\nLargest value:", largest)

# ==================================================
# ==
# Compare lists
# ==================================================

a = [1, 2, 3]
b = [1, 2, 3]

print("\nDo the lists contain the same values?", a == b)

# ==================================================
# NEGATIVE INDEXES
# Count backwards from the end
# ==================================================

myList = [2, 4, 6, 8, 10]

print("\nList:", myList)

print("myList[-1] = Last element =", myList[-1])
print("myList[-2] = Second to last element =", myList[-2])
print("myList[-3] = Third to last element =", myList[-3])
print("myList[-4] = Fourth to last element =", myList[-4])
print("myList[-5] = Fifth to last element =", myList[-5])

# ==================================================
# MEMORY TRICKS
# ==================================================

print("\n========== MEMORY TRICKS ==========")

print("=       -> SHARE the same list")
print("list()  -> COPY the list")
print(".copy() -> COPY the list")

print("-1 -> last element")
print("-2 -> second to last element")
print("-3 -> third to last element")

# ==================================================
# FINAL QUICK REFERENCE
# ==================================================

print("\n========== QUICK REFERENCE ==========")

print("len(myList)      -> number of elements")
print("sum(myList)      -> add all numbers")
print("min(myList)      -> smallest value")
print("max(myList)      -> largest value")
print("a + b            -> combine lists")
print("values * 3       -> repeat list 3 times")
print("values[1:3]      -> slice from 1 up to (not including) 3")
print("a == b           -> compare values in two lists")
print("list(values)     -> copy")
print("values.copy()    -> copy")
print("prices = values  -> share")


print('''##########################################################
##########################################################
##########################################################
##########################################################
##########################################################''')


# ==================================================
# ADDITIONAL LIST METHODS
# ==================================================

# ==================================================
# append(element)
# Add an element to the END of the list
# ==================================================

numbers = [1, 2, 3]

numbers.append(4)

print("After append(4):", numbers)

# ==================================================
# insert(position, element)
# Insert an element at a specific index
# Everything after it moves down
# ==================================================

numbers = [1, 2, 3]

numbers.insert(1, 99)

print("After insert(1, 99):", numbers)

# ==================================================
# pop()
# Remove the LAST element
# ==================================================

numbers = [1, 2, 3, 4]

removed = numbers.pop()

print("Removed element:", removed)
print("List after pop():", numbers)

# ==================================================
# pop(position)
# Remove an element at a specific index
# Everything after it moves up
# ==================================================

numbers = [1, 2, 3, 4]

removed = numbers.pop(1)

print("Removed element at index 1:", removed)
print("List after pop(1):", numbers)

# ==================================================
# index(element)
# Find the index of an element
# The element must exist
# ==================================================

numbers = [10, 20, 30, 40]

position = numbers.index(30)

print("Index of 30:", position)

# ==================================================
# remove(element)
# Remove a VALUE from the list
# The element must exist
# ==================================================

numbers = [10, 20, 30, 40]

numbers.remove(30)

print("After remove(30):", numbers)

# ==================================================
# sort()
# Sort from smallest to largest
# ==================================================

numbers = [8, 3, 10, 1, 5]

numbers.sort()

print("Sorted list:", numbers)

# ==================================================
# COMMON BEGINNER MISTAKE
# ==================================================

numbers = [10, 20, 30, 40]

numbers.pop(2)

print("pop(2) removes INDEX 2:", numbers)

numbers = [10, 20, 30, 40]

numbers.remove(20)

print("remove(20) removes VALUE 20:", numbers)

# ==================================================
# ADDITIONAL MEMORY TRICKS
# ==================================================

print("\n========== ADDITIONAL MEMORY TRICKS ==========")

print("append(x) -> add x to END")
print("insert(i, x) -> add x at INDEX i")
print("pop() -> remove LAST item")
print("pop(i) -> remove item at INDEX i")
print("remove(x) -> remove VALUE x")
print("index(x) -> find INDEX of VALUE x")
print("sort() -> sort smallest to largest")

# ==================================================
# ULTIMATE LIST MEMORY TRICKS
# ==================================================

print("\n========== ULTIMATE LIST MEMORY TRICKS ==========")

print("= -> SHARE")
print("list() -> COPY")
print(".copy() -> COPY")

print("-1 -> last element")
print("-2 -> second to last element")
print("-3 -> third to last element")

print("append(x) -> add to END")
print("insert(i, x) -> add at INDEX")
print("pop() -> remove LAST")
print("pop(i) -> remove by INDEX")
print("remove(x) -> remove by VALUE")
print("index(x) -> find INDEX")
print("sort() -> sort ascending")

# ==================================================
# QUICK REFERENCE
# ==================================================

print("\n========== QUICK REFERENCE ==========")

print("len(myList) -> number of elements")
print("sum(myList) -> add all numbers")
print("min(myList) -> smallest value")
print("max(myList) -> largest value")

print("a + b -> combine lists")
print("values * 3 -> repeat list")

print("values[1:3] -> slice")
print("a == b -> compare lists")

print("prices = values -> SHARE")
print("list(values) -> COPY")
print("values.copy() -> COPY")

print("append(x) -> add to end")
print("insert(i, x) -> insert at index")
print("pop() -> remove last")
print("pop(i) -> remove at index")
print("remove(x) -> remove value")
print("index(x) -> find index")
print("sort() -> sort list")