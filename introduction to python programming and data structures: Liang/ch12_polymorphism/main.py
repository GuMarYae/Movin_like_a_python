from GeometricShape import GeometricShape
from Circle import Circle
from Rectangle import Rectangle


def main():
    geo1 = GeometricShape() # invokes __init__(), the constructor
    circle1 = Circle(7)
    rect1 = Rectangle(7,11)

    print(" ============================================>> \n Before the function call",geo1, "\n ============================================>>") # invokes the the status, so it invokes __str__()
    
    # what we're gonna do is throw this function call inside a function itself
    display(geo1)
    display(circle1)
    #display(rect1)


def display(object):
    print() ##new line
    # NOTE the isinstance(object, GeometricShape) will not work because all chilfdren of geometricShape as. umm. geimetricShapes
    # my practice was to print the parent functions __init__ even though its not an actual shape. jst wanted to see the default printout 
    if type(object) is GeometricShape:
        print(f"The main stats for Geometric object with no assgned shape is: {object}")
        print()
    else:
        print(f"The area is {object.getArea()}")
        print ("The perimeter is: ", object.getPerimeter())
        
                # isinstance is definetely case sensative. Its not is Instance != isinstance
        if isinstance(object, Circle): # Checks whether object was created from the Circle class
                                    # or from a subclass of Circle.
            print(f"For this circle, the Diameter is {object.getDiameter()}. The status is this circle is: {object}")
            
                #Circles have a diameter. Rectangles have width and height.
        elif isinstance(object,Rectangle):
            print(f"For this rectangle, the width is: {object.getWidth()}\n the height is {object.getHeight()}")

        
main()
        
        
        
    
    
    



