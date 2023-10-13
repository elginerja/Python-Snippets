def multiply(x, y):
    if y == 1:
        return x
    elif y > 1:
        return x + multiply(x, y - 1)
    else:
        return -multiply(x, -y)
number_1 = float(input('\n''enter the first number my guy (make sure its a whole number): '))
number_2 = float(input('\n''enter the second number my dawg (make sure its a whole number): '))
result = multiply(number_1, number_2)
print('\n''the product of', number_1, 'and', number_2, 'is: ', result)