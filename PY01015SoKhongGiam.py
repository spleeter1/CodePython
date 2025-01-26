for i in range (int(input())):
    s = input()
    j=1
    ok = 1
    while j<len(s):
        if int(s[j]) < int(s[j-1]):
            ok=0
            break
        j+=1
    if ok ==1:
        print("YES")
    else:
        print("NO")