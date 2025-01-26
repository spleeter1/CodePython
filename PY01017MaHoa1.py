t = input()
for i in range(0,int(t)):
    s = input()
    cnt=1
    res = ""
    ok=0
    for j in range (1,len(s)):
        if s[j-1] != s[j] :
                res =res + str(cnt) +s[j-1]
                cnt=1
                ok=1
        else:
            cnt+=1
            ok =0
    if ok == 0:
        res=res+str(cnt)+s[len(s)-1]
    else:
        res=res+"1"+s[len(s)-1]
    print(res)