#Author: Aaron Mclynn
#Date:25/09/26
#Functions Revision, The mean

def return_list_AVERAGE (Average):
    a = len(user_list)
    b = sum(user_list)
    result = b/a
    return result

user_list = eval(input("Enter Number List"))

solution = return_list_AVERAGE(user_list)
print("The Average of this list is:",solution)

