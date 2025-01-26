for _ in range(int(input())):
    n,m = map(int,input().split())
    
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
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