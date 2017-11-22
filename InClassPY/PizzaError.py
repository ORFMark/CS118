print("There are 6 slices of Pizza")
people=(input("How many people want to split the pizza?"))

try:
    if int(people)<0:
        raise TypeError("Negative People")
    slices=6/int(people)
    print("Each person gets ", slices ," peices of pizza")
except ZeroDivisionError:
    print("You have noone to share the pizza with, how sad")
except ValueError:
    print("Exception: Can only divide by ints")
except TypeError:
    print("How did you get a negative amount of people")
except:
    print("Cannot handle, please try again")

    
