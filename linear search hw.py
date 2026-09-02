#Author:Aaron Mclynn
#Date:2/9/26
#Desc:Linear search question

lst = [7,15,4,30,17]
x = 30
answer = -1

for i in range (len(lst)):
    if lst[i] == x:
        answer = i
        break
    
if answer != -1:
    print ("found at;", answer)
else:
    print("-1")