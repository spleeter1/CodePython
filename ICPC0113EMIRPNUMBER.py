kt = [1] * 1000005
snt = []
for i in range(2, 1000005):
    if kt[i] == 1:
        for j in range(i * i, 1000005, i):
            kt[j] = 0

for _ in range(int(input())):
    n = int(input())
    for i in range (2,n):
        s1 = str(i)
        s2 = s1[::-1]
        if kt[i] == 1 and kt[int(s2)] and int(s1)<n and int(s2)<n and i<int(s2):
            print(i,int(s2),end=" ")
    print()
