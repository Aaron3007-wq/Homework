#Author:Aaron Mclynn
#Date:10/9/26
#Desc:Simple Sort
unsorted = [4,8,2,7,9]
lst = []

for i in range(len(unsorted)):
    s_value = 99999999999999999999999999999999999999999999999999999999999
    for j in range(len(unsorted)):
        if s_value > unsorted[j]:
            s_value = unsorted[j]
            s_index = j
    lst.append(s_value)
    unsorted.pop(s_index)
    
    
    
    
    
    
    
    
    
    
    
    
    
print(lst)