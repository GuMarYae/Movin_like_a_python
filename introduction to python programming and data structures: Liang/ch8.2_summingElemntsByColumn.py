# this is to show how to sum by the COLUMN instead of the row., so uts summing from top to bottom
# note: a matrix is just a setup of [[],[],[],[],[]]. plug in the values and then press enter at the beginning of every new row to make a new line

matrix = [[23,44,12],
          [12,17,1],
          [217,777,18]]

globalTotal = 0


for column in range(len(matrix[0])): # range(len(matrix[0])): is [23, 44, 12] = length is 3 so range(0,3):
                                     # which is really saying column = 0, while column < 3 do the thing, then after column ++ (by looking back at that column word) best way to remember these forloops
                                     # column = 0, column < 3, column++, from now on look at the varible word as the only thing that increments
                                     # even if it just says something like "column" everything to the right of that are values that are set in stone
                                     # range(len(matrix[0])) == range(0,3) == range(3) never increments
                                     #
                                     # IMPORTANT WITH RANGE: remember range starts from 0 unless mentioned a starting point in the parens
                                     # range(3) == range(0,3) so it starts at 0
                                     # range(1,3) starts at 1 because you see thats where we wanna start it at
                                     # range(1, len(matrix[0])) starts at 1 because you see thats where we wanna start it at


    total = 0 # total needs to be inside because its summing up each row before the next column is incremented
              # if total was a global variable itll just be ading the sum for all the rows and columns. example: why do you think I made a global total


    for row in range(len(matrix)): # lets do it again: row increments. Thats the purpose. len(matrix) is just a solid number that row cant get to
                                   # range(len(matrix)): while range defaults at starting point of 0, length is counting starting from 1. no matter what language, the length starts from 1. the index coint starts from 0
                                   # so row = 0, row < 3, row++

        total = total + matrix[row][column]
        globalTotal += matrix[row][column]


    print("total sum for column: ", column, "is", total)


print("global total is: ", globalTotal)


# -------------------- IMPORTANT SIDE NOTE --------------------
#
# THIS CODE IS NOT ROBUST IF THE ROWS HAVE DIFFERENT LENGTHS.
#
# len(matrix[0]) ONLY looks at the length of ROW 0.
#
# Example:
#
# matrix = [[1,2,3],
#           [4,5,6,7],
#           [8,9,10]]
#
# len(matrix[0]) = 3
#
# So the column loop only does:
# column = 0, 1, 2
#
# The 7 is at column 3, so it NEVER gets counted.
#
# This code assumes EVERY ROW has the same number of columns.
#
# A more robust version would need to find the longest row
# and check whether each row actually has that column.