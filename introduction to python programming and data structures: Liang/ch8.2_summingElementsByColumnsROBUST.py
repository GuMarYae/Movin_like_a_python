# ROBUST VERSION:
# This can handle rows that have DIFFERENT numbers of columns.

matrix = [[23, 44, 12],
          [12, 17, 1, 100],
          [217, 777, 18]]


# OLD CODE:
# len(matrix[0])
#
# only looked at row 0:
# [23, 44, 12]
#
# That would give us 3 columns and completely miss
# the 100 in row 1 at column 3.
#
# Instead, look at the length of EVERY row:
#
# len(row):
#
# row 0 = [23, 44, 12]       -> 3
# row 1 = [12, 17, 1, 100]   -> 4
# row 2 = [217, 777, 18]      -> 3
#
# max(3, 4, 3) = 4
#
# So maxColumns = 4

# this 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 
maxColumns = max(len(row) for row in matrix)
#      🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 

# range(maxColumns)
# range(4)
#
# column = 0, 1, 2, 3
#
# NOW we will actually reach column 3.

for column in range(maxColumns):

    total = 0

    for row in range(len(matrix)):

        # VERY IMPORTANT:
        #
        # Not every row necessarily HAS the current column.
        #
        # When column = 3:
        #
        # row 0 has indexes 0,1,2       -> NO index 3
        # row 1 has indexes 0,1,2,3     -> YES index 3
        # row 2 has indexes 0,1,2       -> NO index 3
        #
        # So BEFORE doing:
        #
        # matrix[row][column]
        #
        # we ask:
        #
        # "Does this row actually have this column?"
        #
        # Example:
        #
        # column = 3
        # len(matrix[0]) = 3
        #
        # 3 < 3 -> False
        # DON'T access matrix[0][3]
        #
        # len(matrix[1]) = 4
        #
        # 3 < 4 -> True
        # matrix[1][3] exists -> 100

        if column < len(matrix[row]):

            total = total + matrix[row][column]


    print("total sum for column:", column, "is", total)