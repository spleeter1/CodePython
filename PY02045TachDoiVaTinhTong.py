def calc(n):
    x = len(n)//2
    ans = int(n[:x])+int(n[x:])
    return ans

n = input()
while int(n)>=10:
    n = str(calc(n))
    print(n)