tong = 0
for i in range(int(input())):
    n = int(input())
    for j in range(2,n+1):
        cnt = 0
        while n%j==0:
            n/=j
            tong+=j
print(tong)