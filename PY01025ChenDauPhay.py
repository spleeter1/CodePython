n = input()
res=""
cnt=0
for i in range (len(n)-1,-1,-1):
    cnt+=1
    res = n[i]+res
    if cnt == 3:
        res = ","+res
        cnt=0
print(res[1:]) if res[0] ==',' else print(res)