#Author:Aaron Mclynn
#Date:16/10/25
#Desc:Ex9 Q4,takes in a word and count the amount of times a giving letter is inside that word
count =0
total =0
W = input('Enter Word')
L = input('Give Letter')
for i in range (0,len(W)):
               if (L ==W[i]):
                total=total + 1
                print(total)