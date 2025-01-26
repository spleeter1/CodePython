
for _ in range(0,int(input())):
    s = input()
    s2 = s[::-1]
    ok = 1
    for i in range(1,len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            ok=0
    print("NO") if ok == 0 else print("YES")