from GeometricShape import GeometricShape
import math

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
        return 2 * currentObj.__radius * math.pi
        
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
        