s = input()
cnt = [0]*100
a = []
for i in range(0,len(s),2):
    if i+2 > len(s):
        break
    n = int(s[i:i+2])
    a.append(n)
    cnt[n]+=1
a.sort()
for i in a:
    if cnt[i] != 0:
        print(i,end=" ")
        cnt[i] = 0