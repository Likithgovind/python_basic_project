#weight convertor

weight=float(input("enter your weight: "))
unit=input("kilogram or pound? (k or p): ")

if unit=="k":
    print("your weight is",round(weight*2.205),"Lbs")
elif unit=="p":
    print("your weight is",round(weight/2.205),"kgs")
else:
    print(unit,"is invalid unit")
