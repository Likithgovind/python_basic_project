# Python credit card validator program

even_number=0
odd_number=0
total=0

card_number=input("enter the your credit card number: ")
card_number=card_number.replace("-","")
card_number=card_number.replace(" ","")
card_number=card_number[::-1]


for i in card_number[::2]:
    odd_number+=int(i)


for i in card_number[1::2]:
    i=int(i)*2
    if i >=10:
        even_number+=(1+(i%10))
    else:
        even_number+=i

total=odd_number+even_number
if total%10==0:
    print("VALID")
else:
    print("INVALID")