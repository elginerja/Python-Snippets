# File: <Chapter 4 problem 14>
# Description: <displaying number of stars>
# Assignment Name and Number: chapter 4 problem 14
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.

size = 7
output = "\n"
for row in range(size, 0, -1):

    for column in range(row):

        output += "* "

    output += "\n"
print(output)