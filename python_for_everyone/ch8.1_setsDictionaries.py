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
## or, just re-set the myList. myList was never affcted
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

otherDictionary = {
    "Eve": "555-3333",
    "Frank": "555-4444",
    "Grace": "555-5555",
    "Henry": "555-6666",
    "Isabella": "555-7777",
    "Jack": "555-8888",
    "Karen": "555-9999",
    "Liam": "555-0000",
    "Mia": "555-1111",
    "Noah": "555-2222",
    "Olivia": "555-1212",
    "Peter": "555-3434",
    "Quinn": "555-5656",
    "Rachel": "555-7878",
    "Sam": "555-9090",
    "Taylor": "555-2468",
    "Uma": "555-1357",
    "Victor": "555-8642",
    "Wendy": "555-9753",
    "Xavier": "555-1478",
    "Yasmine": "555-2589",
    "Zach": "555-3690"
}
# Update one dictionary with another
myDictionary.update(otherDictionary)
print("the dictionary is updated to: ", myDictionary)

for key in myDictionary:
    print("the names in this dictionary are : ", key)

for i in range(len(myDictionary)):
    print(i)
    
print("max lengthe is: ",len(myDictionary))

##does not work because dictinaries does not use indexes
# 💥 range() makes i an integer.
# Dictionaries do not use integer indexes, only keys.
# So this gives a KeyError.
##for i in range(len(myDictionary)):
##    print(i,myDictionary[i])

# Dictionaries do NOT use integer indexes like lists.
# enumerate() creates a counting index while looping
# through the dictionary's keys.

for index, key in enumerate(myDictionary):
    print("index:", index, "key:", key)

# enumerate() gives you:
# 1. An index (0, 1, 2, ...)
# 2. The key
# 3. The value associated with that key

for index, (key, value) in enumerate(myDictionary.items()):
    print("index:", index, "key:", key, "value:", value)
    
#############################dictionary methods##################### 
# Get the value associated with the key "Alice".
myDictionary.get("Alice")

# Get all key-value pairs.
# an item is a key and a value
myDictionary.items()

# Get all the keys.
myDictionary.keys()

# Get all the values.
myDictionary.values()

# Update the left dictionary with the contents of another dictionary.
myDictionary.update(otherDictionary)

# Remove the key "Alice" and its associated value.
myDictionary.pop("Alice")

# Remove all key-value pairs from the dictionary.
myDictionary.clear()

# Make a copy of the dictionary.
myDictionary.copy()

############################################################
############### RECAP: STORING POPPED VALUES ################
############################################################

######################## LIST ########################

# Store a popped list item in a variable.
poppedListItem = myList.pop()

# Store a popped list item in another list.
removedList = []
removedList.append(myList.pop())


######################## SET #########################

# Store a popped set item in a variable.
poppedSetItem = mySet.pop()

# Store a popped set item in another list.
removedSetItems = []
removedSetItems.append(mySet.pop())


##################### DICTIONARY #####################

# Store the popped VALUE in a variable.
poppedValue = myDictionary.pop("Alice")

# Store the popped key-value pair in another dictionary.
removedDictionary = {}
removedDictionary["Bob"] = myDictionary.pop("Bob")



###############################################################################
############### RECAP: WHY range() + [i] DOESN'T WORK IN DICTIONARIES #########
############### OR WHY myDictionary[i] DOESN'T WORK ###########################
####################### SAME THING ############################################
###############################################################################

# ❌ WRONG: range() makes i an integer (0, 1, 2, ...).
# Dictionaries use keys ("Alice", "Bob", ...) instead of integer indexes.
for i in range(len(myDictionary)):          # i = 0, then 1, then 2, ...
    print(myDictionary[i])                  # Looks for integer keys 0, 1, 2...
                                            # But the dictionary's keys are strings like "Alice", "Bob", ...
                                            # Since keys 0, 1, 2 don't exist, Python raises a KeyError.


# ✅ RIGHT: Loop directly through the dictionary.
# i becomes each key instead of an integer.
for i in myDictionary:                      # i = "Alice", then "Bob", then "Charlie", ...
    print(i)                                # Prints the current key.
    print(myDictionary[i])                  # Uses the current key to get its matching value.


# ✅ RIGHT: Use range() only when you need a counter.
for i in range(len(myDictionary)):          # i = 0, then 1, then 2, ...
    print(i)                                # Prints only the counter, not dictionary values.


# ✅ BEST: Use enumerate() when you want both a counter and the dictionary's keys.
for index, key in enumerate(myDictionary):  # index = 0,1,2...   key = "Alice","Bob","Charlie",...
    print(index, key)                       # Prints both the counter and the key.
    
