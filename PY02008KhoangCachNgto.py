a = [1] * 10000
snt = []

for i in range(2, 10000):
    if a[i] == 1:
        for j in range(i * i, 10000, i):
            a[j] = 0

for i in range(2, 10000):
    if a[i] == 1:
        snt.append(i)

cnt = 0
n, x = map(int, input().split())
print(x, end=" ")
for i in range(n):
    x += snt[cnt]
    print(x, end=" ")
    cnt += 1