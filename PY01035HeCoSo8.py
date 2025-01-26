n = input()
ans = ""
l = len(n)

if l%3!=0:
    n = "0"*(3 - l%3)+n

j = 2
res = 0
for i in range (0,len(n)):
    if n[i]=='1':
        res += 2**j
    j-=1
    if j == -1:
        ans+=str(res)
        j = 2
        res = 0
    
print(ans)
#print(n)