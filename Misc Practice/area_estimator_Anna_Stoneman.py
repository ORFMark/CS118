#by Anna Stoneman

import math;
while True:
    eqn = input('type eqn: ');

    n = int(input("number of rectangles: "));
    area = 0;
    i = 0;
    d0 = eval(input("lower value of domain: "));
    d1 = eval(input("upper value of domain: "));
    r = input("right/left/midpoint(r/l/m): ");
    y = d1-d0; #domain
    z = y/n; #length of one rectangle

    if r == "r":
        while (d0 + (i*z)) < d1:
            i+=1;
            x = (i*z) + d0;
            area += eval(eqn);
    elif r =='l':
        while (d0 + (i*z)) < d1:
            x = (i*z) + d0;
            area += eval(eqn);
            i+=1;
    elif r == 'm':
        i = .5;
        while (d0 + (i*z)) < d1:
            x = (i*z) + d0;
            area += eval(eqn);
            i+=1;
    else:
        print("type legal stuff pls");
           
    area *= z;
    print ("estimated area under curve: ", area);
