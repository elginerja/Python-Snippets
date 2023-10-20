# File: <Chapter 5 problem 13>
# Description: <falling object>
# Assignment Name and Number: chapter 5 problem 13
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
def falling_distance(time):
    g = 9.8
    distance = 0.5 * g * (time ** 2)
    return distance
for time in range(1, 11):
    distance = falling_distance(time)
    print(f'At the time: {time} seconds, the distance it has fallen is: {distance:.2f} meters')