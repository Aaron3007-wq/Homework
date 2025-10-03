#Author:Aaron Mclynn
#Date:2/11/25
#Desc:Programming Exercise 6,Q2 Outputs average of users grades with there Result
G = 1 
total = 0
count = 0
while True:
    G = input('Enter Grade %')
    G = int(G)
    if G<0:
        break
    G = int(G)
    total += G
    count +=1
print('average is: ', total/count)
if (total/count>=90):
    print('This is an A')
    
elif (total/count<89 and total/count>80):
    print('This is a B')
    
elif (total/count<79 and total/count>70):
    print('This is a C')
    
elif (total/count<69 and total/count>60):
    print('This is a D')
    
elif (total/count<59):
    print('This is an F')

