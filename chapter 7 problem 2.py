import random
random_lottery = []
for num in range(7):
    random_number = random.randint(0, 9)
    random_lottery.append(random_number)
print('\n','The Random Lottery Number is: ', end='',)
for num in random_lottery:
    print(num, end= '')
print('\n')

