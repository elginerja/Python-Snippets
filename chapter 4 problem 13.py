# # File: <Chapter 4 problem 13>
# # Description: <multiplying organisms>
# # Assignment Name and Number: chapter 4 problem 13
# #
# # Name: <John Jack Elginer>
# # GitHub: <johnjack>
# #
# # On my honor, <Jack Elginer>, this programming assignment is my own work
# # and I have not provided this code to any other student.

the_starting_number_of_organisims = int(input("\nStarting number of organisims: "))
while the_starting_number_of_organisims < 0:
    the_starting_number_of_organisims = int(input("Error: Enter a positive number. "))
the_average_daily_increase = float(input("Average daily increase: "))
while the_average_daily_increase < 0:
    the_average_daily_increase = float(input("Error: Enter a positive number. "))
the_average_daily_increase /= 100
number_of_days_to_multipy_by = int(input("Number of days to multiply: "))
while number_of_days_to_multipy_by < 0:
    number_of_days_to_multipy_by = int(input("Error: Enter a positive number. "))
output = "\nDay Approximation \tPopulation\n" + "----------------------------------\n"
population = the_starting_number_of_organisims
for day in range(number_of_days_to_multipy_by):

    if day == 0:
        output += format(day + 1) + "\t\t" + format(population) + "\n"
    
    else: 
        population += (population * the_average_daily_increase)
        output += format(day + 1) + "\t\t" + format(population) + "\n"
        output += "----------------------------------\n"
print(output)