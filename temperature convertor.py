#temperature convertor
symbol=input("Is this temperature is in celsius or Fahrenheit (C/F): ").upper()
temperature=int(input("enter temperature: "))

if symbol=="C":
    F = (temperature*(9/5))+32
    print(f"the temperature in Fahrenheit is {F}^F")
elif symbol=="F":
    C=(temperature-32)*5/9
    print(f"the temperature in celsius is {C}^C")
else:
    print("invalid unit")