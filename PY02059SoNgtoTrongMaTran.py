kt = [1] * 1005
kt[0] = 0
kt[1] = 0
for i in range (2,1005):
    if kt[i] == 1:
        for j in range(i*i,1005,i):
            kt[j] = 0

n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
positions = []
valmax = 1
for i in range(n):
    for j in range(m):
        if kt[a[i][j]] == 1:
            if a[i][j] > valmax:
                valmax = a[i][j]
                positions.clear()
                positions.append((i,j))
            elif a[i][j] == valmax:
                positions.append((i,j))

if valmax == 1:
    print("NOT FOUND")
else:
    print(valmax)
    # print(positions)
    for i in range(len(positions)):
        print("Vi tri ["+str(positions[i][0])+"]["+str(positions[i][1])+"]")