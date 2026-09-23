

lst = [11,7,14,19,12]
for i in range(1,len(lst)):
    marker = lst[i]
    for j in range(i-1,-1,-1):
        if lst[j]<lst[i]:
            lst[i],lst[j] =lst[j],lst[i]
print(lst)
            
            
            
            
        
        
        