#Author:Aaron Mclynn
#Date:3/9/26
#Desc:Bubble sort algorithm Version 1
lst = [10,8,6,4,2]

for i in range (len(lst)):



    for i in range (0,len(lst) -1):
        if lst[i]>lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst [i+1] = temp

        
        
    

    print(lst)
