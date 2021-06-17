import math

from datetime import datetime

curent_date_and_time = datetime.now()

UnitChoice = int(input('Do you prefer inches (1) or mm (2)?:\n    '))

if UnitChoice == 1:
    TireWidth_in = float(input('Enter the width of the tire in inches (ex 8):\n    '))
    TireWidth_mm = TireWidth_in * 25.4
    TireDiameter_in = float(input('Enter the diamater of the wheel in inches (ex 15):\n    '))
elif UnitChoice == 2:
    TireWidth_mm = float(input('Enter the width of the tire in mm (ex 205):\n    '))
    TireDiameter_mm = float(input('Enter the diamater of the wheel in mm (ex 380):\n    '))
    TireDiameter_in = TireDiameter_mm / 25.4


TireWidth = TireWidth_mm
TireAR = int(input('Enter the aspect ratio of the tire (ex 60):\n    '))
TireDiameter = TireDiameter_in

TireVolume = (math.pi * (TireWidth ** 2) * TireAR * (TireWidth * TireAR + (2540 * TireDiameter))) / 10000000

TireVolumeRounded = round(TireVolume, 1)

print(f'The approximate volume is {TireVolumeRounded} milliliters.')

#New edit

volumes_list = [curent_date_and_time, TireWidth_mm, TireAR, TireDiameter_in, TireVolumeRounded]
volumes_list_str = ', '.join(map(str, volumes_list))

print(volumes_list_str)

with open('volumes.txt', mode='w+') as volumes_file:
    volumes_file.write(volumes_list_str)
    volumes_file.close()
