import re
regex=re.compile("ghost|Ghost")
count=0
f=open("TextStuff/JokesPC.txt",'r')
for line in f.readlines():
    if regex.search(line):
        count=count+1
f.close()
print("I found ghost",count,"times")
