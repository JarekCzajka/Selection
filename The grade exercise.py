#Jaroslaw Czajka
#06.10.2014
#The-grade-Exercise

#This program will ask the user for their result marks and it will show their grade

print("This program will show you the grade you have achived in your exam")
grade=int(input("Please enter the amount of marks you have scored:"))
if grade <=81 and grade >=100:
    print("You have an A")
elif grade <=71 or grade ==80:
    print("You have a B")
