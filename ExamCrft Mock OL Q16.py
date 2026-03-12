#Author: Aaron Mclynn
#Date: 12/3/26
#Desc: ExamCraft Mock OL Q16:
Total = 0
print("This program can find the perimeter or area of a quadllateral")
Name = input("Please Enter your name")
length = input("Enter Length")
width = input("Enter Width")
length = float(length)
width = float(width)
            
            
choice = input("Do you want to find the (p)erimeter or (a)rea ?")

if choice == "p":
    Total = (length*2) + (width*2)
    Total = round(Total,2)
    print("A quadrillateral with a length of ",length,"and a width of",width,"as a perimeter is:",Total)
elif choice == "a":
    Total = length*width
    Total = round(Total,2)
    print("A quadrillateral with a length of ",length,"and a width of",width,"as an area is:",Total)
print("Thank you for using the program", Name)
