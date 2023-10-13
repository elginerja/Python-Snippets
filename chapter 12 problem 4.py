def find_the_largest_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    rest_of_the_list_max = find_the_largest_recursive(lst[1:])
    return lst[0] if lst[0] > rest_of_the_list_max else rest_of_the_list_max
# An example of numbers that I chose, theoretically you could use any numbers
my_list = [21, 43, 17, 54, 89, 32, 65]
largest_value = find_the_largest_recursive(my_list)
print('\n''yo dawg the biggest number in that list is: ', largest_value, '\n')