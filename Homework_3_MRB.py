import time
#This si the looping assignment for Mark Burrell, and everything runs
print("This is CS118 assignment 3 for Mark Burrell, and everything runs")
#This block of code will theroretically print 0 to 9 10 times
#This runs
print("1.\n")
numList=[]
for x in range (0,10):  ##Creates the list of Numbers and converts it to a string
    numList.append(str(x)) 
numJoin=" ".join(numList)
for y in range (0,10): ##Prints the joined string 10 times
    print(numJoin)

#This block of code will print n, n+1, and so on
#This runs
numList2=[]
print("\n2.\n")
for k in range (0,10):
    numList2.append(str(k))
    numJoin2 = " ".join(numList2)
    print(numJoin2)

#This bock of code starts with 0-9 and ends with 0
#this runs
print("\n3.\n")
numList3=[]
for l in range (0,10):
    numList3.append(str(l)) ##Creates the List
for m in range (0,10): ##print loop
    if m == 0: ##ceates the special first case
        numJoin3=" ".join(numList3)
        print(numJoin3)
        continue
    else: ## prints the desent on new lines
        numList3.pop()
        numList3.insert(0," ")
        numJoin3=" ".join(numList3)
        print(numJoin3)
#This will theoretically run 0-->9 times its positon in the list
print("\n4.\n")
#This block runs but gets the spacing wrong
##iterList=[0,1,2,3,4,5,6,7,8,9]
##multList=[]
##for d in range (0,10):
##    multList=[]
##    for j in range (0,10):
##        multList.append(str(iterList[j]*d))
##    printMult=" ".join(multList)
##    print(printMult)

##This block runs and gets the spacing right
iterList=[0,1,2,3,4,5,6,7,8,9]
multList=[]
for d in range (0,10):
    multList=[]
    for j in range (0,10):
        if iterList[d]*j <10:
            multList.append(str((iterList[d]*j)) + "  ");
        else:
            multList.append(str(iterList[d]*j) + " ")
    multJoin="".join(multList)
    print(multJoin)
    
print("\n5.\n")
#This block will in theory print a prymid starting at 1, next line is 1,2,1 and so on
#This Runs
numbList=[]
for x in range (1,10):
    numbList.append(x) ##adds plus one each iteration
    printList=[]
    L = len(numbList)
    for y in range(0,L): ##adds the numbers
        printList.append(str(numbList[y]))
    P=len(printList)
    if P != 1:
        for z in range ((L-2),-1,-1): ##adds the desent on the sides
            printList.append(str(numbList[z]))
    for q in range ((9-P),0,-1): ##adds spaces
        printList.insert(0, " ")
    
    print(" ".join(printList)) ##converts the list into one string and prints it
    printList.clear()
#This block will 3 quarters of a rombus rotating counter-clockwise
#who knows if this runs
print("\n6.\n")
numbList.clear()
for X in range (1,10): ##copypaste of code above to generate top half of the rombus
    numbList.append(X)
    printList=[]
    L = len(numbList)
    for Y in range(0,L):
        printList.append(str(numbList[Y]))
    P=len(printList)
    if P != 1:
        for Z in range ((L-2),-1,-1):
            printList.append(str(numbList[Z]))
    for Q in range ((9-P),0,-1):
        printList.insert(0, " ")
    
    print(" ".join(printList)) 
    printList.clear()
for U in range (0,9): 
    catch=numbList.pop(); ##removes the last number of the list
    L = len(numbList)
    for W in range(0,L): ##sets up the print list with the numbers for the first quarter while excluding the second
        printList.append(str(numbList[W]))
    P = len(printList)
    for Q in range (0,9-P): ##adds spaces to set up spacing in the rombus
        printList.insert(0, " ")
    print(" ".join(printList)) 
    printList.clear()
    
