## This is the encryption side of assignment 6 for Mark Burrell, And who knows if it runs
import random
f=open("H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\Test.txt",'r') #Opens the cleartext file to read
lineList=[]
I=f.readline()
while I != '': ##creates the list of lines in the file
    lineList.append(I)
    print(I)
    I=f.readline()
f.close()
f=open('H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\encrypted.txt','w+') #creates the file to write the encrypted infomation to
alphaList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #creaation of scramble
deltaList=alphaList.copy()
keyList=[]
cryptlist=[]
orderList=[]
random.shuffle(alphaList)
random.shuffle(deltaList)
shuffleLine=lineList.copy()
random.shuffle(shuffleLine)
print(shuffleLine)
for i in lineList: ##shuffles the lines
    for z in range(0,len(lineList)):
        if i == shuffleLine[z]:
            y=str(z)
            orderList.append(y)
for i in range(0,len(alphaList)): #key creation
    keyList.append(alphaList[i])
    keyList.append(deltaList[i])
    #print(alphaList[i], ' = ', deltaList[i])
for i in range (0,len(lineList)): #scrambles the file
    text=shuffleLine[i]
    for j in range (0,len(text)):
        if text[j].isalpha()==False:
            if text[j]!='\n':
                cryptlist.append(text[j])
               # print("found non-alpha character: ",text[j])
            #else:
               # print("found newline: ",str(text[j]))
        else:
            for k in range (0,len(alphaList)):
                if text[j]==alphaList[k]:
                   cryptlist.append(deltaList[k])        
    #print(cryptlist)
    crypt=''.join(cryptlist)
    #print(crypt)
    f.write(crypt)
    f.write('\n')
    cryptlist.clear()
f.close()
f=open('H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\Key.txt','w+') #write the key
key=''.join(keyList)
order=''.join(orderList)
f.write(key)
f.write('\n')
f.write(order)
f.close()
    



