#for exiting program if user doesnot enter correct input
import sys

#installing random lib to select random variable
import random

from enum import Enum

class RPS(Enum):
    Stone = 1
    Paper = 2
    Scissors = 3



print("*"*80)
print("")

print("SS Gaming presents -: ".center(80, "-"))
print("STONE, PAPER & SCISSORS".center(80, " "))

#for importing emoji using unicode
st = "\U0001FAA8"
sc ="\u2702"
pa = "\U0001F4C4"
fc = "\U0001F91E"
tie = "\U0001F91D"
win = "\U0001F3C6"
los = "\U0001F97A"
end = "\U0001F3C1"

userin = input("Enter....\n*1 for Stone" + st + "\n*2 for Paper" + pa +"\n*3 for Scissors" + sc + "\n Your selection is : ")

user = int(userin)


if user < 1 | user >3:
     sys.exit("You must Enter 1, 2, or 3.")

com_in = random.choice("123")

com = int(com_in)

print("")
print("You choose : " + str(RPS(user)).replace("RPS.", "") + ".")
print("Computer choose : " + str(RPS(com)).replace("RPS.", "") + ".")

print("")

print("RESULT TIME".center(47, "\U0001F91E"))

print("")

if user == 1 and com == 3:
     print("🎉🎉You Won!" + win)

elif user == 2 and com == 1:
     print("You Won!" + win)
    

elif user == 3 and com == 2:
     print("🎉🎉You Won!" + win)

elif user == com:
     print("It's a Tie" + tie)

else:
     print("You lost!"+ los)

print("")
print("END GAME".center(45, end))