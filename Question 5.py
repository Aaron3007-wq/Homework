#Author:Aaron Mclynn
#Date:9/2/26
#Desc:Import random Ex Q5
import random
while True:
    Selector_One = random.randint(1,100)
    Selector_Two = random.randint(1,100)
    Correct = Selector_One + Selector_Two
    Counter = 0
    print("Anwser The Question:",Selector_One,"+",Selector_Two)
    Answer = eval(input("Answer Here:"))
    if Answer == Correct:
        Counter = Counter + 1
        print("Correct Answer!")
        print("Select Q to Quit")
        print("Points =",Counter)
    else:
        print("incorrect answer, try again")
        print("Select Q to Quit")
    if Answer == "Q":
        print("Try again Soon!")
        break
                  
