# File: <Chapter 5 problem 6>
# Description: <carbs from fat>
# Assignment Name and Number: chapter 5 problem 6
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
fat_grams_per_day = float(input('please enter the number of fat grams consumed in a day: '))
carbs_grams_per_day = float(input('please enter the number of carb grams consumed in a day: '))
amount_of_calories_from_fat_grams = (fat_grams_per_day * 9)
amount_of_calories_from_carb_grams = (carbs_grams_per_day * 4)
print('The amount of calories from fat grams is:', amount_of_calories_from_fat_grams, 'calories. ')
print('The amount of calories from carbs is', amount_of_calories_from_carb_grams, 'calories. ')