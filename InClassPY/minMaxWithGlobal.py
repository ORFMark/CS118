numbList=[]
for i in range (0,10):
    if i == 0:
        numbList.append(int(input("Please input an integer: ")))
    else:
        numbList.append(int(input("Please input another number: ")))
def minMax():
    global numbList
    return sorted(numbList)
print(minMax())

def MinMax():
    global numbList
    printList=[]
    mini=numbList[0]
    l=len(numbList)
    for m in range(0,l):
        mini=numbList[0]
        for i in numbList:
            if i<mini:
                mini=i
        printList.append(mini)
        numbList.remove(mini)
    return(printList)
print(MinMax())
        
