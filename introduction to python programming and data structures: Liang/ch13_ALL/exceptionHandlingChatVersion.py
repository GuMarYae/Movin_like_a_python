
# 💥 EXCEPTION HANDLING PRACTICE

# PURPOSE:
# Prevent the program from crashing when a user
# enters invalid numbers or tries to divide by zero.
1
def main():

    try:
        # Ask the user to enter two numbers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Divide the first number by the second
        result = num1 / num2

        print("Result:", result)

    except ValueError:
        # Runs if the user enters something that
        # cannot be converted into an integer.
        # Example: entering "hello" instead of 10.
        print("Error: You must enter valid integers!")

    except ZeroDivisionError:
        # Runs if the user attempts to divide by zero.
        # Example: 10 / 0
        print("Error: You cannot divide by zero!")

    else:
        # Runs ONLY if no exception occurred.
        print("Calculation completed successfully!")

    finally:
        # Runs whether an exception occurred or not.
        print("Program finished.")


main()  # Execute the program
