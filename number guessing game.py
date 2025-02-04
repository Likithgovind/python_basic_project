import random
lowest_number=1
higest_number=100
answer=random.randint(lowest_number,higest_number)
guesses=0

print("welcome to the number guessing game")
print(f"enter the number between {lowest_number} and {higest_number}")
while True:
    guess=input("enter your guess : ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess>answer:
            print("your guess is too high")
        elif guess<answer:
            print("your guess is too low")
        else:
            print("THAT'S CORRECT")
            break

    else:
        print("INVALID GUESS")
        print(f"please enter the number between {lowest_number} and {higest_number}")
print("==============================")
print("your total guess is",guesses)
