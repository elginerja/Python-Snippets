# File: <Chapter 10 problem 1>
# Description: <pet naming>
# Assignment Name and Number: chapter 10 problem 1
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
print(input("This program will tell you to input details about your pet. Press any key to start\n"))
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    def set_name(self, name):
        self.__name = name
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    def set_age(self, age):
        self.__age = age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
my_pet_name = Pet(" ", " ", 0)
name_of_animal = input("\nPlease enter the name of the pet that \nyou are talking about: ")
type_of_animal = input("\nPlease enter the type of animal \n(like is it a dog or a bird or a cat): ")
age_of_animal = input("\nNow enter the pet's age: ")
my_pet_name.set_name(name_of_animal)
my_pet_name.set_animal_type(type_of_animal)
my_pet_name.set_age(age_of_animal)
print("\nHere are the deatils for your pet dude: ")
print("\nName of your pet: " + my_pet_name.get_name())
print("\nYour pet is a: " + my_pet_name.get_animal_type())
print("\nAge of your pet: " + str(my_pet_name.get_age()))
print(input("\nPress any key to exit the program: "))