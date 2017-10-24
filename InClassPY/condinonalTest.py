#conditonal test
age=input("Enter your Age: ")
age = int(age)
if age < 18:
    print("You cannot vote yet, please wait until you are 18.")
elif 18<=age<21:
    print("you can vote, but cannot yet drink")
elif 21<=age<56:
    print("You can vote, and drink, but not yet recive retierment benifits")
elif age>=56:
    print("you can vote, drink, and retire. Lucky you!")
else:
    print("Quantaum age unsupported, please try again")
