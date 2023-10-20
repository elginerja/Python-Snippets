# File: <Chapter 7 problem 2>
# Description: <lottery numbers>
# Assignment Name and Number: chapter 7 problem 2
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
random_lottery = []
for num in range(7):
    random_number = random.randint(0, 9)
    random_lottery.append(random_number)
print('\n','The Random Lottery Number is: ', end='',)
for num in random_lottery:
    print(num, end= '')
print('\n')

