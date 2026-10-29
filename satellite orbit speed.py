# Uses Earth’s mass, the gravitational constant, and a 7,000 km orbit radius. 
# To calculate the circular orbital speed with v = √(GM/r), printed to 2 decimal places.

# code

import math
G=6.674e-11
earth_mass=5.972e24
orbital_radius=7_000_000
satellite_orbital_speed=math.sqrt(G*earth_mass/orbital_radius)
print('Satellite Orbital Speed:',round(satellite_orbital_speed,2),'m/s')
