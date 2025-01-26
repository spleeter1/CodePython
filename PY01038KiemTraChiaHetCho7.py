for i in range(int(input())):
    n = input()
    cnt =0
    ans = int(n)
    while cnt<1000 and ans%7 !=0:
        ans = int(str(ans)[::-1] )+ans
        cnt+=1
    if cnt<1000:
        print(ans)
    else:
        print("-1")
