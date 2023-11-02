# File: <Chapter 5 problem 7>
# Description: <number of class tickets>
# Assignment Name and Number: chapter 5 problem 7
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
def total_income(class_a_seat, class_b_seat, class_c_seat):
    a_ticket_income = class_a_seat * 20
    b_ticket_income = class_b_seat * 15
    c_ticket_income = class_c_seat * 10
    total_income_from_all_seats_combined = a_ticket_income + b_ticket_income + c_ticket_income
    return total_income_from_all_seats_combined
def main():
    number_of_class_a_tickets_sold = int(input('\nMy guy!!! Please enter the number of class a tickets sold: '))
    number_of_class_b_tickets_sold = int(input('\nMy dude!!! Please enter the number of class b tickets sold: '))
    number_of_class_c_tickets_sold = int(input('\nDawg!!! Please enter the number of class c tickets sold: '))
    total = total_income(number_of_class_a_tickets_sold, number_of_class_b_tickets_sold, number_of_class_c_tickets_sold)
    print('\nThe total income from all three seat kinds combined is: $ ',total, 'dollars. ')
main()
print(input('\nPress any key to exit the program: '))