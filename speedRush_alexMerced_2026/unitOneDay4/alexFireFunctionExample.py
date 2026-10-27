import math

def main():

    def checkLimit(number):

        # STEP 1: Loop through numbers from 0 up to number - 1.
        for i in range(number):

            # STEP 2: Pass the current value of i to checkSquare().
            # IMPORTANT: The loop WAITS for checkSquare() to return
            # True or False BEFORE moving to the next iteration.
            if checkSquare(i):

                # STEP 5: If checkSquare(i) returns True,
                # print the current value of i.
                print(i)

            # STEP 6: Once the if statement finishes,
            # the loop moves to the next value of i.
            # Then the process repeats.


    def checkSquare (number):

        # STEP 3: Calculate the square root of the number.
        # Example: 9 ** 0.5 = 3.0
        # Raising a number to 0.5 finds its square root.

        sq = number ** .5 #anything to the power of half of itself is a square root. 9^0.5. == the sqr root of 9 which is 3

        # STEP 4: Check whether the square root is a whole number.
        # % 1 checks for a fractional remainder.
        #
        # Example:
        # 3.0 % 1 == 0  -> True
        # 2.5 % 1 == 0  -> False
        #
        # Return True or False to checkLimit().
        # Execution resumes at the if statement.
        return sq % 1 == 0


    number = int(input("Enter a number\n"))
    checkLimit(number)

main()


# ============================================================
# IMPORTANT NOTE: FUNCTION EXECUTION BEFORE i INCREMENTS
# ============================================================

# Example: User enters 10.

# 1. checkLimit(10) starts.
# 2. The for loop assigns i = 0.
# 3. checkSquare(0) is called.
# 4. checkSquare calculates 0 ** 0.5 = 0.0.
# 5. checkSquare checks 0.0 % 1 == 0.
# 6. The result is True.
# 7. checkSquare returns True to checkLimit.
# 8. The if statement receives True.
# 9. print(i) executes and displays 0.
# 10. NOW the loop advances to i = 1.
# 11. The entire process repeats with checkSquare(1).


# ============================================================
# EXECUTION ORDER
# ============================================================

# checkLimit()
#      |
#      v
# for i in range(number)
#      |
#      v
# checkSquare(i)
#      |
#      v
# Calculate square root
#      |
#      v
# Return True or False
#      |
#      v
# if True -> print(i)
# if False -> skip print(i)
#      |
#      v
# NEXT ITERATION (i increments)


# IMPORTANT:
# checkSquare() must finish executing and return its result
# BEFORE checkLimit() can finish the current iteration.
#
# The loop does NOT increment i while checkSquare() is running.
#
# This is an example of the CALL STACK:
# checkLimit() calls checkSquare().
# checkSquare() returns first (LIFO).
# checkLimit() resumes execution.