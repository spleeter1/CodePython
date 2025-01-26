for i in range (0,int(input())):
    s = input()
    strr =""
    a = s[:2]
    b = s[len(s)-2:]
    if a==b:
        print("YES")
    else:
        print("NO")