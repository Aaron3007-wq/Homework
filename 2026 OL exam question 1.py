#Author:Aaron Mclynn
#Date:21/4/26
#Desc:2026 OL Exaxm Question 1:

print("Welcome to the step Tracker App!")
name = input("Please enter your name")

#this is where user enters number of steps
steps_today = int(input("Enter the number of steps you walked today: "))

if steps_today >=10000:
    print("Well done!",name, "You reached your goal.")

if steps_today <=10000 and steps_today >=0:
    print("Aim to do more steps tommorow", name)
    
if steps_today <=-1:
    print("The number of steps cannot be negitive")
    