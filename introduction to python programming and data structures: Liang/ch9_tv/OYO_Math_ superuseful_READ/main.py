import OperatorPractice

def main():

    # OperatorPractice = the module
    # Add = the class inside the module
    # Add(50) creates an Add object and automatically calls Add's __init__().
    # a1 now refers to that object, and that object stores 50 in currentObject.__a.
    #
    # Think of Alex Merced's JavaScript explanation:
    # seeing .something usually means we are accessing something that belongs
    # to an object/module/class.
    #
    # OperatorPractice.Add
    #        ^          ^
    #      module      class
    a1 = OperatorPractice.Add(50)

    # Same thing here.
    # This creates a SECOND Add object.
    # a2 refers to this object, which stores -7.
    a2 = OperatorPractice.Add(-7)


    # a1 + a2 uses the + operator between TWO Add objects.
    #
    # Python sees:
    # a1 + a2
    #
    # and automatically calls:
    # a1.__add__(a2)
    #
    # currentObject = a1
    # otherObject   = a2
    #
    # __add__ then gets:
    # currentObject.__a = 50
    # otherObject.__a   = -7
    #
    # 50 + -7 = 43
    print(f"the answer is equal to {a1 + a2}")
    

main()

#now, were gonn import the whole class for main2.py and see if it can be done and if it can , is it better