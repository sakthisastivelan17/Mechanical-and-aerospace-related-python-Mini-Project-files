import math
torque=float(input('enter the torque:'))
rpm=int(input('enter the rpm:'))
omega=(2*math.pi*rpm)/60
power=torque*omega
print('Mechanical power:',round(power,2),'watts')
