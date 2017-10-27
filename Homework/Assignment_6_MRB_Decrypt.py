scrambleLine=[]
lineCrypt=[]
lineClear=[]
Order=[]
f=open('H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\Key.txt','r') ##opens and copies the key
stringKey=f.readline()
stringKeyList=list(stringKey)
stringKeyList.pop()
stringKey=''.join(stringKeyList)
lineOrder=f.readline()
f.close()
f=open('H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\encrypted.txt','r') #opens the scrambled file and reads it
i=f.readline()
while i != '':
    scrambleLine.append(i)
    i=f.readline()
f.close()
f=open("H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\Decrypt.txt",'w+')
for i in range(0,len(lineOrder)): ##puts the lines back in the right order
    Order.append(int(lineOrder[i]))
for i in Order:
    lineCrypt.append(scrambleLine[i]) 
for i in range (0,len(lineCrypt)): ##unscrambles the lines
    for j in lineCrypt[i]:
        if j.isalpha()==False:
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
