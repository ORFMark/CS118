print("This is the homework for the Second week of Class from Mark Burrell, and Everything runs")
import time
import sys
#This Runs!
#This is a program that prints the value of an amount of nickles and quarters
print("10.");
time.sleep(0.5);
q=input("How many quarters do you have? (Input as a number, ie 5) ");
q=int(q);
n=input("And how many nickles do you have? ")
n=int(n)
m=(.25*q)+(0.05*n);
print("You have $", m, " USD.");
#This runs
#This program tells if a number is postive or negative
print("11.");
time.sleep(0.5);
i=input("Pick a number between -100 and 100. ");
i=float(i);
if i==0:
    print("Your number is 0");
elif i<0:
    print("you have chosen a negative number.");
else:
    print("You Have chosen a positive number."); 
#This does run
#This program is supposed to take a list of numbers and sort them into postive and negative values
print("13.");
time.sleep(0.5);
print("Chose 7 numbers")
numberList=[]
numberList.append(float(input("First number: ")))
numberList.append(float(input("Second number: ")))
numberList.append(float(input("Third number: ")))
numberList.append(float(input("Forth number: ")))
numberList.append(float(input("Fifth number: ")))
numberList.append(float(input("Sixth number: ")))
numberList.append(float(input("Seventh number: ")))
positiveList=[]
negativeList=[]
zeroList=[]
counter = 0
counter = int(counter)
for counter in range (0,7):
    tester = numberList.pop()
    if tester==0:
        zeroList.append(tester);
    elif tester<0:
        negativeList.append(tester);
    else:
        positiveList.append(tester);
    counter=int(counter)
    counter+=1
print("you have", len(positiveList) , "postive numbers, ", len(zeroList) , " zeros, and ", len(negativeList) ," negative numbers")
#Who Knows if this runs
#This program prints the length of a string and the first letter
print("7, 6.6")
time.sleep(0.5);
usrStr=[]
usrStr = list(input("Please Type a word: "))
print("The word is " , len(usrStr) , " characters and the first character is " , usrStr.pop(0) , ".")
#This does run
#this a program for reversing a string
print("Bonus.");
time.sleep(0.5)
userStr=list(input("Write a sentence: "))
l=len(userStr)
revStr=[]
counter = 0
for counter in range (0,l):
    revStr.append(userStr.pop())
revString="".join(revStr);
print(revString)
time.sleep(3.0)
