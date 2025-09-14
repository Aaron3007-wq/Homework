#Author:Aaron Mclynn
#Date:14/09/25
#Desc:Programming1,Pg174,Q11
principle = int(input('how much is the loan: '))
interest = float(input('how much is the interest, write as a decimal: '))
years = int(input('how many years: '))

simpleInterest = principle + (interest * principle) * years
compoundInterest = principle * ((interest + 1) ** years)

print('your simple interest is: ',simpleInterest)
print('your compound interest ',compoundInterest)
