import math
def snt(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

n = input()
for i in range (0,int(n)):
    a,b = map(int,input().split())
    c = math.gcd(a,b)
    tong = 0
    for i in (str(c)):
        tong+=int(i)
    if snt(tong):
        print("YES")
    else:
        print("NO")