# BRO STEVE THIS TOOK FOREVER AHHHH
number_of_people = int(input("Enter number of people: "))
number_of_hotdogs_per_person = int(input("Enter number of hot dogs per person: "))

number_of_hotdogs_per_package = 10
number_of_buns_per_package = 8

total_number_of_hotdogs = number_of_people * number_of_hotdogs_per_person

number_of_hotdog_packages_needed = total_number_of_hotdogs / number_of_hotdogs_per_package
number_of_hotdog_bun_packages_needed = total_number_of_hotdogs / number_of_buns_per_package

if (total_number_of_hotdogs % number_of_buns_per_package):
    number_of_hotdog_bun_packages_needed += 1
    
if (total_number_of_hotdogs % number_of_hotdogs_per_package):
    number_of_hotdog_packages_needed += 1

total_number_of_buns = number_of_hotdog_bun_packages_needed * number_of_buns_per_package

number_of_hotdogs_left_over = total_number_of_hotdogs % number_of_hotdogs_per_package
number_of_hotdog_buns_left_over = total_number_of_buns - total_number_of_hotdogs

print("Minimum number of packages of hot dogs required =", number_of_hotdog_packages_needed)
print("Minimum number of packages of hot dog buns required =", number_of_hotdog_bun_packages_needed)
print("Number of hot dogs left over =", number_of_hotdogs_left_over)
print("Number of hot dogs buns left over =", number_of_hotdog_buns_left_over)