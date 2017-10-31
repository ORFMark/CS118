scrambleLine=[]
lineCrypt=[]
lineClear=[]
Order=[]
def posFinder(usrlist, key): ##function that will find a value in a list and return the position
    """Finds the position of the key in a list"""
    found=False
    for i in range (0,len(usrlist)):
        if usrlist[i]==key:
            found==True
            return i
    if found==False:
        return None

f=open('Key.txt','r') ##opens and copies the key
stringKey=f.readline()
stringKeyList=list(stringKey)
stringKeyList.pop()
stringKey=''.join(stringKeyList)
lineOrder=f.readline()
f.close()
f=open('encrypted.txt','r') #opens the scrambled file and reads it
i=f.readline()
while i != '':
    scrambleLine.append(i)
    i=f.readline()
f.close()
lineOrder=list(lineOrder)
f=open("Decrypt.txt",'w+')
t=0
while t < len(lineOrder): ##puts the lines back in the right order
    print(lineOrder[t])
    if lineOrder[t].isalnum()==True:
        Order.append(int(lineOrder[t]))
        t=t+1
        continue
    if lineOrder[t]=="'":
        lineTest=list(lineOrder[t:])
        for i in range len(lineTest):
            posList.append(posFinder(lineTest[i],"'")
            
        if "'" in lineTest and :
            if lineTest[0] != "'":
                pos=posFinder(lineTest,"'")
                multDig=lineTest[0]
            else:
                pos=posFinder(lineTest[1:],"'")
                multDig=lineTest[1]
            print("Pos= ",pos)
            for g in range(1,pos):
                multDig=multDig+lineTest[g]
            print(multDig)
            Order.append(int(multDig))
            t=t+pos+1
            lineTest=[]
            continue
        else:
            t=t+1
            continue
    else:
        t=t+1
        continue
print(Order)
for k in Order:
    lineCrypt.append(scrambleLine[k]) 
for i in range (0,len(lineCrypt)): ##unscrambles the lines
    for j in lineCrypt[i]:
        if j.isalnum()==False:
            lineClear.append(j)
            continue
        for m in range(1,len(stringKey),2):
            if stringKey[m]==j:
                lineClear.append(stringKey[m-1])
               ## print(stringKey[m+1], ' = ', j)
    line=''.join(lineClear)
    f.write(line)
    lineClear.clear()
    ##line=''.join(scrambleLine[i]
f.close()
print("done")
