f=open('TextStuff\limmerick.txt','w+')
for x in range(5):
    line=input("Enter Line"+str(x+1)+"of the limmerick:")
    f.write(line+"\n")
f.close()
