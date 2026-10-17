
# make a set
set1 = {"red","yellow","pink","green","purple","orange","blue"}
print(set1) # boom

set2 = set([7, 1, 2, 23, 2, 4, 5]) # create a set from a list
print(set2)

check =  "red" in set1 #this can easily be inside the print as, print("red" in set1)
print("is red in set1? ", check) 

#length
print(f"the length set1 is {len(set1)}")
print(f"the minimum set1 is {min(set1)}")
print("the maximum for set2 is ", sum(set2))  # normal way without the f function
print(f"the maximum is {max(set1)}")

# so its saying set3 = set1 U exit shyt; set3 = set1 union extra shyt
# its not checking shyt. all its saying is that this variable name is equal to some shyt U some other shyt
# so some shyt Unionized with some other shyt is assigned to set3
# Union isn't checking anything. It's combining sets and assigning the result to a variable.

# UNION (|): Combines two sets into one.
set3 = set1 | ({"black","gold"}) # set3 = set1 union black and gold
print(set3)

# UNION (|): Combines a set with itself.
set4 = set2 | set2 # set4 = set2 union with itself
print(set4)

# # DIFFERENCE (-): Keeps only the elements in the FIRST set that are NOT in the SECOND set.
# this is saying only include the things that are in set1 that are different(not in) {"green, yellow"}
# set4 equals everything in set1 MINUS green and yellow.
# test ex.
# Suppose s1 = {1, 2, 4, 3} and s2 = {1, 5, 4, 13}, what is s1 - s2?
#  A. {2, 3, 5, 13}
#  B. {1, 2, 4, 3, 5, 13}
#  C. {1, 2, 4, 3}
#  D. {1, 5, 4, 13}
#  (E.) --> {2, 3}. -----> s1 - s2 means only show whats in s1 thats not in s2
set4 = set1 - {"green","yellow"}
print("Set 4 is: ",set4)

# INTERSECTION (&): Finds items that exist in BOTH sets.
# If green and yellow exist in BOTH sets, print only those matching colors.
set3 = set1 & {"green", "yellow"}
print(set3)

# SYMMETRIC DIFFERENCE (^): Keeps colors that exist in ONE set but NOT BOTH.
# set3 equals colors from set1 and the second set that are NOT shared by both sets.
# Take everything in set1, compare it with the second set, and keep ONLY what's different.
# Any colors shared by both sets get removed from the result.

# 💥 SYMMETRIC DIFFERENCE (^) EXAMPLE
# Suppose s1 = {1, 2, 4, 3} and s2 = {1, 5, 4, 13}
# What is s1 ^ s2?
#
# A. {2, 3, 5, 13}  ✅
# B. {4, 3, 5, 13}
# C. {1, 4}
# D. {1, 5, 4, 13}
# E. {2, 3}
#
# EXPLANATION:
# 1 and 4 exist in BOTH sets, so exclude them.
# 2 and 3 exist ONLY in s1.
# 5 and 13 exist ONLY in s2.
# ANSWER: {2, 3, 5, 13}

print(set1)
set3 = set1 ^ {"green", "yellow", "purple", "red", "pink","orange"}
print(set3)

# LIST CONVERSION: Converts set2 into a list and stores it in list1.
list1 = list(set2)
print(list1)

# SET COMPARISON (==): Checks if set1 contains EXACTLY the same colors.
# Returns True if both sets have identical elements; otherwise False.
print(set1 == {"green", "red", "blue"})

# ADD: Adds "yellow" to set1 if it doesn't already exist.
# Sets don't allow duplicates, so nothing changes if yellow is already there.
set1.add("yellow")

print(sum(set2))
set1.add(42 == sum(set2))

print(set1)

set1.remove("yellow")
print(set1)






