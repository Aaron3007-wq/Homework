#Author:Aaron Mclynn
#Date:3/2/26
#Desc:HangMan Challenge:
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

Wlst = random.choice(["Hangman","Apple"])
Wlst = list(Wlst)
print(Wlst)
Lives = 7
S = []
Wlst2 = random.choice(["_ _ _ _ _ _ _","_ _ _ _ _"])
while Lives > 0:
    Glst = eval(input("Guess a Letter _ _ _ _ _ _ _:"))
    count = 0
    if Glst in S:
        print("You already guess this")
    else:
        S.append(Glst)
        Valid_Guess = False    
        for i in Wlst:
            if Glst == i:
                Wlst2[count] = Glst
                Valid_Guess = True
            count = count + 1
        print(Wlst2)
        if Valid_Guess == False:
            Lives = Lives - 1
            print("Incorrect Word,Lives Left" ,Lives)
        if Lives == 6:
            print(HANGMANPICS[1])
        if Lives == 5:
            print(HANGMANPICS[2])
        if Lives == 4:
            print(HANGMANPICS[3])
        if Lives == 3:
            print(HANGMANPICS[4])
        if Lives == 2:
            print(HANGMANPICS[5])
        if Lives == 1:
            print(HANGMANPICS[6])
        if Wlst == Wlst2:
            print("You Win!")
            break
