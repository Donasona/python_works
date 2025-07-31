weight_in_kg = int(input("enter your weight in kg:"))

height_in_kg = int(input("enter the height:"))

height_in_meter = height_in_kg/100

bmi = (weight_in_kg)/(height_in_meter)**2

print(bmi)