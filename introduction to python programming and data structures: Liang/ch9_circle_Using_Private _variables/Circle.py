class Circle:
    #constructor with privates
    def __init__(self, radius = 1, area = 1):
        self.__radius = radius
        self.__area = area
    
    
    # getters: you always RETURN it.. ALWAYS
    def getArea(self):
        return self.__radius**2 * 3.14159
    
    def getRadius(self):
        return self.__radius
    
    
    
    # setters always "point" the variable to the instance variable
    def setRadius(self, radius):
        #remember, instance variable = the parameter variable in the parens ()
        self.__radius = radius