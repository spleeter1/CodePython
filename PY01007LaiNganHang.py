for i in range(0,int(input())):
    # n = float(input())
    # x = float(input())
    # m = float(input())
    n, x, m = map(float, input().split())
    cnt=0
    while (n*pow((x/100+1),cnt) <= m):
        cnt+=1
    print(cnt)
