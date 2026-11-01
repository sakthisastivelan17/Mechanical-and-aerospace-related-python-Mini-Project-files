object_speed=float(input('enter the object speed(m/s):'))
sound_speed=float(input('enter the speed of sound(m/s):'))
mach=object_speed/sound_speed

print('Mach Number:',round(mach,2))

if mach == 1:
    print('sonic')

elif mach >1:
    print('supersonic')

else:
    print('subsonic')
                  

                  
