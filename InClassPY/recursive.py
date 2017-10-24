printList=[]
def recMult(n):
    print(n)
    global printList
    if n==0:
        return 0
    else:
        return (2*n)+(recMult(n-1))
print(recMult(4))


def mult(n):
    numbList = []
    total=0
    while n >= 0:
        numbList.append(2*n)
        n=n-1
    numbList.append(0)
    for i in numbList:
        total=total+i
    return total
print(mult(4))
    
    
    
