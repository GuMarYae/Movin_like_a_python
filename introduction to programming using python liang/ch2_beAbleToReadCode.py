###########################################################################################
# 💥 SIMPLE WAY TO THINK ABOUT IT 💥
#
# x does NOT change until the computer finishes the entire right side.
#
# x only gets a new value AFTER the calculation is finished.
#
# Example:
#
# x = 1
# x = 2
#
# NOW x becomes 2 immediately because the right side is already just 2.
#
# But:
#
# x = 1
# x = 2 * x + 1
#
# x is STILL 1 while Python does the math.
# Python mentally sees:
#
#     x = 2 * 1 + 1
#
# 💥 hen x finally becomes 3. 💥
###########################################################################################

x = 1                  # x is 1.

# x is STILL 1 while Python solves the right side.
x = 2 * x + 1          # 2 * 1 + 1 = 3

print(x)               # Prints 3.

# A. 0
# B. 1
# C. 2
# D. 3  ✅
# E. 4

############## another ###############
x = 1
# x is 1
# x is x + 1 + 2.5

x = 1
x = x + 2.5 

print(x)

x = 100000
x = 7
print(x)

###########################################################################################
# 💥 REMEMBER THIS FROM ALGEBRA 💥
#
# If there are NO parentheses, the exponent ONLY applies to the number
# or expression immediately to its LEFT.
#
# Example:
#
#     2 * 3²
#
# is NOT:
#
#     (2 * 3)²
#
# Instead, it is:
#
#     2 * (3²)
#
#     2 * 9
#
#     = 18 ✅
#
# If you wanted BOTH numbers to be squared, you MUST use parentheses:
#
#     (2 * 3)²
#
#     6²
#
#     = 36
#
# Rule:
#
#     Exponents stay attached to whatever is immediately to their left,
#     unless parentheses tell them otherwise.
###########################################################################################
a = 2 * 3 ** 2
print(a)    # 2 * (3 ** 2) = 2 * 9 = 18

# A. 36
# B. 18  ✅
# C. 12
# D. 81
# now look at the next ex below

b = (2 * 3)**2
print (b)

###########################################################################################
# 💥 another ex assigning y to x 💥
#
# Python solves the RIGHT SIDE first.
#
# x = 1
#
# y = x = x + 1
#
# Step 1:
# x + 1 = 2
#
# Step 2:
# x = 2
#
# Step 3:
# y = 2
#
# So BOTH x and y become 2.
#
# Think of it like this:
#python and any ther lang is looking at x = x + 1 and saying y equals that
#  so 1 = 1 + 1
# y = 1 + 1
# y = 2
###########################################################################################

x = 1                  # x is 1.

y = x = x + 1          # x + 1 = 2, then x = 2, then y = 2.

print("y is", y)       # Prints: y is 2

# Answer: C ✅

###########################################################################################
# 💥 more confusion to read better,  +=  operator 💥
#
# Remember:
#
# i += something
#
# ALWAYS means:
#
# i = i + something 💥💥💥💥💥 remmber this line, the something..  that whoole right side is "something"
#
# Example:
#
# j = i = 1
#
# i += j + j * 5 💥💥💥💥💥 all of that is the something. but remember i += is saying i = itself , 1
#
# First, rewrite it:
#
# i = i + j + j * 5 💥💥💥💥💥 the something is j + j * 5
#
# Now replace the variables with their values:
#
# i = 1 + 1 + 1 * 5 💥💥💥💥💥 the something is 1 + 1 * 5, thile i += is still 1, thats where the extra left most 1 came from
#                   💥💥💥💥💥 the the 1 * 5 executes first to just 5, 1 + 1 + (1 * 5 ) == 1 + 1 + 5
# Do the multiplication first:
#
# i = 1 + 1 + 5
#
# Then add left to right:
#
# i = 2 + 5
#
# i = 7 ✅
#
# A good trick:
#
# Don't think of "j" anymore.
# Replace every variable with its CURRENT value first.
###########################################################################################

j = i = 1          # i = 1, j = 1

i += j + j * 5     # Same as: i = 1 + 1 + 1 * 5

print(i)           # 7
###########################################################################################
############################ more tricks ##################################################
###########################################################################################


# Starting values
x = 2
y = 1

# Compound assignment
x *= y + 1

# Python sees it as:
# x = x * y + 1
# or
# x = x * (y + 1)

# Step 1:
# x = 2 * (1 + 1)

# Step 2:
# x = 2 * 2

# Step 3:
# x = 4

print(x)   # 4