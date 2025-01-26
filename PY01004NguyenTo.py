import math
def nto(n):
    if(n<2):
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1
        
for i in range(0,int(input())):
    n = int(input())
    k = 0
    for j in range(1,n):
        if math.gcd(n,j) == 1:
            k+=1
    if nto(k):
        print("YES")
    else:
        print("NO")