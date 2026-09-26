data = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# data[1][0][0]
#
# First [1]:
# data[1] = [[5, 6], [7, 8]]
#
# Second [0]:
# data[1][0] = [5, 6]
#
# Third [0]:
# data[1][0][0] = 5
#
# Each [] goes one level deeper into the nested list.

print(data[1][0][0])  # 5

########################################################################
##################### another problem ##################################
########################################################################


points = [
    [1, 2],
    [3, 1.5],
    [0.5, 0.5]
]

# .sort() sorts the INNER lists by looking at
# the FIRST value of each list first.
#
# First values:
#
# [1, 2]     → 1
# [3, 1.5]   → 3
# [0.5, 0.5] → 0.5
#
# Python compares:
# 0.5, 1, 3
#
# So the order becomes:
#
# [0.5, 0.5]
# [1, 2]
# [3, 1.5]
#
# It DOES NOT need to look at 1.5 because
# the first values already determine the order.

points.sort()

print(points)

# Output:
# [[0.5, 0.5], [1, 2], [3, 1.5]]


####################################################
################### another problem ################

data = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]


def ttt(m):

    # We call ttt(data[0])
    #
    # data[0] is:
    # [[1, 2], [3, 4]]
    #
    # So m becomes:
    # [[1, 2], [3, 4]]

    v = m[0][0]

    # m[0] = [1, 2]
    # m[0][0] = 1
    #
    # So:
    # v = 1


    # Go through each row:
    #
    # First row  = [1, 2]
    # Second row = [3, 4]

    for row in m:

        # Go through each number in the current row
        for element in row:

            # If v is smaller than element,
            # replace v with the bigger number

            if v < element:
                v = element

            # v changes like this:
            #
            # 1 < 1 → False → v = 1
            # 1 < 2 → True  → v = 2
            # 2 < 3 → True  → v = 3
            # 3 < 4 → True  → v = 4


    # Return the largest number found
    return v


print(ttt(data[0]))

# OUTPUT:
# 4