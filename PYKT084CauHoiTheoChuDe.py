n= int(input())
a = []
s = ''
cnt = 0
ans = []
for i in range (n):
    s = input()
    if s == '' or i == n-1 :
        if i == n - 1:
            cnt+=1
        ans.append((a[0],cnt-1))
        cnt = 0
        a.clear()
    else:
        a.append(s)
        cnt+=1

for j in range(len(ans)):
    print(ans[j][0] +": "+str(ans[j][1]))
