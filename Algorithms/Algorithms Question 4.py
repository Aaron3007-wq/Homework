#Author:Aaron Mclynn
#Date:19/9/25
#Desc:Programming Exercise Algorithms, Q4,To check wheter its a leap year or not
Days =input('Enter Days in this Year')
Days =int(Days)
if (Days>365):
    print('This is leap year')
elif (Days<366):
    print('This is not a leap year')
