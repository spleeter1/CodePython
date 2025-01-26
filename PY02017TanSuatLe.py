for _ in range(int(input())):
    n = int(input())
    a = []*n 
    cnt = [0]*100000
    a = [int(i) for i in input().split()]
    for i in a:
        cnt[i] +=1
    for i in range(0,len(cnt)):
        if cnt[i] %2 ==1:
            print(i)
            break