import math
n = int(input())
a = []*n
a = [int(i) for i in input().split()]
a.sort()
for i in range (0,n):
    for j in range(i+1,n):
        if math.gcd(a[i],a[j]) == 1:
            print(a[i], " ",a[j])