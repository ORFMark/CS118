def tempConvert(tempType, value):
    TempF=0
    TempC=0
    TempK=0
    if tempType=='K':
        tempC=-273.15+value
        tempF=(tempC*(9/5))+32
        tempK=value
    elif tempType=='C':
        tempC=value
        tempF=(tempC*(9/5))+32
        tempK=value-273.15
    else:
        tempC=5*((value-32)/9)
        tempF=value
        tempK=tempC-273.15
    print("The Temperature in F is ", tempF , ", the Temperature in C is ", tempC ,", and the Temperature in K is ", tempK, ".")
tempSys=input("What system is your current temperature in? (F,K,C) ")
tempVal=input("And what is the value in that system? (dont include degree symbol) ")
tempConvert(tempSys, int(tempVal))

    
