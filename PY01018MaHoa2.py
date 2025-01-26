P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    tmp = input()
    if tmp == "0":
        break
    k,s = tmp.split()
    k=int(k)
    res = ''
    for i in s:
        j = P.find(i)
        res  += P[(j+k)%28]
    print(res[::-1])