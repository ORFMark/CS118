Q='Y'
def strReverse(usrName):
    m=int((len(usrName)-1))
    wordRevList=[]
    while 0<=m:
        wordRevList.append(usrName[m])
        m=m-1
    wordRev="".join(wordRevList)
    return wordRev
def palindromeCheck(arg):
    lowArg=arg.lower()
    argList=list(lowArg)
    argListCopy=argList.copy()
    argListCopy2=argList.copy()
    for x in argList:
        if x.isalpha():
            print("keeping ", x)
        else:
            print("removing ", x)
            argListCopy.remove(x)
    argStrip="".join(argListCopy2)
    argRev=strReverse("".join(argListCopy))
    print(argStrip, " ", argRev)
    return argRev==argStrip
while Q == 'Y' or Q=="y":
    name=input("What str do you want to check for palindrome? ")
    if palindromeCheck(name) == True:
        print("This word is a Palindrome")
    elif palindromeCheck(name) == False:
        print("This is not a Palindrome")
    else:
        print("This word is not a word")
    while True:
        Q=input("\nDo you want to input another String? (Y/N): ")
        if Q=='N' or Q=='n' or Q=='Y' or Q=='y':
            break
        else:
            print("Please input Y or N")
    
print("Have a nice day!")    

          
