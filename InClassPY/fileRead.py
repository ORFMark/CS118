f=open("H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\InClassPY\myFile.txt",'r')
count=0
line=f.readline()
while line !='':
    print("Read: ",line)
    count+=1
    line=f.readline()
print("read",count," lines")
