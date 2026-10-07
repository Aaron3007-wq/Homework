#Author: Aaron Mclynn
#Date:25/09/26
#Functions Revision, The mode

def  return_list_mode(L):
    
    counter = 0
    
    for i in range L:
        if i == [L]:
            counter = counter + 1
        
        result = counter
    
    
    
    
    return result



user_list = eval(input("Enter Number List"))

solution = return_list_mode(user_list)
print("The mode of this list is:",solution)

