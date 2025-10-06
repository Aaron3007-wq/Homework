#Author:Aaron Mclynn
#Date:8/9/25
#Desc:Programming Exercise 6,Q5, count to n squared and stops before 51
n = input ('Enter Number')
n = int(n)
iteration = 1
while iteration < n**2:
    iteration = iteration + 1 
    if iteration >= 51:
        break
    print(iteration)
    
    
