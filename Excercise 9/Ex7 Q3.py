#Author:Aaron Mclynn
#Date:16/10/25
#Desc:Ex9 Q3:If use enters first letter as aVowel it adds "way" to end of string,if user enter first letter as a Consonant, it moves first letter to end and adds on "ay" at end
W = input('Enter Word')
if (W[0] == 'a'or W[0] =='e' or W[0] =='i'or W[0] =='o'or W[0]== 'u'):
    print(W+"way")
else:
    Newword = ""
    for i in range (1,len(W)):
        Newword=Newword+W[i]
    Newword =Newword+W[0]
    Newword =Newword+"ay"
    print(Newword)
