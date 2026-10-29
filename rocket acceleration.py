# Uses fixed velocities of 20 and 100 m/s over 10 seconds to calculate acceleration 
# The formula is reversed, so it prints -8.0 m/s² instead of +8.0 m/s².

#code

velocity_1=20
velocity_2=100
time=10
acceleration=(velocity_1-velocity_2)/10
print('Acceleration =',acceleration,'m/s\u00b2')
