#Author:Aaron Mclynn
#Date:16/10/25
#Desc:Ex9 Q4,
count =0
total =0
W = input('Enter Word')
L = input('Give Letter')
for i in range (0,len(W)):
               if (L ==W[i]):
                total=L+count
                print(total)