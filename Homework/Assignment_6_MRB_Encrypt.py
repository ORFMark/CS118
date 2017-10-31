## This is the encryption side of assignment 6 for Mark Burrell, And who knows if it runs
import random
f=open("Test.txt",'r') #Opens the cleartext file to read
lineList=[]
I=f.readline()
while I != '': ##creates the list of lines in the file
    lineList.append(I)
    print(I)
    I=f.readline()
f.close()
f=open('encrypted.txt','w+') #creates the file to write the encrypted infomation to
alphaList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0'] #creaation of scramble
deltaList=alphaList.copy()
keyList=[]
cryptlist=[]
orderList=[]
random.shuffle(alphaList)
random.shuffle(deltaList)
shuffleLine=lineList.copy()
random.shuffle(shuffleLine)
for i in lineList: ##shuffles the lines
    for z in range(0,len(lineList)):
        if i == shuffleLine[z]:
            if z>=10:
                m="'"+str(z)+"'"
                orderList.append(m)
            else:
                y=str(z)
                orderList.append(y)
for i in range(0,len(alphaList)): #key creation
    keyList.append(alphaList[i])
    keyList.append(deltaList[i])
    #print(alphaList[i], ' = ', deltaList[i])
for i in range (0,len(lineList)): #scrambles the file
    text=shuffleLine[i]
    for j in range (0,len(text)):
        if text[j].isalnum()==False:
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
f=open('Key.txt','w+') #write the key
key=''.join(keyList)
order=''.join(orderList)
f.write(key)
f.write('\n')
f.write(order)
f.close()
    



