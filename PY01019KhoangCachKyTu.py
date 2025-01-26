import math
t = input()
for j in range(0,int(t)):
    k = input()
    k2 = k[::-1]
    ok=1
    for i in range (1,len(k)):
        if abs(ord(k[i]) - ord(k[i-1])) != abs(ord(k2[i]) - ord(k2[i-1])):
            print("NO")
            ok=0
            break
    if ok==1:
        print("YES")
