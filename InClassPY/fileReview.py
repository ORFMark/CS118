def writeLimmerick():
    f=open("TextStuff\inClassReview.txt",'a+')
    for x in range(0,5):
        line=input("Please enter a line: ")
        f.write(line+"\n")
    f.close()
    print("done")

def readLimmerick():
    f=open("TextStuff\inClassReview.txt",'r')
    poem=f.readlines()
    for i in poem:
        print(i, end="")
    f.close()
writeLimmerick()
readLimmerick()
