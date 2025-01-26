for i in range(0,int(input())):
    s1 = input()
    s1 = ''.join(sorted(s1))

    s2 = input() 
    s2 ="".join(sorted(s2))
    print("Test",str(i+1),end=": ")
    if s1 == s2:
        print("YES")
    else:
        print("NO")