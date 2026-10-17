def main ():

    # makes a tuple with strings in the indexes from 0 - 6
    tuple1 = ("green", "red", "pink", "green", " purple", "orange", "blue")
    print (tuple1)


    # makes a tuple of floats and ints in indexes from 0 - 6
    tuple2 = (0.5,2,3,4,5,6,7)
    print(tuple2)

    # self expainatory
    print(f"the length for tuple 2 is {len(tuple2)} ")


    # prints the max of the tuple2 tuple, the  min and finally, the sum
    print("The max is ", max(tuple2))
    print("the min is ", min(tuple2))
    print("The sum is ", sum(tuple2))

    # Tuples support indexing like lists and arrays, but cannot be modified.

    print("the index for tuple number 2 is ", tuple2[3])
    tuple3 = ("the first two tuples combined is ", tuple1 + tuple2)
    print(tuple3)

    # Slicing [2:4] returns elements at indexes 2 and 3.
    # Index 4 is excluded.
    print(tuple2[2 : 4])

    # prnts the last value because -1 starts from the end
    print(tuple2[-1])


    # sees if 2 is in tuple2
    print(2 in tuple2)


    for v in tuple2:
        print(v, end = " ")


    for v in tuple1:
        print(v, end =" ") # end means NOT to move to a new line after printing
    print() #new line this way

    list1 = list(tuple1)
    tuple4 = tuple(list1)
    tuple5 = tuple(list1)
    print(tuple4)
    print(tuple4 ==tuple5)

       ######## my random stuff ###########

    # TUPLES ARE IMMUTABLE (CANNOT BE MODIFIED AFTER CREATION)
    #
    # 1. You CANNOT change an individual element in a tuple.
    # 2. You CANNOT add elements directly to an existing tuple.
    # 3. You CANNOT remove individual elements from a tuple.
    #
    # HOWEVER:
    # 4. You CAN create an empty tuple.
    # 5. You CAN assign a completely new tuple to the same variable.
    # 6. You CAN combine tuples to create a new tuple.
    # 7. You CAN convert a tuple into a list to modify its elements.
    #
    # IMPORTANT: You cannot reassign an element inside a tuple,
    # but you CAN reassign the variable itself to a new object.

    tuple6 = ()                  # Create an empty tuple
    tuple6 = tuple()             # Also Create an empty tuple
    tuple6 = (10, 20, 30)        # Assign a new tuple
    tuple6 = tuple6 + (40,)      # Create a new tuple containing 40

    print(tuple6)                # (10, 20, 30, 40)

  ###############################################################
      ######## GENERATOR EXPRESSION VS. LIST COMPREHENSION ########

        # EXAMPLE 1: GENERATOR EXPRESSION ()
    # Creates a generator, NOT a tuple.
    # Uses a for loop to iterate through the specified range automatically.
    # 💥 Behaves like yield, producing one value at a time when requested.
    # Each x is multiplied by 2, starting at x = 1 and ending at x = 98.
    # Uses less memory because values aren't all stored at once.
    #
    # WHAT TO WATCH OUT FOR:
    # 1. You cannot access values using indexes like tuple7[0].
    # 2. Printing the generator directly won't display its numbers.
    # 3. Once you consume all its values, the generator is exhausted.
    # 4. Parentheses () do NOT automatically mean you're creating a tuple.
    # 5. The generator does NOT execute all iterations immediately.
    # 6. Each requested value advances the loop to the next iteration.
    # 7. range(1, 99) excludes 99, so the last x is 98.
    # 8. The highest result is 196 because 2 * 98 = 196.

    tuple7 = (2 * x for x in range(1, 99))
    print(list(tuple7))  # Produces all remaining values and displays them as a list.

    # tuple 7 might look like tuple9 but tuple 9 has tuple() as the layout
    # this one is tuple = (x for x in range())
    tuple7 = (2 * x for x in range(1, 99)) 
    print(list(tuple7))  # Converts generator values into a list for display


    # EXAMPLE 2: LIST COMPREHENSION []. 🔥 this one is the examole from the book page 474
    # Creates a list, NOT a generator or tuple.
    # Generates and stores all values immediately.
    # Uses more memory because it stores every value.
    #
    # WHAT TO WATCH OUT FOR:
    # 1. Large lists can consume more memory.
    # 2. You CAN access values using indexes like tuple8[0].
    # 3. You CAN modify, add, or remove elements.
    # 4. Adding parentheses around [] does NOT create a tuple.

    # this creates a list and stores the numbers in indexes as values
    # this one is tuple = ([x for x in range()]) the added [] makes the big diffeence
    tuple8 = ([2 * x for x in range(1, 99)])
    print(tuple8)        # Displays all the values stored in the list
    print(tuple8[0])     # Displays the first element in the list (2)


    # EXAMPLE 3: TUPLE CREATED FROM A GENERATOR
    # Converts the generated values into an actual tuple.
    # Stores all values immediately.
    #
    # WHAT TO WATCH OUT FOR:
    # 1. You CAN access elements using indexes.
    # 2. You CANNOT change, add, or remove individual elements.
    # 3. You CAN reassign the variable to a completely new tuple.

    ## tuple = tuple(x for x in range(1, 99)) the difference is the word tuple --->. | tuple9 = tuple() |
    tuple9 = tuple(2 * x for x in range(1, 99))
    print(tuple9)        # Displays all the values stored in the tuple
    print(tuple9[0])     # Displays the first element in the tuple (2)
    
    #############################################################################################
    ######## 1. GENERATOR: LONGER VERSION ########

    def generateNumbers():
        for x in range(1, 99):
            yield 2 * x # yield produces one value at a time, pauses the function, and resumes at the next iteration when requested.

    tuple7 = generateNumbers()

    print(list(tuple7))


    ######## 2. LIST COMPREHENSION: LONGER VERSION ########

    tuple8 = []

    for x in range(1, 99):
        tuple8.append(2 * x)

    print(tuple8)
    print(tuple8[0])


    ######## 3. TUPLE: LONGER VERSION ########

    numbers = []

    for x in range(1, 99):
        numbers.append(2 * x)

    tuple9 = tuple(numbers)
    
    ###############
    # tuple7 = (2 * x for x in range(1, 99))       # Generator: yield-like behavior

    # tuple8 = ([2 * x for x in range(1, 99)])     # List: NO yield behavior

    # tuple9 = tuple(2 * x for x in range(1, 99))  # Tuple: NO yield behavior in the final result
    ###############

    print(tuple9)
    print(tuple9[0])
    
main()