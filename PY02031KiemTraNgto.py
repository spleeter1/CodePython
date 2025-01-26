def ngto(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n%i == 0:
            return False
    return True

n,m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

#print(a)
for i in range(0,n):
    for j in range(m):
        if ngto(a[i][j]):
            print("1",end=" ")
        else:
            print("0",end=" ") 
    print()
