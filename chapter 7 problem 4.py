# File: <Chapter 7 problem 4>
# Description: <average, total, list of numbers>
# Assignment Name and Number: chapter 7 problem 4
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
list_of_numbers = []
for num in range(20):
    while True:
        try:
            num = float(input('\n''Yo, enter a number broski: '))
            list_of_numbers.append(num)
            break
        except ValueError:
            print("Yo dawg, that's not a number input, try again. ")
lowest_number = min(list_of_numbers)
highest_number = max(list_of_numbers)
total_of_numbers = sum(list_of_numbers)
average_of_numbers = total_of_numbers / len(list_of_numbers)
print('\n' 'The total of all of the numbers is: ', total_of_numbers)
print('\n' 'The average of all of the numbers is: ', average_of_numbers)
print('\n' 'The lowest of all of the numbers is: ', lowest_number)
print('\n' 'The highest of all of the numbers is: ', highest_number)