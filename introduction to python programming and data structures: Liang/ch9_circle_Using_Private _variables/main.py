from Circle import Circle

circle1 = Circle()

print("here: ", circle1.getArea(), " and here ", circle1.getRadius())

# means that both variables point to the same object
circle2 = circle1

circle2.setRadius(15)

print("The area of thic circle is ", circle2.getArea())

circle1.setRadius(1)
print("The area of thic circle is ", circle2.getArea())


#############################################################################

circle1.radius = 100
print("The area of thic circle is ", circle2.getArea())

circle1.__radius = 100
print("The area of thic circle is ", circle2.getArea())

