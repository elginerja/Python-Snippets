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