# create a roulettle wheel with the colors
users_pocket_number = int(input('Enter your pocket number: '))
if users_pocket_number >=0 and users_pocket_number <=36:
    if users_pocket_number == 0:
        users_pocket_color = 'green'
    elif users_pocket_number >=1 and users_pocket_number <=10:
        if users_pocket_number / 2 == 0:
            users_pocket_color = 'black'
        else:
            users_pocket_color = 'red'
    elif users_pocket_number >= 11 and users_pocket_number <= 18:
        if users_pocket_number / 2 == 0:
            users_pocket_color = "red"
        else:
            users_pocket_color = "black"
    elif users_pocket_number >= 19 and users_pocket_number <= 28:
        if users_pocket_number / 2 == 0:
            users_pocket_color = "black"
        else:
            users_pocket_color = "red"
    elif users_pocket_number >= 29 and users_pocket_number <= 36:
        if users_pocket_number / 2 == 0:
            users_pocket_color = "red"
        else:
            users_pocket_color = "black"
    print("Your pocket color = ", users_pocket_color)
else:
    print('Error, the number you entered must be between 0 and 36. ')