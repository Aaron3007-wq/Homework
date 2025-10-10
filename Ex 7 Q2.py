#Author: Aaron Mclynn
#Date 8/10/25
#Desc:Ex7, Q2, A program that counts up postive numbers and negitive numbers and stops when 0 is entered.
N = 0
total = 0
while True:
    N = input('Enter Numbers')
    N = int (N)
    total = int (total)
    if (N!=0):
        total = N+total
        continue
    if (N==0):
        print(total)
        
        


