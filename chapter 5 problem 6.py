# File: <Chapter 5 problem 6>
# Description: <carbs from fat>
# Assignment Name and Number: chapter 5 problem 6
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
def calories(fat_grams, carb_grams):
    calaries_from_fat_grams = fat_grams * 9
    calories_from_carb_grams = carb_grams * 4
    total_calories = calaries_from_fat_grams + calories_from_carb_grams
    return total_calories
    
def main():
    fat_grams = float(input('\nDude!!! Please enter the amount of fat grams you consume a day: '))
    carb_grams = float(input('\nDude!!! Please enter the amount of carb grams you consume a day: '))
    total = calories(fat_grams, carb_grams)
    print('\nThe total colaries from carbs and fat grams combined is:', total, 'calories. ')
main()
print(input('\nPress any key to exit the program: '))