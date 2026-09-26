import math


class Circle:
    # Adding a variable to self creates a data field for that object.
    # Example:
    # self.radius = 5
    # self.name = "Circle"
    # self.area = 0
    # These data fields can then be accessed by the object's methods.


    # __init__ is Python's constructor.
    # It automatically runs every time a new Circle object is created.
    #
    # 🔥🔥🔥🔥🔥 In C++, you might write TWO constructors:
    #
    # Circle()              -> constructor with no arguments
    # Circle(double radius) -> constructor that takes an argument
    #
    # 🔥🔥🔥🔥🔥 Python can handle BOTH situations with ONE constructor
    # by giving the parameter a default value:
    #
    # radius=1 means:
    # "If no radius is given, use 1."
    #
    # Circle()  -> radius becomes 1
    # Circle(5) -> radius becomes 5
    #
    # Circle(5) DOES NOT overwrite or change the default radius=1.
    # The 1 remains the default for future objects.
    #
    # Python simply checks whether a radius was provided:
    #
    # No argument:
    # Circle() -> uses radius=1
    #
    # Argument provided:
    # Circle(5) -> skips the default 1 and uses radius=5
    #
    # BOTH objects use the SAME __init__ constructor.
    # The constructor simply receives a different radius each time.

    def __init__(self, radius=1):
        # radius = local parameter for THIS constructor call
        #
        # Circle()  -> radius = 1
        # Circle(5) -> radius = 5
        #
        # self is the specific object currently being created.
        # self.radius creates/stores radius on that specific object.
        self.radius = radius  # Creates the radius data field


    # Methods are simply functions inside a class
    def getParameter(self):
        # self = the specific object calling this method
        # If c1.getParameter() is called, self = c1
        # If c2.getParameter() is called, self = c2
        # self lets this method access that object's data fields
        return 2 * self.radius * math.pi


    def getArea(self):
        # self.radius = the SAME radius data field created in __init__
        return self.radius * self.radius * math.pi


    def setRadius(self, radius):
        # radius = a NEW local parameter
        # self.radius = the SAME data field created in __init__
        # This changes/updates THIS object's radius
        self.radius = radius


def main():

    # Creates c1 using the SAME constructor.
    # No radius was provided, so Python uses the default radius=1.
    c1 = Circle()

    print("The area of the circle of radius, ",
          c1.radius, "is ", c1.getArea())


    # Creates c2 using the SAME constructor.
    # We provided 5, so Python uses 5 instead of the default 1.
    #
    # This DOES NOT change radius=1 in the constructor.
    # It only means radius=5 during THIS constructor call.
    c2 = Circle(5)

    print("The area of the circle of radius, ",
          c2.radius, "is ", c2.getArea())


    # c1.radius is still 1
    # c2.radius is 5
    #
    # c1 and c2 are completely separate objects.
    #
    # When c1 calls a method:
    # self = c1
    #
    # When c2 calls a method:
    # self = c2
    
    
    #simly changing c2 = Circle(5) into c2 = Circle(3)
    c2.radius = 3
    print("The area of the circle of radius, ",
              c2.radius, "is ", c2.getArea())
    

    print(c1.getParameter())
    print(c1.getArea())


main()