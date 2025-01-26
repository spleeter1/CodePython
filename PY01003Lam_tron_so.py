import math
t = int(input())
while(t>0):
    n = input()
    tmp = int(n)
    length = len(n)
    a = pow(10,length-1)
    temp = int(n[0]) * a 
    res = abs(temp - tmp)
    if tmp < 10 and tmp !=5:
        print(tmp)
    else:
        if( tmp%10 == 5 or res >= a/2):
            print((int(n[0])+1)*a)
        else:
            print(temp)
    t-=1