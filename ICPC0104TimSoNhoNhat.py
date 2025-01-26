for _ in range(int(input())):
    s = input()
    a = []
    res = ""
    for i in range(len(s)):
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            res+=s[i]
        else:
            if res != "":
                a.append(int(res))
                res = ""
    if res != "":
        a.append(int(res))
    a.sort()
    print(a[0])