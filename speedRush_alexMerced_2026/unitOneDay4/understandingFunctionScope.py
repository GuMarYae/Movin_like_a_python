# ============================================================
# UNDERSTANDING FUNCTION SCOPE IN PYTHON (CLOSURES)
# ============================================================

# A closure allows an inner function to remember variables
# from its outer function, even after the outer function ends.


# STEP 1: CREATE THE OUTER FUNCTION
def outer():

    x = 10  # Local variable belonging to outer()

    # STEP 2: CREATE THE INNER FUNCTION
    def inner():

        # Access x from the outer function's scope
        return x

    # IMPORTANT:
    # Returning inner WITHOUT parentheses means
    # we return the FUNCTION ITSELF, not its value.
    return inner


# STEP 3: CALL THE OUTER FUNCTION
result = outer()

# outer() executes and creates x = 10.
# It then returns the inner function.
#
# result now holds the inner function, NOT 10.


# STEP 4: DISPLAY THE FUNCTION ITSELF
print(result)

# OUTPUT:
# <function outer.<locals>.inner at 0x...>
#
# This displays the function object, not its return value.


# STEP 5: EXECUTE THE INNER FUNCTION
print(result())

# OUTPUT:
# 10
#
# result() executes inner().
# inner() returns x, which is 10.


# ============================================================
# IMPORTANT NOTES
# ============================================================

# 1. FUNCTION SCOPE:
#    Variables created inside a function are normally local.

# 2. NESTED FUNCTION:
#    A function defined inside another function.

# 3. CLOSURE:
#    The inner function remembers variables from its
#    enclosing function, even after that function returns.

# 4. PARENTHESES:
#    result   = Reference to the function itself.
#    result() = Execute the function and get its return value.

# 5. RETURN VALUES:
#    return inner   = Returns the function itself.
#    return inner() = Executes inner and returns its result.

# 6. IMPORTANT:
#    outer() has already finished executing.
#    However, inner() still remembers x = 10.

# THIS IS HOW CLOSURES TAKE ADVANTAGE OF FUNCTION SCOPE.



for i in range(1,19):
    cheese = i
    
print(cheese)


def recurse(limit, number):
    if number == limit:
       return ("we lit")
    else:
       recurse(limit, number+1)
       print ("The limit is: ",limit, " and the number is ",number)
       
        
userNumber = int(input("Enter a number: "))
userLimit = userNumber * 10

print("Your limit is ", userLimit)
recurse(userLimit, userNumber)
    
    
#making default functions

# def sum (x = 50, y = 100):
#     print(x+y)
    

# print("Sum is",sum()," Because its using the defualt arguments")
# print("Sum is",sum(5,10)," Because its using these arguments")