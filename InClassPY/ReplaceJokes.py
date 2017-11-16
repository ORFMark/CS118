f=open("TextStuff\JokesPC.txt",'r')
jokes=f.readlines()
repabale=[]
for j in jokes:
    if j=="Your answer here\n":
        repabale.append(j)
repabale[0]='The Living Room\n'
repabale[1]='Ice Scream\n'
repabale[2]='He was allergic to nuts\n'
repabale[3]='He was too wrapped up in himself\n'
for i in range(1,len(jokes),2):
    if jokes[i]=='Your answer here\n':
        jokes[i]=repabale.pop(0)
f.close()
f=open("TextStuff\JokesPC.txt",'w')
f.writelines(jokes)
f.close()

