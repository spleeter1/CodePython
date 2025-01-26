kt = [1] * 1000005
for i in range(2, 1000005):
    if kt[i] == 1:
        for j in range(i * i, 1000005, i):
            kt[j] = 0

n = int(input())
a = [int(i) for i in input().split()]

check = [0] * 1005
b = []
for i in range(len(a)):
    if check[a[i]] == 0:
        b.append(a[i])
        check[a[i]] = 1

tong = sum(b)
ok = 0
for i in range(len(b)):
    tong1 = sum(b[:i+1])
    if kt[tong1] == 1 and kt[tong - tong1] == 1:
        print(i)
        ok = 1
        break
if ok == 0:
    print("NOT FOUND")