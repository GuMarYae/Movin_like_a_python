numberMax = 1000

# With Python, you have to use range() to increment numbers.
# Just say to yourself, "for a number in the range of some other number."
# range() is a built in function.
for number in range(numberMax):
    print(number)

# Notice it went up to 999 instead of 1000.
# That's because range() starts at 0 by default and stops
# BEFORE the ending number. The ending number is NOT included.


#starting at 2
#max value of numberMax
#increment in increments of 5

for number in range(2, numberMax, 5):
    print(number)
    
    
    
# miltiplication table

print ("      Multiplication table")
# display numbers but you have to space first for the numbers on top
print("   ", end = "")
# new empty line
print()
# make the numbers 1 through 10

for i in range(1, 11):
    # you can spresd the empty space  " ", like "     ", etc instead od adding " " + " 
    print(i,"|", "  ", end = "")
    for j in range(1, 11):
        print(f"{j * i: 4d}", end = "")
    print()