def currency_converter(euro,rate):
    dollers = euro*rate
    return dollers
e = input("Enter the euro: ")
r = input("Enter the rate: ")
print(currency_converter(float(e),float(r)))