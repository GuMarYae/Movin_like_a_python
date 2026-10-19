def main():  # Defines the main function where our program starts

    # Ask the user for a Fibonacci index, convert the input to an integer,
    # and store that number in the variable 'index'
    index = int(input("Enter index for a Fibonacci number: "))
    
    def fib(theIndex):
  
          # BASE CASE 1: Check whether theIndex equals 0
          if (theIndex == 0):
              return 0  # Return 0 and stop this function call
  
          else:  # Runs if theIndex is NOT 0
  
              # BASE CASE 2: Check whether theIndex equals 1
              # This nested if could also be written using elif
              if (theIndex == 1):
                  return 1  # Return 1 and stop this function call
  
              else:  # Runs if theIndex is neither 0 nor 1
  
                  # RECURSIVE CASE:
                  # Calls fib() twice with smaller index values
                  # fib(theIndex - 1) calculates the previous Fibonacci value
                  # fib(theIndex - 2) calculates the Fibonacci value two positions back
                  # Adds both returned values together
                  # Returns the sum to the function call that requested it
                  return fib(theIndex - 1) + fib(theIndex - 2)  

    # Find and display the Fibonacci number
    # fib(index) calls the fib() function and passes 'index' as its argument
    # The returned Fibonacci value is displayed using print()
    print("The Fibonacci number at index", index, "is", fib(index))


# Defines a separate function named fib()
# 'theIndex' is the parameter that receives the argument passed from fib(index)
    def fib(theIndex):

        # BASE CASE 1: Check whether theIndex equals 0
        if (theIndex == 0):
            return 0  # Return 0 and stop this function call

        else:  # Runs if theIndex is NOT 0

            # BASE CASE 2: Check whether theIndex equals 1
            # This nested if could also be written using elif
            if (theIndex == 1):
                return 1  # Return 1 and stop this function call

            else:  # Runs if theIndex is neither 0 nor 1

                # RECURSIVE CASE:
                # Calls fib() twice with smaller index values
                # fib(theIndex - 1) calculates the previous Fibonacci value
                # fib(theIndex - 2) calculates the Fibonacci value two positions back
                # Adds both returned values together
                # Returns the sum to the function call that requested it
                return fib(theIndex - 1) + fib(theIndex - 2)


# Calls main() to begin executing the program
main()


# look at the other version.. these simply chow indentation of functions in main
# Indent when defining a function INSIDE main().
# Keep the same indentation as def main() when defining a separate function OUTSIDE main().
# When defining a function inside main(), define it before calling it.