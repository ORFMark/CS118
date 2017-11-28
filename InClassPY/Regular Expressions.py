import re
regex=re.compile("[\n]")
count=0
f=open("TextStuff/JokesPC.txt",'r')
for line in f.readlines():
    count=count+1
    words=line.split(" ")
    for x in words:
        if regex.search(x):
            for z in x:
                if z.isalpha()==False:
                    x.strip(z)
            print("The last word of line",count,"is ",x,'.')
f.close()
