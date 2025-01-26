def solve():
    n = int(input())
    my_list = []

    for i in range(n):
        my_list.append([int(x) for x in input().split()])

    my_list.sort(key = lambda x : x[1])

    res, finish = 0, -1
    for x in my_list:
        if x[0] >= finish:
            res += 1
            finish = x[1]
    
    return res

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        print(solve())