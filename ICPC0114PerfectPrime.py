import math
def ngto(n):
    if n<=1:
        return False
    x = math.sqrt(n)
    for i in range (2,n):
        if i > x:
            return True
        if n%i == 0:
            return False
    return True

for _ in range(int(input())):
    n = input()
    tmp = n[::-1]
    ok = 1
    tong = 0
    for i in range(len(n)):
        tong += int(n[i])
        if not ngto(int(n[i])):
            ok =0
    if ngto(int(n)) and ngto(int(tmp)) and ok!=0 and ngto(tong):
        print("Yes")
    else:
        print("No")