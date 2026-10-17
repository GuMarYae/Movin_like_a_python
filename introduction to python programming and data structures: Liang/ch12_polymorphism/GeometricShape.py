import math

class GeometricShape:
    # This is a constructor
    # This constructor has default arguments
    # This constructor has private parts 😏
    def __init__(currentObj, color="red", isFilled=False):
        # Private member variables
        currentObj.__color = color; currentObj.__isFilled = isFilled

    def getColor(currentObj):
        # Getters don't assign shit
        # They just return the current value/state of instance variables
        return currentObj.__color

    def isFilled(currentObj):
        return currentObj.__isFilled

    def setColor(currentObj, color):
        currentObj.__color = color

    def setFilled(currentObj, isFilled):
        currentObj.__isFilled = isFilled

    ## IMPORTANT
    # You know how we do:
    # geoShape = GeometricShape()
    #
    # Without __str__, doing:
    # print(geoShape)
    #
    # will print some bullshit like:
    # <__main__.GeometricShape object at 0x...>
    #
    # So we'd normally need something like:
    # print(geoShape.getColor(), geoShape.isFilled())
    #
    # But when we define __str__ below, we can simply do:
    # print(geoShape)
    #
    # Python automatically calls geoShape.__str__()
    # and prints the string that __str__ RETURNS.

    def __str__(currentObjStatus): # this function is so a user can just print the object.. ex. print (geometricObject_1. itll print this below)
                                   # without this itll print: <GeometricShape.GeometricShape object at 0x106916a50> which is unuseful
                                   
        return f"The color is: {currentObjStatus.__color}, and the filled status is: {currentObjStatus.__isFilled}"
    
    #__________________________________ thats it for GeeometricShape: parent, superclass______________________________________
    

        
            