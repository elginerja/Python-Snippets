# File: <Chapter 7 problem 3>
# Description: <rainfall>
# Assignment Name and Number: chapter 7 problem 3
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
rainfall_monthly = []
for month in range(1, 13):
    while True:
        try:
            rainfall = float(input('\n''Please enter the rainfall for each month, starting with January, in inches: '))
            if rainfall < 0:
                print('Please enter a positive number for rainfall. Try again bucko.')
            else: 
                rainfall_monthly.append(rainfall)
                break
        except ValueError:
            print('Bro enter a valid number please. ')
total_rainfall = sum(rainfall_monthly)
average_rainfall = total_rainfall / 12
min_rainfall = min(rainfall_monthly)
max_rainfall = max(rainfall_monthly)
print('\n''The total yearly rainfall is:', total_rainfall, 'inches. ')
print('\n''The average monthly rainfall is: ', average_rainfall, 'inches. ')
print('The month with the most rainfall is the month where there was: ', max(rainfall_monthly), 'inches of rain. ')
print('The month with the least rainfall is the month where there was: ', min(rainfall_monthly), 'inches of rain. ')
print(input('press any key to exit: '))
