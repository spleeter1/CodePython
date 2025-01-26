for i in range(int(input())):
    n = int(input())
    res = "1 * "
    for j in range(2,n+1):
        cnt = 0
        while n%j==0:
            n/=j
            cnt+=1
        if cnt!=0:
            res+= str(j)+"^"+str(cnt)+" * "
         
    print(res[:len(res) - 3])