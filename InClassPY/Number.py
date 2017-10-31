f=open("TextStuff/NumberWrite.txt","w+")
for i in range (1,1001):
    f.write(str(i)+',')
    if str(i)[-1]==0:
        f.write("\n")
f.close()
