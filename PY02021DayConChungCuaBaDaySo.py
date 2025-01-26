for _ in range(int(input())):
    n,m,k = list(map(int,input().split()))
    a = [int (i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int (i) for i in input().split()]
    i=j=h =0
    ans = [] 
    while i<len(a) and j <len(b) and h <len(c):
        if a[i] == b[j] == c[h]:
            ans.append(a[i])
            i+=1
            j+=1
            h+=1
        else:
            if a[i] <= b[j] and a[i] <= c[h]:
                i+=1
            elif b[j] <= a[i] and b[j]<= c[h]:
                j+=1
            else:
                h+=1
            
    if len(ans) == 0:
        print("NO")
    else:
        print(" ".join(str(i) for i in ans))