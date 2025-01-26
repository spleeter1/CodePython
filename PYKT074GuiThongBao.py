def message(s):
    tmp = s.split()
    res = ''
    i = 0
    while i<99 and i < len(s):
        res += s[i]
        i+=1
    res = res.split()
    if res[len(res )-1] != tmp[len(res)-1]:
        res.pop(len(res)-1)
    print(" " .join(res))
n = int(input())
for i in range(n):
    s = input()
    message(s)
