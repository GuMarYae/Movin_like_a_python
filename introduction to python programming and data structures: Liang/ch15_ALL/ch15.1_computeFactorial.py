def main():

    n = eval(input("Enter a non negative number: "))
    print(f"factorial of {n} is {factorial(n)}")
    
def factorial(n): 
        if n == 0: 
            return 1 # Base case
        else:
            return n * factorial(n - 1)# recursive call
        
        # STEP 1: FUNCTION CALLS (Going DOWN)

# STEP 1: FUNCTION CALLS (Going DOWN)

# 1. factorial(5)
#    5 * factorial(5 - 1)
#    5 * factorial(4)  ← Waiting

# 2. factorial(4)
#    4 * factorial(4 - 1)
#    4 * factorial(3)  ← Waiting

# 3. factorial(3)
#    3 * factorial(3 - 1)
#    3 * factorial(2)  ← Waiting

# 4. factorial(2)
#    2 * factorial(2 - 1)
#    2 * factorial(1)  ← Waiting

# 5. factorial(1)
#    1 * factorial(1 - 1)
#    1 * factorial(0)  ← Waiting

# 6. factorial(0)
#    return 1          ← BASE CASE


# STEP 2: CALCULATIONS (Going UP)

# 1. factorial(1)
#    n * factorial(n - 1)
#    1 * factorial(1 - 1)
#    1 * factorial(0) remember line 7, if n == 1, the value is 1
#    1 * 1 = 1
#        ↑
#    1 returned from factorial(0)
#    Returns 1 to factorial(2)


# 2. factorial(2)
#    n * factorial(n - 1)
#    2 * factorial(2 - 1)
#    2 * factorial(1)
#    2 * 1 = 2
#        ↑
#    1 returned from factorial(1)
#    Returns 2 to factorial(3)


# 3. factorial(3)
#    n * factorial(n - 1)
#    3 * factorial(3 - 1)
#    3 * factorial(2)
#    3 * 2 = 6
#        ↑
#    2 returned from factorial(2)
#    Returns 6 to factorial(4)


# 4. factorial(4)
#    n * factorial(n - 1)
#    4 * factorial(4 - 1)
#    4 * factorial(3)
#    4 * 6 = 24
#        ↑
#    6 returned from factorial(3)
#    Returns 24 to factorial(5)


# 5. factorial(5)
#    n * factorial(n - 1)
#    5 * factorial(5 - 1)
#    5 * factorial(4)
#    5 * 24 = 120
#        ↑
#    24 returned from factorial(4)
#    Returns 120 to main()

############################################################
################ summary of recursion ######################
############################################################

# SUMMARY OF RECURSION
#
# STEP 1: GOING DOWN (FUNCTION CALLS)
# The factorial function calls itself repeatedly.
# Each call decreases n by 1 (n - 1).
# It starts at factorial(5) and continues down to factorial(0).
# Each unfinished function call waits in memory on the call stack.
# No multiplication is completed yet because each function
# is waiting for the next function to return a value.
#
# STEP 2: BASE CASE (STOPPING CONDITION)
# When n == 0, the function stops calling itself.
# factorial(0) returns 1.
# This is the first value returned and starts the calculations.
#
# STEP 3: GOING UP (CALCULATIONS)
# Python now resumes the waiting functions in reverse order.
# The functions DO NOT call themselves again on the way up.
# Instead, each function receives the return value
# from the function it previously called.
#
# That returned value replaces the factorial(n - 1) expression.
# Python multiplies n by that returned value.
# The result is then returned to the next waiting function.
#
# Example:
# factorial(3) = 3 * factorial(2)
# factorial(2) previously returned 2.
# Therefore, factorial(3) = 3 * 2 = 6.
# That 6 is returned to factorial(4).
#
# STEP 4: FINAL RESULT
# This continues until the original factorial(5) call resumes.
# factorial(4) returns 24.
# factorial(5) calculates 5 * 24 = 120.
# factorial(5) returns 120 to main().
# main() prints the final result.
#
# IMPORTANT:
# Going DOWN = Recursive function calls (5 to 0).
# Going UP = Returning values and completing calculations (0 to 5).
# Each function uses the return value from the function it called.
# This follows LIFO (Last In, First Out) using the call stack.


############################################################
################ CALL STACK AND LIFO #######################
############################################################

# RECURSION USES THE CALL STACK, WHICH FOLLOWS LIFO.
#
# LIFO = LAST IN, FIRST OUT.
#
# STEP 1: GOING DOWN (PUSH)
# Each recursive function call is added to the call stack.
# Each unfinished function waits for the next call to return.
#
# factorial(5)  ← FIRST IN
# factorial(4)
# factorial(3)
# factorial(2)
# factorial(1)
# factorial(0)  ← LAST IN
#
# STEP 2: GOING UP (POP)
# Because the call stack follows LIFO, the LAST function
# called is the FIRST function to finish.
#
# factorial(0) returns 1    ← FIRST OUT
# factorial(1) returns 1
# factorial(2) returns 2
# factorial(3) returns 6
# factorial(4) returns 24
# factorial(5) returns 120  ← LAST OUT
#
# Each function receives the return value from the
# function it called, completes its calculation,
# and is removed from the call stack.
#
# IMPORTANT:
# Recursion itself is not LIFO.
# Recursion USES the CALL STACK, which follows LIFO.
#
# PUSH = Adding a function call to the stack.
# POP = Removing a completed function call from the stack.
#
# REMEMBER:
# GOING DOWN = PUSHING recursive calls onto the stack.
# GOING UP = POPPING completed calls off the stack.
# LIFO = LAST IN, FIRST OUT.

        

main() # call the main function