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


# 🔥 IMPORTANT:
#
# "for row in matrix" goes through EACH row:
#
# [23, 44, 12]       -> len(row) = 3
# [12, 17, 1, 100]   -> len(row) = 4
# [217, 777, 18]      -> len(row) = 3
#
# So this part:
#
# len(row) for row in matrix
#
# produces:
#
# 3, 4, 3
#
# Then max() grabs the BIGGEST number:
#
# max(3, 4, 3) = 4
#
# This means we DO NOT have to manually write:
#
# maxColumns = 4
#
# Python figures out the maximum number of columns
# automatically based on the longest row.
#
# If the matrix changes and another row becomes longer,
# maxColumns will automatically change too.


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

    # Reset total to 0 for EACH new column.
    #
    # column 0 gets its own total
    # column 1 gets its own total
    # column 2 gets its own total
    # column 3 gets its own total

    total = 0


    # len(matrix) = 3 because there are 3 rows.
    #
    # range(3) -> 0, 1, 2
    #
    # This lets us check the current column
    # against every row.

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

            # If the column EXISTS in this row,
            # grab that value and add it to total.
            #
            # Example for column 0:
            #
            # matrix[0][0] = 23
            # matrix[1][0] = 12
            # matrix[2][0] = 217
            #
            # total = 23 + 12 + 217
            # total = 252

            total = total + matrix[row][column]


    # The row loop is finished.
    # We now have the complete total for this column.

    print("total sum for column:", column, "is", total)