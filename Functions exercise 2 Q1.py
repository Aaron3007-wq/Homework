#Date:11/5/26
#Author: Aaron Mclynn
#Desc: Functions Exercise 2 Q1:
def return_list_RANGE (Max_Min):
        a = min(user_list)
        b = max(user_list)
        result = b - a
        return result

user_list = eval(input("Enter Number List"))

solution = return_list_RANGE(user_list)
print("The Range of The List is:",solution)

    