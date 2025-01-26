def is_hamming_number(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5
    if n == 1:
        return True
    else:
        return False

a = []
for i in range(10000):
    if is_hamming_number(i):
        a.append(i)

c = int(input())
for i in range(c):
    n = int(input())
    if n in a:
        print(a.index(n)+1)
    else:
        print ("Not in sequence")