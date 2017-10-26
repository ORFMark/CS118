def limwrite():
    f=open("H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\InClassPY\myPoem.txt",'w+')
    for i in range(1,6):
        limLine=input("input a line of your limerick")
        f.write(limLine)
        f.write("\n")
    f.close()
def limread():
    f=open("H:\ERAU_Year_1\Fall_Semester\CS118\GitHub2\InClassPY\myPoem.txt",'r')
    global poem
    poem=f.read()
    f.close()
limwrite()
limread()
print(poem)
