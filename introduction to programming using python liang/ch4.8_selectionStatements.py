# Long Version

number = 5

if (number % 2 == 0):
    even = True
else:
    even = False

############################################################################

# Equivalent (Short Version)
# This is like saying true or false, depending on what the outcome is: even = True or even = False
# the parens have to be simplified first
# we have number being 5. First, 5 % 2 = 1. Now Python compares: 1 == 0
# try printing 5 % 2 == 0, it'll say False, so if that value is False then even = False because 5 made the expression evaluate to False
# # it's like saying even = (a Boolean expression), and this Boolean expression evaluates to False

even = (number % 2 == 0)


# ----------------------------------------
# Example 1
# ----------------------------------------

number = 8

# Long Version
if (number % 2 == 0):
    even = True
else:
    even = False

print(even)      # True


# Short Version
even = (number % 2 == 0)

print(even)      # True


# ----------------------------------------
# Example 2
# ----------------------------------------

number = 7

# Long Version
if (number % 2 == 0):
    even = True
else:
    even = False

print(even)      # False


# Short Version
even = (number % 2 == 0)

print(even)      # False