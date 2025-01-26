n = int(input())
a = []
for i in  range (0,n):
        a.append(list(map(int,input().split())))

tong1 = 0
tong2 = 0
for i in range(0,n):
    for j in range(i+1,n):
        tong1+=a[i][j]

for i in range(0,n):
    for j in range(0,i):
        tong2+=a[i][j]

k = int(input())
x = abs(tong1 - tong2)
if x > k:
    print("NO")
else:
    print("YES")

print(x)
