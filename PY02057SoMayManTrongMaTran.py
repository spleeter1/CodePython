n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
positions = []
valmax = 0
valmin = 9999999
for i in range(n):
    for j in range(m):
        if a[i][j] > valmax:
            valmax = a[i][j]
        elif a[i][j] < valmin:
            valmin = a[i][j]
ans = valmax - valmin
ok = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == ans:
            ok = 1
            positions.append((i,j))
if ok == 0:
    print("NOT FOUND")
else:
    print(ans)
    # print(positions)
    for i in range(len(positions)):
        print("Vi tri ["+str(positions[i][0])+"]["+str(positions[i][1])+"]")

