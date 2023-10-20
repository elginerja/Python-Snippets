# File: <Chapter 7 problem 1>
# Description: <valid numbers>
# Assignment Name and Number: chapter 7 problem 1
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []
for num in numbers:
    if 0 <= num <= 100:
        valid_numbers.append(num)
total = sum(valid_numbers)
average = total / len(valid_numbers) if len(valid_numbers) > 0 else 0
print('Valid Numbers are: ', valid_numbers)
print('Total of the numbers is: ', total)
print('The average of the numbers is: ', average)