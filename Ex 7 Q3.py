#Author: Aaron Mclynn
#Date 8/10/25
#Desc:Ex7, Q3,Program that converts binary to decimal
total = 0
N = 0

N =input('Enter Binary')
Power = len(N)-1
for digit in N:
        total = total+int(digit)*2**Power
        Power =Power -1
print(total)
