a,k,n = map(int,input().split())
b = k - k*a//k 
arr = [-1]
while a+b<=n :
    if (b>0):
        arr.append(b)
    b+=k
if len(arr) > 1:
    for i in range(1,len(arr)):
        print(arr[i],end=" ")
else:
    print("-1")