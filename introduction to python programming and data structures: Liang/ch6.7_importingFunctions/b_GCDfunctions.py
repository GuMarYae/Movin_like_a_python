# Import only the gcd() function from the module named a_GCDfunctions.
# This is similar to saying:

# import a_GCDfunctions
# and then calling:
# a_GCDfunctions.gcd(...)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# Think of it like an object:
# object.function()
# module.function()
#
# Since we imported only the gcd() function, we can call gcd()
# directly without writing a_GCDfunctions.

from a_GCDfunctions import gcd


def main():
    # Ask the user for the first integer.
    number_one = int(input("Enter the first integer: "))

    # Ask the user for the second integer.
    number_two = int(input("Enter the second integer: "))

    # Call the imported gcd() function and display the result.
    # We do NOT write:
    # a_GCDfunctions.gcd(number_one, number_two)
    # because we imported the function itself.
    print("The GCD is", gcd(number_one, number_two))


# Start the program by calling the main() function.
main()