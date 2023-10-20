# File: <Chapter 7 problem 6>
# Description: <dice roll>
# Assignment Name and Number: chapter 7 problem 6
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
def roll(number_of_throws_from_user):
    throws = [random.randint(1,6) for num in range(number_of_throws_from_user)]
    return sorted(throws)
try:
    number_of_throws_from_user = int(input('\n''MY GUYYYYYYYY, enter the number of throws pleaseeeee: '))
    if number_of_throws_from_user <= 0:
        print('Have you learned nothing? Enter a positive integer please dude')
    else:
        result = roll(number_of_throws_from_user)
        print('Your sorted list of random numbers is the following:', result)
except ValueError:
    print('BRO. POSITIVE INTEGER. PLEASE. ')