#Jaroslaw Czajka
#05-10-2014
#Selection-Class_Exercises_Development_Exercise-Task 4
 
#This porgram will show what grade the user has achived after entering a number
 
print("Welcome")
grade_achived=int(input("Please enter the amount of marks achived:"))
if grade_achived <=100 and grade_achived >=81:
    print("Your grade is A")
elif grade_achived  <=80 and grade_achived  >=71:
    print("Your grade is B")
elif grade_achived  <=70 and grade_achived  >=61:
    print("Your grade is C")
elif grade_achived  <=60 and grade_achived  >=51:
    print("Your grade is D")
elif grade_achived  <=50 and grade_achived  >=41:
    print("Your grade is E")
elif grade_achived  <=40 and grade_achived  >=0:
    print("Your grade is U")
else:
    print("Please enter a value between 0 and 100")
#The program has carried out the task
