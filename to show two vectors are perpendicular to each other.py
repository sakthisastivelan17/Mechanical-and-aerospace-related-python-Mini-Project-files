# x is distance b/w two diatomic molecule
# Nu is reduced mass of the diatomic molecule

x=int(input('enter the distance b/w two atoms(mg):'))
Nu=int(input('enter the reduced mass(nm):'))

I=Nu*x**2
print('Moment of inertia of diatomic molecule:',I,'mgnm\u00b2')
