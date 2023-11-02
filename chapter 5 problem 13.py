# File: <Chapter 5 problem 13>
# Description: <falling distance>
# Assignment Name and Number: chapter 5 problem 13
#
# Name: <John Jack Elginer>
# GitHub: <elginerja>
#
# On my honor, <Jack Elginer>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
   for falling_time in range(1, 11):
      times = falling_distance(falling_time)
      print('\nThe distance that it has fallen is', format(times, '.2f'), 'meters at', falling_time, 'seconds.')

def falling_distance(time):
   gravity = 9.8
   distance = (.5 * gravity * (time ** 2))
   return distance


main()
print(input('\npress any key to exit the program: '))