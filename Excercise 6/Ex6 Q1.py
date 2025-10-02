#Author:Aaron Mclynn
#Date:2/10/25
#Desc:Programming Exercise 6,Program give average of numbers using a while loop and ends when giving a string input
n = 0 
total = 0
count = 0
while n!='':
    n = input('Enter Number')
    if n.isdigit():
        total += int(n)
        count +=1
print('average is: ', total/count)

        
