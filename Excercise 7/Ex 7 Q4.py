#Author: Aaron Mclynn
#Date 14/10/25
#Desc:Ex7, Q4,Program that converts decimal to binary
total = 0
N = 0

N =input('Enter Decimal')
Power =len(N)
Power=Power -1
for digit in N:
    total = total+int(digit)*(2**Power)
    Power =Power -1
print(total)
    
