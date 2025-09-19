#Author: Aaron Mclynn
#Date 3/9/25
#Desc:Ask User is it raining, if they answer yes ask, is it windy, if yes then respond, its too windy for an umbrella, if no, take an umbrella, and if they dont answer first question, say have a nice day.
rain =input('is it raining?')
if (rain=='yes' or rain=='YES'):
    wind = input('is it windy?')
    
    if  (wind=='yes' or wind=='YES'):
        print('it is too windy for an umbrella')
    else:print('Take an umbrella')
else:print('Have a nice day')


    

    


