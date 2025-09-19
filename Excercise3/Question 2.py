#Author: Aaron Mclynn
#Date 3/9/25
#Desc:Ask user to input a number under 20, display thank you if the number is equal or under 20, display "too high" if over 20
number1 = input('Input number under 20')
number1 =int(number1)

if (number1 <=20):
    print('Thank you')

elif (number1 >=20):
    print('Too High')
