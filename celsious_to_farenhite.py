def temperature_conversion(celsious):
    ferenhite = (celsious * 9/5)+32
    return ferenhite
celsious = float(input("Enter the celsious temperature: "))
print(temperature_conversion(celsious)," F")