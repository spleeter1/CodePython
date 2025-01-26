s1 = input().strip()
s2 = input().strip()
n = int(input())
res = ""
# for i in range(0,n-1):
#     res += s1[i]+ " "
res +=s1[:n-1]
# for i in range(0,len(s2)):
res += s2
# res = res.strip()
# for i in range(n-1,len(s1)):
#     res+= s1[i]+" "
res+=s1[n-1:len(s1)]
print(res)
