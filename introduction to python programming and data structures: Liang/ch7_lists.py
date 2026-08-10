import random

list = [] #one way
list.append(7)
list.append(11)
print(list)

list2 = [8,9,10,11]
print(list2)

list3 = ["red, " "green"]
print(list3)
#################################
def slogan():
    slogan1 = "myyyyyyYYY NIGGAAAA"
    return slogan1
    
list4 = [1, "hi",(slogan())]
print(list4)
#################################

list5 = "abcde"
print (list5)
print(list5[2])

list6 = 'a', 'b', 'c'
print(list6)

list7 = [1, 2, 3, 4]
print(sum(list7))

randomNums = random.shuffle(list7)                                                     
print(randomNums)
 

print("is the number 2 in the list: ",2 in list7)


#_____________separate each input_________________________

# Create an empty list to store the numbers
myList8 = []

# Ask the user to enter numbers separated by spaces
# Example input: 1 2 3 4 5
s = input("Enter some numbers followed by spaces: ")

# split() creates a list by separating the string wherever it finds a space
#🔥 again this creates an actual list 🔥
items = s.split()

############################################################
# EXAMPLE 1: CREATE A LIST FROM USER INPUT USING split()
############################################################

# Create an empty list
myList8 = []

# Ask the user to enter numbers separated by spaces
# Example input:
# 1 2 3 4 5
s = input("Enter some numbers followed by spaces: ")

# split() creates a NEW list by splitting the string at each space
# items is now:
# ["1", "2", "3", "4", "5"]
items = s.split()


############################################################
# EXAMPLE 2: CONVERT A LIST OF STRINGS INTO A LIST OF FLOATS
############################################################

# Loop through each string in the items list
# Convert each string to a float
# Store each float in the myList8 list
for x in items:
    myList8.append(float(x))

# Display the completed list
print(myList8)   



