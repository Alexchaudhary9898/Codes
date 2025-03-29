
import turtle

# Setup screen

screen = turtle.Screen()

screen.bgcolor("lightblue") # Background color

# Create turtle

spiral = turtle.Turtle()

spiral.speed(0) # Set the speed to the fastest

size = 5 # Initial size of the square side

angle = 90 # Turning angle

# Draw the spiral square

for _ in range(50): # Increase the range for a larger spiral

 spiral.forward(size)

 spiral.left(angle)

 size += 5 # Increase the size to form the spiral effect

# Finish the drawing

turtle.done()