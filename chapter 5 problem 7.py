class_a_ticket_price = 20
class_b_ticket_price = 15
class_c_ticket_price = 10
number_of_a_tickets = float(input('Please enter the amount of class A tickets sold: '))
number_of_b_tickets = float(input('Please enter the amoun tof class B tickets sold: '))
number_of_c_tickets = float(input('Please enter the amoun tof class C tickets sold: '))
income_from_class_a = class_a_ticket_price * number_of_a_tickets
income_from_class_b = class_b_ticket_price * number_of_b_tickets
income_from_class_c = class_c_ticket_price * number_of_c_tickets
total_income = income_from_class_a + income_from_class_b + income_from_class_c
print('The income from class A tickets is', income_from_class_a, 'dollars. ')
print('The income from class B tickets is', income_from_class_b, 'dollars. ')
print('The income from class C tickets is', income_from_class_c, 'dollars. ')
print('The total income from all of the tickets is', total_income, 'dollars. ')