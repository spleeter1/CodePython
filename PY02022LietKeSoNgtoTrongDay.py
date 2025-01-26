kt = [1] * 1000005
snt = []
for i in range(2, 1000005):
    if kt[i] == 1:
        for j in range(i * i, 1000005, i):
            kt[j] = 0

n = int(input())
a = [int(i) for i in input().split()]
cnt = {}
for i in a:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1

for i in a:
    if kt[i] == 1 and cnt[i] != 0:
        print(i," ",cnt[i])
        cnt[i] = 0
