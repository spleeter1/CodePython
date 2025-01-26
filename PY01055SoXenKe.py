for i in range(0,int(input())):
    n = input()
    ok=1
    if len(n)%2 ==0 or n[0] == n[1]:
        ok=0
    tmp = n[0]
    for j in range (0,len(n),2):
        if n[j] != tmp:
            ok = 0
    if ok==1:
        print("YES") 
    else:
        print("NO")