import math
def nto(n):
    n = int(n)
    if(n<2):
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1
        
for i in range(0,int(input())):
    n = input()
    cnt=0
    for j in range(0,len(n)):
        if nto(n[j]) == 1:
            cnt+=1
           # print(n[j],end=" ")
    if cnt>len(n)-cnt and nto(len(n)) == 1:
        print("YES")
    else: 
        print("NO")