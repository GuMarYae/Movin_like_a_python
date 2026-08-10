matrix = [
    [1, 2, 3],        # row 0, length = 3
    [4, 5, 6],        # row 1, length = 3
    [7, 8, 9, 10]     # row 2, length = 4
]


# len(matrix) = 3 because there are 3 ROWS.
#
# range(3) gives: 0, 1, 2
#
# Python:
# for row in range(len(matrix))
#
# Think C++:
# int row = 0; row < 3; row++
#
# Python basically hides the starting at 0
# and the ++ because range() handles the counting.

#   row = 0, less than 3, i++
for row in range(len(matrix)):


    # len(matrix[row]) = length of CURRENT row.
    #
    # row 0 → range(3) → column = 0, 1, 2
    # row 1 → range(3) → column = 0, 1, 2
    # row 2 → range(4) → column = 0, 1, 2, 3
    #
    # Think C++:
    # int column = 0;
    # column < matrix[row].size();
    # column++

    for column in range(len(matrix[row])):


        # First [] = row
        # Second [] = column
        #
        # matrix[0][0] = 1
        # matrix[1][2] = 6
        # matrix[2][3] = 10
        #
        # end=" " keeps values on the SAME line.

        print(matrix[row][column], end=" ")


    # Column loop finished.
    # Move to a new line for the next ROW.

    print()


# OUTPUT:
#
# 1 2 3
# 4 5 6
# 7 8 9 10