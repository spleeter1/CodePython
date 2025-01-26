n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

x = abs(n-m)
ans = []
if n>m:
    i = 0
    dem = 0
    while i < n and dem < x:
        for j in range(0,m):
            a[i][j] = -1
        i+=2  
        dem += 1
elif(n<m):
    dem = 0
    for i in range(n):   
        j = 1
        dem = 0
        while j < m and dem < x:
            a[i][j] = -1
            j+=2
            dem+=1

for i in range(0,n):
    tmp = []
    for j in range(0,m):
        if a[i][j] != -1:
            tmp.append(a[i][j])
    if len(tmp) != 0:
        ans.append(tmp)

for i in range(len(ans)):
    for j in range(len(ans)):
        print(ans[i][j],end=" ")
    print()