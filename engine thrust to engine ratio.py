thrust=float(input('enter the thrust (N):'))
mass=float(input('enter the mass of engine (m):'))
g=9.8

aircraft_weight=mass*g
thrust_to_weight_ratio=thrust/aircraft_weight
print('Thrust to Weight Ratio :',thrust_to_weight_ratio)
