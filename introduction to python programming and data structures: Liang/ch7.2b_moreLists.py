############################################################
# Shifting Left
############################################################

# Create a list
myList = [1, 2, 3, 4, 5, 6, 7]

# Save the first element before it gets overwritten
temp = myList[0]

# Display the original list
print(myList)

# Loop through every index in the list
for i in range(1, len(myList)):

    # It's 1 because when i = 0:
    # range(0, len(myList))
    # myList[i - 1] becomes myList[-1]
    # Remember:
    # myList[-1] means the LAST element in the list.

    # The first value in range() is the first value assigned to i.
    # Example: range(7, 10) assigns i = 7, then 8, then 9.

    # First iteration (i = 1):
    # myList[0] = myList[1]
    #
    # Before:
    # [1, 2, 3, 4, 5, 6, 7]
    #
    # After:
    # [2, 2, 3, 4, 5, 6, 7]
    #
    # That's why the loop starts at 1 instead of 0.

    myList[i - 1] = myList[i]

# Put the original first element at the end of the list.
# We saved it in temp because myList[0] was overwritten during the shift.
# Without temp, the original first value would be lost forever.
myList[len(myList) - 1] = temp

# Display the modified list
print(myList)

###################################################################################################
########### another ex showing months this is to show how to think since elements start at 0
###################################################################################################

myListMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
cin = eval(input("Enter the number of the Month: "))

print("the monthe represented by the number you enteres is: ",myListMonths[cin -1])