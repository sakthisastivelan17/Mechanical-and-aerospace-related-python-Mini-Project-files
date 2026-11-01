fuel_consumption_per_hour = float(input('enter the fuel consumed by aircraft per hour:'))
flight_time=float(input('enter the flight time:'))
tot_fuel_consumption=fuel_consumption_per_hour*flight_time
print('During a',flight_time,'th hour flight consumes',tot_fuel_consumption,'of litres')
