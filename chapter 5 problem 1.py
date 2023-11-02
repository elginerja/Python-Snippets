# File: <Chapter 5 problem 1>
# Description: <kilometers to miles>
# Assignment Name and Number: chapter 5 problem 1
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.

print("\nThis program takes a distance in kilometers and changes it into miles. ")
kilometers=int(input("\nDude!!! Please enter a distance in kilometers: "))
def convert_to_miles(kilo):
    miles = kilo * 0.6214
    print("\nThere are",miles,"miles in",kilometers,"kilometers.")

convert_to_miles(kilometers)
print(input('\nPress any key to exit program: '))
