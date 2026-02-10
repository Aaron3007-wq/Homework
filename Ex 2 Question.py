#Author:Aaron Mclynn
#Date:10/2/26
#Desc:Dice Game Ex
import random
print("Welcome to dice game!")
Name = input("Enter Your Name")
lucky_num = eval(input("Enter Your Lucky Number 1-6"))
print ("Your lucky number is:",lucky_num)
dice = random.randint(1,6)
print("initializing computer number")
print ("Computer rolled:",dice)
if lucky_num == dice:
    print("You Guess Correct Well Done!")
if lucky_num > dice:
    print("You Guessed Too High")
if lucky_num < dice:
    print("You Guessed Too Low")
