Q='Y'
def strReverse(usrName):
    m=int((len(usrName)-1))
    while 0<=m:
        print(usrName[m], end="")
        m=m-1
while Q == 'Y' or Q=="y":
   name=input("What str do you want to invert? ")
   strReverse(name)
   Q=input("\nDo you want to input another String? (Y/N): ")
print("Have a nice day!")    

          
