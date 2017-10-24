print("Hello World")
import math
number=225
print("The square root of ", number, " is ", math.sqrt(number))
import random
value = random.randint(1,6)
print("The dice rolled a ", value)
def weight(planet,weight):
    if planet=="Earth":
        return weight;
    elif planet == "Meurcury":
        return (weight*0.378);
    elif planet=="Luna":
        return  weight*0.166;
    elif planet=="Jupiter":
        return  weight * 2.364;
    elif planet == 'Venus':
        return (weight*0.907);
    elif planet=="Uranus":
        return (weight*0.889);
    else:
        return 0;
usrWeight=int(input("How much does an object weight (input a number): "))
usrPlanet=input("What planet do you want to be on? ")
print("Your object weighs ", weight(usrPlanet,usrWeight), " on ", usrPlanet)
              
