#in order to get random, you always want to import random
import random

number = random.randint(0, 1000)
count = 0


print("Enter a number from 1 to 1000, gang: ")

while number >= 0:
    
    storedNumber = int(input("enter number: "))

    if storedNumber == number:
        print("Good shyt")
    elif storedNumber < number:
        print("Number is too small, gang. Enter another one: ")
    else: print("Too big")
    break
        
