user_number = int(input('Enter an integer: '))

if user_number > 0:
    print("Positive")
elif user_number < 0:
    print("Negative")
elif user_number == 0:
    print("Zero")
if user_number % 2 == 0:
    print("Even")
else:
    print("Odd")