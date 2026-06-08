limit = 100          # Number we are comparing against

pos = 0              # Start at the first position (index 0)

found = False        # We have not found a matching value yet

values = [12, 99.99, 645, 86, 242, 64564, 23423, 5]

# Index : Value
#   0   : 12
#   1   : 99.9
#   2   : 645 ==> after the loop finds this value, its going to print the index number 2, 
#         which is the position of the value 645, which is greater than the limit of 100
#         the loop will then terminate
#   3   : 86
#   4   : 242
#   5   : 64564
#   6   : 23423
#   7   : 5

# Keep looping while we are inside the list
# and have not found a matching value
while pos < len(values) and not found:

    # Check if the current value is greater than limit
    if values[pos] > limit:

        found = True     # We found a value greater than limit

    else:

        pos = pos + 1    # Move to the next position in the list

# After the loop ends, check if we found a match
if found:

    print("Found at position:", pos)   # Print where it was found

else:

    print("Not found")     
    
######################### Removing Matches ####################################
    
words = ["Welcome", "to", "the", "island"]

for i in range(len(words)):      # Loop through each index
    word = words[i]              # Get the word at index i

    if len(word) < 4:            # Remove only if length is LESS than 4
                                 # len = 2 -> removed
                                 # len = 3 -> removed
                                 # len = 4 -> NOT removed
                                 # len = 5+ -> NOT removed
                                 # Because < means "strictly less than"
                                 # If it were <= 4, then length 4 would be removed too

        words.pop(i)             # Remove the word at index i# No value greater than limit exists