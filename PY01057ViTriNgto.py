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
        if nto(str(k)) :
            if nto(n[k]):
                continue
            else:
                ok=0
                break
        if nto(str(k))==0 :
            if nto(n[k]):
                ok=0
                break
    print("YES") if ok == 1 else print("NO")