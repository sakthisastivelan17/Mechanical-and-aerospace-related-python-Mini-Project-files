fuel_per_hour = float(input('enter fuel consumption per hour(litres)approx:'))
total_hour=int(input('enter total flight time(hour):'))
total_fuel=0

for hour in  range(total_hour):
    total_fuel=total_fuel+fuel_per_hour
print()
print('Total fuel consumption:',round(total_fuel,2),'(litres)')
    
