import math
print("My name is Mark")
##This is an Example of a python Comment
print(2/3)
pi=math.pi
print(pi)

temperature = float(input("Temperature: "))
if temperature > 90:
    print("It is hot outside")

x=4
if x>=0:
    print("x is positive.")
else:
    print("X is not positive.")

answer = input("Who is Dr. Bunsen Honeydew's assistnat? ")
if answer == "Beaker":
    print("Correct!")
else:
    print("Incorrect, It is Beaker")

print("A cherry is a: ")
print("A: A dessert Topping")
print("B. A Desert Topping")
userInput = input("What is the Answer? (Input to letter) ")
if userInput == 'A':
    print("Correct")

x=int(input("Enter a number: "))
if x == 3:
    print("You entered 3")
else: 
    print("you did not enter 3")

x=input("How are you Today? ")
if x =="Happy" or "Glad":
    print("That is good to hear!")


x=5
y=x==6
z=x==5
print("x=",x)
print("y=",y)
print("z=",z)
if y:
    print("fizz")
if z:
    print("Buzz")

answer = bool(input("True or False, is 3+4 equal to 7"))
if answer:
	print("correct")
if answer == False:
	print("incorrect")
