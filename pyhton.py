import turtle=

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")  # Background screen

# Create a turtle object
flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)  # Set the speed of the turtle

# Function to draw a flower petal
def draw_petal():
    flower.color("red")
    flower.circle(100, 60)  # Draw a circular arc with radius 100 and angle 60 degrees
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)

# Function to draw a complete flower
def draw_flower():
    for _ in range(6):  # 6 petals for the flower
        draw_petal()
        flower.left(60)  # Rotate the turtle by 60 degrees for next petal

# Function to draw the stem of the flower
def draw_stem():
    flower.color("green")
    flower.right(90)
    flower.forward(300)

# Move the turtle to the starting position
flower.penup()
flower.setpos(0, -100)
flower.pendown()

# Draw the flower
draw_flower()

# Draw the stem
flower.penup()
flower.setpos(0, -100)
flower.pendown()
draw_stem()

# Hide the turtle after drawing
flower.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
