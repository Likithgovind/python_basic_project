#Snack Bar menu
menu={"french fries"  :80.00,
      "sandwich" : 100.00,
      "samosa" :50.00,
      "cheese nachos" :150.00,
      "popcorn" :80.00,
      "pav bhaji"  :120.00,
      "chicken role"  :180.00,
      "veg spring Rolls"  :120.00,
      "paneer pakora"  :100.00,
      "coffee"  :12.00,
      "ice cream"  :40.00}
cart=[]
total=0
print("============ menu ================")
for key,value in menu.items():
  print(f"{key:20}: ₹{value:.2f}")
print("===================================")
while True:
  food=input("enter your order (q for quit): ").lower()
  if food == "q":
    break
  elif menu.get(food) is not None:
    cart.append(food)
print("----------your order ---------------")
for food in cart:
  total+=menu.get(food)
  print(food,end=", ")

print()
print("your total is ₹",total)
