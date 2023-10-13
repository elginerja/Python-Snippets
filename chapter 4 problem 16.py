import turtle
turtle.penup()
turtle.goto(335, -335)
turtle.pendown()
number_of_squares = 100
side_length = 3
angle = 90
animation_speed = 0
turtle.speed(animation_speed)
for count in range(number_of_squares):
    for count in range (3):
        turtle.forward(side_length)
        turtle.left(angle)
        side_length += 3
input('press a key to exit')

