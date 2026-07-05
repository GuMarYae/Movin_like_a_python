# Enter the coordinates for the first point.
x1, y1 = eval(input("Enter x1 and y1 coordinates followed by commas: "))

# Enter the coordinates for the second point.
x2, y2 = eval(input("Now, gang, enter the x2 and y2 coordinates followed by commas: "))

# Compute the distance between the two points using the distance formula.
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

# Display the answer.
print("The distance between the two points is", distance)