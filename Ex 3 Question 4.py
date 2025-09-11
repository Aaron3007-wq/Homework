#Author:Aaron Mclynn
#Date:8/9/25
#Desc:Programming Exercise 3,Ask the user to enter their name and a number and display the number for the value of the number they entered in one letter per line.
name = input('enter your name')
number = input('enter your number')
number=int(number)
for i in range(number):
    for letter in name:
        print(letter)