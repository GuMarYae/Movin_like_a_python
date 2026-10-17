def sum_numbers(n):
    if n == 0:
        return 0  # BASE CASE
    else:
        return n + sum_numbers(n - 1)  # RECURSIVE CALL


print(sum_numbers(4))


# STEP 1: FUNCTION CALLS (GOING DOWN)
#
# Each recursive call decreases n by 1.
# Each unfinished function waits on the CALL STACK.
#
# 1. sum_numbers(4)
#    4 + sum_numbers(3)  ← Waiting
#
# 2. sum_numbers(3)
#    3 + sum_numbers(2)  ← Waiting
#
# 3. sum_numbers(2)
#    2 + sum_numbers(1)  ← Waiting
#
# 4. sum_numbers(1)
#    1 + sum_numbers(0)  ← Waiting
#
# 5. sum_numbers(0)
#    return 0            ← BASE CASE
#
# The function stops calling itself when n == 0.


# STEP 2: CALCULATIONS (GOING UP)
#
# The CALL STACK follows LIFO (Last In, First Out).
# The last function called is the first to finish.
#
# Python resumes each waiting function in reverse order.
# Each function receives the RETURN VALUE from
# the function it previously called.


# 1. sum_numbers(1)
#    n + sum_numbers(n - 1)
#    1 + sum_numbers(1 - 1)
#    1 + sum_numbers(0)
#    1 + 0 = 1
#        ↑
#    0 returned from sum_numbers(0)
#    Returns 1 to sum_numbers(2)


# 2. sum_numbers(2)
#    n + sum_numbers(n - 1)
#    2 + sum_numbers(2 - 1)
#    2 + sum_numbers(1)
#    2 + 1 = 3
#        ↑
#    1 returned from sum_numbers(1)
#    Returns 3 to sum_numbers(3)


# 3. sum_numbers(3)
#    n + sum_numbers(n - 1)
#    3 + sum_numbers(3 - 1)
#    3 + sum_numbers(2)
#    3 + 3 = 6
#        ↑
#    3 returned from sum_numbers(2)
#    Returns 6 to sum_numbers(4)


# 4. sum_numbers(4)
#    n + sum_numbers(n - 1)
#    4 + sum_numbers(4 - 1)
#    4 + sum_numbers(3)
#    4 + 6 = 10
#        ↑
#    6 returned from sum_numbers(3)
#    Returns 10 to print()


# STEP 3: CALL STACK (LIFO)
#
# LIFO = LAST IN, FIRST OUT
#
# GOING DOWN (PUSHING CALLS ONTO THE STACK)
#
#    sum_numbers(0)  ← LAST IN (BASE CASE)
#    sum_numbers(1)
#    sum_numbers(2)
#    sum_numbers(3)
#    sum_numbers(4)  ← FIRST IN
#
# Each function call has its own stack frame.
# Each frame stores information needed to resume
# that particular function call.
#
# When sum_numbers(0) returns 0,
# its stack frame is removed.
#
# GOING UP (RETURNING AND POPPING STACK FRAMES)
#
#    sum_numbers(0) returns 0
#    sum_numbers(1) returns 1
#    sum_numbers(2) returns 3
#    sum_numbers(3) returns 6
#    sum_numbers(4) returns 10
#
# Each function finishes its calculation,
# returns its value, and is removed from the stack.


# STEP 4: SUMMARY
#
# 1. The function starts with sum_numbers(4).
#
# 2. Each recursive call decreases n by 1.
#    4 → 3 → 2 → 1 → 0
#
# 3. Each unfinished function call remains
#    on the CALL STACK, waiting for a return value.
#
# 4. When n == 0, the BASE CASE returns 0.
#    This stops further recursive calls.
#
# 5. The CALL STACK follows LIFO:
#    Last In, First Out.
#
# 6. Python resumes the waiting functions
#    in reverse order.
#
# 7. Each function receives the RETURN VALUE
#    from the function it previously called.
#
# 8. That returned value replaces
#    sum_numbers(n - 1) in the calculation.
#
# 9. Each function finishes its calculation,
#    returns its result, and exits the stack.
#
# 10. The calculations are:
#
#     sum_numbers(0) = 0
#     sum_numbers(1) = 1 + 0 = 1
#     sum_numbers(2) = 2 + 1 = 3
#     sum_numbers(3) = 3 + 3 = 6
#     sum_numbers(4) = 4 + 6 = 10
#
# FINAL OUTPUT: 10
#
#
# IMPORTANT CONCEPTS:
#
# RECURSION = A function calling itself.
#
# BASE CASE = The condition that stops recursion.
#
# CALL STACK = Memory structure that keeps track
#              of active function calls.
#
# LIFO = Last In, First Out.
#
# PUSH = A new function call is added to the stack.
#
# POP = A completed function call leaves the stack.
#
# RETURN VALUE = The result passed back to
#                the function that made the call.
#
# GOING DOWN = Recursive calls are added to the stack.
#
# GOING UP = Functions resume, calculate, return
#            their values, and leave the stack.
#
# REMEMBER:
# The functions DO NOT call themselves again going up.
# They resume their unfinished calculations.