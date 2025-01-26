n,m = map(int,input().split())
a = [int(i) for i in input().split()]
cnt = [0]*(m+1)
tmp = []

for i in range(0,len(a)):
    cnt[a[i]]+=1

ok = 0
for i in range(1,m):
    if cnt[a[i]] != cnt[a[i-1]]:
        ok =1
if ok == 0:
    print("NONE")
else:
    valmax  = max(cnt)
    smax2 = 0
    for i in cnt:
        if i < valmax and i >= smax2:
            smax2 = i
    for i in a:
        if cnt[i] == smax2:
            tmp.append(i)
    tmp.sort()
    print(tmp[0])