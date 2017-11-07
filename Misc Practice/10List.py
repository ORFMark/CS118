global p
global s
p=0
tenList=[]
boo=False
while p<10**100:
    s=(1**p)+(2**p)+(3**p)+(4**p)
    t=list(str(s))
    if int(t[0])==1:
        t.pop(0)
        for i in t:
            i=int(i)
            if i != 0:
                boo=False
                p+=1
                break
            else:
                boo=True
    else:
        boo=False
        p+=1
        continue
    if boo==True:
            print("the first four ",p,"returns a power of 10")
            tenList.append(p)
    p+=1
    boo=False
    print(p)


        
            
        
