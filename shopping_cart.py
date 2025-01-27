#shopping cart
foods=[]
prices=[]
total=0
while True:
    food=input("enter your food (q for quit): ")
    if food.lower()=="q":
        break
    else:
        foods.append(food)
        price=input("enter the prize: ₹")
        prices.append(price)

print("-----your cart-----")
for i in foods:
    print(i,end=" ")
for j in prices:
    total+=int(j)
print()
print("your total amount is ₹",total,end=" ")
