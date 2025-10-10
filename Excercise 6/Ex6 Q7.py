#Author: Aaron Mclynn
#Date 8/10/25
#Desc:Ex6 Q7,takes a number between 10-20 and says thank you, will not take a number lower or higher than its range and will amke user retry.
n = 0
while True:
    n = input ('Enter Number')
    n = int (n)
    if (n<10 or n>20):
        print('Try Again')
        continue
    
    if (n>10 and n<20):
        print('thank you')
        break

    
