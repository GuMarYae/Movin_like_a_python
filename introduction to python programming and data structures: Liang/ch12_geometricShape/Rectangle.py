from GeometricShape import GeometricShape

class Rectangle(GeometricShape): ## using the parent ###############
    def __init__(currentObject, width = 1, height = 1):
        
        #### i guess super means super class
        #### so we are invoking class's init method 
        #### Python says: Go to my superclass GeometricShape and invoke its __init__().
        super().__init__()
        currentObject.__width = width; currentObject.__height = height
        
    ###### getters #######################
    def getWidth(currentObject):
        return currentObject.__width
    def getHeight(currentObject):
        return currentObject.__height
    
    def getArea(currentObject):
        return currentObject.__width * currentObject.__height
    def getPerimeter(currentObject):
        return 2 * (currentObject.__width + currentObject.__height)
    
    ###### setters #######################
    def setWidth(currentObject, width):
        currentObject.__width = width
        
    def setHeight(currentObject, height):
        currentObject.__height = height
        
    def printRectangle(currentObj):
    # Invoking __str__() from GeometricShape to get color + filled
    # Then adding Rectangle's private width + height
        print(f"{currentObj.__str__()} width: {currentObj.__width} and the height: {currentObj.__height}")
        
    