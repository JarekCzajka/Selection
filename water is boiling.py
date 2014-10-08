#Jaroslaw Czajka
#08-10-2014
#Program which asks the userfor the temperature of water container and displyes if the water is frozen,boiling or neither

print("Welcome to  find the temperature of water ")
temperature_of_water=int(input("Please enter the temperature of your water:"))
if temperature_of_water >=100:
    print("your water is boiling")
elif temperature_of_water <=0:
    print("your water is frozen")
else:
    print("your water is normal")
