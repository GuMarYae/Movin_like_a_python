def recursive_sum(m, n):
    if m == n:
        return m  # Base case
    else:
        return m + recursive_sum(m + 1, n)  # Recursive call


def main():
    m = 1
    n = 5

    print(f"Sum = {recursive_sum(m, n)}")


# STEP 1: FUNCTION CALLS (GOING DOWN)

# 1. recursive_sum(1, 5)
#    m + recursive_sum(m + 1, n)
#    1 + recursive_sum(1 + 1, 5)
#    1 + recursive_sum(2, 5)  ← Waiting

# 2. recursive_sum(2, 5)
#    m + recursive_sum(m + 1, n)
#    2 + recursive_sum(2 + 1, 5)
#    2 + recursive_sum(3, 5)  ← Waiting

# 3. recursive_sum(3, 5)
#    m + recursive_sum(m + 1, n)
#    3 + recursive_sum(3 + 1, 5)
#    3 + recursive_sum(4, 5)  ← Waiting

# 4. recursive_sum(4, 5)
#    m + recursive_sum(m + 1, n)
#    4 + recursive_sum(4 + 1, 5)
#    4 + recursive_sum(5, 5)  ← Waiting

# 5. recursive_sum(5, 5)
#    if m == n:
#       return m
#    return 5  ← BASE CASE


# STEP 2: CALCULATIONS (GOING UP)
#####################################################################
# IMPORTANT NOTE:
#              n = 5            
#                  ⬇️   
# recursive_sum(4, 5)
#              (start, stop, step[wasnt in this example])
# recursive_sum(4, 5)
# is ONLY used as the stopping point while m increments.
# Once m reaches n (m == n), recursion stops.
# n has already served its purpose. We, in most cases, calculate the start number unless we write code that says otherwise.
#
# During LIFO, we DO NOT add or multiply by n directly.
# We ONLY calculate using m and the returned value
# from the previous recursive function call.
#
# IMPORTANT: The number 5 IS included in the calculation,
# but ONLY because the base case returns m (which is 5).
# It is NOT included because n = 5.
######################################################################
# 1. recursive_sum(4, 5)
#    m + recursive_sum(m + 1, n)
#    4 + recursive_sum(4 + 1, 5)
#    4 + recursive_sum(5, 5)
#    4 + 5 = 9
#        ↑
#    5 returned from recursive_sum(5, 5)
#    Returns 9 to recursive_sum(3, 5)


# 2. recursive_sum(3, 5)
#    m + recursive_sum(m + 1, n)
#    3 + recursive_sum(3 + 1, 5)
#    3 + recursive_sum(4, 5)
#    3 + 9 = 12
#        ↑
#    9 returned from recursive_sum(4, 5)
#    Returns 12 to recursive_sum(2, 5)


# 3. recursive_sum(2, 5)
#    m + recursive_sum(m + 1, n)
#    2 + recursive_sum(2 + 1, 5)
#    2 + recursive_sum(3, 5)
#    2 + 12 = 14
#        ↑
#    12 returned from recursive_sum(3, 5)
#    Returns 14 to recursive_sum(1, 5)


# 4. recursive_sum(1, 5)
#    m + recursive_sum(m + 1, n)
#    1 + recursive_sum(1 + 1, 5)
#    1 + recursive_sum(2, 5)
#    1 + 14 = 15
#        ↑
#    14 returned from recursive_sum(2, 5)
#    Returns 15 to main()


############################################################
################ SUMMARY OF RECURSION ######################
############################################################

# STEP 1: GOING DOWN (FUNCTION CALLS)
#
# The recursive_sum function calls itself repeatedly.
# Each call increases m by 1 (m + 1).
# The value of n stays at 5.
#
# It starts at recursive_sum(1, 5)
# and continues until recursive_sum(5, 5).
#
# Each unfinished function call waits in memory
# on the CALL STACK.
#
# No addition is completed yet because each function
# is waiting for the next function to return a value.


# STEP 2: BASE CASE (STOPPING CONDITION)
#
# When m == n, the function stops calling itself.
#
# recursive_sum(5, 5) returns 5.
#
# This is the first value returned and starts
# the calculations going back up.


############################################################
############ UNDERSTANDING FUNCTION PARAMETERS #############
############################################################

# IMPORTANT: UNDERSTANDING FUNCTION PARAMETERS
#
# recursive_sum(m, n)
#
# m = START value (the number being added)
# n = STOP value (the stopping point)
#
# Example: recursive_sum(1, 5)
#
# m increases: 1 → 2 → 3 → 4 → 5
# n stays at 5 throughout the recursion.
#
# ONLY m is directly used in the addition.
# n is ONLY used to check the stopping condition.
#
# When m == n, the base case returns m (which is 5).
# That returned 5 IS included in the final sum.
#
# IMPORTANT:
# Function parameters do not automatically get calculated.
# The code determines which parameters are used in the math.
#
# If a function has (start, stop, count), that does NOT
# automatically mean only start is calculated.
# It depends on how the function is written.


# STEP 3: GOING UP (CALCULATIONS)
#
# Python now resumes the waiting functions
# in reverse order.
#
# The functions DO NOT call themselves again
# on the way up.
#
# Instead, each function receives the return value
# from the function it previously called.
#
# That returned value replaces the
# recursive_sum(m + 1, n) expression.
#
# Python adds m to that returned value.
#
# The result is then returned to the
# next waiting function.
#
# Example:
#
# recursive_sum(4, 5) = 4 + recursive_sum(5, 5)
#
# recursive_sum(5, 5) previously returned 5.
#
# Therefore:
#
# recursive_sum(4, 5) = 4 + 5 = 9
#
# That 9 is returned to recursive_sum(3, 5).


# STEP 4: FINAL RESULT
#
# This continues until the original
# recursive_sum(1, 5) call resumes.
#
# recursive_sum(2, 5) returns 14.
#
# recursive_sum(1, 5) calculates 1 + 14 = 15.
#
# recursive_sum(1, 5) returns 15 to main().
#
# main() prints the final result.
#
# FINAL OUTPUT: Sum = 15


############################################################
################ CALL STACK AND LIFO #######################
############################################################

# RECURSION USES THE CALL STACK, WHICH FOLLOWS LIFO.
#
# LIFO = LAST IN, FIRST OUT.


# STEP 1: GOING DOWN (PUSH)
#
# Each recursive function call is added to the stack.
# Each unfinished function waits for a return value.
#
# recursive_sum(1, 5)  ← FIRST IN
# recursive_sum(2, 5)
# recursive_sum(3, 5)
# recursive_sum(4, 5)
# recursive_sum(5, 5)  ← LAST IN


# STEP 2: GOING UP (POP)
#
# Because the CALL STACK follows LIFO,
# the LAST function called is the FIRST to finish.
#
# recursive_sum(5, 5) returns 5    ← FIRST OUT
# recursive_sum(4, 5) returns 9
# recursive_sum(3, 5) returns 12
# recursive_sum(2, 5) returns 14
# recursive_sum(1, 5) returns 15   ← LAST OUT
#
# Each function receives the return value
# from the function it called.
#
# It completes its calculation and
# is removed from the CALL STACK.


# IMPORTANT:
#
# Recursion itself is not LIFO.
# Recursion USES the CALL STACK, which follows LIFO.
#
# PUSH = Adding a function call to the stack.
# POP = Removing a completed function call from the stack.
#
# GOING DOWN = PUSHING recursive calls onto the stack.
# GOING UP = POPPING completed calls off the stack.
#
# LIFO = LAST IN, FIRST OUT.


############################################################
################ FINAL COMPARISON ##########################
############################################################

# OUR PREVIOUS PYTHON EXAMPLE:
#
# n - 1
# Decreases n until n == 0.
# Base case returns 0 for sum_numbers().
#
# CODE BEAUTY'S EXAMPLE:
#
# m + 1
# Increases m until m == n.
# Base case returns m.
#
# BOTH:
#
# 1. Use recursion.
# 2. Store unfinished calls on the CALL STACK.
# 3. Follow LIFO (Last In, First Out).
# 4. Stop when the base case is reached.
# 5. Resume calculations in reverse order.
# 6. Use returned values from previous function calls.


main()  # Call the main function