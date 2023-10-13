def kinetic_energy(mass, velocity):
    kinetic_energy = 0.5 * mass * (velocity ** 2) 
    return(kinetic_energy)
mass = float(input('Please enter the objects mass (in kilograms): '))
velocity = float(input('Please enter the objects velocity (in meters per second): '))
ke = kinetic_energy(mass, velocity)
print(f'The kinetic energy of the object is: {ke: .2f} joules.')