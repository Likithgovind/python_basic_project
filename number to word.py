#convertig number to word less than 1000
numbers=int(input("enter the number: "))

ones=["","one","two","three","four","five","six","seven","eight","nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

if numbers==0:
    print("zero")

else:
    words=[]

    if numbers//100:
        words.append(ones[numbers//100]+" hundered")
        numbers%=100
    if numbers>=10 and numbers<20:
        words.append(teens[numbers%10])
        numbers=0
    elif numbers>=20:
        words.append(tens[numbers//10])
        numbers%=10
    if numbers>0:
        words.append(ones[numbers])

    print(" ".join(words))



