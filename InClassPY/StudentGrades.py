student_grades={}
for i in range(0,5):
    name=input("What is the students name?")
    grade=input("What is the student's grade? ")
    student_grades[name.lower()]=grade
    student_grades[name]=grade
print(student_grades)
continueLoop=True
while continueLoop==True:
    key=input("Enter a Name")
    print(student_grades.get(key, "Name not in list"))
    z=input("Would you like to find more grades?[Y/N]")
    if z=='N' or z=='n':
        continueLoop=False
        print("Have a nice day!")
    elif z=='Y' or z=='y':
        continueLoop=True
        
