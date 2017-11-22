name=input("What is your name? ")
age=input("How old are you? ")
try:
    if int(age)<0:
        raise TypeError("Cannot have negative age")
    drink=21-int(age)
    print(name, "will be able to drink in ",drink,"Years.")
except ValueError:
    print("Please input a number in numeric symbols")
except TypeError as e:
    print(e.args[0], "Excepting, please input positive values")
except BaseException as e:
    print(e.args[0])
