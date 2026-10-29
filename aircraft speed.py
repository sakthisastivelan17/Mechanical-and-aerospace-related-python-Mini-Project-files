# Takes distance (km) and time (seconds), divides them to get average speed, and prints it. 
# The label says km/h, but since time is in seconds the result is actually km/s.

# code

distance = float(input('enter the travelled distance(km):'))
time = float(input('enter the time(sec) :'))
average_speed=distance/time
print('Average Speed=',average_speed,'km/h')
