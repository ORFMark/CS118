numList=[]
tot=0
f=open("TextStuff\Pizza.txt","w")
for i in range(5):
    x=input("How many days has it been since you ate pizza?")+"\n"
    f.write(x)
f.close()
f=open("TextStuff\Pizza.txt","r")
info=f.readlines()
for z in info:
    k=list(z)
    k.pop()
    y=''.join(k)
    x=int(y)
    numList.append(x)
min=numList[0]
max=numList[1]
for l in numList:
    tot=tot+l
    if max<l:
        max=l
    if min>l:
        min=l
average=tot/len(numList)
print("\nThe highest number of days is ",max,",The lowest number of days is ",min,",and the average is ",average,".")
f.close()
