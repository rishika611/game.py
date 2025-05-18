import turtle

# Set up the screen

screen = turtle.Screen()

screen.bgcolor("pink")

screen.setup(300,400)

# Create a turtle object

square = turtle.Turtle()

# Define the number of sides and side length

n =4 # square

l = 70 # Side length

angle = 360.0 / n # Interior angle

# Draw the square

for i in range(n):

    square.forward(l) # Move forward by 'l' instead of 'n'

    square.right(angle) # Turn right

# Finish turtle graphics

turtle.done()