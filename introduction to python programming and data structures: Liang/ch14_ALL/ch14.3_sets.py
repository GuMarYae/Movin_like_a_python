# sets uses no duplicates, theyre unordered, no idexes ex.  no print(set1[2]), 
# you can mutate them unlike tuples, fast search, set operations (union, intersection, difference etc), 
# unique elements mudt be hashable, like integers, strings


# just like tuples, declaring an empty set
set1 = set()
# HOWEVER:
tuple1 = ()        # Create an empty tuple
tuple2 = tuple()   # Also create an empty tuple
# We're just gonna focus on the the set iin this module
# create set from a list


# so why tf would someone make a set from a list
# to remove duplicates
set2 = set([x  * 2 for x in range(1,11)])
# then you can make the list from a set again to duplicates | list = list(set2) now you have a list that has ni duplicates in the list
# Converts the string into individual characters, including spaces.
# Removes duplicate letters automatically.
# Uses hashing to organize characters, so their printed order is not guaranteed.
set5 = set("Toooony Daanniieellssss")
print(set5)
set6 = set(['t','o','n','y'])
print(set6)

#############################
# subset and superset
s1 = {1,2,3,4,5,6,7}
s2 = {1,2,3,4,5,6,7,8,9,10}

print(s1.issubset(s2))
print(s2.issubset(s1)) #false because s2 has a value(s) that s1 doesnt have

print(s1.issuperset(s2))
print(s2.issuperset(s1))


