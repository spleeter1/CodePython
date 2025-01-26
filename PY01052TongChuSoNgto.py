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
    tong = 0
    for j in n:
        tong+=int(j)
    if nto(tong):
        print("YES")
    else:
        print("NO")