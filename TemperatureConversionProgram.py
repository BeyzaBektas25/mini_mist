unit=input("Celsius or fahrenheit? (C or F)").upper()
temp=float(input("Enter the temperature:"))
if unit=="C":
   temp=(temp*1.8)+32
   print ("Celsius to fahrenheit:",temp)
elif unit=="F":
   temp=(temp-32)*(5/9)
   print ("fahrenheit to Celsius :",temp)

else:
   print("ERROR, try again.")