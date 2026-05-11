#Date:11/5/26
#Author: Aaron Mclynn
#Desc: Lesser of two evens Function:
def check_two_numbers(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            return b
        else:
            return a
    if a%2!=0:
        if a>b:
            return a
        else:
            return b
        
    if b%2!=0:
        if a>b:
            return a
        else:
            return b
x = check_two_numbers(8,7)
print(x)