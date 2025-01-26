for i in range (int(input())):
    s = input()
    res = ""
    for i in range (len(s)):
        if i%2 == 1:
            tmp = int(s[i])
            for j in range(tmp):
                res+=s[i-1]
    print(res)