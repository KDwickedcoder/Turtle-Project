from turtle import Turtle, Screen

Timmy_the_turtle = Turtle()
Timmy_the_turtle.shape("turtle")
Timmy_the_turtle.color("blue")

n = int(input("Enter the sides of the figure: "))

angle = (n-2)*180/n
left_angle = 180-angle
for round in range(n):
    Timmy_the_turtle.forward(100)
    Timmy_the_turtle.left(left_angle)
screen = Screen()
screen.exitonclick()