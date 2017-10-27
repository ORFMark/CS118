## This is the encryption side of assignment 6 for Mark Burrell, And who knows if it runs
import random
f=open("H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\Test.txt",'r')
lineList=[]
I=f.readline()
while I != '':
    lineList.append(I)
    I=f.readline()
f.close()
f=open('H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\encrypted.txt','w+')
alphaList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
deltaList=alphaList.copy()
keyList=[]
cryptlist=[]
random.shuffle(alphaList)
random.shuffle(deltaList)
for i in range(0,len(alphaList)):
    keyList.append(alphaList[i])
    keyList.append(deltaList[i])
print(keyList)
for i in range (0,len(lineList)):
    text=lineList[i]
    for j in range (0,len(text)):
        if text[j].isalpha()==False:
            if text[j]!='\n':
                cryptlist.append(text[j])
        else:
            for k in range (0,len(alphaList)):
                if text[j]==alphaList[k]:
                   cryptlist.append(deltaList[k])
    print(cryptlist)        
    crypt=''.join(cryptlist)
    f.write(crypt)
    f.write('\n')
    cryptlist.clear()
f.close()
f1=open('H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\Key.txt','w+')
key=''.join(keyList)
print(key)
f1.write(key)
f1.close()
    



