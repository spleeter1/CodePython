for i in range(int(input())):
    n = int(input())
    if n%2==0:
        be=2
    else: be=1
    tong = 0.0
    for i in range (be,n+1,2):
        tong+=1/i
    print("{:.6f}".format(tong))
