#This is the 5th assignment from Mark Burrell, and who knows if anything runs
print("HW5_MRB_10_03_17")
#Problem one, which is to find the minimum value of a list, and it runs
print("1.\n")
def min(*inputs):
    """finds the alphanumeric minimum of a group of values"""
    minimum=inputs[0]
    for x in inputs:
        if x<minimum: #this statment will always set minimum to the lowest x value currently found
            minimum=x
    return minimum
print(min(4,7,5))
print(min(-2,-6,-100))
print(min('Z','A','B'))

#problem 2, whicj will in theroy print boxes of various sizes, and runs
print("\n2.\n") 
def box(height, width):
    """prints a box of * with the specified height and witdth"""
    sideList=[]
    for i in range(0,width):
        sideList.append('*')
    side="".join(sideList)
    for i in range(0,height):
        print(side)
box(7,5)
print()
box(3,2)
print()
box(3,10)

#problem 3, this is to print the location of a number in a random list, and runs
print("\n3.\n")
##begin list creation
import random
userList=[]
for i in range (0,100):
    userList.append(i)
random.shuffle(userList)

##end list creation
def posFinder(usrlist, key): ##function that will find a value in a list and return the position
    """Finds the position of the key in a list"""
    found=False
    for i in usrlist:
        if userList[i]==key:
            print("found ", key ," in the list at positon ", i , ".")
            found=True
    if found==False:
        print("The key was not found in the list.")
posFinder(userList, 10)
posFinder(userList, 31)
posFinder(userList, 93)

##This will take an input string and say how many times a word has been repeated, and does
print("\n4\n") 
def repeatCheck(string):
    """Takes a string and returns the number of times a word is repeated"""
    #begin init of function variables
    stringLower=string.lower()
    stringList=list(stringLower)
    stringList.insert(0,' ')
    stringList.append(' ')
    spaceList=[]
    wordList=[]
    charList=[]
    repeat=0
   #print(stringList)
    #end variable create
    for m in range (0, len(stringList)): #finds and notes all the spaces
        if stringList[m]==' ':
            spaceList.append(m)
    t=len(spaceList)
  #  print(t,spaceList)
    for i in range(0,t):
        start=spaceList[0] ##uses the spaces to find words and add them to a list
        if len(spaceList) != 1:
            end=spaceList[1]
        else:
            end=None
        charList=stringList[start+1:end]
     #   print(charList)
        for m in charList: ##removes non alpha-numeric characters
            if m.isalpha() == False:
                charList.remove(m)
            #    print("removing non-alphaCharacter")
        spaceList.pop(0)
        wordList.append("".join(charList))
    #    print(wordList)
    for i in wordList: ##determines if words are repeated
        for j in wordList:
            if i==j:
                repeat+=1
        if repeat != 1:
     #       print(wordList)
            print("'",i,"'", " is repeated", repeat-1, "time(s), ", end="")
            for k in range (repeat-1): ##removes already found words to prevent duplicates
                wordList.remove(i)
        repeat=0
repeatCheck(input("Please input a sentence "))
#This is a program a program that will take an unknown imput of numbers and print them in ascending order
print("\n5.\n")

def numberSort(*numbList):
    if len(numbList)==1 and type(numbList[0])==list:
        numbList=numbList[0]
    return sorted(numbList)
print(numberSort(1,4,5,4,1,435,123,324,325))
print(numberSort(userList))
