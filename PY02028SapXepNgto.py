kt = [1] * 1000005
for i in range(2, 1000005):
    if kt[i] == 1:
        for j in range(i * i, 1000005, i):
            kt[j] = 0
n = int(input())
a = [int(i) for i in input().split()]
b=[]
c=[]
for i in a:
    if kt[i] == 1:
        b.append(i)
b.sort()
j = 0
for i in a:
    if kt[i] == 1:
        c.append(b[j])
        j+=1
    else:
        c.append(i)
for i in c:
    print(i,end=" ")