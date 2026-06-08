myList = []
myOtherList = [4, 7, 4, 78, 34,34,77,3,5, 2, 1, 0, 9, 8, 6, 5, 4, 3, 2, 1]

# myList = myOtherList.len()

for i in myOtherList:
    print(i)
    
for hiddenValue in myOtherList:
    print(hiddenValue)

personalData = [7]

personalData = [2,"john", False, "three", print('''From: Tony Daniels, PO Box rocNation''')]
print(personalData[2],personalData[4],personalData[3])

##just add something
add = []
add.append ("dipset")

##Inserting an element inside a specific index number
print("\n ______________________")
for i in personalData:
    print(i)
# print(personalData[1])

personalData.insert(1, "John Doe")
print(personalData[1])

##finding an element
##i goess this is another type of scan/loop. ask chat
if "three" in personalData:
        print("this element is in this list")
else: print("naw")

##printing the elemtnt index for that confirmation
indexNumber = personalData.index("John Doe")
print(indexNumber)

personalData.pop(1)
print(indexNumber)

#6.2.7
#print sum of elements values in a list
print((sum([1, 4, 9, 16])))

#MAX NUMBER can do the same thing with MIN
print(max(1,56,72,2,12,199))
 #sort out numbers

print("before the sort :")
for i in myOtherList:
    print(i)
   
myOtherList.sort()

print("after the sort :")
for i in myOtherList:
    print(i)
 ################# more fire shyt #########################
 
 # LISTS CHEAT SHEET

# Create an empty list
myList = []

# Create a list with values
myList = [1, 2, 3]

# len() = number of elements in a list
count = len(myList)

# prices = values
# SHARES the same list
# Changes affect both variables
values = [1, 2, 3]
prices = values

# list(values)
# MAKES A COPY of the list
# Changes do NOT affect the other list
values = [1, 2, 3]
prices = list(values)

# .copy()
# Also makes a copy
prices = values.copy()

# values * num
# Repeats the list num times
values = [1, 2]
result = values * 3
# [1, 2, 1, 2, 1, 2]

# values + moreValues
# Combines two lists into a new list
a = [1, 2]
b = [3, 4]
c = a + b
# [1, 2, 3, 4]

# l[from:to]
# Creates a new sublist
values = [10, 20, 30, 40]
part = values[1:3]
# [20, 30]

# sum()
# Adds all numbers in a list
values = [1, 2, 3]
total = sum(values)
# 6

# min()
# Smallest value in a list
smallest = min(values)

# max()
# Largest value in a list
largest = max(values)

# ==
# Checks if two lists have the same values
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
# True

# IMPORTANT MEMORY TRICK:
# =      -> SHARE
# list() -> COPY
# .copy()-> COPY
 
