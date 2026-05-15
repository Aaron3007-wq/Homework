#Date:11/5/26
#Author: Aaron Mclynn
#Desc: Functions Exercise 2 Q2:
def return_list_AVERAGE (Average):
    a = len(user_list)
    b = sum(user_list)
    result = b/a
    return result
    

user_list = eval(input("Enter Number List"))

solution = return_list_AVERAGE(user_list)
print("The Average of this list is:",solution)
