s = input()
cnt = [0]*100
a = []
for i in range(0,len(s),2):
    if i+2 > len(s):
        break
    n = int(s[i:i+2])
    a.append(n)
    cnt[n]+=1

k = int(input())
ok = 0
a.sort()
for i in a:
    if cnt[i] >=k:
        print(i,cnt[i])
        cnt[i] = 0
        ok = 1
if ok == 0:
    print("NOT FOUND")


