# J - rotatinal quantum number
# h_bar - reduced planck constant
# E_j -rotational energy level of the diatomic molecule
# Nu - reduced mass
# x - distance between two atoms

J=int(input('enter rotational quantum number:'))
h_bar=6.626*10-34
Nu=float(input('enter the reduced mass:'))
x=float(input('enter the distance between two atoms:'))

E_j= J * J+1 * h_bar /2 * Nu * x ** 2

print('Rotational energy level of the diatomic molecule:',round(E_j,2))







