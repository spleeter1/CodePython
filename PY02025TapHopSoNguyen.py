n,m = list(map(int,input().split()))
a = [int (i) for i in input().split()]
b = [int(i) for i in input().split()]
giao = sorted(set(a) & set(b))
t1 = sorted(set(a) - set(b))
t2 = sorted(set(b) - set(a))
print(" ".join(str(i) for i in giao))
print(" ".join(str(i) for i in t1))
print(" ".join(str(i) for i in t2))