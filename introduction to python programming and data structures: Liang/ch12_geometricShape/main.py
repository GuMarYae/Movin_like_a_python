from GeometricShape import GeometricShape
from GeometricShape import Circle
from Rectangle import Rectangle

# ========================== UML DIAGRAM ==========================
#
#                 ┌─────────────────────────────┐
#                 │       GeometricShape        │
#                 ├─────────────────────────────┤
#                 │ - __color                   │
#                 │ - __isFilled                │
#                 ├─────────────────────────────┤
#                 │ + getColor()                │
#                 │ + isFilled()                │
#                 │ + setColor()                │
#                 │ + setFilled()               │
#                 │ + __str__()                 │
#                 └─────────────────────────────┘
#                              ▲
#                     inherits │ inherits
#                    ┌─────────┴─────────┐
#                    │                   │
#       ┌───────────────────────┐   ┌────────────────────────┐
#       │        Circle         │   │       Rectangle        │
#       ├───────────────────────┤   ├────────────────────────┤
#       │ - __radius            │   │ - __width              │
#       ├───────────────────────┤   │ - __height             │
#       │ + getRadius()         │   ├────────────────────────┤
#       │ + getArea()           │   │ + getWidth()           │
#       │ + getDiameter()       │   │ + getHeight()          │
#       │ + getPerimeter()      │   │ + getArea()            │
#       │ + setRadius()         │   │ + getPerimeter()       │
#       │ + printCircle()       │   │ + setWidth()           │
#       └───────────────────────┘   │ + setHeight()          │
#                                   └────────────────────────┘
#
#  + = public method
#  - = private member variable
#
#  Circle and Rectangle BOTH inherit GeometricShape's:
#  getColor(), isFilled(), setColor(), setFilled(), and __str__()
#
# ================================================================
def main():
    
    geoShape1 = GeometricShape()
    print(f"The geo shape status: ", geoShape1)

    ##################################################################
    rect1 = Rectangle()
    print(f"The rectangle status is : {rect1}")

    rect1.setColor("Pink")
    rect1.setFilled(True)
    print(f"The rectangle status is : {rect1}")
    print(f"the area is {rect1.getArea()}")
    rect1.setHeight(15)
    print(f"the area is {rect1.getArea()}")
    rect1.setWidth(10)
    print(f"the area is {rect1.getArea()}")
    ###################################################################

    circle1 = Circle()
    circle1.setRadius(11)

    print("Radius: ",circle1.getRadius())
    print("Circle stats: ", circle1)
    print("the area is :", circle1.getArea())
    
main() # calls the main function









