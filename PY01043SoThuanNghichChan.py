def kt(n):
    if n != n[::-1] or len(n)%2 == 1:
        return False
    for i in n:
        if int(i)%2 == 1:    
            return False
    return True
if __name__ == "__main__":
    for j in range (int(input())):
        n = input()
        for i in range (22,int(n),2):
            if kt(str(i)):
                print(str(i),end=" ")
        print()

        