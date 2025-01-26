for _ in range(0,int(input())):
    s = input()
    res=[]
    cnt=0
    tong = 0
    for i in range(0,len(s)):
        if ord(s[i]) >=48 and ord(s[i])<=57:
            tong+=int(s[i])
        else:
            res += s[i]
    res.sort()
    res = "".join(res) + str(tong)
    print(res)