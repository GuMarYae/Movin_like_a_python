# DICTIONARIES STORE DATA AS KEY: VALUE PAIRS.
#
# THE KEY IS ALWAYS ON THE LEFT SIDE OF THE COLON (:).
# THE VALUE IS ALWAYS ON THE RIGHT SIDE OF THE COLON (:).
#
# FORMAT: dictionary = {key: value}
#
# 💥 KEYS DO NOT HAVE TO BE NUMBERS!
# KEYS CAN BE STRINGS, INTEGERS, TUPLES, OR OTHER HASHABLE TYPES.
# KEYS MUST BE UNIQUE AND HASHABLE.
# VALUES CAN BE DUPLICATED.
#
# 💥 MULTIPLE-CHOICE EXAMPLE:
# WHICH OF THE FOLLOWING STATEMENTS CREATE A DICTIONARY?
#
# A. d = {}                              ✅ VALID — EMPTY DICTIONARY
# B. d = {"john":40, "peter":45}         ✅ VALID — STRING KEYS
# C. d = {40:"john", 45:"peter"}         ✅ VALID — INTEGER KEYS
#
# CORRECT ANSWERS: A, B, AND C.
#
# 💥 EXAMPLE B:
# "john" IS THE KEY, 40 IS THE VALUE.
# "peter" IS THE KEY, 45 IS THE VALUE.
#
# 💥 EXAMPLE C:
# 40 IS THE KEY, "john" IS THE VALUE.
# 45 IS THE KEY, "peter" IS THE VALUE.
#
# 🔥 GOLDEN RULE:
# KEY : VALUE
# LEFT : RIGHT
#
# REMEMBER: {} CREATES AN EMPTY DICTIONARY, NOT AN EMPTY SET!
# TO CREATE AN EMPTY SET, USE set().

# ========================================================================
# 🔥 CHAPTER 14.6 — DICTIONARIES (LIANG TEXTBOOK EXPLAINED SIMPLY)
# ========================================================================

# 💥 14.6 — WHAT IS A DICTIONARY?
#
# A DICTIONARY IS A CONTAINER THAT STORES KEY/VALUE PAIRS.
#
# THINK OF A REAL DICTIONARY:
# THE WORD IS THE KEY.
# THE DEFINITION IS THE VALUE.

definitions = {"apple": "a fruit", "car": "a vehicle"}

# "apple" IS THE KEY.
# "a fruit" IS THE VALUE.
#
# A DICTIONARY IS ALSO CALLED A MAP.
# MAP MEANS A KEY POINTS TO A CORRESPONDING VALUE.
#
# EACH KEY/VALUE PAIR IS CALLED AN ITEM OR ENTRY.
#
# 💥 WHY USE DICTIONARIES?
#
# THEY ALLOW FAST LOOKUPS, UPDATES, AND DELETIONS USING KEYS.

students = {101: "Tony", 102: "John"}

# students[101] RETURNS "Tony".
# YOU DON'T HAVE TO SEARCH THROUGH EVERY STUDENT MANUALLY.

print(students[101])

# 🔥 IMPORTANT:
# LISTS USE INTEGER INDEXES TO ACCESS POSITIONS.
# DICTIONARIES USE KEYS TO ACCESS VALUES.

lst = ["Tony", "John"]

print(lst[0])       # GET THE ELEMENT AT INDEX 0.
print(students[101]) # GET THE VALUE ASSOCIATED WITH KEY 101.

# DICTIONARY KEYS MUST BE HASHABLE.
# THIS GENERALLY MEANS THEIR HASH VALUE CANNOT CHANGE.
#
# STRINGS AND INTEGERS WORK AS KEYS.
# LISTS AND SETS CANNOT BE DICTIONARY KEYS.
#
# A DICTIONARY CANNOT HAVE DUPLICATE KEYS.
# EACH KEY MAPS TO ONE VALUE.


# ========================================================================
# 💥 14.6.1 — CREATING A DICTIONARY
# ========================================================================
#
# USE CURLY BRACES {}.
# EACH ITEM IS WRITTEN AS KEY: VALUE.
# SEPARATE MULTIPLE ITEMS WITH COMMAS.

students = {"111-34-3434": "John", "132-56-6290": "Peter"}

# FIRST ITEM:
# KEY   = "111-34-3434"
# VALUE = "John"
#
# SECOND ITEM:
# KEY   = "132-56-6290"
# VALUE = "Peter"
#
# 💥 EMPTY DICTIONARY:

emptyDictionary = {}

# 💥 EMPTY SET:

emptySet = set()

# REMEMBER:
# {} IS AN EMPTY DICTIONARY.
# set() IS AN EMPTY SET.
#
# VALUES CAN BE STRINGS, NUMBERS, LISTS, OR OTHER OBJECTS.


# ========================================================================
# 💥 14.6.2 — ADDING, MODIFYING, AND RETRIEVING VALUES
# ========================================================================
#
# FORMAT:
# dictionaryName[key] = value

students = {"101": "John", "102": "Peter"}

# 💥 ADDING A NEW ITEM:

students["103"] = "Susan"

# THIS ADDS A NEW KEY/VALUE PAIR.
# KEY = "103"
# VALUE = "Susan"
#
# 💥 MODIFYING AN EXISTING ITEM:

students["101"] = "John Smith"

# SINCE KEY "101" ALREADY EXISTS,
# PYTHON REPLACES ITS OLD VALUE WITH "John Smith".
#
# 💥 RETRIEVING A VALUE:

print(students["103"])

# OUTPUT: Susan
#
# 🔥 IMPORTANT:
# dictionaryName[key] CAN BE USED TO READ OR UPDATE VALUES.
#
# IF THE KEY DOESN'T EXIST WHEN RETRIEVING IT,
# PYTHON RAISES A KeyError.
#
# EXAMPLE OF AN ERROR (LEFT COMMENTED SO THE PROGRAM KEEPS RUNNING):
# print(students["999"])  # KeyError
#
# REMEMBER:
# NEW KEY = ADD A NEW ITEM.
# EXISTING KEY = REPLACE ITS VALUE.


# ========================================================================
# 💥 14.6.3 — DELETING ITEMS
# ========================================================================
#
# FORMAT:
# `del` dictionaryName[key]

students = {"101": "John", "102": "Peter"}

del students["101"]

# THIS REMOVES THE ENTIRE ITEM:
# "101": "John"
#
# RESULT:
# {"102": "Peter"}

print(students)

# 🔥 REMEMBER:
# del REMOVES THE KEY AND ITS ASSOCIATED VALUE.
#
# IF THE KEY DOESN'T EXIST, PYTHON RAISES A KeyError.


# ========================================================================
# 💥 14.6.4 — LOOPING THROUGH DICTIONARIES
# ========================================================================
#
# A for LOOP CAN LOOP THROUGH THE KEYS OF A DICTIONARY.

students = {"101": "John", "102": "Peter"}

for key in students:
    print(key, students[key])

# OUTPUT:
# 101 John
# 102 Peter
#
# 💥 BREAKDOWN:
#
# for key in students:
#     -> EACH ITERATION GIVES YOU A KEY.
#
# students[key]
#     -> GETS THE VALUE ASSOCIATED WITH THAT KEY.
#
# 🔥 REMEMBER:
# LOOPING DIRECTLY THROUGH A DICTIONARY GIVES YOU KEYS.
# USE dictionaryName[key] TO GET EACH KEY'S VALUE.


# ========================================================================
# 💥 14.6.5 — THE len() FUNCTION
# ========================================================================
#
# len(dictionary) RETURNS THE NUMBER OF KEY/VALUE PAIRS.

students = {"101": "John", "102": "Peter"}

print(len(students))

# OUTPUT: 2
#
# 🔥 REMEMBER:
# EACH KEY/VALUE PAIR COUNTS AS ONE ITEM.
#
# THIS IS THE SAME len() FUNCTION YOU USED WITH LISTS,
# TUPLES, STRINGS, AND SETS.


# ========================================================================
# 💥 14.6.6 — CHECKING WHETHER A KEY EXISTS
# ========================================================================
#
# USE in OR not in.

students = {"101": "John", "102": "Peter"}

print("101" in students)      # True
print("999" in students)      # False
print("999" not in students)  # True

# 🔥 IMPORTANT:
# in CHECKS THE KEYS, NOT THE VALUES!

print("John" in students)     # False

# WHY?
# "John" IS A VALUE, NOT A KEY.
#
# REMEMBER YOUR SET LESSON:
# "red" in set1
#
# SAME in OPERATOR, BUT WITH DICTIONARIES
# IT CHECKS WHETHER THE KEY EXISTS.


# ========================================================================
# 💥 14.6.7 — COMPARING DICTIONARIES
# ========================================================================
#
# USE == TO CHECK IF TWO DICTIONARIES CONTAIN THE SAME ITEMS.
# USE != TO CHECK IF THEY ARE DIFFERENT.

d1 = {"red": 41, "blue": 3}
d2 = {"blue": 3, "red": 41}

print(d1 == d2)  # True
print(d1 != d2)  # False

# 💥 WHY ARE THEY EQUAL?
#
# BOTH DICTIONARIES HAVE THE SAME KEYS AND VALUES.
# THE INSERTION ORDER DOES NOT AFFECT EQUALITY.
#
# 🔥 IMPORTANT:
# DICTIONARIES PRESERVE INSERTION ORDER IN MODERN PYTHON,
# BUT THEIR EQUALITY IS BASED ON ITEMS, NOT ORDER.
#
# YOU CANNOT DIRECTLY COMPARE TWO DICTIONARIES
# USING <, >, <=, OR >=.
#
# THESE OPERATORS RAISE A TypeError.


# ========================================================================
# 💥 14.6.8 — DICTIONARY METHODS
# ========================================================================
#
# THE PYTHON CLASS FOR DICTIONARIES IS dict.
#
# REMEMBER:
# METHOD() MEANS YOU ARE CALLING THAT METHOD IMMEDIATELY.

students = {"101": "John", "102": "Peter"}

# 💥 .keys()
# RETURNS A VIEW OF ALL THE KEYS.

print(tuple(students.keys()))

# OUTPUT: ("101", "102")
#
# NOTE: .keys() ITSELF RETURNS A VIEW, NOT A TUPLE.
# tuple() CONVERTS THAT VIEW INTO A TUPLE.


# 💥 .values()
# RETURNS A VIEW OF ALL THE VALUES.

print(tuple(students.values()))

# OUTPUT: ("John", "Peter")


# 💥 .items()
# RETURNS A VIEW OF ALL KEY/VALUE PAIRS.

print(tuple(students.items()))

# OUTPUT: (("101", "John"), ("102", "Peter"))
#
# EACH ITEM IS REPRESENTED AS A (KEY, VALUE) TUPLE.


# 💥 .get(key)
# GETS THE VALUE FOR A KEY.

print(students.get("101"))  # John

# IF THE KEY DOESN'T EXIST:

print(students.get("999"))  # None

# 🔥 IMPORTANT DIFFERENCE:
# students["999"]     -> KeyError
# students.get("999") -> None
#
# YOU CAN ALSO SUPPLY A DEFAULT VALUE:

print(students.get("999", "Not found"))

# OUTPUT: Not found


# 💥 .pop(key)
# REMOVES THE ITEM WITH THAT KEY AND RETURNS ITS VALUE.

print(students.pop("101"))

# OUTPUT: John
#
# THE ITEM "101": "John" IS REMOVED.
#
# 🔥 DIFFERENCE BETWEEN del AND pop():
#
# del students["101"] -> DELETES THE ITEM.
# students.pop("101") -> DELETES AND RETURNS ITS VALUE.
#
# BOTH RAISE KeyError IF THE KEY DOESN'T EXIST,
# UNLESS pop() IS GIVEN A DEFAULT VALUE.


# 💥 .popitem()
# REMOVES AND RETURNS ONE KEY/VALUE PAIR AS A TUPLE.

students = {"101": "John", "102": "Peter"}

print(students.popitem())

# OUTPUT: ("102", "Peter")
#
# 🔥 REMEMBER:
# IN MODERN PYTHON, popitem() REMOVES THE LAST INSERTED ITEM.
# IT IS NOT RANDOM.


# 💥 .clear()
# REMOVES EVERY ITEM FROM THE DICTIONARY.

students.clear()

print(students)

# OUTPUT: {}
#
# 🔥 REMEMBER:
# clear() EMPTIES THE DICTIONARY.
# IT DOES NOT DELETE THE VARIABLE ITSELF.


# ========================================================================
# 🔥 FINAL DICTIONARY CHEAT SHEET
# ========================================================================
#
# {key: value}       -> CREATE A DICTIONARY.
# {}                 -> CREATE AN EMPTY DICTIONARY.
# dict()             -> CREATE AN EMPTY DICTIONARY.
#
# d[key]             -> RETRIEVE A VALUE.
# d[key] = value    