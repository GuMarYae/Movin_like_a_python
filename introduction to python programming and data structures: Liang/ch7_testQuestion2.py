# values = [] is a DEFAULT parameter.
# IMPORTANT: Python creates this default list ONCE.
# It does NOT create a new empty list every time f() is called.

def f(i, values=[]):

    # append(i) adds i to the SAME list
    values.append(i)

    # return sends the current list back
    return values


# FIRST CALL
# i = 1
# values starts as []
# append(1)
# values = [1]
f(1)


# SECOND CALL
# i = 2
#
# IMPORTANT:
# values DOES NOT go back to []
# It remembers [1] from the first call.
#
# append(2)
# values = [1, 2]
f(2)


# THIRD CALL
# i = 3
#
# values is currently [1, 2]
# append(3)
# values = [1, 2, 3]
#
# f(3) returns [1, 2, 3]
# That returned list gets stored in v.
v = f(3)


# v = [1, 2, 3]
print(v)


# OUTPUT:
# [1, 2, 3]
#
# ANSWER: C
#
# MAIN THING TO REMEMBER:
# A default list like values=[] is created ONCE
# and the SAME list is reused on later calls.