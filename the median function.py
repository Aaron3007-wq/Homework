#Author: Aaron Mclynn
#Date:25/09/26
#Functions Revision, The median

def  return_list_median(L):
    
    
    a = L[len(L)//2]
    o = 2
    e = L[len(L)//2 -1]
    if len(L)%2==0:#even result
        result = (a+e)/2
    else:#odd result
        result = a
    
    return result

user_list = eval(input("Enter Number List"))
list.sort(user_list)

solution = return_list_median(user_list)
print("The median of this list is:",solution)

#[3,5,8,9,11,16,17]
#[4,5,9,10,14,16,18,24]