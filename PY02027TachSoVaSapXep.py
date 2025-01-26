n = int(input())
a = []
for _ in range(n):
    s = input()
    res = ""
    for i in range(0,len(s)):
        if(ord(s[i]) >= 48 and ord(s[i]) <= 57):
            res+=s[i]
        else:
            if res != "":
                a.append(int(res))
                res = ""
    if res != "":
        a.append(int(res))
        res = ""
a.sort()
for i in a:
    print(i)