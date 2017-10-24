printList=[]
def recMult(n):
    global printList
    if n==1:
        printList.append(2)
        return 0
    else:
        printList.append(2*n)
        return 2*recMult(n-1)
recMult(4)
print(printList)
