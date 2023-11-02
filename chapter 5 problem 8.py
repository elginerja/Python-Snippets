# File: <Chapter 5 problem 8>
# Description: <painting with square feet>
# Assignment Name and Number: chapter 5 problem 8
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
user_area = float(input('\nYooooo!!! Please enter how many square feet of wall that you need to be painted: '))
user_price = float(input('\nDude!!! Please enter the price of the paint per gallon: '))
gallons_needed = user_area / 112
print('\nYou are going to need', format(gallons_needed, '.2f'), 'gallons of paint to paint this wall.')
total_hours = user_area * 8/112
print('\nYou are going to need', format(total_hours, '.2f'), 'hours of labor to complete the painting of this wall.')
total_cost = gallons_needed * user_price
print('\nYou are going to need', format(total_cost, '.2f'), 'dollars to buy the paint.')
total_charge = total_hours * 35
print('\nYou are going to need', format(total_charge, '.2f'), 'dollars to pay for the labor.')
total_cost_of_all = total_cost + total_charge
print('\nThe total cost for the entire project is:', format(total_cost_of_all, '.2f'), 'dollars.')
print(input('\nPress any key to exit the program: '))