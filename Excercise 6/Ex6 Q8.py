#Author: Aaron Mclynn
#Date 8/10/25
#Desc:Ex6 Q8,makes user guess the number, if they guess too high then the program makes then retry and same for if they guess too low, prints 'Well done' when the number is successfully entered
#A = Answer
#G = guess
A = 24

while True:
    G = input('Make a Guess')
    G = int (G)
    if (G>24):
        print('Too High')
        continue
    if (G<24):
        print('Too Low')
        continue 
    if (G==24):
        print('Well Done')
        break
    
