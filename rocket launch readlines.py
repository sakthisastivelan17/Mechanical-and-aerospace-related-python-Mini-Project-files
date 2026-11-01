# A simplified practice system allows launch.
# only if the fuel level is at least 80% and the engine is ready.
# another automated spelling correcter allow

fuel_level=float(input('enter fuel level(%):'))
engine_status=input('enter the engine is ready(yes/no):').strip().lower()

if fuel_level>80 and engine_status=='yes' or engine_status=='yrs' or engine_status=='yed' or engine_status=='yus' or engine_status=='yas':
    print('ready to launch')

else:
    print('warning! not to launch')
