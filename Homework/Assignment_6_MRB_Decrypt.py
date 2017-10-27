scrambleLine=[]
lineCrypt=[]
lineClear=[]
Order=[]
f=open('H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\Key.txt','r')
stringKey=f.readline()
lineOrder=f.readline()
f.close()
f=open('H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\encrypted.txt','r')
i=f.readline()
while i != '':
    scrambleLine.append(i)
    i=f.readline()
f.close()
f=open("H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\Decrypt.txt",'w+')
for i in range(0,len(lineOrder)):
    Order.append(int(lineOrder[i]))
for i in Order:
    lineCrypt.append(scrambleLine[i])
for i in range (0,len(lineCrypt)):
    for j in lineCrypt[i]:
        if j.isalpha()==False:
            lineClear.append(j)
            continue
        for m in range(1,len(stringKey),2):
            print(len(stringKey),",", m, ',', stringKey[m],",",stringKey[m+1])
            if stringKey[m]==j:
                lineClear.append(stringKey[m+1])
               ## print(stringKey[m+1], ' = ', j)
    line=''.join(lineClear)
    f.write(line)
    lineClear.clear()
    ##line=''.join(scrambleLine[i]
f.close()

