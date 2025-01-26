n= int(input())
dic ={}
for i in range(n):
    res = ''
    s = input().lower()+' '
    for j in s:
        if (j >= 'a' and j <= 'z') : res+= j
        else:
            if res != '' :
                if res in dic:
                    dic [res] += 1
                else:
                    dic[res] = 1
                res = ''
dic = sorted(dic.items(),key = lambda x : (-x[1],x[0]))
# print(dic)
for i in dic:
        print(f"{i[0]} {i[1]}")
