# Takes air density, velocity, wing area, and lift coefficient as input,  
# Then calculates lift using L = ½ × ρ × v² × S × Cₗ and prints the result in newtons.

# code

air_density=float(input('enter air density(kg/m\u00b3):'))
velocity=float(input('enter velocity of aircraft(m/s):'))
wing_area=float(input('enter wing area(m\u00b2):'))
lift_coefficent=float(input('enter the lift coefficient:'))
aircraft_lift=1/2*(air_density)*(velocity**2)*(wing_area)*(lift_coefficent)
print()
print('Aircraft_lift:',aircraft_lift)

                        
