# Finds the Greatest Common Divisor (GCD) of two numbers
def gcd(num1, num2):

    # Start with 1 because 1 divides every positive integer.
    # If no larger common divisor is found, the GCD will stay 1.
    gcd = 1

    # Start checking at 2 because we already know 1 is a common divisor.
    # k represents the current number we are testing as a possible GCD.
    k = 2

    # Continue checking while k is less than or equal to BOTH numbers.
    # A divisor cannot be larger than the smaller of the two numbers,
    # so once k passes one of them, there is no reason to keep checking.
    while (k <= num1 and k <= num2):

        # Check if BOTH numbers divide evenly by k.
        # The % operator returns the remainder.
        # If the remainder is 0, then k is a divisor.
        if num1 % k == 0 and num2 % k == 0:

            # Since k divides both numbers, it is a common divisor.
            # We keep updating gcd because k keeps getting larger,
            # so the last value stored will be the greatest one found.
            gcd = k

        # Move on to the next possible divisor.
        k += 1

    # After checking every possible divisor,
    # return the greatest common divisor found.
    return gcd


def main():

    # First number
    number_one = 8

    # Second number
    number_two = 24

    # Call the gcd function and store the returned value.
    result_gcd = gcd(number_one, number_two)

    # Display the greatest common divisor.
    print(result_gcd)


# Start the program by calling main().
main()