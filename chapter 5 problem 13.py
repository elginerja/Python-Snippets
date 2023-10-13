def falling_distance(time):
    g = 9.8
    distance = 0.5 * g * (time ** 2)
    return distance
for time in range(1, 11):
    distance = falling_distance(time)
    print(f'At the time: {time} seconds, the distance it has fallen is: {distance:.2f} meters')