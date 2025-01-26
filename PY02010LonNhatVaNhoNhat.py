
while(True):
    n = int(input())
    if n==0:
        break
    a = []*n
    for i in range(0,n):
        a.append(int(input()))
    a.sort()
    if a[0] == a[n-1]:
        print("BANG NHAU")
    else:
        print(a[0],a[n-1])

