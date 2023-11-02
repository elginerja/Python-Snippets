# File: <Chapter 9 problem 1>
# Description: <jupiter's moons>
# Assignment Name and Number: chapter 9 problem 1
#
# Name: <John Jack Elginer>
# GitHub: <johnjack>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
juiter_moons = {}
jupiter_moons_radius = {'Io': '1821.6','Europa': '1560.8', 'Ganymede': '2634.1', 'Castillo': '2410.3'}
jupiter_moons_surface_gravity = {'Io': '1.796','Europa': '1.314', 'Ganymede': '1.428', 'Castillo': '1.235'}
jupiter_moons_orbitial_period = {'Io': '1.769','Europa': '3.551', 'Ganymede': '7.154', 'Castillo': '16.689'}
moon_name = input('\nEnter a name of one of the moons for Jupiter: ')
if moon_name in jupiter_moons_radius:
        mean_radius = jupiter_moons_radius[moon_name]
        gravity = jupiter_moons_surface_gravity[moon_name]
        period = jupiter_moons_orbitial_period[moon_name]
        print(moon_name, "\nThe Moon's mean radius is: ", mean_radius, 'km. \n' "The Moon's gravity is: ",gravity,'m/s^2. \n'"The Moon's period is period: ", period, 'days.')
else:
        print('Invalid moon name, try again. ')


