# ===========================================================
# Example 1: while randomNumber > 0
# ===========================================================

import random

randomNumber = random.randint(1,1000)

print("Enter a number from 1 to 1000 ")

# This loop keeps running because randomNumber never changes.
# It only stops when the break statement is executed.
while randomNumber > 0:
    
    userNumber = int(input(""))
    
    if userNumber > randomNumber:
        print("too big")
        
    else:
        if userNumber < randomNumber:
            print("too small")
            
        # If else and print are on the same line,
        # Python allows ONLY ONE statement after the colon.  
        # else: print("got it")
        
        # This is equivalent to:
        #
        # else:
        #     print("got it")
        #
        # Since break is a second statement, it MUST be indented
        # underneath else. Otherwise, it executes after the if/else
        # block and ends the loop every time. so the  else: print("got it") wont work. it has to be indented after else:
        else:
            print("got it")
            break


# ===========================================================
# Example 2: while True
# ===========================================================

randomNumber = random.randint(1,1000)

print("Enter a number from 1 to 1000 ")

# Loop forever until the break statement is executed.
# This is the standard way to write an infinite loop.
while True:
    
    userNumber = int(input(""))
    
    if userNumber > randomNumber:
        print("too big")
        
    else:
        if userNumber < randomNumber:
            print("too small")
            
        else:
            print("got it")

            # Ends the infinite loop once the correct number is guessed.
            break


# ===========================================================
# Example 3: while True with elif
# ===========================================================


randomNumber = random.randint(1,1000)

print("Enter a number from 1 to 1000 ")

# Loop forever until the break statement is executed.
# elif removes the need to nest another if statement.
while True:
    
    userNumber = int(input(""))
    
    if userNumber > randomNumber:
        print("too big")

    # Runs only if the first if statement is False.
    elif userNumber < randomNumber:
        print("too small")

    # Runs only if both previous conditions are False.
    # This means the numbers are equal.
    else:
        print("got it")

        # Ends the infinite loop once the correct number is guessed.
        break