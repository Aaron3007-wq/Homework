#Author:Aaron Mclynn
#Date:9/2/26
#Desc:Import random Ex Q4
import random
Lives = 7
Selector = random.randint(1,100)
print (Selector)
while Lives > 0:
    Guess = eval(input("Guess a Number:"))
    if Guess == Selector:
        print("You Win!")
        break
    else:
        if Guess != Selector:
            print("incorrect, try again")
            Lives = Lives - 1
        if Lives == 0:
            print("You lost")
        
        
    
    
    

