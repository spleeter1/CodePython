n = int(input())
check = [0]*n
a = []
while(len(a) < n):
    s = input()
    tmp = [int(x) for x in s.split()]
    a.extend(tmp)
a1 = []
a2 = []
for i in range(0,len(a)):
    if a[i]%2 == 1:
        check[i] = 1
        a1.append(a[i])
    else:
        a2.append(a[i])

a1.sort(reverse=True)
a2.sort()
j1 = 0
j2 = 0
for i in range(0,len(a)):
    if check[i] == 1:
        print(a1[j1],end=" ")
        j1+=1
    else:
        print(a2[j2],end=" ")
        j2+=1