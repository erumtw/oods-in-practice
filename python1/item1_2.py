print(" *** Wind classification ***")
speed = float(input("Enter wind speed (km/h) : "))

if speed >= 209:
   wind = 'Super Typhoon'
elif speed >= 102:
   wind = 'Typhoon'
elif speed >= 56:
   wind = 'Tropical Storm'
elif speed >= 52:
   wind = 'Depression'
else :
   wind = 'Breeze'

print(f"Wind classification is {wind}.")
    