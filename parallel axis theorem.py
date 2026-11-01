mass=float(input('enter mass of a rod(kg):'))
length=float(input('enter length of a rod(m):'))

I_cm= mass*length**2/12
I= I_cm+mass*length**2/4

print('Moment of inertia at one end of a rod:',round(I,2))
