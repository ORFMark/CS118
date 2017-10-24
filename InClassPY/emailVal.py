fail="invalid email"
hacker="hackerEmail"
success="This is a valid Email"
print("When you are finished entering email addresses, type 'done'.")
cont="Yes"
while True:
    usrEmail=input("Please input an email address: ")
    if usrEmail == 'done':
        break
    elif usrEmail.find('@') == -1:
        print("Invalid email")
    elif len(usrEmail) <= 4 or usrEmail[-4] == None or usrEmail[-4] != '.':
        print(fail)
    elif usrEmail.startswith('@')==True:
        print(fail)
    elif usrEmail.find('@hacker.com') != -1:
        print(hacker)
    
    else:
        print(success)
print("Thank you for using Email Validator")
