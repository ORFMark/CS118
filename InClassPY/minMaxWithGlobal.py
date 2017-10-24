numbList=[]
for i in range (0,10):
    if i == 0:
        numbList.append(int(input("Please input an integer: ")))
    else:
        numbList.append(int(input("Please input another number")))
def minMax():
    global numbList
    return sorted(numbList)
print(minMax())

        
        
