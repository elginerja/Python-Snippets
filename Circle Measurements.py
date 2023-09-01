import math

# Calculating and displaying the area and circumfrence of a circle
r = float(input ('what is your radius:'))
# Define how to get the area of a circle
area_of_circle = float(math.pi * r**2)
# Tell the user what the area of their circle is
print('Your area is', area_of_circle)
# Define how to get the circumference of a circle
circumference = float(2 * math.pi * r)
# Tell the user what the circumference of their circle is
print('Your circumference is', circumference)
