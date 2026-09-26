# This shows how to return a two-dimensional list from a function
# and pass that two-dimensional list to another function


def getMatrix():

    matrix = []  # Empty list that will hold all the rows

    numberOfRows = int(input("Enter the amount of rows: "))  # Example: 5

    # If 5 was entered, row will be: 0, 1, 2, 3, 4
    for row in range(numberOfRows):

        # User enters the numbers for the current row
        # Example for row 0: 1 2 3
        # str(row) converts the row number into a string so it can be concatenated
        # with the rest of the string
        s = input("Enter the number for row index " + str(row) + ": ")

        # s.split() turns "1 2 3" into ["1", "2", "3"]
        # float(x) turns each one into 1.0, 2.0, 3.0
        # This creates [1.0, 2.0, 3.0]
        matrix.append([float(x) for x in s.split()])

    # Return the completed two-dimensional list
    return matrix   


def accumulate(m):

    total = 0  # Start the total at 0

    # Go through each row in the two-dimensional list
    for row in m:

        # sum(row) is a built-in FUNCTION that adds the numbers in the row
        # Add that row's sum to total
        total += sum(row)

    # Return the sum of every number in the matrix
    return total


def main():

    # Call getMatrix() and store the returned 2D list in m
    m = getMatrix()

    # Print the entire two-dimensional list
    print(m)

    # Pass the two-dimensional list to accumulate()
    # accumulate() returns the sum of every number
    total = accumulate(m)

    # Print the returned total
    print(total)


main()