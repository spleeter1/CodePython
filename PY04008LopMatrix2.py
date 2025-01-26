for _ in range(int(input())):
    tmp = []
    while len(tmp)<2:
        tmp.extend(map(int,input().split()))
    n = tmp[0]
    m = tmp[1]
    while(len(tmp) <m*n):
        tmp.extend(map(int,input().split()))
    a = []
    dem =2
    for i in range(n):
        a.append(tmp[dem:dem+m])
        dem += m
    # print(a)
    trans = []
    for i in range(m):
        trans_row = []
        for j in range(n):
            trans_row.append(a[j][i])
        trans.append(trans_row)
    ans = []
    for i in range(n):
        ans.append([0] * n)
        for j in range(n):
            for k in range (m):
                ans[i][j] = ans[i][j] + a[i][k]*trans[k][j]
    for i in range(n):
        for j in range(n):
            print(ans[i][j],end=" ")
        print()