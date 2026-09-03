#Author:Aaron Mclynn
#Date:3/9/26
#Desc:Binary Search
lst = [2,5,8,12,16,56,23,72,38,91]
list.sort(lst)
Target_Value = 23

High_index = len(lst)
High_index = High_index - 1

Low_index = 0

while Low_index <= High_index:

    middle = (High_index + Low_index) // 2
    
    if lst[middle] == Target_Value:
        print("Found",Target_Value,"at index",middle)
        break
    
    elif lst[middle] > Target_Value:
        High_index = middle - 1
        
    else:
        Low_index = middle + 1
else:
    print("Not found")
        
        
    

    
print(lst)


