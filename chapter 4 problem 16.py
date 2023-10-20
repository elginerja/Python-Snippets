# File: <Chapter 4 problem 16>
# Description: <100 iterations>
# Assignment Name and Number: chapter 4 problem 16
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.

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

