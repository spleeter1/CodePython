import math
def kt(n):
    if n<=1:
        return False
    for i in range(2,n):
        if i>math.sqrt(n):
            return True
        if n%i == 0:
            return False
for i in range(int(input())):
    n = input()
    res = int(n[len(n)-3:])
    res2 = int(n[:3])
    print("YES") if kt(res)and kt(res2) else print("NO")
        