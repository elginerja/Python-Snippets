# File: <Chapter 4 problem 2>
# Description: <display the number of calories burned in an interveral of time>
# Assignment Name and Number: chapter 4 problem 2
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.

number_of_cal_per_min = 4.2
num_burned_after_minutes = 0
message = ''

for minutes in range(5, 31, 5): 

    num_burned_after_minutes = minutes * number_of_cal_per_min

    message += "number of calories burned after "   \
            + format(minutes) + ' minutes = '       \
            + format(num_burned_after_minutes)      \
            + "\n"

print(message)