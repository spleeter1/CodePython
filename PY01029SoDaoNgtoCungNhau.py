import math
for i in range(int(input())):
    n = input()
    n2 = n[::-1]
    res = math.gcd(int(n),int(n2))
    print("YES") if res== 1 else print("NO")
