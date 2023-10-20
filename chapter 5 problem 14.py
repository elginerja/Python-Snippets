# File: <Chapter 5 problem 14>
# Description: <kinetic energy>
# Assignment Name and Number: chapter 5 problem 14
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
def kinetic_energy(mass, velocity):
    kinetic_energy = 0.5 * mass * (velocity ** 2) 
    return(kinetic_energy)
mass = float(input('Please enter the objects mass (in kilograms): '))
velocity = float(input('Please enter the objects velocity (in meters per second): '))
ke = kinetic_energy(mass, velocity)
print(f'The kinetic energy of the object is: {ke: .2f} joules.')