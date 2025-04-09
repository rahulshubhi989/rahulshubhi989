#GUESSING GAME USING PYTHON

import random

randnum = random.randint(1, 100)

while True:
    usernum = int(input("enter your number: "))
    if(usernum == randnum):
        print("success : you guessed correct! ")
        break
    elif(usernum < randnum):
        print("your number is small! take a bigger guess!")
    else:
        print("your number is big! take a smaller guess!")


print("---- GAMEOVER ----")