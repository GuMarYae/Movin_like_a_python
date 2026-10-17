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

    def __str__(currentObjStatus):
        return f"The color is: {currentObjStatus.__color}, and the filled status is: {currentObjStatus.__isFilled}"
    
    #__________________________________ thats it for GeeometricShape: parent, superclass______________________________________
    
class Circle(GeometricShape):  ## using the parent ###############
   
    def __init__(currentObj, radius = 1):
   
        # enable the parents privates: def __init__(currentObj, color="red", isFilled=False):
        super().__init__()  
        # circles privates
        currentObj.__radius = radius
        
        # getters #############################
    def getRadius(currentObj):
            return currentObj.__radius
        
    def getArea(currentObj): # we never needed area ar a member variable because 
        return currentObj.__radius **2 * math.pi
        
    def getDiameter(currentObj):
        return 2 * currentObj.__radius
        
    def getPerimeter(currentObj):
        return 2 * currentObj.__radius * math
        
        # setter ################################
    def setRadius(currentObj, radius):
        currentObj.__radius = radius
            
       # function ###############################
    def printCircle(currentObj):
    # Not required, just a convenient way to print all Circle info together
    # __str__() gets color + filled from the parent
    # __radius gets the radius from Circle
    # This saves us from having to print each value separately
        print(currentObj.__str__() + " radius: " + str(currentObj.__radius))
        
        ## so you can put classes in one module but ow im gonna show how to have a separate class file
        ## to import classes from here, like GeometeriObject and use it as a parent
        
        
            