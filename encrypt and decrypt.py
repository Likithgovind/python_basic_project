import random
import string

chars=" " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)

#encrypt
plain_text=input("enter the message to encrypt: ")
chiper_text=""

for letter in plain_text:
    index=chars.index(letter)
    chiper_text+=key[index]

print("the original message: ",plain_text)
print("the encrypt message: ",chiper_text)

#decrypt
chiper_text=input("enter the message to encrypt : ")
plain_text=""

for letter in chiper_text:
    index=key.index(letter)
    plain_text+=chars[index]

print("the encrypt message: ", chiper_text)
print("the original message: ",plain_text)


