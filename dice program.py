#rolling dice
import random

dice_art={
    1:("┌---------┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└---------┘"),
    2:("┌---------┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└---------┘"),
    3:("┌---------┐",
       "│ ●       │",
       "│    ●    │",
       "│        ●│",
       "└---------┘"),
    4:("┌---------┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└---------┘"),
    5:("┌---------┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└---------┘"),
    6:("┌---------┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└---------┘"),
}
dice=[]
total=0
num=int(input("enter number of dice: "))

for die in range(num):
    dice.append(random.randint(1,6))

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()

for die in dice:
    total+=die
print("total is",total)