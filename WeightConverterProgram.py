#weight converter
weight=float(input("enter your weight "))
unit=input("kilograms or pounds? (K or L):").upper()#What is the unit of the value you entered?

if unit=="K":
    weight*=2.205
    print("Kilograms to Pounds--> ",weight,"lbs")
elif unit=="L":
    weight/=2.205
    print("pounds to kilograms-->",weight,"kg")
else:
    print("Please enter a correct value (K or L)")