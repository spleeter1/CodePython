n = int(input())
a=[]
while len(a) < n:
    tmp = [int(i) for i in input().split()]
    a.extend(tmp)

ans = []
j = 0
for i in range(1,a[-1]+1):
    if i < a[j]:
        ans.append(i)
    elif i> a[j]:
        j+=1
        ans.append(i)
    else:
        j+=1
if len(ans) !=0:
    for i in range(0,len(ans)):
        print(ans[i])
else:
    print("Excellent!")
