line="   "
qList=[]
aList=[]
jList=[]
repeated=0
def repeatCheck(string,key):
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
                #print("removing non-alphaCharacter")
        spaceList.pop(0)
        wordList.append("".join(charList))
    for j in wordList:
        if key==j:
            print(j,key)
            repeat+=1
    return repeat
f=open("Text Stuff\JokesHW.txt",'a')
f.write("What is the most annoying kind of ghost?\n")
f.write("Your answer here\n")
f.close()
f=open("Text Stuff\\JokesHW.txt",'r')
qsList=f.readlines()
for i in range(0,len(qsList),2):
    qList.append(qsList[i])
print(qList)
f.close()
g=open("Text Stuff\\answers.txt",'a')
g.write(input("What is the most annoying kind of ghost?")+'\n')
g.close()
g=open("Text Stuff\\answers.txt",'r')
line=" "
aList=g.readlines()
  
print(len(qList),len(aList))
for i in range(0,len(aList)):
    jList.append(qList[i])
    jList.append(aList[i])
g.close()
h=open("Text Stuff\JokesAns.txt",'w+')
h.writelines(jList)
print(jList)
for n in jList:
    print(n)
    repeated=repeated+repeatCheck(n,"ghost")+repeatCheck(n,"ghosts")+repeatCheck(n,"ghosts")
print("Ghost is repeated ",repeated,"times.")
h.close()
