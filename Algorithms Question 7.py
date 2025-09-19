#Author:Aaron Mclynn
#Date:18/9/25
#Desc:Programming Exercise Algorithms,Q7,To categorise a person as a child,teen or adult based off age given
age=input('Enter your age')
age=int(age)
if (age<13):
    print('you are a child')
elif(age>=13,age<=18):
    print('you are a teenager')
elif(age>=19):
    print('you are an adult')

    