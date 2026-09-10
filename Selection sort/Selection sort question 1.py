#Author:Aaron Mclynn
#Date:9/9/26
#Desc:Selection sort
lst = [7,67,2,9,36]


for i in range (len(lst)):
    current_min = i
    
    for j in range (i+1,len(lst)):
        if lst[j] < lst[current_min]:
            previous = lst[current_min]
            lst.insert(i,lst[j])
            lst.pop(i+1)
            lst.insert(j,previous)
            lst.pop(j+1)
            
print(lst) 
            
        


