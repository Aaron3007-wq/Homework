#Author:Aaron Mclynn
#Date:9/2/26
#Desc:Import random Ex Q3
import random
HT = ["Heads","Tails"]
RandomHT = random.choice(HT)
Guess = eval(input("Make your guess"))
print(RandomHT)
if Guess == RandomHT:
    print("You Win!")
else:
    print("you lost")
