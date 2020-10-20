import csv
import math

fuel = 0.0

def recursive_fuel(fuel):
    print("fuel: {}".format(fuel))
    rem_fuel = math.floor(fuel/ 3.0) - 2
    if(rem_fuel <= 0.0):
       return 0.0
    else:
        return rem_fuel + recursive_fuel(rem_fuel)

with open('fuel.csv') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
       extrafuel = recursive_fuel(float(row[0]))
       fuel = fuel + extrafuel
       print("extrafuel: {}".format(extrafuel))


    print("fuel: {}".format(fuel))
            
