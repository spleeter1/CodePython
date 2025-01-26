n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
positions = []
valmax = 0
ok = 0
for i in range(n):
    for j in range(m):
        x = a[i][j]
        if a[i][j] > valmax and str(x) == str(x)[::-1] and len(str(x))>1:
            ok = 1
            valmax = a[i][j]
            positions.clear()
            positions.append((i,j))
        elif a[i][j] == valmax:
            positions.append((i,j))

if ok == 0:
    print("NOT FOUND")
else:
    print(valmax)
    # print(positions)
    for i in range(len(positions)):
        print("Vi tri ["+str(positions[i][0])+"]["+str(positions[i][1])+"]")