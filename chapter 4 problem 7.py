#I went back and changed this btw after chapter 7
pennies = 0.01
number_of_days = int(input("My guy, please enter the amount of days the pennies will double for: "))
while number_of_days < 0:
    number_of_days = int(input("You need to enter a positive number dude cmon now: "))
output = "\nDay\tPay\n"  "---------------\n"
total_pay = 0.0
day_pay = 0.0
for day in range(number_of_days):
    day_pay = pennies
    output += format(day + 1) + "\t$" + format(day_pay, '.2f') + "\n"
    total_pay += day_pay
    pennies *= 2
output += "---------------\n"  "Bro you are richhhhhh your total pay will be = $" + format(total_pay, '.2f') + "\n"
print(output)