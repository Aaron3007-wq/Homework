#Author:Aaron Mclynn
#Date:8/9/25
#Desc:Programming Exercise 6,Q3 Program that takes an interger and and outputs all even numbers up to that number
n = input ('Enter Number')
n = int(n)
iteration = 0
while iteration < n:
    iteration = iteration + 1
    if (iteration % 2 == 0):
        print(iteration)
    
    