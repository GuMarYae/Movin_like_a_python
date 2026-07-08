import turtle  # Import the turtle graphics module

# Set the pen thickness
turtle.pensize(3)

########################################
# Triangle (Not Filled)
########################################

turtle.penup()                  # Lift the pen
turtle.goto(-300, -50)          # Move to the starting position
turtle.pendown()                # Put the pen down
turtle.circle(59, steps=3)      # Draw a triangle
turtle.pencolor("yellow")       # Change the pen color

########################################
# Change Pen Thickness
########################################

turtle.pensize(7)               # Make the pen thicker

########################################
# Square (Not Filled)
########################################

turtle.penup()                  # Lift the pen
turtle.goto(-100, -50)          # Move to the starting position
turtle.pendown()                # Put the pen down
turtle.circle(40, steps=4)      # Draw a square
turtle.speed(17)                # Change drawing speed
turtle.pencolor("black")        # Change the pen color

########################################
# Pentagon (Not Filled)
########################################

turtle.penup()                  # Lift the pen
turtle.goto(0, -50)             # Move to the starting position
turtle.pendown()                # Put the pen down
turtle.circle(40, steps=5)      # Draw a pentagon
turtle.speed(100)               # Change drawing speed
turtle.pencolor("blue")         # Change the pen color

########################################
# Hexagon (Not Filled)
########################################

turtle.penup()                  # Lift the pen
turtle.goto(100, -50)           # Move to the starting position
turtle.pendown()                # Put the pen down
turtle.circle(40, steps=6)      # Draw a hexagon
turtle.speed(2)                 # Slow the drawing speed

########################################
# Change Pen Settings
########################################

turtle.pensize(25)              # Make the pen very thick
turtle.pencolor("red")          # Change the pen color

########################################
# Circle (Not Filled)
########################################

turtle.penup()                  # Lift the pen
turtle.goto(200, -50)           # Move to the starting position
turtle.pendown()                # Put the pen down
turtle.circle(26)               # Draw a circle
turtle.speed(10)                # Change drawing speed
turtle.pencolor("pink")         # Change the pen color

###############################################################
# Added Filled Shapes
###############################################################

########################################
# Octagon (Filled)
########################################

turtle.penup()                  # Lift the pen
turtle.goto(-300, 120)          # Move to the starting position
turtle.pendown()                # Put the pen down
turtle.begin_fill()             # Begin filling the shape
turtle.color("orange")          # Set the outline and fill color
turtle.circle(35, steps=8)      # Draw an octagon
turtle.end_fill()               # Fill the octagon

########################################
# Heptagon (Filled)
########################################

turtle.penup()                  # Lift the pen
turtle.goto(-150, 120)          # Move to the starting position
turtle.pendown()                # Put the pen down
turtle.begin_fill()             # Begin filling the shape
turtle.color("cyan")            # Set the outline and fill color
turtle.circle(35, steps=7)      # Draw a heptagon
turtle.end_fill()               # Fill the heptagon

########################################
# Nonagon (Filled)
########################################

turtle.penup()                  # Lift the pen
turtle.goto(0, 120)             # Move to the starting position
turtle.pendown()                # Put the pen down
turtle.begin_fill()             # Begin filling the shape
turtle.color("pink")            # Set the outline and fill color
turtle.circle(35, steps=9)      # Draw a nonagon
turtle.end_fill()               # Fill the nonagon

########################################
# Decagon (Filled)
########################################

turtle.penup()                  # Lift the pen
turtle.goto(150, 120)           # Move to the starting position
turtle.pendown()                # Put the pen down
turtle.begin_fill()             # Begin filling the shape
turtle.color("brown")           # Set the outline and fill color
turtle.circle(35, steps=10)     # Draw a decagon
turtle.end_fill()               # Fill the decagon

########################################
# Star (Filled)
########################################
turtle.pensize(0.5)               # Make the pen thicker

turtle.penup()                  # Lift the pen
turtle.goto(300, 120)           # Move to the starting position
turtle.pendown()                # Put the pen down
# turtle.begin_fill()             # Begin filling the star
# turtle.color("gold")            # Set the outline and fill color

for i in range(5):              # Repeat 5 times
    turtle.forward(70)          # Draw one side
    turtle.right(144)           # Turn 144 degrees

# turtle.end_fill()               # Fill the star

########################################
# Write a Title
########################################

turtle.color("green")           # Set the text color
turtle.penup()                  # Lift the pen
turtle.goto(-170, 220)          # Move to the title position
turtle.pendown()                # Put the pen down

turtle.write(
    "Cool Colorful Shapes",     # Text to display
    font=("Times", 20, "bold")  # Font style and size
)

########################################
# Finish the Program
########################################

turtle.hideturtle()             # Hide the turtle cursor
turtle.done()                   # Keep the window open