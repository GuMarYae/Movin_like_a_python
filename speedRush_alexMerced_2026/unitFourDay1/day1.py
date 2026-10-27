import random

# while loop
counter = 0 # this means counter is false, remember 0 and false are true be be false

while counter < 101:
    if counter == 0:
          #print ("This has printed")
          counter += 1
    elif counter == 1: print(print ("This has printed", counter, "time so far")); counter+=1
    elif (counter > 0): print ("This has printed", counter, "times");  counter += 1
    
#array he calls is an array
print("###############################")

for i in [1,2,3,4,5,6,7,8,9]:
    print(i)
print("###############################")

for j in range(1, 100):
    print(j)
print("###############################")

for k in range(2,200,10):
    print(k)
            

# DIFFERENCE BETWEEN A LIST AND A TUPLE
#
# LIST []:
# - Mutable: You can add, remove, or change elements.
# - Uses square brackets [].
#
# TUPLE ():
# - Immutable: You cannot add, remove, or change elements.
# - Uses parentheses ().
#
# IMPORTANT:
# Both behave the SAME in a for loop because both are iterable.
# The loop visits each element individually.
# Neither automatically generates numbers between 1 and 100.


# 1. LIST []
for j in [1, 100]:
    print(j)

# Output:
# 1
# 100


# 2. TUPLE ()
for j in (1, 100):
    print(j)

# Output:
# 1
# 100


# 3. EXAMPLE OF THEIR DIFFERENCE

# LIST: Can be modified
numbers = [1, 100]
numbers[0] = 50
print(numbers)  # [50, 100
  
print("###############################")

# 10 minute challengs
for i in range(11):
    if i % 2 == 0:
        print (i," Its even")
    elif i % 2 != 0 and i % 3 == 0:
        print(i," Meow")
      
counter = 12  
while counter <= 30:
     if counter % 2 == 0:
            print (counter," Its even")
     elif counter % 2 != 0 and counter % 3 == 0:
            print(counter," Meow")
     counter += 1
   
   
# Array length

myArr = [0,1,2,3,4,5,6,7,8,9,0,11]

print("The length of this array is", len(myArr))

myArr.pop()
myArr.append("whyy")
print(len(myArr))


#reverse string 2:43. 

def reverseString(word):
   reverseWord = list(word) #Since you cant reverse a string, this, turns the string into an array or a list
   print(reverseWord)
   reverseWord.reverse()
   print(reverseWord)
   stringWord = " ".join(reverseWord)
   return ((stringWord))
   

   
print(reverseString("wowzers"))

### calculator

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
             return(" you cant divide that shyt")
    if operator == "//":
        if num2 != 0:
            return num1 // num2
        else:
            return(" you cant divide that shyt")
         
         
print(calculator(32, 54, "+"))
print(calculator(32, 54, "-"))
print(calculator(32, 54, "*"))
print(calculator(32, 54, "/"))
print(calculator(32, 54, "//"))

print(calculator(32, 0, "/"))
print(calculator(32, 0, "//"))

high = 100
low = random.random()

def ranDumb(low, max):  
    random.randrange(low, max)
    while random.randrange(low, max) != 0:
        print("Zero aint found")
        return random.randrange(low, max) 
    return("a Zero was found")

print(ranDumb(0, 122))

##############. were gonna do a list again for the hell of it

userInput = (input("enter some letters: "))
value = str(userInput)
myList = []
myList.append("tony")
print(myList)

for i in userInput:
    myList.append(i)
print(myList)
finalPhrase = " ".join(myList)  
print(finalPhrase)

#############################filtering #################################

# Takes a list and a callback function
def myFilter(arr, callback):

    # Store numbers that pass the condition
    newArr = []

    # Start at the first index
    index = 0

    # Loop through the entire list
    while index < len(arr):

        # Get the current number from the list
        item = arr[index]

        # AT 3:05 explaination
        # callback refers to the function passed in (isEven).
        # Parentheses invoke isEven(item, index).
        # If it returns True, execute the if statement.
        if callback(item):

            # Add the number if the condition is True
            newArr.append(item)

        # Move to the next index
        index += 1

    # Return the completed filtered list
    return newArr


# Check if a number is even
def isEven(item):

    # Return True if even, False if odd
    # index is accepted but not used
    return item % 2 == 0


# Lambda version: pass an unnamed function
print(myFilter([1,2,3,4,5,6,7,8,9], lambda item: item % 2 == 0))


##### or just make a damn function

# Pass isEven WITHOUT parentheses (which   means, not executed yet).
# myFilter receives isEven through callback, as a REFERENCE -> THINK OF IT AS A POINTER THATS GONNA BE USED LATER, WHEN ITS CALLED.
# callback(item, index) executes isEven later.  
print("Understandable way: ",myFilter([1,2,3,4,5,6,7,8,9], isEven))


###################### heres an easier example of a callback #############################

# Callback function that receives True or False
def sayHi(condition):

    # If condition is True, print Hi
    if condition:
        print("Hi")


# Addition function that receives two numbers and a callback
def addition(a, b, callback):

    # Add the two numbers and store the result
    result = a + b

    # Check if result is greater than 0
    # Pass True or False into the callback
    # callback(...) invokes sayHi(...)
    callback(result > 0) # this is basically saying     callback(True) remember almost everything in coding is 
                         # supposed to result into being true
    
    # Return the addition result
    return result


# Pass sayHi as a reference (without parentheses)
# addition will invoke it later through callback
print(addition(5, 3, sayHi))



############## USING A DICTIONARY ##############

# Create a function that takes a name and age
def makePerson(name, age):

    # Create a dictionary with name and age as keys
    # Store the arguments as their values
    person = {"name": name,
              "age": age}

    # Return the dictionary
    return person


###### Another way: Return the dictionary directly
def makePerson2(name, age):

    # Create and return the dictionary in one line
    return {"name": name, "age": age}


# Ask the user for their name
userName = input("Statcha name, Ock: ")

# Ask the user for their age
userAge = input("How old are you: ")


# Call makePerson and pass the user's information
# The function returns a dictionary
print("User name and age is:", makePerson(userName, userAge))


# Another way: Call makePerson2
# Same result, but the function returns the dictionary directly
print("User name and age is:", makePerson2(userName, userAge))





    

   

