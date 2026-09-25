#to find the frequency
l=[4,5,9,10,14,16,18,24]
unique =[]
freq = []

#get a list of the unique values
for i in l:
    if i not in unique:
        unique.append(i)
        
for i in unique:
    freq.append(l.count(i))
    
print(unique)

print(freq)
        
        