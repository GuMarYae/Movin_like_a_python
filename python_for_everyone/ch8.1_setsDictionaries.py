## 💥 If you want to print each color on its own line, then yes, you need a for loop:
## 💥 In node.js and python If you just want to print the whole list at once, you can just print a list
## java and cpp, you almost always need a for loop to print each element

#lists can have duplicates
myList = ["red", "yellow", "pink","pink", "green", "purple","purple", "orange", "blue"]
for color in myList:
    print(color)

#dont need this.im just tryna get use to it
print(end = " ")

#the set removes the dupicate colors, 
#but puts them out of order by default
mySet = set(myList)

## Sort it back into a list.
#THE ORDER DOESNT EVER GO BACK INTO WHAT WAS CREATED BEFORE
#it goes into alphabetical order
myList = sorted(mySet)
print("myList: ", myList)

####################################################################
########################set from scratch############################
####################################################################
# notice, when making a set, you need curly brackets not square brackets
#also notice , when printing a set, it still removes duplicates and doesn't maintain the original order
mySet_two = {"red", "yellow", "pink","pink", "green", "purple","purple", "orange", "blue"}
print("mySet_two: ", mySet_two)

mySet.add("black")
print("mySet: ", mySet)
mySet.remove("blue")
print("mySet: ", mySet)
# Add an item
mySet.add("white") 

# Remove an item (error if it doesn't exist)
mySet.remove("white")
print("mySet: ", mySet)

# Remove an item (no error if it doesn't exist)
mySet.discard("pink")
print("mySet: ", mySet)

# Remove and return a random item
print("Popped item: ", mySet.pop())
print("mySet: ", mySet)


#store popped items in a variable
popped_item = mySet.pop()
print("Popped item: ", popped_item)
print("mySet: ", mySet)

#if you want to store popped items in a list you neeed to make a popped_items list
poppedItemsList = []
poppedItemsList.append(mySet.pop())
print("poppedItemsList: ", poppedItemsList)
print("myset: ", mySet)

# Remove everything
mySet.clear()
if (len(mySet) <= 0):
    print("damn, gang! You dont have shyt in your set. You worse than dipset: ", mySet, "! \n If it said \"set()\" then you dont have anything in your set") 

# Number of items
len(mySet)
print("Number of items in mySet: ", len(mySet))

# Check if an item exists
##💥💥💥 boolean
"green" in mySet
print("Is 'green' in mySet: ", "green" in mySet)

## we're gonna append some stuff in the set
## or, just re-set the myList. myList was never affected
mySet = set(myList)
mySet.add("indigo")
print("mySet: ", mySet)
#re check ig green is in the set now
print("Is 'green' in mySet: ", "green" in mySet)


# Copy a set
copySet = mySet.copy()

# Combine two sets
mySet.union(mySet_two)

# Keep only common items
mySet.intersection(mySet_two)

# Keep only items different from the other set
mySet.difference(mySet_two)

# Is one set contained in another?
mySet.issubset(mySet_two)

# Does one set contain another?
mySet.issuperset(mySet_two)


####################################################################
########################dictioary###################################
####################################################################
# an empty dictionary
myDictionary = {}
# a dictionary
contacts = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9012", "jimmy": "555-1234"}


# A dictionary is NOT a list or an array.
# It stores data as key-value pairs instead of indexes.
# You use the key to get the value.
# Behind the scenes, Python hashes the key to quickly find the value.
# Think: Key -> Hash -> Value


# duplicate contacts dictionary
myDictionary = dict(contacts)
print("The number for Alice is", myDictionary["Alice"])

print("the dictionary: list ", myDictionary)
## in this order key, hash value
print("the number for alice is", contacts["Alice"]  )

#adding a new contact
myDictionary["john"] = "222-2224"
print("the dictionary: list ", myDictionary, '\n', "the contacts are ", contacts)
## so even though dictionary is a duplicate/copy of contacts, john only goes to dictionary
# change a value
myDictionary["john"] = "222-1113"
print("the dictionary: list ", myDictionary)

#another empty dictionary
colors = {}

# how to add to a dictionary
colors["sharks"] = "grey"
colors["sharks2"] = "greyer"
colors["killer whale"] = "black and white"
colors["tigers"] = "orange and black"
print("the colors: list ", colors)

# remove
colors.pop("sharks2")
print("the colors: list ", colors)

################ the common methods used in dictionaries#################

# Number of key-value pairs
len(myDictionary)

# Get a value by its key
myDictionary["Alice"]

# Safer way to get a value
myDictionary.get("Alice")

# Add or update a key-value pair
myDictionary["David"] = "555-7777"

# Remove a key-value pair
myDictionary.pop("Bob")

# Remove the last inserted key-value pair
myDictionary.popitem()

# Remove everything
myDictionary.clear()

# Make a copy
copyDictionary = myDictionary.copy()

# Check if a key exists (Boolean)
"Alice" in myDictionary

# Get all keys
myDictionary.keys()

# Get all values
myDictionary.values()

# Get all key-value pairs
myDictionary.items()

otherDictionary = {"Eve": "555-3333", "Frank": "555-4444"}

# Update one dictionary with another
myDictionary.update(otherDictionary)
print("the dictionary is updated to: ", myDictionary)