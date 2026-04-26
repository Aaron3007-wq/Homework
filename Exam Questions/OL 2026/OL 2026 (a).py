#Author:Aaron Mclynn
#Date:21/4/26
#Desc:2026 OL Exaxm Question 1: (a)

print("Welcome to the Step Tracker App!")

name = input("Please enter your name: ")

steps_today = int(input("Enter the number of steps you walked today: "))

if steps_today < 0:
    print("The number of steps cannot be negative")
else:
    if steps_today < 5000:
        print("Try to be more active today", name)
    elif steps_today < 10000:
        print("Good effort", name , "! Almost there.")
    else:
        print("Well done", name, "you reached your goal!")
