import random
def roll(number_of_throws_from_user):
    throws = [random.randint(1,6) for num in range(number_of_throws_from_user)]
    return sorted(throws)
try:
    number_of_throws_from_user = int(input('\n''MY GUYYYYYYYY, enter the number of throws pleaseeeee: '))
    if number_of_throws_from_user <= 0:
        print('Have you learned nothing? Enter a positive integer please dude')
    else:
        result = roll(number_of_throws_from_user)
        print('Your sorted list of random numbers is the following:', result)
except ValueError:
    print('BRO. POSITIVE INTEGER. PLEASE. ')