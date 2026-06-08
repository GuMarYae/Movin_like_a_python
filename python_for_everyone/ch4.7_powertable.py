COLUMN_MAX = 4          # number of columns in the table
ROW_MAX = 10            # number of rows in the table

#printing the table header
for i in range(1, COLUMN_MAX + 1):   # loop from 1 up to COLUMN_MAX (inclusive)
    # %d = integer, 15 = minimum width of 15 spaces for wide column alignment, end="" prevents newline: we use the \n in cpp
    print("%15d" % i, end="")        # print column header value right aligned in 15 spaces

print()   # move to next line after printing header row

for i in range(1, ROW_MAX +1):       # outer loop controls each row
    for j in range(1, COLUMN_MAX +1):  # inner loop controls each column
        
        #print("%15d" % i**j, end = "")   # exponent using Python power operator
        
        # or ooooor
        print("%15d" % pow(i,j), end = "")  # pow(i, j) raises i to the power of j

    print()   # move to next line after finishing one full row
