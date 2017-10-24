inputList=[]
totalList=[]
for x in range (0,5):
    inputList.append(int(input("Please enter a positive number")))
    if totalList[x]<0:
        print("Sorry, negative numbers are not supported")
        break
    else:
        totalList.append(x)
        print(totalList.sum())
        
        
