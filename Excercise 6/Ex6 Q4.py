#Author:Aaron Mclynn
#Date:8/9/25
#Desc:Programming Exercise 6,Q4 counts to n while skipping 5 
n = input ('Enter Number')
n = int(n)
iteration = 1
while iteration < n:
    iteration = iteration + 1
    if (iteration % 5 == 0):
        continue
    print(iteration)
       
    
