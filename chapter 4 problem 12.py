# File: <Chapter 4 problem 12>
# Description: <factorial for a number>
# Assignment Name and Number: chapter 4 problem 12
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.

print("\n")
users_number = int(input("Please enter a positive number: "))
while users_number < 0:
    users_number = int(input("Error: You need to enter a positive number, try again. : "))
total = 0
if users_number > 0:
    total = 1

    for number in range(users_number):
        total *= (number + 1)
output = format(total)
print("\n", output, "is your number's factorial. ", "\n")