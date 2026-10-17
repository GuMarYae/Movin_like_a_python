import random
import time

CONST_NUMBER_OF_ELEMENTS = 10000

# MAKE A LIST WITH 10,000 ELEMENTS.
# RANGE GENERATES NUMBERS FROM 0 TO 9,999.
# REMEMBER: RANGE IS USED TO GENERATE A SEQUENCE OF NUMBERS.
lst = list(range(CONST_NUMBER_OF_ELEMENTS))
random.shuffle(lst) # shuffle the 10000 elements from 0 - 9999

# CREATE A SET FROM THE LIST
# REMEMBER, SETS REMOVES DUPLICATES
s = set(lst)

# 💥 TEST IF AN ELEMENT IS IN THE ➡️SET
startTime = time.time() # get a start time
# THIS SHYT IS CALLED IMMEDIATELY! REMEMBER: USING () INVOKES A FUNCTION AT THAT EXACT INSTANT.
# time.time() EXECUTES RIGHT NOW, AND startTime STORES THE RESULT.

# LOOP THROUGH NUMBERS 0 TO 9,999.
# REMEMBER: "i in s" IS THE SAME AS "red" in set1.
# EXAMPLE: check = "red" in set1  # Returns True or False
# THE RESULT IS NOT STORED OR PRINTED BECAUSE WE'RE TESTING SPEED.
for i in range(CONST_NUMBER_OF_ELEMENTS):
    i in s # remember frim the setDemo, EXAMPLE: check = "red" in set1 ➡️ line 9
endTime = time.time() # get the endtime
# THIS SHYT IS CALLED IMMEDIATELY! REMEMBER: USING () INVOKES A FUNCTION AT THAT EXACT INSTANT.
# time.time() EXECUTES RIGHT NOW, AND endTime STORES THE RESULT.

runTime = int(1000 * (endTime - startTime))# get the test time. 1000 are milliseconds. remember arduiuno
setTimeStamp = runTime
# 🔥 IMPORTANTX : REMEMBER HOW int() WORKS!
#
# KEEP THE ENTIRE CALCULATION INSIDE int() IF YOU WANT
# THE FINAL RESULT CONVERTED TO AN INTEGER.
# 🚫 int(endTime - startTime) * 1000\
# 👍 int(1000 * (endTime - startTime))
# 👍 int((endTime - startTime)* 1000)
# int() ONLY CONVERTS WHAT'S INSIDE ITS PARENTHESES.
# ANYTHING OUTSIDE IS NOT INCLUDED IN THAT CONVERSION.
# IT IS NOT OMITTED; IT IS CALCULATED SEPARATELY.
#
# WRONG: int(0.003) * 1000 = 0
# RIGHT: int(0.003 * 1000) = 3
#
# REMEMBER: int() REMOVES THE DECIMAL PORTION.
# CONVERTING TOO EARLY CAN CAUSE YOU TO LOSE IMPORTANT VALUES.
print(f"How fast to test if {CONST_NUMBER_OF_ELEMENTS} elements are in the set,\nthe runtime is {runTime} milliseconds")

# 💥 test if an element is in the ➡️list
startTime = time.time() # remember, instantly record the timestamp
for i in range(CONST_NUMBER_OF_ELEMENTS):
    i in lst
endTime = time.time() # instantly record the timestamp
runTime = int(1000 * (endTime - startTime)) # get the test time timestamp
print(f"How fast to test if {CONST_NUMBER_OF_ELEMENTS} elements are in the list, the rumtime is {runTime} milliseconds")

listTimeStamp = runTime

# my own code
# 💥 COMPARE THE PERFORMANCE OF THE SET AND LIST
if listTimeStamp < setTimeStamp:
    print("The list is faster than the set")
elif setTimeStamp < listTimeStamp:
    print("The set is faster than the list")
else:
    print("The set and list have the same recorded runtime")

######################### removing elements ##############################

#remove an element from the set one at a time
startTime = time.time()

for i in range(CONST_NUMBER_OF_ELEMENTS):
    s.remove(i) # line 14 -> thats a set of 10000 values
                # 💥💥💥 remember, Sets don't have indexes. You're removing values.
    
endTime = time.time()
runTime = int(1000 * (endTime - startTime))
print(f"the speed to remove {CONST_NUMBER_OF_ELEMENTS} elements from the set,\nthe runtime is, {runTime} milliseconds")

# remove an element from athe list one at a time
startTime = time.time()
for i in range(CONST_NUMBER_OF_ELEMENTS):
    lst.remove(i) # line 9 -> thats a list of 10000 values with values from 0 - 9999
                  # 💥💥💥 Lists have indexes, but remove() removes by value, not index.
endTime = time.time()
runTime = int(1000 * (endTime - startTime))
print(f"The speed to remove every single {CONST_NUMBER_OF_ELEMENTS} elementS in the list,\nthe runtime is {runTime} milliseconds")




    


    

    

