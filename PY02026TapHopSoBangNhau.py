n,m = map(int,input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a1 = sorted(set(a))
b1 = sorted(set(b))
if len(a1) == len(b1) and a1 == b1:
        print("YES")
else:
        print("NO")