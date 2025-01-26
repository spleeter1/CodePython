import math
def nto(n):
    n = int(n)
    if(n<2):
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1
for i in range(0,int(input())):
    n = input()
    ok=1
    for k in range(0,len(n)):
        if (k%2 !=0 and int(n[k])%2 == 1) or (k%2 !=1 and int(n[k])%2 == 0):
            continue
        else:
            ok=0
            break
    tong = 0
    for j in n:
        tong+=int(j)
    if nto(tong) and ok==1:
        print("YES")
    else:
        print("NO")